> **⚠️ LEGACY — archived 2026-06-30.** This document belongs to the previous VECTO design-system effort (the custom red/dark Figma system). VECTO is now being rebuilt in React on a shadcn **Luma** baseline. Kept for historical reference only — not a current source of truth.

---

# VECTO Figma — Token Reference (enumerated)

**Source:** `figma.com/design/emDaz5ZTNMna0jK1al4G9z` ("VECTO universal style — TEST"), styles & components page (node `317:12497`).
**Method:** full Plugin-API enumeration — `getLocalVariableCollectionsAsync` + `getLocalVariablesAsync`, `valuesByMode` across all modes, aliases resolved. (Not `get_variable_defs`, which is node-scoped/single-mode.)
**Use:** this is the authoritative token extract for `tokens.css` / `typography.css`. Claude Code should still re-enumerate live at build time (values may change), but this captures the structure and current values.

> ⚠️ This supersedes the earlier placeholder assumption (`#1a1a18` nav + `#f0c040` yellow). The real brand is **red**, the theme is **dark**, buttons are **pill**, and the font is **Google Sans**.

> 🛠️ **Wireframe scope:** this file documents the FULL production token system (two-tier, 3 responsive modes) for completeness and the future production build. The desktop-only clickable **wireframe deliberately flattens it** to a single `:root` of resolved **Desktop-mode** values — no base→semantic aliasing, no mobile/Desktop-HD modes, no media queries. Use the **Desktop** column and the resolved colors below; ignore the mode machinery for the wireframe. See build-plan §2.

---

## Collections & mode architecture (critical)

| Collection | Vars | Modes | Maps to CSS as |
|---|---|---|---|
| `variables - style` | 98 | **single** ("Mode 1") | one `:root` block. Two tiers: base (primitive) + semantic (aliased). **No theme switching.** |
| `variables - numbers` | 69 | **3: Desktop / Desktop HD / mobile** | custom properties **redefined per breakpoint via media queries**. NOT a `[data-theme]` switch — these are responsive sizes. |

**Breakpoint mapping (recommended):**
- `mobile` → base (`:root`, mobile-first) OR `@media (max-width: 600px)` depending on chosen strategy
- `Desktop` → `@media (min-width: 601px)` (the primary desktop values; `content-max-width` 1200)
- `Desktop HD` → `@media (min-width: 1521px)` (`content-max-width` 1520)

So the numeric tokens (type sizes, line-heights, spacing, radius, layout) each have **three values**. Implement as CSS custom properties overridden at two breakpoints, then consume everywhere via `var(--…)`. (Alternative: `clamp()` per token — but explicit breakpoints match the Figma modes exactly.)

---

## Typeface

- `typeface` = **"Google Sans"** (STRING variable).
- **Available on the Google Fonts API** (confirmed live). Load it directly:
  `<link href="https://fonts.googleapis.com/css2?family=Google+Sans:wght@400;500;700&display=swap" rel="stylesheet">`
  Weights 400 and 700 confirmed resolving; include 500 for medium (confirm at build). Stack: `font-family: "Google Sans", system-ui, sans-serif;` — system fallback only, no substitute brand font needed.

---

## Color — base (primitives), single mode

```
brand/primary-1   #9E1300   (deep red — hover/darker)
brand/primary-2   #CA1D00   (core brand red)
brand/primary-3   #EB3213   (bright red/orange — accent-light)
brand/primary-alpha #CA1D00 @48%
brand/secondary-1 #2291A5   (teal-dark)
brand/secondary-2 #2BBAD6   (cyan — focus)
brand/secondary-3 #64C7D8   (cyan-light)
brand/secondary-alpha #2BBAD6 @56%

dark 1 #111214   dark 2 #222429   dark 3 #2B2C33   dark 4 #35363D
dark 5 #58595C   dark 6 #696B70   dark 7 #999BA3
light 1 #CBCDD4  light 2 #DCDDE0  light 3 #E6E7EB  light 4 #F2F3F7
pure white #FFFFFF
error #E06531

dark overlay 1 #000 @48%   dark overlay 2 #000 @24%   dark overlay 3 #000 @12%
dark overlay neutral #303138 @68%
light overlay 1 #FFF @48%  light overlay 2 #FFF @24%  light overlay 3 #FFF @12%
```

## Color — semantic (aliased → base)

