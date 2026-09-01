# VECTO Wireframe — Claude Code Prompt Package

Sequenced prompts to build the wireframe in Claude Code. Run **in order** — each builds on the last. Paste one prompt per turn; let it finish and eyeball the result before moving on.

**Before you start, make sure Claude Code can see:**
- `docs/vecto-master-ia-revised.html` — canonical content & block structure (the source of truth)
- `docs/wireframe-build-plan.md` — architecture, component inventory, page inventory, pathing rules, fidelity standard
- `docs/legacy/figma-tokens-reference.md` — the enumerated Figma token system (authoritative values for `tokens.css`/`typography.css`) [archived 2026-06-30]
- Figma access (file `emDaz5ZTNMna0jK1al4G9z`) — to re-enumerate tokens live and to screenshot components for visual matching

**Working location:** build inside `wireframe/`. The plan docs + IA live in the sibling `../docs/` — request read access to `../docs/` (or copy the 4 files into `wireframe/docs-ref/` first).

**Standing instructions to include in your first prompt (or a CLAUDE.md):**
> Build a static HTML/CSS/JS **clickable prototype** — no framework, no build step, opens via a static server. It exists to validate IA, block & CTA placement, and copy with stakeholders. **Desktop-only — no mobile, no responsive breakpoints, no hamburger drawer** (fixed ≈1200px content width). Fidelity bar = the HES wireframe: token-driven CSS system, shared nav/footer partials pasted into every page with documented path prefixes, real on-brand placeholder copy (never lorem ipsum), semantic HTML + ARIA, prototype-only JS in one file. The IA (`vecto-master-ia-revised.html`) is the source of truth for every page's blocks and copy — reuse its hero headlines, FAQ questions, and CTA labels verbatim. Visual system = VECTO's Figma file: **dark theme, red brand (`#CA1D00`), pill buttons, Google Sans (Google Fonts API)**; for the wireframe **flatten the tokens to one simple `:root` of resolved Desktop-mode values — no two-tier aliasing, no responsive modes** (values in `figma-tokens-reference.md`). **Layout rule, tiered by IA depth (build-plan §4a): the Homepage and main hub/full pages must be strongly editorial — no default card grids (use splits, full-bleed bands, rails, lead+supporting, stat bands). Deep utilitarian reference pages (technologies/methodologies/tools indexes, glossary) MAY use clean categorized grids/index lists — don't force editorial gymnastics there, just keep them on-brand.** This is a premium agency site, not a SaaS dashboard. **Icons: use Lucide (no emojis, ever).** **Copy: reuse IA copy verbatim where given; otherwise mine each block's IA description/rationale to write believable, specific placeholder copy — never lorem ipsum.** Follow `wireframe-build-plan.md`. Don't contradict the IA; don't hardcode values that should be tokens.

---

## Prompt 0 — Scaffold

```
Read ../docs/wireframe-build-plan.md, ../docs/legacy/figma-tokens-reference.md, and ../docs/vecto-master-ia-revised.html in full first (request access to ../docs/ if needed).

Working inside wireframe/, create the complete empty file/folder tree exactly as specified in build-plan §4.1 (all directories, all .html files, the 4 .css files, prototype.js, and the 3 partials). Create empty placeholder files for now — no content yet except a one-line HTML comment in each naming the page and its IA section.

Then create a short README.md documenting: the path-depth convention (§4.3), the stylesheet load order, that this is a desktop-only clickable prototype, and that prototype.js is prototype-only. Confirm the tree matches §4.1 before stopping.
```

## Prompt 1 — Layout + utilities (`layout.css`)

```
Build layout.css — desktop-only, fixed values (no media queries, no mobile). Using the Figma layout tokens (figma-tokens-reference.md, Desktop values):
- .container: max-width = var(--content-max-width) (1200), centered, side padding = var(--grid-margins).
- .container-narrow, .section (vertical padding = var(--section-padding-v)).
- EDITORIAL primitives (this is the core of layout.css — see build-plan §4a): .split + .split--reverse (image↔text rows, 50/50 and a 60/40 variant), .band (full-bleed section), .rail (horizontal scroller for collections), .feature-lead (asymmetric lead item + smaller supporting items), .stat-band (figures + labels inline across the width), .index-list (categorized link index). These — NOT card grids — are the default building blocks.
- Provide .grid-2/.grid-3 ONLY for the rare deliberate case; do not make them the default. If used, prefer asymmetric/varied sizing.
- flex + gap + margin/padding utilities keyed to the spacing/base scale names (min, 4xs, 3xs, xxs, xs, s, m, l, xl, xxl, 3xl, 4xl) — e.g. .gap-s, .mt-m.
Use CSS variables only — no hardcoded px.
```

