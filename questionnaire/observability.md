---
id: centralized-logging
category: observability
---
# Centralized Logging

**What is it?** Sending your app's log messages to one place (a service or dashboard) so you can search and filter them instead of only viewing files on a single server.

**Why is it important?** When something goes wrong in production, you need to see what happened. Without a central place, you may not find the right log or the server may already be gone.

**How badly can things break?** You cannot debug production issues, cannot prove what a user did, and outages take much longer to fix.

---

Do you have centralized logging (e.g., CloudWatch, Datadog, ELK)?

- 1: No logging or only local files, no aggregation
- 10: Centralized, searchable, retention and access controlled

---

---
id: error-collection
category: observability
---

# Error Collection

**What is it?** A service that captures errors and exceptions from your app (e.g., Betterstack, Sentry, Rollbar, Logtail) so they appear in a dashboard with stack traces and context. Applies to web apps, mobile apps, and backends.

**Why is it important?** Users do not always report bugs. Without error collection, you may not know the app is failing until it is too late.

**How badly can things break?** Silent failures, unreported crashes, no way to see patterns or fix issues before they affect many users.

---

Do you have error collection (e.g., Betterstack or Sentry for web, Sentry for mobile, or equivalent for backend)?

- 1: No error collection; errors only in logs or invisible
- 10: Error tracking in place with alerts and context (e.g. Betterstack, Sentry, Rollbar)

---

---
id: health-readiness-endpoints
category: observability
---
# Health and Readiness Endpoints

**What is it?** The app exposes health (liveness) and readiness (dependencies up) endpoints so load balancers or orchestrators (e.g. k8s) can route traffic only to healthy instances and avoid sending requests to instances that cannot serve (e.g. DB down).

**Why is it important?** Without health/readiness, bad instances keep receiving traffic and users see errors. Orchestrators need a way to know when to restart or drain.

**How badly can things break?** Traffic to broken instances, slow failure detection, and restarts that do not fix the problem because readiness was never checked.

---

Are there health/readiness endpoints that reflect real dependency state (e.g. DB, cache)?

- 1: No health/readiness or they do not check dependencies
- 10: Health and readiness endpoints; used by LB or orchestrator; reflect actual state

---

---
id: monitoring-alerting
category: observability
---
# Monitoring and Alerting

**What is it?** Beyond logging: metrics and alerting so that failures (high error rate, latency, downtime) are detected and someone is notified. Not just "we have logs" but "we get paged when something is wrong".

**Why is it important?** Logs alone do not wake you up. Without alerting, outages are discovered by users and response is delayed.

**How badly can things break?** Outages that last until users complain, no visibility into degradation, and no way to meet SLOs.

---

Is there monitoring and alerting on failures (error rate, latency, downtime)—not just logging?

- 1: No alerting; issues discovered by users
- 10: Monitoring and alerting in place; on-call or defined response when alerts fire

---

---
id: user-facing-errors-and-logging
category: observability
---
# User-Facing Errors Safe and Proper Error Logging

**What is it?** When something fails, users see a safe, generic message (or a friendly error page)—not stack traces, internal URLs, or sensitive data. At the same time, errors are logged properly (e.g. to console or your logging system) with enough context for debugging so developers can fix issues.

**Why is it important?** Exposing stack traces or internal details to users is a security and UX failure. Without proper error logging, developers cannot debug production issues.

**How badly can things break?** Users see scary or sensitive information; attackers get hints; support and devs have no way to diagnose what went wrong.

---

Do users see safe error messages (no stack traces or secrets), and are errors logged properly for debugging (e.g. to console or logging system)?

- 1: Stack traces or internal details shown to users; no useful error logging
- 10: User-facing errors safe and generic; errors logged with context for debugging
