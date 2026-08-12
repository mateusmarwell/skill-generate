---
description: Identifies if it should generate (new project) or regenerate (existing project) the skills based on the manifest.
allowed-tools: SlashCommand, Read, Bash, Glob, Grep
---

# generate-skills

You are the router for the `spec-skill-generator` plugin. Your goal is to trigger the main generation skill.

## Behavior
1. Check if the `.agents/skills/.spec-skill-manifest.json` file exists in the current project root.
2. If it does NOT exist: You must trigger the `spec-skill-generator` skill to run in **generate** mode.
3. If it DOES exist: You must trigger the `spec-skill-generator` skill to run in **regenerate** mode.
4. Inform the user what is being done, and ensure the script `validate-generated-skills.py` is called at the end.
5. Obey all rules in `references/regeneration-rules.md`.
