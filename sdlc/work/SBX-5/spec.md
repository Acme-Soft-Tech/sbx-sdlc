# SBX-5 — Spec

Reads: `intent.md` (merged 2026-09-15, G1 passed)

> Rig spec. Deliberately thin. The only section that must be rigorous is
> **Acceptance** — that is what G2 and G4 test. Product-quality questions are out of
> scope and noted, not argued.

## Design

`ProgressBar` rendered by `Onboarding`, above the active step. Takes `step` and `total`
as props. No counter of its own.

## DOM contract  *(the interface between the two repos)*

The only thing `sbx-qa` can see is the DOM, so it is pinned here rather than left to
whoever implements first:

    <div data-testid="progress" role="progressbar"
         data-step="{step}" aria-valuenow="{step}" aria-valuemin="1" aria-valuemax="{total}">

`data-testid="progress"` matches the selector convention every existing helper uses.

## Analytics

None. No new event, no `FUNNEL_STEP_MAP` change. Settled at G1.

## Acceptance   *(the part that matters)*

    sbx-web · src/ui/onboarding/__tests__/ProgressBar.test.tsx          [PR 1]
      new — required. The changed-file coverage gate fails any changed source file
      under 60%, so a new component with no test blocks its own PR.

    sbx-qa · wizard_helpers.py :: progress_step(page) -> int            [PR 2]
      new helper reading [data-testid="progress"] data-step.
      In wizard_helpers.py, NOT inlined per test — AGENTS.md requires it, and
      wizard_helpers.py is not matched by test-freeze.sh.

    sbx-qa · tests/test_Smoke_Class.py::TestSmoke::test_progress_bar_renders      [PR 2]
      marker: inherited from the class (@pytest.mark.smoke on TestSmoke) — nothing
      new to add at method level.
      asserts: [data-testid="progress"] is visible on first load.

    sbx-qa · tests/test_Regression_Class.py::TestRegression::test_progress_bar_tracks_step
      marker: inherited from the class.                                [PR 2]
      asserts: progress_step(page) == current_step(page) at step 1, and again after
               advancing. Uses drive_to_otp_step, which stops short of "Send code".

## Sequencing  *(corrected — the previous rule was impossible)*

**Two PRs, in two repos, strictly ordered. No `xfail` anywhere.**

1. **PR 1 — `sbx-web`**: component + unit test. Merge. Vercel deploys.
2. Confirm the deploy serves `[data-testid="progress"]`.
3. **PR 2 — `sbx-qa`**: helper + both tests. Merge.

The old rule said the QA test "lands xfail in the web PR". That is physically
impossible — a Python test cannot run in a repo with no pytest — and `xfail` has no
safe setting here: non-strict means the tests XPASS after deploy and silently assert
nothing forever; strict means the XPASS is a failure at 06:00, which auto-files a
Linear bug through `regression.yml`'s triage job. Ordering the two PRs removes the
mechanism entirely.

## test-freeze authorisation

`test-freeze.sh` blocks writes to `tests/`, `__tests__/` and `test_*.py`. The three
files above are **new tests this spec mandates**, not edits to a test that caught a bug.
This line is the authorisation the hook's message asks for; a human sets
`SBX_ALLOW_TEST_EDIT=1` for that session and says so in the PR.

## Flagged concerns

None that block. Visible "Step 2 of 4" text, aria semantics at the last step, and
styling tokens are product questions, **out of scope for the rig** — none makes a gate
more testable.

---
Gate G2 — accepted by: _pending_
