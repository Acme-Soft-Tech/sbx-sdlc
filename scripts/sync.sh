#!/usr/bin/env bash
# Nightly, and before any /work. Every sync commit is a dated record of which SHAs
# the lifecycle saw — that record is the audit trail the whole loop rests on.
set -euo pipefail
cd "$(dirname "$(readlink -f "$0")")/.."

if [ ! -f .gitmodules ]; then
  echo "no submodules yet — run scripts/link-local.sh or add them once the remotes exist"
  exit 0
fi

git submodule update --remote --merge
msg="chore(sync):"
for p in repos/*/; do
  [ -d "$p/.git" ] || [ -f "$p/.git" ] || continue
  msg="$msg $(basename "$p")@$(git -C "$p" rev-parse --short HEAD)"
done
if git diff --quiet; then echo "already at tip: ${msg#chore(sync): }"; exit 0; fi
git commit -am "$msg"
echo "$msg"
