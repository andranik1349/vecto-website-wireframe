> **⚠️ LEGACY — archived 2026-06-30.** This document belongs to the previous VECTO design-system effort (the custom red/dark Figma system). VECTO is now being rebuilt in React on a shadcn **Luma** baseline. Kept for historical reference only — not a current source of truth.

---

# VECTO Design System — Conventions

_Draft for review — v0.1, 2026-06-28. These are the agreed-upon standards for VECTO's design system. Once we sign off, every new token, component, and property follows them, and the cleanup checklist brings existing assets into line._

**Scope of the system.** One system serves three surfaces:

1. **The website** — dark, branded, marketing-led (the primary driver today).
2. **Internal tools** — denser, utility-led; may eventually want a light theme.
3. **Small VECTO-branded products** — e.g. the "VECTO Plugins" pages already in Figma.

**Theming decision (this round):** **dark-only now, theme-ready structure.** We do not build a light mode yet, but we name and scope everything so a light mode is a value swap later — never a rename. The single rule that makes this work is in §1.3.

---

## 1. Semantic variable usage — what each token is for, and how to apply it

### 1.1 Three tiers (Primitive → Semantic → Component)

**Architecture decision:** VECTO-native naming + a formal **3-tier** token pipeline, adopting two conventions from shadcn — **foreground pairing** and **theme-first overrides** — but **not** shadcn's literal token names. Rationale: tokens are consumed by **bespoke CSS** (the wireframe model), so shadcn's vocabulary (`background`/`card`/`ring`…) adds no benefit and would shrink VECTO's richer role set (elevation scale, overlay ramp, multiple borders). We keep the expressive names and borrow only the discipline.

You already have all three tiers — they're mixed into one collection and aliased inconsistently. We separate and re-alias them; we do not invent new ones.

```
Tier 1 — Primitive       Tier 2 — Semantic         Tier 3 — Component
(raw values)        →    (role · THEME layer) →    (component-scoped)
base/dark-2              surface/raised            button/primary-bg
#222429                  action/primary            input/border
                         text/primary              card/bg
```

- **Tier 1 — Primitive** (`base colors/*` today). The raw palette. The _only_ place a literal value lives. Single value, never theme-aware, **never consumed directly by a component**.
- **Tier 2 — Semantic** (`surface/*`, `text-generic/*`, `border/*`, `overlay/*`). Role-based names. **This is the theme layer — the only tier that ever receives a second (Light) value.** Aliases Tier 1.
- **Tier 3 — Component** (`button/*`, `input/*`, `tag/*`, `breadcrumbs/*`). Component-scoped tokens. **Aliases Tier 2 only — never a primitive.**

**The one discipline rule: `T3 → T2 → T1`, no skipping.**
Today `button/main-default → base/brand/primary-2` skips Tier 2 — that's the violation to fix. Correct routing: add `action/primary → brand/primary-2` (Tier 2), then `button/primary-bg → action/primary` (Tier 3). Likewise, a semantic (Tier 2) token must never hold a raw hex — if you reach for hex there, a primitive is missing; add it and alias. (Cleanup P2 covers the current violations.)

### 1.1a Foreground pairing (stolen from shadcn)

Every surface/fill role that carries content defines the foreground (text/icon) color guaranteed legible on it. We do this **lightly**, not mechanically: VECTO's dark elevations (`canvas`/`default`/`raised`/`overlay`) share one foreground set (`text/primary`/`secondary`/`tertiary`), so we don't explode a foreground per elevation. We only add explicit pairings where the foreground *flips*: `text/on-accent` (on brand fills), `text/on-inverse` (on light surfaces). Component tokens then reference the pairing, e.g. `button/primary-fg → text/on-action`.

### 1.1b Figma collection structure

Split the single style collection into **three collections**, mirroring the tiers:

| Collection | Modes | Holds |
|------------|-------|-------|
| **Primitives** | 1 (modeless) | `base/*` palette |
| **Semantic** | `Dark` now → `Light` later | all role tokens — **the only collection that gets a theme mode** |
| **Component** | 1 (modeless) | `button/*`, `input/*`, `tag/*`, … aliasing Semantic |

