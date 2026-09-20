#!/usr/bin/env python3
"""Check local Markdown links in the repository."""

from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote


LINK = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")


def main() -> int:
    root = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
    failures: list[str] = []

    for source in root.rglob("*.md"):
        if ".git" in source.parts:
            continue
        text = source.read_text(encoding="utf-8")
        for raw in LINK.findall(text):
            target = raw.strip().strip("<>")
            if target.startswith(("http://", "https://", "mailto:", "#")):
                continue
            target = unquote(target.split("#", 1)[0])
            if not target:
                continue
            resolved = (source.parent / target).resolve()
            if not resolved.exists():
                failures.append(f"{source.relative_to(root)} -> {raw}")

    if failures:
        print(f"link check failed: {len(failures)} unresolved link(s)")
        for failure in failures:
            print(failure)
        return 1

    print(f"link check passed: {root}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
