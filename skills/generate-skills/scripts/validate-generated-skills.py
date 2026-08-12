import os
import yaml
import sys
import glob

def validate_frontmatter(content):
    try:
        parts = content.split("---")
        if len(parts) >= 3:
            frontmatter = parts[1]
            data = yaml.safe_load(frontmatter)
            if not data:
                return False, "Frontmatter is empty."
            if "name" not in data or "description" not in data:
                return False, "Missing 'name' or 'description' in frontmatter."
            return True, "Valid frontmatter"
        return False, "No frontmatter found."
    except Exception as e:
        return False, f"YAML parsing error: {e}"

def validate_blocks(content):
    if "<!-- BEGIN SPEC-GENERATED:" in content and "<!-- END SPEC-GENERATED:" not in content:
        return False, "Unmatched SPEC-GENERATED blocks"
    if "<!-- BEGIN SPEC-CUSTOM:" in content and "<!-- END SPEC-CUSTOM:" not in content:
        return False, "Unmatched SPEC-CUSTOM blocks"
    return True, "Blocks matched"

def main():
    print("Starting validation of generated skills...")
    skills_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
    skill_files = glob.glob(os.path.join(skills_dir, '*', 'SKILL.md'))

    errors = []
    
    if not skill_files:
        print("No SKILL.md files found to validate.")
        return 0

    for file in skill_files:
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()

        is_valid, msg = validate_frontmatter(content)
        if not is_valid:
            errors.append(f"[{file}] {msg}")

        is_valid, msg = validate_blocks(content)
        if not is_valid:
            errors.append(f"[{file}] {msg}")

    if errors:
        print("Validation FAILED with errors:")
        for err in errors:
            print(f" - {err}")
        sys.exit(1)
    
    print("Validation PASSED.")
    sys.exit(0)

if __name__ == "__main__":
    main()
