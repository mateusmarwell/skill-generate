# Regeneration Rules (Regenerate Mode)

When the command `/generate-skills regenerate` is executed, the main `spec-skill-generator` skill must re-process the documentation and apply modifications strictly adhering to these rules:

## 1. Block Handling
- **Generated Blocks (`SPEC-GENERATED`)**: Can be completely overwritten by the newly read data from `.spec/init` or the project source.
- **Custom Blocks (`SPEC-CUSTOM`)**: Must NEVER be overwritten, deleted, or altered by the automation. They belong to the human developer.

## 2. Replaced or Deprecated Technologies
- If a technology is detected as replaced (e.g., The code stopped using MySQL and now uses PostgreSQL), do not silently delete the previous rules if there is associated manual content.
- Add a note stating that the technology was discontinued for the skill that consumed it, and log the deprecation in the manifest.

## 3. Missing Markers
- If the file exists and contains no `SPEC-*` blocks, **create a backup** (e.g., `SKILL.md.bak`) of the content and do not apply substitutions until the developer organizes the blocks.
- Inform the developer that the files do not follow the standard block format.

## 4. Content Differential
- Do not rewrite the entire file unless there are changes. Compare the new information against the current file or the source hash stored in the manifest.
