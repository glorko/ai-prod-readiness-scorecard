---
id: code-reusability
category: code-quality
---
# Component Approach and Reusability

**What is it?** Code is organized into reusable components or modules instead of copy-paste and one-off solutions. LLMs tend to reinvent the wheel; a component approach encourages shared, consistent behaviour.

**Why is it important?** Duplicated logic means bugs get fixed in one place and not another. Reusable components make changes consistent and reduce "400 places to change" situations.

**How badly can things break?** Inconsistent behaviour across the app, fixes that miss half the copies, and unmaintainable sprawl.

---

Is there a component approach with reusability (shared components, no reinventing the wheel per feature)?

- 1: Copy-paste and one-off code; no shared components
- 10: Clear component/module boundaries, reuse, and consistent patterns

---

---
id: libraries-stable
category: code-quality
---
# Libraries: Stable and Up-to-Date Versions

**What is it?** Dependencies (libraries) in use are stable, reasonably up-to-date versions—not abandoned or known vulnerable. No "we built this from scratch" when a mature library exists.

**Why is it important?** Old or unmaintained libs have security and compatibility issues. Reinventing core functionality (parsing, HTTP, crypto) is error-prone and wastes time.

**How badly can things break?** Security vulnerabilities, breaking changes when you finally upgrade, and bugs that a standard library would have avoided.

---

Are libraries in use stable and at reasonable/latest versions? Is the app using established libraries instead of reinventing core functionality?

- 1: Abandoned or very old libs; or critical things built from scratch
- 10: Stable, maintained versions; standard libs used for standard problems

---

---
id: libraries-standard-practice
category: code-quality
---
# Libraries: Using Standard Practice (No Custom Reinvention)

**What is it?** For standard tasks (JSON parsing, HTTP client, DB driver, validation), the app uses the language/framework standard or well-known libraries—not custom implementations. Example: in Go, use encoding/json (unmarshaller), not a hand-rolled JSON parser.

**Why is it important?** LLMs often generate "custom" parsers or utilities that are buggy and incomplete. Standard libs are tested and handle edge cases.

**How badly can things break?** Parsing bugs, encoding errors, and subtle bugs that standard libraries would have prevented. "We wrote our own JSON parser" is a red flag.

---

Does the code use standard/library implementations for standard tasks (e.g. JSON, HTTP, validation) instead of custom reinventions?

- 1: Custom parsers or critical utilities reinvented; LLM-style "custom" code for standard problems
- 10: Standard library or well-known libs for parsing, HTTP, DB, validation; no reinvention

---

---
id: no-oversized-files
category: code-quality
---
# No Oversized Files (Under ~1000 Lines)

**What is it?** No single source file (code that humans or an LLM need to read and edit) is over roughly 1000 lines. Large files are split into modules or components.

**Why is it important?** Files over ~1000 lines are extremely hard to maintain with LLM assistance: the model often cannot or does not read the whole file, so it misses context and makes inconsistent or wrong edits. For humans, huge files are also hard to reason about and review.

**How badly can things break?** LLM edits in the middle of a 2000-line file that ignore logic at the top or bottom; merge conflicts; and changes that break behaviour the editor never "saw". Refactors become risky.

---

Are there any source files over ~1000 lines of code? (Exclude generated code if clearly separated.)

- 1: Multiple files over 1000 LOC; or one or more very large files (e.g. 2000+)
- 10: No files over ~1000 LOC; codebase split into maintainable file sizes

---

---
id: dependency-scanning
category: code-quality
---
# Dependency Vulnerability Scanning

**What is it?** Dependency vulnerability scanning (e.g. Dependabot, Snyk, npm audit) is enabled and failures are either blocking in CI or reviewed so known-vulnerable dependencies are not ignored in production.

**Why is it important?** Old or vulnerable dependencies are a major attack vector. Scanning catches known CVEs before they reach prod.

**How badly can things break?** Supply-chain and dependency vulnerabilities in production; compliance and security incidents that could have been avoided.

---

Is dependency vulnerability scanning enabled and are failures blocking or reviewed?

- 1: No scanning or known vulnerabilities ignored
- 10: Scanning in CI; critical/high addressed or blocking; no ignored known vulnerabilities

---

---
id: static-analysis-lint-ci
category: code-quality
---
# Static Analysis and Lint in CI

**What is it?** Static analysis and lint (e.g. linters, type checks, formatters) run in CI and failures block or are enforced so code quality and style are consistent and many bugs are caught before merge.

**Why is it important?** Lint and types catch mistakes early. Without them in CI, quality drifts and broken code can be merged.

**How badly can things break?** Style and type errors in prod, inconsistent codebase, and bugs that static analysis would have caught.

---

Are static analysis and lint run in CI and blocking on failure?

- 1: No lint/static analysis in CI or always bypassed
- 10: Lint and type checks in CI; failures block merge; consistent quality

---

---
id: code-review
category: code-quality
---
# Code Review Before Merge

**What is it?** Changes are reviewed before merging to main or release branches. For solo vibecoders, AI-assisted code review (e.g. LLM review of diffs, Copilot review) is acceptable—the point is that code is not merged without some review, not that it must be human-only. Most applicable for **big projects or those with complicated business logic**; for small/simple apps it's nice to have in general.

**Why is it important?** Unreviewed code increases the chance of bugs and bad patterns. For large or complex codebases, a second pair of eyes (human or AI) is critical. For small projects it still helps catch obvious issues. Most vibecoders work alone; AI review is better than none.

**How badly can things break?** Obvious bugs and security issues merged; no second pair of eyes. Risk scales with project size and complexity. AI code review is good enough when human reviewers are not available.

---

Is there code review (human or AI-assisted) before merge? (Most critical for big or complex projects; nice to have in general. AI review is acceptable for solo devs.)

- 1: No review; direct push to main
- 10: PR review (human or AI) before merge; feedback addressed
