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

For each question below:

1. Decide whether the question **is_applicable** to this app (yes/no). For example, "db-migrations" only applies if the app uses a relational database; "error-collection" for a backend-only API might be less relevant than for a mobile app. If the question does not apply, set is_applicable to **no**, leave score empty, and put a brief reason in the comment column.
2. If the question **is applicable** (yes), assign a score from **1 to 10** (1 = worst, 10 = best) and write a short comment on the current state.

**Output format:** Reply with a CSV file and one instruction line after it.

1. **CSV:** Use exactly this header:
   ```
   question_id,is_applicable,score,comment
   ```
   Then one row per question_id. Use commas only as column separators; if a comment contains a comma, wrap the comment in double quotes. For non-applicable rows, leave the score cell empty.

2. **After the CSV:** Add exactly one line so the user knows where to save the file and how to run the script:  
   *"Save this CSV as `assessment.csv` in the `ai-prod-readiness-scorecard` folder (the cloned repo root). From that folder run: `python scripts/score.py assessment.csv`"*

**Question IDs and what to assess:**

| question_id | What to assess |
|-------------|----------------|
| db-migrations | Only if the app uses a relational DB: Do they use migrations or measures to prevent schema corruption/inconsistencies in production? |
| centralized-logging | Do they have centralized logging (e.g., CloudWatch, Datadog, ELK)? |
| error-collection | Do they have error collection (e.g., Sentry for mobile/web or equivalent for backend)? |
| non-prod-env | Do they have at least one non-prod environment (staging, dev) besides local? |
| microservices-scale | For ~100 users or similar small scale: Are they avoiding microservices (not over-engineered)? |
| secrets-management | Are secrets (API keys, DB credentials) stored outside code (env vars, vault)? |
| auth-mechanism | Is there a defined auth mechanism (not hardcoded passwords)? |

Output your CSV (with the save instruction line after it) now.

---

## After you get the CSV

1. Save the LLM’s CSV output as **`assessment.csv`** in the **scorecard repo root** (the `ai-prod-readiness-scorecard/` folder). Using this name and location ensures the script runs without path errors.
2. From inside that folder, run:
   ```bash
   python scripts/score.py assessment.csv
   ```
3. The script generates `assessment-report.md` in the same folder. Open it to see the score, recommendation, and Red/Amber zones.

**Recommendation:** For the full assessment (analyzing the app and filling the questionnaire), use **plan mode** so the task is done in a structured way.
