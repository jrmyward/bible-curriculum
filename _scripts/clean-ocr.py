#!/usr/bin/env python3
"""Clean raw OCR text into structured markdown.

Reads raw OCR text dumps from `<target>/.raw-ocr/chNN.txt` and writes cleaned
markdown to `<target>/chNN.md`. Designed for the teaching-manual / textbook
chapter directory layout under `_source-text/`.

Usage:
    python3 clean-ocr.py <target-dir> <chapter-number|all>

Examples:
    python3 _scripts/clean-ocr.py classes/understanding-the-faith/_source-text/teaching-manual all
    python3 _scripts/clean-ocr.py classes/understanding-the-faith/_source-text/teaching-manual 5
"""

import re
import sys
from collections import Counter
from pathlib import Path


def is_page_number_line(line: str) -> bool:
    """Match standalone page numbers like '- 43-', '• 49 •', '-40 -', '- 65 -'."""
    s = line.strip()
    if not s or len(s) > 10:
        return False
    return bool(re.match(r"^[-–—•·.\s]*\d{1,4}[-–—•·.\s]*$", s))


def fix_section_labels(line: str) -> str:
    """Fix common OCR errors in [N.M] style section labels."""
    # (3.4) or (3.4] → [3.4]
    line = re.sub(r"\((\d{1,2})\.(\d{1,2})[\]\)]", r"[\1.\2]", line)
    # [3.4) → [3.4]
    line = re.sub(r"\[(\d{1,2})\.(\d{1,2})\)", r"[\1.\2]", line)
    # (3.11] → [3.11]
    line = re.sub(r"\((\d{1,2})\.(\d{1,2})\]", r"[\1.\2]", line)
    return line


def stitch_numbered_lists(lines: list[str]) -> list[str]:
    """Combine 'N.' on its own line with the text on the next non-empty line."""
    out = []
    i = 0
    while i < len(lines):
        line = lines[i]
        m = re.match(r"^(\s*)(\d{1,2})\.\s*$", line)
        if m and i + 1 < len(lines):
            indent = m.group(1)
            num = m.group(2)
            j = i + 1
            while j < len(lines) and not lines[j].strip():
                j += 1
            if j < len(lines):
                out.append(f"{indent}{num}. {lines[j].strip()}")
                i = j + 1
                continue
        out.append(line)
        i += 1
    return out


def clean(raw_text: str, chapter_num: int) -> str:
    raw_lines = raw_text.split("\n")

    counts = Counter(line.strip() for line in raw_lines if line.strip())
    repeating = {
        line for line, count in counts.items()
        if count >= 3 and len(line) >= 3
    }

    out: list[str] = []
    page_count = 0

    for line in raw_lines:
        stripped = line.strip()

        if re.match(r"^=== IMG_\d+\.jpg ===$", stripped):
            page_count += 1
            out.append("")
            out.append(f"<!-- page-{page_count} -->")
            out.append("")
            continue

        if is_page_number_line(line):
            continue

        if stripped in repeating:
            continue

        out.append(fix_section_labels(line))

    out = stitch_numbered_lists(out)

    final: list[str] = []
    blank_run = 0
    for line in out:
        if line.strip() == "":
            blank_run += 1
            if blank_run <= 2:
                final.append(line)
        else:
            blank_run = 0
            final.append(line)

    while final and final[0].strip() == "":
        final.pop(0)
    while final and final[-1].strip() == "":
        final.pop()

    header = f"# Chapter {chapter_num}\n\n"
    return header + "\n".join(final) + "\n"


def process(target: Path, chapter_num: int) -> tuple[int, int]:
    raw_path = target / ".raw-ocr" / f"ch{chapter_num:02d}.txt"
    out_path = target / f"ch{chapter_num:02d}.md"
    if not raw_path.exists():
        print(f"skip ch{chapter_num:02d}: no raw OCR file at {raw_path}", file=sys.stderr)
        return 0, 0
    raw = raw_path.read_text()
    cleaned = clean(raw, chapter_num)
    out_path.write_text(cleaned)
    return len(raw.split("\n")), len(cleaned.split("\n"))


def main():
    if len(sys.argv) != 3:
        print("usage: clean-ocr.py <target-dir> <chapter-number|all>", file=sys.stderr)
        sys.exit(1)

    target = Path(sys.argv[1]).resolve()
    if not target.is_dir():
        print(f"error: target dir not found: {target}", file=sys.stderr)
        sys.exit(1)

    arg = sys.argv[2]
    if arg == "all":
        for n in range(1, 19):
            in_lines, out_lines = process(target, n)
            if in_lines:
                print(f"ch{n:02d}: {in_lines} → {out_lines} lines")
    else:
        n = int(arg)
        in_lines, out_lines = process(target, n)
        print(f"ch{n:02d}: {in_lines} → {out_lines} lines")


if __name__ == "__main__":
    main()
