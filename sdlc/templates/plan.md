# <KEY> — Plan

Reads: `spec.md` (accepted <date>)

## sbx-web
- <path>    new | edit — <what>

## sbx-qa
- <path>    new | edit — <what>

## Risks
- <what could go wrong, and what would tell us early>

## Verify
- sbx-web: npm run lint · npx tsc --noEmit · npm run test:coverage
- sbx-qa:  ruff check . · pytest -m "smoke or regression"

---
Plan accepted by: <human>   *(plan mode enforces this)*
