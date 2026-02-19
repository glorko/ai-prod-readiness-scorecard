---
id: resource-cost-awareness
category: costs
---
# Resource Cost Awareness

**What is it?** You have a basic idea of what the app costs to run: compute, database, third-party APIs, storage, and any platform (e.g. Supabase, Vercel) or LLM usage. There are simple controls to avoid runaway bills—e.g. budget alerts, spending limits, or at least checking the billing dashboard so a leak or abuse doesn't go unnoticed for weeks.

**Why is it important?** Many vibecoded apps are deployed without cost in mind. One misconfigured loop, an open API key, or a sudden traffic spike can generate a huge bill. Knowing roughly what you spend and having a basic safety net is part of production readiness.

**How badly can things break?** Surprise bills, services cut off for non-payment, or discovering too late that one feature (e.g. an LLM call per request) is costing more than the whole product makes.

---

Are you aware of the cost of resources (compute, DB, APIs, platform, LLM) and do you have basic controls (alerts, limits, or regular checks) to avoid runaway bills?

- 1: No idea of costs; no alerts or limits; first time checking is when the bill arrives
- 10: Cost awareness; budget alerts or limits in place; regular check on spend
