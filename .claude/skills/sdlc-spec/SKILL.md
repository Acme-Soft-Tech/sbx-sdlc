---
name: sdlc-spec
description: Writing spec.md, the Stage 2 artifact, including the Acceptance contract. Use for /spec.
---

## Keep it thin — this is a rig

The stop rule: **if it does not make a gate testable, it does not get written.** The
sandbox tests the process, not the product, and it only pays for itself while it stays
ugly. A spec here needs enough detail to build from and no more.

The one section that must be rigorous is **Acceptance**, because that is what G2 and G4
actually test. Product-quality concerns — accessibility semantics, design polish, API
ergonomics — are real, and out of scope: note them in a line and move on. Time spent
arguing them is time the rig is not testing anything.

A policy CONFLICT still gets flagged, because catching those is what Stage 2 is for.
A product OPINION does not.

Read `intent.md`. Load the policy skills — `sbx-design-system`, `sbx-analytics`,
`sbx-api-route`, `qa-test-authoring` — and write the design the team can plan against.

**Flag every conflict you cannot satisfy rather than resolving it quietly.** A mock that
wants a type-scale role that does not exist, an API shape that would put PII in a log
line: these surface here, as a document, or they surface in review three weeks later.
A spec with no flagged concerns on a change that has them is a failed spec.

## The Acceptance section is mandatory

This is what makes the rig a two-repo lifecycle rather than two projects. Name the
`sbx-qa` markers and test classes the change needs **before anyone writes code**:

    ## Acceptance
    - sbx-qa · tests/test_Regression_Class.py::TestRegression::test_progress_bar_advances
      marker: inherited from the class · PR 2, after the web deploy

A funnel change with no `@pytest.mark.regression` coverage fails G2 on the document.

**Pin the DOM contract.** On any two-repo change the DOM is the only interface between
`sbx-web` and `sbx-qa`. State the exact `data-testid` and attributes, or both sides
guess and the acceptance tests cannot be written at all.

Template: `sdlc/templates/spec.md`. **Gate G2: concerns resolved, then a human accepts.**
Run the `spec-reviewer` subagent before presenting it.
