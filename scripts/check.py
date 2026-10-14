#!/usr/bin/env python3
"""Verify key accessibility structure and local resource references."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit, unquote

ROOT = Path(__file__).resolve().parents[1] / "dist"
class Check(HTMLParser):
    def __init__(self):
        super().__init__()
        self.headings = 0
        self.main = 0
        self.language = False
        self.resources = []
    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        self.headings += tag == "h1"
        self.main += tag == "main"
        if tag == "html":
            self.language = bool(attrs.get("lang"))
        if tag == "img" and "alt" not in attrs:
            raise SystemExit("Every image needs an alt attribute.")
        for key in ("href", "src"):
            if attrs.get(key):
                self.resources.append(attrs[key])

for page in ROOT.rglob("*.html"):
    check = Check()
    check.feed(page.read_text())
    if check.headings != 1 or check.main != 1 or not check.language:
        raise SystemExit(f"{page.name}: expected one h1, one main, and a page language.")
    for resource in check.resources:
        url = urlsplit(resource)
        if not url.scheme and not url.netloc and url.path:
            if url.path.startswith("/"):
                raise SystemExit("Use relative paths so project Pages URLs work.")
            target = (page.parent / unquote(url.path)).resolve()
            if not target.is_relative_to(ROOT.resolve()) or not target.is_file():
                raise SystemExit(f"Missing or invalid local resource: {resource}")
print("Checks passed: page structure and local resources.")
