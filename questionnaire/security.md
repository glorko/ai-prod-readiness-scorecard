---
id: db-network-isolation
category: security
---
# Database and Inner Resources: Network Isolation

**What is it?** Databases and other inner resources (caches, internal services) are not exposed to the public internet. DB has no outbound internet access except, if needed, through a secured tool (e.g. admin with login) or tunnel—not open to the world.

**Why is it important?** Exposed DBs get scanned, brute-forced, and breached. Inner resources should only be reachable from the app and trusted ops; internet-facing storage is a major risk.

**How badly can things break?** Data breach, ransomware, unauthorized access, and compliance failures. One exposed DB can compromise the whole system.

---

Are databases and inner resources isolated from the public internet (no direct DB exposure; outbound from DB only via secured tool/tunnel if at all)?

- 1: DB or inner resources exposed to internet; no isolation
- 10: DB and inner resources not exposed; access only via secured path (e.g. tunnel, VPN, private network)

---

---
id: secrets-management
category: security
---
# Secrets Management

**What is it?** Storing API keys, database passwords, and other secrets outside your code—for example in environment variables or a vault—so they are never committed to the repo.

**Why is it important?** If secrets are in code, anyone with repo access (or a leaked backup) can use them. Once in git history, they are hard to remove.

**How badly can things break?** Stolen keys, breached databases, abused third-party APIs, and having to rotate every secret and redeploy after a leak.

---

Are secrets (API keys, DB credentials) stored outside code (env vars, vault)?

- 1: Secrets in code or config committed to repo
- 10: Secrets in env or vault; not in repo; rotation possible

---

---
id: auth-mechanism
category: security
---
# Auth Mechanism (Market Solution, Not From Scratch)

**What is it?** Authentication and authorization use a market solution (e.g. OAuth provider, Auth0, Cognito, Firebase Auth, Keycloak)—not built from scratch. Same principle for other cross-cutting concerns: use established solutions (payments, email, etc.) instead of custom implementations.

**Why is it important?** Custom auth is fragile and insecure: session handling, password hashing, and edge cases are easy to get wrong. Market solutions are audited and maintained. Cross-cutting functions (auth, payments) should not be reinvented.

**How badly can things break?** Unauthorized access, session hijacking, data leaks, and compliance failures. Custom auth is a critical risk.

---

Is there a defined auth mechanism using a market solution (OAuth provider, Auth0, Cognito, etc.)—not built from scratch?

- 1: No auth, hardcoded credentials, or custom-built auth from scratch
- 10: Market solution for auth (e.g. OAuth, Auth0, Cognito); no custom auth implementation

---

---
id: payments-and-sensitive-data
category: security
condition: "payment_or_card_data_collected"
---
# Payments and Sensitive Data (No Plain-Text Storage)

**What is it?** If the app collects card details or other highly sensitive payment data: use a market payment solution (Stripe, Adyen, etc.) and never store raw card numbers or full card data in your database. Tokenization and PCI-compliant flows only. Same idea for other cross-cutting functions—use market solutions, not custom storage of secrets.

**Why is it important?** Storing card details (or equivalent) in plain text in the DB is a critical hit: one breach exposes everything. PCI and regulators require no storage of raw card data; payment providers handle that.

**How badly can things break?** Storing card details in plain text in DB = 1/10 and critical: breach, regulatory fines, and loss of trust. Collecting cards via proper provider/tokenization = acceptable; never store raw cards.

---

If the app collects card details or similar payment data: are they using a market payment solution and never storing raw card data in the database?

- 1: Card details (or equivalent) collected and stored as plain text in DB — critical hit
- 5: Card data collected but via provider; check for any plain-text storage or leakage
- 10: Market payment solution (e.g. Stripe, Adyen); tokenization only; no raw card data in DB

---

---
id: input-validation
category: security
---
# Input Validation and Sanitization

**What is it?** All user and external input is validated and sanitized to prevent injection (SQL, XSS, command injection) and malformed data from reaching the app or database.

**Why is it important?** Unvalidated input is the main vector for attacks. One missing check can lead to data loss or full compromise.

**How badly can things break?** SQL injection, XSS, remote code execution, and corrupted data. Critical for any app that accepts input.

---

Is there input validation and sanitization to prevent injection (SQL, XSS, command injection)?

- 1: No systematic validation; raw input used in queries or output
- 10: Input validated and sanitized; parameterized queries; output encoding where needed

---

---
id: security-headers-cors
category: security
---
# Security Headers and CORS

**What is it?** Web/API responses use appropriate security headers (e.g. CSP, X-Frame-Options, HSTS) and CORS is configured correctly—not overly permissive (e.g. no blanket `*` in production).

**Why is it important?** Misconfigured CORS or missing headers enable cross-site attacks and data leakage. Production should not trust all origins.

**How badly can things break?** Cross-site request forgery, clickjacking, and unintended API access from malicious sites.

---

Are security headers and CORS configured correctly for web/API (no overly permissive `*` in prod)?

- 1: No security headers or CORS allows all origins in prod
- 10: Security headers in place; CORS restricted to known origins

---

---
id: rate-limiting
category: security
---
# Rate Limiting and Abuse Protection

