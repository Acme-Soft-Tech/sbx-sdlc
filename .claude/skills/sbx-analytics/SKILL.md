---
name: sbx-analytics
description: Analytics contract for sbx-web — EVENTS, EventPropertiesMap and FUNNEL_STEP_MAP. Use when adding a funnel step, a new event, or any capture call.
---

Three things move together. Changing one without the others is the most common
silent break in the funnel, because nothing fails — the data just goes wrong.

1. **`EVENTS`** — the event name constant. Never a string literal at the call site.
2. **`EventPropertiesMap`** — the typed properties for that event. A new event with no
   entry here is a type error, which is the point.
3. **`FUNNEL_STEP_MAP`** — step index to event. **Decoupled from UI state on purpose**:
   reordering the UI must not silently renumber the funnel, because the PostHog funnel
   is defined over these indices and six weeks of history depends on them.

## Rules

- Every step transition emits exactly one event. Not zero, not two.
- `session_id` on every event, client and server, so the two halves join.
- Never a PII property: no phone, email, full name, OTP value.
- Adding a step means adding to `FUNNEL_STEP_MAP` **and** naming the acceptance test in
  the spec's Acceptance section. A funnel change with no `@pytest.mark.regression`
  coverage fails G2 on the document, not in production.
