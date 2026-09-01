# VECTO Wireframe — Drift-Fix Build Prompts (Stream A)

Sequenced Claude Code prompts to apply the **build fixes** from `drift-report.md` (reconciliation pass, 2026-06-27). The IA edits (Stream B) are applied separately to `docs/vecto-master-ia-revised.html` — after both streams land, IA and build agree.

**How to use:** run in order. Each prompt is self-contained and copy-pasteable. They are mostly independent; the only soft dependency is that P4 builds on the Our Work facet system, so run it after P3. Follow the repo's existing conventions in `CLAUDE.md` (token vars only, Lucide-only, geometry+screenshot verification, nav-is-pasted-not-included).

**Canonical decisions these encode:**
- Industries canonical count = **13** (Travel and Hospitality are separate; "Retail · E-commerce" collapses to **Retail**). Full list: Tech · Travel · Hospitality · Finance · Healthcare · Manufacturing · Retail · Education · Sport · Media & Entertainment · Professional Services · Non-Profit · Beauty & Wellness.
- Services sub-services canonical count = **11** for both Build and Grow; the **megamenu must show all 11**, the services-hub cards may stay narrowed.

---

## P1 — Homepage Industries band: 13 tiles (keep editorial layout)

**Context:** `index.html` industries band ("Depth in the industries we know best.") currently shows 2 featured cards (Healthcare, Finance) + a 10-item index = **12** tiles, with Travel & Hospitality and Retail · E-commerce each combined into one. Canonical count is 13.

**Task:** Update the homepage industries band to represent **13** industries, keeping the editorial 2-featured + index treatment (do NOT convert to a uniform grid — the IA was updated to bless the editorial layout):
- Keep **Healthcare** and **Finance** as the two featured cards.
- The index must list the remaining **11**: Tech, Travel, Hospitality, Retail, Education, Manufacturing, Media & Entertainment, Sport, Professional Services, Non-Profit, Beauty & Wellness.
- Specifically: split the existing "Travel & Hospitality" tile into separate **Travel** and **Hospitality** tiles, and relabel "Retail · E-commerce" → **Retail**. Pick appropriate distinct Lucide icons for Travel (`plane`) and Hospitality (`concierge-bell` or `bed`); keep Retail on `shopping-cart`.
- All tiles continue to link to the single `industries/healthcare.html` placeholder per the one-template-per-family convention (leave the placeholder-convention comment intact).

**Files:** `index.html` only.

**Verify:** Count the industry tiles/links in the band — must be 13 total (2 featured + 11 index). Assert `document.querySelectorAll('i[data-lucide]').length === 0` after Lucide runs (no dead icon names from the new Travel/Hospitality icons). Take a top-of-band screenshot to confirm the split reads cleanly and the index wraps without an orphan.

---

## P2 — Nav megamenu: 13 industries + 11 Build/Grow sub-services (then re-propagate to every page)

**Context:** The nav is **pasted** into every page's `<header>`, not included — so a megamenu change must be made in `_nav.html` and then re-propagated to all pages with the correct `../` depth (see `CLAUDE.md` "Depth-1/Depth-2 partials" recipe). Two drift fixes land here:
1. **By industry** panel currently lists **12** (Travel & Hospitality combined; Retail · E-commerce combined) — must list the canonical **13**.
2. **Build** and **Grow** stage columns currently collapse sub-services (Build shows 8: CRM/ERP, Bot/Game, SPA/PWA merged; Grow shows 8: SEO·GEO·ASO, PPC·SMM merged) — the megamenu must show **all 11** each.

**Task (in `_nav.html` first):**
- **By industry:** make the list the canonical 13 — split "Travel & Hospitality" → **Travel** + **Hospitality**; relabel "Retail · E-commerce" → **Retail**. Final: Tech, Travel, Hospitality, Finance, Healthcare, Manufacturing, Retail, Education, Sport, Media & Entertainment, Professional Services, Non-Profit, Beauty & Wellness.
- **Build column:** split into all 11 — Web Development, Mobile App Development, E-commerce Development, **CRM Development**, **ERP Development**, **Bot Development**, **Game Development**, **SPA Development**, **PWA Development**, 3rd Party Integrations, Platform Migration.
- **Grow column:** split into all 11 — Marketing Strategy, Full Digital Marketing, **SEO**, **GEO**, **ASO**, Lead Generation, **PPC**, **SMM**, Digital Branding, Copywriting, Graphic Design.
- Keep all the conventions from `CLAUDE.md`: section headings stay clickable hub links; interactive list items use `--text-secondary-strong`; nav heading links keep `text-decoration:none`.

