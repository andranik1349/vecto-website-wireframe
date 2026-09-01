# VECTO Website — Wireframe Build Plan

**Companion to:** `vecto-master-ia-revised.html` (the IA is the source of truth for page content & block structure)
**Fidelity reference:** the HES wireframe (`github.com/andranik1349/HES → /wireframe`)
**Purpose of this doc:** the bridge between the IA (what to build) and Claude Code (how to build it). It defines the architecture, the design-system/component inventory, the navigation spec, the page inventory, and the representative-instance decisions. It deliberately does **not** re-transcribe the IA's block-by-block tables — for any page, the IA section named here is the canonical content spec.

**How this is used (your workflow):** plan & prompt-engineer here → build in Claude Code. The sequenced prompts live in `claude-code-prompts.md`. Build them in order.

---

## 1. Fidelity standard — what "HES-level" means

Every page must clear this bar (lifted from how HES is actually built):

1. **Token-driven design system, split across 4 CSS files** — `tokens.css` (variables only), `typography.css` (type scale), `components.css` (reusable UI), `layout.css` (containers/grids/utilities). No hardcoded colors, spacing, or font values in page files — everything references a CSS variable or utility class.
2. **Shared nav + footer partials, pasted into every page.** Source of truth is `_nav.html` / `_footer.html`. Pages are static HTML (no build step), so the fragment is copied into each page's markup, with documented path-depth prefixes (see §4.3).
3. **A `_skeleton.html` QA page** rendering every component once, so the design system can be eyeballed in isolation.
4. **Real, on-brand placeholder copy — never lorem ipsum.** HES writes actual microcopy ("From the Blog", "No spam. Unsubscribe any time."). VECTO copy is written for the non-technical founder per the IA's voice (see §9). The IA already supplies most hero headlines and FAQ questions verbatim — use them.
5. **Semantic HTML + accessibility.** `role` landmarks, `aria-label`/`aria-expanded`, `.sr-only` labels on inputs, `aria-labelledby` on sections, real `<button>`/`<nav>`/`<header>`/`<footer>`/`<main>`.
6. **Prototype-only JS in one `prototype.js`**, clearly commented "do not port to production." Drives menus, accordions, sticky CTA, filters, the decision tree, and the estimator stub. No framework.
7. **Desktop-only.** This is a clickable prototype to validate IA, block & CTA placement, and copy with stakeholders — **not** a production site. Build for a fixed desktop viewport (≈1200–1440px content width). **No mobile, no responsive breakpoints, no hamburger drawer.** Skip all mobile-mode tokens and media queries. (If a window gets narrow, graceful is a bonus, not a requirement.)
8. **Editorial, premium layouts — not card grids.** See §4a. Uniform N-column card grids read as low-effort "AI slop"; the wireframe must lean into wide editorial composition even at this stage.
9. **Complete pathing.** Every nav, footer, breadcrumb, card, and CTA link resolves to a real file in the wireframe (see §4.4 for how template-class links are handled).

---

## 2. Visual direction & the Figma token system  *(Figma inspected — see `figma-tokens-reference.md`)*

**Decision (from kickoff):** VECTO's own aesthetic, on HES's architecture. The look is now sourced from the actual Figma file (`emDaz5ZTNMna0jK1al4G9z`, "VECTO universal style — TEST"), enumerated via full Plugin API. The full token extract lives in **`figma-tokens-reference.md`** — that file is the authoritative values source; this section captures only the architectural implications.

**What the Figma file actually is:** a **dark-themed, red-brand design system** with an atomic + dashboard-flavored component set. It supplies the token system and the atomic components (buttons, inputs, tags, breadcrumbs, cards, tabs, calendar, tables, global nav). It does **not** contain the marketing-site molecules the IA needs (megamenu, hero, portfolio grid, process strip, etc.) — those are built from spec, styled with these tokens and the visual language from the sample marketing page (node `8018:3317`).

