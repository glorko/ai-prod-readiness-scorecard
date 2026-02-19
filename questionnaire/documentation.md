---
id: readme-local-run
category: documentation
---
# README or Local Run Instructions

**What is it?** A README or equivalent explains how to run the app locally (e.g. one command, docker-compose, required env vars) so a new contributor or reviewer can get the app running without tribal knowledge.

**Why is it important?** Without it, onboarding is slow and "works on my machine" is the only check. Reproducibility starts with "how do I run it?".

**How badly can things break?** New devs cannot run the app; debugging and contributions are blocked. Critical for collaboration.

---

Is there a README or equivalent that explains how to run the app locally?

- 1: No README or no run instructions
- 10: Clear local run instructions (e.g. one command, docker-compose); env and deps documented

---

---
id: deploy-docs
category: documentation
---
# Deployment and Release Documentation

**What is it?** Deployment and release process are documented: how to deploy, how to rollback, which environments exist, and what the pipeline does. Not tribal knowledge.

**Why is it important?** When something goes wrong, everyone needs to know how to deploy and roll back. Onboarding and incidents depend on this.

**How badly can things break?** Only one person can deploy; rollback is guesswork; new team members cannot release. Critical for operations.

---

Is deployment and release process documented (how to deploy, rollback, envs)?

- 1: No deploy docs; process in someone's head
- 10: Deploy and rollback documented; envs and pipeline described

---

---
id: changelog-release-notes
category: documentation
---
# Changelog or Release Notes

**What is it?** Changes are traceable to releases: a changelog, release notes, or commit discipline so "what changed in this release?" can be answered. Helps with support and rollback decisions.

**Why is it important?** When users report bugs or you need to roll back, you need to know what was in each release. No traceability means blind debugging.

**How badly can things break?** "We don't know what changed"; rollback and support are guesswork. Helpful for any team or future maintainer.

---

Is there a changelog or release notes (or equivalent) so changes are traceable to releases?

- 1: No changelog or release notes; no traceability
- 10: Changelog or release notes; or clear convention (e.g. tagged releases with summaries)
