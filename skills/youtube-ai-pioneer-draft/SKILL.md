---
name: youtube-ai-pioneer-draft
description: End-to-end workflow for turning a YouTube video link into an AI Pioneer-style Chinese WeChat article with transcript extraction, real images, AI Pioneer fixed banners, local Markdown draft, and upload to the WeChat Official Account draft box. Use when the user gives a YouTube URL and asks to write/publish/send/upload/create an AI Pioneer 公众号文章、草稿箱、视频解读、播客总结、访谈深度稿, or says they want to drop a YouTube link and get a WeChat draft.
---

# YouTube to AI Pioneer Draft

Use this skill to handle the full path:

`YouTube URL -> transcript/materials -> AI Pioneer article -> images/banners -> WeChat draft upload`

Default workspace: `~/Documents/公众号`.

## Core Workflow

1. **Prepare materials**
   - Run `scripts/prepare_youtube_material.py` with the YouTube URL.
   - Save transcript/metadata under `原始素材/`.
   - Save thumbnail/images under `配图/<slug>/`.
   - Do not paste the full transcript in the chat; use it as source material.

2. **Write the article**
   - Write a Chinese AI Pioneer article in `草稿/<slug>.md`.
   - Prefer 2500-5000 Chinese characters for long expert interviews; shorten only if the user asks.
   - Use objective, logical, high-signal language. Avoid inflated words such as “封神、颠覆、命运、最危险、刺耳”.
   - First screen must answer: what is the video, why should readers care, what can they take away.
   - Build around one core judgment. For expert interviews, use this shape:
     - title with concrete tension
     - direct opening judgment
     - 3-5 numbered sections
     - each section: claim -> evidence from transcript -> reader/company/industry implication
     - restrained ending with one actionable question or observation

3. **Images**
   - First image: YouTube thumbnail from `prepare_youtube_material.py`.
   - Prefer real, traceable images: video screenshots, official pages, Wikimedia/official portraits, product screenshots, data-center/infrastructure photos from reliable sources.
   - If direct video frame extraction fails, use the thumbnail plus source-traceable related images. State source in short captions.
   - Keep image count purposeful; 4-6 content images are usually enough.

4. **AI Pioneer fixed banners**
   - Confirm these files exist in the workspace:
     - `配图/AI-Pioneer固定banner/01-header-logo.png`
     - `配图/AI-Pioneer固定banner/02-business-contact.png`
     - `配图/AI-Pioneer固定banner/03-about-services.png`
     - `配图/AI-Pioneer固定banner/04-follow-banner.png`
     - `配图/AI-Pioneer固定banner/05-star-guide.png`
   - Insert:
     - header logo immediately after H1
     - business-contact after first core image and caption
     - about/follow/star-guide after references

5. **Preflight**
   - Check every local image path exists.
   - Run `md2wechat inspect <markdown> --draft --upload --cover <cover> ...` when available.
   - Fix duplicate/missing image issues before upload.

6. **Upload**
   - Use `scripts/upload_ai_pioneer_draft.py` from this skill.
   - It wraps the workspace uploader at `scripts/wechat_draft_upload.py`.
   - It reads `WECHAT_APPID` and `WECHAT_APPSECRET` from environment first, then `~/.config/md2wechat/config.yaml`.
   - If the user supplies an AppSecret in chat, use it only as a temporary environment variable; do not write it to files or repeat it back.

## Commands

Prepare materials:

```bash
python3 ~/.codex/skills/youtube-ai-pioneer-draft/scripts/prepare_youtube_material.py \
  --url "https://www.youtube.com/watch?v=..." \
  --workspace ~/Documents/公众号 \
  --slug "short-topic-slug"
```

Upload draft:

```bash
python3 ~/.codex/skills/youtube-ai-pioneer-draft/scripts/upload_ai_pioneer_draft.py \
  --workspace ~/Documents/公众号 \
  --markdown "草稿/<slug>.md" \
  --cover "配图/<slug>/01-youtube-thumbnail.jpg" \
  --title "<final title>" \
  --digest "<digest under 128 chars>" \
  --output "草稿/<slug>_公众号草稿箱_result.json"
```

## Upload Failure Handling

- `40164 invalid ip`: tell the user the exact IP in the error and ask them to add it to the WeChat IP whitelist, then retry.
- `40125 invalid appsecret`: ask for the correct AppSecret or tell the user to update `~/.config/md2wechat/config.yaml`.
- Missing `WECHAT_APPID/WECHAT_APPSECRET`: read `~/.config/md2wechat/config.yaml`; if unavailable, ask the user for the missing value.
- Do not switch to Chrome/browser publishing unless the user explicitly authorizes browser-based publishing.

## Final Response

Report:

- whether draft upload succeeded
- draft `media_id`
- result JSON path
- Markdown path
- image count uploaded

If upload is blocked, report the blocker and the exact next action needed.
