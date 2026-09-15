---
description: Where every in-flight Linear key is in the six stages
---
For each directory under `sdlc/work/`, report which artifacts exist (`intent.md`,
`spec.md`, `plan.md`, `links.md`), which gate it is waiting on, and how long it has sat
there. Read `repos.yml` for the recorded submodule SHAs.

Then read the same keys from Linear and **report any disagreement between the two**.
The ledger and the ticket drifting apart is itself the finding: it means a stage
completed without writing to Linear, and from then on the ticket is fiction.

Show the ones **blocked on a human** first — that is where the queue actually is.
