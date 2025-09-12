#!/usr/bin/env python3
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXCLUDE_DIRS = { 'docs-rtf', 'scripts', '.git' }

# Keywords to bold (outside code blocks). Keep specific > generic ordering.
KEYWORDS = [
    # Languages / Platforms
    'JavaScript', 'TypeScript', 'Python', 'PHP', 'Ruby', 'Go', 'Swift', 'Kotlin',
    'Node.js', 'Node', 'Deno', 'Bun', 'Java',
    # Frontend / Frameworks / Tools
    'React', 'Vue', 'Next.js', 'Nuxt', 'Vite', 'Webpack', 'Babel',
    # Backend / Frameworks
    'Laravel', 'Symfony', 'Express', 'Serverless',
    # Web / CSS
    'CSS', 'HTML', 'SQL', 'Twig', 'Responsive', 'Breakpoints',
    # DevOps / Systems
    'Docker', 'Linux', 'Homebrew', 'Brew', 'Shell', 'Bash', 'Zsh', 'Git', 'Gitignore',
    # WordPress / Bedrock
    'WordPress', 'Bedrock', 'wpackagist',
    # Security / Network
    'Cybersecurity', 'Network', 'Permissions',
    # Misc
    'Mac', 'Apple', 'Raspberry', 'Package', 'NPM', 'Yarn', 'npm', 'yarn', 'Composer', 'composer'
]

# Precompile regex for word boundaries; avoid touching inside existing bold or code spans
KEYWORD_PATTERNS = [
    (kw, re.compile(rf"(?<!\*)\b{re.escape(kw)}\b(?!\*)")) for kw in KEYWORDS
]

DASH_SEP = re.compile(r"^[\-–—_]{5,}\s*$")  # long run of dashes/em-dashes/underscores
HEADING_RE = re.compile(r"^(#+)\s+(.*)$")
PROMPT_CMD = re.compile(r"^\$\s+(.*)$")
CODE_FENCE_RE = re.compile(r"^```+")


def style_markdown(text: str, file_title: str) -> str:
    lines = text.splitlines()

    # Normalize headings: ensure only the first heading is H1; others H2+.
    first_heading_seen = False
    styled = []
    in_code = False

    i = 0
    while i < len(lines):
        ln = lines[i]

        # Track code blocks
        if CODE_FENCE_RE.match(ln.strip()):
            in_code = not in_code
            styled.append(ln)
            i += 1
            continue

        # Convert repeated separators to horizontal rule
        if not in_code and DASH_SEP.match(ln):
            # collapse surrounding blank lines to a single
            if styled and styled[-1].strip() != '':
                styled.append('')
            styled.append('---')
            # ensure one blank line after; will normalize later
            styled.append('')
            i += 1
            continue

        # Group shell commands starting with "$ " into fenced code blocks
        if not in_code and PROMPT_CMD.match(ln):
            # start code block
            if styled and styled[-1].strip() != '':
                styled.append('')
            styled.append('```bash')
            # consume consecutive $ lines
            while i < len(lines) and PROMPT_CMD.match(lines[i]):
                cmd = PROMPT_CMD.sub(r"\1", lines[i]).rstrip()
                styled.append(cmd)
                i += 1
            styled.append('```')
            styled.append('')
            continue

        # Headings normalization
        if not in_code:
            # Handle stray '#' line used as a heading marker
            if ln.strip() == '#':
                # Look ahead for the next non-empty line to become the title
                j = i + 1
                next_text = None
                while j < len(lines):
                    if lines[j].strip() and not lines[j].strip().startswith('#'):
                        next_text = lines[j].strip()
                        break
                    elif lines[j].strip() == '':
                        j += 1
                        continue
                    else:
                        break
                if next_text:
                    if styled and styled[-1].strip() != '':
                        styled.append('')
                    if not first_heading_seen:
                        first_heading_seen = True
                        styled.append(f"# {next_text}")
                    else:
                        styled.append(f"## {next_text}")
                    styled.append('')
                    # skip the '#' line and the consumed title line
                    i = j + 1
                    continue
            m = HEADING_RE.match(ln)
            if m:
                hashes, title = m.group(1), m.group(2).strip()
                if not first_heading_seen:
                    # Make this H1, title-case lightly (keep acronyms)
                    first_heading_seen = True
                    ln = f"# {title}"
                else:
                    # Downgrade to H2+ (ensure at least H2)
                    ln = f"## {title}"
                # Ensure blank line before
                if styled and styled[-1].strip() != '':
                    styled.append('')
                styled.append(ln)
                # Ensure blank line after
                styled.append('')
                i += 1
                continue

        # Default: pass through line
        styled.append(ln)
        i += 1

    # If no H1 found, inject one based on file_title
    if not any(ln.startswith('# ') for ln in styled if ln is not None):
        styled = [f"# {file_title}", '', *styled]

    # Collapse multiple blank lines to max two, then to one around blocks
    out = '\n'.join(styled)
    # Normalize 3+ newlines to 2
    out = re.sub(r"\n{3,}", "\n\n", out)

    # Bold keywords outside code blocks and links
    out_lines = out.splitlines()
    final = []
    in_code = False
    for ln in out_lines:
        stripped = ln.strip()
        if CODE_FENCE_RE.match(stripped):
            in_code = not in_code
            final.append(ln)
            continue
        if in_code:
            final.append(ln)
            continue
        # Avoid touching markdown links [text](url)
        # Apply keyword bolding; keep order to prefer specific tokens
        new_ln = ln
        for kw, pat in KEYWORD_PATTERNS:
            new_ln = pat.sub(f"**{kw}**", new_ln)
        final.append(new_ln)

    # Ensure trailing newline
    result = '\n'.join(final).rstrip() + '\n'
    return result


def detect_title_from_path(path: Path) -> str:
    # Use parent folder name as title if matches filename, else filename stem
    if path.parent.name and path.parent.name != '.':
        return path.parent.name.replace('-', ' ')
    return path.stem.replace('-', ' ')


def process_all() -> int:
    count = 0
    for md in ROOT.glob('**/*.md'):
        # Skip excluded dirs
        parts = set(p.name for p in md.parents)
        if parts & EXCLUDE_DIRS:
            continue
        # Only process top-level topic folders (one level deep) and their files
        if md.parent == ROOT:
            # skip root README.md and LICENSE.txt converted to md if any
            if md.name.lower() == 'readme.md':
                continue
        # Read, style, and write back
        text = md.read_text(encoding='utf-8', errors='ignore')
        title = detect_title_from_path(md)
        styled = style_markdown(text, title)
        if styled != text:
            md.write_text(styled, encoding='utf-8')
            count += 1
    return count


def main():
    changed = process_all()
    print(f"Styled {changed} Markdown file(s).")


if __name__ == '__main__':
    main()
