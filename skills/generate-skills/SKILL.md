---
name: generate-skills
description: Reads the project's living specification and dynamically discovers the stack, generating or updating the architect, backend, frontend, and tester skills. Use when requirements, architecture, tech stack, business rules, acceptance criteria, or project setup change.
---

# generate-skills

This skill reads the living documentation and the project's source code to dynamically discover the technology stack, business rules, and architecture, generating four specialized skills (architect, backend, frontend, tester) to work on the project.

## Objective
Transform the project specification into four living, updatable skills that are stack-agnostic until evidence is found.

## Execution Flow

1. **Read Specification:**
   - Look for relevant files, primarily in the `.spec/init/` folder, such as project descriptions, requirements, user stories, data models, and technical decisions.
   - The specification does not have a strict format; analyze the files that exist.

2. **Dynamic Stack Discovery (Evidence-based):**
   - Inspect repository files (e.g., `package.json`, `pom.xml`, `go.mod`, `Dockerfile`, `.yml`, etc.) and configurations (tests, builds, DB) to infer real technologies.
   - Differentiate between the "desired state" (specification) and the "current state" (code).
   - **IMPORTANT:** Do not assume any language (e.g., JS, TS, Python, Go) or framework in advance. Use only what you find with concrete evidence.

3. **Generate the Four Skills:**
   - Based on the gathered data, generate/update 4 skill files in `.agents/skills/`:
     - `<project>-architect/SKILL.md`: Focused on overall architecture.
     - `<project>-backend/SKILL.md`: Focused on backend development and database.
     - `<project>-frontend/SKILL.md`: Focused on UI development.
     - `<project>-tester/SKILL.md`: Focused on test scenarios, unit tests, and E2E.
   - Use the detected project name to name the folders. If not found, prefix with `project-`.
   - Refer to `references/output-contract.md` for the expected format.
   - **CRITICAL RULE:** All generated `SKILL.md` files must be written strictly in **English** (including headings, e.g., `## Business Rules`).

4. **Extra Specialties Analysis (Suggestions):**
   - In addition to the 4 standard skills, analyze if the project requires other specialized disciplines (e.g., `devops`, `security-auditor`, `dba`, `mobile`).
   - Do not generate these extra skills automatically. Just record your recommendations in the `suggested_skills` array within `.spec-skill-manifest.json`, providing a suggested name and reason.
   - Display these suggestions prominently in the final report, recommending the user run the `/generate-skill-suggest` command if they wish to create them.

5. **Regeneration (Regenerate Mode):**
   - Follow the rules in `references/regeneration-rules.md`.
   - Re-run the Extra Specialties Analysis (step 4), as the project stack may have evolved (e.g., a new database was added).
   - Replace ONLY the content of blocks marked with `SPEC-GENERATED`.
   - PRESERVE entirely the blocks marked with `SPEC-CUSTOM`.
   - If the markers do not exist, create a backup before updating.
   - Update only the real changes instead of rewriting the entire file.

6. **Manage Conflicts:**
   - If there is a disparity between sources (e.g., Docs say X, code uses Y), do not guess or silently modify source files.
   - Create/Record the conflict in `SPEC_CONFLICTS.md` at the project root, explain the issue, and display it at the end.

7. **Update Manifest:**
   - Maintain `.agents/skills/.spec-skill-manifest.json` following the schema in `references/manifest-schema.json`.
   - Update used sources, ignored files, missing files, the stack, and what changed.

8. **Validate Generated Files:**
   - Execute the script `scripts/validate-generated-skills.py` and verify integrity (YAML frontmatter, preserved blocks, consistency).
   - Do not finish without passing all validations successfully.

9. **Final Report:**
   - Display the detected technologies, altered/preserved files, conflicts, and git status.
   - **CRITICAL:** If any `suggested_skills` were added to the manifest, you MUST explicitly list them in your final chat response to the user, explaining why they were suggested and instructing the user to run the `/generate-skill-suggest` skill to create them.
   - **CHAT LANGUAGE RULE:** Explain your final response and chat messages in the language the user is currently writing in (e.g., Portuguese), even though you just generated all files in English.
