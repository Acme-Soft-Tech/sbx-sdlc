#!/usr/bin/env python3
"""Write to Linear from anywhere — a shell, a slash command, or CI.

Linear is the system of record for this loop. The GitHub integration attaches PRs
on its own, but it only reacts to git events, and the moments that matter here are
not git events: a spec being accepted, QA going green, a monitoring band breaching.
Those have to be written deliberately, which is what this does.

    linear_sync.py state   SBX-5 "In Progress"
    linear_sync.py comment SBX-5 --body "Stage 2 complete"
    linear_sync.py comment SBX-5 --body-file spec-summary.md
    linear_sync.py link    SBX-5 --url https://preview.vercel.app --title "Preview"

Needs LINEAR_API_KEY. Exits non-zero with a plain message on failure — a silent
no-op here means the ticket quietly stops reflecting reality, which is worse than
a loud failure.
"""
import argparse
import json
import os
import sys
import urllib.error
import urllib.request

API = "https://api.linear.app/graphql"
ENV_FILE = os.environ.get("SBX_ENV", os.path.expanduser("~/.config/sbx/linear.env"))


def _load_local_env():
    """A GitHub Actions secret is write-only and cannot be read back, so anything
    running on a workstation needs its own copy. Kept outside every repo."""
    if os.environ.get("LINEAR_API_KEY") or not os.path.exists(ENV_FILE):
        return
    with open(ENV_FILE) as fh:
        for line in fh:
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            k, v = line.split("=", 1)
            os.environ.setdefault(k.strip(), v.strip().strip("\"'"))


_load_local_env()


def gql(query, variables=None):
    key = os.environ.get("LINEAR_API_KEY", "").strip()
    if not key:
        sys.exit("LINEAR_API_KEY is not set. Refusing to continue: without it the "
                 "ticket silently stops reflecting what actually happened.")
    req = urllib.request.Request(
        API,
        data=json.dumps({"query": query, "variables": variables or {}}).encode(),
        headers={"Content-Type": "application/json", "Authorization": key},
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            body = json.load(r)
    except urllib.error.HTTPError as e:
        sys.exit(f"Linear HTTP {e.code}: {e.read().decode(errors='replace')[:300]}")
    except Exception as e:
        sys.exit(f"Could not reach Linear: {e}")
    if body.get("errors"):
        sys.exit("Linear API error: " + body["errors"][0].get("message", "unknown"))
    return body["data"]


ISSUE = """query($id:String!){ issue(id:$id){
  id identifier branchName url
  state { id name type }
  team { id key }
}}"""

STATES = """query($teamId:String!){ team(id:$teamId){
  states { nodes { id name type } }
}}"""

UPDATE = """mutation($id:String!,$input:IssueUpdateInput!){
  issueUpdate(id:$id,input:$input){ success issue{ identifier state{name} } }
}"""

COMMENT = """mutation($input:CommentCreateInput!){
  commentCreate(input:$input){ success comment{ id } }
}"""

ATTACH = """mutation($input:AttachmentCreateInput!){
  attachmentCreate(input:$input){ success attachment{ id } }
}"""


def get_issue(key):
    issue = gql(ISSUE, {"id": key})["issue"]
    if not issue:
        sys.exit(f"No such issue: {key} (is the token for this workspace?)")
    return issue


def cmd_state(args):
    issue = get_issue(args.key)
    if issue["state"]["name"].lower() == args.state.lower():
        print(f"{issue['identifier']} already {issue['state']['name']} — nothing to do")
        return
    states = gql(STATES, {"teamId": issue["team"]["id"]})["team"]["states"]["nodes"]
    match = next((s for s in states if s["name"].lower() == args.state.lower()), None)
    if not match:
        sys.exit(f"No state named {args.state!r} on team {issue['team']['key']}. "
                 f"Available: {', '.join(s['name'] for s in states)}")
    gql(UPDATE, {"id": issue["id"], "input": {"stateId": match["id"]}})
    print(f"{issue['identifier']}: {issue['state']['name']} -> {match['name']}")


def cmd_comment(args):
    body = args.body
    if args.body_file:
        body = sys.stdin.read() if args.body_file == "-" else open(args.body_file).read()
    if not body or not body.strip():
        sys.exit("Refusing to post an empty comment")
    issue = get_issue(args.key)
    gql(COMMENT, {"input": {"issueId": issue["id"], "body": body}})
    print(f"{issue['identifier']}: commented ({len(body)} chars)")


def cmd_link(args):
    issue = get_issue(args.key)
    gql(ATTACH, {"input": {"issueId": issue["id"], "url": args.url, "title": args.title}})
    print(f"{issue['identifier']}: linked {args.title} -> {args.url}")


def cmd_branch(args):
    print(get_issue(args.key)["branchName"])


p = argparse.ArgumentParser(description=__doc__.split("\n")[0])
sub = p.add_subparsers(dest="cmd", required=True)

s = sub.add_parser("state", help="move the issue to a named workflow state")
s.add_argument("key"); s.add_argument("state"); s.set_defaults(fn=cmd_state)

c = sub.add_parser("comment", help="post a comment")
c.add_argument("key")
c.add_argument("--body"); c.add_argument("--body-file")
c.set_defaults(fn=cmd_comment)

l = sub.add_parser("link", help="attach a URL to the issue")
l.add_argument("key"); l.add_argument("--url", required=True); l.add_argument("--title", required=True)
l.set_defaults(fn=cmd_link)

b = sub.add_parser("branch", help="print the issue's Linear branch name")
b.add_argument("key"); b.set_defaults(fn=cmd_branch)

args = p.parse_args()
args.fn(args)
