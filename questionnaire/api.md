---
id: api-contract
category: api
condition: "api_heavy_or_many_endpoints"
---
# API Contract (OpenAPI/Swagger)

**What is it?** For API-heavy apps (many endpoints, external API consumers), there is a formal API contract (e.g. OpenAPI/Swagger) that describes endpoints, request/response shapes, and is kept in sync with the implementation. Not required for simple SaaS with only a few controllers—that may be overkill.

**Why is it important?** When many clients depend on the API, a contract prevents breaking changes and enables codegen and testing. For 2–3 controllers it can be overengineering.

**How badly can things break?** Breaking changes for API consumers, no single source of truth, and integration bugs. Only assess for API-heavy apps.

---

Only if the app is API-heavy (many endpoints or external API consumers): Is there an API contract (e.g. OpenAPI/Swagger) kept in sync with the implementation?

- 1: No contract or severely out of sync
- 10: OpenAPI or equivalent; updated with code; used for docs or codegen

---

---
id: api-versioning
category: api
condition: "api_heavy_or_many_endpoints"
---
# API Versioning

**What is it?** For API-heavy apps, there is a versioning strategy (e.g. URL path, header) so that changes do not break existing clients. New behaviour can be added without forcing all consumers to change at once.

**Why is it important?** Without versioning, any change can break integrators. With many API consumers, backward compatibility is critical.

**How badly can things break?** Breaking changes that take down all API consumers; no way to evolve the API safely. Only assess for API-heavy apps.

---

Only if the app is API-heavy: Is there an API versioning strategy so clients do not break on changes?

- 1: No versioning; any change can break consumers
- 10: Clear versioning (URL or header); backward compatibility considered
