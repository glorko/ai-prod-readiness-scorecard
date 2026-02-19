---
id: microservices-scale
category: architecture
---
# Architecture Fit for Scale

**What is it?** Choosing a simple architecture (e.g., one app, one database) when you have a small number of users, instead of splitting into many microservices too early.

**Why is it important?** Microservices add complexity: deployment, debugging, and coordination. For a small app, that complexity slows you down and increases the chance of failures without real benefit.

**How badly can things break?** Over-engineering leads to more moving parts, harder debugging, and more ways for deployments to fail—often without any gain for a small user base.

---

For an app with ~100 users (or similar small scale), are you avoiding microservices (i.e., not over-engineered)?

- 1: Unnecessarily complex (e.g., many services for a tiny app)
- 10: Simple, appropriate architecture (e.g., modular monolith or minimal services)

---

---
id: backend-tech-applicability
category: architecture
---
# Backend Technology Applicability

**What is it?** Using a backend technology that fits the app's seriousness and domain. Scripting languages (e.g. Node.js, Python for heavy backend) are fine for simple apps and scripts; serious or regulated domains (e.g. banking, money flows, enterprise integrations) expect typed, robust runtimes (e.g. Rust, Go, Java). Typed languages catch many errors at compile time.

**Why is it important?** Non-typed or scripting backends for critical logic are a ticking bomb: one runtime type error or unhandled edge case can cause data or money errors. Regulators and partners expect proven stacks for serious workloads.

**How badly can things break?** Money miscalculations, data corruption, and production bugs that could have been caught at compile time. In banking or high-stakes apps, Node.js (or similar) without strong typing is a major risk.

---

Is the backend technology appropriate for the app's domain? (Simple apps: scripting/Node OK. Serious apps, money, enterprise: typed languages like Rust, Go, Java expected. Prefer typed for compile-time safety.)

- 1: Scripting/untyped backend for serious or money-related app; high risk
- 10: Typed, appropriate stack (e.g. Rust, Go, Java) for domain; or simple app on scripting with clear boundaries

---

---
id: timeouts-considered
category: architecture
---
# Timeouts Considered and Relevant

**What is it?** The app sets timeouts on external calls (APIs, DB, queues, HTTP clients) and internal operations where relevant, so a hung dependency does not block the app forever. Timeouts are appropriate to the operation (not "no timeout" or "30s for everything").

**Why is it important?** Without timeouts, one slow or stuck dependency can tie up threads or connections and take down the app. Cascading failures start with "waiting forever".

**How badly can things break?** Thread pool exhaustion, cascading failures, and outages that last until restarts. Critical for any app that calls external services or DB.

---

Are timeouts set and relevant for external calls and blocking operations?

- 1: No timeouts or inappropriate (e.g. infinite wait, same value everywhere)
- 10: Timeouts on external calls and blocking ops; values appropriate to each operation

---

---
id: idempotency-critical-ops
category: architecture
---
# Idempotency for Critical Operations

**What is it?** For critical or non-idempotent operations (e.g. payments, signup, order placement), the app has idempotency keys or duplicate protection so that retries or double submissions do not create duplicate side effects.

**Why is it important?** Networks and clients retry. Without idempotency, one double-click or retry can charge twice or create two accounts. Payment and order flows must be safe under retries.

**How badly can things break?** Double charges, duplicate records, and user distrust. Critical for payments and any non-idempotent action.

---

For critical operations (payments, orders, signup), is there idempotency or duplicate protection?

- 1: No idempotency; retries can double-charge or duplicate
- 10: Idempotency keys or equivalent; duplicate detection; safe under retries

---

---
id: caching-strategy
category: architecture
---
# Caching Strategy

**What is it?** If the app uses caching, there is a clear strategy: what is cached, how it is invalidated, and how consistency is maintained. Not "cache everything" without thought, and not caches that never expire or are never invalidated.

**Why is it important?** Bad caching leads to stale data, wrong results, and bugs that are hard to reproduce. Invalidation is the hard part.

**How badly can things break?** Users seeing wrong or stale data, cache stampedes, and "we fixed it but the cache still has the old value" for days.

---

Is there a clear caching strategy (what is cached, invalidation, consistency)?

- 1: Ad-hoc or no invalidation; stale data risk
- 10: Defined what is cached; invalidation and TTL; consistency considered

---

---
id: config-management
category: architecture
---
# Configuration Management

**What is it?** Feature toggles and environment-specific configuration (staging vs prod, feature flags) are managed outside code—e.g. env vars, config service—and not hardcoded. Changes do not require a code change for every toggle.

**Why is it important?** Hardcoded config forces redeploys for every change and makes env-specific behaviour error-prone. Feature flags enable safe rollouts.

**How badly can things break?** Wrong config in prod, no way to turn off a feature without deploy, and "we had to change code to change a flag".

---

Is configuration (feature toggles, env-specific settings) managed outside code and not hardcoded?

- 1: Config hardcoded; no feature flags or env-specific management
- 10: Config external (env, vault, config service); feature flags where needed

