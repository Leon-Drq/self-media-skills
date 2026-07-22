#!/usr/bin/env python3
"""Render an English Markdown article as a paste-ready X Articles rich-copy page."""

from __future__ import annotations

import argparse
import html
import os
from pathlib import Path
import re


IMAGE_RE = re.compile(r"!\[[^\]]*\]\([^\)]+\)\s*")
LINK_RE = re.compile(r"\[([^\]]+)\]\((https?://[^\s\)]+)\)")


def render_inline(value: str) -> str:
    links: list[tuple[str, str, str]] = []

    def hold_link(match: re.Match[str]) -> str:
        placeholder = f"\x00LINK{len(links)}\x00"
        links.append((placeholder, match.group(1), match.group(2)))
        return placeholder

    value = LINK_RE.sub(hold_link, value)
    value = html.escape(value, quote=False)
    value = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", value)
    value = re.sub(r"(?<!\*)\*([^*\n]+)\*(?!\*)", r"<em>\1</em>", value)
    value = re.sub(r"`([^`\n]+)`", r"<code>\1</code>", value)
    for placeholder, label, url in links:
        label_html = html.escape(label, quote=False)
        label_html = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", label_html)
        value = value.replace(
            placeholder,
            f'<a href="{html.escape(url, quote=True)}">{label_html}</a>',
        )
    return value


def markdown_to_html(markdown: str) -> tuple[str, str]:
    markdown = IMAGE_RE.sub("", markdown)
    lines = markdown.splitlines()
    title = ""
    output: list[str] = []
    paragraph: list[str] = []

    def flush_paragraph() -> None:
        if paragraph:
            text = " ".join(part.strip() for part in paragraph if part.strip())
            if text:
                output.append(f"<p>{render_inline(text)}</p>")
            paragraph.clear()

    index = 0
    while index < len(lines):
        line = lines[index].rstrip()
        stripped = line.strip()

        if not stripped:
            flush_paragraph()
            index += 1
            continue

        if stripped.startswith("# "):
            flush_paragraph()
            if not title:
                title = stripped[2:].strip()
            index += 1
            continue

        if stripped.startswith("### "):
            flush_paragraph()
            output.append(f"<h3>{render_inline(stripped[4:].strip())}</h3>")
            index += 1
            continue

        if stripped.startswith("## "):
            flush_paragraph()
            output.append(f"<h2>{render_inline(stripped[3:].strip())}</h2>")
            index += 1
            continue

        if stripped in {"---", "***", "___"}:
            flush_paragraph()
            output.append("<hr>")
            index += 1
            continue

        if stripped.startswith(">"):
            flush_paragraph()
            quote_lines: list[str] = []
            while index < len(lines) and lines[index].lstrip().startswith(">"):
                quote_lines.append(lines[index].lstrip()[1:].strip())
                index += 1
            quote = " ".join(part for part in quote_lines if part)
            output.append(f"<blockquote><p>{render_inline(quote)}</p></blockquote>")
            continue

        paragraph.append(stripped)
        index += 1

    flush_paragraph()
    if not title:
        raise ValueError("The Markdown file must contain an H1 title or use --title.")
    return title, "\n".join(output)