**What is it?** Public endpoints (login, API, signup) have rate limiting or similar protection against abuse, brute force, and DDoS so a single client cannot overwhelm the app.

**Why is it important?** Without limits, attackers can brute-force passwords, scrape data, or take the app down with traffic. Cost and availability suffer.

**How badly can things break?** Service outage, account takeover, runaway costs, and abuse that is hard to stop after the fact.

---

Is there rate limiting or similar protection against abuse on public endpoints?

- 1: No rate limiting; endpoints can be hammered
- 10: Rate limiting (and/or abuse protection) on auth and critical public endpoints

---

---
id: https-tls
category: security
---
# HTTPS and TLS

**What is it?** All production traffic uses HTTPS. TLS certificates are valid and renewal (e.g. Let's Encrypt) or certificate management is in place so traffic is not sent in clear text.

**Why is it important?** Clear-text traffic can be intercepted. Expired or misconfigured certs cause browser warnings and loss of trust.

**How badly can things break?** Man-in-the-middle attacks, credential theft, and compliance failures. Users may refuse to use the app.

---

Is HTTPS enforced everywhere and is certificate renewal or TLS config managed?

- 1: HTTP in production or expired/misconfigured certs
- 10: HTTPS everywhere; cert renewal automated or managed

---

---
id: data-retention-legal
category: security
---
# Data Retention, Legal Documents, and B2B API Security

**What is it?** If the app handles PII or regulated data: (1) there is a retention and deletion policy and the app has capabilities to delete or anonymize data when required. (2) If the app is for end consumers (B2C), privacy policy, terms of service, and other required legal documents are present. (3) If the app is B2B or exposes APIs to other systems, API-to-API security and keys management (e.g. API keys, scopes, rotation) are in place.

**Why is it important?** GDPR and similar regulations require retention limits and right to deletion; missing capabilities mean legal risk. B2C apps need clear legal docs. B2B APIs need key management so partners cannot abuse or leak access.

**How badly can things break?** Fines, inability to comply with deletion requests, and partner keys leaking or being misused. Missing legal docs increase liability.

---

Does the app have data retention/deletion capabilities and policy? If B2C: are privacy policy and legal documents present? If B2B/API consumers: is API-to-API security and keys management in place?

- 1: No retention policy or capabilities; no legal docs where required; no API key management for B2B
- 10: Retention policy and deletion capabilities; legal docs for B2C; API keys and security for B2B

---

---
id: admin-panel
category: security
---
# Admin Panel for Critical Operations

**What is it?** Where applicable, the app has an admin (or support) panel that allows blocking users, modifying or viewing critical data when needed (e.g. support, compliance, abuse). This is considered in advance—not added only when an incident happens.

**Why is it important?** Without admin capabilities, you cannot quickly block an abusive user, fix bad data, or respond to legal requests. Adding it "when needed" is often too late and risky.

**How badly can things break?** Inability to stop abuse, manual DB access for every support case, and compliance or legal response delays.

---

If applicable, does the app have an admin panel (or equivalent) to block users and manage critical data when needed, considered in advance?

- 1: No admin capabilities; critical operations require direct DB or code changes
- 10: Admin/support panel with block user and critical data operations; designed in advance

---

---
id: audit-logging
category: security
---
# Audit Logging for Sensitive Operations

**What is it?** For sensitive or critical operations (e.g. auth changes, payment actions, admin actions), the app logs who did what and when so actions can be traced and investigated.

**Why is it important?** When something goes wrong or is disputed, you need an audit trail. Compliance often requires it for financial or sensitive data.

**How badly can things break?** No way to prove who did what; compliance failures; and investigations that hit a dead end.

---

Is there audit logging (who did what, when) for sensitive or critical operations?

- 1: No audit trail for critical operations
- 10: Audit logging for auth, admin, payment or other sensitive actions; queryable and retained

---

---
id: session-auth-expiry
category: security
---
# Session and Auth Expiry

**What is it?** Sessions expire in a sensible way so abandoned devices don't stay logged in forever. When a session expires or the user is logged out, there is a clear re-login flow. Token or session lifetime is appropriate to the app's risk.

**Why is it important?** Forever sessions on shared or lost devices are a security risk. Users need to understand when they're logged out and how to log back in.

**How badly can things break?** Abandoned devices with permanent access; confused users who don't know why they were logged out or how to log back in.

---

Do sessions expire appropriately, and do users get a clear re-login flow when needed?

- 1: Sessions never expire or no re-login flow; security and UX risk
- 10: Sensible session expiry; clear re-login flow; appropriate to app risk

---

---
id: no-secrets-in-user-output
category: security
---
# No Secrets in User-Visible Output

**What is it?** The app does not leak env vars, internal URLs, API keys, or other secrets in error pages, API responses, or logs that could reach users or support. Production errors are safe for external eyes.

**Why is it important?** One leaked secret in an error message can compromise the system. Support tickets and user screenshots should never contain credentials or internal paths.

**How badly can things break?** Secrets in error messages or responses; credentials exposed in logs that get shared; full compromise from one bad error path.

---

Do we avoid leaking secrets or internal details in error pages, API responses, or user-visible logs?

- 1: Secrets or internal URLs in error output or logs that can reach users
- 10: No secrets in user-visible output; errors and logs safe for external view
