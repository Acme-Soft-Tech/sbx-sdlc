---
description: Stage 4 — run the acceptance subset against a preview URL
argument-hint: <preview-url>
---
Delegate to the `qa-runner` subagent with `SBX_BASE_URL=$1`.

Never widen the marker expression past `smoke or regression`. Report pass/fail counts,
failing test ids, and trace artifacts. This is gate G4.
