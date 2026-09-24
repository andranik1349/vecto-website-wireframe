# VECTO — Figma-to-Code Handoff

**Purpose.** How design decisions land in shadcn + Tailwind code: the component-property → cva
mapping used when reading a kit component, theme modes and inversion, the typeface implementation,
the content model's first expression, and the naming contract. **Doc-key: `f2c` · Species: living
reference.**

**Scope.** Code-side rules. The Figma file's contents and the handoff read-out contract live in
`fig-conv`; build/setup/portability rules live in `fe-arch`; decision rationale lives in the
decision log, cited by ID. Corpus map: `docs/README.md`.

**Standing context (DL-26).** Design is authored in code after the Phase 1 handoff; Figma settles the
foundations before it and stays available for sketches. The translation rules below apply at that handoff,
when reading an upstream kit component, and when a Figma sketch is the input to a change — not as an
ongoing sync. Nothing here obliges the code to match a Figma file afterwards.

**Status legend.** ✅ established · 🔧 decided in principle, spec pending · 📎 reference/context.

---

## 1. Component property → code mapping

✅ Figma component properties map to shadcn `cva` variants (cva — class-variance-authority, the class-recipe utility shadcn uses to map prop values to Tailwind class lists) with high fidelity. Rules (Button as the representative example):

- **`Variant`** (Default, Secondary, Destructive, Outline, Ghost, Link) → `cva` `variant` — **names match exactly**.
- **`Size`** (default, xs, sm, lg, icon, icon-xs, icon-sm, icon-lg) → `cva` `size` — **exact match**.
- **`State`** (Default, Hover, Focus, Loading, Disabled, Pressed) → **not a prop.** Becomes CSS pseudo-class variants (`hover:`, `focus-visible:`, `disabled:`) or a `disabled`/loading flag. Figma materializes states as variants only because it has no pseudo-states.
- **Boolean `Show …` props** (e.g. Show Left Icon) → optional **composed children** in JSX, not boolean props.
- **TEXT props** (e.g. Button Text) → `children`.
- Figma property names carry a `#id` suffix + Title Case → **normalize** on translation.
- shadcn emits `data-slot` / `data-variant` / `data-size` attributes → stable hooks for styling overrides and tests.

**Three caveats to always hold:** (1) the State axis collapses to pseudo-classes, not props; (2) "Show X" booleans become composed children; (3) Tailwind alpha-modifier utilities (`/90`, `/30`) live in Figma as the style layer's `custom/*` and `alpha/*` tokens — a base token plus a percentage (`fig-conv` §3), not a stored colour.

## 2. Text & effect styles → Tailwind

- ✅ The file's text styles are the **Tailwind type matrix enumerated** — `text-{size}/leading-{normal|none}/{weight|decoration}`, carrying whichever family the style layer's `font/family/*` currently names. A designer's chosen style equals the equivalent utility classes. (Enumerate the current style set live from the file; style counts in a doc go stale.)
- ✅ The effect styles map to Tailwind `shadow-*` / `inset-shadow-*` / `drop-shadow-*` / `blur-*` / `backdrop-blur-*` utilities, plus `focus/default` and `focus/destructive` ring treatments.

## 2a. Theme modes & inversion

✅ **Light and dark are the same components reading different values.** The `Mode` collection's semantic tokens
become CSS custom properties, and a theme class on an ancestor redefines them for everything beneath it — nothing
about a component changes between themes. That is why **every colour in the system comes from a semantic token**: a
hand-written colour, or a Tailwind `dark:` utility, is invisible to this mechanism and survives into the wrong theme.

✅ **The marketing site ships dark only** — background media, video and shader effects don't adapt cleanly across
themes, and the brand is dark-first. **The admin and any hosted tools carry a real light/dark switch** on the same
kit, so both themes are live in the codebase even though site visitors only ever see one.

✅ **Inverted sections are relative, not pinned.** An element needing outstanding emphasis takes the opposite theme
of whatever surrounds it — a light band on the dark site, a dark band if the surrounding admin page is light. It
expresses a contrast *relationship*, not a fixed colour:

