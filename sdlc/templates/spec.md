# <KEY> — Spec

Reads: `intent.md` (merged <date>)

## Design
<What changes, per surface.>

## Analytics
<New EVENTS entries, EventPropertiesMap additions, FUNNEL_STEP_MAP indices.>

## API
<Endpoints, following the six-step handler shape.>

## Acceptance   *(mandatory)*
<Markers and test classes in sbx-qa this needs, named before code is written.>

    tests/<file>::<Class>::<test>
      marker: smoke | regression · new | existing · xfail until web deploys

## Flagged concerns
<Every policy conflict you could not satisfy. Empty only if there genuinely are none.>

## Sequencing
web merges first · QA test lands xfail in the web PR · follow-up flips it

---
spec-reviewer verdict:
Gate G2 — accepted by:
