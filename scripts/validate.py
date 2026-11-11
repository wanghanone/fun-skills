#!/usr/bin/env python3
"""Validate skills/ against the Agent Skills spec and this repo's conventions.

Runs with a plain python3 (standard library only), both locally and in CI.

Usage:
    python3 scripts/validate.py
    python3 scripts/validate.py --check-readme
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILLS_DIR = ROOT / "skills"
MARKETPLACE = ROOT / ".claude-plugin" / "marketplace.json"
README = ROOT / "README.md"

NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
KNOWN_FIELDS = {
    "name", "description", "license", "compatibility", "metadata", "allowed-tools"
}
LINK_RE = re.compile(r"\]\(([^)]+)\)")
PRIVATE_FILES = {"_user_meta.json"}
PRIVATE_DIRS = {"agents"}
FORBIDDEN_PATH_HINTS = ("/Users/", "/home/", ":\\", "C:/")
IMAGE_SUFFIXES = {".png", ".jpg", ".jpeg", ".gif", ".webp"}

errors: list[str] = []
warnings: list[str] = []


def err(skill: str, msg: str) -> None:
    errors.append(f"{skill}: {msg}")


def warn(skill: str, msg: str) -> None:
    warnings.append(f"{skill}: {msg}")


def parse_frontmatter(text: str):
    """Return (fields, body_start_line, error). No PyYAML needed for flat fields."""
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return None, 0, "SKILL.md 必须以 --- 开头的 YAML frontmatter 起始"
    end = None
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            end = i
            break
    if end is None:
        return None, 0, "frontmatter 缺少结束的 ---"
    fields = {}
    for line in lines[1:end]:
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue
        match = re.match(r"^([A-Za-z][A-Za-z0-9_-]*):\s*(.*)$", line)
        if match:
            value = match.group(2).strip().strip('"').strip("'")
            fields[match.group(1)] = value
    return fields, end + 1, None


def validate_skill(skill_dir: Path) -> None:
    name = skill_dir.name
    skill_md = skill_dir / "SKILL.md"
    if not skill_md.is_file():
        err(name, "缺少 SKILL.md")
        return

    text = skill_md.read_text(encoding="utf-8")
    fields, body_start, problem = parse_frontmatter(text)
    if problem:
        err(name, problem)
        return

    skill_name = fields.get("name", "")
    if not skill_name:
        err(name, "frontmatter 缺少 name")
    else:
        if len(skill_name) > 64:
            err(name, f"name 超过 64 字符: {len(skill_name)}")
        if not NAME_RE.match(skill_name):
            err(name, f"name 只能用小写字母、数字与单个连字符: {skill_name}")
        if skill_name != name:
            err(name, f"name({skill_name}) 必须与目录名({name})一致")

    description = fields.get("description", "")
    if not description:
        err(name, "frontmatter 缺少 description")
    elif len(description) > 1024:
        err(name, f"description 超过 1024 字符: {len(description)}")

    compatibility = fields.get("compatibility", "")
    if compatibility and len(compatibility) > 500:
        err(name, "compatibility 超过 500 字符")

    for key in fields:
        if key not in KNOWN_FIELDS:
            warn(name, f"未知的 frontmatter 字段: {key}")

    body_lines = len(text.splitlines()) - body_start
    if body_lines >= 500:
        err(name, f"SKILL.md 正文 {body_lines} 行，建议拆到 references/ 并控制在 500 行内")

    if any(hint in text for hint in FORBIDDEN_PATH_HINTS):
        err(name, "SKILL.md 含本机绝对路径，请改用相对路径")

    for target in LINK_RE.findall(text):
        path = target.split("#")[0].strip()
        if not path or path.startswith(("http://", "https://", "mailto:", "/", "#")):
            continue
        if not (skill_dir / path).exists():
            err(name, f"SKILL.md 引用的文件不存在: {path}")

    if not (skill_dir / "README.md").is_file():
        err(name, "缺少给人看的 README.md（效果截图、依赖、快速开始）")

    examples = skill_dir / "examples"
    if not examples.is_dir():
        warn(name, "建议建立 examples/ 目录存放成品图")
    elif not any(p.suffix.lower() in IMAGE_SUFFIXES for p in examples.iterdir()):
        warn(name, "examples/ 里还没有效果图片")

    for path in skill_dir.rglob("*"):
        if path.is_file() and path.name in PRIVATE_FILES:
            err(name, f"含平台私有文件: {path.relative_to(skill_dir)}")
        if path.is_dir() and path.name in PRIVATE_DIRS:
            err(name, f"含平台私有目录: {path.relative_to(skill_dir)}")


def check_index(skill_names: list[str]) -> None:
    """Keep README table and marketplace.json in sync with skills/."""
    if not README.is_file():
        err("README", "缺少根目录 README.md")
        return
    readme = README.read_text(encoding="utf-8")
    for name in skill_names:
        if name not in readme:
            err("README", f"技能目录表缺少 {name}")

    if not MARKETPLACE.is_file():
        err("marketplace", "缺少 .claude-plugin/marketplace.json")
        return
    try:
        data = json.loads(MARKETPLACE.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        err("marketplace", f"JSON 解析失败: {exc}")
        return

    listed: set[str] = set()
    for plugin in data.get("plugins", []):
        for entry in plugin.get("skills", []):
            listed.add(Path(entry).name)
            if not (ROOT / entry).is_dir():
                err("marketplace", f"引用的技能目录不存在: {entry}")
    for name in set(skill_names) - listed:
        err("marketplace", f"未登记技能: {name}")
    for name in listed - set(skill_names):
        err("marketplace", f"登记了不存在的技能: {name}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--check-readme", action="store_true",
        help="also verify README table and marketplace.json match skills/"
    )
    args = parser.parse_args()

    if not SKILLS_DIR.is_dir():
        err("repo", "找不到 skills/ 目录")
    skill_dirs = sorted(p for p in SKILLS_DIR.iterdir() if p.is_dir()) if SKILLS_DIR.is_dir() else []
    if not skill_dirs:
        err("repo", "skills/ 下没有任何技能")

    print(f"Checking {len(skill_dirs)} skill(s)...")
    for skill_dir in skill_dirs:
        validate_skill(skill_dir)

    if args.check_readme:
        check_index([p.name for p in skill_dirs])

    for msg in errors:
        print(f"  [ERROR] {msg}")
    for msg in warnings:
        print(f"  [WARN]  {msg}")
    for skill_dir in skill_dirs:
        if not any(m.startswith(skill_dir.name + ":") for m in errors):
            print(f"  [OK]    {skill_dir.name}")

    if args.check_readme and not any(m.startswith(("README:", "marketplace:")) for m in errors):
        print("  [OK]    README / marketplace.json 索引一致")

    print(f"Errors: {len(errors)}, Warnings: {len(warnings)}")
    if errors:
        print("Validation failed.")
        return 1
    print("All checks passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
