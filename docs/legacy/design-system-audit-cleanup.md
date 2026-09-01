> **⚠️ LEGACY — archived 2026-06-30.** This document belongs to the previous VECTO design-system effort (the custom red/dark Figma system). VECTO is now being rebuilt in React on a shadcn **Luma** baseline. Kept for historical reference only — not a current source of truth.

---

# VECTO Design System — Audit & Cleanup Checklist

_File: "VECTO universal style — TEST" (`emDaz5ZTNMna0jK1al4G9z`). Audited 2026-06-28 via full Plugin-API enumeration (all variables, all modes, all components — no sampling)._

This is an actionable checklist for you to execute in Figma. Items are grouped by priority. Each item notes **what**, **where**, and **why**. Nothing here changes visual design — it's hygiene that makes the system trustworthy and ready to extend.

---

## Snapshot of what's in the file

| Area | Count | Notes |
|------|-------|-------|
| Color variables (`variables - style`) | 98 | Single mode ("Mode 1"). Two-tier: 36 base primitives → ~62 semantic aliases + `typeface` string |
| Number variables (`variables - numbers`) | 69 | 3 modes: Desktop / Desktop HD / mobile. Type sizes, line-heights, spacing, layout, radii |
| Text styles | 50 | Heading/Paragraph/Caption ramps + Components/Buttons + Components/Input |
| Effect styles | 11 | Shadow ramp (dark/light × on-light/on-dark × small/large) + button effects |
| Paint styles | 2 | `translucent bg`, `gr 1` — leftovers |
| Component sets | ~30 | Buttons, full form/input family, navigation, chips, tables, card, logo |
| Standalone components | ~210 | Incl. ~200 icons (small + large) |
| Pages | 4 | `ui concept`, `+++ library` (empty), `styles & components`, `+++ UI` (empty) |

**Overall:** the foundation is stronger than "incomplete" implies. The token architecture is sound. Most issues are naming hygiene, scoping, and a handful of discipline breaks — not structural rebuilds.

---

## P0 — Junk & errors (remove/fix first, ~15 min)

- [ ] **Delete gibberish variant** `Property 1=ьгдешыудусе` in the `dropdown` component set. It's an accidental wrong-keyboard-layout name. Keep only the real `Default` variant (and rename its property — see P1).
- [ ] **Delete stray text node** `sdsd` on the `styles & components` page.
- [ ] **Rename `Frame 355`** (unnamed default frame on the page) to whatever it actually is, or delete if scratch.
- [ ] **Fix typo** `vecto-buletpoint` → `vecto-bulletpoint`.
- [ ] **Resolve duplicate `logout` icons** (two components named `icons small / logout`, IDs `8018:2593` and `8067:3925`). Keep one, delete the other, repoint instances.
- [ ] **Fix Cyrillic character** in `icons small / icons8-х-close` — the `х` is a Cyrillic letter. Rename to the new icon convention (see P1).

## P1 — Naming consistency (do before writing/finalizing conventions)

- [ ] **Standardize variant-state casing.** Pick one (recommend lowercase: `default`, `hover`, `selected`, `disabled`) and apply across every set. Today you have `Default`, `hover`, `default hover`, `selected hover` mixed.
- [ ] **Replace generic `Property 1`** variant-property names with semantic ones (`state`, `type`, etc.). Affects `dropdown` and `calendar` sets.
- [ ] **Apply consistent component namespacing.** Form parts use `input-blocks / …`; buttons, chips, pagination, tabs, breadcrumbs sit at the root. Adopt the functional-group prefixes from the conventions doc (e.g. `Actions / `, `Forms / `, `Navigation / `).
- [ ] **Retire version-suffix names** `card-list-v1` / `card-list-v2`. Use variant properties on one `Card` set instead of `-v1/-v2` clones.
- [ ] **Rename the icon library.** ~200 icons carry raw Icons8 export names (`icons8-arrow (2) 2`, trailing `1`/`2`). Move to semantic names (`Icons / arrow-right`, `Icons / calendar`, `Icons / user`). High-volume but high-value for searching and instance-swap. Can be staged.
- [ ] **Rename mode `Mode 1` → `Dark`** in the `variables - style` collection. Costs nothing now and signals theme-readiness (see conventions doc).

## P2 — Token discipline (scopes & two-tier integrity)

- [ ] **Tighten variable scopes.** Many tokens are `ALL_SCOPES`, which pollutes every picker. Apply intent-based scopes:
  - Spacing tokens → `GAP` (most already correct; fix `spacing/layout/*` which are `ALL_SCOPES`).
  - Corner radii → `CORNER_RADIUS` (fix `corner radius/pill`, currently `ALL_SCOPES`).
  - Layout sizes (`content-max-width`, `navbar-height`, `section-padding-v`) → `WIDTH_HEIGHT` / `GAP` as appropriate.
  - Text-color semantics (`button/text-*`, `breadcrumbs/*`) → `TEXT_FILL` (+ `SHAPE_FILL` if used on icons).
  - Overlays / fills → `FRAME_FILL`, `SHAPE_FILL`.
  - Base primitives: scope to fill/stroke/effect rather than `ALL_SCOPES` so designers reach for semantic tokens first.
- [ ] **Fix raw values leaking into the semantic layer.** Semantic tokens should always alias a primitive. These hold hardcoded hex instead:
  - `semantic colors/border/semi-transparent-light` = `#e0dedf @16%` — this color isn't even in the palette. Add a base primitive for it, then alias.
  - `semantic colors/button/ghost-default` = `#ffffff @0%` — alias a transparent primitive.
  - `semantic colors/breadcrumbs/lightbg-default` = `#ffffff @0%` and `…/darkbg-default` = `#000000 @0%` — alias transparent primitives.
- [ ] **Reconsider `spacing/special/negative-3xs`.** A lone negative spacing token is a smell; confirm it's genuinely needed (overlap layouts) or remove.

## P3 — Style cleanup

- [ ] **Remove leftover paint styles** `translucent bg` and `gr 1` if superseded by variables/effect styles (`translucent bg` also exists as an effect style — duplicated).
- [ ] **Fix double-spaces in effect style names**: `standard/light on light  - small`, `standard/dark on dark  - small`, `standard/light on dark -  small`.

## P4 — Confirm (possible responsive bugs, not auto-fix)

These look like slips but may be intentional — **confirm before changing**:

- [ ] Several **`Desktop HD` type sizes are smaller than `Desktop`**: `h5` 22→18, `h6` 16→15, `p1` 20→17, `p2`/`p3`/`c1`–`c4` also flat or smaller. h1–h4 scale up correctly (e.g. h1 56→72), so the small end inverts. Intended, or should HD be ≥ Desktop throughout?
- [ ] `line-height/general/c2` = Desktop 16 but mobile/HD 12 (Desktop taller than HD).
- [ ] `spacing/base/3xs` = Desktop 12, mobile 10, HD 10 (HD tighter than Desktop, unlike the rest of the scale).

## P5 — Structure (sets up the expansion phase)

- [ ] **Resolve the two empty pages** `+++ library` and `+++ UI` — either delete or make them the real homes (see next item).
- [ ] **Separate library from documentation.** Today components, color/type reference frames, and laptop mockups share `styles & components`. Recommended split: a **Library** page (published components only), a **Foundations** page (color/type/spacing/effect reference), and keep **mockups/concepts** separate. Clean separation is what makes the file safe to publish as a team library.

---

_Next: see `design-system-conventions.md` for the naming/usage standards these fixes align to, and the functional component hierarchy._
