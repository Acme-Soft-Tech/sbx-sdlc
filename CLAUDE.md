# sbx-sdlc — how work moves here

You are in the orchestrator. It holds policy, templates, the work ledger and scripts.
**It never holds application code.**

## The loop

    Plan ──G1──> Design ──G2──> Build ──G3──> Test ──G4──> Deploy ──G5──> Maintain
    intent.md    spec.md        plan.md      green x2     2 PRs         bands.yaml
                                                                           │
                    a 3-sigma breach or a QA regression bug ────────────────┘
                    writes the next intent.md by itself

Every stage ends by committing a file; the next stage begins by **reading that file**.
Nothing is handed over in a chat window. If you find yourself re-explaining the ticket
at the build stage despite a committed `spec.md`, say so loudly — that is the single
outcome that falsifies this whole design.

## Linear is the record

Every stage writes to the ticket: a state change, a comment, or both. This is not
bookkeeping — it is the only place a non-engineer can see where work actually is.

The GitHub integration attaches PRs by itself, but it reacts only to git events, and
none of this loop's gates are git events. Verified on 2026-09-15: pushing a correctly
named branch to the fork AND to the connected repo left SBX-5 in Backlog both times.
Branch names matter for PR matching, not for status.

So each command writes deliberately, via the Linear MCP in session or
`scripts/linear_sync.py` from a shell or CI. **A failed Linear write stops the stage.**
A ticket that has quietly stopped reflecting reality is worse than one that is obviously
broken, because people keep trusting it.

Branch names come from Linear, never invented — and never cached. SBX-5's changed from
`alroydsouza/...` to `feature/...` the moment the GitHub integration was connected.

State mapping: Todo after G1, In Progress at Stage 3, **In Review** once both PRs are
open, Done only when G4 is green against the deployed change. Merged is not Done — a
ticket closed over a red acceptance suite is how a regression escapes.

## The work ledger

One directory per Linear key: `sdlc/work/<KEY>/` holding `intent.md`, `spec.md`,
`plan.md`, `links.md`. Templates are in `sdlc/templates/`.

## repos/ is read-only

The submodules under `repos/` are reference, not a workspace. `scripts/sync.sh` is the
only thing that may move them. A hook blocks every write tool under `repos/` — if you
need to change app code, cut a worktree with `scripts/work.sh <KEY>`, which works from
the **fork** clones, never from here.

## Gates

| Gate | Kind | Enforced by | Stops |
|---|---|---|---|
| G1 intent | human | PR merge in this repo | Building what nobody agreed was a problem |
| G2 spec+plan | human | plan mode, spec-reviewer | Code before the design argument is settled |
| branch | hook | `protect-branch.sh` | Commit on `main`, force push, `--no-verify` |
| secrets | hook | `no-env.sh` | `.env` reaching a commit |
| test integrity | hook | `test-freeze.sh` | Fixing a bug by editing the test that caught it |
| real SMS | hook | `sms-guard.sh` | Widening pytest markers into `e2e` |
| G3 code health | CI | eslint, unit tests | Merging under the coverage floor |
| G4 acceptance | CI | `qa-gate.yml` | Shipping a funnel change no test exercises |
| G5 review | human | branch protection, REVIEW.md | The agent that wrote the diff approving it |
| G5 release | human | `production-gate.sh` | A prod deploy with no named authorisation |
| config drift | CI | `agent-evals.yml` | A skill edit quietly degrading every agent |

A skill makes the right thing likely. A hook makes the wrong thing impossible.
Policy that must always hold gets both.

## Honest limits of this rig

- **Hooks are not a control against a person.** They are fast feedback that stops
  mistakes. Branch protection and required checks are the real, server-side controls.
- **Guard scripts pattern-match command text.** An agent that writes a shell script and
  runs it routes around them without intending to. That is why `sbx-api`'s SMS stub
  *also* refuses writes unless the job sets an env var — defence in depth.
- **The bands thresholds are unprovable here.** Near-zero traffic. Claim the trigger
  path works; never claim the thresholds are right.
