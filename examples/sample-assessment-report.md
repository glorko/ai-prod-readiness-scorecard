# Production Readiness Scorecard Report

Generated: 2026-02-19 09:32 UTC

## Overall

- **Score:** 54.2%
- **Recommendation:** Ready with risks — read report and consider improvements

## Red zone (score &lt; 4)

Items that need immediate attention:

| Question ID | Score | Comment |
|-------------|-------|---------|
| db-migrations | 3 | No migrations; schema changes done manually in prod |
| db-er-documentation | 2 | Only ORM entities; no ER diagram |
| admin-panel | 3 | No admin UI; DB access for support |
| audit-logging | 3 | Only auth events logged; no admin audit trail |
| centralized-logging | 2 | Only console.log and local files |
| non-prod-env | 2 | Only prod and local; no staging |
| rollback-approach | 3 | Manual redeploy of previous image; not documented |
| feature-flags-rollouts | 3 | No feature flags; full deploy per change |
| changelog-release-notes | 3 | Tagged releases; no changelog |


## Amber zone (score 4–7)

Items to review and improve:

| Question ID | Score | Comment |
|-------------|-------|---------|
| sql-normal-forms | 5 | Some normalization; a few redundant columns |
| backup-system | 4 | Weekly backups; restore not tested recently |
| db-network-isolation | 7 | DB in private subnet; admin via tunnel |
| secrets-management | 5 | Some in env; one key still in config |
| auth-mechanism | 7 | JWT in place; no hardcoded passwords |
| input-validation | 6 | Validation on API inputs; some paths could be stricter |
| security-headers-cors | 5 | CORS restricted; some security headers missing |
| rate-limiting | 4 | Basic rate limit on login only |
| data-retention-legal | 4 | No formal retention policy; B2B API keys in use |
| session-auth-expiry | 6 | JWT expiry set; refresh flow in place |
| resource-cost-awareness | 5 | Basic cloud billing alerts; no formal budget |
| health-readiness-endpoints | 6 | /health and /ready; ready does not check DB |
| monitoring-alerting | 4 | Metrics in place; no alerting configured |
| user-facing-errors-and-logging | 6 | Safe API error responses; logging to stdout |
| environment-description | 5 | README has basic stack; no full env spec |
| backend-tech-applicability | 6 | Go backend; some critical paths could be stricter |
| timeouts-considered | 7 | Timeouts on HTTP client and DB; one external call unbounded |
| idempotency-critical-ops | 5 | Idempotency keys on payment path; not on all critical ops |
| caching-strategy | 6 | Cache for session; TTL set; invalidation on logout |
| config-management | 6 | Env vars for config; no feature flags |
| graceful-degradation | 5 | Timeouts on external calls; no offline handling (API only) |
| resource-request-isolation | 6 | Connection limits; no per-request isolation |
| bottleneck-one-slow-thing | 7 | No single blocking query; one export could be throttled |
| regression-testing | 4 | Unit tests for core; no e2e or integration suite |
| code-reusability | 5 | Some shared components; some copy-paste |
| libraries-stable | 7 | Go modules; mostly current |
| dependency-scanning | 6 | Dependabot enabled; not blocking |
| static-analysis-lint-ci | 7 | golangci-lint in CI; blocks on failure |
| code-review | 6 | AI-assisted PR review; solo dev |
| cicd-pipeline | 5 | GitHub Actions build and test; manual prod deploy |
| deploy-repeatable-automated | 6 | Scripted deploy; some manual steps |
| readme-local-run | 7 | README with docker-compose and env vars |
| deploy-docs | 4 | Deploy steps in wiki; not in repo |
| git-usage | 6 | Single repo; main branch only; no formal strategy |


## All items

