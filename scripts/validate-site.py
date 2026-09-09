"""Validate generated page and asset paths before packaging a private preview."""
from html.parser import HTMLParser
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit


class Page(HTMLParser):
    def __init__(self, text):
        super().__init__()
        self.refs = []
        self.ids = set()
        self.styles = []
        self.feed(text)

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if "id" in attrs:
            self.ids.add(attrs["id"])
        if tag == "link" and attrs.get("rel") == "stylesheet":
            self.styles.append(attrs.get("href", ""))
        self.refs.extend(attrs[key] for key in ("href", "src") if attrs.get(key))


root = Path(sys.argv[1] if len(sys.argv) > 1 else "dist").resolve()
pages = {path: Page(path.read_text()) for path in root.rglob("*.html")}
errors = []
if root / "index.html" not in pages:
    errors.append("Missing home page")


def validate_ref(source, ref):
    if re.search(r"/https?:", ref):
        errors.append(f"{source.name}: malformed host inside path: {ref}")
        return
    url = urlsplit(ref)
    if url.scheme or url.netloc:
        return
    path = unquote(url.path)
    target = ((root / path.lstrip("/")) if path.startswith("/")
              else (source.parent / path if path else source)).resolve()
    if not target.is_relative_to(root):
        errors.append(f"{source.name}: reference escapes site: {ref}")
        return
    if target.is_dir():
        target /= "index.html"
    if not target.is_file():
        errors.append(f"{source.name}: missing local resource: {ref}")
    elif url.fragment and target in pages and unquote(url.fragment) not in pages[target].ids:
        errors.append(f"{source.name}: missing anchor: {ref}")


for path, page in pages.items():
    if not page.styles:
        errors.append(f"{path.name}: no stylesheet linked")
    for ref in page.refs:
        validate_ref(path, ref)

for path in root.rglob("*.css"):
    for ref in re.findall(r"url\([\"']?([^\)\"']+)", path.read_text()):
        validate_ref(path, ref)

for path in root.glob("*.xml"):
    if re.search(r"/https?:|localhost:4000|127\.0\.0\.1:4000", path.read_text()):
        errors.append(f"{path.name}: invalid production URL")

if errors:
    raise SystemExit("\n".join(errors))
print(f"Validated {len(pages)} HTML pages, stylesheets, local resources, and anchors.")