def build_page(title: str, body_html: str, cover: Path | None, output: Path) -> str:
    cover_html = ""
    if cover:
        cover_absolute = cover.resolve()
        cover_relative = os.path.relpath(cover_absolute, output.parent.resolve()).replace("\\", "/")
        cover_html = f"""
    <section class="cover-card">
      <img src="{html.escape(cover_relative, quote=True)}" alt="Cover preview">
      <div class="cover-path">Cover file: {html.escape(str(cover_absolute))}</div>
    </section>"""

    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>X Rich Copy — {html.escape(title)}</title>
  <style>
    :root {{ color-scheme: light; font-family: Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif; }}
    * {{ box-sizing: border-box; }}
    body {{ margin: 0; background: #f5f7f9; color: #0f1419; }}
    .toolbar {{ position: sticky; top: 0; z-index: 3; background: rgba(255,255,255,.96); border-bottom: 1px solid #d8e0e5; padding: 14px 20px; backdrop-filter: blur(10px); }}
    .toolbar-inner {{ max-width: 900px; margin: auto; display: flex; flex-wrap: wrap; gap: 10px; align-items: center; }}
    button {{ border: 0; border-radius: 999px; padding: 10px 18px; font: inherit; font-weight: 700; cursor: pointer; }}
    .primary {{ color: white; background: #0f1419; }}
    .secondary {{ color: #0f1419; background: #e7ecf0; }}
    #status {{ color: #536471; font-size: 14px; }}
    main {{ max-width: 900px; margin: 28px auto 80px; padding: 0 20px; }}
    .instructions, .title-card, .cover-card, article {{ background: white; border: 1px solid #d8e0e5; border-radius: 18px; box-shadow: 0 6px 22px rgba(15,20,25,.06); }}
    .instructions {{ padding: 18px 22px; margin-bottom: 18px; color: #536471; }}
    .instructions strong {{ color: #0f1419; }}
    .title-card {{ padding: 22px 28px; margin-bottom: 18px; }}
    .eyebrow {{ color: #536471; font-size: 13px; font-weight: 700; letter-spacing: .08em; text-transform: uppercase; }}
    .article-title {{ margin: 8px 0 0; font-family: Georgia, "Times New Roman", serif; font-size: 34px; line-height: 1.15; }}
    .cover-card {{ padding: 18px; margin-bottom: 18px; }}
    .cover-card img {{ display: block; width: 100%; max-height: 420px; object-fit: cover; border-radius: 12px; }}
    .cover-path {{ margin-top: 10px; color: #536471; font-size: 13px; overflow-wrap: anywhere; }}
    article {{ padding: 42px 54px; font-family: Georgia, "Times New Roman", serif; font-size: 20px; line-height: 1.65; }}
    article h2 {{ margin: 2.2em 0 .7em; font-family: Inter, ui-sans-serif, system-ui, sans-serif; font-size: 28px; line-height: 1.2; }}
    article h3 {{ margin: 1.8em 0 .6em; font-family: Inter, ui-sans-serif, system-ui, sans-serif; font-size: 23px; line-height: 1.25; }}
    article p {{ margin: 0 0 1.15em; }}
    article blockquote {{ margin: 0 0 1.6em; padding: 16px 20px; border-left: 4px solid #0f1419; background: #f7f9f9; color: #3d4b55; }}
    article blockquote p:last-child {{ margin-bottom: 0; }}
    article a {{ color: #006fd6; text-decoration: underline; }}
    article code {{ font-family: ui-monospace, SFMono-Regular, Consolas, monospace; font-size: .9em; }}
    article hr {{ margin: 3em 0 2em; border: 0; border-top: 1px solid #cfd9de; }}
    @media (max-width: 680px) {{ article {{ padding: 28px 22px; font-size: 18px; }} .article-title {{ font-size: 28px; }} }}
  </style>
</head>
<body>
  <div class="toolbar">
    <div class="toolbar-inner">
      <button class="secondary" onclick="copyTitle()">Copy title</button>
      <button class="primary" onclick="copyArticle()">Copy formatted article</button>
      <span id="status">Use normal paste in X — not Ctrl+Shift+V.</span>
    </div>
  </div>
  <main>
    <div class="instructions"><strong>For X Articles:</strong> copy the title into X’s title field, upload the cover separately, then copy the formatted article and paste normally into the body editor.</div>
    <section class="title-card">
      <div class="eyebrow">Article title</div>
      <div class="article-title" id="articleTitle">{html.escape(title)}</div>
    </section>{cover_html}
    <article id="xBody" contenteditable="true" spellcheck="true">
{body_html}
    </article>
  </main>
  <script>
    function setStatus(message) {{ document.getElementById('status').textContent = message; }}
    async function copyTitle() {{
      const title = document.getElementById('articleTitle').textContent;
      try {{ await navigator.clipboard.writeText(title); }}
      catch (_) {{
        const range = document.createRange(); range.selectNodeContents(document.getElementById('articleTitle'));
        const selection = window.getSelection(); selection.removeAllRanges(); selection.addRange(range);
        document.execCommand('copy'); selection.removeAllRanges();
      }}
      setStatus('Title copied. Paste it into X’s title field.');
    }}
    function copyArticle() {{
      const range = document.createRange(); range.selectNodeContents(document.getElementById('xBody'));
      const selection = window.getSelection(); selection.removeAllRanges(); selection.addRange(range);
      const ok = document.execCommand('copy'); selection.removeAllRanges();
      setStatus(ok ? 'Formatted article copied. Paste normally into X.' : 'Copy failed. Select the article body manually and copy.');
    }}
  </script>
</body>
</html>
"""


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path, help="English Markdown article")
    parser.add_argument("--output", type=Path, help="Output HTML path")
    parser.add_argument("--title", help="Override the Markdown H1 title")
    parser.add_argument("--cover", type=Path, help="Local cover image for preview/manual upload")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    source = args.input.resolve()
    if not source.is_file():
        raise SystemExit(f"Input file not found: {source}")

    markdown = source.read_text(encoding="utf-8")
    detected_title, body_html = markdown_to_html(markdown)
    title = args.title or detected_title
    output = (args.output or source.with_name(f"{source.stem}-x-rich-copy.html")).resolve()
    cover = args.cover.resolve() if args.cover else None
    if cover and not cover.is_file():
        raise SystemExit(f"Cover image not found: {cover}")

    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(build_page(title, body_html, cover, output), encoding="utf-8")
    print(output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
