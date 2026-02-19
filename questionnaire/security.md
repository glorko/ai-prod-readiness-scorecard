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
# Auth Mechanism

**What is it?** A defined way to know who a user is (login, session, or API key) instead of hardcoded passwords or no auth at all.

**Why is it important?** Without proper auth, anyone can access data or actions that should be restricted. Hardcoded or shared passwords are not real security.

**How badly can things break?** Unauthorized access, data leaks, compliance failures, and no way to revoke access or audit who did what.

---

Is there a defined auth mechanism (not hardcoded passwords)?

- 1: No auth or hardcoded credentials
- 10: Proper auth (e.g., OAuth, sessions, API keys) with no secrets in code
