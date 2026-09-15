# The seeded backlog

Five rig tickets, each engineered so one specific gate has to fire. **A gate that does
not fire is a finding**, not a pass.

Linear's four default onboarding issues had already taken SBX-1..SBX-4, so the build
sheet's numbering shifted. They are cancelled, not deleted. The mapping:

| Build sheet | Actual | Ticket | Proves | Expected |
|---|---|---|---|---|
| SBX-1 | **SBX-5** | Add a progress bar to the onboarding funnel | The golden path — UI + analytics + named QA coverage | Clean run |
| SBX-2 | **SBX-6** | Set the step label at 18px, per the mock | Policy conflict: no 18px role exists | Spec flags it at G2 |
| SBX-3 | **SBX-7** | Add a resend-OTP endpoint | The API skill, all six clauses | Clean run |
| SBX-4 | *(none)* | — planted bug, no ticket — | The closed loop | Bug + intent.md appear unasked |
| SBX-5 | **SBX-8** | Loosen the API-route skill | The eval gate | Eval pass rate drops, PR blocked |

https://linear.app/sbx-acme/team/SBX

## The one with no ticket

Nobody files it, nobody runs it, nobody asks for the fix. At the end of Day 2, merge a
change that breaks a regression assertion in `sbx-qa`. The 06:00 scheduled suite fails,
the triage job writes the Linear bug **and** an `intent.md`, and the next morning there
is work in the queue that no human created.

That is the whole thesis of Stage 6 in one overnight, and it is the finding worth
waiting for — in either direction.

## Order

SBX-5 → SBX-6 → SBX-7 one at a time, by hand at every stage, watching two things:

- **where you get bored** — that is the handoff to automate next
- **where you override the agent** — that correction belongs in a skill

Then the seven probes. Then SBX-8 last, as deliberate sabotage.

## The stop rule

If a sandbox change does not make a gate testable, it does not get made. The rig only
pays for itself while it stays ugly.
