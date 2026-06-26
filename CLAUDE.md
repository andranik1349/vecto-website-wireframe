# VECTO Website Wireframe — Claude Code working rules

Auto-loaded every session. Read this first, then read the relevant section of the source docs before each task.

## What this is
A **desktop-only, static, clickable prototype** (no framework, no build step) to validate IA, block & CTA placement, and copy with stakeholders. Fidelity bar = the HES wireframe. NOT a production site.

## Source-of-truth docs (in the sibling `../docs/` folder — request read access if needed)
- **`vecto-master-ia-revised.html`** — canonical content & block structure for every page. The authority on *what* each page contains. Reuse its hero headlines, FAQ questions, and CTA labels verbatim; mine its per-block prose for believable placeholder copy elsewhere.
- **`wireframe-build-plan.md`** — architecture, file tree (§4.1), pathing (§4.3), layout principles (§4a), component inventory (§5), per-page specs (§8).
- **`figma-tokens-reference.md`** — the design tokens (use the **Desktop** column / resolved colors; the wireframe flattens the full system).
- **`claude-code-prompts.md`** — the ordered build prompts (run 0 → 19).

**Before each task, open the doc section it references and read it** — don't build from memory.

## Hard constraints (do not violate)
1. **Desktop-only.** No mobile, no responsive breakpoints, no hamburger drawer. Fixed ≈1200px content width.
2. **Tokens flattened.** One flat `:root` of resolved Desktop-mode values (no two-tier aliasing, no modes, no media queries). Nothing hardcodes a color/size — always `var(--…)`.
3. **Editorial layouts, tiered by depth (build-plan §4a):**
   - Tier 1 (Homepage + main hub/full pages): strongly editorial — NO default card grids. Use splits, full-bleed bands, rails, lead+supporting, stat bands. Vary section rhythm.
   - Tier 3 (deep utilitarian reference/index pages: technologies/methodologies/tools, glossary, deep templates): clean categorized grids/index lists are fine — keep on-brand, don't force editorial gymnastics.
4. **Icons: Lucide only. NO emojis anywhere.**
5. **Copy: never lorem ipsum.** Verbatim from IA where given; otherwise believable, specific copy reflecting each block's IA intent.
6. **Visual system:** dark theme, red brand (`#CA1D00`), pill buttons, Google Sans (Google Fonts API). Use the sample Figma page (`8018:3317`) for visual *language* only, not layout.

## Architecture
- 4 CSS files loaded in order on every page: `tokens.css → typography.css → components.css → layout.css`.
- Shared `_nav.html` / `_footer.html` pasted into each page; adjust `../` path depth per folder (build-plan §4.3).
- One `prototype.js` (prototype-only) for menus, accordions, sticky CTA, filters, decision tree, estimator stub, Lucide init.
- Template classes: build one representative example each; link all siblings to it (build-plan §4.4).

## Page-building playbook (learned while building home + services)
- **Depth-1 partials:** `_nav.html`/`_footer.html` are written at depth 0. To paste into a sub-folder page, generate a prefixed copy — `perl -0pe 's{(href|src)="(?!#|https?://|mailto:|/|\.\./)}{$1="../}g'` — then extract just the `<header>`/`<footer>` element. Use `../../` for depth 2.
- **Nav contract (prototype.js `initMenus`):** hub triggers (Services / Who We Serve / How We Work / About) are `<a href>` that **navigate on click** and **reveal their panel on hover**; Resources is a `<button>` (no hub page) that toggles. Panels are DOM descendants of `<header>`, so close is driven by `<header>`'s `mouseleave` + a ~220ms grace delay — never per-trigger hover-close (it flickers). Active section is flagged from `location.pathname`.
- **Six-stage representation differs by page:** horizontal `.stage-journey` on the **homepage only**. On hubs the stages are **vertical anchored blocks** (alternating splits, Build = heaviest). A scroll-spy/anchor nav needs vertically-stacked, distinct targets — never put one over a one-row horizontal strip. Re-read the IA block-by-block per page; "same content" ≠ same layout.
- **Layout gotchas that bit us:** (a) never nest `<a>` inside `<a>` — e.g. an author link inside a card-link; make the card a `<div>` with separate links. (b) Match `.feature-lead` variant to child count: 1+2 = base, 1+3 = `--3up` (lead needs `align-self:stretch`). (c) Put button icons in the button's own slot, not as a separate circular icon-button.
- **Verify by DOM geometry** (`getBoundingClientRect` via preview_eval), not screenshots — the preview reliably captures only the top of the page, and caches CSS/JS hard (cache-bust `<link>`/`<script>` with `?v=…` to re-test). See memory `preview-tooling-quirks`.
- **Git rhythm:** commit only when asked, push only when asked — they are separate instructions.

## Figma (file `emDaz5ZTNMna0jK1al4G9z`)
Re-enumerate tokens via full Plugin API when needed (not `get_variable_defs`). Screenshot component nodes (IDs in build-plan §10) to match atomic components.
