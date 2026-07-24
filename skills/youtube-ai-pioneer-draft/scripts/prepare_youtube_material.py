#!/usr/bin/env python3
import argparse
import html
import json
import re
import subprocess
import sys
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import parse_qs, urlparse
from urllib.request import Request, urlopen


TMP_DEPS = Path("/tmp/codex_youtube_transcript")


def ensure_transcript_api():
    if TMP_DEPS.exists() and str(TMP_DEPS) not in sys.path:
        sys.path.insert(0, str(TMP_DEPS))
    try:
        from youtube_transcript_api import YouTubeTranscriptApi  # type: ignore

        return YouTubeTranscriptApi
    except ModuleNotFoundError:
        TMP_DEPS.mkdir(parents=True, exist_ok=True)
        subprocess.run(
            [
                sys.executable,
                "-m",
                "pip",
                "install",
                "--target",
                str(TMP_DEPS),
                "--upgrade",
                "youtube-transcript-api",
            ],
            check=True,
        )
        sys.path.insert(0, str(TMP_DEPS))
        from youtube_transcript_api import YouTubeTranscriptApi  # type: ignore

        return YouTubeTranscriptApi


def video_id_from_url(value):
    value = value.strip()
    if re.fullmatch(r"[A-Za-z0-9_-]{11}", value):
        return value
    parsed = urlparse(value)
    host = parsed.netloc.lower()
    if "youtu.be" in host:
        return parsed.path.strip("/").split("/")[0]
    if "youtube.com" in host:
        if parsed.path == "/watch":
            return parse_qs(parsed.query).get("v", [""])[0]
        parts = [p for p in parsed.path.split("/") if p]
        for marker in ("shorts", "embed", "live"):
            if marker in parts:
                idx = parts.index(marker)
                if idx + 1 < len(parts):
                    return parts[idx + 1]
    raise SystemExit(f"Could not parse YouTube video id from: {value}")


def fetch_text(url):
    req = Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urlopen(req, timeout=30) as res:
        return res.read().decode("utf-8", errors="replace")


def fetch_bytes(url):
    req = Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urlopen(req, timeout=30) as res:
        return res.read()


def extract_title(page, video_id):
    patterns = [
        r'<meta property="og:title" content="(.*?)"',
        r"<title>(.*?)</title>",
    ]
    for pattern in patterns:
        match = re.search(pattern, page, re.S)
        if match:
            title = html.unescape(match.group(1))
            title = re.sub(r"\s+-\s+YouTube\s*$", "", title).strip()
            if title:
                return title
    return video_id


def slugify(value, fallback):
    value = re.sub(r"\s+", "-", value.strip().lower())
    value = re.sub(r"[^a-z0-9\u4e00-\u9fff_-]+", "", value)
    value = re.sub(r"-{2,}", "-", value).strip("-_")
    return value[:80] or fallback


def snippet_text(snippet):
    if hasattr(snippet, "text"):
        return snippet.text
    return snippet.get("text", "")


def snippet_start(snippet):
    if hasattr(snippet, "start"):
        return float(snippet.start)
    return float(snippet.get("start", 0))


def format_ts(seconds):
    seconds = int(seconds)
    h, rem = divmod(seconds, 3600)
    m, s = divmod(rem, 60)
    if h:
        return f"{h:02d}:{m:02d}:{s:02d}"
    return f"{m:02d}:{s:02d}"


def get_transcript(video_id, languages):
    YouTubeTranscriptApi = ensure_transcript_api()
    api = YouTubeTranscriptApi()
    transcript_list = api.list(video_id)
    chosen = None
    try:
        chosen = transcript_list.find_transcript(languages)
    except Exception:
        for transcript in transcript_list:
            chosen = transcript
            break
    if chosen is None:
        raise RuntimeError("No transcript found.")
    fetched = chosen.fetch()
    snippets = list(fetched)
    return chosen, snippets


def download_thumbnail(video_id, out_dir):
    candidates = [
        f"https://i.ytimg.com/vi/{video_id}/maxresdefault.jpg",
        f"https://i.ytimg.com/vi/{video_id}/sddefault.jpg",
        f"https://i.ytimg.com/vi/{video_id}/hqdefault.jpg",
    ]
    for url in candidates:
        try:
            data = fetch_bytes(url)
            if len(data) < 1000:
                continue
            path = out_dir / "01-youtube-thumbnail.jpg"
            path.write_bytes(data)
            return path, url
        except (HTTPError, URLError):
            continue
    return None, None


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", required=True)
    parser.add_argument("--workspace", default=".")
    parser.add_argument("--slug", default="")
    parser.add_argument(
        "--languages",
        default="en,zh-Hans,zh-CN,zh",
        help="Comma-separated preferred transcript languages.",
    )
    args = parser.parse_args()

    workspace = Path(args.workspace).resolve()
    video_id = video_id_from_url(args.url)
    page = fetch_text(f"https://www.youtube.com/watch?v={video_id}")
    title = extract_title(page, video_id)
    slug = args.slug or slugify(title, video_id)

    source_dir = workspace / "原始素材"
    image_dir = workspace / "配图" / slug
    source_dir.mkdir(parents=True, exist_ok=True)
    image_dir.mkdir(parents=True, exist_ok=True)

    languages = [x.strip() for x in args.languages.split(",") if x.strip()]
    transcript, snippets = get_transcript(video_id, languages)
    transcript_path = source_dir / f"{slug}-youtube-transcript.txt"
    with transcript_path.open("w", encoding="utf-8") as f:
        f.write(f"URL: https://www.youtube.com/watch?v={video_id}\n")
        f.write(f"TITLE: {title}\n")
        f.write(
            f"TRANSCRIPT: {getattr(transcript, 'language_code', '')} "
            f"{getattr(transcript, 'language', '')}\n\n"
        )
        for snippet in snippets:
            text = html.unescape(snippet_text(snippet)).replace("\n", " ").strip()
            if text:
                f.write(f"[{format_ts(snippet_start(snippet))}] {text}\n")

    thumbnail_path, thumbnail_source = download_thumbnail(video_id, image_dir)
    word_count = sum(len(snippet_text(s).split()) for s in snippets)
    metadata = {
        "video_id": video_id,
        "url": f"https://www.youtube.com/watch?v={video_id}",
        "title": title,
        "slug": slug,
        "transcript_path": str(transcript_path),
        "image_dir": str(image_dir),
        "thumbnail_path": str(thumbnail_path) if thumbnail_path else None,
        "thumbnail_source": thumbnail_source,
        "snippet_count": len(snippets),
        "word_count_approx": word_count,
        "language_code": getattr(transcript, "language_code", ""),
        "language": getattr(transcript, "language", ""),
        "is_generated": getattr(transcript, "is_generated", None),
    }
    metadata_path = source_dir / f"{slug}-youtube-metadata.json"
    metadata_path.write_text(json.dumps(metadata, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(metadata, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
