# Output Contract for Generated Skills

The four generated skills (`architect`, `backend`, `frontend`, `tester`) must strictly adhere to this block structure and filling conventions.

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
2. **Backend:** Focus on controllers, validations, persistence, database (if detected), and server-side integrations.
3. **Frontend:** Focus on frameworks (if detected), components, route consumption and contracts, states, and UI/UX/Accessibility.
4. **Tester:** Transform specification scenarios into a clear matrix of pre-conditions, inputs, and outputs, linking them to the testing framework (if detected). If no testing tools are detected, recommend the manual creation of scripts.
