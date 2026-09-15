---
description: Stage 3 — sync, cut worktrees in both fork clones, plan, then build
argument-hint: <LINEAR-KEY>
---
Use the `sdlc-plan` and `sbx-git-flow` skills.

1. `scripts/sync.sh` — record which SHAs this run saw.
2. `scripts/work.sh $1` — cuts a worktree per repo from the **fork** clones, on the
   branch name Linear gives. Never invent a branch name: Linear matches by that exact
   string, and it can change when workspace settings change.
3. Read `sdlc/work/$1/spec.md`. Write `sdlc/work/$1/plan.md` and commit it **before**
   any edit, so the record predates the diff.
4. Plan mode holds until I accept. Then build, with the hooks holding the lines.
5. Verify with the `verifier` subagent before you claim anything is done.

## Update Linear

- Move `$1` to **In Progress** and assign it.
- Comment: the branch name, both worktree paths, and the plan's two file lists.

This is the transition a branch push does NOT make on its own — verified: pushing a
correctly named branch to either the fork or the connected repo leaves the ticket in
Backlog. Only a PR event or a deliberate write moves it. So write it.
