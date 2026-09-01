#!/usr/bin/env python3
"""
check-ia-sync.py — assert the facts that MUST agree between the IA doc and the built wireframe.

Why this exists: `docs/ia.md` owns the structural contract, the wireframe owns rendered UX, and a
handful of facts are unavoidably stated in both. Those are the ones that drift. Rather than another
prose rule telling a future session to remember, this makes drift a command you can run.

Run from the repo root:   python3 tools/check-ia-sync.py
Exit status: 0 = no FAILs (WARNs allowed), 1 = at least one FAIL.

Deliberately NOT checked: anything the wireframe cannot answer — deferred pages, production route
shapes, localization, mobile behaviour. Those live in ia.md alone and have no second source to
disagree with.
"""

import html
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
IA = ROOT / "docs" / "ia.md"
NAV = ROOT / "prototype" / "_nav.html"
PROTO = ROOT / "prototype"

results = []  # (level, check, message)


def record(level, check, message):
    results.append((level, check, message))


def clean(s):
    """HTML fragment -> comparable plain text."""
    s = re.sub(r"<[^>]+>", "", s)
    s = html.unescape(s)
    return re.sub(r"\s+", " ", s).strip()


def head_of(item):
    """Normalise 'Technologies — full stack index →' and 'Fixed Price — defined scope' to their head."""
    item = item.split(" — ")[0]
    return item.replace("→", "").strip()


# ─────────────────────────────────────────────────────────────────────────────
# Parse the built nav: columns -> (heading text, heading is a link, [item texts])
# ─────────────────────────────────────────────────────────────────────────────
def parse_nav(navsrc):
    cols = []
    for m in re.finditer(
        r'<div class="(?:megamenu__col|dropdown__col)[^"]*">(.*?)(?=<div class="(?:megamenu__col|dropdown__col)|</div>\s*</div>)',
        navsrc,
        re.S,
    ):
        block = m.group(1)
        h = re.search(
            r'<(a|span) class="(?:megamenu|dropdown)__heading[^"]*"(?P<attrs>[^>]*)>(?P<text>.*?)</\1>',
            block,
            re.S,
        )
        if not h:
            continue
        hh = re.search(r'href="([^"]*)"', h.group("attrs"))
        items = []
        for li in re.finditer(
            r'<a class="(?:megamenu|dropdown)__link" href="(?P<href>[^"]*)"[^>]*>(?P<text>.*?)</a>',
            block,
            re.S,
        ):
            t = clean(li.group("text"))
            if t:
                items.append({"text": t, "href": li.group("href")})
        cols.append(
            {
                "heading": clean(h.group("text")),
                "href": hh.group(1) if hh else None,
                "is_link": h.group(1) == "a",
                "items": items,
                "bold_first": bool(re.search(r'__link"[^>]*>\s*<strong>', block)),
            }
        )
    return cols


navsrc = NAV.read_text(encoding="utf-8")
iasrc = IA.read_text(encoding="utf-8")
cols = parse_nav(navsrc)
by_heading = {c["heading"]: c for c in cols}

if not cols:
    record("FAIL", "nav parse", "parsed 0 columns out of _nav.html — the parser or the markup changed")

# ─────────────────────────────────────────────────────────────────────────────
# CHECK 1 — top-level slot count matches ia.md's stated shape
# ─────────────────────────────────────────────────────────────────────────────
WORDS = {"six": 6, "seven": 7, "eight": 8, "nine": 9, "ten": 10}
nav_items = len(re.findall(r'<div class="nav__item">', navsrc))
ctas = len(re.findall(r'class="[^"]*nav__cta', navsrc))
m = re.search(r"(\w+) slots in the primary navigation: (\w+) content menus \+ (\w+) primary CTA", iasrc)
if not m:
    record("WARN", "top-level slots", "could not find ia.md's slot-count sentence to check against")
