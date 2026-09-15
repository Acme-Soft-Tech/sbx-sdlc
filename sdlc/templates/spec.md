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

    <repo> · tests/<file>::<Class>::<test>            [PR 1 | PR 2]
      marker: inherited from the class, or named if new
      asserts: <what, concretely>

## Flagged concerns
<Every policy conflict you could not satisfy. Empty only if there genuinely are none.>

## DOM contract   *(mandatory for any two-repo change)*
<the exact data-testid / attributes sbx-qa will select on. The DOM is the only
interface between the repos; leaving it unstated makes the acceptance tests unwritable.>

## Sequencing
PR 1 sbx-web -> merge -> deploy -> confirm the hook is live -> PR 2 sbx-qa. No xfail.

---
spec-reviewer verdict:
Gate G2 — accepted by:
