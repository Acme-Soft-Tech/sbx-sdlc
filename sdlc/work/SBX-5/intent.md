# SBX-5 — Intent

**Source:** Linear SBX-5 — https://linear.app/sbx-acme/issue/SBX-5
**Requested by:** Alroy (product owner)
**Date:** 2026-09-15

## The problem

The onboarding funnel is four steps long and gives no indication of where you are in
it. Someone on step 2 cannot tell whether one question remains or ten, and the only
way to find out is to keep answering.

This is the rig's golden-path ticket: it is deliberately ordinary. It should pass
through every stage without a gate firing. **If any gate fires here, that is the
finding** — it means a gate is miscalibrated and will cry wolf on routine work, which
is how gates get disabled.

## Who it affects

Everyone entering the funnel. In the sandbox that is the acceptance suite and nobody
else, which is the point: the rig is testing the process, not the product.

## Success looks like

- A person on any step can see how many steps there are and which one they are on.
- The step they are on is derived from the same source of truth the funnel already
  uses, not a second counter that can drift from it.
- The funnel's analytics still report the same step indices they did before. Existing
  PostHog history must remain comparable — a renumbering here would silently
  invalidate every funnel chart built on those indices.

## Out of scope

- Any change to the number or order of steps.
- Any change to `FUNNEL_STEP_MAP` indices. Adding a *view* of progress must not
  become a reason to renumber the funnel.
- Visual design beyond the existing type scale. If the progress indicator seems to
  need a size the scale does not have, that is a spec conflict to raise, not a
  licence to hand-type one.
- Persisting progress across a reload.

## Open questions

1. **Does reaching a step count as completing the previous one?** A bar that fills on
   arrival and one that fills on completion tell different stories on the last step.
   Assumed: fills on arrival, so step 4 of 4 shows full.
2. **Does the progress bar emit its own analytics event?** Assumed no — it is a view
   of state the funnel already reports, and a second event per step would double-count
   every transition in PostHog.
3. **Is the OTP step counted?** It is step 4 in `FUNNEL_STEP_MAP`, so assumed yes.

These are assumptions, not decisions. Correct any that are wrong before merging —
that correction is cheap here and expensive at Stage 3.

---
Gate G1 — merged by: _pending_
