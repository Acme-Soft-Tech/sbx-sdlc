---
description: Stage 5 — open the two PRs, in the right order
argument-hint: <LINEAR-KEY>
---
Use `sbx-git-flow`.

1. Push both branches to the **forks**. PRs target `Acme-Soft-Tech/*:main`.
2. Both subjects carry `($1)`, and both bodies carry a magic word — `Part of $1` — so
   the link survives even where fork PRs confuse branch matching.
3. **Web PR merges first**; the new acceptance test rides in it marked `xfail`.
4. Request the code owner. You have no route to approve, and that is deliberate.
5. Write `sdlc/work/$1/links.md` with both PR URLs and the Linear issue.

## Update Linear

- Comment both PR URLs and which merges first.
- The team has no **In Review** state today, so the ticket stays **In Progress** and the
  comment carries the review status. Adding that state would make the queue visible at a
  glance — worth doing, but do not silently write a state that does not exist: that call
  fails and the ticket stops reflecting reality.
- On merge, comment the merge SHAs. Move to **Done** only once G4 is green against the
  deployed change — merged is not the same as working.
