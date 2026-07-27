#!/usr/bin/env python3
import argparse
import os
import subprocess
import sys
from pathlib import Path


def read_md2wechat_config():
    candidates = [
        Path.home() / ".config" / "md2wechat" / "config.yaml",
        Path.home() / ".md2wechat.yaml",
    ]
    values = {}
    for path in candidates:
        if not path.exists():
            continue
        for raw in path.read_text(encoding="utf-8", errors="ignore").splitlines():
            line = raw.strip()
            if not line or line.startswith("#") or ":" not in line:
                continue
            key, value = line.split(":", 1)
            values[key.strip()] = value.strip().strip("\"'")
        break
    return values


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--workspace",
        default=str(Path.home() / "Documents" / "公众号"),
    )
    parser.add_argument("--markdown", required=True)
    parser.add_argument("--cover", required=True)
    parser.add_argument("--title", required=True)
    parser.add_argument("--digest", required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument("--author", default="AI Pioneer")
    args = parser.parse_args()

    workspace = Path(args.workspace).resolve()
    uploader = workspace / "scripts" / "wechat_draft_upload.py"
    if not uploader.exists():
        raise SystemExit(f"Missing workspace uploader: {uploader}")

    cfg = read_md2wechat_config()
    env = os.environ.copy()
    appid = env.get("WECHAT_APPID") or cfg.get("appid")
    secret = (
        env.get("WECHAT_APPSECRET")
        or env.get("WECHAT_SECRET")
        or cfg.get("secret")
    )
    if not appid:
        raise SystemExit("Missing WECHAT_APPID and md2wechat appid.")
    if not secret:
        raise SystemExit("Missing WECHAT_APPSECRET/WECHAT_SECRET and md2wechat secret.")
    env["WECHAT_APPID"] = appid
    env["WECHAT_APPSECRET"] = secret

    cmd = [
        sys.executable,
        str(uploader),
        "--markdown",
        args.markdown,
        "--cover",
        args.cover,
        "--title",
        args.title,
        "--author",
        args.author,
        "--digest",
        args.digest,
        "--output",
        args.output,
    ]
    result = subprocess.run(cmd, cwd=str(workspace), env=env)
    raise SystemExit(result.returncode)


if __name__ == "__main__":
    main()
