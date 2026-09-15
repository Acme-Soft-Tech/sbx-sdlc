#!/usr/bin/env bash
# Cut a worktree per repo from the FORK clones. Agents never edit under repos/ —
# those are read-only reference and a hook enforces it.
set -euo pipefail
# Ask Linear for the issue's branch name. Uses the API directly rather than MCP so
# this works in CI and in a plain shell, not only inside an agent session.
# Local credentials. A GitHub Actions secret is write-only — there is no read path,
# by design — so scripts running on a workstation need their own copy. Kept outside
# every repo so no .gitignore mistake can commit it.
SBX_ENV="${SBX_ENV:-$HOME/.config/sbx/linear.env}"
# shellcheck disable=SC1090
[ -f "$SBX_ENV" ] && { set -a; . "$SBX_ENV"; set +a; }

KEY="${1:?usage: work.sh <LINEAR-KEY>}"
cd "$(dirname "$(readlink -f "$0")")/.."
ROOT=$PWD

# The branch name MUST come from Linear, not from us. Linear matches branches and
# pull requests by this exact string — invent one and the issue never moves to
# In Progress, the PR never attaches, and the preview link never lands on the ticket.
# Every bit of the automation downstream keys off this.
branch="$("$ROOT/scripts/linear_sync.py" branch "$KEY")"
for name in sbx-web sbx-qa; do
  clone="$ROOT/../forks/$name"
  if [ ! -d "$clone" ]; then
    echo "missing fork clone: $clone"
    echo "  git clone git@github-sbx:sbx-alroy/$name.git $clone"
    echo "  git -C $clone remote add upstream git@github-sbx:Acme-Soft-Tech/$name.git"
    continue
  fi
  git -C "$clone" fetch upstream --quiet
  # Branches track upstream/main for rebasing, but pushes must go to the FORK.
  # Without this a plain `git push` targets upstream, whose push URL is no_push.
  git -C "$clone" config remote.pushDefault origin
  wt="$ROOT/.worktrees/$KEY/$name"
  mkdir -p "$(dirname "$wt")"
  git -C "$clone" worktree add -B "$branch" "$wt" upstream/main
  echo "worktree  $wt  ($branch off upstream/main)"
done
mkdir -p "$ROOT/sdlc/work/$KEY"
echo "ledger    sdlc/work/$KEY/"
