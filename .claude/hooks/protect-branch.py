#!/usr/bin/env python3
# Blocks: a commit while main/master is checked out, --no-verify, and force push.
import re, subprocess, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _input import read, block

name, ti, cmd = read()
if name != "Bash" or "git" not in cmd:
    sys.exit(0)

if re.search(r'--no-verify|-n\b(?=.*commit)', cmd):
    block("BLOCKED: --no-verify strips the commit-msg and pre-commit hooks.\n"
          "Those hooks are the only thing enforcing the Linear key in the subject.\n"
          "Fix what the hook is complaining about instead of skipping it.")

if re.search(r'push\b.*(--force\b|-f\b|--force-with-lease)', cmd):
    block("BLOCKED: force push. History on a shared branch is an audit trail.\n"
          "If you must rewrite, do it on your own feature branch and say so in the PR.")

if re.search(r'\bgit\s+commit\b', cmd):
    # symbolic-ref, not rev-parse: on a repo with no commits yet the branch is
    # "unborn" and rev-parse --abbrev-ref errors, which would fail the guard OPEN.
    br = ""
    for argv in (["git", "symbolic-ref", "--quiet", "--short", "HEAD"],
                 ["git", "rev-parse", "--abbrev-ref", "HEAD"]):
        try:
            r = subprocess.run(argv, capture_output=True, text=True, timeout=5)
            if r.returncode == 0 and r.stdout.strip():
                br = r.stdout.strip()
                break
        except Exception:
            pass
    if br in ("main", "master"):
        block(f"BLOCKED: commit on '{br}'.\n"
              f"Branch protection on the remote would reject this anyway; this hook just\n"
              f"tells you now instead of after the push.\n"
              f"  git switch -c <linear-branch-name>   # Linear gives you the name\n"
              f"then commit and open a PR.")
