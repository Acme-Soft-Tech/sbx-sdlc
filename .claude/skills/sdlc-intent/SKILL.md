---
name: sdlc-intent
description: Writing intent.md, the Stage 1 artifact. Use for /intent or whenever work enters the loop from Linear, a QA regression bug, or a monitoring band breach.
---

`intent.md` answers one question: **why does this change exist?** It is not a design and
not a plan. If it contains a file path, it has gone too far.

Pull the Linear issue over MCP, then interview the requester about scope, affected
surfaces and what success looks like. Write what they said, not what you would have said.
Flag what you could not get an answer to — an unanswered question here is much cheaper
than the same question at Stage 3.

Template: `sdlc/templates/intent.md`. Commit to `sdlc/work/<KEY>/intent.md`.
**Gate G1: the product owner merges it.** Nothing downstream starts until then.
