#!/usr/bin/env python3
"""
Meta-Knowledge Lexicon Validator & CLI Search Tool
用于校验 references/ 目录下的元知识词典格式规范（供社区 PR 自动检查），并支持按大白话痛点关键词快速检索对应的“专业词钥匙”。
"""

import argparse
import pathlib
import re
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8")

ROOT_DIR = pathlib.Path(__file__).resolve().parent.parent
REFERENCES_DIR = ROOT_DIR / "references"

REQUIRED_SECTIONS = [
    "概念出处",
    "用户大白话痛点",
    "行业隐性共识",
    "核心执行准则",
]


def parse_keys_from_markdown(md_path: pathlib.Path) -> list[dict]:
    content = md_path.read_text(encoding="utf-8")
    blocks = re.split(r"^##\s+🔑\s+", content, flags=re.MULTILINE)
    keys = []
    for block in blocks[1:]:
        lines = block.strip().splitlines()
        title = lines[0].strip()
        body = "\n".join(lines[1:])
        missing = [req for req in REQUIRED_SECTIONS if req not in body]
        keys.append({
            "file": md_path.name,
            "title": title,
            "body": body,
            "missing_sections": missing,
        })
    return keys


def validate_all() -> int:
    if not REFERENCES_DIR.exists():
        print(f"[ERROR] 找不到词典目录: {REFERENCES_DIR}", file=sys.stderr)
        return 1

    md_files = sorted(REFERENCES_DIR.glob("*.md"))
    if not md_files:
        print("[ERROR] references/ 目录下没有任何 .md 词典文件", file=sys.stderr)
        return 1

    total_keys = 0
    errors = 0
    print("=" * 65)
    print("🔍 元知识词典规范校验报告 (Meta-Knowledge Lexicon Validator)")
    print("=" * 65)

    for md_file in md_files:
        keys = parse_keys_from_markdown(md_file)
        print(f"📘 {md_file.name}: 共收录 {len(keys)} 把专业词钥匙")
        total_keys += len(keys)
        for k in keys:
            if k["missing_sections"]:
                errors += 1
                print(
                    f"  ❌ [{k['title']}] 缺少必填字段: {', '.join(k['missing_sections'])}"
                )
            elif "(" not in k["title"] or ")" not in k["title"]:
                errors += 1
                print(
                    f"  ❌ [{k['title']}] 标题需包含英文专业术语对照，格式如：钥匙 XX：中文名 (English Term)"
                )

    print("-" * 65)
    print(f"✅ 总计扫描分册: {len(md_files)} 个 | 收录高密度专业词钥匙: {total_keys} 把")
    if errors > 0:
        print(f"❌ 发现 {errors} 处格式不规范，请按 CONTRIBUTING.md 修正。")
        return 1
    print("🎉 所有元知识钥匙均符合「大白话痛点 -> 行业隐性共识 -> 专业词 -> 核心执行准则」标准！")
    return 0


def search_keyword(query: str) -> None:
    md_files = sorted(REFERENCES_DIR.glob("*.md"))
    matches = []
    for md_file in md_files:
        for k in parse_keys_from_markdown(md_file):
            if query.lower() in k["title"].lower() or query.lower() in k["body"].lower():
                matches.append(k)

    print(f"🔎 搜索关键词「{query}」，共匹配到 {len(matches)} 把元知识钥匙：\n")
    for idx, m in enumerate(matches, 1):
        print(f"[{idx}] 🔑 {m['title']}  (来源: {m['file']})")
        for line in m["body"].splitlines():
            if "用户大白话痛点" in line or "行业隐性共识" in line or line.strip().startswith("1."):
                print(f"    {line.strip()}")
        print()


def main() -> None:
    parser = argparse.ArgumentParser(
        description="校验或检索 Meta-Knowledge Prompt Translator 词典库"
    )
    parser.add_argument(
        "--validate", action="store_true", help="校验所有词典分册是否符合开源格式规范"
    )
    parser.add_argument(
        "--search", "-s", type=str, help="按大白话痛点或专业词检索钥匙（如：'界面'、'PPT'、'动画'）"
    )
    args = parser.parse_args()

    if args.search:
        search_keyword(args.search)
    else:
        sys.exit(validate_all())


if __name__ == "__main__":
    main()
