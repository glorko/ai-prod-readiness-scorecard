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
