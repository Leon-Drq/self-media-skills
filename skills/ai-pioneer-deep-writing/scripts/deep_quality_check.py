#!/usr/bin/env python3
"""Heuristic quality gate for AI Pioneer deep articles.

This script does not judge taste. It catches common measurable failures:
thin body, too few images, report-like paragraph blocks, weak sourcing, and
phrases that often signal meta-commentary instead of reader-facing prose.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


BANNED_PATTERNS = [
    r"这件事真正值得关注的是",
    r"真正值得关注的是",
    r"如果只看成",
    r"就写小了",
    r"这里有个反常识",
    r"这很容易被写成",
    r"最容易被讲成",
    r"最容易被传播成",
    r"但这么说太快",
    r"但这么说太粗",
    r"更准确的说法是",
    r"这不是一个玄学问题",
    r"下面我们来",
    r"今天我们来聊",
    r"综上所述",
    r"总而言之",
    r"标志着.*新阶段",
    r"深刻影响.*未来",
]

REPORT_WORDS = [
    "核心变量",
    "价值迁移",
    "底层逻辑",
    "范式转移",
    "赋能",
    "抓手",
    "闭环",
    "生态位",
]


def is_content_para(line: str) -> bool:
    stripped = line.strip()
    if not stripped:
        return False
    if stripped.startswith("#"):
        return False
    if stripped.startswith("!["):
        return False
    if stripped.startswith("http://") or stripped.startswith("https://"):
        return False
    if stripped.startswith("图源") or stripped.startswith("资料参考"):
        return False
    if stripped.startswith("|") and stripped.endswith("|"):
        return False
    return True


def cjk_len(text: str) -> int:
    return len(re.findall(r"[\u4e00-\u9fff]", text))


def count_fact_anchors(text: str) -> int:
    patterns = [
        r"\d{4}\s*年",
        r"\d+(\.\d+)?\s*%",
        r"\d+/\d+",
        r"\b[A-Za-z]+[- ]?\d+(\.\d+)?\b",
        r"论文",
        r"报告",
        r"官方",
        r"GitHub",
        r"benchmark",
        r"eval",
        r"测试",
        r"实验",
        r"数据显示",
    ]
    total = 0
    for pat in patterns:
        total += len(re.findall(pat, text, flags=re.IGNORECASE))
    return total


def analyze(path: Path) -> dict[str, object]:
    text = path.read_text(encoding="utf-8")
    lines = [line.rstrip() for line in text.splitlines()]
    paras = [line.strip() for line in lines if is_content_para(line)]
    body = "\n".join(paras)
    para_lens = [cjk_len(p) for p in paras if cjk_len(p) > 0]
    image_count = len(re.findall(r"!\[[^\]]*\]\([^)]+\)", text))
    url_count = len(re.findall(r"https?://[^\s)]+", text))
    short_count = sum(1 for n in para_lens if n <= 25)
    long_count = sum(1 for n in para_lens if n >= 120)
    banned = [p for p in BANNED_PATTERNS if re.search(p, text)]
    report_words = [w for w in REPORT_WORDS if w in text]
    return {
        "path": str(path),
        "cjk_chars": cjk_len(body),
        "paragraphs": len(para_lens),
        "avg_para_cjk": round(sum(para_lens) / max(len(para_lens), 1), 1),
        "short_para_rate": round(short_count / max(len(para_lens), 1), 2),
        "long_paragraphs": long_count,
        "images": image_count,
        "urls": url_count,
        "fact_anchors": count_fact_anchors(body),
        "questions": body.count("？") + body.count("?"),
        "quotes": body.count("“") + body.count("「"),
        "banned_phrases": banned,
        "report_words": report_words,
    }


def check(stats: dict[str, object], args: argparse.Namespace) -> list[tuple[str, str]]:
    failures: list[tuple[str, str]] = []
    warnings: list[tuple[str, str]] = []

    def fail(cond: bool, name: str, msg: str) -> None:
        if cond:
            failures.append((name, msg))

    def warn(cond: bool, name: str, msg: str) -> None:
        if cond:
            warnings.append((name, msg))

    fail(stats["cjk_chars"] < args.min_chars, "length", f"body has {stats['cjk_chars']} CJK chars; target >= {args.min_chars}")
    fail(stats["images"] < args.min_images, "images", f"{stats['images']} images; target >= {args.min_images}")
    fail(stats["urls"] < args.min_urls, "sources", f"{stats['urls']} source URLs; target >= {args.min_urls}")
    fail(stats["fact_anchors"] < args.min_facts, "facts", f"{stats['fact_anchors']} fact anchors; target >= {args.min_facts}")
    fail(stats["avg_para_cjk"] > args.max_avg_para, "rhythm", f"avg paragraph {stats['avg_para_cjk']} CJK chars; target <= {args.max_avg_para}")
    warn(stats["short_para_rate"] < args.min_short_rate, "short-paragraph-rate", f"short paragraph rate {stats['short_para_rate']}; target >= {args.min_short_rate}")
    warn(stats["long_paragraphs"] > args.max_long_paras, "long-paragraphs", f"{stats['long_paragraphs']} long paragraphs; target <= {args.max_long_paras}")
    warn(bool(stats["report_words"]), "report-words", "report-like words found: " + ", ".join(stats["report_words"]))
    fail(bool(stats["banned_phrases"]), "banned-phrases", "reader-facing meta phrases found: " + ", ".join(stats["banned_phrases"]))

    return [("FAIL", f"{name}: {msg}") for name, msg in failures] + [("WARN", f"{name}: {msg}") for name, msg in warnings]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("article", type=Path)
    parser.add_argument("--min-chars", type=int, default=4500)
    parser.add_argument("--min-images", type=int, default=10)
    parser.add_argument("--min-urls", type=int, default=5)
    parser.add_argument("--min-facts", type=int, default=8)
    parser.add_argument("--max-avg-para", type=float, default=48)
    parser.add_argument("--min-short-rate", type=float, default=0.32)
    parser.add_argument("--max-long-paras", type=int, default=8)
    parser.add_argument("--strict", action="store_true")
    args = parser.parse_args()

    stats = analyze(args.article)
    issues = check(stats, args)

    print("AI Pioneer deep article quality check")
    print("=" * 44)
    for key, value in stats.items():
        if key == "path":
            continue
        print(f"{key}: {value}")

    if issues:
        print("\nIssues")
        for level, msg in issues:
            print(f"{level}: {msg}")
    else:
        print("\nPASS: no measurable issues found.")

    has_fail = any(level == "FAIL" for level, _ in issues)
    return 1 if args.strict and has_fail else 0


if __name__ == "__main__":
    sys.exit(main())
