---
description: Performs a dry-run (test) without modifying any files, informing what changes would occur.
allowed-tools: SlashCommand, Read, Bash, Glob, Grep
---

# check-skills

You are a dry-run simulator for the `spec-skill-generator` plugin.

## Behavior
1. Run the stack detection and check the differences between the current sources and the manifest `.agents/skills/.spec-skill-manifest.json`.
2. Do not write, edit, or delete any files.
3. Simply inform the user (dry-run) what changes would happen if they were to run `/generate-skills regenerate` right now.