## Prompt 2 — Design tokens from Figma (`tokens.css` + `typography.css`)

```
Build tokens.css and typography.css from figma-tokens-reference.md. This is a desktop-only wireframe, so SIMPLIFY — do not replicate the full Figma token architecture:

tokens.css — ONE flat :root, resolved Desktop-mode values, no modes/media queries, no [data-theme], no two-tier aliasing. Define only what the wireframe uses, with semantic names but final values:
- colors: --surface-dark:#222429; --surface-elevated:#2B2C33; --surface-deep:#111214; --accent:#CA1D00; --accent-hover:#9E1300; --accent-light:#EB3213; --focus:#2BBAD6; --text-primary:#fff; --text-secondary:rgba(255,255,255,.48); --text-tertiary:rgba(255,255,255,.24); --border-default:#58595C; --border-light:#DCDDE0; --error:#E06531; (+ a couple of overlays as needed).
- type sizes & line-heights: Desktop column only (h1 56/64, h2 48/56, h3, h4 28/32, h5 22/28, h6 16/20, p1 20/32, p2 16/24, p3 14/20, c1–c4, button sizes). Single fixed values.
- spacing scale (spacing/base Desktop): --space-min..--space-4xl. Layout: --content-max-width:1200; --navbar-height; --section-padding-v; --grid-gap; --grid-margins. Radius: --radius-xxs..--radius-xl + --radius-pill:256px.
(The full two-tier/3-mode system stays in figma-tokens-reference.md for the future production build — the wireframe just doesn't need it.)

typography.css — load Google Sans from the Google Fonts API (<link href="https://fonts.googleapis.com/css2?family=Google+Sans:wght@400;500;700&display=swap" rel="stylesheet">); stack "Google Sans", system-ui, sans-serif. Type-scale utility classes mirroring Figma names: .t-h1…t-h6, .t-p1…t-p3, .t-c1…t-c4, plus .t-btn-huge/large/medium/small and input text styles. Fixed desktop sizes from the custom properties.

No page or component may hardcode a color, size, or radius — everything via var(--…).
```

## Prompt 3 — Components (`components.css`)

```
Build components.css per build-plan §5. Two buckets:

(A) ATOMIC — match the Figma components (screenshot each from file emDaz5ZTNMna0jK1al4G9z to verify) and bind to the semantic tokens:
- Button: PILL radius (var(--radius-pill)); 4 sizes huge/large/medium/small (font from --t-btn-*; padding from spacing scale); variants main/accent/secondary-light/secondary-dark/ghost/text; states default/hover/disabled — bind to button/* tokens. Plus the circular icon-button companion (arrow-in-circle) that pairs with pill CTAs on the sample page.
- Input: text/label(lg,sm)/placeholder/helper/error; border default/active/readonly/error; bg default/active — bind to input/* tokens.
- Tag/chip (tag/* tokens, primary/secondary + hover), Breadcrumb (breadcrumbs/* tokens), Card (surface/dark-elevated; small / list-v1 / list-v2 / with-image), horizontal tabs, comparison table (from the tables component), calendar (Schedule page).

(B) MOLECULES — not in Figma; build from spec, compose from the atoms + the layout.css editorial primitives (.split/.band/.rail/.feature-lead/.stat-band/.index-list), styled with tokens + the sample page's visual LANGUAGE only (node 8018:3317: dark elevated surfaces, small red icons, full-bleed red-tinted hero imagery, pill CTA + circular arrow icon, generous padding — NOT its card-grid layouts):
- 3 megamenus (Services 6-stage + AI band; Who We Serve 2-axis; How We Work 3-col), Resources/About dropdowns, persistent accent CTA in topbar, sticky Estimator CTA, process step strip (timeline, not cards), engagement decision tree, estimator widget shell, booking widget placeholder, specialist row, in-page anchor nav strip, stat-band, feature-lead collection block.
- CRITICAL (build-plan §4a): do NOT default collections to uniform card grids. Services 6-stage = horizontal journey/timeline; industries/tech = editorial index lists or rails; benefits/sub-services = alternating splits or lead+supporting; portfolio = outcome groups with varied card sizes. A "card" component may exist, but rows of identical cards must not be the default layout.

Icons via Lucide everywhere (data-lucide attributes; the circular-arrow CTA motif = arrow-right/arrow-up-right in a pill/circle). No emojis. Everything token-driven: colors → semantic vars, sizes/spacing/radius → vars. No hardcoded values.
```

