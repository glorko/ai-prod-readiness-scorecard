# AI Production Readiness Scorecard

A questionnaire and scoring workflow to assess whether an app (especially one built with AI/vibecoding) is ready for production. An LLM analyzes the codebase and answers the questions; a script turns the answers into a percentage score and a Markdown report with Red/Amber zones for human review.

## How to run

**Tip:** Use **plan mode** when running the full assessment (LLM analysis + questionnaire + script), so the task is structured and repeatable.

1. **Assess the app with an LLM**
   - Open [prompts/assessment-prompt.md](prompts/assessment-prompt.md).
   - Provide the prompt to your LLM along with the app’s codebase (or key files) and any requirements/docs.
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
   - Overall score (%) and recommendation (ready / ready with risks / hire a programmer).
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
- **[scripts/score.py](scripts/score.py)** — Single script: parses CSV, computes score, writes MD report.
- **[REQUIREMENTS.md](REQUIREMENTS.md)** — Full requirements and scoring rules.

Scoring: percentage = (sum of applicable scores) / (count × 10) × 100. Thresholds: &gt;80% ready for production; 50–80% ready with risks; &lt;50% recommend hiring a programmer.
