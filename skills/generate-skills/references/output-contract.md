# Output Contract for Generated Skills

The generated core skills (up to five: `architect`, `tester`, and `security` always generated; `backend` and `frontend` conditionally generated based on stack evidence) must strictly adhere to this block structure and filling conventions.

## Mandatory Structure for SKILL.md

```markdown
---
name: [Skill Name, e.g.: myproject-backend]
description: [Description focused on the responsibilities of the detected skill]
---

# Objective
[Short description of the skill within the context of the project]

## Technologies and Stack (Evidence-based)
<!-- BEGIN SPEC-GENERATED: detected-stack -->
- Language: [Detected]
- Framework: [Detected]
<!-- END SPEC-GENERATED: detected-stack -->

## Business Rules
<!-- BEGIN SPEC-GENERATED: business-rules -->
- Rule 1...
<!-- END SPEC-GENERATED: business-rules -->

## Real Commands (Detected)
<!-- BEGIN SPEC-GENERATED: commands -->
- Tests: `[detected command]`
<!-- END SPEC-GENERATED: commands -->

## Custom Manual Rules (Do not delete)
<!-- BEGIN SPEC-CUSTOM: project-rules -->
[Placeholder for the developer to write persistent manual rules]
<!-- END SPEC-CUSTOM: project-rules -->

## Engineering Technical Decisions
<!-- BEGIN SPEC-CUSTOM: engineering-decisions -->
[Placeholder to log technical decisions that must not be lost upon regeneration]
<!-- END SPEC-CUSTOM: engineering-decisions -->
```

## Rules per Skill

1. **Architect:** Focus on module separation, allowed dependencies, documented architecture, and potential integration conflicts.
   - **Legacy Protection Guardrails (Mandatory):**
     - **Pattern Continuity:** Strictly adhere to the project's existing folder layout, naming conventions, and structural architecture without imposing unrequested paradigms (e.g., Clean Architecture, DDD, microservices).
     - **No Global Reorganization:** Do NOT move, rename, or reorganize existing core modules or directories without explicit developer instructions.
     - **Dependency Restraint & Lockfile Preservation:** Prefer native language features and existing utility functions over adding new dependencies. Never install unrequested libraries or delete/regenerate lockfiles (`package-lock.json`, `poetry.lock`, `composer.lock`, etc.). When a package is required, pin the exact version compatible with the legacy environment.
     - **Path Portability & Zero Machine Hardcoding:** Prohibit absolute machine-specific paths (e.g., `C:\Users\...`, `/home/...`). Always resolve paths dynamically or relatively (`path.join`, `os.path.join`, `Pathlib`). Use environment variables for hosts, ports, and external endpoints instead of hardcoding `localhost`.
2. **Tester:** Transform specification scenarios into a clear matrix of pre-conditions, inputs, and outputs, linking them to the testing framework (if detected). If no testing tools are detected, recommend the manual creation of scripts.
   - **Legacy Protection Guardrails (Mandatory):**
     - **Test Runner Parity:** Author test cases using strictly the detected test runner, assertion libraries, and execution conventions.
     - **CI/CD Compatibility:** Ensure new tests execute via native project test commands (`npm test`, `pytest`, `mvn test`) without requiring modifications to existing CI/CD or build pipelines.
     - **Fixture & Helper Reuse:** Reutilize existing test utilities, fixtures, seeders, and mocks rather than creating conflicting test harnesses.
3. **Security:** Focus on application security posture, OWASP Top 10 prevention, secrets management (`.env`, no hardcoded tokens/credentials), input sanitization, authentication/authorization validation, and detected security audit commands (e.g., `npm audit`, `pip-audit`, `cargo audit`, `bandit`, `trivy`, `semgrep`).
   - **Legacy Protection Guardrails (Mandatory):**
     - **Scoped Enforcement:** Apply strict security validations only to newly created code or code explicitly targeted for editing.
     - **No Mass Refactoring:** Do NOT unilaterally rewrite existing working legacy authentication, raw database queries, or legacy dependencies unless explicitly requested by the developer.
     - **Sanitized Logging & PII Redaction:** Never log sensitive data (e.g., `password`, `token`, `secret`, `credit_card`, CPF/SSN, PII). Use existing leveled logger methods (`logger.info`, `logger.error`) rather than raw `console.log` or `print` dumps.
     - **Flag & Warn:** If legacy vulnerabilities are identified in untouched code, report them in the final chat response/notes instead of modifying unrequested files.
     - **Stack & Version Respect:** Recommend and enforce security practices compatible with the detected version of the language/framework without forcing breaking dependency upgrades.
4. **Backend:** Focus on controllers, validations, persistence, database (if detected), and server-side integrations.
   - **Legacy Protection Guardrails (Mandatory):**
     - **Contract Immutability:** Never alter existing endpoint signatures, response schemas, status codes, or parameter names of working APIs.
     - **Additive & Non-Destructive Migrations:** Prohibit destructive schema alterations (`DROP COLUMN`, `DROP TABLE`, in-place column renames). Database changes must follow the Expand-Contract pattern with nullable columns or safe defaults to avoid production downtime.
     - **Bounded Queries & No N+1:** Always include pagination (`LIMIT`/`OFFSET` or cursor) on list queries. Never execute database queries inside loops (`for`, `forEach`, `while`); use batching, joins, or eager loading.
     - **Explicit Error Handling (No Silent Swallowing):** Never swallow exceptions with empty `catch` or `except: pass` blocks. Catch specific exceptions, preserve error context/stack for developers, and return structured, sanitized error messages.
     - **Persistence Pattern Parity:** Respect and maintain the existing database access patterns (e.g., raw SQL with parameter binding, custom DAOs, ORMs, stored procedures) without forcing modern ORM rewrites.
     - **Runtime Version Parity:** Restrict language features and standard library methods strictly to what is supported by the detected runtime version (e.g., Node 14/16, PHP 7.x, Python 3.8, Java 8/11).
5. **Frontend:** Focus on frameworks (if detected), components, route consumption and contracts, states, and UI/UX/Accessibility.
   - **Legacy Protection Guardrails (Mandatory):**
     - **Styling Consistency:** Adhere strictly to the existing styling paradigm (e.g., Global CSS, BEM, SASS/SCSS, CSS Modules, Bootstrap) without injecting competing CSS frameworks (e.g., Tailwind).
     - **Component Pattern Continuity:** Match the component style (class-based vs functional components, state management version) of the file or module being touched.
     - **Global Layout Preservation:** Do NOT modify global CSS resets, shared layout wrappers, or root styling tokens that could distort existing legacy screens.
