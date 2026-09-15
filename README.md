# sbx-sdlc — the orchestrator

The control plane for the sandbox rig. It **observes** the three app repos through
branch-tracking submodules and never holds a working copy that can be committed to.
Its own commits are the lifecycle record.

This is the one repo in the rig meant to be **promoted** to the real estate. The other
three (`sbx-web`, `sbx-qa`, `sbx-api`) are scaffolding, deleted the day the findings
are written up.

Mirrors the design in *Evafi SDLC Control Plane*; built per *Evafi SDLC Sandbox*.

## Identity

Everything here runs as the sandbox identity (`sbx-alroy`, Linear workspace `SBX`).
That is automatic inside `~/Codebase/sandbox/` — see `~/.gitconfig-sbx`.
