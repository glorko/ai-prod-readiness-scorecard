---
id: cicd-pipeline
category: delivery
---
# CI/CD Pipeline: Quality Checks and Delivery to Production

**What is it?** A continuous integration and delivery (or deployment) pipeline that runs quality checks (build, test, lint, security) and delivers the app to production only after those checks pass.

**Why is it important?** Without CI/CD, releases are manual and inconsistent; broken or untested code can reach production. Automated pipeline enforces "no deploy without green checks".

**How badly can things break?** Broken builds in prod, untested code deployed, and no single path from commit to release.

---

Is there an appropriate CI/CD pipeline that checks quality and delivers the app to production after all checks pass?

- 1: No CI/CD; manual or ad-hoc deploys only
- 10: CI/CD in place: build, test, and quality gates; production deploy only after success

---

---
id: feature-flags-rollouts
category: delivery
---
# Feature Flags and Safe Rollouts (Including Mobile)

**What is it?** Feature flags or similar mechanisms allow turning features on/off without redeploy, so rollouts can be gradual and critical issues can be turned off quickly. For users this is critical: a bad feature can be disabled before it affects everyone. For mobile apps: validate that the app uses a proper paradigm and framework for internal builds, testing, and propagation to production (e.g. TestFlight, internal tracks, staged rollouts)—not "only prod build" with no way to test before release.

**Why is it important?** Without feature flags, the only way to stop a bad feature is a full redeploy and rollback—slow and risky. For mobile, internal builds and staged rollout are essential so not every user gets a broken version at once.

**How badly can things break?** A bad feature affects 100% of users until a new release; mobile users get broken builds with no way to test first. Critical for safe rollouts and mobile release hygiene.

---

Are feature flags or similar used for safe rollouts and quick kill switches? For mobile: is there a proper paradigm for internal builds, testing, and propagation to production (e.g. TestFlight, internal tracks)?

- 1: No feature flags; no mobile internal/testing track—full blast to prod
- 10: Feature flags for rollouts and kill switch; mobile: internal builds and staged rollout to prod

---

---
id: deploy-repeatable-automated
category: delivery
---
# Repeatable and Automated Deploy

**What is it?** The release and deploy process is repeatable and automated—not "run these 12 manual steps from a doc". Same command or pipeline produces a deploy; no tribal knowledge required.

**Why is it important?** Manual steps are error-prone and do not scale. Only one person may know the "real" steps; bus factor is one.

**How badly can things break?** Failed deploys because a step was forgotten, and inability to release when that one person is unavailable.

---

Is the deploy process repeatable and automated (not a long list of manual steps)?

- 1: Deploy is a manual checklist; not automated
- 10: Deploy is automated and repeatable; same process every time

---

---
id: background-jobs-configured
category: delivery
condition: "app_uses_background_jobs"
---
# Background Jobs Configured Properly

**What is it?** If the app uses background jobs (queues, workers, cron, scheduled tasks), they are configured properly: how they run, how they are monitored, retries and failure handling, and that they don't exhaust resources or block the main app.

**Why is it important?** Misconfigured jobs can run forever, run twice, or bring down the app. Users may see delayed or missing work (e.g. emails not sent, exports never finish).

**How badly can things break?** Jobs that crash the worker, duplicate work, or never run; main app blocked by runaway jobs. Only assess when the app actually uses background jobs.

---

If the app uses background jobs (queues, workers, cron): Are they configured properly (run model, retries, failure handling, resource limits)?

- 1: Jobs ad-hoc or misconfigured; risk of runaway or blocking
- 10: Jobs properly configured; monitored; retries and limits in place
