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

**What is it?** A service that captures errors and exceptions from your app (e.g., Sentry, Rollbar) so they appear in a dashboard with stack traces and context.

**Why is it important?** Users do not always report bugs. Without error collection, you may not know the app is failing until it is too late.

**How badly can things break?** Silent failures, unreported crashes, no way to see patterns or fix issues before they affect many users.

---

Do you have error collection (e.g., Sentry for mobile/web, or equivalent for backend)?

- 1: No error collection; errors only in logs or invisible
- 10: Error tracking in place with alerts and context
