#!/usr/bin/env bash
# The highest-value guard in the rig: in production the equivalent mistake
# texts real people. Blocks any pytest invocation that can reach the e2e marker.
# No -m at all means the whole suite, e2e included.
# Thin wrapper: the hook payload arrives on stdin, so the Python must be a
# real file. Feeding it as a heredoc silently consumes stdin and fails OPEN.
exec python3 "$(dirname "$(readlink -f "$0")")/sms-guard.py"
