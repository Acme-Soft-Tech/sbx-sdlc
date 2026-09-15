---
description: Stage 4 — run the acceptance subset against a preview URL
argument-hint: <LINEAR-KEY> <preview-url>
---
Delegate to the `qa-runner` subagent with `SBX_BASE_URL=$2`.

Never widen the marker expression past `smoke or regression`. This is gate G4.

## Update Linear

- Attach the preview URL to `$1` (`linear_sync.py link`). The native Vercel integration
  posts previews onto PRs, not tickets, so the ticket needs it written explicitly.
- Comment: pass/fail counts, the failing test ids, and trace artifact links.
- **Green after a red run** → move to **Done** if the PRs have merged; if they have not,
  say green and leave it in **In Review**.
- **Red** → the ticket goes back to **In Progress** and the comment names the failing
  assertion. Reopening is not a formality: a ticket marked Done over a red suite is how
  a regression escapes.
