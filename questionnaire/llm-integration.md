---
id: prompt-management
category: llm-integration
condition: "app_uses_llm"
---
# Prompt Management (LLM Integration)

**What is it?** When the app uses an LLM (e.g. for chat, generation, or classification), prompts are managed in a structured way: not scattered and hardcoded in code, but versioned, testable, and changeable without a full deploy. There is a single place or process to update prompts and to see what changed (e.g. prompt registry, config, or at least a dedicated file that's reviewed).

**Why is it important?** Prompts are the "logic" of LLM features. Hardcoded prompts in code are hard to tune, A/B test, or roll back. Changing a prompt should not require a code release; bad prompts should be fixable quickly.

**How badly can things break?** A broken or outdated prompt ships with every release; no way to fix or roll back without redeploying. Only assess when the app actually uses an LLM.

---

If the app uses an LLM: Are prompts managed (versioned, testable, not hardcoded everywhere) so changes are traceable and can be updated without a full code deploy?

- 1: Prompts hardcoded and scattered; no way to change without code change
- 10: Prompts in a dedicated place or registry; versioned and testable; can update without full deploy

---

---
id: token-cost-management
category: llm-integration
condition: "app_uses_llm"
---
# Token and Cost Management (LLM Integration)

**What is it?** When the app calls an LLM API, token usage and cost are considered: context length is bounded (e.g. not sending the whole database every time), caching is used where it makes sense (e.g. same prompt + inputs), and model choice reflects cost vs capability (e.g. not using the most expensive model for simple tasks). There is at least basic visibility (logs, dashboard, or budget) so token spend doesn't explode unnoticed.

**Why is it important?** LLM APIs are billed per token. Unbounded context, no caching, or "use the biggest model for everything" leads to bills that scale with usage in unpleasant ways. Token cost management is as important as any other resource cost.

**How badly can things break?** Runaway API bills, rate limits hit in production, or the app becoming uneconomic at scale. Only assess when the app uses an LLM.

---

If the app uses an LLM: Is token usage and cost managed (context limits, caching where appropriate, model choice, visibility or budget on spend)?

- 1: No consideration; unbounded context; no caching; no visibility on token spend
- 10: Context bounded; caching where useful; model choice by cost/capability; spend visible or budgeted

---

---
id: llm-output-validation
category: llm-integration
condition: "app_uses_llm"
---
# LLM Output Validation and Safety

**What is it?** When the app uses an LLM, the output is not trusted blindly: it is validated, sanitized, or constrained (e.g. structured output format, allowlists, length limits) so that bad or unexpected output doesn't break the app, leak data, or confuse users. There is a clear path for "what if the LLM returns garbage" (retry, fallback, or safe error).

**Why is it important?** LLMs are non-deterministic. They can hallucinate, return off-format data, or include unsafe content. Feeding raw LLM output into the rest of the app or straight to users is a reliability and safety risk.

**How badly can things break?** Crashes from malformed output, injection or prompt leakage, or users seeing inappropriate or wrong content. Only assess when the app uses an LLM.

---

If the app uses an LLM: Is output validated or constrained (e.g. structured output, sanitization, fallback on failure) so bad output doesn't break the app or reach users unsafely?

- 1: Raw LLM output used; no validation or fallback
- 10: Output validated or structured; fallback or safe error when output is bad or unexpected