| Question ID | Applicable | Score | Zone | Comment |
|-------------|------------|-------|------|---------|
| db-migrations | yes | 3 | Red | No migrations; schema changes done manually in prod |
| sql-normal-forms | yes | 5 | Amber | Some normalization; a few redundant columns |
| nosql-dto-safety | no |  | N/A | Relational DB only; no document store |
| db-er-documentation | yes | 2 | Red | Only ORM entities; no ER diagram |
| backup-system | yes | 4 | Amber | Weekly backups; restore not tested recently |
| db-connection-management | yes | 8 | OK | Connection pooling in use; limits set |
| db-network-isolation | yes | 7 | Amber | DB in private subnet; admin via tunnel |
| secrets-management | yes | 5 | Amber | Some in env; one key still in config |
| auth-mechanism | yes | 7 | Amber | JWT in place; no hardcoded passwords |
| payments-and-sensitive-data | no |  | N/A | No payment or card data collected |
| input-validation | yes | 6 | Amber | Validation on API inputs; some paths could be stricter |
| security-headers-cors | yes | 5 | Amber | CORS restricted; some security headers missing |
| rate-limiting | yes | 4 | Amber | Basic rate limit on login only |
| https-tls | yes | 8 | OK | HTTPS in prod; cert auto-renewal |
| data-retention-legal | yes | 4 | Amber | No formal retention policy; B2B API keys in use |
| admin-panel | yes | 3 | Red | No admin UI; DB access for support |
| audit-logging | yes | 3 | Red | Only auth events logged; no admin audit trail |
| session-auth-expiry | yes | 6 | Amber | JWT expiry set; refresh flow in place |
| no-secrets-in-user-output | yes | 8 | OK | No secrets in API responses; env not in errors |
| api-contract | no |  | N/A | Simple API; 2 controllers; contract would be overkill |
| api-versioning | no |  | N/A | Simple API; no versioning yet |
| platform-fit-for-use-case | no |  | N/A | Custom Go backend; no no-code/BaaS platform |
| platform-limits-understood | no |  | N/A | Custom backend; not using Lovable/Supabase etc |
| platform-lock-in-and-exit | no |  | N/A | No vendor platform in use |
| resource-cost-awareness | yes | 5 | Amber | Basic cloud billing alerts; no formal budget |
| prompt-management | no |  | N/A | No LLM in this app |
| token-cost-management | no |  | N/A | No LLM in this app |
| llm-output-validation | no |  | N/A | No LLM in this app |
| centralized-logging | yes | 2 | Red | Only console.log and local files |
| error-collection | no |  | N/A | Backend-only API; no client-side error tracking |
| health-readiness-endpoints | yes | 6 | Amber | /health and /ready; ready does not check DB |
| monitoring-alerting | yes | 4 | Amber | Metrics in place; no alerting configured |
| user-facing-errors-and-logging | yes | 6 | Amber | Safe API error responses; logging to stdout |
| non-prod-env | yes | 2 | Red | Only prod and local; no staging |
| rollback-approach | yes | 3 | Red | Manual redeploy of previous image; not documented |
| environment-description | yes | 5 | Amber | README has basic stack; no full env spec |
| microservices-scale | yes | 9 | OK | Monolith; ~50 users; appropriate |
| backend-tech-applicability | yes | 6 | Amber | Go backend; some critical paths could be stricter |
| timeouts-considered | yes | 7 | Amber | Timeouts on HTTP client and DB; one external call unbounded |
| idempotency-critical-ops | yes | 5 | Amber | Idempotency keys on payment path; not on all critical ops |
| caching-strategy | yes | 6 | Amber | Cache for session; TTL set; invalidation on logout |
| config-management | yes | 6 | Amber | Env vars for config; no feature flags |
| stateful-session-handling | yes | 8 | OK | Stateless JWT; no sticky sessions needed |
| multi-tenant-isolation | no |  | N/A | Single-tenant app |
| graceful-degradation | yes | 5 | Amber | Timeouts on external calls; no offline handling (API only) |
| circuit-breaker | no |  | N/A | Simple app; not many external deps |
| resource-request-isolation | yes | 6 | Amber | Connection limits; no per-request isolation |
| bottleneck-one-slow-thing | yes | 7 | Amber | No single blocking query; one export could be throttled |
| regression-testing | yes | 4 | Amber | Unit tests for core; no e2e or integration suite |
| code-reusability | yes | 5 | Amber | Some shared components; some copy-paste |
| libraries-stable | yes | 7 | Amber | Go modules; mostly current |
| libraries-standard-practice | yes | 8 | OK | Standard lib and known deps; one custom helper |
| no-oversized-files | yes | 8 | OK | Max file ~600 LOC; no files over 1000 |
| dependency-scanning | yes | 6 | Amber | Dependabot enabled; not blocking |
| static-analysis-lint-ci | yes | 7 | Amber | golangci-lint in CI; blocks on failure |
| code-review | yes | 6 | Amber | AI-assisted PR review; solo dev |
| cicd-pipeline | yes | 5 | Amber | GitHub Actions build and test; manual prod deploy |
| feature-flags-rollouts | yes | 3 | Red | No feature flags; full deploy per change |
| deploy-repeatable-automated | yes | 6 | Amber | Scripted deploy; some manual steps |
| background-jobs-configured | no |  | N/A | No background jobs; sync only |
| readme-local-run | yes | 7 | Amber | README with docker-compose and env vars |
| deploy-docs | yes | 4 | Amber | Deploy steps in wiki; not in repo |
| changelog-release-notes | yes | 3 | Red | Tagged releases; no changelog |
| ui-design-consistency | no |  | N/A | No UI; API only |
| git-usage | yes | 6 | Amber | Single repo; main branch only; no formal strategy |

## Not applicable

These items were excluded from scoring:

| Question ID | Reason |
|-------------|--------|
| nosql-dto-safety | Relational DB only; no document store |
| payments-and-sensitive-data | No payment or card data collected |
| api-contract | Simple API; 2 controllers; contract would be overkill |
| api-versioning | Simple API; no versioning yet |
| platform-fit-for-use-case | Custom Go backend; no no-code/BaaS platform |
| platform-limits-understood | Custom backend; not using Lovable/Supabase etc |
| platform-lock-in-and-exit | No vendor platform in use |
| prompt-management | No LLM in this app |
| token-cost-management | No LLM in this app |
| llm-output-validation | No LLM in this app |
| error-collection | Backend-only API; no client-side error tracking |
| multi-tenant-isolation | Single-tenant app |
| circuit-breaker | Simple app; not many external deps |
| background-jobs-configured | No background jobs; sync only |
| ui-design-consistency | No UI; API only |