**Then re-propagate** the updated `<header>` to every built page at the correct depth (root, depth-1, depth-2) using the perl path-depth recipe in `CLAUDE.md`. Don't forget the depth-2 `how-we-work/<x>/` pages.

**Files:** `_nav.html` + every `*.html` page (header block) + check `404.html`.

**Verify:** On a root page, a depth-1 page (e.g. `services/index.html`), and a depth-2 page (e.g. `how-we-work/tools/jira.html`): open the Services megamenu and assert the Build column has 11 items and Grow has 11; open Who We Serve and assert By industry has 13. Re-run the Lucide assertion (`i[data-lucide].length === 0`) and `preview_network` (filter `failed`) on a depth-2 page to catch any broken `../` links introduced during propagation. Spot-screenshot one megamenu to confirm columns didn't overflow.

---

## P3 — Our Work: rename "Company size" facet → "Company stage"

**Context:** The IA listed both a "Stage" and a "Company size" facet; they're the same axis (Early-stage → Enterprise). Reconciliation: keep one facet, named **Company stage** (the IA dropped the duplicate "Stage").

**Task:** In `our-work/index.html`, rename the facet currently labeled **"Company size"** to **"Company stage"** — the visible legend/label, the `aria-label`/heading, and any human-readable copy. Keep the `data-facet="size"` attribute value as-is unless trivial to rename to `stage` without breaking `initFacetFilter` wiring in `prototype.js` (if you rename the attribute, update both sides). The facet's option values (Early-stage Startup, Scale-up, Small Business, Midsize Business, Enterprise) are unchanged.

**Files:** `our-work/index.html` (+ `prototype.js` only if you rename the `data-facet` value).

**Verify:** Load Our Work, confirm the facet reads "Company stage" and still filters correctly (select a value, confirm the result set narrows and `[data-filter-count]` updates). Confirm no `[hidden]` regression on the facet menu (see `CLAUDE.md` hidden-attr note).

---

## P4 — AI Transformation "See our AI work" CTA: deep-link to a pre-filtered Our Work

**Context:** IA `services/ai-transformation` block 1 specifies "See our AI work → (/our-work, **AI tag pre-filtered**)." The build currently links to a plain `../our-work/index.html`. The Our Work hub has a working multi-facet filter (`initFacetFilter`) but doesn't read filter state from the URL on load.

**Task:**
1. In `prototype.js` `initFacetFilter`, add **deep-link support**: on init, read a URL parameter or hash (e.g. `?facet=technology:AI` or `#technology=AI`) and pre-apply the matching facet checkbox(es) before the first filter pass, so the page loads already filtered. Keep it generic (any facet:value), not AI-hardcoded.
2. Update the `services/ai-transformation.html` hero "See our AI work" CTA to link to `../our-work/index.html` with that pre-filter param targeting the AI/Technology facet value used in the portfolio data.
3. Confirm the AI value exists in at least one `[data-portfolio-item][data-tags]` so the filtered view isn't empty (the case study `fintech-platform.html` / Our Work items should carry an AI tag; add it to a relevant item if missing).

**Files:** `prototype.js`, `services/ai-transformation.html`, `our-work/index.html` (data tags only if needed).

**Verify:** Navigate from the AI Transformation CTA; confirm Our Work loads with the AI/Technology facet checked and the result set already narrowed (not the full list), with `[data-filter-count]` reflecting the subset and no `[data-filter-empty]` state. Also confirm a normal (no-param) visit to Our Work still shows everything unfiltered. Test on a cache-busted load (`?v=…`).

---

## P5 — Industries hub: de-count the FAQ heading

**Context:** `industries/index.html` FAQ heading hard-codes "Two questions we hear a lot." — brittle if a question is added.

**Task:** Change the heading to **"Questions we hear a lot."** (drop "Two"). Copy-only edit; leave the two FAQ items unchanged.

**Files:** `industries/index.html`.

**Verify:** Confirm the heading text changed and nothing else in the FAQ block moved.

---

## After all five
- Re-run a quick whole-site Lucide assertion and `preview_network` failed-filter sweep (P2's propagation is the main risk).
- Commit per the repo's git rhythm (`CLAUDE.md`: commit only when asked, push only when asked).
- The build and `vecto-master-ia-revised.html` (post Stream B) should now be reconciled; `drift-report.md` is the record of why each change was made.