Figma aliases across collections fine. This keeps the future Light mode confined to the Semantic collection instead of bloating Primitives and Component with a mode they don't need. **Do the split now, while dark-only and pre-production** — splitting after a Light mode exists is a much worse migration. (Moving a variable between collections means recreating it, so fold this into the same pass as the cleanup renames.)

### 1.1c CSS cascade (the consumption model)

Bespoke CSS emits one `:root` block, layered by tier. A theme switch overrides **only Tier 2**:

```css
:root {
  /* T1 — primitives (raw; rarely referenced directly) */
  --neutral-dark_1:#111214; --brand-red:#ca1d00; /* … */
  /* T2 — semantic (THE theme layer) */
  --surface-canvas:  var(--neutral-dark_1);
  --content-primary: var(--neutral-white);
  --action-primary:  var(--brand-red);
  /* T3 — component (alias T2 only) */
  --button-primary_bg: var(--action-primary);
  --button-primary_fg: var(--content-on_accent);
  --input-border:      var(--line-default);
}
[data-theme="light"] {            /* override ONLY T2 → entire UI reskins */
  --surface-canvas:  var(--neutral-light_4);
  --content-primary: var(--neutral-dark_2);
}
```

Numbers stay their own layer regardless (§1.4): redefined per breakpoint in media queries, orthogonal to theme.

### 1.2 The semantic color roles (current + recommended renames)

Your roles are good; the _names_ bake in the literal tone, which blocks theming. Recommended target naming on the right.

| Role group | Purpose | Today | Theme-ready target |
|------------|---------|-------|--------------------|
| **surface** | Backgrounds, by elevation | `surface/dark-deep`, `surface/dark`, `surface/dark-elevated`, `surface/popout`, `surface/muted`, `surface/light`, `surface/secondary-light` | `surface/canvas`, `surface/default`, `surface/raised`, `surface/overlay`, `surface/muted`, `surface/inverse`, `surface/inverse-muted` |
| **text-generic** | Text & icon foreground | `primary`, `secondary`, `tertiary`, `accented-darker/-lighter`, `*-inverse`, `error` | keep — these are already role-named (good model to copy) |
| **border** | Strokes & dividers | `default`, `light`, `semi-transparent-light`, `brand-accent`, `focus`, `focus-muted` | `default`, `subtle`, `strong`, `accent`, `focus`, `focus-muted` |
| **button** | Action fills & labels | `main-*`, `secondary-light-*`, `secondary-dark-*`, `ghost-*`, `accent-*`, `disabled`, `text-*` | `action-primary-*`, `action-neutral-*`, `action-ghost-*`, `action-accent-*`, `action-disabled`, `on-action-*` |
| **input** | Form field parts | `input-border-*`, `input-bg-*`, `input-text-*`, `input-label-*`, `input-icon-*`, `input-helper`, `input-error` | keep structure; drop the redundant `input-` stem since they're already under `input/` |
| **tag / chip** | Pills & labels | `tag/primary-*`, `tag/secondary-*` | `tag/default-*`, `tag/emphasis-*` |
| **breadcrumbs** | Breadcrumb states | `breadcrumbs/lightbg-*`, `breadcrumbs/darkbg-*` | fold into generic `text-generic` + `surface` where possible; keep only if genuinely distinct |
| **overlay** | Scrims & translucent layers | `overlay/dark-1..3`, `overlay/light-1..3`, `overlay/modal`, `overlay/neutral` | keep |

**Tier note:** `surface`, `text-generic`, `border`, `overlay` are **Tier 2 (Semantic)**. `button`, `input`, `tag`, `breadcrumbs` are **Tier 3 (Component)** and relocate to the Component collection (§1.1b), re-aliased to route through Tier 2.

> The naming target is the meaningful change, not a churn for its own sake. **A semantic name should answer "what is this for?" never "what color is it?"** `surface/canvas` can become light or dark by mode; `surface/dark` can't. Rename is optional for v0.1 if disruptive, but it's the one thing that unlocks the "theme-ready" goal — recommended.

### 1.3 The theme-readiness rule

When light mode arrives, it should be: add a **`Light` mode** to the **Semantic collection** (§1.1b) and give each Tier-2 token a second value. Primitives and Component tokens stay modeless — Component tokens inherit the theme automatically because they alias Semantic. This only works if:

- semantic names are role-based (§1.2),
- nothing downstream binds a primitive where a semantic exists (the `T3→T2→T1` rule, §1.1), and
- the theme layer is isolated in its own collection.

