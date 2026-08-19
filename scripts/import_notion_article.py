#!/usr/bin/env python3
"""Import one Notion Markdown export into a draft Quarto post.

Usage:
  python scripts/import_notion_article.py EXPORT_DIR SLUG --categories machine-learning implementation

The export directory must contain one Markdown file and may contain a sibling
media directory. The source export is never modified.
"""
from __future__ import annotations

import argparse
import re
import shutil
from datetime import datetime
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("export_dir", type=Path)
    parser.add_argument("slug")
    parser.add_argument("--date", help="Override YYYY-MM-DD extracted from export")
    parser.add_argument("--categories", nargs="+", required=True)
    parser.add_argument("--published", action="store_true")
    return parser.parse_args()


def clean_inline_math(text: str) -> str:
    pattern = re.compile(r"(?<!\\)(?<!\$)\$(?!\$)(.*?)(?<!\\)(?<!\$)\$(?!\$)")
    lines = []
    in_fence = False
    for line in text.splitlines(keepends=True):
        if re.match(r"^\s*(```|~~~)", line):
            in_fence = not in_fence
        if not in_fence:
            line = pattern.sub(lambda match: f"${match.group(1).strip()}$", line)
        lines.append(line)
    return "".join(lines)


def main() -> None:
    args = parse_args()
    markdown_files = sorted(args.export_dir.glob("*.md"))
    if len(markdown_files) != 1:
        raise SystemExit(f"expected exactly one Markdown file in {args.export_dir}")
    source = markdown_files[0]
    lines = source.read_text(encoding="utf-8").splitlines()
    if len(lines) < 4:
        raise SystemExit("export is missing title/date/author header")

    title = lines[0].removeprefix("# ").strip()
    date_match = re.search(r"([A-Z][a-z]+ \d{1,2}, \d{4})", "\n".join(lines[1:5]))
    date = args.date or datetime.strptime(date_match.group(1), "%B %d, %Y").date().isoformat()
    author = next((line.strip().title() for line in lines[1:8] if line.strip().isupper()), "Muhammad Ghifary")
    marker = next((i for i, line in enumerate(lines) if line.strip().isupper()), None)
    if marker is None:
        raise SystemExit("could not locate author header")
    body = "\n".join(lines[marker + 1:]).lstrip() + "\n"

    post_dir = Path("posts") / f"{date}-{args.slug}"
    media_dir = post_dir / "media"
    post_dir.mkdir(parents=True, exist_ok=True)
    media_dir.mkdir(exist_ok=True)
    source_media = next((p for p in args.export_dir.iterdir() if p.is_dir()), None)
    if source_media:
        for item in source_media.iterdir():
            if item.is_file():
                shutil.copy2(item, media_dir / item.name)
                encoded = item.name.replace(" ", "%20").replace("(", "%28").replace(")", "%29")
                body = body.replace(f"{source_media.name}/{item.name}", f"media/{item.name}")
                body = body.replace(f"{source_media.name}/{encoded}", f"media/{item.name}")
                body = body.replace(f"{source_media.name.replace(' ', '%20')}/{encoded}", f"media/{item.name}")
                if item.suffix.lower() in {".mp4", ".webm", ".mov"}:
                    body = body.replace(
                        f"[{item.name}](media/{item.name})",
                        f'<video controls preload="metadata" width="100%"><source src="media/{item.name}" type="video/{item.suffix[1:]}">Your browser does not support embedded video.</video>',
                    )

    body = clean_inline_math(body)
    categories = "".join(f"  - {category}\n" for category in args.categories)
    draft = "false" if args.published else "true"
    frontmatter = (
        "---\n"
        f'title: "{title.replace(chr(34), chr(92) + chr(34))}"\n'
        f'author: "{author}"\n'
        f"date: {date}\n"
        "description: \"Imported and normalized from a Notion article.\"\n"
        "categories:\n"
        f"{categories}"
        f"draft: {draft}\n"
        f"aliases:\n  - /{args.slug}/\n"
        "---\n\n"
    )
    (post_dir / "index.qmd").write_text(frontmatter + body, encoding="utf-8")
    print(post_dir / "index.qmd")


if __name__ == "__main__":
    main()
