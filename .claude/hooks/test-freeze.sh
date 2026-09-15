#!/usr/bin/env bash
# Stops the classic agent failure: making a red test green by editing the test.
# repos/ is read-only reference, never a workspace.
# Thin wrapper: the hook payload arrives on stdin, so the Python must be a
# real file. Feeding it as a heredoc silently consumes stdin and fails OPEN.
exec python3 "$(dirname "$(readlink -f "$0")")/test-freeze.py"
