---
name: wechat-to-x-article
description: Convert a WeChat Official Account article or Chinese Markdown article into an idiomatic English X Article and a browser-based rich-text copy page. Use when the user provides an mp.weixin.qq.com link or Chinese article and asks for an English X Article, X long-form post, source-attributed translation, or paste-ready X rich text with working headings, bold text, links, and quotations.
---

# WeChat to X Article

Produce two deliverables:

1. An idiomatic English Markdown article.
2. A self-contained HTML page with separate **Copy title** and **Copy formatted article** buttons for X Articles.

## Workflow

### 1. Acquire clean source content

- For an `mp.weixin.qq.com` URL, use the available `crawl-wechat` skill or another browser-based extractor.
- Extract only the article body (`#js_content`) plus title, account, date, source URL, and local images.
- Remove WeChat interface text such as likes, comments, complaints, login prompts, and recommendation controls.
- Preserve a clean Chinese Markdown source before translating.

### 2. Adapt the article into English

- Write natural editorial English; do not translate sentence by sentence.
- Preserve all factual claims, numbers, names, qualifications, and section order.
- Keep the author’s voice. Prefer established English terms such as “consumer,” “enterprise,” “foundation model,” “continuous learning,” and “embodied intelligence.”
- Expand culture-bound metaphors briefly when a literal version would confuse an English reader.
- Do not add unsupported facts or turn second-hand material into direct evidence.
- Use compact paragraphs suitable for reading on X.

Start with a source note in this form, adapted to the available metadata:

```markdown
> **Source note:** This English adaptation is based on the Chinese article [“Original title”](SOURCE_URL), published by **ACCOUNT** on DATE. State whether the source is a transcript, compilation, commentary, or reported account. Clarify that this is an idiomatic adaptation rather than an official verbatim translation when appropriate.
```

Use one H1 title, H2 section headings, semantic links, and Markdown emphasis. Keep image references relative to the article directory.

### 3. Create the X rich-copy page

Run the bundled renderer with a standard Python 3 interpreter:

```powershell
python scripts/render_x_rich_copy.py ARTICLE.md --cover COVER_IMAGE
```

Optional arguments:

- `--output FILE.html` — choose the output path.
- `--title "Title"` — override the Markdown H1.
- `--cover IMAGE` — display the local cover separately for manual upload to X.

The renderer uses only the Python standard library. It removes local images from the copied body because X cannot reliably ingest local image paths through rich-text paste.

### 4. Verify

- Confirm the English Markdown contains the source URL and correct account/date.
- Compare names, numbers, quotations, caveats, and section count against the source.
- Open or inspect the HTML and confirm it contains:
  - one article title,
  - the source note as a blockquote,
  - expected headings and links,
  - no raw Markdown markers such as `**text**` or `[text](url)` in the rendered article,
  - no local `<img>` elements inside the copied body.
- Tell the user to paste normally with `Ctrl+V`, not `Ctrl+Shift+V`.

## Output naming

Place outputs beside the source unless the user specifies another directory:

- `<slug>-x-article.md`
- `<slug>-x-rich-copy.html`

