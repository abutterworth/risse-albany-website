#!/usr/bin/env python3
"""Build the static website with Python's standard library."""
from pathlib import Path
from string import Template
from urllib.parse import urlsplit
import html
import json
import shutil

ROOT = Path(__file__).resolve().parents[1]
data = json.loads((ROOT / "content/site.json").read_text())
required = {"title", "description", "heading", "intro", "notice", "link_label", "link_url"}
if set(data) != required or any(not isinstance(v, str) or not v.strip() for v in data.values()):
    raise SystemExit("site.json must contain all documented fields as nonempty strings.")
url = urlsplit(data["link_url"])
if url.scheme != "https" or not url.netloc:
    raise SystemExit("link_url must be an absolute HTTPS URL.")
output = ROOT / "dist"
output.mkdir(exist_ok=True)
page = Template((ROOT / "templates/index.html").read_text()).substitute(
    {key: html.escape(value, quote=True) for key, value in data.items()}
)
(output / "index.html").write_text(page)
shutil.copytree(ROOT / "assets", output / "assets", dirs_exist_ok=True)
(output / ".nojekyll").touch()
print("Built dist/index.html")
