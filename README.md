# Spec Skill Generator Plugin

This repository contains the `spec-skill-generator` plugin for Google Antigravity. This plugin was developed to be strictly **stack-agnostic and language-agnostic**.

## Objective

Transform the living specification of the project (usually located in `.spec/init/`) into active and updatable skills that guide the AI agents:

1. **Architect**: Technical decisions and module organization.
2. **Backend**: Persistence, validations, and controllers (if applicable).
3. **Frontend**: Components, UI/UX, and route consumption (if applicable).
4. **Tester**: Transforming acceptance criteria and stories into test scenarios.

## Plugin Structure

- `.agents/skills/spec-skill-generator/SKILL.md`: The main skill that triggers the generation.
- `.agents/skills/spec-skill-generator/references/`: Rules for preservation (`regeneration-rules.md`), output contract (`output-contract.md`), and manifest schema (`manifest-schema.json`).
- `.agents/skills/spec-skill-generator/scripts/validate-generated-skills.py`: Python script used to ensure the integrity of the generated skills.
- `.agents/workflows/generate-skills.md`: Workflow containing chat commands to trigger the plugin.

## How to Use (Workflow Commands)

In the Antigravity chat, you can invoke:

- `/generate-skills` - Automatically identifies whether to generate (new project) or regenerate (existing project).
- `/generate-skills check` - Performs a dry-run without modifying any files.
- `/generate-skills force` - Forces recreation, ignoring the hash in the manifest.
- `/generate-skill-suggest [skill-name]` - Generates additional specialized skills suggested by the AI based on the project's infrastructure.

## Customization and Safety

All generated skills use blocks marked with `<!-- BEGIN SPEC-GENERATED: ... -->` and `<!-- BEGIN SPEC-CUSTOM: ... -->`.
During a regeneration, **only the generated content** is replaced, ensuring that the developer's manual rules and engineering notes are never lost.
