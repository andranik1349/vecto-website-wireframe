# VECTO Website — Clickable Wireframe

Desktop-only static clickable prototype. Validates IA, block/CTA placement, and copy with stakeholders. Not a production site — no framework, no build step, opens via `file://` or any static server.

---

## Stylesheet load order

Every page loads these four files in this exact order, then an optional page-scoped `<style>` block for page-unique layout:

```html
<link rel="stylesheet" href="tokens.css">
<link rel="stylesheet" href="typography.css">
<link rel="stylesheet" href="components.css">
<link rel="stylesheet" href="layout.css">
```

| File | Contents |
|---|---|
| `tokens.css` | One flat `:root` of resolved Desktop-mode values — ~30–40 semantic color, type, spacing, radius, and layout tokens. No media queries, no modes. |
| `typography.css` | Google Sans font stack, type-scale utility classes `.t-h1`…`.t-h6`, `.t-p1`…`.t-p3`, `.t-c1`…`.t-c4`, button/input text styles. |
| `components.css` | Every reusable UI component: buttons (pill radius), cards, nav, megamenus, footer, forms, accordion, chips, tables, etc. |
| `layout.css` | `.container` (max-width 1200px), `.section`, editorial layout primitives (`.split`, `.band`, `.rail`, `.feature-lead`, `.stat-band`, `.index-list`), spacing utilities. |

---

## Path-depth convention (build-plan §4.3)

Because pages are static HTML with relative paths, the `../` prefix depth varies by folder depth. Adjust when pasting `_nav.html` and `_footer.html` into a page:

| Page location | Depth | Prefix for assets & root pages | Example |
|---|---|---|---|
| `wireframe/` (root) | 0 | none | `href="tokens.css"` |
| `wireframe/services/` etc. | 1 | `../` | `href="../tokens.css"` |
| `wireframe/how-we-work/technologies/` etc. | 2 | `../../` | `href="../../tokens.css"` |

**Recommended alternative:** serve with any static server (`npx serve .` or similar) and use root-relative paths (`/tokens.css`, `/services/index.html`) to eliminate per-depth bookkeeping entirely.

---

## Partials

`_nav.html` and `_footer.html` are the single source of truth for navigation and footer markup. Paste them into each page — no server-side includes. Apply the correct path-depth prefix (above) when pasting.

`_skeleton.html` is a QA page that renders every component once in isolation.

---

## prototype.js

`prototype.js` is **prototype-only** — clearly marked "do not port to production." It drives megamenu open/close, accordions, sticky Estimator CTA, portfolio filter chips, the engagement decision tree, the estimator stub, and Lucide icon initialization (`lucide.createIcons()`).

---

## Desktop-only

This prototype targets a fixed desktop viewport (~1200–1440px). No mobile breakpoints, no hamburger drawer, no responsive media queries. `tokens.css` contains a single flat token set using Desktop-column values from the Figma file (`emDaz5ZTNMna0jK1al4G9z`).

---

## Icons

Lucide only — no emoji anywhere in markup or copy. Load via CDN UMD script; initialize with `lucide.createIcons()` in `prototype.js`.

---

## Source docs (sibling `../docs/` folder)

| File | Purpose |
|---|---|
| `vecto-master-ia-revised.html` | Canonical content & block structure for every page |
| `wireframe-build-plan.md` | Architecture, file tree, layout principles, component inventory, per-page specs |
| `figma-tokens-reference.md` | Full Figma token extract — authoritative values source for `tokens.css` / `typography.css` |
| `claude-code-prompts.md` | Ordered build prompts (run 0 → 19) |