```css
.dark  .theme-invert { /* the light values */ }
.light .theme-invert { /* the dark values  */ }
```

✅ **Name the class for the relationship (`theme-invert`), never for the resulting colour.** `class="light"` records
an outcome and loses the intent, leaving the next reader unable to tell a brand-fixed light band from an inverted
one — and unable to change either safely.

Three conditions this mechanism depends on, each of which fails *silently* when broken:

- ✅ **The theme class is always explicit** — `.light` or `.dark` stamped on `<html>`. Never "no class means light":
  an implicit light theme gives `.light .theme-invert` nothing to match, and the inversion simply doesn't happen.
- ✅ **Invert scopes never nest.** A nested `.theme-invert` matches its outer ancestor's theme class rather than its
  own scope, so it renders identically to its parent with no error.
- ✅ **No `dark:` colour utilities anywhere.** Inside an inverted section the page ancestor still carries `.dark`, so
  the utility fires against the inversion.

✅ **`color-scheme` follows the scope** — set at the root and re-set on every inverted section, so browser-rendered
chrome (scrollbars, form controls, autofill) matches the section it sits in rather than the page around it.

## 3. Typeface

✅ **Main typeface: Google Sans Flex.** In Figma anchored at `Style` → `font/family/sans`. Site is multilingual: **English (default) at launch; Armenian + Russian at/soon after.**

