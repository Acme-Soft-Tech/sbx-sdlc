#!/usr/bin/env bash
# Blocks staging a .env or anything gitleaks flags in the staged diff.
# Broad stage (git add . / -A) — scan what would actually land.
# Thin wrapper: the hook payload arrives on stdin, so the Python must be a
# real file. Feeding it as a heredoc silently consumes stdin and fails OPEN.
exec python3 "$(dirname "$(readlink -f "$0")")/no-env.py"
