# Spec Skill Generator Plugin

This repository contains the `spec-skill-generator` plugin for Google Antigravity. This plugin was developed to be strictly **stack-agnostic and language-agnostic**.

## Objective

Transform the project into active and updatable skills that guide the AI agents:

1. **Architect**: Technical decisions and module organization. (Always generated)
2. **Tester**: Transforming acceptance criteria and stories into test scenarios. (Always generated)
3. **Backend**: Persistence, validations, and controllers. (Generated ONLY if backend evidence is found)
4. **Frontend**: Components, UI/UX, and route consumption. (Generated ONLY if frontend evidence is found)

### Modes of Operation
- **Spec-Driven**: If the project has a `.spec/init/` directory (living specification), the plugin will read those formal contracts to generate the skills.
- **Code-Driven (Legacy/Fallback)**: If no specification exists, the plugin will seamlessly fallback to reverse-engineering the project by deeply analyzing the source code, package configurations, and directory structure to infer the architecture and business rules.

## Plugin Structure

- `skills/generate-skills/SKILL.md`: The main skill that triggers the generation.
- `skills/generate-skills/references/`: Rules for preservation (`regeneration-rules.md`), output contract (`output-contract.md`), and manifest schema (`manifest-schema.json`).
- `skills/generate-skills/scripts/validate-generated-skills.py`: Python script used to ensure the integrity of the generated skills.

## How to Use (Skills)

In the Antigravity chat, simply type `/` to see the native skills autocompleted:

- `/generate-skills` - Automatically identifies whether to generate (new project) or regenerate (existing project).
- `/check-skills` - Performs a dry-run without modifying any files.
- `/force-generate-skills` - Forces recreation, ignoring the hash in the manifest.
- `/generate-skill-suggest` - Generates additional specialized skills suggested by the AI based on the project's infrastructure.

## Customization and Safety

All generated skills use blocks marked with `<!-- BEGIN SPEC-GENERATED: ... -->` and `<!-- BEGIN SPEC-CUSTOM: ... -->`.
During a regeneration, **only the generated content** is replaced, ensuring that the developer's manual rules and engineering notes are never lost.
