---
description: Generates additional specialized skills suggested by the AI based on the project's infrastructure.
allowed-tools: SlashCommand, Read, Bash, Glob, Grep
---

# generate-skill-suggest

You are responsible for executing the creation of suggested skills.

## Behavior
1. Read the `.agents/skills/.spec-skill-manifest.json` file.
2. Find the `suggested_skills` array.
3. If the user passed no arguments, create ALL skills listed in the `suggested_skills` array using the `spec-skill-generator` logic.
4. If the user passed a specific skill name, verify if it makes sense for the project and create only that skill.
5. Update the manifest moving the created skill from `suggested_skills` to `generated_skills`.
6. Ensure to call the validation script at the end.
