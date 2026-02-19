---
id: db-migrations
category: data-persistence
condition: "relational_database_used"
---
# DB Migrations

**What is it?** A way to change your database structure (tables, columns) in a controlled, step-by-step manner instead of editing it manually.

**Why is it important?** Without it, different versions of your app may expect different database shapes, and changes can overwrite or corrupt data.

**How badly can things break?** Data loss, app crashes on deploy, "column not found" errors in production, users seeing wrong or missing data.

---

Do you use any database migrations approach or have measures that prevent agent-generated code from corrupting database structure or causing inconsistencies in production?

- 1: No migrations, manual SQL, high risk of schema drift
- 10: Versioned migrations (e.g., Flyway, Alembic), CI-enforced, rollback tested

---

---
id: sql-normal-forms
category: data-persistence
condition: "relational_database_used"
---
# SQL Database Structure (Normal Forms)

**What is it?** Organizing relational database tables so data is not duplicated or inconsistent (normal forms). Each piece of information lives in one place; relationships use keys.

**Why is it important?** Denormalized or ad-hoc SQL leads to update bugs, inconsistent data, and hard-to-change schemas. Normalized structure scales with changes.

**How badly can things break?** Wrong results, duplicate or conflicting records, migrations that can't fix the mess, and "which value is the truth?" problems.

---

Does the SQL database follow normal forms and is the structure coherent (assess tables, keys, duplication)?

- 1: Ad-hoc tables, heavy duplication, no clear keys or consistency
- 10: Normalized structure, clear keys and relationships, documented

---

---
id: nosql-dto-safety
category: data-persistence
condition: "nosql_or_document_storage_used"
---
# NoSQL / Document Storage: DTO and Schema Compatibility

**What is it?** When you change the shape of objects (DTOs, models) stored in document/NoSQL DBs, existing documents already in the DB should keep working. Versioning or backward-compatible reads avoid breaking old data.

**Why is it important?** Without this, changing a field or adding a required one can break reads for existing documents or require risky big rewrites. Agent-generated code often ignores existing data.

**How badly can things break?** Crashes when reading old records, data loss on "migrations", silent wrong values, and production outages after a simple model change.

---

Do you assume or ensure that DTO/object changes do not break existing documents in the database (e.g. versioned schema, backward-compatible reads, no required fields added without defaults)?

- 1: No; model changes can break existing documents or are not considered
- 10: Yes; versioning or compatibility strategy so existing data is safe

---

---
id: db-er-documentation
category: data-persistence
---
# Database Documentation (ER Diagram or ORM Representation)

**What is it?** A visible representation of how data is structured: ER diagram, schema diagram, or at least ORM entities / models that document tables and relationships.

**Why is it important?** Without it, only "the code" knows the real structure. Onboarding and refactors are guesswork; migrations and integrations break things.

**How badly can things break?** Wrong assumptions about relationships, duplicate logic, and changes that break other parts of the app because nobody had a single picture of the data.

---

Is there an ER diagram or other representation of the database (ORM entities, schema docs) so the structure is documented?

- 1: No documentation; structure only in code or unknown
- 10: ER diagram or equivalent and/or ORM entities documented and up to date

---

---
id: backup-system
category: data-persistence
---
# Backup System for Databases and Persistent Storage

**What is it?** Regular, automated backups of all databases and any persistent storage (object store, file storage). Backups are stored safely and can be restored.

**Why is it important?** Disks fail, people delete data, and bugs corrupt data. Without backups, one incident can mean total loss.

**How badly can things break?** Permanent data loss, no recovery from ransomware or mistakes, and business failure for data-dependent apps.

---

Is there a defined backup system for all databases and persistent storages (frequency, retention, restore tested)?

- 1: No backups or ad-hoc only; restore not tested
- 10: Automated backups, retention policy, restore tested and documented

---

---
id: db-connection-management
category: data-persistence
condition: "app_opens_db_connections"
---
# Database Connection Management

**What is it?** If the app opens database connections, they are managed properly: connection pooling (or equivalent) so the app does not open a new connection per request and exhaust resources. Connections are closed or returned to the pool so the DB is not overwhelmed.

**Why is it important?** Opening a new connection per request leads to exhaustion under load, timeouts, and DB crashes. Proper pooling is standard for production.

**How badly can things break?** DB "too many connections", app timeouts under load, and cascading failures. Critical for any app that talks to a DB.

---

If the app opens DB connections, is connection management (e.g. pooling, limits, proper close/return) in place?

- 1: New connection per request or no pooling; risk of exhaustion
- 10: Connection pooling (or equivalent) with sensible limits; connections properly managed