So even though we ship dark-only, **name the Semantic collection's mode `Dark` now** and treat that collection as the single source of theming.

### 1.4 Numbers: responsive modes, not themes

`variables - numbers` already does the right thing — Desktop / Desktop HD / mobile are **breakpoints**, expressed as modes. Keep type size, line-height, spacing, radius, and layout values there. In code these become CSS custom properties redefined per media query (matches the wireframe token approach). Confirm the P4 inversions are intentional.

---

## 2. Token naming conventions

**The delimiter rule (resolves the CSS-export problem):**

- **`/` = hierarchy** — real groups only, kept shallow (1–2 levels) so Figma's variable tree stays flat and usable.
- **`_` = word-join inside a single name** — `red_strong`, `primary_hover`, `on_accent`, `focus_muted`.
- **No hyphens in Figma names.** Hyphens appear only in the exported CSS, generated from `/`.

Why: most exporters collapse both `/` and `-` to `-` in CSS, so an in-name hyphen (`red-strong`) becomes indistinguishable from a hierarchy boundary. Banning `-` in source names and joining words with `_` makes the export **lossless and reversible** — in the CSS, every `-` is a hierarchy level and every `_` is a word-join. `_` is valid in CSS custom-property names, so `--brand-red_strong` is legal and unambiguous. Example: Figma `action/primary_hover` → CSS `--action-primary_hover`.

Other rules:

- **Lowercase** throughout.
- **Order within a name:** role → modifier → state, joined by `_` — `primary_hover`, `border_error`, `text_readonly`.
- **State vocabulary** (last word): `default`, `hover`, `active`, `selected`, `disabled`, `error`, `readonly`, `focus`.
- **No literal color values** in semantic/component names (`dark`, `light`, hex) — those are mode values (§1.3).
- **No `+`, spaces, or source-tool stems.** `input-text+placeholder` → `input_field`; drop `icons8_`.

| Token type | Convention | Example |
|------------|-----------|---------|
| Color primitive (T1) | `family / name_variant` | `brand/red_strong`, `neutral/dark_2` |
| Color semantic (T2) | `role / name_state` | `surface/raised`, `action/primary_hover` |
| Color component (T3) | `component / part_state` | `button/primary_bg`, `input/border_error` |
| Type size | `text_size / scope / token` | `text_size/general/h2` |
| Line height | `line_height / scope / token` | mirror type-size 1:1 |
| Spacing | `spacing / base / step` | `spacing/base/m` |
| Layout metric | `spacing / layout / name` | `spacing/layout/grid_gap` |
| Radius | `radius / step` | `radius/m`, `radius/pill` |

---

## 3. Component & component-property naming conventions

### 3.1 Component names

**Pattern:** `Group / ComponentName` (group prefix from §4). Component name in `PascalCase` or natural case, singular (`Button`, not `Buttons`). No version suffixes (`-v1`) — variants express versions. No abbreviations that aren't obvious.

### 3.2 Variant properties (the contract that makes components predictable)

Use a small, consistent vocabulary of property names and values across **every** set:

| Property | Allowed values | Use for |
|----------|---------------|---------|
| `size` | `huge`, `large`, `medium`, `small` (lowercase) | scale variants |
| `style` | `primary`, `neutral`, `ghost`, `accent`, `disabled` | visual emphasis (rename "secondary light/dark" → tones handled by theme + `neutral`) |
| `state` | `default`, `hover`, `active`, `selected`, `disabled`, `error`, `readonly`, `focus` | interaction state |
| `type` | component-specific set | structural variants (e.g. input `layout`: `standard`, `combo-left`, `combo-right`) |

Rules:

- **Property names lowercase**, values lowercase, no spaces (`secondary light` → use `style=neutral` + tone via theme, or `style=neutral-strong`).
- Every interactive component exposes a `state` property with at least `default` and `hover`; add `disabled`/`focus` where applicable.
- **Boolean props** read as `show <thing>` (`show left icon`, `show helper text`) — you already do this; keep it.
- **Instance-swap props** named for the slot (`left icon`, `right icon`, `input type`).
- **Text props** named for content (`btn-label`, `placeholder`, `input label`).
- Strip the auto-generated `#5:0` hashes from property labels where you can (cosmetic, but cleaner in the picker).

