# AI Production Readiness Scorecard — Requirements Document

## 1. Problem Statement

**Context:** Non-technical "vibecoders" (people building apps with AI/LLM assistance) often ship applications that appear to work but lack production-grade foundations. This creates friction with engineering teams who see structural risks (data integrity, observability, scalability, security) that vibecoders don't recognize.

**Goal:** Provide a structured, score-based questionnaire that:
- Guides an LLM-assisted review of an app's codebase and docs
- Produces a **maturity score** as percentage (0–100%) with a clear recommendation
- Makes gaps explicit so both sides can align on what "production ready" means

---

## 2. Core Concepts

| Term | Definition |
|------|------------|
| **Scorecard** | The full questionnaire with all questions, conditions, and scoring rules |
| **Assessment** | One run of the questionnaire for a specific app |
| **Applicable question** | A question that applies to the app (e.g., DB migrations only if a relational DB exists) |
| **N/A question** | A question that does not apply; excluded from scoring |
| **Maturity score** | Percentage: sum of applicable scores ÷ (count × 10) × 100 |

---

## 3. Functional Requirements

### 3.1 Questionnaire Content

- **Format:** Markdown file(s) with clear structure
- **Per question:**
  - Unique ID (for parsing and referencing)
  - Question text (human-readable)
  - **Plain-language description** (for non-technical readers):
    - *What is it?* — Simple explanation of the concept
    - *Why is it important?* — Business/risk rationale
    - *How badly can things break without it?* — Consequence of neglect
  - Optional **condition** (when the question applies)
  - Scoring scale: 1 (worst) to 10 (best)
  - Optional guidance for the LLM on how to interpret 1 vs 10

- **Question categories** (examples):
  - Data & persistence (migrations, backups, schema integrity)
  - Observability (logging, error collection, monitoring)
  - Environments (dev/staging vs prod)
  - Architecture (avoiding over-engineering, e.g., no microservices for 100 users)
  - Security (auth, secrets, input validation)
  - Testing & CI/CD
  - Documentation & runbooks

### 3.2 Conditional Logic

- Some questions apply only when certain conditions are met
- Examples:
  - "Do you use database migrations?" → only if relational DB is used
  - "Do you use Sentry/equivalent?" → only if mobile app or client-side errors matter
- **N/A handling:** If a question does not apply, it is excluded from the final score calculation

### 3.3 LLM-Assisted Assessment Flow

1. **Input:** Human provides (or LLM has access to):
   - App codebase (or key files)
   - Business requirements / design docs (if any)

2. **Process:** Human uses a predefined prompt that:
   - Instructs the LLM to analyze the app
   - Lists all questions from the questionnaire
   - Asks the LLM to answer each applicable question with:
     - **is_applicable** (yes/no)
   - **Score** (1–10 when applicable)
   - **Short comment** (1–2 sentences on current state, or reason when not applicable)

3. **Output:** LLM produces a CSV file in predefined format that a script can parse

### 3.4 Scoring Script (single file)

- **Input:** CSV file (assessment results in predefined format)
- **Output:**
  - **MD report** for human review (primary output)
  - Report includes: final maturity score (%), recommendation, per-question scores and comments, non-applicable items (with reasons), optional category breakdown

---

## 4. Non-Functional Requirements

- Questionnaire and template should be **human-editable** (Markdown, YAML, or similar)
- Script should be **deterministic** and **idempotent** for the same input
- LLM output format must be **unambiguous** and easy to parse (no free-form prose for scores)
- Repo should be usable without heavy tooling (e.g., Python or Node script, no complex infra)

---

## 5. Proposed Structure

### 5.1 Repository Layout

```
ai-prod-readiness-scorecard/
├── REQUIREMENTS.md           # This document
├── README.md                 # Usage, flow, how to run
├── questionnaire/
│   ├── index.md              # Main questionnaire (or index of categories)
│   ├── data-persistence.md   # DB, migrations, backups
│   ├── observability.md      # Logging, errors, monitoring
│   ├── environments.md       # Dev/staging/prod
│   ├── architecture.md       # Over-engineering, scale fit
│   └── ...                   # Other categories
├── prompts/
│   └── assessment-prompt.md  # Predefined prompt for LLM
├── templates/
│   └── assessment-template.csv # Empty CSV template for LLM to fill
├── scripts/
│   └── score.py              # Parse CSV, compute score, generate MD report
└── examples/
    └── sample-assessment.csv # Example assessment output for testing
```

### 5.2 Questionnaire Storage Format

**Option A: Single Markdown with frontmatter (YAML)**

```yaml
---
id: db-migrations
category: data-persistence
condition: "relational_database_used"
---
# DB Migrations

**What is it?** A way to change your database structure (tables, columns) in a 
controlled, step-by-step manner instead of editing it manually.

**Why is it important?** Without it, different versions of your app may expect 
different database shapes, and changes can overwrite or corrupt data.

**How badly can things break?** Data loss, app crashes on deploy, "column not found" 
errors in production, users seeing wrong or missing data.

---

Do you use any database migrations approach or have measures that prevent 
agent-generated code from corrupting database structure or causing 
inconsistencies in production?

- 1: No migrations, manual SQL, high risk of schema drift
- 10: Versioned migrations (e.g., Flyway, Alembic), CI-enforced, rollback tested
```