**Corrected assumptions** (the earlier `#1a1a18`/`#f0c040` guess was wrong):
- **Brand is red:** `#CA1D00` core, `#9E1300` dark/hover, `#EB3213` bright/accent-light. Secondary is **cyan** `#2BBAD6` (used for focus rings).
- **Theme is dark:** primary surface `#222429` (`surface/dark`), cards `#2B2C33` (`surface/dark-elevated`), deep `#111214`; text is white with @48%/@24% secondary/tertiary.
- **Buttons are pill** (`corner radius/pill` = 256), in **4 sizes** (huge/large/medium/small) × variants (main/accent/secondary-light/secondary-dark/ghost/text) × states (default/hover/disabled). Signature motif from the sample page: a **pill CTA paired with a circular arrow icon-button**.
- **Font is "Google Sans"** (proprietary — see fallback note in §9).

**Token strategy for the wireframe — deliberately simplified.** The Figma system is two-tier (base→semantic) with 3 responsive modes. For a desktop-only clickable prototype that's more machinery than the goal needs, so **flatten it**:

- **One flat `:root` of resolved values.** Don't replicate all 98 color vars with the full alias chain. Define the ~30–40 tokens the wireframe actually uses, as final values: surfaces (`--surface-dark:#222429`, `--surface-elevated:#2B2C33`, `--surface-deep:#111214`), accent (`--accent:#CA1D00`, `--accent-hover:#9E1300`, `--accent-light:#EB3213`), focus (`--focus:#2BBAD6`), text (`--text-primary:#fff`, `--text-secondary:rgba(255,255,255,.48)`, `--text-tertiary:rgba(255,255,255,.24)`), borders, error. Keep the *names* semantic so intent stays readable; skip the primitive layer.
- **Desktop mode values only.** Take the `Desktop` column from `variables - numbers` (type sizes, line-heights, spacing, radius, layout) as single fixed values. **No media queries, no Desktop HD / mobile modes.** `content-max-width` = 1200. Buttons use the pill radius.
- Full extract (all tiers/modes) stays in `figma-tokens-reference.md` for the eventual production build — the wireframe just doesn't need it.

Layout tokens still apply as fixed desktop values: `content-max-width` 1200, `navbar-height`, `section-padding-v`, `grid-gap`, `grid-margins` → `.container`, topbar, section rhythm bind to these, not magic numbers.

---

## 3. Tech & conventions

