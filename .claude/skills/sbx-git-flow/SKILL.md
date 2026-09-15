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
them. The rule: **web merges first.** The new acceptance test lands in the *same web PR*
marked `xfail`, and a follow-up commit flips it once the deploy is live. Merging the QA
side first turns the scheduled suite red against behaviour that has not shipped.

## Never

- No commit on `main`. No force push. No `--no-verify`. Hooks block all three.
- No `.env` staged, ever.
