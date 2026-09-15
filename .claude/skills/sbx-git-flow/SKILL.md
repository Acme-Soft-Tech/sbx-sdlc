---
name: sbx-git-flow
description: Fork workflow, branch naming and commit format for the sandbox repos. Use before any commit, branch, push or PR.
---

## Fork, never upstream

`Acme-Soft-Tech/*` is authoritative `main`. You commit from **`sbx-alroy/*`**, the fork,
and open PRs back to upstream. This mirrors relintex -> vspl-alroy exactly, and it is the
one thing every agent session touches, so it is the one thing the rig must test.

    origin    git@github-sbx:sbx-alroy/sbx-web.git      # yours, push here
    upstream  git@github-sbx:Acme-Soft-Tech/sbx-web.git  # theirs, PR here, never push

## Branch names

Take the branch name from the Linear issue. Never invent one.

## Commits

Conventional Commits, with the Linear key in the subject. The key is what makes the
whole audit chain work; `commitlint` enforces it.

    feat(onboarding): add progress bar to funnel (SBX-7)
    fix(api): emit analytics on the OTP failure path (SBX-9)

## Two repos, one change: web merges first

A change spanning `sbx-web` and `sbx-qa` is two PRs in two repos and nothing sequences
them. The rule: **web merges and deploys first, then the QA PR opens.**

    1. PR in sbx-web   -> merge -> Vercel deploys
    2. confirm the deploy actually serves the new DOM hook
    3. PR in sbx-qa    -> merge

**Do not put the acceptance test in the web PR marked `xfail`.** That instruction was
wrong and stood here for a day. It is impossible — `sbx-web` has no pytest, so a Python
test cannot run there — and `xfail` has no safe setting in this repo:

- non-strict (the default, `pytest.ini` sets no `xfail_strict`): after the deploy the
  test XPASSes, which reports green. Nothing forces anyone to flip it, so it can sit
  there asserting nothing indefinitely — the same silent-green failure mode as an unset
  `SBX_BASE_URL`.
- strict: the XPASS becomes a failure on the 06:00 scheduled run, whose triage job
  auto-files a Linear bug. It creates exactly the spurious red the rule claimed to avoid.

Ordering the PRs removes the mechanism instead of tuning it.

## Never

- No commit on `main`. No force push. No `--no-verify`. Hooks block all three.
- No `.env` staged, ever.