```
surface/dark            → dark 2 (#222429)   ← primary page surface
surface/dark-elevated   → dark 3 (#2B2C33)   ← cards
surface/dark-deep       → dark 1 (#111214)
surface/secondary-dark  → dark 5
surface/muted           → dark 6
surface/popout          → dark 4
surface/light           → light 4
surface/secondary-light → light 3
surface/accent          → brand/primary-2 (#CA1D00)
surface/accent-light    → brand/primary-3 (#EB3213)

text-generic/primary          → pure white
text-generic/secondary        → light overlay 1 (#FFF @48%)
text-generic/tertiary         → light overlay 2 (#FFF @24%)
text-generic/accented-darker  → brand/primary-2
text-generic/accented-lighter → brand/primary-3
text-generic/primary-inverse  → dark 2
text-generic/secondary-inverse→ dark overlay 2
text-generic/error            → error

border/default      → dark 5      border/light → light 2
border/brand-accent → primary-2   border/focus → secondary-2
border/focus-muted  → secondary-alpha
border/semi-transparent-light → #E0DEDF @16%

button/main-default → primary-2     button/main-hover → primary-1
button/accent-default → surface/accent    button/accent-hover → surface/accent-light
button/secondary-light-default → light 4  …-hover → light 2
button/secondary-dark-default → dark 1    …-hover → dark 2
button/ghost-default → #FFF @0%           ghost-hover → light overlay 3
button/disabled → dark 2
button/text-on-brand → text/primary   button/text-accent → text/accented-darker   button/btn-text-disabled → text/tertiary

input/input-bg-default → overlay/dark-3   input-bg-active → overlay/dark-2
input/input-border-default → border/default   …-active → border/focus-muted   …-readonly → border/semi-transparent-light   …-error → border/brand-accent
input/input-text-default → text/primary   …-readonly → text/tertiary   input-placeholder → text/tertiary
input/input-label-default → dark 7   …-readonly → dark 5
input/input-helper → text/secondary   input-error → text/error
input/input-icon-default → primary-2   …-readonly → dark 7

tag/primary-default → surface/dark    …-hover → dark 1
tag/secondary-default → surface/secondary-dark   …-hover → dark 6
breadcrumbs/lightbg-default → #FFF @0%   …-hover → button/secondary-light-hover
breadcrumbs/darkbg-default → #000 @0%    …-hover → dark overlay 2
overlay/modal → dark overlay 2
overlay/{dark,light}-{1,2,3}, overlay/neutral → corresponding base overlays
```

**tokens.css structure:** emit base colors as primitives (`--base-brand-primary-2: #CA1D00;`), then semantic as references (`--surface-dark: var(--base-dark-2);`). Mirror the two-tier aliasing — don't flatten.

---

## Type scale — `text-size` & `line-height` (px; Desktop / Desktop HD / mobile)

| Token | size D / HD / M | line-height D / HD / M |
|---|---|---|
| h1 | 56 / 72 / 36 | 64 / 80 / 40 |
| h2 | 48 / 60 / 32 | 56 / 68 / 36 |
| h3 | *(exists; re-read live — was truncated)* | *(exists)* |
| h4 | 28 / 32 / 22 | 32 / 40 / 28 |
| h5 | 22 / 18 / 18 | 28 / 24 / 24 |
| h6 | 16 / 15 / 15 | 20 / 16 / 16 |
| p1 | 20 / 17 / 17 | 32 / 24 / 24 |
| p2 | 16 / 15 / 15 | 24 / 20 / 20 |
| p3 | 14 / 13 / 13 | 20 / 16 / 16 |
| c1 | 13 / 13 / 13 | 16 / 16 / 16 |
| c2 | 12 / 12 / 12 | 16 / 12 / 12 |
| c3 | 12 / 12 / 12 | 16 / 12 / 12 |
| c4 | 10 / 11 / 11 | 12 / 12 / 12 |
| button btn-huge | 24 / 20 / 20 | 32 / 24 / 24 |
| button btn-large | 18 / 16 / 16 | 24 / 20 / 20 |
| button btn-medium | 16 / 14 / 14 | 24 / 16 / 16 |
| button btn-small | 13 / 13 / 13 | 16 / 16 / 16 |
| input input-label | 14 / 13 / 13 | 16 / 16 / 16 |
| input input-text+placeholder | 20 / 18 / 18 | 24 / 20 / 20 |
| input input-helper | 14 / 13 / 13 | 16 / 14 / 14 |

Type-scale utility classes in `typography.css`: `.t-h1`…`.t-h6`, `.t-p1`…`.t-p3`, `.t-c1`…`.t-c4`, plus component text styles for buttons/inputs. Each consumes the responsive custom property.

---

## Spacing — `spacing/base` (px; Desktop / Desktop HD / mobile)

```
none 0 · min 4 · 4xs 8 · 3xs 12/10/10 · xxs 16/12/12 · xs 20/16/16 · s 24/20/20
m 32/24/24 · l 40/28/28 · xl 48/36/36 · xxl 64/44/44 · 3xl 72/88/52 · 4xl 96/112/64
special/negative-3xs (negative gap)
```

## Layout — `spacing/layout` (px; Desktop / Desktop HD / mobile)

```
content-max-width 1200 / 1520 / 540     ← .container max-width per breakpoint
navbar-height                           ← topbar height
section-padding-v                       ← vertical section padding
grid-gap                                ← grid column gap
grid-margins                            ← page side margins
form-inner-margin · skip-column
```

## Corner radius (px; same across modes unless noted)

```
none 0 · xxs 4 · xs 8 · s 12 · m 24 · l 32 · xl 48 · pill 256 (fully rounded)
```

Buttons & many CTAs use **pill (256)**. Cards likely use s/m — confirm per component during build.
