---
description: Stage 1 — pull a Linear issue and write sdlc/work/<KEY>/intent.md
argument-hint: <LINEAR-KEY>
---
Use the `sdlc-intent` skill.

1. Fetch `$1` over the Linear MCP connection (`mcp__linear-sbx__get_issue`).
2. Interview me about scope, affected surfaces, and what success looks like. Ask what
   the issue does not already answer — do not re-ask what it says.
3. Write `sdlc/work/$1/intent.md` from `sdlc/templates/intent.md`.
4. Commit on a branch and open a PR. **Merging it is gate G1** — do not start Stage 2.

## Update Linear — every stage ends here

Linear is the record. The GitHub integration reacts only to git events, and none of
the gates in this loop are git events, so each stage writes to the ticket itself.

- Move `$1` to **Todo** (it is specified, not yet being built).
- Comment: the intent PR link, the assumptions you raised, and what Stage 2 will do.

Prefer the MCP tools in an interactive session; `scripts/linear_sync.py` does the same
from a shell or CI. **If the update fails, say so and stop** — a ticket that silently
stops reflecting reality is worse than a loud failure, because everyone keeps trusting it.
