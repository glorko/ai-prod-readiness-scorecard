---
id: regression-testing
category: testing
---
# Regression Prevention and Test Coverage

**What is it?** Measures so that new changes do not silently break existing behaviour. Automated tests (unit, integration, e2e) catch regressions before they reach production. The worst case is undocumented implementation with no tests—every bugfix can introduce new bugs.

**Why is it important?** Vibecoded and LLM-assisted code often changes quickly; without tests, refactors and "small fixes" break things that used to work. Regression suite is the safety net.

**How badly can things break?** Every release can break something else; no way to know without tests. "We fixed login but broke payments" is typical when there is no automation.

---

How well are regressions prevented? (New changes should not override or break previous behaviour.)

- 1: No tests; only undocumented implementation; any change is a gamble
- 5: At least unit tests for critical paths
- 10: App covered by automated regression suite (unit + integration or e2e as appropriate)
