# Generate Skills Workflow

This file dictates the rules and commands for the bot to execute the `spec-skill-generator` plugin.

## Available Commands

- `/generate-skills`
  - **Default Behavior**: If the `.agents/skills/.spec-skill-manifest.json` manifest does not exist, it runs the `generate` mode. If the manifest exists, it runs the `regenerate` mode.
- `/generate-skills generate`
  - Creates the 4 skills (`architect`, `backend`, `frontend`, `tester`) for the first time, reading the documentation and detecting the stack.
- `/generate-skills regenerate`
  - Reads the updated documentation and source code, updating only the `SPEC-GENERATED` blocks within the 4 skills, preserving any content in `SPEC-CUSTOM`.
- `/generate-skills check`
  - Only analyzes the stack and the changes between sources and the manifest, reporting (dry-run) what changes would happen without modifying any files.
- `/generate-skills force`
  - Forces the regeneration of all skills, ignoring the current hash state in the manifest.
- `/generate-skill-suggest [skill-name]`
  - Creates the skills suggested by the generator (logged in `suggested_skills` inside the manifest).
  - If executed **without arguments**, creates all suggested skills.
  - If a **name** is provided, creates only the requested skill, as long as it makes sense for the project.

## Required Actions when Executing Commands
The agent must:
1. Internally invoke the `spec-skill-generator` skill.
2. Follow the block preservation rules described in `regeneration-rules.md`.
3. Inform the user of the created/modified/preserved files and any conflicts found.
4. Pass the mandatory validation using `validate-generated-skills.py`.
