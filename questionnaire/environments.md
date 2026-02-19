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
