#!/usr/bin/env python3
"""
check-links.py — resolve every relative link in the prototype against the filesystem.

Why this exists: the nav and footer are pasted into every page, so a single route rename touches
hundreds of hrefs across dozens of files, and a wrong relative prefix produces a 404 that nothing
else notices — the page still renders. This walks every link and every cross-page `#anchor` and
says which ones do not resolve.

  python3 tools/check-links.py              # report unresolvable links
  python3 tools/check-links.py --baseline   # write the current result to tools/.links-baseline
  python3 tools/check-links.py --compare    # fail only on links broken SINCE the baseline

Exit status: 0 = clean (or no regression under --compare), 1 = broken links.

Deliberately NOT flagged: `href="#"` placeholders (the Service Areas footer stubs are intentional),
external URLs, and `mailto:`/`tel:`.
"""

import re
import sys
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parent.parent
BASELINE = ROOT / "tools" / ".links-baseline"

SKIP = re.compile(r"^(?:#|https?:|mailto:|tel:|javascript:|data:)", re.I)
ATTR = re.compile(r'\b(?:href|src)\s*=\s*"([^"]*)"', re.I)
ID = re.compile(r'\bid\s*=\s*"([^"]+)"')
COMMENT = re.compile(r"<!--.*?-->", re.S)


def blank_comments(text):
    """HTML comments carry example paths on purpose — the path-depth table in _nav.html, the
    placeholder-link convention notes, the template banners' prose. Those are documentation, not
    links. Blank them to spaces so offsets (and therefore line numbers) stay exact."""
    return COMMENT.sub(lambda m: re.sub(r"[^\n]", " ", m.group(0)), text)


def pages():
    out = sorted(p for p in (ROOT / "prototype").rglob("*.html"))
    root404 = ROOT / "404.html"
    if root404.is_file():
        out.append(root404)
    return out


def ids_of(path, _cache={}):
    if path not in _cache:
        try:
            _cache[path] = set(ID.findall(blank_comments(path.read_text(encoding="utf-8"))))
        except OSError:
            _cache[path] = set()
    return _cache[path]


def check():
    broken = []
    for page in pages():
        text = blank_comments(page.read_text(encoding="utf-8"))
        # line number per match, without re-scanning the whole file each time
        starts = [0]
        for line in text.split("\n"):
            starts.append(starts[-1] + len(line) + 1)

        def lineno(pos):
            lo, hi = 0, len(starts) - 1
            while lo < hi:
                mid = (lo + hi) // 2
                if starts[mid] <= pos:
                    lo = mid + 1
                else:
                    hi = mid
            return lo

        for m in ATTR.finditer(text):
            raw = m.group(1).strip()
            if not raw or raw == "#" or SKIP.match(raw):
                continue
            if raw.startswith("/"):
                broken.append((page, lineno(m.start()), raw, "root-relative (prototype is served from a subpath)"))
                continue
            target, _, frag = raw.partition("#")
            target = unquote(target.split("?")[0])
            dest = (page.parent / target).resolve() if target else page
            if not dest.exists():
                broken.append((page, lineno(m.start()), raw, "no such file"))
            elif frag and dest.suffix == ".html" and frag not in ids_of(dest):
                broken.append((page, lineno(m.start()), raw, f"file ok, but #{frag} not found in it"))
    return broken


def key(b):
    page, line, raw, why = b
    return f"{page.relative_to(ROOT)}|{raw}|{why}"   # line-independent, so edits elsewhere don't churn it


def main():
    broken = check()
    n_pages = len(pages())

    if "--baseline" in sys.argv:
        BASELINE.write_text("\n".join(sorted(key(b) for b in broken)) + "\n", encoding="utf-8")
        print(f"baseline written: {len(broken)} known-broken links across {n_pages} pages")
        return 0

    if "--compare" in sys.argv:
        if not BASELINE.is_file():
            print("FAIL  no baseline — run: python3 tools/check-links.py --baseline")
            return 1
        known = set(BASELINE.read_text(encoding="utf-8").split("\n")) - {""}
        now = {key(b) for b in broken}
        new, fixed = now - known, known - now
        for b in sorted(broken, key=key):
            if key(b) in new:
                print(f"  ✗ {b[0].relative_to(ROOT)}:{b[1]}  {b[2]}  — {b[3]}")
        print(f"\n  {len(new)} newly broken · {len(fixed)} fixed · {len(known & now)} unchanged")
        return 1 if new else 0

    for b in sorted(broken, key=key):
        print(f"  ✗ {b[0].relative_to(ROOT)}:{b[1]}  {b[2]}  — {b[3]}")
    print(f"\n  {n_pages} pages scanned · {len(broken)} unresolvable link(s)")
    return 1 if broken else 0


if __name__ == "__main__":
    sys.exit(main())