### 3.3 Layer naming inside components

Name structural layers by role (`label`, `icon-left`, `container`), not by content or Figma defaults (`Frame 12`). This pays off when devs read the inspect panel and for Code Connect later.

---

## 4. Hierarchy — functional grouping

We organize by **purpose**, not by atomic tier. Six groups. Every component (and the page structure) lives in exactly one.

### 4.1 The groups

| Group | What belongs | Why |
|-------|-------------|-----|
| **Foundations** | Tokens, type styles, effects, icon library, logo | The raw materials; not "components" in the UI sense |
| **Actions** | Button, Icon Button, Chip, Link | Things you click to do something |
| **Forms** | Input (all field types), Dropdown, Select rows, Switch, Slider, Calendar/Date, Helper text, Label | Data entry & selection |
| **Navigation** | Global menu link, Header/Top nav, Dashboard nav, Tabs, Tab selector, Breadcrumbs, Pagination | Moving around the product |
| **Data Display** | Card, Table (header/row/cell), List, Stat/Metric, Avatar, Badge/Tag | Presenting information |
| **Feedback** | Alert/Banner, Toast, Tooltip, Modal/Dialog, Empty state, Loading/Skeleton | System → user communication |

### 4.2 Where your existing components land

| Group | Existing in file | Status |
|-------|-----------------|--------|
| **Foundations** | Color + number tokens, 50 text styles, 11 effect styles, ~200 icons, `logo final` | Present — needs icon rename + library/doc split |
| **Actions** | `CTA button` (36), `single icon button` (28), `chip` (2) | Present — solid. Add `Link`. Reconcile button `style` values |
| **Forms** | `input main`, `input base tall/short`, `input-helper-text`, `dropdown` family, `switch`, `input-slider`, `calendar` family | Strong — the deepest area. Add Checkbox/Radio as real components (only select icons exist today) |
| **Navigation** | `global menu link`, `dashboard global nav`, `horizontal tabs`, `tab selector`, `breadcrumbs-elements`, `pagination` | Present — reconcile `horizontal tabs` vs `tab selector` (likely merge). Add a composed Header/Top-nav |
| **Data Display** | `card small`, `card-list-v1/v2`, `table-column-header` | Thin — consolidate cards into one `Card` set; build Table rows/cells, Badge/Tag, Avatar, Stat |
| **Feedback** | (helper text / error states only) | **Largest gap** — no Alert, Toast, Tooltip, Modal, Empty state, Skeleton |

### 4.3 Page structure in Figma (mirrors the groups)

```
📄 Foundations        — color, type, spacing, effects, icons, logo (reference)
📄 Library            — published components, sectioned by the 6 groups
📄 Patterns           — composed blocks (forms, headers, hero, plugin-page layouts)
📄 Concepts / Mockups — explorations (your current "ui concept")
```

---

## 5. What "working design system" means here (bridge to expansion)

To support website + internal tools + products, the priority build order after cleanup:

1. **Reconcile Actions** — settle button `style` vocabulary; add `Link`.
2. **Close Forms gaps** — Checkbox, Radio (as components), confirm field family is complete.
3. **Build Data Display** — one `Card` set (replaces v1/v2 + card small), Table row/cell, Badge/Tag, Avatar, Stat/Metric.
4. **Build Feedback** — Alert/Banner, Toast, Tooltip, Modal, Empty state, Skeleton.
5. **Compose Patterns** — Header, footer, hero, and a reusable "Plugin page" template, assembled from the above using only semantic tokens.
6. **Publish** as a team library once Foundations + Library pages are clean.

Each new component must: consume semantic tokens only, expose the §3 property vocabulary, include `default`/`hover` (+ `disabled`/`focus`) states, and be named per §3–4.

---

## Open questions for sign-off

1. **Semantic renames (§1.2):** adopt role-based names now (recommended, unlocks theming) or defer to avoid churn on existing instances?
2. **Button `style` vocabulary (§3.2):** OK to collapse `secondary light` / `secondary dark` into `neutral` (with tone handled by theme), or keep them as explicit styles?
3. **Tabs:** merge `horizontal tabs` and `tab selector`, or are they genuinely different patterns?
4. **Expansion scope:** build all of §5 in Figma, or do you want to take the conventions and build yourself with me reviewing?
