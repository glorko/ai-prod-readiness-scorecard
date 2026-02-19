# Production Readiness for Vibe-Coders & Agentic Builders

**AI Production Readiness Scorecard** — A questionnaire and scoring workflow so **non-technical builders**, **vibe-coders**, and teams using **agentic / AI-assisted development** can see how close their app is to production—and what to fix (or who to hire) to get there.

---

## Why this exists

More and more people are **shipping apps they built with AI**: prompting, iterating with LLMs, maybe a bit of no-code, or full-on **vibe-coding** where the “engineer” is you + the agent. The app runs on your machine, looks good, and you’re proud of it. Then someone with a classic engineering background takes one look and says: *not ready for production*—no migrations, no staging, secrets in code, no observability. You feel dismissed (“it works!”); they feel they’re saving you from a time bomb. **Nobody has a shared language.**

This scorecard **bridges that gap**. It turns “is this ready?” into a concrete checklist: data, security, observability, testing, delivery, and more. You run an LLM over your app with a fixed prompt, get back a CSV of answers, and a script gives you a **percentage**, a short **estimate** (fine / okay / needs work), and **tangible recommendations**—including when it’s time to hire an engineer. Red (critical) and Amber (improve) zones make the gaps visible. The goal isn’t to shame the builder; it’s to give **vibe-coders and non-technical founders** a way to show they’ve thought about production, and give **engineers** a structured way to explain risks without just saying no. **Shared definition of “ready.”**

---

## How to run

1. **Run the assessment**
   - Use the prompt from **[prompts/assessment-prompt.md](prompts/assessment-prompt.md)** in your existing instrument (Cursor, Claude, ChatGPT, etc.). **Planning mode** is recommended so the task is structured and you can wait for the full results.
   - Give the instrument access to your app’s codebase (and this repo if it can run `scripts/list_questions.py` or read the questionnaire). Wait for the LLM to produce the CSV and (if requested) the architecture description.
   - Save the CSV (e.g. `my-assessment.csv`).

2. **Generate the report**
   ```bash
   python scripts/score.py my-assessment.csv
   ```
   This creates `my-assessment-report.md`. Custom output:
   ```bash
   python scripts/score.py my-assessment.csv -o reports/scorecard.md
   ```

3. **Review the assessment and the report**
   **Review the assessment:** some things may be missed or need extra context only a human can provide (e.g. “do we have staging?” or “where are secrets?”). Spot-check a few answers and correct the CSV if needed, then re-run the script.
   The generated `*-report.md` includes:
   - **Score (%)** and **recommendation**: short estimate (fine / okay / needs work) plus concrete next steps (fix Red/Amber, consider an engineer, or “recommend hiring an engineer before production” when score is low).
   - **Red zone** (score &lt; 4): fix before production.
   - **Amber zone** (score 4–7): plan improvements.
   - Full table and a “Not applicable” section.

**Quick test:**
```bash
python scripts/score.py examples/sample-assessment.csv
```
Then open `examples/sample-assessment-report.md`.

---

## What’s in the repo

| Path | What it is |
|------|------------|
| **[questionnaire/](questionnaire/)** | Questions by category (data, security, observability, architecture, LLM integration, …). Plain-language “What / Why / How badly” for non-technical readers. |
| **[prompts/assessment-prompt.md](prompts/assessment-prompt.md)** | Ready-to-use prompt for the LLM. |
| **[scripts/score.py](scripts/score.py)** | Parses CSV, computes score, writes the MD report. |
| **[scripts/list_questions.py](scripts/list_questions.py)** | Outputs question IDs from `questionnaire/*.md` (source of truth; prompt uses this, not a hardcoded list). |
| **[REQUIREMENTS.md](REQUIREMENTS.md)** | Full spec and scoring rules. |

Scoring: `(sum of applicable scores) / (count × 10) × 100`. Recommendations: estimate + tangible actions (e.g. light review, fix Red/Amber, hire an engineer), with bands at 80%, 60%, 40%.
