---
description: Stage 1 — pull a Linear issue and write sdlc/work/<KEY>/intent.md
argument-hint: <LINEAR-KEY>
---
Use the `sdlc-intent` skill.

1. Fetch `$1` over the Linear MCP connection (`mcp__linear-sbx__get_issue`).
2. Interview me about scope, affected surfaces, and what success looks like. Ask what
   the issue does not already answer — do not re-ask what it says.
3. Write `sdlc/work/$1/intent.md` from `sdlc/templates/intent.md`.
4. Commit it on a branch and open a PR. **Merging it is gate G1** — do not start Stage 2.
