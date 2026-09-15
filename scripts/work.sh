#!/usr/bin/env bash
# Cut a worktree per repo from the FORK clones. Agents never edit under repos/ —
# those are read-only reference and a hook enforces it.
set -euo pipefail
KEY="${1:?usage: work.sh <LINEAR-KEY>}"
cd "$(dirname "$(readlink -f "$0")")/.."
ROOT=$PWD

branch="$(echo "$KEY" | tr '[:upper:]' '[:lower:]')-work"   # replace with Linear's name
for name in sbx-web sbx-qa; do
  clone="$ROOT/../forks/$name"
  if [ ! -d "$clone" ]; then
    echo "missing fork clone: $clone"
    echo "  git clone git@github-sbx:sbx-alroy/$name.git $clone"
    echo "  git -C $clone remote add upstream git@github-sbx:Acme-Soft-Tech/$name.git"
    continue
  fi
  git -C "$clone" fetch upstream --quiet
  wt="$ROOT/.worktrees/$KEY/$name"
  mkdir -p "$(dirname "$wt")"
  git -C "$clone" worktree add -B "$branch" "$wt" upstream/main
  echo "worktree  $wt  ($branch off upstream/main)"
done
mkdir -p "$ROOT/sdlc/work/$KEY"
echo "ledger    sdlc/work/$KEY/"
