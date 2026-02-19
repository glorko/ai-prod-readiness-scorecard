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
