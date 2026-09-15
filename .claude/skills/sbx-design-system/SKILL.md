---
name: sbx-design-system
description: Type scale and token rules for sbx-web. Use when writing or editing any component, className, or globals.css.
---

The type scale has exactly five roles, defined in `@theme` in `app/globals.css`:
`--text-display`, `--text-heading`, `--text-subheading`, `--text-body`, `--text-caption`.

**A hand-typed size is a policy violation.** `text-[18px]`, `style={{fontSize:18}}`,
`text-lg` — all three are the same mistake. If a mock calls for a size no role covers,
that is a **design conflict to raise in the spec**, not something to resolve in a
component. Stage 2 exists to catch exactly this.

## Legacy — read before you "fix" anything

`sbx-web` carries deliberately planted legacy: two hand-typed `text-[18px]` values and
one inline-SVG icon component, all marked legacy-but-supported below. They mirror the
34 such cases in the real repo.

- `src/ui/onboarding/section/DebtStep.tsx` — two `text-[18px]`, legacy, **leave alone**
- `src/ui/icons/LegacyChevron.tsx` — inline SVG, legacy, **leave alone**

Do not fix these as a drive-by while doing something else in the same file. If you
notice one while working, say so in the PR description and move on. An unrelated diff
that also "tidies" legacy is a finding against you, not a contribution.
