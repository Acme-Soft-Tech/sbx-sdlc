# Review policy — imported by both app repos

Three passes, in this order. Claude reviews and fixes on `@claude` mention. **It has no
route to approve.** Branch protection still wants a human, and that is the point of G5.

## 1. Bugs
Against the committed `plan.md`. Does the diff do what the plan said, and nothing else?
An unrelated change in the diff is a finding even when it is an improvement.

## 2. Security
- PII in a log line or analytics property — phone, email, name, OTP value
- A bare `fetch(` inside `app/api`
- Upstream error text reaching a client response
- Anything resembling a credential

## 3. Compliance with the spec
- Does the **Acceptance** section's named coverage actually exist in the diff?
- Type scale: any hand-typed size is a finding unless the spec flagged it at G2
- Analytics: both success and failure paths emit
- Legacy marked in `sbx-design-system` untouched — a drive-by tidy is a finding

## What a finding is not
Style preference already settled by a linter. Say it once in the skill, not every PR.
