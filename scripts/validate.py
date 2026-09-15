"""Dependency-free repository validation for the production toolkit."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from typing import Iterable

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = (
    "README.md",
    "LICENSE",
    "CONTRIBUTING.md",
    "CODE_OF_CONDUCT.md",
    "docs/workflow.md",
    "docs/compositions.md",
    "docs/expressions.md",
    "docs/essential-graphics.md",
    "docs/render-queue.md",
    "docs/color-management.md",
    "docs/audio-handoff.md",
    "docs/version-compatibility.md",
    "docs/troubleshooting.md",
    "docs/team-handoff.md",
    "docs/naming-conventions.md",
    "templates/project-manifest.json",
    "templates/mogrt-manifest.json",
    "templates/review-checklist.md",
)
LINK_RE = re.compile(r"\[[^\]]+\]\(([^)]+)\)")


def markdown_files() -> Iterable[Path]:
    return (p for p in ROOT.rglob("*.md") if ".git" not in p.parts)


def check_required(errors: list[str]) -> None:
    for relative in REQUIRED:
        if not (ROOT / relative).is_file():
            errors.append("missing required file: " + relative)


def check_links(errors: list[str]) -> None:
    for source in markdown_files():
        for target in LINK_RE.findall(source.read_text(encoding="utf-8")):
            if target.startswith(("http://", "https://", "#", "mailto:")):
                continue
            path = target.split("#", 1)[0]
            if path and not (source.parent / path).resolve().is_file():
                errors.append(f"broken link: {source.relative_to(ROOT)} -> {target}")


def check_json(errors: list[str]) -> None:
    for path in (ROOT / "templates").glob("*.json"):
        try:
            json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as exc:
            errors.append(f"invalid JSON {path.relative_to(ROOT)}: {exc}")


def check_placeholders(errors: list[str]) -> None:
    for path in (ROOT / "examples").glob("*"):
        if path.is_file() and "PLACEHOLDER" not in path.read_text(encoding="utf-8"):
            errors.append(f"example should identify editable placeholders: {path.relative_to(ROOT)}")


def main() -> int:
    errors: list[str] = []
    check_required(errors)
    check_links(errors)
    check_json(errors)
    check_placeholders(errors)
    if errors:
        print("\n".join("ERROR: " + error for error in errors))
        return 1
    print("Validation passed: required files, local links, JSON templates, and examples checked.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

