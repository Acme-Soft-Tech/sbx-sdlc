#!/usr/bin/env bash
# Blocks: a commit while main/master is checked out, --no-verify, and force push.
# Thin wrapper: the hook payload arrives on stdin, so the Python must be a
# real file. Feeding it as a heredoc silently consumes stdin and fails OPEN.
exec python3 "$(dirname "$(readlink -f "$0")")/protect-branch.py"