else:
    want_total, want_menus = WORDS.get(m.group(1).lower()), WORDS.get(m.group(2).lower())
    got = f"{nav_items} content menus + {ctas} CTA = {nav_items + ctas}"
    if want_menus == nav_items and want_total == nav_items + ctas:
        record("PASS", "top-level slots", f"ia.md says {m.group(1)} slots ({m.group(2)} menus + CTA); nav has {got}")
    else:
        record("FAIL", "top-level slots", f"ia.md says {m.group(1)} slots / {m.group(2)} menus; nav has {got}")

# ─────────────────────────────────────────────────────────────────────────────
# CHECK 2 — taxonomy lists agree with the nav
# ia.md is the contract; the nav is where the taxonomy is visible. These must not diverge.
# Known, accepted difference: each Services stage column leads with a BOLD parent-category link
# that ia.md's stage lists deliberately omit (they list sub-services only). Excluded below.
# ─────────────────────────────────────────────────────────────────────────────
LIST_RE = re.compile(r"^\*\*(?P<name>[^*]+?)\*\*(?:\s*\*\([^)]*\)\*)?:\*{0,2}\s*(?P<body>.+)$", re.M)
ALT_RE = re.compile(r"^\*\*(?P<name>[^*:]+?):\*\*\s*(?P<body>.+)$", re.M)

def split_items(body):
    """Split an ia.md inline list. Items are ' · '-separated — except the numbered process list
    ('1 · Kickoff → 2 · Scoping'), where ' · ' sits INSIDE each item and ' → ' separates them.
    Detect that by a bare-number fragment appearing after a ' · ' split."""
    parts = [x.strip() for x in body.split(" · ") if x.strip()]
    if any(p.isdigit() for p in parts):
        parts = [x.strip() for x in body.split(" → ") if x.strip()]
    return [head_of(x) for x in parts if head_of(x)]


def is_section_nav(col):
    """True when a column deep-links the sections of ONE page rather than listing sibling entities.
    Those columns are navigation aids, not taxonomy: ia.md names the page, the nav expands it into
    its own anchors, and neither is wrong. Detected structurally, not by a hardcoded column list."""
    if not col["href"] or not col["items"]:
        return False
    same = sum(1 for i in col["items"] if "#" in i["href"] and i["href"].split("#")[0] == col["href"])
    return same * 2 >= len(col["items"])


ia_lists = {}
for rx in (ALT_RE, LIST_RE):
    for mm in rx.finditer(iasrc):
        name = mm.group("name").strip()
        if name in by_heading and name not in ia_lists:
            ia_lists[name] = split_items(mm.group("body").strip())

if not ia_lists:
    record("FAIL", "taxonomy", "matched 0 taxonomy lists in ia.md against nav column headings")

for name, want in sorted(ia_lists.items()):
    col = by_heading[name]
    if is_section_nav(col):
        record("SKIP", f"taxonomy · {name}",
               "column deep-links one page's own sections — not a taxonomy list, not compared")
        continue
    got = [head_of(i["text"]) for i in col["items"]]
    if col["bold_first"] and got:
        got = got[1:]  # drop the bold parent-category link (accepted difference)
    missing = [x for x in want if x not in got]
    extra = [x for x in got if x not in want]
    if not missing and not extra:
        record("PASS", f"taxonomy · {name}", f"{len(want)} items agree")
    else:
        bits = []
        if missing:
            bits.append(f"in ia.md but not the nav: {missing}")
        if extra:
            bits.append(f"in the nav but not ia.md: {extra}")
        record("FAIL", f"taxonomy · {name}", "; ".join(bits))

# ─────────────────────────────────────────────────────────────────────────────
# CHECK 3 — ia.md must not contradict the nav on which headings are links
# ia.md deliberately keeps no census (the nav is the inventory), so this looks for
# sentences that reintroduce one and disagree with the DOM.
# ─────────────────────────────────────────────────────────────────────────────
LINKY = re.compile(r"\b(are links|is a link|heading links|links `)", re.I)
LABELY = re.compile(r"non-interactive|not a link|\blabel\b", re.I)

