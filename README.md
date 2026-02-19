# AI Production Readiness Scorecard

A questionnaire and scoring workflow to assess whether an app (especially one built with AI/vibecoding) is ready for production. An LLM analyzes the codebase and answers the questions; a script turns the answers into a percentage score and a Markdown report with Red/Amber zones for human review.

---

## Why this exists: the conflict we're trying to solve

More and more people without a classic engineering background are building apps with AI—prompting, iterating with LLMs, and shipping something that *works* on their machine. For them the app looks fine: they designed it (often with an LLM), it runs, and they're confident. From the outside, though, people with an engineering background often see the same app and say it's **not ready for production**: no migrations, no staging, secrets in code, no observability, or a dozen other structural risks they've learned the hard way.

That creates a real conflict. The builder feels dismissed ("it works"); the engineer feels they're saving the team from a time bomb. Neither side has a shared language or evidence. "Production ready" means different things to each.

This scorecard is an attempt to **bridge that gap**. It turns "is this ready?" into a concrete set of questions (data, security, observability, testing, delivery, and more) with scores and plain-language explanations. A human runs an LLM over the app with a fixed prompt, gets back a CSV of answers, and the script produces a percentage plus a report with **red** (critical) and **amber** (needs work) zones. The goal isn't to shame the builder—it's to make the gaps visible and debatable. Both sides can look at the same report and say: "We're at 45%; here's what we're missing and why it matters." So the conversation shifts from "you don't get it" to "here's what we should fix first."

If you're a vibecoder: this gives you a checklist and a way to show you've thought about production. If you're an engineer: this gives you a structured way to explain risks without sounding like you're just saying no. If you're both: it's a shared definition of "ready" you can improve over time.

---

## How to run

**Tip:** Use **plan mode** when running the full assessment (LLM analysis + questionnaire + script), so the task is structured and repeatable.

1. **Assess the app with an LLM**
   - Open [prompts/assessment-prompt.md](prompts/assessment-prompt.md).
   - The prompt tells the LLM to get the list of questions from the **questionnaire files** in the repo (via `python scripts/list_questions.py`), not from a fixed list—so adding or changing questions in `questionnaire/` is enough; no need to edit the prompt.
   - Provide the prompt to your LLM along with the app’s codebase (or key files) and any requirements/docs. If the LLM can read the cloned scorecard repo, it can run the script or read the questionnaire `.md` files directly.
   - Copy the LLM’s CSV output and save it (e.g. `my-assessment.csv`).

2. **Generate the report**
   ```bash
   python scripts/score.py my-assessment.csv
   ```
   This creates `my-assessment-report.md` next to the CSV. You can set a custom output path with `-o`:
   ```bash
   python scripts/score.py my-assessment.csv -o reports/scorecard.md
   ```

3. **Review the report**
   Open the generated `*-report.md`. It includes:
   - Overall score (%) and recommendation: short estimate (fine / okay / needs work) plus tangible next steps (e.g. fix Red/Amber, hire an engineer).
   - **Red zone** (score &lt; 4): items that need immediate attention.
   - **Amber zone** (score 4–7): items to review and improve.
   - A full table of all items with a Zone column, and a “Not applicable” section.

**Quick test:** Run the script on the example assessment to confirm everything works:
```bash
python scripts/score.py examples/sample-assessment.csv
```
Then open `examples/sample-assessment-report.md`.

## Contents

- **[questionnaire/](questionnaire/)** — Questions by category (data, observability, environments, architecture, security), each with plain-language “What / Why / How badly” for non-technical readers.
- **[prompts/assessment-prompt.md](prompts/assessment-prompt.md)** — Ready-to-use prompt for the LLM.
- **[scripts/score.py](scripts/score.py)** — Parses CSV, computes score, writes MD report.
- **[scripts/list_questions.py](scripts/list_questions.py)** — Outputs all question IDs from `questionnaire/*.md` (source of truth for the assessment; prompt uses this, not a hardcoded list).
- **[REQUIREMENTS.md](REQUIREMENTS.md)** — Full requirements and scoring rules.

Scoring: percentage = (sum of applicable scores) / (count × 10) × 100. Recommendations: estimate (ready / fine / okay / needs work) plus tangible actions (e.g. light review, fix Red/Amber, hire an engineer).