**Option B: Structured YAML/JSON for questions, MD for human reading**

```yaml
# questions.yaml
questions:
  - id: db-migrations
    category: data-persistence
    condition: relational_database_used
    text: "Do you use any database migrations approach..."
    what_is_it: "A way to change your database structure in a controlled manner"
    why_important: "Without it, different app versions may expect different DB shapes"
    how_bad_without: "Data loss, crashes on deploy, column not found errors"
    scale_low: "No migrations, manual SQL"
    scale_high: "Versioned migrations, CI-enforced"
```

**Recommendation:** Use **Option A** (MD + YAML frontmatter) for:
- Easy editing and reading
- Single source of truth
- Simple extraction of `id`, `condition`, `text` for prompt building and parsing

### 5.3 Assessment Output Format (CSV)

**Target:** CSV — simple to parse (built-in Python `csv` module), portable (Excel, Sheets), and easy for LLMs to generate consistently.

**Schema:**

| Column          | Description                          | Values                    |
|-----------------|--------------------------------------|---------------------------|
| `question_id`   | Unique question identifier           | e.g. `db-migrations`      |
| `is_applicable` | Whether the question applies         | `yes` or `no`             |
| `score`         | Numeric score (only when applicable) | 1–10                      |
| `comment`       | Short explanation or N/A reason       | Free text (comma-safe)     |

**Example:**

```csv
question_id,is_applicable,score,comment
db-migrations,yes,3,No migrations; schema changes done manually in prod
centralized-logging,yes,7,Structured logging; no aggregation yet
non-prod-env,yes,2,Only prod and local; no staging
microservices-scale,yes,9,Monolith; ~50 users; appropriate
mobile-error-tracking,no,,Web app only; no mobile
```

**Applicability:** Rows with `is_applicable` = `no` are excluded from scoring. `score` can be empty for non-applicable rows; `comment` holds the reason.

**Notes:** Use proper CSV quoting for comments containing commas or newlines. The prompt should provide this exact header row and require the LLM to output valid CSV.

### 5.4 Prompt Design

The assessment prompt should:

1. **Context:** Explain the goal (production readiness scorecard)
2. **Input:** Describe what the LLM will analyze (codebase, docs)
3. **Instructions:**
   - Go through each question
   - For each: set `is_applicable` (yes/no) based on conditions
   - If applicable: assign score 1–10 + short comment
   - If not applicable: set `is_applicable` = no, leave score empty, put reason in comment
4. **Output format:** Provide exact CSV template (header + row format) for the LLM to fill
5. **Tone:** Be objective; base answers on evidence from the codebase/docs

---

## 6. Example Questions (Draft)

Each question in the questionnaire must include the plain-language block (What / Why / How badly).

| ID | Category | Condition | Question |
|----|----------|-----------|----------|
| `db-migrations` | data-persistence | `relational_database_used` | Do you use migrations or measures to prevent schema corruption / inconsistencies in production? |
| `centralized-logging` | observability | — | Do you have centralized logging (e.g., CloudWatch, Datadog, ELK)? |
| `error-collection` | observability | — | Do you have error collection (e.g., Sentry for mobile/web)? |
| `non-prod-env` | environments | — | Do you have at least one non-prod environment (staging, dev) besides local? |
| `microservices-scale` | architecture | — | For an app with ~100 users, are you avoiding microservices (i.e., not over-engineered)? |
| `secrets-management` | security | — | Are secrets (API keys, DB credentials) stored outside code (env vars, vault)? |
| `auth-mechanism` | security | — | Is there a defined auth mechanism (not hardcoded passwords)? |

*(More questions to be added in the questionnaire files.)*

---

## 7. Scoring Logic

- **Per question:** 1–10 (only when `is_applicable` = yes)
- **Non-applicable:** Excluded from calculation
- **Formula:** `percent = (sum of applicable scores) / (count of applicable × 10) × 100`
  - Example: 5 applicable questions, sum = 32 → 32 / 50 × 100 = **64%**

### 7.1 Recommendation Thresholds

| Score | Recommendation |
|-------|-----------------|
| **>80%** | Ready for production |
| **50–80%** | Ready with risks — recommended to read output and consider improvements |
| **<50%** | Recommend hiring a programmer before production |

---

## 8. Open Decisions

1. **Weights:** Start unweighted; add weights if needed
2. **Condition evaluation:** Who decides if a condition is met?
   - Option A: LLM decides during assessment (simpler)
   - Option B: Separate "context" step that fills conditions (e.g., `relational_database_used: true`)
3. **Versioning:** Should questionnaire versions be tracked for reproducibility?
4. **Multi-language:** Script in Python vs Node? (Python suggested for simplicity; CSV parsing is built-in)

---

## 9. Success Criteria

- [ ] Questionnaire with 15–25 questions across key categories (each with plain-language What/Why/How badly)
- [ ] Clear conditional logic and N/A handling
- [ ] Single assessment prompt that produces CSV output
- [ ] Single script that parses CSV, computes score, and generates MD report for human review
- [ ] Example assessment for testing
- [ ] README with end-to-end flow for a human + LLM

---

## 10. Out of Scope (for now)

- Web UI for the scorecard
- Integration with specific LLM APIs (human copies prompt + output)
- Automated codebase analysis (human provides context)
- Historical tracking / dashboards
