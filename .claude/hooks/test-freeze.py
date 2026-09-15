#!/usr/bin/env python3
# Stops the classic agent failure: making a red test green by editing the test.
# repos/ is read-only reference, never a workspace.
import re, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _input import read, block

name, ti, cmd = read()
path = ti.get("file_path") or ti.get("notebook_path") or ""

TEST = re.compile(r'(^|/)(tests?|__tests__)/|(^|/)test_[^/]+\.py$|\.(test|spec)\.[jt]sx?$')

if name in ("Edit", "Write", "NotebookEdit") and TEST.search(path):
    if os.environ.get("SBX_ALLOW_TEST_EDIT") == "1":
        sys.exit(0)
    block(f"BLOCKED: edit to a test file.\n  {path}\n\n"
          "If a test is failing, the default assumption is that it is right and the\n"
          "source is wrong. Fix the source.\n\n"
          "A test legitimately needs changing when the spec changed. In that case say\n"
          "which line of the committed spec.md authorises it, and a human sets\n"
          "SBX_ALLOW_TEST_EDIT=1 for the session.")

# repos/ is read-only reference, never a workspace.
if name in ("Edit", "Write", "NotebookEdit") and re.search(r'(^|/)repos/', path):
    block(f"BLOCKED: write under repos/.\n  {path}\n\n"
          "Submodules here are read-only reference. scripts/sync.sh is the only thing\n"
          "that may move them. To change app code: scripts/work.sh <LINEAR-KEY>, which\n"
          "cuts a worktree from the fork clone.")
