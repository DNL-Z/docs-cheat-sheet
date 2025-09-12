#!/usr/bin/env python3
import os
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RTF_DIR = ROOT / 'docs-rtf'

# Simple RTF to text/markdown converter (very naive but works for these notes)
HEX_ESC_RE = re.compile(r"\\'([0-9a-fA-F]{2})")
CTRL_WORD_RE = re.compile(r"\\[a-zA-Z]+-?\d* ?")  # \\word123 or \\word-1
BRACE_RE = re.compile(r"[{}]")
MULTI_NL_RE = re.compile(r"\n{3,}")
MULTI_SPACE_RE = re.compile(r"[ \t]{2,}")

# Map some common controls to newlines explicitly before blanket removal
LINE_BREAK_CONTROLS = [
    r"\par", r"\line", r"\page"
]


def rtf_to_text(rtf: str) -> str:
    # Convert hex escapes like \'97 to unicode char using cp1252
    def hex_sub(m):
        byte_val = int(m.group(1), 16)
        return bytes([byte_val]).decode('cp1252', errors='replace')

    text = HEX_ESC_RE.sub(hex_sub, rtf)

    # Replace explicit line breaks with newlines (match whole control words only)
    text = re.sub(r"\\par(?![a-zA-Z])", "\n", text)
    text = re.sub(r"\\line(?![a-zA-Z])", "\n", text)
    text = re.sub(r"\\page(?![a-zA-Z])", "\n", text)

    # Remove other control words
    text = CTRL_WORD_RE.sub('', text)

    # Remove braces
    text = BRACE_RE.sub('', text)

    # Normalize CR/LF
    text = text.replace('\r', '\n')

    # Collapse many newlines, but keep double newlines for paragraphs
    text = MULTI_NL_RE.sub('\n\n', text)

    # Trim trailing spaces on lines
    text = '\n'.join(line.rstrip() for line in text.splitlines())

    # Strip leading/trailing blank lines
    text = text.strip('\n ').strip()

    # Remove lines that are just a single backslash and strip trailing backslashes
    raw_lines = text.splitlines()
    cleaned = []
    for ln in raw_lines:
        if ln.strip() == '\\':
            continue
        if ln.endswith('\\'):
            ln = ln[:-1]
        cleaned.append(ln)
    lines = cleaned

    # If there's a markdown heading, keep content starting from the first heading
    first_heading_idx = next((i for i, ln in enumerate(lines) if ln.lstrip().startswith('#')), None)
    if first_heading_idx is not None:
        lines = lines[first_heading_idx:]

    # Re-join and normalize excessive blank lines
    text = '\n'.join(lines)
    text = MULTI_NL_RE.sub('\n\n', text)

    # Some RTFs insert long runs of dashes as separators; keep them as is.
    return text.strip() + '\n'


def make_names(base: str):
    # base is filename without extension
    if base.startswith('doc-'):
        name_part = base[4:]
    else:
        name_part = base
    # Folder and Markdown file name: capitalize first letter only
    if not name_part:
        folder = 'Docs'
    else:
        folder = name_part[0].upper() + name_part[1:]
    md_file = f"{folder}.md"
    return folder, md_file


def main():
    if not RTF_DIR.exists():
        raise SystemExit(f"RTF directory not found: {RTF_DIR}")

    created = []
    for entry in sorted(RTF_DIR.iterdir()):
        if entry.is_file() and entry.suffix.lower() == '.rtf':
            base = entry.stem
            folder, md_file = make_names(base)
            target_dir = ROOT / folder
            target_dir.mkdir(parents=True, exist_ok=True)
            target_path = target_dir / md_file

            rtf_content = entry.read_text(encoding='utf-8', errors='ignore')
            md_content = rtf_to_text(rtf_content)

            # Ensure top-level title is present: if first non-empty line doesn't start with '#', keep as-is.
            # We trust the RTF already contains markdown-like headings (as seen in examples).
            target_path.write_text(md_content, encoding='utf-8')
            created.append(str(target_path.relative_to(ROOT)))
            print(f"Wrote {target_path}")

    print(f"Converted {len(created)} file(s):")
    for c in created:
        print(f" - {c}")


if __name__ == '__main__':
    main()
