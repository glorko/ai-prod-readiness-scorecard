# AI Production Readiness Scorecard — Questionnaire

Use this questionnaire with an LLM to assess whether an app is ready for production. Each category has questions with plain-language explanations for non-technical readers.

## Categories and question IDs

| Category | File | Question IDs |
|----------|------|--------------|
| Data & persistence | [data-persistence.md](data-persistence.md) | `db-migrations`, `sql-normal-forms`, `nosql-dto-safety`, `db-er-documentation`, `backup-system`, `db-connection-management` |
| Security | [security.md](security.md) | `db-network-isolation`, `secrets-management`, `auth-mechanism`, `payments-and-sensitive-data`, `input-validation`, `security-headers-cors`, `rate-limiting`, `https-tls`, `data-retention-legal`, `admin-panel`, `audit-logging`, `session-auth-expiry`, `no-secrets-in-user-output` |
| API | [api.md](api.md) | `api-contract`, `api-versioning` |
| Platforms (no-code / BaaS) | [platforms.md](platforms.md) | `platform-fit-for-use-case`, `platform-limits-understood`, `platform-lock-in-and-exit` |
| Costs | [costs.md](costs.md) | `resource-cost-awareness` |
| LLM integration | [llm-integration.md](llm-integration.md) | `prompt-management`, `token-cost-management`, `llm-output-validation` |
| Observability | [observability.md](observability.md) | `centralized-logging`, `error-collection`, `health-readiness-endpoints`, `monitoring-alerting`, `user-facing-errors-and-logging` |
| Environments | [environments.md](environments.md) | `non-prod-env`, `rollback-approach`, `environment-description` |
| Architecture | [architecture.md](architecture.md) | `microservices-scale`, `backend-tech-applicability`, `timeouts-considered`, `idempotency-critical-ops`, `caching-strategy`, `config-management`, `stateful-session-handling`, `multi-tenant-isolation`, `graceful-degradation`, `circuit-breaker`, `resource-request-isolation`, `bottleneck-one-slow-thing` |
| Testing | [testing.md](testing.md) | `regression-testing` |
| Code quality | [code-quality.md](code-quality.md) | `code-reusability`, `libraries-stable`, `libraries-standard-practice`, `no-oversized-files`, `dependency-scanning`, `static-analysis-lint-ci`, `code-review` |
| Delivery | [delivery.md](delivery.md) | `cicd-pipeline`, `feature-flags-rollouts`, `deploy-repeatable-automated`, `background-jobs-configured` |
| Documentation | [documentation.md](documentation.md) | `readme-local-run`, `deploy-docs`, `changelog-release-notes` |
| Frontend | [frontend.md](frontend.md) | `ui-design-consistency` |
| Tooling | [tooling.md](tooling.md) | `git-usage` |

Open the category files for full question text, scale hints, and "What / Why / How badly" descriptions.
