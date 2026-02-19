---
id: non-prod-env
category: environments
---
# Non-Production Environment

**What is it?** At least one environment (e.g., staging, dev) that is not production and not just your laptop, where you can test deployments and changes before they go live.

**Why is it important?** Production should not be the first place you run a new version. Without a staging-like environment, every deploy is a gamble.

**How badly can things break?** Broken deploys go straight to users, rollbacks are guesswork, and "works on my machine" becomes "broken in production."

---

Do you have at least one non-prod environment (staging, dev) besides local?

- 1: Only production and local; no staging
- 10: Staging (or equivalent) with parity to prod, used for releases

---

---
id: rollback-approach
category: environments
---
# Rollback: Restoring Previous Version on Critical Failure

**What is it?** A defined way to put the previous version of the app back in production when a new release has critical issues (e.g. one-click rollback, redeploy last known good, feature flags).

**Why is it important?** Bad releases happen. Without a rollback path, you are stuck between "broken prod" and "risky fix forward"—often under pressure.

**How badly can things break?** Extended outages, "we can't roll back" panic, and data or config tied to the bad version with no clean revert.

---

What is the approach to restore the previous version of the app if the new version has critical issues?

- 1: No defined rollback; manual guesswork or impossible
- 10: Documented, tested rollback (e.g. redeploy previous artifact, feature flags, DB-compatible releases)

---

---
id: environment-description
category: environments
---
# Environment Description (Prod and Staging)

**What is it?** The production (and staging) environment is described somewhere: OS, runtime version, key services, so that "it works on my machine" can be checked and new contributors know what they are deploying to.

**Why is it important?** Without a written description, only one person may know the real env; upgrades and debugging are guesswork. Reproducibility requires knowing the target.

**How badly can things break?** Deploys that fail in prod because "we didn't know it was different", and long debugging when the env is undocumented.

---

Is the production (and staging) environment described (OS, runtime, key services) so the target is known?

- 1: No description; env is tribal knowledge
- 10: Documented env (e.g. README, runbook, IaC); runtime and key deps listed
