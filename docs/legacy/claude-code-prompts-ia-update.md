# VECTO Wireframe — IA-Update Build Prompts (Part F)

Sequenced Claude Code prompts to build the **confirmed wireframe changes** from `plan-ia-update-audit.md` **Part F** into `wireframe/`. These follow the doc reconciliation of 2026-07-03; after they land, the wireframe and `vecto-master-ia-revised.html` agree again on the reconciled IA.

**How to use:** run in order. Unlike the drift-fix set, these have **real dependencies** — P1 (nav/footer) is the spine and must run first; several later prompts create the pages P1's new links point at. Follow the repo's conventions in `wireframe/CLAUDE.md` (flat `:root` tokens only, `var(--…)` everywhere, Lucide-only + no emojis, real placeholder copy never lorem ipsum, editorial Tier-1 / clean-grid Tier-3, geometry+screenshot verification, **nav/footer are pasted partials not includes**, one-representative-example-per-template + `.tmpl-banner` convention). Before each prompt, open the referenced page entry in `../docs/vecto-master-ia-revised.html` and read it — don't build from memory.

**First-class requirement on every prompt — route/URL fidelity.** Under the SSG model the production site is, like the wireframe, real HTML at real paths. So each prompt must land correct paths, breadcrumbs, and depth-correct `../` nav/footer, not just correct visuals. `/projects/[project-name]` is a verbatim SEO contract.

**The nav-target ordering rule.** P1 rewrites `_nav.html`/`_footer.html` to their **final** state and points new links at their real target paths (`solutions/index.html`, `about/company.html`, `about/team.html`, `about/careers/index.html`, `about/testimonials.html`). Those targets don't exist until later prompts. Therefore:
- P1's verification treats those specific new routes as **expected-missing** — do not fail P1 on them.
- Every page built in P2–P11 pastes the **already-updated** partial at its correct depth.
- **P12 is the reconciliation sweep** — once all targets exist, it re-runs the whole-site Lucide + `preview_network` failed-link check so nothing is left dangling.

**Canonical facts these encode (from the reconciliation):**
- Nav is now **7 top-level links + the estimate CTA** (was 6 links + CTA): Services · **Solutions** · Who We Serve · Our Work · How We Work · Resources · About, then the CTA. Solutions sits **right after Services** ("what we offer" pair). The main CTA may render more compactly to fit — the sticky/floating estimate CTA carries conversion regardless, so compaction is acceptable.
- **Security & Compliance is removed from every visible surface** (About menu, footer Company column, About cross-link block, Contact procurement/InfoSec path). The page is dropped from the wireframe.
- About is a **hub-and-spokes**: `/about` (deliberately simple, skippable — the megamenu About headline is itself clickable) + `/about/company` + `/about/team` + `/about/careers` (+ `/about/careers/[job-slug]`) + `/about/testimonials`.
- Portfolio structural reference = **miiind.co/portfolio**: header + filters → featured section → asymmetric grid on three aspect presets (1:1, 2:3, 3:2). **Outcome groupings are gone** (Our Work block 3 *and* homepage block 9).
- **Facet landings are ENTRY pages under a one-way-door model.** Hub filter dropdowns compose freely as query-param state and **never navigate**. A facet landing has its own H1 + editorial intro with the filter pre-selected; touching its filters drops into hub-style filtering. URL scheme is namespaced: `/our-work/industry/<slug>` and `/our-work/service/<slug>`. Wireframe keeps the `/our-work` base (D18 exact name is a pre-launch call).
- **Blog is the opposite of the portfolio:** category chips **do navigate** to `/blog/category/[topic]` (categories are single-select, so no composition conflict). Pagination validated here — instinct is load-more over numbered pages.
- **Pipeline simplified:** Get an Estimate = simple form → success state offering an optional Schedule a Call. Contact = two paths (Get an Estimate · Send a question). All "90 seconds"/instant-ballpark copy is gone — human-reply framing ("get a ballpark from the team").
- **Solutions** = VECTO's own B2B/SaaS products (onemall, onesocial, quickoffer, plugins) — categorically separate from Services (custom work) and Our Work (client proof); **never** mixed into the portfolio grid.
- **External product CTA** ("Launch website / Try now") is an optional field on case study + solution templates — **hidden when absent**. Build one example with it; exercise the absent state on another.
- **Language switcher** renders only when >1 language is published, so the wireframe must **simulate a "second language live" state** to show it at all. **Desktop header placement only** — the desktop-only constraint stands; no mobile drawer is prototyped. Content stays EN-only.
- **Menu headings: label by default, link only with a real destination** (2026-07-03, replaces nav-headings-are-links). Interactive headings = accent-red text; non-interactive labels = muted grey. Links: Services stage headings, HWW Process/Engagement Models, Resources Blog, WWS both headings, About The company/The team. Labels: HWW "Reference", Resources "Glossary" (tagline + single "Browse A–Z" link), About "Trust & contact". Menu placement ≠ hierarchy (Schedule/Contact stay root-level standalone pages).
- **"Project Estimator" naming is retired until the AI estimator returns** — the page and every reference are "Get an Estimate"; the Resources-menu Tools entry is deleted (redundant with the nav CTA), the footer entry is relabeled.

**Boundary (applies to all prompts):** the wireframe validates **structure, routes, and UX only**. Do not simulate CMS mechanics or the field-level content model — that lives in the Figma P2 annotation discipline. Where the IA notes a CMS entity (facet entry, testimonial, job, solution, featured flag, aspect preset, cta fields), represent it as static placeholder markup, not a data layer.

---

## P1 — Nav + footer overhaul, then re-propagate to every page (the spine)

**Sources:** E5 (Solutions slot + CTA compaction), E3a/E3c (About menu rebuild + S&C removal), C2 (language switcher). **Run first — everything depends on it.**

**Context:** `_nav.html` currently has **6 menu slots + CTA** (Services, Who We Serve, Our Work, How We Work, Resources, About). The About megamenu points every link at `about/index.html` or `about/security-compliance.html` (columns: The company / The team / Trust & contact, the last containing Security & Compliance). There is no Solutions item and no language switcher. `topbar__actions` holds only the estimate CTA. The nav/footer are **pasted** into every page's `<header>`/`<footer>` (not included), so a change must be made in the partials then re-propagated at correct `../` depth (root / depth-1 / depth-2 — see `CLAUDE.md` recipes).

