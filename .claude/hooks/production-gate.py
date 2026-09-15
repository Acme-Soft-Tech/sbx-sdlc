#!/usr/bin/env python3
# A production deploy needs a named human authorisation. Its absence is the point.
import re, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _input import read, block

name, ti, cmd = read()
if name != "Bash":
    sys.exit(0)

PROD = re.compile(r'(vercel\s+.*--prod|gh\s+workflow\s+run\s+deploy|'
                  r'wmill\s+sync\s+push.*prod|npm\s+run\s+deploy:prod)', re.I)
if not PROD.search(cmd):
    sys.exit(0)

who = os.environ.get("RELEASE_APPROVAL", "").strip()
if not who:
    block(("BLOCKED: production deploy with no named authorisation.\n\n"
          f"  command: {cmd.strip()[:160]}\n\n"
          "RELEASE_APPROVAL is unset. It must carry the name of the person who\n"
          "authorised this release, so the deploy log says who decided, not just who ran it:\n"
          "  RELEASE_APPROVAL='<name> <linear-key>' <command>\n\n"
          "This is gate G5. It is held by a person on purpose."))
print(f"[production-gate] release authorised by: {who}", file=sys.stderr)
