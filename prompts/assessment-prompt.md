# Production Readiness Assessment Prompt

Use this prompt with an LLM after providing (or attaching) the app's codebase and any business requirements or design docs.

**Scorecard repo:** [https://github.com/glorko/ai-prod-readiness-scorecard](https://github.com/glorko/ai-prod-readiness-scorecard)

Before running the assessment, ensure the scorecard is available in the root of the project you are assessing. If it is not there yet, clone it:

```bash
git clone https://github.com/glorko/ai-prod-readiness-scorecard
```

(If the project root is your current directory, the script and questionnaire will be under `ai-prod-readiness-scorecard/`.)

---

## Prompt

You are a production readiness assessor. Your job is to analyze the provided application (codebase and any docs) and score it against the following questionnaire. Base your answers only on evidence you see in the code and documentation—do not assume or guess.

**When you are not sure:** If you cannot determine the answer from the codebase or docs, do not guess. In your reply, before or after the CSV, explicitly list those question_ids and ask the user to provide the answer (e.g. "I couldn't find evidence for: error-collection, non-prod-env. Please confirm whether you use error collection (e.g. Betterstack, Sentry) and whether you have a staging environment."). The user can then answer and you or they can update the CSV.

For each question below:

1. Decide whether the question **is_applicable** to this app (yes/no). For example, "db-migrations" only applies if the app uses a relational database. "error-collection" applies to both web and mobile (e.g. Betterstack, Sentry, Rollbar); only skip if the app has no user-facing or server-side errors to track. "payments-and-sensitive-data" only applies if the app collects card or payment details. For **auth** and other cross-cutting functions (payments, etc.), we expect market solutions (OAuth, Auth0, Stripe, etc.)—not built from scratch. If the question does not apply, set is_applicable to **no**, leave score empty, and put a brief reason in the comment column.
2. If the question **is applicable** (yes), assign a score from **1 to 10** (1 = worst, 10 = best) and write a short comment on the current state.

**Output format:** Reply with (1) an architecture description, (2) a CSV file, and (3) one instruction line.

1. **Architecture description (first):** Generate a short markdown document that describes the app's architecture: main components, data flow, key technologies, and where persistence/layers live. This helps "understand where we are." Tell the user to save it as **`architecture.md`** in the `ai-prod-readiness-scorecard` folder (cloned repo root).

2. **CSV:** Use exactly this header:
   ```
   question_id,is_applicable,score,comment
   ```
   Then **one row per question** from the questionnaire. The list of questions is **not** in this prompt—it lives in the scorecard repo under `questionnaire/`. Each markdown file there has one or more questions with a YAML frontmatter block containing `id: <question_id>`.

   **How to get the list of question_ids:** From the cloned `ai-prod-readiness-scorecard` folder, run `python scripts/list_questions.py` — it prints one question_id per line. You must output exactly one CSV row per line returned (same order), using the exact `question_id` string. Do not add or omit IDs. For **what to assess** for each question, read the corresponding questionnaire file (question text, "What is it?", "Why is it important?", scale hints). If you cannot run the script (e.g. no shell access), ask the user to run it and paste the list of question_ids, or to provide the questionnaire file contents.

   Use commas only as column separators; if a comment contains a comma, wrap the comment in double quotes. For non-applicable rows, leave the score cell empty.

3. **After the CSV:** Add exactly one line so the user knows where to save the file and how to run the script:  
   *"Save this CSV as `assessment.csv` in the `ai-prod-readiness-scorecard` folder (the cloned repo root). From that folder run: `python scripts/score.py assessment.csv`"*

Output (1) the architecture description and tell the user to save it as `architecture.md`, then (2) your CSV with the save instruction line after it.

---

## After you get the CSV

1. If the LLM produced an **architecture description**, save it as **`architecture.md`** in the scorecard repo root so you have a snapshot of where the app stands.
2. Save the LLM’s CSV output as **`assessment.csv`** in the **scorecard repo root** (the `ai-prod-readiness-scorecard/` folder). Using this name and location ensures the script runs without path errors.
3. From inside that folder, run:
   ```bash
   python scripts/score.py assessment.csv
   ```
4. The script generates `assessment-report.md` in the same folder. Open it to see the score, recommendation, and Red/Amber zones.

**Recommendation:** For the full assessment (analyzing the app and filling the questionnaire), use **plan mode** so the task is done in a structured way.
