---
name: generate-skills
description: Reads the project's living specification and dynamically discovers the stack, generating or updating the architect, security, tester, backend, and frontend skills. Use when requirements, architecture, tech stack, business rules, acceptance criteria, or project setup change.
---

# generate-skills

This skill reads the living documentation and the project's source code to dynamically discover the technology stack, business rules, and architecture, generating specialized skills (architect, tester, security, backend, frontend) to work on the project.

## Objective
Transform the project specification into living, updatable skills that are stack-agnostic until evidence is found.

## Execution Flow

1. **Read Specification or Fallback (Legacy Mode):**
   - **Spec-Driven Mode:** First, look for formal specification files in the `.spec/init/` folder (such as project descriptions, user stories, and data models).
   - **Code-Driven Mode (Fallback):** If the `.spec/init/` folder does not exist or is empty, DO NOT stop. Assume the project is a legacy or undocumented codebase. Perform reverse engineering by deeply analyzing the root `README.md`, package configs, directory structures (e.g., `src/domain`, `src/controllers`), and key source files to infer the project's purpose, architecture, and implicit business rules.

2. **Dynamic Stack Discovery (Evidence-based):**
   - Inspect repository files (e.g., `package.json`, `pom.xml`, `go.mod`, `Dockerfile`, `.yml`, etc.) and configurations (tests, builds, DB) to infer real technologies.
   - If specifications exist, differentiate between the "desired state" (specs) and the "current state" (code).
   - If in Code-Driven Mode, rely entirely on the discovered stack and codebase structure.
   - **IMPORTANT:** Do not assume any language (e.g., JS, TS, Python, Go) or framework in advance. Use only what you find with concrete evidence.

3. **Generate Core Skills Conditionally:**
   - Based on the gathered data, generate/update up to 5 skill files in `.agents/skills/`:
     - `<project>-architect/SKILL.md`: (Always generate) Focused on overall architecture.
     - `<project>-tester/SKILL.md`: (Always generate) Focused on test scenarios, unit tests, and E2E.
     - `<project>-security/SKILL.md`: (Always generate) Focused on application security, OWASP Top 10 prevention, secrets management, input sanitization, legacy protection rules (do not refactor unrequested legacy, flag and warn), and detected security audit commands.
     - `<project>-backend/SKILL.md`: (Generate ONLY if backend evidence is found, e.g., APIs, databases, backend languages/frameworks).
     - `<project>-frontend/SKILL.md`: (Generate ONLY if frontend evidence is found, e.g., UI code, React, Vue, HTML/CSS).
   - If a skill is not applicable (e.g., a pure API project with no UI), do NOT create its folder or skill file.
   - Use the detected project name to name the folders. If not found, prefix with `project-`.
   - Refer to `references/output-contract.md` for the expected format.
   - **CRITICAL RULE:** All generated `SKILL.md` files must be written strictly in **English** (including headings, e.g., `## Business Rules`).

4. **Extra Specialties Analysis (Suggestions):**
   - In addition to the standard skills, analyze if the project requires other specialized disciplines (e.g., `devops`, `dba`, `mobile`, `cloud-architect`, `performance-engineer`).
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
   - **CRITICAL:** Do NOT leave the `.spec-skill-manifest.json` data hidden in the background! You MUST output a detailed Markdown summary of the manifest contents in your final chat response.
   - Include the **Detected Stack**, the **Sources** used, and a list of all **Changes** (files added/altered/preserved) and **Conflicts** (if any).
   - If any `suggested_skills` were added to the manifest, you MUST explicitly list them, explaining why they were suggested, and instruct the user to run the `/generate-skill-suggest` skill to create them.
   - **NO AUTOMATIC COMMITS:** Do NOT automatically run `git commit` or `git push`. Leave the files in the working directory. In your final report, ask the user if they want you to commit the changes, so they have a chance to review the generated files first.
   - **CHAT LANGUAGE RULE:** Explain your final response and chat messages in the language the user is currently writing in (e.g., Portuguese), even though you just generated all files in English.
