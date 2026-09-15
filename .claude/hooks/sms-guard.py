#!/usr/bin/env python3
# The highest-value guard in the rig: in production the equivalent mistake
# texts real people. Blocks any pytest invocation that can reach the e2e marker.
# No -m at all means the whole suite, e2e included.
import re, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _input import read, block

name, ti, cmd = read()
if name != "Bash" or not re.search(r'\bpytest\b', cmd):
    sys.exit(0)
if os.environ.get("SBX_ALLOW_SMS") == "1":
    sys.exit(0)

m = re.search(r'-m\s+(["\']?)([^"\']+)\1', cmd)
expr = m.group(2) if m else None

# No -m at all means the whole suite, e2e included.
if expr is None or re.search(r'\be2e\b', expr):
    block("BLOCKED: this pytest run can reach the `e2e` marker, which sends SMS.\n"
          f"  marker expression: {expr or '<none — runs everything>'}\n"
          "In sbx-qa the e2e suite writes to sent_messages; in the real repo it texts\n"
          "real people, and the rest of the suite carries flaky(reruns=0) for that reason.\n\n"
          "Run the acceptance subset instead:\n"
          '  pytest -m "smoke or regression"\n\n'
          "If you genuinely need e2e, a human sets SBX_ALLOW_SMS=1 for that one command.")
