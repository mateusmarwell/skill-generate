---
name: force-generate-skills
description: Forces the regeneration of all skills, ignoring the current hash state in the manifest.
tools:
  - invoke_subagent
  - view_file
  - write_to_file
  - list_dir
  - grep_search
  - run_command
  - define_subagent
---

# force-generate-skills

You are the force-recreator for the `generate-skills` skill.

## Behavior
1. You must invoke the `generate-skills` logic.
2. Instruct the process to completely ignore the current source hashes in `.agents/skills/.spec-skill-manifest.json`.
3. Even if the hashes match, force the regeneration of the `SPEC-GENERATED` blocks for all 4 standard skills.
4. Call `validate-generated-skills.py` at the end.
