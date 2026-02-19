---
id: git-usage
category: tooling
---
# Version Control: Git Usage and Workflow Quality

**What is it?** All application code is in Git (or equivalent). Beyond that, the quality of Git workflow matters for scalability: single repo (monorepo) is a start; a clear branching strategy (e.g. main/develop, release branches, PR flow) is better for team and release discipline.

**Why is it important?** Code not in Git can be lost and is not reviewable. Poor or no branching strategy leads to "everything on main" chaos and hard rollbacks.

**How badly can things break?** Lost code, no history, and impossible to scale collaboration. No branching strategy = 5; defined and used strategy = 10.

---

Is all code in Git? What is the quality of Git workflow (branching, releases)?

- 1: Code not in Git or only partially; no real version control
- 5: Code in Git; single repo (monorepo) but no clear branching strategy
- 10: Code in Git; branching strategy identified and in use (e.g. main/develop, PRs, release flow)
