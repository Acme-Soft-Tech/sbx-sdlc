---
name: sbx-api-route
description: The six-step API route handler shape for sbx-web. Use when adding or editing any file under app/api/, or when a spec calls for a new endpoint.
---

Every handler in `app/api/**/route.ts` follows the same six steps, in this order.
Deviating is a review finding, not a style preference.

1. **Parse and validate** the body. Reject malformed input with 400 before anything else.
2. **Capture the attempt** — `captureServer(EVENTS.X_ATTEMPTED, { session_id, ... })`.
3. **Call upstream through `upstreamFetch`**, never a bare `fetch(`. It carries the
   timeout and retries *transport* failures only — never a 4xx/5xx, which are answers.
4. **Branch on the upstream result**, and emit analytics on **both** paths. The failure
   path is the one people forget and the one that matters in a funnel.
5. **`captureExceptionServer`** in the catch. Every catch, no exceptions.
6. **Return a generic message** on 500. Never leak upstream text to the client.

## Never

- No PII in a log line or an analytics property: no phone, email, name, or OTP value.
  `session_id` is the join key; that is what it is for.
- No bare `fetch(` inside `app/api`. Semgrep rule `sbx-no-bare-fetch` catches it.
- No upstream error text in a client-facing response body.

## Shape

```ts
export async function POST(req: Request) {
  const body = await req.json().catch(() => null)
  if (!body?.session_id) return Response.json({ error: 'Bad request' }, { status: 400 })
  await captureServer(EVENTS.OTP_REQUEST_ATTEMPTED, { session_id: body.session_id })
  try {
    const res = await upstreamFetch('/lead-dr-request-otp', { method: 'POST', body })
    if (!res.ok) {
      await captureServer(EVENTS.OTP_REQUEST_FAILED, { session_id: body.session_id, status: res.status })
      return Response.json({ error: 'Could not send code' }, { status: 502 })
    }
    await captureServer(EVENTS.OTP_REQUEST_SUCCEEDED, { session_id: body.session_id })
    return Response.json(await res.json())
  } catch (e) {
    await captureExceptionServer(e, { session_id: body.session_id })
    return Response.json({ error: 'Something went wrong' }, { status: 500 })
  }
}
```