---

---
id: stateful-session-handling
category: architecture
---
# Stateful and Session Handling

**What is it?** If the app has stateful behaviour (sessions, affinity), it is explicit and documented: e.g. sticky sessions, shared session store (Redis, DB), or stateless tokens. Not "we don't know how sessions work" or single-instance assumption when there are many.

**Why is it important?** With multiple instances, in-memory sessions break. Users get logged out or see wrong data. Load balancers need to know if affinity is required.

**How badly can things break?** Session loss on every request, login loops, and "it works with one instance but not two". Critical for any multi-instance deploy with sessions.

---

If the app has sessions or stateful behaviour, is it explicit (sticky sessions, shared store) and documented?

- 1: Sessions in memory with multiple instances or undocumented
- 10: Shared session store or stateless tokens; behaviour documented

---

---
id: multi-tenant-isolation
category: architecture
condition: "multi_tenant_app"
---
# Multi-Tenant Isolation

**What is it?** If the app is multi-tenant, tenant data and config are isolated so one tenant cannot see or affect another. Abuse or misconfiguration in one tenant does not impact others. Only assess when the app is actually multi-tenant.

**Why is it important?** Without isolation, one tenant can access another's data (compliance and legal disaster) or overload the system for everyone.

**How badly can things break?** Data leakage between tenants, compliance failures, and noisy-neighbour outages. Only applicable to multi-tenant apps.

---

Only if the app is multi-tenant: Is tenant isolation (data, config, abuse) enforced?

- 1: No isolation; tenants can see or affect each other
- 10: Clear tenant isolation; data and access scoped; abuse contained

---

---
id: graceful-degradation
category: architecture
---
# Graceful Degradation When Dependencies Fail or Are Unavailable

**What is it?** When a critical dependency (payment provider, auth, external API, or DB) is down or slow, the app degrades gracefully—e.g. read-only mode, queue for later, or a clear message—instead of failing for everyone. For mobile: when the network is not available, the app handles offline (e.g. queue actions, show offline state, retry when back) instead of crashing or showing useless errors.

**Why is it important?** One failing dependency should not take down the whole app. Users on bad networks or during an outage should see predictable behavior, not random failures. Application updates should also be non-breaking where possible so users don't get broken flows after an update.

**How badly can things break?** One provider outage takes down the app for all users; mobile users in poor connectivity see crashes or dead screens; a bad update breaks the app for everyone.

---

When a critical dependency is down or slow (or, for mobile, when network is unavailable), does the app degrade gracefully and handle offline/retry? Are application updates non-breaking for users?

- 1: One failure breaks everyone; no offline handling; updates often break users
- 10: Graceful degradation and clear behavior; mobile handles offline; updates are non-breaking or well managed

---

---
id: circuit-breaker
category: architecture
condition: "complex_app"
---
# Circuit Breaker or Dependency Failure Handling (Complex Apps)

**What is it?** For apps with several external dependencies: when an external service is failing or very slow, the app stops hammering it (or fails fast / uses a fallback) so the rest of the app stays up for other users. Only relevant for more complex apps with multiple external calls.

**Why is it important?** Without it, one bad dependency can exhaust timeouts and threads and take down the whole app. Circuit breaker or similar patterns limit blast radius.

**How badly can things break?** One failing API brings down the entire app; cascading timeouts; all users affected. Only assess for complex apps.

---

Only if the app is complex (multiple external dependencies): When an external service is failing, do we stop hammering it or fail fast so the rest stays up?

- 1: No protection; one bad dependency can take down the app
- 10: Circuit breaker or equivalent; fail fast or fallback; rest of app stays up

---

---
id: resource-request-isolation
category: architecture
---
# Resource and Request Isolation

**What is it?** One heavy or slow request (or one abusive user) cannot tie up all threads/connections and starve others. There are limits or isolation so the app stays responsive for everyone.

**Why is it important?** Without isolation, one bad request or one power user can make the app unusable for everyone else.

**How badly can things break?** One request or user blocks the whole app; timeouts and 503s for all users when one dependency or one client misbehaves.

---

Can one heavy or abusive request/user starve others? Are there limits or isolation so the app stays responsive for everyone?

- 1: No isolation; one request or user can block everyone
- 10: Limits and isolation; app stays responsive under partial abuse or slow clients

---

---
id: bottleneck-one-slow-thing
category: architecture
---
# No Single Bottleneck That Blocks the Whole App

**What is it?** There is no one slow query, one big synchronous job, or one unthrottled operation that can block or slow the whole app for all users.

**Why is it important?** A single bottleneck (e.g. one table scan, one unthrottled export) can make the entire app slow or unresponsive. Users see timeouts or hangs.

**How badly can things break?** One slow query or job blocks all requests; the app becomes unusable for everyone until that one thing finishes or is killed.

---

Is there one slow query, one big job, or one unthrottled operation that can block or slow the whole app for users?

- 1: Yes; one bottleneck can block or slow the whole app
- 10: No single bottleneck; slow work isolated or throttled; app stays responsive