**Task — in `_nav.html` and `_footer.html` first:**
1. **Add Solutions as a 7th top-level link** (taking the bar from 6 links + CTA to **7 links + CTA**), directly after Services, as a **direct `<a href="solutions/index.html">Solutions</a>`** top-level link (no megamenu — it's a direct link like Our Work). Preserve the `initMenus`/`initActiveNav` contract (Solutions is a plain nav link; `initActiveNav` flags it from `location.pathname`).
2. **CTA compaction:** if the 7 links + CTA crowd the bar, render the `nav__cta` more compactly (e.g. `btn--small`, tighter label) so it fits at ~1200px. This is a deliberate, acceptable trade — validate interactively that the bar doesn't wrap or overflow.
3. **NEW HEADING CONVENTION (replaces the old nav-headings-are-links rule — update `CLAUDE.md` accordingly).** Dropdown/megamenu column headings are **non-interactive labels by default**; a heading is a **link only when a real destination page exists for it**. The two states must be **visually distinct**: interactive heading = **accent-red text** (text colour only — NOT a button/pill), non-interactive label = the current muted grey. No invented hub pages, no next-best-option targets (the old prototype pointed "Reference" at `how-we-work/index.html` and "Trust & contact" at `about/security-compliance.html` — both are exactly the pathology this kills). Add a `.dropdown__heading--link` (or equivalent) modifier + one CSS rule using tokens; HTML comment noting the final visual treatment is a Figma/DS task (new component pair: nav heading-link vs nav label).

3a. **Rebuild the About megamenu** as the IA's **simple 3-column dropdown** (IA "About menu" mock, `cols-3`). The **About headline itself is a clickable `<a href="about/index.html">`** (navigates to the hub). Columns exactly per the IA:
   - **The company** → heading links to `about/company.html`; one item "Company — history, mission & vision, partners" → `about/company.html`.
   - **The team** → heading links to `about/team.html`; items "Team — leadership & specialists" → `about/team.html`, "Careers — open roles" → `about/careers/index.html`.
   - **Trust & contact** → **non-interactive label** (no page behind it); items "Testimonials" → `about/testimonials.html`, "Schedule a Call" → `schedule-a-call.html`, "Contact" → `contact.html`. (Schedule/Contact are standalone root-level pages — menu placement, not hierarchy.)
   Do **not** use the old "Trust & contact = Security & Compliance" structure — S&C is gone (step 4).

3b. **Heading sweep across ALL menus** (apply the step-3 convention everywhere):
   - **Services megamenu:** stage-column headings stay **links** to their category hub pages (IA-explicit); the AI band link unchanged.
   - **How We Work:** "Our Process" and "Engagement Models" headings stay **links** to their pages; **"Reference" becomes a non-interactive label** (currently mis-linked to `how-we-work/index.html`) — its three items (Technologies / Methodologies / Tools) remain the links.
   - **Resources:** rebuild per the updated IA mock — **two columns**. "Blog" heading = **link** to `blog/index.html` (items: Latest posts, By topic, Authors). "Glossary" heading = **non-interactive label** with the tagline "Tech terms, explained for founders" as plain text (NOT a link — the old prototype's interpretation was wrong) and **"Browse A–Z" → `glossary/index.html`** as the column's single link. **Delete the Tools column / Project Estimator entry entirely** — redundant with the adjacent Get an Estimate CTA; the tool framing rode on the deferred AI estimator and returns with it.
   - **Who We Serve:** both headings become **links** — "By company stage" → `who-we-serve/index.html`, "By industry" → `industries/index.html` (both legit hubs).
4. **Remove Security & Compliance entirely** from the nav — no link anywhere in `_nav.html`.
5. **Footer (`_footer.html`)** per the IA's 5-column + utility-row spec:
   - **Column 1 → rename to "Services & Solutions"**: the 8 service categories + "All services →", then a **Solutions** group linking the hub (`solutions/index.html`) (D11). *(The IA lists individual solution pages here too; in the wireframe the hub link stands in for them per the one-representative convention — don't hardcode links to per-solution pages that don't exist, to avoid re-propagation.)*
   - **Column 5 "Company"**: `About` (`about/index.html`) · `Company` (`about/company.html`) · `Team` (`about/team.html`) · `Careers` (`about/careers/index.html`) · `Testimonials` (`about/testimonials.html`) · Partners · Press · `Contact`. **Remove the Security & Compliance link entirely.**
   - Leave columns 2 (Industries & Stage), 3 (Service Areas) as-is except any stale About/S&C links.
   - **Column 4 (Resources): relabel "Project Estimator" → "Get an Estimate"** (same `get-an-estimate.html` target — the tool name is retired until the AI estimator returns; the footer entry stays for wayfinding).
6. **Language switcher (C2) — desktop header only.** Add a compact switcher to `topbar__actions` **beside** the CTA, simulating a **"second language published"** state so it renders (e.g. a small `EN ▾` control listing EN / Հայ / Рус; Lucide `globe` or `languages` icon, no emoji). It is display-only in the wireframe (content stays EN); clicking need not navigate. Add an HTML comment stating the production visibility rule ("rendered only when >1 language is published; hidden entirely at EN-only launch"). **Do not** add any mobile/drawer treatment — desktop-only stands.
7. Keep the placeholder-convention comment block at the top of `_nav.html`'s `<body>`; extend it to name the new About/Solutions template targets.

**Then re-propagate** the updated `<header>` and `<footer>` to **every existing built page** at the correct depth (root, depth-1, depth-2), using the perl path-depth recipes in `CLAUDE.md` (don't forget the depth-2 `how-we-work/<x>/` pages; one identical depth-2 partial works for all of them). Also update `404.html`. **Skip `about/security-compliance.html`** — P3 deletes it, so propagating into it is wasted work.

**Files:** `_nav.html`, `_footer.html`, **every existing `*.html` except `about/security-compliance.html`** (header + footer blocks), `404.html`.

**Verify:**
- On a root page, a depth-1 page (`services/index.html`), and a depth-2 page (`how-we-work/tools/jira.html`): assert **7 top-level nav links** in order (Services, Solutions, Who We Serve, Our Work, How We Work, Resources, About) **plus the estimate CTA**; open About and assert the rebuilt columns; assert **zero** occurrences of "Security & Compliance" anywhere in nav/footer across all three depths; assert the language switcher is present in `topbar__actions` and lists 3 languages.
- **Heading convention:** assert "Reference", "Glossary", and "Trust & contact" headings are **not** `<a>` elements; assert "Our Process", "Engagement Models", "Blog", "By company stage", "By industry", "The company", "The team" headings **are** links with correct targets; assert no nav/footer link to `how-we-work/index.html` from a heading; assert the Resources dropdown contains **no** estimator entry and no "Project Estimator" string anywhere in nav (footer column 4 reads "Get an Estimate"). Screenshot one open menu showing the red-vs-grey heading distinction.
- Re-run `document.querySelectorAll('i[data-lucide]').length === 0` after Lucide (catches bad new icon names).
- `preview_network` (filter `failed`) on a depth-2 page to catch broken `../` links from propagation. **Expected-missing (do NOT fail on):** `solutions/index.html`, `about/company.html`, `about/team.html`, `about/careers/index.html`, `about/testimonials.html` — these are built in P2–P4. Every *other* link must resolve.
- One screenshot of the top bar at ~1200px confirming the 7 links + compacted CTA + switcher fit without wrapping.

---

## P2 — Solutions branch: hub + one example solution page

**Sources:** E5 (new Solutions concept), E6 (external product CTA on the solution template). Depends on P1 (uses the updated partial; satisfies P1's `solutions/index.html` target).

**Context:** Solutions is an entirely new branch — VECTO's own B2B/SaaS products (onemall, onesocial, quickoffer, plugins), **categorically separate** from Services (custom work) and Our Work (client proof); it must **never** be mixed into the portfolio grid. Read the new Solutions branch spec in `../docs/vecto-master-ia-revised.html` (Solutions hub = intro + listing; Solution page template ≈ case-study anatomy adapted to product-selling).

**Task — to the IA Solutions specs (4-block hub + 8-block template):**
1. Create **`solutions/index.html`** (Tier-1 hub, 4 blocks): **(1) Hero + intro** concept framing ("we don't just build for clients — we ship our own products") · **(2) Solutions listing** a card per solution (name, one-line value proposition, category/status, visual) for onemall · onesocial · quickoffer · plugins, each linking to the example solution page per the one-template convention · **(3) "Why we build products"** short editorial band (practitioner-credibility angle) · **(4) Closing CTA** Estimate + Contact dual CTA. Add the top-of-body placeholder-convention comment.
2. Create **`solutions/onemall.html`** as the **one representative solution page** (8 blocks, case-study anatomy adapted to product-selling): **(1) Breadcrumb** Home › Solutions › [Solution] · **(2) Hero** name, tagline, product visual + **external product CTA** (see step 3) · **(3) What it is / who it's for** · **(4) Features & screens** · **(5) Tech stack** badges linking to `../how-we-work/technologies/…` pages · **(6) Pricing / plans** (optional) · **(7) Related case studies & services** cross-links · **(8) Closing CTA** external CTA repeated + Contact. Add the `.tmpl-banner` naming its template role and `/solutions/[solution-slug]` production target.
3. **External product CTA (E6):** give the example solution page a **present** external CTA ("Launch website" / "Try now" / "Download app") in the hero and repeated in the closing CTA, linking out — with an HTML comment noting `cta_label`/`cta_url` are optional fields, hidden when absent. (The **absent-CTA state is exercised in P8** against the second `/projects/` case study — don't add it to the hub listing here: the IA hub card is name / one-liner / status / visual, with **no CTA on cards at all**, so there's no card-level CTA to hide.)
4. Homepage Solutions strip (block 10a) is handled in **P11** (batched homepage), not here.

**Files:** `solutions/index.html` (new), `solutions/onemall.html` (new). Paste the P1 depth-1 partial.

**Verify:** both pages load; nav shows Solutions active (`initActiveNav`); the solution page carries the `.tmpl-banner` and a working external CTA; the hub cards are name / one-liner / status / visual (no CTA on cards). Lucide assertion === 0; `preview_network` failed === none. Screenshot the hub to confirm editorial (not a default card grid) treatment.

---

## P3 — About rebuild: hub + Company + Team + Testimonials; drop Security & Compliance

**Sources:** E3a (split), E3c (S&C removal), E3d (Testimonials spec). Depends on P1. Satisfies P1's `about/company.html`, `about/team.html`, `about/testimonials.html` targets.

**Context:** `about/index.html` is currently a single rich page (hero + 12-years history + mission/vision + team lead-row + team grid + tools/certs + proof + careers callout + Security-conscious-buyer cross-link). It must split into a **deliberately simple hub** plus spokes. Most visitors deep-link from the megamenu (the About headline itself is clickable), so **don't over-design `/about`**. Read the About page specs (hub + `/about/company` + `/about/team` + `/about/testimonials`) in the IA.

**Task — build all four pages to the IA's block-by-block specs (About §, page bodies):**

1. **`about/index.html` → rewrite into the deliberately-simple hub (IA "About hub", 3 blocks).** This is a full build, not a stub: **(1) Hero** — short framing line, who VECTO is in two sentences; **(2) Section cards** — four entry cards linking to Company · Team · Careers · Testimonials; **(3) Contact strip** — Schedule + Estimator dual CTA. Strip out everything from the old team-heavy page — the hub exists only for nav consistency (the megamenu About headline needs a destination) and for direct-URL/straggler visitors, who mostly skip it. Deliberately unsophisticated design-wise; markedly lighter than the current page.

2. **`about/company.html`** — the "humanise the agency" narrative page (7 blocks): **(1) Hero** company-story framing · **(2) History** founding story, milestones, where we are today · **(3) Mission & Vision** · **(4) Partners** (technology/certified partnerships) · **(5) Trust signals** (aggregate numbers: years, projects, retention, NPS, awards) · **(6) Team callout** cross-link to `about/team.html` (faces belong there) · **(7) Contact / CTA** Schedule + Estimator dual CTA. Migrate the relevant prose from the old About page (12-years narrative, milestones, mission/vision, tools/certs).

3. **`about/team.html`** — "who you'll actually work with" (5 blocks): **(1) Hero** "The team behind every project we ship." · **(2) Leadership grid** named, photographed, role + bio · **(3) Specialists grid** named, role, author-page cross-links where they write · **(4) Careers callout** "Want to join them?" → `careers/index.html` (the About-folder-relative path to `about/careers/index.html`, built in P4) · **(5) Contact / CTA** dual CTA.

4. **`about/testimonials.html`** (E3d, 5 blocks): **(1) Hero** "What clients say" + aggregate trust numbers · **(2) Featured testimonials** 2–3 editorially picked, larger treatment · **(3) Full testimonial list** all CMS testimonials, each with author, company, text, **link to source** (Google/Clutch/GoodFirms) · **(4) Review-platform strip** platform badges as **static trust marks** with outbound profile links · **(5) Closing CTA** Estimator + Schedule dual CTA. **No embedded third-party review widgets.** HTML comment: CMS-hosted Testimonial entity.

5. **Delete `about/security-compliance.html`** and remove its cross-links: the "Security-conscious buyer?" block at the bottom of the old About content, and (completed in P9) the Contact procurement/InfoSec path. Confirm no remaining link to it anywhere in the About area.

6. Homepage Reviews block (block 10) → CMS-testimonial cards is handled in **P11**.

**Files:** `about/index.html` (rewrite), `about/company.html` (new), `about/team.html` (new), `about/testimonials.html` (new), delete `about/security-compliance.html`. Paste the P1 depth-1 partial.

**Verify:** four About pages load; **`/about` has exactly the 3 hub blocks** (hero, four section cards → Company/Team/Careers/Testimonials, contact strip) and is markedly lighter than the old page; Company shows its 7 blocks incl. the Team callout, Team shows its 5 blocks incl. the Careers callout → `careers/index.html` (resolving to `about/careers/index.html`); Testimonials renders cards each with a source link and **no iframe/embed**; grep confirms `security-compliance` appears **nowhere** in the About area. Breadcrumbs correct at depth-1. Lucide === 0; `preview_network` failed === none **except `about/careers/index.html`** (the hub's Careers section card + Team's careers callout point at it; it's built in P4 — expected-missing here, resolved by P12).

---

## P4 — Careers: list page + one example job posting with application form

**Source:** E3b. Depends on P1 (satisfies the `about/careers/` hub target) and reads well after P3 (Team careers callout points here).

**Context:** New careers surface under About. Job detail pages are the SEO/shareable surface (recommended over in-page expansion). Application forms are **provider-backed** (per C4 — a client leaf inside a static page; no backend). Read the `/about/careers` + `/about/careers/[job-slug]` specs in the IA.

**File-vs-folder convention (match the repo):** the wireframe puts every hub-with-children at **`<folder>/index.html`** — `how-we-work/technologies/index.html` + `how-we-work/technologies/react.html`, and likewise methodologies/tools. Careers has children (job postings), so the careers list is **`about/careers/index.html`** (a folder + index), **not** a `about/careers.html` file sitting beside the `about/careers/` folder. Both careers pages therefore live at **depth-2** and share **one** depth-2 nav/footer partial — cleaner than a depth-1 list + depth-2 details split. Do not create `about/careers.html`.

**Task — to the IA Careers specs (3-block list + 7-block posting):**
1. Create **`about/careers/index.html`** (list page, **depth-2**, 3 blocks): **(1) Hero** short "working at VECTO" framing · **(2) Open roles list** job cards (title, team, location/remote, technology tags), each linking to its sibling posting page (`[job-slug].html`) per the one-template convention, **with a designed empty state** ("no open roles right now — leave your CV") · **(3) "Don't see your role?"** general **provider-backed** application form. Add the top-of-body placeholder-convention comment. Breadcrumb: Home → `../../index.html`, About → `../index.html`, Careers (current).
2. Create **`about/careers/senior-frontend-engineer.html`** (or similar) as the **one representative job posting page** (**depth-2**, sibling of the list, 7 blocks): **(1) Breadcrumb** Home (`../../index.html`) › About (`../index.html`) › Careers (`index.html`) › [Role] · **(2) Role hero** title, team, location/remote, employment type · **(3) About the role** · **(4) Responsibilities & requirements** (two lists) · **(5) Tech stack** technology tags linking to `../../how-we-work/technologies/…` pages (jobs↔tech relation) · **(6) Application form** per-job, provider-backed (name, contact, CV upload, note) · **(7) Related roles** other open postings. Add the `.tmpl-banner` naming its template role and `/about/careers/[job-slug]` production target.
3. Forms are static markup only (name/email/message/upload placeholders) — **do not** wire submission; add an HTML comment noting the provider-backed pattern (C4, the site-wide forms note).

**Files:** `about/careers/index.html` (new, **depth-2**), `about/careers/senior-frontend-engineer.html` (new, **depth-2**). Both use the **same depth-2 nav/footer partial** — a clean depth-2 partial where **every** nav/footer link is `../../`-prefixed (do NOT reuse the how-we-work depth-2 partial, whose how-we-work-local links use `../technologies/…` — those would be wrong here; generate the all-`../../` variant).

**Verify:** both pages load at `about/careers/`; job page tech tags link correctly to `../../how-we-work/technologies/…`; the list's breadcrumb reaches the About hub via `../index.html` and root via `../../index.html`; both forms render as static fields; **no `about/careers.html` file exists**; depth-2 nav/footer resolve (run `preview_network` failed on both — they're the deepest new About pages). `.tmpl-banner` present on the job page. Lucide === 0.

---

## P5 — Our Work rebuilt to the miiind.co structure (outcome groupings removed)

**Sources:** E1 (remove outcome groupings, rebuild), C1 (filter strip reflects the active facet). Depends on P1. C6 keyword-filters and C1 one-way-door behavior land in P6; this prompt is structure + presets.

**Context:** `our-work/index.html` currently uses **outcome-grouped** sections (`.og-item`, "featured" rows inside outcome stories) with the multi-facet `[data-facet-bar]` (industry/technology/service/subservice/platform/country/size) wired by `initFacetFilter`. The hero reads "The outcomes that mattered." The IA has been rewritten **filter-led**: header + filters → **Featured** section (CMS-flagged, order) → **asymmetric grid** on three aspect-ratio presets (1:1, 2:3, 3:2). Outcome groupings are removed. Read the rewritten Our Work hub spec + the new structural reference (miiind.co/portfolio) note in the IA.

**Task:**
1. **Remove the outcome groupings** entirely (the `.og-item` outcome-story sections and the "grouped by outcome" rationale/design copy). **"Away from outcome framing" means removing the outcome-grouped *organization* — not the word "outcomes."** The current hero line "The outcomes that mattered." is replaced by the IA's canonical counter hero in step 2 (which *does* keep the word "outcomes"); what's retired is grouping the grid into outcome stories, not the vocabulary. Do not drop or reword the counter line to avoid "outcomes" — it is IA canon (see step 2).
2. Build the new structure to the IA's **7-block hub spec**: **(1) Hero** — the IA-canon counter line "[N] projects. [N] industries. [N] outcomes that mattered." **kept verbatim** (this replaces the old "The outcomes that mattered." hero; counts are build-time, never hardcoded — comment it) · **(2) Filter strip** (see P6 for behavior) · **(3) Featured projects** — a handful of CMS-flagged featured cards (comment noting `featured` flag + order), larger editorial cards · **(4) Asymmetric project grid** — all projects, each card using one of three **aspect presets** (1:1 / 2:3 / 3:2); card = thumbnail + client + industry tag + service tag (**no headline outcome metric on cards — retired feature**) · **(5) Filter result count** (client-side) · **(6) Sticky Estimator CTA** · **(7) Closing CTA** "Want a project like one of these? Get an estimate →". Add an HTML comment noting `aspect_preset` is a per-project CMS enum and three image-constraint sets exist.
3. **Keep the `initFacetFilter` contract intact** (`[data-facet-bar]`, `.facet[data-facet]` checkboxes, `[data-filter-count]`, `[data-filter-empty]`, `[hidden]` reset gotcha) — the facet strip stays; only the results layout changes from outcome groups to featured + asymmetric grid. Rename the `data-facet="size"` legend to **"Company stage"** if not already (drift-fix P3 may have landed this — confirm).
4. Reuse the contained-banner pattern for featured cards (avoid the `.card--with-image` "void" — see `CLAUDE.md` gotcha (e)).
5. All project cards continue to link to `fintech-platform.html` per the one-template convention until P8 updates the case-study path.

**Files:** `our-work/index.html`. Possibly `components.css`/`layout.css` for the aspect-preset card classes (add, don't hardcode values — use tokens).

**Verify:** no `.og-item`/outcome-story markup remains; the page renders header+filters → Featured → asymmetric grid; filtering still works (select a facet value, `[data-filter-count]` updates, `[data-filter-empty]` behaves, no `[hidden]` regression — this bit the filter 3× before); the three aspect presets are visibly distinct. Geometry for counts + **one screenshot** (the `[hidden]`/display blind spot needs a visual). Lucide === 0.

---

## P6 — Portfolio filter behavior: keyword comboboxes + one-way-door (dropdowns never navigate)

**Sources:** C6 (keyword filters in Service/Sub-services + Industry dropdowns), C1 (one-way-door hub semantics). Depends on P5 (operates on the rebuilt filter strip).

**Context:** The hub filter is the **one-way door's hub side**: dropdowns compose **freely as query-param state** and **never navigate** (facet *landings* are the entry pages — P7). With 13 industries and 46 sub-services, the Service/Sub-services and Industry dropdowns need **type-to-narrow** keyword filters (combobox pattern). `initFacetFilter` already does AND-across/OR-within with dependent sub-services, and (post drift-fix P4) **reads** filter state from the URL on load — but **writing** state back to the URL on selection is not yet implemented. This prompt establishes the write side so read + write form a complete, shareable loop.

**Task:**
1. Add a **client-side keyword filter (combobox)** inside the **Industry**, **Service**, and **Sub-services** facet dropdowns: a text input at the top of the dropdown that narrows the visible checkboxes as you type. Keep it consistent with the existing static-index/build-time-search pattern (C6) — no search backend. Extend `prototype.js` with a small generic helper (e.g. `initFacetKeyword`) reusing the existing dropdown DOM; respect the `[hidden]`-needs-display-reset rule for hidden options.
2. **Write filter state to the URL (decided — do build this, don't just assert it).** On every facet change, `initFacetFilter` should **write the current selection into the URL via `history.replaceState`** (query params matching the format drift-fix P4's deep-link reader already parses — keep read and write on one shared param scheme, e.g. `?industry=healthcare&industry=fintech&service=…`). Use `replaceState` (not `pushState`) so composing a filter doesn't spam the back button; clearing all facets should clear the params. This is cheap — the read half already exists — and makes **shareable/deep-linkable filter URLs** a real, testable behavior rather than an assumption. It also underpins P7's canonicalization ("query states matching a promoted facet canonicalize to its landing").
3. **Encode the one-way-door hub behavior:** dropdown selections update **query-param state only** (via step 2) and **never trigger navigation, a reload, or a page-shape shift**. Add an HTML comment stating the model (hub filtering = pure in-place query-param state written to the URL; facet landings are the canonical link targets everywhere except these hub controls). No visual re-architecture — this is the behavioral contract for P7.

**Files:** `our-work/index.html`, `prototype.js`.

**Verify:** typing in the Industry combobox narrows to matching industries and still lets you check/uncheck; same for Service and Sub-services; **selecting facets rewrites the URL query params in place (assert `location.search` reflects the current selection after a change) with no navigation, reload, or route change**; **reloading the rewritten URL restores the same selection** (proves the read↔write loop and shareable URLs); clearing all facets clears the params. Existing `initFacetFilter` behavior (dependent sub-services, count, empty state) still intact. Lucide === 0; screenshot an open, filtered dropdown.

---

## P7 — Facet landing pages: two examples (industry + service) on one shared template

**Source:** C1. Depends on P5/P6 (shares the hub's filter strip + one-way-door semantics) and P1 (the AI deep-links repointed here also touch the homepage in P11).

**Context:** Facet landings are **ENTRY pages**, not filter states — the canonical link targets everywhere **except** the hub's own filter controls. Namespaced URLs: `/our-work/industry/<slug>` and `/our-work/service/<slug>`. Each has its **own H1 + editorial intro** with its filter **pre-selected**; **touching its filters navigates to the hub** carrying the composed state (option (b) — see task step 3, not filter-in-place); matching query states canonicalize to the landing. Build **both axes on one shared template** (per Andranik: same template, different axes). Keep the `/our-work` base.

**Task:**
1. Create **two depth-2 example pages sharing one template**: `our-work/industry/healthcare.html` (or another industry — pick one representative) and `our-work/service/ai-transformation.html`. Same layout, differing only in the pre-selected facet axis and the editorial header/intro.
2. Each page: unique **H1** + editorial intro slot naming the facet, breadcrumbs (Home → Our Work → [facet]), the **filter strip reflecting the active facet pre-selected**, the filtered grid (reuse the P5 asymmetric-grid + `initFacetFilter`), an empty/low-count state, and a `.tmpl-banner` naming the template role and `/our-work/[facet-type]/[slug]` production target (the two namespaced axes as examples).
3. **One-way-door wiring — build option (b), navigate to the hub (NOT filter-in-place).** A **facet selection change** on a landing — a checkbox toggle in any facet dropdown — must **navigate to the hub** (`../index.html` → `/our-work`) carrying the landing's pre-selected facet **plus** whatever the user just selected, applied as hub query-param state (e.g. `../index.html?industry=healthcare&industry=fintech`). It must **not** refilter the grid in place on the landing. **Clarification — the keyword combobox is not a selection:** typing in the P6 keyword-filter box only narrows the *visible* checkbox options and must **not** navigate; navigation fires on the actual facet selection change (checkbox toggle), never on keystrokes in the keyword input. Rationale to bake in: a landing is a page you *arrive* at; the moment you start filtering you're *browsing*, and browsing (any combined/composed state) lives on the hub's URL — filtering in place would strand a composed state like "healthcare + fintech" on the healthcare landing's URL, validating the wrong production behavior. This is intentional: it exposes the one UX seam worth testing here — **the editorial facet header disappears the instant you leave the landing for the hub**. If that transition feels jarring in stakeholder testing, that's a finding, not a bug to hide. Implementation note: on a landing, the P6 `initFacetFilter`/keyword-combobox interactions are re-bound (or intercepted) to compose a hub URL and navigate, rather than running the in-place filter pass they run on the hub itself. Add an HTML comment stating: landing = canonical entry (query states matching this facet canonicalize here); first filter interaction → navigate to hub query-param state.
4. **Repoint deep-links** to the new landings where they are landing-eligible: the homepage AI band "See it in practice →" and AI Transformation hero "See our AI work →" → `our-work/service/ai-transformation.html` (the homepage repoint executes in P11; do the **AI Transformation hero** repoint here in `services/ai-transformation.html`). Glossary "See [term] in our work" stays a **query-param/noindex** link (terms are not promoted facets) — leave as-is.

**Files:** `our-work/industry/healthcare.html` (new, depth-2), `our-work/service/ai-transformation.html` (new, depth-2), `services/ai-transformation.html` (hero CTA repoint). Depth-2 nav/footer + breadcrumbs.

**Verify:** both landings load with the correct facet pre-selected and their own H1/intro; **toggling a facet checkbox navigates to `/our-work` (the hub) with the composed query-param state — the landing's facet stays applied AND the just-toggled value is added — and the grid does NOT refilter in place on the landing** (confirm the URL changes to the hub path and the editorial facet header is gone post-navigation); **typing in the keyword combobox only narrows the visible options and does NOT navigate** (assert the URL/page is unchanged while typing); breadcrumbs + depth-2 `../../` links resolve (`preview_network` failed on both); the AI Transformation hero CTA points at `../our-work/service/ai-transformation.html`. `.tmpl-banner` present. Lucide === 0; screenshot one landing.

---

## P8 — Case study example: `/projects/[project-name]` URL contract + external product CTA

**Sources:** C8 (verbatim `/projects/` URL preservation), E6 (external CTA present + absent-state). Depends on P1; relates to P5/P7 (hub/landing links).

**Context:** Existing live case studies keep their slugs **verbatim** — full-path preservation: detail pages live at **`/projects/[project-name]`** (zero redirects). The wireframe currently has the case study at `our-work/fintech-platform.html`, and **20 pages across all three depths link to it** (~137 hrefs: `fintech-platform.html`, `our-work/fintech-platform.html`, `../our-work/fintech-platform.html`, `../../our-work/fintech-platform.html`) plus a `legal/sitemap.html` entry. The **hub + facet/filter pages keep their own `/our-work` base**; only the **detail** page reflects `/projects/`. Read the case-study template spec + the "URL contract" impact-note in the IA.

**Decision (settled here): relocate, don't keep a stub.** The wireframe's `our-work/fintech-platform.html` was never a real live URL — it's a wireframe artifact — so there's no ranking equity to protect and no redirect to simulate. Move the page to `projects/[slug]`, repoint every inbound link, and **delete the old file**. No stub, no redirect page. (Real production `/projects/*` URL preservation is a hosting-layer concern, out of the wireframe's scope.)

**Task:**
1. Create the case-study detail at the **`/projects/` path**: **`projects/sentigraph-ai.html`** (a real preserved-slug example, matching the IA's `/projects/sentigraph-ai/` sample). Start from the existing `our-work/fintech-platform.html` content and **adapt it to match the slug** — the current page is about a *fintech platform*, so **rename the placeholder client/product to "SentiGraph"** (a believable AI product — e.g. sentiment-analysis / social-graph intelligence) and adjust the copy that names the domain (hero, client snapshot, challenge, industry/service tags, testimonial attribution) so the page is internally consistent with a sentigraph-ai slug. **Keep the 11-block case-study anatomy** (Hero · Client snapshot · Challenge · Approach · Tech stack · Timeline & team · Outcomes · Testimonial · What's next · Related case studies · CTA) and the placeholder metrics/figures — this is a copy adaptation, not a rewrite. Note the **headline outcome metric is retired from the hero** (quantified results stay in the Outcomes block). The **breadcrumb + any self-referential URL** must read `/projects/[project-name]`. Add a `.tmpl-banner` naming the template and the `/projects/[project-name]` verbatim-URL contract.
2. **External product CTA (E6):** this example **has** one — external CTA in the **hero** and repeated in the **closing CTA row** ("Launch website" / "Try now"), linking out. Add an HTML comment: `cta_label`/`cta_url` optional, hidden when absent.
3. **Exercise the absent state:** add a second lightweight `/projects/` example **without** the external CTA (e.g. `projects/[second-slug].html`, minimal anatomy is fine) and have at least one hub/landing card point at it — so the hidden-when-absent discipline is visible against a real page, not just a comment. Repoint a share of the cards to this second example so both `/projects/` pages are reachable.
4. **Site-wide repoint + delete (the critical step).** `grep -rl "fintech-platform.html"` across the wireframe (exclude `.git`/worktrees) — currently ~20 files including `index.html`, `get-an-estimate.html`, every `services/*.html`, `industries/*`, `who-we-serve/*`, `how-we-work/technologies/*` (depth-2), `our-work/index.html`, `legal/sitemap.html`, and the P7 landings (built earlier, so they'll be in the grep). **Repoint every href to `projects/sentigraph-ai.html` at the correct depth** (root → `projects/…`; depth-1 → `../projects/…`; depth-2 → `../../projects/…`; and from `our-work/index.html` → `../projects/…`). Update the `legal/sitemap.html` entry to the `/projects/` URL. Then **delete `our-work/fintech-platform.html`**. (The homepage hrefs are repointed here too — P11 only changes homepage *structure*, not this link.)

**Files:** `projects/sentigraph-ai.html` (new, depth-1 under `/projects/`) + `projects/[second-slug].html` (new, absent-CTA example), **every file returned by the grep** (~20, all depths) for href repointing, `legal/sitemap.html`, and **delete** `our-work/fintech-platform.html`.

**Verify:** both case studies resolve under `projects/…`; the SentiGraph page's copy matches its slug (no leftover "fintech platform" naming — grep the page); breadcrumb/self-URL reads `/projects/`; **`grep -r "fintech-platform.html"` across the wireframe returns zero** (all repointed, old file deleted); `preview_network` (filter `failed`) on a root, a depth-1, and a depth-2 page returns none (catches any wrong-depth repoint); the CTA-present example shows hero + closing external CTAs and the second example shows the absent state. Lucide === 0; screenshot the SentiGraph hero showing the external CTA.

---

## P9 — Estimate / Contact / Schedule pipeline simplified + "90 seconds" copy sweep

**Source:** E4 (+ D12, D13). Depends on P1 (S&C already gone from nav; Contact procurement path removal completes here).

**Context:** Internal testing found the 3-path contact setup overcomplicated. `get-an-estimate.html` is currently an AI-estimator page (hero "Get a ballpark range in 90 seconds", `[data-estimator]` demo form, output card, "A range not a number" accuracy section, comparable projects, save/share). `contact.html` has **three** intent paths (Get an estimate · Schedule a call · Send a question) + a procurement/InfoSec Security & Compliance block. "90 seconds"/ballpark copy recurs (homepage 418/818-style lines, estimate hero, meta descriptions, hub CTAs). Read the rewritten `/get-an-estimate`, Contact, and Schedule specs in the IA.

**Task:**
1. **`get-an-estimate.html`** → rewrite to the launch flow (IA 6-block spec): **(1) Hero** "Tell us about your project — get a ballpark from the team." + reply-expectation copy (e.g. within one business day), **no "90 seconds"** · **(2) Estimate form** plain-language fields (project description free-text + optional scope selectors: service interest, timeline, budget bracket + contact details), provider-backed · **(3) What happens after you submit** three honest steps (we read it → ballpark by email → optional call) — absorbs the old accuracy reassurance · **(4) Success state** the one designed post-submit moment: confirmation + optional **Schedule a Call** step (build it as a real interactive success state worth validating) · **(5) Comparable case studies** editorially-curated "projects like yours" teaser into the portfolio · **(6) "Wondering which way to work with us?"** cross-link to the **Engagement Models** page. **Park** the AI-estimator specifics (live calculator/output-card/accuracy/dynamic comparables/save-share) — remove from the page (IA Appendix); HTML comment noting the AI estimator returns later as a client island. The `[data-estimator]` demo wiring is no longer the hero mechanic.
2. **`contact.html`** → IA 5-block spec: **(1) Hero** "How would you like to start?" · **(2) Path 1 — Get an Estimate** card ("best when you have a project in mind and want numbers") · **(3) Path 2 — Send a question** lightweight form ("best for general inquiries, partnerships, press") · **(4) Office locations** · **(5) Direct contacts**. **Remove the Schedule-a-call intent card** (scheduling now via the estimate success state) and **remove the procurement/InfoSec Security & Compliance block** entirely (drop the `about/security-compliance.html` cross-link).
3. **`schedule-a-call.html`** → keep as the optional step's destination but **demote its prominence** (reached from the estimate success state + About menu + direct bookings; no longer a peer path). Keep its "Not ready to talk yet? → Get a ballpark first" estimator cross-link.
4. **Copy sweep:** replace every "ballpark in 90 seconds" / "About 90 seconds" / instant-ballpark promise across `get-an-estimate.html`, `contact.html`, any hub CTA pages + meta descriptions with human-reply framing ("tell us about your project — get a ballpark from the team"). **On `index.html`, sweep only the blocks that survive P11's restructure** (e.g. the AI band / intro CTA line at ~L418) — **skip block 13** (the estimator embed at ~L818): P11 replaces it wholesale with new copy, so touching it here is wasted/conflicting work. Nav-strip copy was handled in P1; grep the whole site for "90 seconds" to catch stragglers (P11 finishes the homepage, so a residual in block 13 at this stage is fine).
5. **Naming sweep:** grep the whole site for **"Project Estimator"** and replace with **"Get an Estimate"** (page `<title>`/H1/meta on `get-an-estimate.html` included) — the tool name is retired until the AI estimator returns. Nav/footer instances were handled in P1; this catches page copy, titles, and cross-link labels (e.g. the schedule-a-call cross-link, blog-hub cross-promo cards).

**Files:** `get-an-estimate.html`, `contact.html`, `schedule-a-call.html`, `index.html` (surviving-block copy only here — structural homepage edits + block-13 copy in P11), `prototype.js` (success-state toggle, step below), plus any hub page with the promise.

**Success-state toggle (resolves the "don't wire forms" tension):** forms stay **static markup with no real submission** (C4 pattern) — but the success state must be *viewable* to validate the designed post-submit moment. Add a **prototype-only** toggle in `prototype.js` (e.g. `initEstimateSuccess`: on the estimate form's submit event, `preventDefault()` and reveal the success-state block instead of posting) — a display toggle, **not** a submission. This is the sanctioned exception to "don't wire," scoped to showing/hiding the success panel.

**Verify:** grep the whole wireframe for `90 seconds` / `ballpark in` → **zero except possibly homepage block 13** (the estimator embed, which P11 replaces — P12's sweep confirms zero site-wide). Estimate page shows form → success-state-with-schedule-step: **trigger the toggle** (dispatch the form submit) and confirm the success panel + optional Schedule CTA appear and no navigation/POST occurs. Contact shows exactly **two** intent paths, no procurement/S&C block, no `security-compliance` link. Lucide === 0; screenshot the estimate success state.

---

## P10 — Blog: category chips as real links + one example category page + load-more

**Sources:** C5 (category routes), E2 (two-tier tagging). Depends on P1.

**Context:** Blog is the **opposite of the portfolio** — categories are **single-select**, so the hub's category chips **ARE navigation** (real links to `/blog/category/[topic]`), no composition conflict, no one-way door. `blog/index.html` currently uses `initPortfolioFilter` (client-side single-select chips: **All / Build / Design / AI / Founder advice / Engineering / Industry insights** — the *old topic-cluster set*) with `[data-filter-group]`. **The reconciled IA (blog hub block 3, E2/D8) retired that list and replaced it with a placeholder primary set: Tech News · Company Updates · Insights · Guides** (marked placeholder pending D15 — final list with the content/SEO team). Read the rewritten Blog hub Categories block + post-template tagging (two tiers: one **primary** routable category + **secondary** relations: projects/services/technologies/industries) in the IA.

**Task:**
1. **Replace the chip set** with the IA's placeholder primary categories — **Tech News · Company Updates · Insights · Guides** (drop the old Build/Design/AI/Founder advice/Engineering/Industry insights clusters). Add an HTML comment noting this is a **marked placeholder set pending D15** (content/SEO team finalizes the list).
2. Convert those chips **from client-side filter buttons to real `<a>` links** pointing at `/blog/category/[topic]` routes (e.g. `blog/category/insights.html`). Keep an "All" that returns to the hub. (The `initPortfolioFilter` client-filter can be retired from the hub, or kept only for a non-navigational secondary control — but the primary category axis must be links.) Update any post `data-tags` that referenced the old clusters to the new primary categories.
3. Create **one example category page** — **`blog/category/insights.html`** (one of the new primary set; depth-2 under `blog/category/`): H1 for the category, optional editorial intro, the filtered post list, breadcrumbs (Home → Blog → [category]), `.tmpl-banner` naming `/blog/category/[topic]` as the template target. (Do **not** build `blog/category/ai.html` — "AI" is no longer a primary category.)
4. **Pagination — validate load-more (instinct):** implement a **load-more** control on the **recent-posts list on the hub AND on the example category page** (both are post lists that can exceed one batch; the IA says the category page paginates "as on the hub"). Reveal the next batch of placeholder posts client-side rather than numbered pages. Use **one shared helper** `initLoadMore` in `prototype.js` (bind to any `[data-load-more]` list, so both pages reuse it — don't write two). HTML comment noting the pattern decision was validated here (D9).
5. **Post template two-tier relations — build the modules, don't just comment them.** On the example post (`blog/building-ai-that-ships.html`), make the two-tier model **visible and interactive**: (a) show its **one primary category** as a routable chip/label linking to its `/blog/category/[topic]` page; (b) build the **secondary-relation cross-discovery modules** as real on-page sections — "Related projects" (cards → `../projects/…`), "Related services" (→ `../services/…`), "Related technologies" (→ `../how-we-work/technologies/…`), "Related industries" (→ `../industries/…`) — populated with believable placeholder links. These modules are a UX element worth validating, so they must render, not sit in a comment. Add a short HTML comment stating the *rule* (exactly one primary category = routable; the four relations power cross-discovery in both directions and **never** create routes) — the comment documents the model, the modules demonstrate it.

**Files:** `blog/index.html`, `blog/category/insights.html` (new, depth-2), `prototype.js` (load-more), `blog/building-ai-that-ships.html` (relations comment/modules + primary-category update).

**Verify:** the hub chips read **Tech News · Company Updates · Insights · Guides** (old clusters gone); they are `<a>` links that navigate to `/blog/category/…` (not client toggles); `blog/category/insights.html` loads with correct breadcrumbs and depth-2 links (`preview_network` failed === none); load-more works on **both** the hub and the category page (reveals the next batch, hides its control when exhausted) via the shared `initLoadMore`; `.tmpl-banner` present. **The example post renders visible related-content modules** (Related projects/services/technologies/industries) with resolving links + a routable primary-category chip — not just an HTML comment. Grep confirms no `data-filter="ai"`/old-cluster remnants drive a chip. Lucide === 0; screenshot the hub chips + a load-more interaction + the post's related modules.

---

## P11 — Homepage reconciliation (batched — index.html touched by many items)

**Sources:** E1/D14 (block 9), E3d (block 10), E5 (block 10a), E4 (blocks 13 & 16), C1 (AI band deep-link). **Runs late** because its links depend on pages built in P2, P3, P7, P8. Batched to touch `index.html` once for structure.

**Context:** `index.html` is hit by five reconciled items. Current landmarks: block 9 = outcome-grouped portfolio (`.portfolio-feature` + "grouped by the outcome" + supporting outcomes); block 10 = Reviews (links "Read all reviews" → `about/index.html`); block 13 = estimator embed ("Get a ballpark in 90 seconds", `[data-estimator]`); block 16 = triple contact-CTA (`.contact-ctas` 3-col grid); the AI band "See it in practice →" deep-link. Read the updated homepage block specs in the IA. (The E4 "90 seconds" *copy* on the homepage was swept in P9; this prompt handles the *structural* homepage changes and any remaining links.)

**Task:**
1. **Block 9 (E1/D14):** replace the outcome-grouped portfolio with a **curated featured grid** (6–8 CMS-flagged featured projects, layout validated here to the miiind reference) + a **"Browse all work →"** link to `our-work/index.html`. No outcome axis. Card links point at the P8 `projects/[project-name]` path.
2. **Block 10 (E3d):** Reviews block → **CMS-testimonial cards with source links** (author, company, text, source link — no embedded widgets); "Read all reviews" → **`about/testimonials.html`** (was `about/index.html`).
3. **Block 10a (E5):** add a **compact Solutions strip** — "Products we build and run" — the mini-portfolio (onemall · onesocial · quickoffer · plugins) linking to `solutions/index.html`. Deliberately lighter than the portfolio module; sits with the proof cluster. Keep it distinct from the featured grid (solutions are never mixed with client work).
4. **Block 13 (E4):** mini-estimator embed → a **simple Estimate CTA block** — "Tell us about your project — get a ballpark from the team." → `get-an-estimate.html`. Remove the `[data-estimator]` demo from the homepage.
5. **Block 16 (E4/D12):** triple contact-CTA → **dual CTA** (Get an Estimate · Send a question), mirroring the Contact two-path decision.
6. **AI band deep-link (block 5, C1):** repoint the AI positioning band's "See it in practice →" to **`our-work/service/ai-transformation.html`** (the P7 facet landing). Leave "How we implement AI →" pointing at `services/ai-transformation.html`.

**Files:** `index.html` (+ `components.css`/`layout.css` if the featured grid / solutions strip need classes — tokens only).

**Verify:** no outcome-group markup remains on the homepage; block 9 is a featured grid with a "Browse all work" link to `our-work/`; Reviews cards carry source links and "Read all reviews" → `about/testimonials.html`; a Solutions strip → `solutions/index.html` exists; block 13 is a CTA (no `[data-estimator]` on the homepage); block 16 is dual; AI band → the service facet landing. All new links resolve (`preview_network` failed === none). Lucide === 0; top-of-page + modest-scroll screenshots (mid-page shots are unreliable per `CLAUDE.md`).

---

## P12 — Whole-site reconciliation sweep (run last)

**Purpose:** now that every P1 target exists, confirm the site is internally consistent and no link is dangling.

**Task / Verify (no new content):**
- **Nav/footer consistency:** on a root, a depth-1, and a depth-2 page, re-assert the **7 links + CTA** nav, rebuilt About menu, Solutions link, language switcher, and Testimonials-in-footer — confirm P2–P11's new pages all carry the depth-correct partial.
- **Broken-link sweep:** `preview_network` (filter `failed`) on at least one page per depth **including the deepest new pages** (`about/careers/[job].html`, `our-work/industry/…`, `our-work/service/…`, `blog/category/…`, `projects/…`) — **zero** failures now (the P1 expected-missing targets must all resolve).
- **Dead-reference sweep:** grep the whole wireframe for `security-compliance`, `fintech-platform.html` (old case-study path — deleted + repointed in P8), `90 seconds`, `ballpark in`, `Project Estimator` (naming retired in P1/P9), and outcome-group class names (`.og-item`, "grouped by the outcome") → **zero** live occurrences.
- **Lucide:** `document.querySelectorAll('i[data-lucide]').length === 0` on a sample across depths.
- **Route/URL fidelity:** spot-check breadcrumbs on each new template page and confirm `/projects/[project-name]` reads verbatim on the case study, `/our-work/[axis]/[slug]` on the facet landings, `/blog/category/[topic]` on the category page, `/about/careers/[job-slug]` on the job page.
- Restore `.claude/launch.json` to the original port-4321 config if it was flipped for preview (per `CLAUDE.md`). Commit/push only if asked.

---

## Coverage map (Part F ledger → prompt)

| Ledger row (Src) | Prompt |
|---|---|
| E1 — Our Work miiind rebuild, outcome groups removed | P5 |
| E1/D14 — Homepage portfolio → curated featured grid | P11 |
| E3a — About hub + Company + Team; menu re-propagated | P1 (menu) · P3 (pages) |
| E3b — Careers list + example job posting + form | P4 |
| E3c — Remove Security & Compliance everywhere | P1 (nav/footer) · P3 (About) · P9 (Contact) |
| E3d — Testimonials page; homepage Reviews → CMS cards | P3 (page) · P11 (homepage block 10) |
| E4 — Estimator page simplified; homepage block 13 | P9 (page) · P11 (block 13) |
| E4/D12 — Contact two paths; homepage block 16; Schedule demoted | P9 · P11 (block 16) |
| E4 — "90 seconds" copy sweep | P1 (nav strips) · P9 (site) |
| E5 — Solutions hub + example; 7-link+CTA nav; homepage strip | P1 (nav) · P2 (pages) · P11 (block 10a) |
| E6 — External product CTA (case study + solution) | P2 (solution) · P8 (case study) |
| C1 — Facet landing example(s) + hub filter reflects facet | P5 · P6 · P7 |
| C8 — Case study `/projects/[project-name]` URL/breadcrumb | P8 |
| C2 — Language switcher (simulate 2nd-language state) | P1 |
| C5 — Blog category chips as links + example page + load-more | P10 |
| C6 — Keyword comboboxes in portfolio dropdowns | P6 |

B-series items are doc/code-convention only — no wireframe impact, correctly absent here.