sentences = re.split(r"(?<=[.!?])\s+", iasrc.replace("\n", " "))
contradictions = 0
for c in cols:
    name = c["heading"]
    if not name:
        continue
    for sent in sentences:
        if f'"{name}"' not in sent:
            continue
        says_link = bool(LINKY.search(sent))
        says_label = bool(LABELY.search(sent))
        if says_link and not says_label and not c["is_link"]:
            contradictions += 1
            record("FAIL", f"heading claim · {name}",
                   f'nav says LABEL, ia.md sentence implies link: "{sent.strip()[:150]}"')
        elif says_label and not says_link and c["is_link"]:
            contradictions += 1
            record("FAIL", f"heading claim · {name}",
                   f'nav says LINK, ia.md sentence implies label: "{sent.strip()[:150]}"')
if not contradictions:
    linked = sorted(c["heading"] for c in cols if c["is_link"])
    record("PASS", "heading claims", f"no ia.md sentence contradicts the DOM; nav heading links: {linked}")

# ─────────────────────────────────────────────────────────────────────────────
# CHECK 3b — every column heading ia.md names must actually exist in the nav.
# Catches a renamed column that ia.md never followed: the doc goes on describing a heading the
# built nav no longer has, and nothing else notices because no comparison ever matches it.
# ─────────────────────────────────────────────────────────────────────────────
dom_headings = {c["heading"] for c in cols}
# Heading-behaviour sentences legitimately also quote top-level TRIGGER names (e.g. explaining that
# a heading would restate where its own trigger goes), so those are valid names too.
triggers = {clean(t) for t in re.findall(r'<(?:a|button)[^>]*class="nav__link"[^>]*>(.*?)</(?:a|button)>', navsrc, re.S)}
known_names = dom_headings | triggers
phantoms = set()
for sent in sentences:
    if "Heading behavior" not in sent:
        continue
    for quoted in re.findall(r'"([^"]{2,40})"', sent):
        if quoted not in known_names:
            phantoms.add(quoted)
if phantoms:
    record("FAIL", "heading names exist",
           f"ia.md describes heading(s) the nav does not have: {sorted(phantoms)} "
           f"— renamed in the build without updating ia.md, or vice versa")
else:
    record("PASS", "heading names exist", "every heading ia.md names by quote exists in the nav")

# ─────────────────────────────────────────────────────────────────────────────
# CHECK 3c — the two naming registers must agree on MEMBERSHIP, not wording.
# ia.md states each sub-service twice on purpose: a short nav label in the Services megamenu section
# (which matches the built nav) and a formal page name — H1 + URL slug — in the category's
# site-structure section. Wording differing is correct; a differing COUNT means one register gained
# or lost a sub-service and the other was never updated, which silently forks the taxonomy.
# ─────────────────────────────────────────────────────────────────────────────
STAGE_TO_CATEGORY = {
    "Discover & Validate": "IT Consulting",
    "Design": "Product Design",
    "Build": "Software Development",
    "Grow": "Marketing",
    "Scale": "Outsourcing & Outstaffing",
    "Maintain": "Support & Maintenance",
}
page_names = {}
for mm in re.finditer(
    r"^### (?P<cat>[^·\n]+?) · `/services/[^`]+` · \*\*full\*\*(?P<body>.*?)(?=^### )", iasrc, re.M | re.S
):
    b = re.search(r"\*\*Sub-service pages\*\*[^:]*:\s*(.+)", mm.group("body"))
    if b:
        page_names[mm.group("cat").strip()] = [x.strip() for x in b.group(1).split(" · ") if x.strip()]

register_problems = []
for stage, cat in STAGE_TO_CATEGORY.items():
    labels = ia_lists.get(stage)
    names = page_names.get(cat)
    if labels is None or names is None:
        register_problems.append(f"{stage}/{cat}: could not read both registers")
    elif len(labels) != len(names):
        register_problems.append(
            f"{stage} has {len(labels)} nav labels but {cat} lists {len(names)} page names"
        )
