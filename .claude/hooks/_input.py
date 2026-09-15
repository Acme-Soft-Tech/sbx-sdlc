"""Read a Claude Code hook payload on stdin. Never raise: a crashing hook
that fails open is worse than no hook, so unparseable input yields empties."""
import json, sys

def read():
    try:
        d = json.load(sys.stdin)
    except Exception:
        return "", {}, ""
    ti = d.get("tool_input") or {}
    return d.get("tool_name", ""), ti, (ti.get("command") or "")

def block(msg):
    print(msg, file=sys.stderr)
    sys.exit(2)