- ✅ **Two fonts, one CSS family, per-glyph resolution by codepoint** (browser-native): Google Sans **Flex** serves Latin + Latin-ext (all expressive axes); Google **Sans** serves Cyrillic / Armenian / Greek (and other broad scripts). Both declared under one `@font-face` family name, each scoped with `unicode-range`. Point `--font-sans` at the unified family.
- ✅ **Self-host is mandatory** (the CDN won't unify two families under one name). Both are OFL now (Google Sans went OFL 2025-12-10). Install the **variable** Fontsource packages: `@fontsource-variable/google-sans-flex` and `@fontsource-variable/google-sans` — **not** the static `@fontsource/*` packages (those drop the axes).
- ✅ **Hand-author the `@font-face` blocks** (for the cross-family unify), `src` pointing at the **full variable `.woff2`** (not a weight-only slice). Use modern `format('woff2') tech(variations)`. Keep a real fallback: `--font-sans: '<family>', system-ui, sans-serif` (glyphs outside both ranges fall through).
- ✅ **Optical size (opsz):** `font-optical-sizing: auto` is the browser default → font-size auto-maps to opsz, no per-style/per-breakpoint tuning. Don't pin `opsz` in `font-variation-settings` (that disables auto). Control weight via `font-weight`; roundness/width via `font-variation-settings`; leave opsz to auto.
- ✅ **Axis ranges differ by script:**
  - Flex (Latin): opsz **6–144**, weight **1–1000**, plus width, slant, grade, roundness — full expressive range.
  - Google Sans (non-Latin): opsz **17–18**, weight **400–700**, grade, real `ital` axis. The narrow opsz means glyph
    *shapes* barely change with size — but in practice opsz still **auto-adjusts character spacing/metrics on
    non-Latin**, so mixed Latin + non-Latin runs stay balanced and look good (tested). Heavy/hairline weights
    (200/800/900) clamp to 400–700 on non-Latin; shadcn's 400–700 usage is safe.
- ✅ **Design constraint:** expressive axes (width/roundness/slant) are Latin-only. Don't make hierarchy depend on them — treat as a Latin flourish over a stable multi-script baseline.
- ✅ **Figma gotcha:** per-glyph fallback is a *browser* behavior; Figma won't auto-swap to Google Sans for Armenian/Cyrillic. Multilingual comps must set non-Latin runs to Google Sans manually, or show tofu.
- 📎 **Perf note:** `unicode-range` gates the download — the broad-script file is only fetched when an in-range glyph appears, so all-English pages pay zero bytes for multilingual support.

## 4. Content model — the prop types are its first expression

✅ For every component that will hold editorial content, **the TypeScript prop types are where the content model is
first written down** — at the smallest unit, before it's buried inside a page. This is the first of the content
model's three expressions (prop types → Supabase schema → admin form — see `outline`); because the admin is built
from the same shadcn primitives, a field's type tells you both its Supabase column type and its admin form control
("rich text" → text column + rich-text editor; "image" → Storage URL column + upload control). Typing the component
is already half the admin spec.

✅ **The type is the annotation.** Where a distinction can't survive as a type — cardinality bounds, a pagination
threshold, hide-at-zero behaviour — put it in a docstring on the prop it constrains, never in a separate register.
One home per field, enforced by the compiler wherever the compiler can reach and adjacent to the code where it can't.

**What every editorial component's props must express:**

- Each editable field — its type (text, textarea, richtext, image, number, date, select, toggle, link, relation)
- Static vs dynamic — part of the design (hardcoded) or content (from the CMS). Most images split here; type every one.
- Singleton vs collection — one fixed instance, or a list (drives single-row config vs. a table)
- Cardinality — for collections, min/max and any pagination threshold
- Empty & fallback states — what renders at 2 when 3 were designed; what hides at zero
- Image constraints — aspect ratio and minimum dimensions for every dynamic image
- Locale — every editorial entity carries per-language values and a per-language publish state (EN / HY / RU). The content model is multilingual from the first annotation, even while only EN content exists.

✅ Per the default+exceptions rule (`fe-arch` §2a): content is CMS by default and render is static by default, so
**only the deviations need marking** — (a) hardcoded design-language content (shader backgrounds, foundational
visuals), (b) interactive leaves (forms, filters, menus, motion), (c) first-paint/LCP-critical content. No render
matrix, no per-component tagging pass. The entity noun list itself is maintained by the IA (`ia`) — the types cover
whatever nouns it defines.

## 5. Naming & the design-layer contract

These rules keep names from quietly forking across the codebase — one concept acquiring two names, or a primitive's name being reused by the composition built from it. They pair with the project outline's **structure map & name registry** step and its **two-layer standard**.

- ✅ **Names come from the registry verbatim.** A component's code name is its registry name, transferred exactly (kebab-case, slash-grouped). A rename is a *design decision* — flag it and ask; never rename silently. This is the rule HES learned the hard way (`navbar` → `SiteNav` drift → a 34-commit refactor).
- ✅ **Kebab-case is enforced for component names only.** Figma variables and CSS tokens keep the `fig-conv` §6 rules (no in-segment dashes; `/` for hierarchy, `_` for word-join). Don't reuse a primitive's name for a composition built from it; name a component by what consumes it, not where it came from.
- ✅ **The name registry / manifest is the source of truth for "what exists and what it's called."** A generated
  inventory file lists every shared component and where it lives; new components are registered there. Both you and
  Claude check it before building, so nothing gets rebuilt under a second name. Born ~85% right from the structure-map
  step, not frozen — start-local, promote to shared on a second real reuse.
- ✅ **A living `/styleguide` route is the design system's visual artifact** (DL-26), not a convenience. A hidden page on the site itself rendering the token sheet — every colour, type step and radius as a swatch with its name and resolved value — alongside every shared component and its states. It is where a new shared component gets registered, and it is what design decisions are judged against, because it shows the real renderer: motion, shader surfaces, optical sizing, per-glyph multilingual fallback. Anything that must be looked at to be approved belongs on it.
- ✅ **The vocabulary-translation rule: design-vocabulary instructions are translated, not obeyed literally.** A Figma
  "component" means *reusable unit*; a code component is also a *decomposition chapter* (zero overhead, split for
  maintainability regardless of reuse) — obeying "no need to make each section a component" on the wrong axis is how
  HES got a 750-line homepage file. When a designer instruction touches **code structure**, translate the intent — and
  if in doubt, ask.
