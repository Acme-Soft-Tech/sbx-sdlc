---
name: sdlc-plan
description: Writing plan.md, the Stage 3 artifact — two file lists, one per repo, and the risks. Use for /work.
---

Read `spec.md`. Produce a plan carrying **two file lists, one per repo**, plus the risks
you can see. Claude Code's plan mode is the gate enforcing itself: no file is edited
until a human accepts.

    ## sbx-web
    - src/ui/onboarding/ProgressBar.tsx        new
    - src/lib/analytics/events.ts              add EVENT + FUNNEL_STEP_MAP entry
    ## sbx-qa
    - tests/test_Regression_Class.py           add test, xfail until web deploys
    ## Risks
    - FUNNEL_STEP_MAP indices are load-bearing for six weeks of PostHog history

Once accepted, auto mode does the pass with the hooks holding the lines. Commit to
`sdlc/work/<KEY>/plan.md` **before** editing, so the record predates the diff.
