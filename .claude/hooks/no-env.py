#!/usr/bin/env python3
# Blocks staging a .env or anything gitleaks flags in the staged diff.
# Broad stage (git add . / -A) — scan what would actually land.
import re, shutil, subprocess, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _input import read, block

name, ti, cmd = read()
if name != "Bash":
    sys.exit(0)

if re.search(r'\bgit\s+add\b', cmd) and re.search(r'(^|[\s/"\'])\.env(\.|\b)', cmd):
    block("BLOCKED: that stages a .env file.\n"
          "Sandbox or not, this is the habit the real repo depends on.\n"
          "Put the value in Actions secrets and reference it; add the key to .env.example.")

# Broad stage (git add . / -A) — scan what would actually land.
if re.search(r'\bgit\s+(add|commit)\b', cmd) and re.search(r'(\badd\s+(-A|--all|\.)|commit\s+.*-a\b)', cmd):
    if shutil.which("gitleaks"):
        r = subprocess.run(["gitleaks", "protect", "--staged", "--no-banner", "--redact"],
                           capture_output=True, text=True)
        if r.returncode != 0:
            block("BLOCKED: gitleaks found a credential shape in the staged diff.\n"
                  + (r.stdout or r.stderr)[:1500])
    else:
        st = subprocess.run(["git", "diff", "--cached", "--name-only"],
                            capture_output=True, text=True).stdout.split()
        bad = [f for f in st if re.search(r'(^|/)\.env(\.|$)', f)]
        if bad:
            block("BLOCKED: staged env files: " + ", ".join(bad))