## Prompt 4 — Partials (`_nav.html`, `_footer.html`)

```
Build _nav.html and _footer.html per build-plan §6 and the IA nav sections (mm-services, mm-who, mm-howwework, mm-resources, mm-about, mm-cta, mm-footer).

_nav.html: topbar with logo lockup; primary nav (Services ▾, Who We Serve ▾, Our Work [direct link], How We Work ▾, Resources ▾, About ▾) + the Get an Estimate accent CTA button; the 3 full megamenu panels and 2 dropdown panels as markup; mobile hamburger affordance with the CTA kept in the header. At the very top, include the path-depth prefix table (§4.3) as an HTML comment so anyone pasting it knows how to adjust ../ per folder.

_footer.html: the 5-column footer + utility row exactly per IA mm-footer, with the legal/social/copyright utility row.

Use semantic landmarks and ARIA (role=banner/navigation/contentinfo, aria-haspopup, aria-expanded). Write real labels, not placeholders.
```

## Prompt 5 — Skeleton QA page (`_skeleton.html`)

```
Build _skeleton.html: a single design-system QA page that renders every component from components.css once — type scale, all button variants, badges/tags, cards, the megamenus (with a note to click to open), dropdowns, form elements, accordion, callouts, breadcrumb, filter chips, comparison table, process strip, decision tree, sticky CTA, estimator + booking shells, specialist card. Paste in the _nav and _footer partials (root depth). This is the visual proof the system is complete — make it exhaustive.
```

## Prompt 6 — prototype.js

```
Build prototype.js (prototype-only, commented as such). Desktop-only — NO mobile/hamburger logic. Load Lucide via CDN in the page <head> (<script src="https://unpkg.com/lucide@latest"></script>) and call lucide.createIcons() on DOMContentLoaded so every <i data-lucide="..."></i> renders (no emojis anywhere). Then implement: megamenu open/close (hover + click, keyboard accessible), Resources/About dropdowns, accordion FAQ toggle, sticky Estimator CTA show/hide on scroll, portfolio filtering (client-side filter of demo items + live result count), engagement-models decision tree (Q&A → recommended model), the estimator widget stub (2-question mini → render a placeholder output card with cost range / timeline / recommended model), Process page step expansion, optional .rail horizontal-scroll affordances, in-page anchor nav (services hub + process), and active-nav-link highlighting using resolved pathname (so sub-directory index pages don't false-match — copy HES's approach). No framework.
```

## Prompt 7 — Homepage

```
Build wireframe/index.html — the Homepage — per IA §branch-home (all 17 blocks, in order). Paste in _nav and _footer (root depth). Use the components from components.css and reuse the IA's exact hero/sub copy, the AI positioning band body, FAQ questions, and CTA labels. Section order mirrors the nav narrative. Wire the home mini-estimator stub and the process strip. Every link resolves per §4.4. This is the showcase page — make it the highest-fidelity page in the set.
```

## Prompt 8 — Services hub + AI Transformation

```
Build services/index.html (IA §branch-services hub, 12 blocks: sticky stage anchor strip, the 6 stages as a HORIZONTAL JOURNEY/TIMELINE — not 6 equal cards (§4a) — with Build visually heaviest, the distinct AI Transformation as a full-width band, engagement snapshot, featured cases, FAQ, dual CTA) and services/ai-transformation.html (11 blocks, level-headed tone, 5 sub-services as alternating splits or a feature-lead block, 3 benefits ordered so AI-as-internal-tool is last, mini-process Audit→Pilot→Integrate→Operate timeline, FAQ of 5, specialist row, sticky Estimator CTA).

Apply §4a throughout: vary section rhythm, lean editorial, avoid uniform card rows.

Paste partials at depth 1 (../ prefixes). All sub-service cards link to services/web-development.html (the sub-service template example). Reuse IA copy verbatim.
```

## Prompt 9 — Remaining service category pages

```
Build the other 5 service category pages, each per its IA block list (11 blocks each), depth-1 partials, sub-service links → web-development.html, sticky Estimator CTA, specialist row, reuse IA hero/FAQ copy. Apply §4a — present sub-services as alternating splits / feature-lead / index, NOT uniform card rows; vary section rhythm per page so the six service pages don't all look identical:
- services/software-development.html (11 sub-service cards in 3 groupings; elevated process detail; full 33-tech stack)
- services/product-design.html (6 sub-services research→validation→execution)
- services/marketing.html (11 sub-services in 3 pillars)
- services/it-consulting.html (7 sub-services idea→spec)
- services/support-maintenance.html (4 sub-services; two-buyer hero)
- services/outsourcing-outstaffing.html (2 sub-services + comparison table)
```

