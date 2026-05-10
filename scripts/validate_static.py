#!/usr/bin/env python3
"""Lightweight static validations for awesome-openclaw.

No third-party dependencies. Checks:
- JSON files parse.
- HTML files are parseable by Python's stdlib HTMLParser.
- Vercel static rewrite destinations exist.
- README internal anchors work for GitHub-style headings.
- README anchors that the website will render are reported if the website slugger differs.
"""
from __future__ import annotations

from html.parser import HTMLParser
from pathlib import Path
import json
import re
import sys

ROOT = Path(__file__).resolve().parents[1]


def fail(msg: str) -> None:
    print(f"ERROR: {msg}", file=sys.stderr)
    raise SystemExit(1)


def github_slug(text: str, counts: dict[str, int]) -> str:
    base = re.sub(r"<[^>]+>", "", text).strip().lower()
    base = re.sub(r"[^a-z0-9 -]", "", base)
    # GitHub removes punctuation before replacing each whitespace character,
    # so headings like "Serverless & PaaS" become "serverless--paas".
    base = re.sub(r"\s", "-", base).strip("-")
    n = counts.get(base, 0)
    counts[base] = n + 1
    return base if n == 0 else f"{base}-{n}"


def website_slug(text: str, counts: dict[str, int]) -> str:
    # Mirror docs/website/index.html after the SEO/anchor PR.
    return github_slug(text, counts)


def check_json() -> None:
    for path in ROOT.rglob("*.json"):
        if ".git" in path.parts:
            continue
        try:
            json.loads(path.read_text())
        except Exception as exc:
            fail(f"Invalid JSON in {path.relative_to(ROOT)}: {exc}")
    print("JSON OK")


class Parser(HTMLParser):
    pass


def check_html() -> None:
    for path in list((ROOT / "docs" / "website").glob("*.html")) + list((ROOT / "docs" / "blog").glob("*.html")) + list((ROOT / "docs" / "public").rglob("*.html")):
        parser = Parser()
        try:
            parser.feed(path.read_text(errors="ignore"))
        except Exception as exc:
            fail(f"HTML parse issue in {path.relative_to(ROOT)}: {exc}")
    print("HTML parse OK")


def check_vercel() -> None:
    config = json.loads((ROOT / "vercel.json").read_text())
    missing: list[tuple[str, str]] = []
    for rewrite in config.get("rewrites", []):
        dest = rewrite.get("destination", "")
        if ":" in dest:
            continue
        p = ROOT / dest.lstrip("/")
        if not p.exists():
            missing.append((rewrite.get("source", ""), dest))
    if missing:
        fail("Missing Vercel rewrite destinations: " + repr(missing))
    print("Vercel rewrites OK")


def heading_anchors(markdown: str, slug_fn) -> set[str]:
    counts: dict[str, int] = {}
    anchors: set[str] = set()
    for line in markdown.splitlines():
        match = re.match(r"^(#{1,6})\s+(.+?)\s*$", line)
        if match:
            anchors.add(slug_fn(match.group(2), counts))
    return anchors


def readme_links(markdown: str) -> list[str]:
    return re.findall(r"\[[^\]]+\]\(#([^)]+)\)", markdown)


def check_readme_anchors() -> None:
    readme = (ROOT / "README.md").read_text(errors="ignore")
    links = readme_links(readme)
    gh_anchors = heading_anchors(readme, github_slug)
    bad = [link for link in links if link not in gh_anchors]
    if bad:
        fail("README GitHub anchor links are broken: " + ", ".join(bad))
    web_anchors = heading_anchors(readme, website_slug)
    web_bad = [link for link in links if link not in web_anchors]
    if web_bad:
        fail("README website-rendered anchor links are broken: " + ", ".join(web_bad))
    print("README anchors OK")


def main() -> None:
    check_json()
    check_html()
    check_vercel()
    check_readme_anchors()
    print("All static validations passed")


if __name__ == "__main__":
    main()
