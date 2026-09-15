#!/usr/bin/env bash
# Point repos/ at local clones instead of carrying a second checkout of each.
set -euo pipefail
cd "$(dirname "$(readlink -f "$0")")/.."
SRC="${1:-$HOME/Codebase/sandbox/clones}"
for name in sbx-web sbx-qa sbx-api; do
  [ -d "$SRC/$name" ] || { echo "skip $name — not in $SRC"; continue; }
  ln -sfn "$SRC/$name" "repos/$name"
  echo "repos/$name -> $SRC/$name"
done
echo
echo "Symlinks are for local convenience only. CI uses real submodules, so the SHA"
echo "record stays honest."