## Prompt 10 — Sub-service template example

```
Build services/web-development.html as the representative sub-service template (IA sub-service template, 13 blocks: breadcrumb Home › Services › Software Development › Web Development, hero, what you get, sample work, mini-process, tech stack, timeline & team, case studies, engagement models, FAQ, talk to a specialist, related sub-services, sticky Estimator CTA). Add a small HTML comment banner noting this page represents the sub-service template for all 46 sub-services. Depth-1 partials.
```

## Prompt 11 — Who We Serve + Industries (hubs + template examples)

```
Build, depth-1 partials, IA copy verbatim, template tiles all linking to the built example:
- who-we-serve/index.html (IA §branch-whoweserve, 7 blocks: 5 company stages as an editorial index/list (not equal cards), 13 industries as an editorial index or rail with 1–2 featured verticals enlarged (§4a), cross-cutting cases, process strip, FAQ, dual CTA). Stage links → early-stage-startup.html; industry links → ../industries/healthcare.html.
- who-we-serve/early-stage-startup.html (company stage template, 10 blocks).
- industries/index.html (IA §branch-industries, 5 blocks: search + 13 industries as an editorial index/rail (not a uniform 13-cell grid, §4a) + cross-industry cases + FAQ + CTA). Links → healthcare.html.
- industries/healthcare.html (industry template, 9 blocks, includes the compliance block).
```

## Prompt 12 — Our Work + case study template

```
Build:
- our-work/index.html (IA §branch-ourwork, 7 blocks: counter hero, sticky filter strip, 4 outcome groups each led by one enlarged featured case with smaller supporting items (feature-lead / varied-size — not a flat uniform grid, §4a), client+industry+service tags (no headline metric on cards), live filter count, sticky Estimator CTA, closing CTA). Wire the filter + count via prototype.js. Project links → fintech-platform.html.
- our-work/fintech-platform.html (case study template, 11 blocks: hero with client/industry/service tags, client snapshot, challenge, approach, tech stack badges → technology pages, timeline & team, outcomes, testimonial, what's next, related cases, dual CTA). This is the conversion-critical template — highest fidelity of the template set.
```

## Prompt 13 — How We Work hub + Process + Engagement Models

```
Build, depth-1 partials, IA copy verbatim:
- how-we-work/index.html (IA §branch-howwework, 6 blocks: process snapshot, engagement snapshot, 3 reference-hub cards → technologies/methodologies/tools, FAQ, dual CTA).
- how-we-work/process.html (12 blocks: large interactive expandable 5-step diagram Kickoff→Scoping→Execute→Launch→Iterate, per-stage anatomy, "Sample first 30 days" timeline, communication cadence, tools). Wire step expansion via prototype.js.
- how-we-work/engagement-models.html (9 blocks: interactive decision tree → 4 model sections (Fixed Price / T&M / Dedicated Team / Staff Aug) → comparison table → FAQ → dual CTA). Wire the decision tree via prototype.js.
```

## Prompt 14 — Reference hubs + template examples (depth 2)

```
Build the 3 reference hubs and one template example each. These live 2 levels deep — partials use ../../ prefixes. Reuse IA copy.
- how-we-work/technologies/index.html (IA §branch-tech, 7 blocks: the stack as categorized INDEX LISTS — Frontend 10 / Backend 13 / Infra 10 as labeled columns of links, not 33 tiles (§4a)). Links → react.html.
- how-we-work/technologies/react.html (technology template, 8 blocks).
- how-we-work/methodologies/index.html (IA §branch-methodologies, 7 blocks: Delivery/Engineering/Quality grids). Cards → ci-cd.html.
- how-we-work/methodologies/ci-cd.html (methodology template, 8 blocks).
- how-we-work/tools/index.html (IA §branch-tools, 7 blocks: Collaboration/Dev/AI grids). Cards → jira.html.
- how-we-work/tools/jira.html (tool template, 6 blocks).
```

## Prompt 15 — Conversion pages: Estimator + Schedule

```
Build:
- get-an-estimate.html (IA §p-estimator, 8 blocks: hero, estimator widget stub, output card, "how accurate is this?", comparable case studies, cross-link to engagement-models, save/share, Schedule CTA). Wire the estimator stub via prototype.js (conversational input → placeholder output card with cost range / timeline / recommended model). Root depth.
- schedule-a-call.html (IA §p-schedule, 6 blocks: hero, booking widget placeholder, who you'll meet (specialist cards), what to expect, what to bring, what happens after). Root depth.
```