- **Static HTML/CSS/JS.** No framework, no bundler, no build step — same as HES. Opens via `file://` or any static server.
- **Font:** "Google Sans" (from the `typeface` token), loaded from the Google Fonts API: `https://fonts.googleapis.com/css2?family=Google+Sans:wght@400;500;700&display=swap`. Stack: `"Google Sans", system-ui, sans-serif`.
- **One stylesheet load order on every page:** `tokens.css → typography.css → components.css → layout.css`, then an optional page-scoped `<style>` block for page-specific layout (HES does exactly this — global system in the 4 files, page-unique grid/spacing inline).
- **Desktop-only, fixed values.** Single flat token set (Desktop values); no media queries, no mobile drawer. Pages still consume `var(--…)` so nothing hardcodes a color/size, but there's only one set to resolve.
- **Icons: Lucide. No emojis — ever.** Use [Lucide](https://lucide.dev) for all iconography (stat icons, feature bullets, nav affordances, the circular-arrow CTA motif, social, etc.). Simplest for a static prototype: the Lucide CDN UMD script + `<i data-lucide="name"></i>` placeholders, initialized once in `prototype.js` via `lucide.createIcons()`. Icons inherit `currentColor`, so color them with the accent/text tokens. **No emoji characters anywhere in the markup or copy.**
- **Naming:** kebab-case files; BEM-ish component classes (`.nav-more-item--placeholder`); utility classes for layout (`.grid-3`, `.flex`, `.gap-3`, `.mt-6`).

---

## 4. Architecture

### 4.1 File / folder structure

**Location:** the project root contains both `docs/` (these plan files + the IA) and `wireframe/` (the build target). Claude Code works inside `wireframe/`, but the IA and plan docs it must read live in the sibling `../docs/` — grant it read access to `../docs/` (or copy the three plan files + `vecto-master-ia-revised.html` into `wireframe/docs-ref/` at the start). All paths below are relative to `wireframe/`.

```
wireframe/
  index.html                         FULL  Homepage  (/)
  tokens.css                         design tokens (Figma-sourced)
  typography.css                     type scale / font faces
  components.css                     buttons, cards, badges, nav, megamenu, footer, forms, accordion, chips, tables…
  layout.css                         containers, grids, spacing + utilities
  prototype.js                       prototype-only interactions
  _nav.html                          shared primary nav + 3 megamenus + 2 dropdowns + CTA  (paste source)
  _footer.html                       shared 5-col footer + utility row  (paste source)
  _skeleton.html                     design-system QA page (every component once)

  services/
    index.html                       FULL  Services hub  (/services)
    ai-transformation.html           FULL  (/services/ai-transformation)
    software-development.html        FULL  (/services/software-development)
    product-design.html              FULL  (/services/product-design)
    marketing.html                   FULL  (/services/marketing)
    it-consulting.html               FULL  (/services/it-consulting)
    support-maintenance.html         FULL  (/services/support-maintenance)
    outsourcing-outstaffing.html     FULL  (/services/outsourcing-outstaffing)
    web-development.html             TEMPLATE example → sub-service page template

  who-we-serve/
    index.html                       FULL  Who We Serve hub  (/who-we-serve)
    early-stage-startup.html         TEMPLATE example → company stage page template

  industries/
    index.html                       FULL  Industries hub  (/industries)
    healthcare.html                  TEMPLATE example → industry page template

  our-work/
    index.html                       FULL  Portfolio  (/our-work)
    fintech-platform.html            TEMPLATE example → case study page template

  how-we-work/
    index.html                       FULL  How We Work hub  (/how-we-work)
    process.html                     FULL  (/how-we-work/process)
    engagement-models.html           FULL  (/how-we-work/engagement-models)
    technologies/
      index.html                     FULL  Technologies hub
      react.html                     TEMPLATE example → technology page template
    methodologies/
      index.html                     FULL  Methodologies hub
      ci-cd.html                     TEMPLATE example → methodology page template
    tools/
      index.html                     FULL  Tools hub
      jira.html                      TEMPLATE example → tool page template

  get-an-estimate.html               FULL  Project Estimator  (/get-an-estimate)
  schedule-a-call.html               FULL  Schedule a Call  (/schedule-a-call)

  blog/
    index.html                       FULL  Resources / Blog hub  (/blog)
    building-ai-that-ships.html      TEMPLATE example → blog post template
    authors/
      jane-doe.html                  TEMPLATE example → author page template

  glossary/
    index.html                       (light A–Z index — supports the term template)
    mvp.html                         TEMPLATE example → glossary entry template

  about/
    index.html                       FULL  About  (/about)
    security-compliance.html         FULL  (/about/security-compliance)

  contact.html                       FULL  Contact  (/contact)

  legal/
    privacy.html                     MENTION stub
    terms.html                       MENTION stub
    cookies.html                     MENTION stub
    sitemap.html                     MENTION stub (HTML sitemap of the wireframe)
  404.html                           MENTION stub (branded, search + top links)
```

**Not built this session (deferred per kickoff — handled later if a template needs special treatment):** the remaining 45 sub-service pages, 4 other stage pages, 12 other industry pages, additional case studies, 32 other technology pages, other methodology/tool pages, country (Service Areas) pages, year pages, and the deferred *Why VECTO* page. Each is covered by a template that this session builds one working example of.

### 4.2 CSS layering (what goes where)

| File | Contents |
|---|---|
| `tokens.css` | Custom properties only — **one flat `:root`, desktop values, no modes**. ~30–40 resolved semantic colors (surface/accent/focus/text/border/error), the Desktop type sizes & line-heights, the `spacing/base` scale, radius scale (incl. pill), and layout tokens. Full reference values in `figma-tokens-reference.md`; flatten per §2. |
| `typography.css` | Font stack `"Google Sans", system-ui, sans-serif` (loaded from Google Fonts API), type-scale utility classes mirroring the Figma names: `.t-h1`…`.t-h6`, `.t-p1`…`.t-p3`, `.t-c1`…`.t-c4`, plus button/input text styles. Fixed desktop sizes. |
| `components.css` | Every reusable component (see §5). Atomic ones bind to the semantic color tokens; molecules built from spec **as editorial layouts (§4a), not card grids**. Pill radius on buttons. |
| `layout.css` | `.container` (max-width = `--content-max-width` = 1200, fixed), `.container-narrow`, `.section` (padding = `--section-padding-v`), editorial layout helpers (split rows, full-bleed bands, rails — §4a), spacing utilities keyed to the `spacing/base` scale (`min`→`4xl`). Desktop only. |

### 4.3 Partials & path-depth rules

`_nav.html` and `_footer.html` are the **single source of truth**; their markup is pasted into every page (no server-side includes). Because links are relative, the `../` prefix depth differs by folder. Document this at the top of `_nav.html` exactly like HES does:

| Page location | Depth | Prefix to assets & root pages | Example |
|---|---|---|---|
| `wireframe/` root | 0 | none | `href="services/index.html"`, `href="tokens.css"` |
| `wireframe/services/` etc. | 1 | `../` | `href="../tokens.css"`, `href="../about/index.html"` |
| `wireframe/how-we-work/technologies/` etc. | 2 | `../../` | `href="../../tokens.css"`, `href="../../contact.html"` |

> **Recommended alternative to reduce error:** serve the wireframe with any static server and use **root-relative paths** (`/services/index.html`, `/tokens.css`). This removes the per-depth prefix bookkeeping entirely. Pick one convention and apply it everywhere. Default to HES-style relative paths if the wireframe must open directly via `file://`.

### 4.4 How template-class links resolve

For each repeating page class, this session builds **one** real example. To keep every click landing on a real page:

- Hub grids/cards for a class (e.g. all 13 industry tiles, all sub-service cards, all tech cards) link to the **single built example** for that class.
- Optionally mark non-built tiles with a subtle "Soon" affordance (HES's `.nav-soon` pattern) — but linking them all to the working example is preferred so flows stay walkable.
- The built example carries a small banner/comment noting it represents the template for its class.

---

## 4a. Layout principles — editorial, not grid-of-cards

This is the strongest design directive for the build. We are prototyping a **premium agency site**, not a B2B/SaaS dashboard. Repetitive uniform N-column card grids are the hallmark of low-effort "AI slop" and must be avoided — even at wireframe stage, lean into wide, editorial, art-directed composition. Stakeholders are judging IA, block/CTA placement, and copy by *playing with* the prototype, so the layouts need to feel considered.

**Effort tiers by IA depth — spend the editorial budget where it counts.** The deeper into the IA tree, the more utilitarian and informative the page, and the harder (and less necessary) it is to stay fully editorial. That's fine. Allocate effort accordingly:

- **Tier 1 — paramount (maximum editorial effort):** the **Homepage** and the **main hub / full pages** (Services hub, the 7 service category pages, AI Transformation, Who We Serve hub, Our Work, How We Work hub, Process, Engagement Models, About). These carry the premium impression and the conversion narrative — no default card grids here; art-direct every section.
- **Tier 2 — balanced:** template *examples* (case study, sub-service, industry, company stage) and conversion pages (Estimator, Schedule, Contact). Editorial where it adds value; a tasteful grid is acceptable for genuinely list-like content.
- **Tier 3 — utilitarian, grids OK:** deep **reference/index pages** — `how-we-work/technologies` (33), Methodologies, Tools, Glossary, and the per-tech/-tool/-method template pages. These are informative indexes; clean categorized grids or index lists are appropriate and expected. Don't force editorial gymnastics here — just keep them on-brand (tokens, type, spacing) and uncluttered.

**Do:**
- **Vary section rhythm** — no two consecutive sections share the same structure. Alternate full-bleed bands, asymmetric splits, and centered editorial passages.
- **Image-led splits** — 50/50 and 60/40 text↔visual rows (alternating sides), à la the sample page's "A Ready-Made Solution" / "About VECTO" sections.
- **Full-bleed feature bands** with oversized type and generous whitespace (use the H1/H2 scale; let headlines breathe).
- **Editorial treatments of collections** instead of equal-weight card grids: a lead/featured item + smaller supporting items (asymmetric), horizontal **rails/scrollers**, large **numbered or lettered lists**, or an **index/directory** layout. One hero item carrying more weight beats twelve identical tiles.
- **Wide stat bands** (figure + label inline across the width), not stat cards in a row.
- **Anchored long-form** for reference/template pages (sidebar contents + flowing body) rather than tiling everything.

**Don't:**
- Default any section to a 3- or 4-column grid of identical cards. If a grid is truly the right call (e.g. a portfolio index), make it deliberately asymmetric / masonry / varied-size, not uniform.
- Treat the sample marketing page (`8018:3317`) as a *layout* blueprint — it leans card-grid-heavy. Use it for **visual language only** (dark surfaces, red, pill CTAs, circular-arrow icon, type feel). Deliberately compose **more editorially** than it does.

**Reframing the IA's implied grids:**
| IA element | Avoid | Editorial treatment |
|---|---|---|
| Services 6-stage (home, hub) | 6 equal cards | Horizontal **journey/timeline** (Discover→…→Maintain) with the AI band as a distinct full-width moment; Build visually heaviest. |
| Industries ×13 | 13-cell uniform grid | Editorial **index/list** or wide rail with a couple of featured verticals enlarged. |
| Technologies ×33 / Methodologies / Tools | dense card grids | Categorized **index lists** (Frontend/Backend/Infra as labeled columns of links), not 33 tiles. |
| Sub-service / benefit cards | row of identical cards | Alternating splits or a lead-item + list. |
| Portfolio | flat card grid | Outcome-grouped sections with varied card sizes; one featured case per group enlarged. |
| Team (About) | avatar grid | Leadership as editorial rows (photo + bio split); specialists as a lighter index. |

`layout.css` should provide reusable editorial primitives — `.split` (with `.split--reverse`), `.band` (full-bleed), `.rail` (horizontal scroller), `.feature-lead` (asymmetric lead+supporting), `.stat-band`, `.index-list` — so pages compose from these rather than reaching for a card grid by default.

---

## 5. Design-system / component inventory

Two buckets. **(A) Exists in Figma — match it.** Build to the Figma component's real variants/states/tokens (screenshot it during build to verify). **(B) Build from spec** — marketing molecules not in the Figma library; compose from atomic components + tokens + the sample-page visual language (node `8018:3317`).

**(A) Atomic components present in Figma — match variants/states + bind to semantic tokens:**

| Component | Figma variants / states | Notes |
|---|---|---|
| **Button** | sizes huge/large/medium/small × main/accent/secondary-light/secondary-dark/ghost/text × default/hover/disabled | **Pill** radius (256). Bind to `button/*` tokens. Plus **circular icon-button** companion (the arrow-in-circle paired with pill CTAs). |
| **Input** | text/label(lg,sm)/placeholder/helper/error; border default/active/readonly/error; bg default/active | Bind to `input/*` tokens. |
| **Tag / chip** | primary/secondary × default/hover | `tag/*` tokens. |
| **Breadcrumb** | lightbg/darkbg × default/hover | `breadcrumbs/*` tokens. |
| **Card** | card-small, card-list-v1/v2, card-with-image | `surface/dark-elevated` base; used for features, portfolio, blog, reference. |
| **Tabs** | horizontal tabs | for in-page section nav where it fits. |
| **Global nav / menu link** | dashboard global nav, global menu link | reference for the topbar styling; the marketing megamenu is built from spec. |
| **Calendar, tables, icon sets** | present | calendar → Schedule page; tables → comparison tables; icons → throughout. |

HES patterns still reused where Figma has no equivalent: `.section-label`, `callout`, `divider`, utility classes.

**(B) Marketing molecules to build from spec (styled with tokens + sample-page language):**

| Component | Used on | Notes |
|---|---|---|
| **Megamenu — Services** | nav | 6 transformation-stage columns + a visually distinct cross-cutting **AI Transformation** band; bottom strip links to full-service + Estimator. |
| **Megamenu — Who We Serve** | nav | 2-axis panel: company stage column + industry column; strip → all case studies. |
| **Megamenu — How We Work** | nav | 3 columns: Process (5 steps) · Engagement Models (4) · Reference (Technologies/Methodologies/Tools); strip → Estimator. |
| **Dropdown — Resources / About** | nav | simple multi-column dropdowns (lighter than megamenu). |
| **Primary CTA button** | nav (persists on mobile), page CTAs | accent/yellow filled, high contrast on dark nav. |
| **Sticky Estimator CTA** | service/industry/sub-service/case-study pages | floating, shows/hides on scroll. |
| **Breadcrumb** | sub-service, deep template pages | `Home › Services › Parent › This`. |
| **Service stage card** | home, services hub | stage name + mapped category + sub-service list + "Learn more". |
| **Sub-service / benefit / reference card** | many | card variants for sub-service cards, outcome benefit cards, tech/method/tool reference cards. |
| **Industry tile** | home, industries hub, who-we-serve | icon + name + one-liner. |
| **Stat / trust strip** | home, about, hubs | client logos + numeric proof + review-platform badges. |
| **Portfolio / case-study card** | our-work, related modules | thumbnail + client + industry tag + service tag. |
| **Filter chip strip** | our-work | sticky; client-side filtering of demo cards (JS). |
| **Blog card** | home, blog hub | thumb + date + title + excerpt + read link. |
| **Process step strip / interactive diagram** | home, how-we-work, process, mini-process on service pages | 5-step (Kickoff→Scoping→Execute→Launch→Iterate); expandable on the Process page. |
| **Engagement decision tree** | engagement-models | interactive Q&A → recommended model (JS). |
| **Comparison table** | engagement-models, outsourcing | 4-model side-by-side; 2-model for outsourcing. |
| **Estimator widget (stub)** | get-an-estimate, home mini-version | conversational input → output card placeholder (cost range/timeline/model). Not a real model — a wired-looking stub. |
| **Booking widget (placeholder)** | schedule-a-call | calendar-style placeholder + "who you'll meet". |
| **Specialist card** | service pages | photo placeholder + name + role + "Email me"/"Book 15 min". |
| **Stage/anchor nav strip** | services hub, process | sticky in-page anchor nav. |

---

## 6. Navigation spec

**Primary nav (7 slots), left→right:** Services ▾ · Who We Serve ▾ · Our Work · How We Work ▾ · Resources ▾ · About ▾ · **Get an Estimate** (CTA button).
(IA changes baked in: How We Work is top-level; Technologies relocated under it; "Quote" replaced by the Estimate CTA.)

- **Our Work** is a direct link (no dropdown).
- **3 megamenus:** Services, Who We Serve, How We Work (see §5 for panel contents — full content in IA §`mm-services`, `mm-who`, `mm-howwework`).
- **2 dropdowns:** Resources (Blog/Glossary/Estimator), About (company/team/trust columns).
- **Desktop-only** — no hamburger/mobile drawer. The topbar + megamenus are built for the desktop viewport only.

**Footer — 5 columns + utility row** (IA §`mm-footer`):
1. Services (7 categories + "All services")
2. Industries & Stage (13 industries + 5 stages)
3. Service Areas (country pages — SEO surface)
4. Resources (Blog · Glossary · Estimator · Engagement Models · Process · Technologies · Methodologies · Tools · Year pages)
5. Company (About · Team · Careers · Security & Compliance · Partners · Press · Contact)
Utility row: Logo · Privacy · Terms · Cookies · Sitemap · Social · Copyright.

In the wireframe, footer links to not-built pages point to their class's built example or a stub (legal pages get real stubs).

---

## 7. Page inventory

**24 FULL pages** (full description + rationale + block-by-block in the IA):

Homepage · Services hub · AI Transformation · Software Development · Product Design · Marketing · IT Consulting · Support & Maintenance · Outsourcing & Outstaffing · Who We Serve hub · Industries hub · Our Work/Portfolio · How We Work hub · Process · Engagement Models · Technologies hub · Methodologies hub · Tools hub · Project Estimator · Schedule a Call · Resources/Blog hub · About · Security & Compliance · Contact.

**10 TEMPLATES** (build one representative example each):

Sub-service (`web-development`) · Company stage (`early-stage-startup`) · Industry (`healthcare`) · Case study (`fintech-platform`) · Technology (`react`) · Methodology (`ci-cd`) · Tool (`jira`) · Blog post (`building-ai-that-ships`) · Author (`jane-doe`) · Glossary entry (`mvp`).

**MENTION stubs:** Privacy · Terms · Cookies · Sitemap · 404. (Country pages, Year pages, Why VECTO — deferred.)

---

## 8. Per-page build specs

For each page below: the **file**, the **IA section** that holds its canonical block list (use it verbatim for blocks & copy), and **build notes** specific to the wireframe (components, links, JS). The IA already gives hero headlines and FAQ text — reuse them.

### Full pages

- **Homepage** — `index.html` — IA §`branch-home` (17 blocks). Components: trust strip, service stage grid (6), AI positioning band, benefits, industries grid (13), who-we-serve chip strip, outcome-grouped portfolio module, reviews, process strip, engagement strip, estimator mini-stub, blog teaser (3), FAQ accordion, tri-CTA contact. Section order mirrors the nav narrative.
- **Services hub** — `services/index.html` — IA §`branch-services` (12 blocks). Sticky stage anchor strip; 6 stage cards (Build largest) + distinct AI Transformation section; engagement snapshot; featured cases; FAQ; dual CTA.
- **AI Transformation** — `services/ai-transformation.html` — IA §`branch-services` (AI Transformation, 11 blocks). Level-headed tone; 5 sub-service cards; 3 benefits; mini-process (Audit→Pilot→Integrate→Operate); tech stack; cases; FAQ (5); specialist card; sticky CTA.
- **Software Development** — `services/software-development.html` — IA (11 blocks). 11 sub-service cards in 3 groupings; elevated process detail; full 33-tech stack; specialist; sticky CTA.
- **Product Design** — `services/product-design.html` — IA (11 blocks). 6 sub-services research→validation→execution.
- **Marketing** — `services/marketing.html` — IA (11 blocks). 11 sub-services in 3 pillars.
- **IT Consulting** — `services/it-consulting.html` — IA (11 blocks). 7 sub-services idea→spec.
- **Support & Maintenance** — `services/support-maintenance.html` — IA (11 blocks). 4 sub-services; two-buyer hero.
- **Outsourcing & Outstaffing** — `services/outsourcing-outstaffing.html` — IA (11 blocks). 2 sub-services + comparison table.
- **Who We Serve hub** — `who-we-serve/index.html` — IA §`branch-whoweserve` (7 blocks). 5 stage cards + 13 industry grid + cross-cutting cases.
- **Industries hub** — `industries/index.html` — IA §`branch-industries` (5 blocks). Search field + 13 tiles. Lighter treatment.
- **Our Work / Portfolio** — `our-work/index.html` — IA §`branch-ourwork` (7 blocks). Sticky filter strip (JS) + 4 outcome groups + full project grid + live count + sticky CTA.
- **How We Work hub** — `how-we-work/index.html` — IA §`branch-howwework` (6 blocks). Process snapshot + engagement snapshot + 3 reference-hub cards + FAQ.
- **Process** — `how-we-work/process.html` — IA (12 blocks). Large interactive 5-step diagram (expandable, JS); per-stage anatomy; "Sample first 30 days"; cadence; tools.
- **Engagement Models** — `how-we-work/engagement-models.html` — IA (9 blocks). Interactive decision tree (JS) → 4 model sections → comparison table.
- **Technologies hub** — `how-we-work/technologies/index.html` — IA §`branch-tech` (7 blocks). 3 grids (Frontend 10 / Backend 13 / Infra 10). Note the URL-migration callout (doc only; wireframe uses new paths).
- **Methodologies hub** — `how-we-work/methodologies/index.html` — IA §`branch-methodologies` (7 blocks). 3 card grids (Delivery/Engineering/Quality).
- **Tools hub** — `how-we-work/tools/index.html` — IA §`branch-tools` (7 blocks). 3 card grids (Collaboration/Dev/AI).
- **Project Estimator** — `get-an-estimate.html` — IA §`p-estimator` (8 blocks). Estimator widget stub → output card → comparable cases → cross-link to Engagement Models → save/share → Schedule CTA.
- **Schedule a Call** — `schedule-a-call.html` — IA §`p-schedule` (6 blocks). Booking widget placeholder + who-you'll-meet + expectations.
- **Resources / Blog hub** — `blog/index.html` — IA §`branch-resources` (8 blocks). Featured posts + categories + recent grid (filterable) + author spotlight + glossary/tools entry cards + newsletter.
- **About** — `about/index.html` — IA §`branch-about` (9 blocks). History, Mission/Vision, Team grids (named), Partners, trust signals, Careers callout, Security link, dual CTA.
- **Security & Compliance** — `about/security-compliance.html` — IA (8 blocks). Certifications, NDA/IP, data handling, secure dev, compliance experience, review process, security contact.
- **Contact** — `contact.html` — IA §`p-contact` (7 blocks). 3 intent paths (Estimate / Schedule / Send-a-question form) + locations + direct contacts + procurement cross-link.

### Templates (one representative example each)

- **Sub-service** — `services/web-development.html` — IA §`branch-services` sub-service template (13 blocks). Breadcrumb + sticky Estimator CTA. All sub-service cards across the site link here.
- **Company stage** — `who-we-serve/early-stage-startup.html` — IA company-stage template (10 blocks).
- **Industry** — `industries/healthcare.html` — IA industry template (9 blocks). Includes the compliance block.
- **Case study** — `our-work/fintech-platform.html` — IA case-study template (11 blocks). The conversion-critical template.
- **Technology** — `how-we-work/technologies/react.html` — IA technology template (8 blocks).
- **Methodology** — `how-we-work/methodologies/ci-cd.html` — IA methodology template (8 blocks).
- **Tool** — `how-we-work/tools/jira.html` — IA tool template (6 blocks).
- **Blog post** — `blog/building-ai-that-ships.html` — IA blog-post template (mention). Byline links to author page.
- **Author** — `blog/authors/jane-doe.html` — IA author template (mention).
- **Glossary entry** — `glossary/mvp.html` — IA glossary template (mention).

### Mention stubs

`legal/privacy.html`, `legal/terms.html`, `legal/cookies.html`, `legal/sitemap.html`, `404.html` — real pages with nav + footer + a heading + one paragraph of placeholder, so footer/utility links resolve. Sitemap lists the wireframe's built pages. 404 is branded with search + top entry links.

---

## 9. Placeholder copy guidelines

- **Voice:** plain-English, non-technical-founder-first. No jargon in headlines or CTAs. Outcome-led ("Turn your idea into a product your users love"), not capability-led.
- **Reuse the IA verbatim** wherever it gives copy: hero headlines, sub-headlines, the AI positioning band body, FAQ questions, CTA labels. The IA is rich with these.
- **Mine the IA's prose for everything else.** Each full page in the IA has a *Description* and *Design rationale* paragraph and per-block descriptions — and some blocks include explicit copy suggestions. Use that context to write **believable, specific placeholder copy** for non-template (full) pages: the IA tells you what each block is *about* and who it's for, so the placeholder should reflect that intent (e.g. a block described as "two-buyer hero (post-launch founders + inheritors of legacy systems)" gets copy that actually speaks to both), not generic filler. This is the difference between a prototype stakeholders can react to and one they can't.
- **Never lorem ipsum.** Mirror HES's habit of writing *actual* sentences. Template-example pages can be lighter; full/hub pages should read like real (if placeholder) site copy.
- **Two engagement-axis vocabularies must never blur:** the 6 service **stages** (Discover/Design/Build/Grow/Scale/Maintain) vs. the 5-step **engagement process** (Kickoff/Scoping/Execute/Launch/Iterate). Keep each in its own surface.
- **Names/photos/logos/metrics** are placeholders (e.g. "Clutch", "[Client]", greyed image blocks, "NPS 72"). Use neutral image placeholder blocks like HES's `.blog-thumb` / `.book-cover`.

---

## 10. Open dependencies & handoff notes

1. **Figma tokens — DONE (inspected & enumerated).** Full extract in `figma-tokens-reference.md`. Two collections: `variables - style` (98, single mode, two-tier color) and `variables - numbers` (69, 3 responsive modes). `tokens.css`/`typography.css` build directly from that extract. **Google Sans is on the Google Fonts API** (confirmed) — load it directly, no fallback brand font needed. No open blockers.
2. **Figma covers atomic components only.** Marketing molecules (megamenu, hero, portfolio grid, process strip, decision tree, estimator stub) are not in the Figma library and are built from spec, styled with tokens + the sample-page visual language. No blocker — just sets expectations on what "match Figma" means per component (§5).
3. **Template special-casing** is explicitly deferred to a later session (your call). This session ships one working example per template.
4. **URL migration** for Technologies (`/technologies/*` → `/how-we-work/technologies/*`) is a production SEO concern noted in the IA; the wireframe simply uses the new paths.
5. **Deferred pages** (Why VECTO, country, year, and all non-representative template instances) are out of scope this session.

> **Reference frame node IDs** (file `emDaz5ZTNMna0jK1al4G9z`): styles & components `317:12497` · Typography `2010:295` · Buttons `2009:146` · Input `2028:417` · Semantic Color Reference `10039:4192` · navigation `6006:31816` · sample marketing page (visual ref only) `8018:3317`. Claude Code can screenshot any of these to verify a component during build.
