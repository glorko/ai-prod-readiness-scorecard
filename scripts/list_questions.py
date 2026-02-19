#!/usr/bin/env python3
"""
Extract all question_id values from questionnaire/*.md files.
Each question is in a YAML frontmatter block (--- ... ---) with a line "id: <question_id>".
Output: one question_id per line, in file order then block order.
Used so the assessment prompt does not hardcode the list; the questionnaire files are the source of truth.
"""
import re
import sys
from pathlib import Path

# Default: questionnaire dir next to scripts/
SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parent
QUESTIONNAIRE_DIR = REPO_ROOT / "questionnaire"


def extract_ids_from_content(content: str) -> list[str]:
    """Extract all id: values from YAML frontmatter blocks (--- ... ---)."""
    ids = []
    # Split by --- but keep delimiters to find blocks
    blocks = re.split(r"\n---\n", content)
    for block in blocks:
        block = block.strip()
        if not block or block.startswith("#"):
            continue
        # First line or any line: id: value (value can be quoted)
        match = re.search(r"^id:\s*['\"]?([a-z0-9_-]+)['\"]?", block, re.MULTILINE | re.IGNORECASE)
        if match:
            ids.append(match.group(1).strip())
    return ids


def main():
    questionnaire_dir = QUESTIONNAIRE_DIR
    if not questionnaire_dir.is_dir():
        sys.exit(f"Questionnaire dir not found: {questionnaire_dir}")

    all_ids = []
    # Process .md files in consistent order (sort by name); skip index.md for order (optional)
    for path in sorted(questionnaire_dir.glob("*.md")):
        if path.name == "index.md":
            continue
        text = path.read_text(encoding="utf-8")
        ids = extract_ids_from_content(text)
        all_ids.extend(ids)

    for qid in all_ids:
        print(qid)


if __name__ == "__main__":
    main()
