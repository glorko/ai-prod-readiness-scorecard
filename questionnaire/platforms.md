---
id: platform-fit-for-use-case
category: platforms
condition: "app_uses_nocode_or_baas_platform"
---
# Platform Fit for Use Case (No-Code / BaaS)

**What is it?** Many vibecoders build on no-code/low-code or BaaS platforms (e.g. Lovable, Supabase, Firebase, Retool, Bubble). These are fine for the right use cases—CRUD, auth, simple workflows, MVPs. But **some tasks shouldn't be solved with them**: serious money movement or banking (need full control and auditability), strict compliance where data must stay in your infrastructure (e.g. HIPAA, certain PCI scenarios), complex multi-tenant isolation with custom rules, or high-throughput / low-latency critical paths where you need to tune everything. Using Lovable or Supabase for a simple SaaS or internal tool is often appropriate; using them for a payments ledger or regulated health data may not be.

**Why is it important?** Picking the wrong platform for the use case leads to hitting limits too late, compliance gaps, or inability to meet SLAs. The platform's sweet spot is not "everything."

**How badly can things break?** Compliance failures, "we can't do that on this platform," or scaling/performance walls. Only assess when the app actually uses such a platform.

---

If the app is built on a no-code/low-code or BaaS platform (e.g. Lovable, Supabase, Firebase): Is that platform appropriate for what the app does? (Avoid using them for: serious money movement, strict in-house compliance, complex multi-tenant rules, or high-throughput critical paths.)

- 1: Wrong platform for the use case (e.g. payments or regulated data on a platform that doesn't support it properly)
- 10: Platform fits (simple CRUD, auth, standard workflows; no high-stakes or compliance-heavy work on the wrong stack)

---

---
id: platform-limits-understood
category: platforms
condition: "app_uses_nocode_or_baas_platform"
---
# Platform Limits Understood

**What is it?** When building on a platform (Lovable, Supabase, Firebase, etc.), the team has checked the platform's limits: rate limits, quotas, SLAs, where the vendor is in control (e.g. backups, regions), and whether the app's expected load and requirements fit. Not assuming "it scales" or "it's secure" without reading the docs or checking.

**Why is it important?** Hitting undocumented or misunderstood limits in production (e.g. connection limits, row limits, API throttling) causes outages and surprise. Knowing "we're within Supabase's free tier and that's fine" or "we need Pro for this" is part of production readiness.

**How badly can things break?** Sudden throttling, quota exceeded, or "the platform doesn't support that" mid-project. Only assess when the app uses such a platform.

---

If the app uses a no-code/BaaS platform: Have the builders checked the platform's limits (rate limits, quotas, SLAs, backups) and confirmed the app's needs fit?

- 1: No idea of limits; assuming the platform handles everything
- 10: Limits and SLAs checked; app's load and requirements fit within what the platform provides

---

---
id: platform-lock-in-and-exit
category: platforms
condition: "app_uses_nocode_or_baas_platform"
---
# Platform Lock-In and Exit Path

**What is it?** Awareness that building on Lovable, Supabase, Firebase, etc. creates lock-in: data shape, auth model, and APIs are tied to the vendor. There is a rough idea of what leaving would involve (data export, migrating auth, rewriting against your own backend)—even if there's no plan to leave. Not "we're stuck forever with no idea how we'd get out."

**Why is it important?** Lock-in without awareness means no leverage in vendor negotiations and no way to plan if the platform changes pricing, discontinues a feature, or no longer fits. Knowing the exit path is part of risk management.

**How badly can things break?** Vendor change or cost spike with no migration path; data or auth trapped in a format that's hard to move. Only assess when the app uses such a platform.

---

If the app uses a no-code/BaaS platform: Is there awareness of lock-in and a rough idea of exit (data export, auth migration) if they had to leave the platform?

- 1: No awareness of lock-in; no idea how to export or migrate
- 10: Lock-in understood; data export and migration path roughly known (even if not planned)
