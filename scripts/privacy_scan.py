#!/usr/bin/env python3
"""Fail when public files contain common secrets or private identifiers."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


TEXT_EXTENSIONS = {
    ".md", ".txt", ".py", ".sh", ".js", ".ts", ".json", ".yml", ".yaml",
    ".toml", ".html", ".css", ".xml", ".csv",
}
SKIP_PARTS = {".git", "__pycache__", ".idea", ".vscode"}


def default_patterns() -> list[tuple[str, re.Pattern[str]]]:
    private_key = "-----BEGIN " + "PRIVATE KEY-----"
    return [
        ("absolute home path", re.compile(r"(?:/Users|/home)/[A-Za-z0-9._-]+/")),
        ("Windows home path", re.compile(r"[A-Za-z]:\\Users\\[^\\\s]+\\")),
        ("GitHub token", re.compile(r"\b(?:gh[pousr]_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,})\b")),
        ("API key", re.compile(r"\bsk-[A-Za-z0-9_-]{20,}\b")),
        ("Bearer token", re.compile(r"\bBearer\s+[A-Za-z0-9._~-]{20,}\b", re.IGNORECASE)),
        ("private key", re.compile(re.escape(private_key))),
        ("email address", re.compile(r"\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b", re.IGNORECASE)),
        ("possible phone number", re.compile(r"(?<!\d)1[3-9]\d{9}(?!\d)")),
    ]


def iter_files(root: Path):
    for path in root.rglob("*"):
        if not path.is_file() or any(part in SKIP_PARTS for part in path.parts):
            continue
        if path.suffix.lower() not in TEXT_EXTENSIONS:
            continue
        if path.stat().st_size > 2_000_000:
            continue
        yield path


def scan(root: Path, denied_terms: list[str]) -> list[tuple[Path, int, str, str]]:
    patterns = default_patterns()
    patterns.extend(
        (f"denied term: {term}", re.compile(re.escape(term), re.IGNORECASE))
        for term in denied_terms
        if term.strip()
    )
    findings: list[tuple[Path, int, str, str]] = []
    allowed_email_domains = {"users.noreply.github.com"}

    for path in iter_files(root):
        try:
            lines = path.read_text(encoding="utf-8").splitlines()
        except UnicodeDecodeError:
            continue
        for line_number, line in enumerate(lines, start=1):
            for label, pattern in patterns:
                for match in pattern.finditer(line):
                    value = match.group(0)
                    if label == "email address" and value.rsplit("@", 1)[-1].lower() in allowed_email_domains:
                        continue
                    preview = line.strip()
                    if len(preview) > 180:
                        preview = preview[:177] + "..."
                    findings.append((path, line_number, label, preview))
    return findings


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", nargs="?", default=".", help="Directory to scan")
    parser.add_argument("--deny", action="append", default=[], help="Additional case-insensitive term to reject")
    args = parser.parse_args()

    root = Path(args.path).resolve()
    findings = scan(root, args.deny)
    if findings:
        print(f"privacy scan failed: {len(findings)} finding(s)")
        for path, line, label, preview in findings:
            print(f"{path.relative_to(root)}:{line}: {label}: {preview}")
        return 1

    print(f"privacy scan passed: {root}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
