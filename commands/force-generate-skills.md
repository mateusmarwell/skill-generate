---
description: Forces the regeneration of all skills, ignoring the current hash state in the manifest.
allowed-tools: SlashCommand, Read, Bash, Glob, Grep
---

# force-generate-skills

You are the force-recreator for the `spec-skill-generator` plugin.

## Behavior
1. You must invoke the `spec-skill-generator` skill.
2. Instruct the skill to completely ignore the current source hashes in `.agents/skills/.spec-skill-manifest.json`.
3. Even if the hashes match, force the regeneration of the `SPEC-GENERATED` blocks for all 4 standard skills.
4. Call `validate-generated-skills.py` at the end.
