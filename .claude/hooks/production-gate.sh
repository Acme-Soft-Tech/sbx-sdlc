#!/usr/bin/env bash
# A production deploy needs a named human authorisation. Its absence is the point.
# Thin wrapper: the hook payload arrives on stdin, so the Python must be a
# real file. Feeding it as a heredoc silently consumes stdin and fails OPEN.
exec python3 "$(dirname "$(readlink -f "$0")")/production-gate.py"
