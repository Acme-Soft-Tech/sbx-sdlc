# Findings

What the rig has actually demonstrated. Evidence, not argument.

## Gates

| Gate | Status | Evidence |
|---|---|---|
| G1 intent | **demonstrated** | direct push to main: `remote rejected — must be made through a pull request` |
| G2 spec | **demonstrated** | SBX-5's spec was sent back REWORK by `spec-reviewer` with 4 blocking process defects, before any code |
| G3 code health | **demonstrated** | lint, typecheck, coverage green in CI; changed-file gate caught DebtStep at 0% |
| G4 acceptance | **demonstrated** | 11 passed against the live preview; 3 failed against a wrong host; refuses to run with `SBX_BASE_URL` unset |
| G5 review | **demonstrated** | `Can not approve your own pull request`; every PR sat `BLOCKED / REVIEW_REQUIRED` |
| G6 triage | **pending** | planted bug armed for the 06:00 run |

## Probes

P1–P4, P6 pass against the hooks (17 assertions, `scripts/probe-hooks.sh`).
P5 passed live. P7 not yet run.

## Defects the rig found in itself

1. **All five hooks failed open.** Written as `python3 - <<'PY'`, so the heredoc consumed
   stdin and the payload never arrived. Every guard waved everything through while
   looking correct. Found by writing the probe suite, not by reading the code.
2. **`work.sh` invented branch names.** Linear matches by its own `branchName`; an
   invented one means no status change, no PR attachment, no preview link. The
   `sbx-git-flow` skill already forbade it — nothing enforced it.
3. **Branch names are not stable.** SBX-5's changed from `alroydsouza/...` to
   `feature/...` the moment the GitHub integration was connected. Anything cached breaks.
4. **Branch pushes do not move Linear issues.** Verified on the fork *and* the connected
   repo: SBX-5 stayed in Backlog both times. Status must be written deliberately.
5. **The cross-repo sequencing rule was impossible**, and stood in **six** files —
   `sbx-git-flow`, the spec template, `/ship`, `sdlc-spec`, `sdlc-plan`, and
   `spec-reviewer` itself. It said the acceptance test rides in the web PR marked
   `xfail`. `sbx-web` has no pytest. Worse, `xfail` has no safe setting here: non-strict
   XPASSes green forever, strict turns the 06:00 run red and auto-files a Linear bug.
6. **`test-freeze.sh` blocks the golden path.** Every acceptance artifact SBX-5 needs is
   a new test file, and the hook cannot distinguish "write a new test" from "edit the
   test that caught your bug". Mitigated by spec authorisation + `SBX_ALLOW_TEST_EDIT`;
   not solved.
7. **CI is not per-PR.** `regression.yml` uses `inputs.base_url || vars.SBX_BASE_URL`,
   and `inputs` exist only on `workflow_dispatch` — so on a pull request the suite runs
   against the shared URL, not that PR's preview. G4 is real but not yet per-PR.
8. **`qa-gate.yml` does not exist**, though `CLAUDE.md`'s gate table names it as G4's
   enforcer.
9. **Fork PRs require manual Vercel authorisation** every time. The fork workflow EvaFi
   depends on is what makes this friction, and it lands on a human per PR.

## Not demonstrated

- SBX-8's eval gate — no eval suite built yet.
- Whether a fork PR attaches to a Linear ticket.
- P7 (drive-by refactor of planted legacy).
