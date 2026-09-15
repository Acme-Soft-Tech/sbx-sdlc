---
description: Stage 2 — read the intent and write the spec, including the Acceptance contract
argument-hint: <LINEAR-KEY>
---
Use the `sdlc-spec` skill.

1. Read `sdlc/work/$1/intent.md`. If it is not merged, stop — G1 has not passed.
2. Load `sbx-design-system`, `sbx-analytics`, `sbx-api-route`, `qa-test-authoring`.
3. Write `sdlc/work/$1/spec.md`, flagging every policy conflict rather than resolving it.
4. Run the `spec-reviewer` subagent and address what it finds.
5. Present it. **A human accepts — that is G2.**

## Update Linear

- Comment: the spec PR link, the **Acceptance** section verbatim (the markers and test
  classes this change needs), and every flagged concern.
- Leave the state alone until G2 passes. A spec under argument is not work in progress.
- Once accepted, comment that G2 passed and who accepted it.

The flagged concerns matter most here. If the spec raised a conflict and the ticket does
not show it, the next person reads a ticket that looks settled when it is not.