if register_problems:
    record("FAIL", "naming registers", "; ".join(register_problems))
else:
    total = sum(len(v) for v in page_names.values())
    record("PASS", "naming registers",
           f"nav-label and page-name registers agree in count across all 6 stages ({total} sub-services)")

# ─────────────────────────────────────────────────────────────────────────────
# CHECK 4 — every page ia.md badges **full** exists in the prototype
# Templates and mention-level pages are skipped by design (§4.4 builds one example per family);
# deferred pages are skipped because their whole point is not existing yet.
# ─────────────────────────────────────────────────────────────────────────────
PAGE_RE = re.compile(r"^### (?P<name>.+?) · `(?P<route>[^`]+)`.*?\*\*(?P<badge>[^*]+)\*\*", re.M)
missing_pages, checked = [], 0
for mm in PAGE_RE.finditer(iasrc):
    route, badge = mm.group("route"), mm.group("badge")
    if "full" not in badge or "deferred" in badge or "[" in route:
        continue
    rel = "index.html" if route == "/" else route.strip("/") + ".html"
    cand = [PROTO / rel, PROTO / route.strip("/") / "index.html"]
    checked += 1
    if not any(p.is_file() for p in cand):
        missing_pages.append(f"{route} ({mm.group('name')})")
if missing_pages:
    record("FAIL", "full pages built", f"{len(missing_pages)}/{checked} declared **full** have no page: {missing_pages}")
else:
    record("PASS", "full pages built", f"all {checked} pages badged **full** exist in prototype/")

# ─────────────────────────────────────────────────────────────────────────────
# CHECK 4b — the ia.md table of contents is derived, so it must be current.
# Delegated to the generator so the slug rule has one home (it was verified against GitHub's
# own renderer; two copies of that rule would age apart).
# ─────────────────────────────────────────────────────────────────────────────
import subprocess  # noqa: E402  (local to this check)

gen = ROOT / "tools" / "gen-ia-toc.py"
if not gen.is_file():
    record("FAIL", "toc current", f"{gen.name} is missing — the TOC has no generator")
else:
    r = subprocess.run([sys.executable, str(gen), "--check"], capture_output=True, text=True)
    out = (r.stdout + r.stderr).strip().split("\n")[-1]
    record("PASS" if r.returncode == 0 else "FAIL", "toc current",
           re.sub(r"^(OK|FAIL)\s+", "", out))

# ─────────────────────────────────────────────────────────────────────────────
# CHECK 5 — Lucide icon names: any un-replaced <i data-lucide> is a dead icon name
# ─────────────────────────────────────────────────────────────────────────────
bad_icons = sorted(set(re.findall(r'data-lucide="(trello|kanban)"', navsrc)))
if bad_icons:
    record("FAIL", "lucide names", f"deprecated icon names in the nav: {bad_icons}")

# ─────────────────────────────────────────────────────────────────────────────
# Report
# ─────────────────────────────────────────────────────────────────────────────
ORDER = {"FAIL": 0, "WARN": 1, "SKIP": 2, "PASS": 3}
GLYPH = {"FAIL": "✗", "WARN": "!", "SKIP": "–", "PASS": "✓"}
width = max(len(c) for _, c, _ in results) + 2

print(f"\nia.md ↔ wireframe sync check\n{'=' * 78}")
for level, check, msg in sorted(results, key=lambda r: (ORDER[r[0]], r[1])):
    print(f"  {GLYPH[level]} {check.ljust(width)} {msg}")

n = lambda lv: sum(1 for l, _, _ in results if l == lv)
fails = n("FAIL")
print(f"{'=' * 78}\n  {n('PASS')} passed · {n('SKIP')} skipped · {n('WARN')} warned · {fails} failed\n")
sys.exit(1 if fails else 0)
