---
name: sdlc-spec
description: Writing spec.md, the Stage 2 artifact, including the Acceptance contract. Use for /spec.
---

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
    - tests/test_Regression_Class.py::TestRegression::test_progress_bar_advances
      marker: regression · new · lands xfail in the web PR

A funnel change with no `@pytest.mark.regression` coverage fails G2 on the document.

Template: `sdlc/templates/spec.md`. **Gate G2: concerns resolved, then a human accepts.**
Run the `spec-reviewer` subagent before presenting it.
