#!/usr/bin/env python3
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXCLUDE_DIRS = {'.git', 'docs-rtf', 'scripts'}
TARGET_EXTS = {'.md'}

# Characters to replace: NBSP and NARROW NBSP (common in French typography)
REPLACEMENTS = {
    '\u00A0': ' ',  # NO-BREAK SPACE
    '\u202F': ' ',  # NARROW NO-BREAK SPACE
}


def should_skip(path: Path) -> bool:
    for p in path.parents:
        if p.name in EXCLUDE_DIRS:
            return True
    return False


def clean_text(text: str) -> tuple[str, int]:
    count = 0
    for src, dst in REPLACEMENTS.items():
        before = text
        text = text.replace(src, dst)
        count += before.count(src)
    return text, count


def main() -> int:
    changed_files = 0
    total_replacements = 0
    modified = []

    for path in ROOT.rglob('*'):
        if not path.is_file():
            continue
        if path.suffix.lower() not in TARGET_EXTS:
            continue
        if should_skip(path):
            continue
        try:
            content = path.read_text(encoding='utf-8', errors='ignore')
        except Exception as e:
            print(f"Skip {path}: {e}")
            continue
        new_content, n = clean_text(content)
        if n > 0 and new_content != content:
            path.write_text(new_content, encoding='utf-8')
            changed_files += 1
            total_replacements += n
            modified.append(path.relative_to(ROOT))

    print(f"Replaced NBSPs in {changed_files} file(s), total {total_replacements} replacement(s).")
    for m in modified:
        print(f" - {m}")
    return 0


if __name__ == '__main__':
    sys.exit(main())