## Prompt 16 — Resources/Blog + templates

```
Build:
- blog/index.html (IA §branch-resources, 8 blocks: featured posts, categories, recent grid filterable by category/author, author spotlight, glossary entry card, tools entry cards, newsletter). Depth-1 partials. Post cards → building-ai-that-ships.html; author links → authors/jane-doe.html; glossary card → ../glossary/mvp.html.
- blog/building-ai-that-ships.html (blog post template: title, byline → authors/jane-doe.html, date, body with real placeholder prose, related posts, newsletter, share). Depth-1.
- blog/authors/jane-doe.html (author template, depth 2 — ../../ prefixes: bio, photo placeholder, role, expertise, their posts, social).
- glossary/index.html (light A–Z index) + glossary/mvp.html (glossary entry template: plain-English definition, related terms, related posts, single CTA). Depth-1.
```

## Prompt 17 — About + Security & Compliance + Contact

```
Build, IA copy verbatim:
- about/index.html (IA §branch-about, 9 blocks: history, mission/vision, named team grids, partners, trust signals, careers callout, Security & Compliance link, dual CTA). Depth-1.
- about/security-compliance.html (8 blocks: certifications, NDA/IP, data handling, secure dev practices, compliance experience, review process, security contact). Depth-1.
- contact.html (IA §p-contact, 7 blocks: 3 intent paths — Estimate card / Schedule card / send-a-question form — + office locations, direct contacts, procurement cross-link to security-compliance). Root depth.
```

## Prompt 18 — Mention stubs

```
Build the mention stubs: legal/privacy.html, legal/terms.html, legal/cookies.html, legal/sitemap.html, and 404.html. Each: nav + footer partials (legal/ is depth 1, 404 is root), a heading, and one paragraph of placeholder. sitemap.html lists every built page as a real link tree. 404.html is branded with a search field and links to the top entry points (Home, Services, Our Work, Get an Estimate). Purpose: every footer/utility link resolves.
```

## Prompt 19 — QA pass

```
Do a full QA pass on the wireframe:
1. Crawl every .html file and verify every href resolves to a file that exists (nav, megamenus, footer, breadcrumbs, cards, CTAs). Report and fix broken links. Confirm template-class links all land on the built example per build-plan §4.4.
2. Verify the path-depth prefixes are correct in every pasted partial (root / depth-1 / depth-2).
3. Confirm no page hardcodes a color, font, or spacing value that should be a token/utility — grep for hex codes and px in page <style> blocks.
4. Open the site (static server, desktop viewport) and check: all 3 megamenus + 2 dropdowns open/close, accordions toggle, portfolio filters + count work, decision tree works, estimator stub renders an output card, process steps expand, sticky CTA shows/hides.
5. Confirm every FULL page matches its IA block list (count blocks, check order) and that hero/FAQ/CTA copy matches the IA.
6. EDITORIAL-LAYOUT AUDIT (build-plan §4a, tiered): on Tier-1 pages (Homepage + main hub/full pages) flag any uniform grid of ≥3 identical cards and replace with an editorial alternative (split, band, rail, feature-lead, stat-band, index-list); no two consecutive sections should share structure. Tier-3 utilitarian reference/index pages (technologies/methodologies/tools, glossary, deep templates) MAY use clean grids — do not flag those, just confirm they're on-brand and uncluttered. The site overall must read as a premium agency site.
7. Confirm NO emojis anywhere; all icons are Lucide and render (data-lucide + createIcons). 
8. Confirm copy is believable/specific (reflects each block's IA intent), not lorem ipsum or generic filler — spot-check a few full pages against their IA descriptions.
(No mobile/responsive checks — desktop-only is intended.)
Produce a short QA report of what passed and what you fixed.
```

---

### Notes

- The Figma tokens are already enumerated in `figma-tokens-reference.md`; Prompt 2 re-confirms them live. Because nothing hardcodes color/type/size, any later Figma token change is a `tokens.css`/`typography.css` swap with no page edits.
- "Google Sans" loads from the Google Fonts API (`family=Google+Sans:wght@400;500;700`) — no fallback brand font needed.
- For atomic components (button/input/tag/breadcrumb/card), screenshot the Figma component while building (`get_screenshot` on the node IDs in build-plan §10) to match radius, padding, and states exactly. Marketing molecules are built from spec — use the sample page (`8018:3317`) as the visual north star.
- Prompts 8–17 are independent of each other once 0–6 are done; you can reorder by priority (e.g. build the homepage + services + our-work first to demo flows early).
- Keep the IA open in Claude Code's context the whole time — it's the content authority.
