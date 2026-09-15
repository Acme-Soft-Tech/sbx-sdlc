---
name: qa-test-authoring
description: Conventions for writing tests in sbx-qa. Use when adding or editing any pytest/Playwright test, conftest, or marker.
---

These live only in code comments in the real repo. That is the gap this file closes.

- **`conftest.py` sits at the repo root.** Not in `tests/`. Fixtures break subtly otherwise.
- **PascalCase test filenames**: `test_Smoke_Class.py`, `test_Regression_Class.py`.
- **One class per file.** The real repo's 750-line `test_dailyrun.py` is what happens
  when this slips: seven classes redefined, nineteen diverged helper copies, every test
  running twice per suite.
- **Helpers live in `wizard_helpers.py`.** Never a local copy.
- **Base URL comes from `SBX_BASE_URL`**, with no default host. A default that only
  applies when the var is unset is a trap: CI passes an unset variable, the host blanks,
  and the suite quietly tests nothing.

## The SMS rule

Anything that reaches "Send code" **must** carry `@pytest.mark.flaky(reruns=0)`.
`pytest.ini` sets a global `--reruns 2`; a flaky retry on an SMS test sends real
messages nobody counted. Every SMS-sending test in the suite carries this marker and a
comment saying why. Adding one without it is the single worst change you can make here.

## Markers

`smoke` · `regression` · `e2e` · `ui`. PR and agent runs are `-m "smoke or regression"`.
`e2e` sends SMS and is blocked by `sms-guard.sh` without `SBX_ALLOW_SMS=1`.
