# VECTO — Figma-to-Code Handoff

**Purpose.** How the Figma design system translates faithfully to shadcn + Tailwind code:
component-property → cva mapping, text/effect styles, the typeface implementation, and the
naming contract that keeps design and code honest over time. **Doc-key: `f2c` · Species: living
reference.**

**Scope.** Translation rules only. Figma *authoring* rules (variables, token sync) live in
`fig-conv`; build/setup/portability rules live in `fe-arch`; decision rationale lives in the
decision log, cited by ID. Corpus map: `docs/README.md`.

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
- shadcn emits `data-slot` / `data-variant` / `data-size` attributes → natural **Code Connect** anchors later.

**Three caveats to always hold:** (1) the State axis collapses to pseudo-classes, not props; (2) "Show X" booleans become composed children; (3) Tailwind alpha-modifier utilities (`/90`, `/30`) are pre-baked in Figma as `custom/*` variables because Figma can't do inline opacity math.

## 2. Text & effect styles → Tailwind

- ✅ The file's text styles are the **Tailwind type matrix enumerated** — `text-{size}/leading-{normal|none}/{weight|decoration}` in Inter. A designer's chosen style equals the equivalent utility classes. (Enumerate the current style set live from the file; style counts in a doc go stale.)
- ✅ The effect styles map to Tailwind `shadow-*` / `inset-shadow-*` / `drop-shadow-*` / `blur-*` / `backdrop-blur-*` utilities, plus `focus/default` and `focus/destructive` ring treatments.

## 3. Typeface

✅ **Main typeface: Google Sans Flex.** In Figma anchored at `Theme / font / font-sans`. Site is multilingual: **English (default) at launch; Armenian + Russian at/soon after.**

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

## 4. Content-model annotation (in Figma, per component)

✅ For every component that will hold editorial content, record what's editable and how — at design time, at the
smallest unit, before it's buried inside a page. The thinking already happens when the component is drawn; annotation
just externalizes it. This is the first of the content model's four expressions (annotation → TypeScript type →
Supabase schema → admin form — see `outline`); because the admin is built from the same shadcn primitives, a field's
type tells you both its Supabase column type and its admin form control ("rich text" → text column + rich-text editor;
"image" → Storage URL column + upload control). Marking the field type in Figma is already half the admin spec.

**Pick one tagging scheme and commit — mixing all three is the failure mode:**

| Mechanism | Use for | Example |
|---|---|---|
| Component property | Per-field source & type (most robust — structured, travels with instances) | `Source: CMS \| Static`, `Field: text \| richtext \| image \| toggle` |
| Annotation | Section-level behaviour that doesn't fit a property | `cardinality [2–6]`, `paginate past 6`, `hide at zero` |
| Layer name | Lightweight fallback only | `cms:title`, `static:hero-bg` |

**What gets recorded per component:**

- Each editable field — its type (text, textarea, richtext, image, number, date, select, toggle, link, relation)
- Static vs dynamic — part of the design (hardcoded) or content (from the CMS). Most images split here; mark every one.
- Singleton vs collection — one fixed instance, or a list (drives single-row config vs. a table)
- Cardinality — for collections, min/max and any pagination threshold
- Empty & fallback states — what renders at 2 when 3 were designed; what hides at zero
- Image constraints — aspect ratio and minimum dimensions for every dynamic image
- Locale — every editorial entity carries per-language values and a per-language publish state (EN / HY / RU). The content model is multilingual from the first annotation, even while only EN content exists.

✅ Per the default+exceptions rule (`fe-arch` §2a): content is CMS by default and render is static by default, so
**annotation only flags the deviations** — (a) hardcoded design-language content (shader backgrounds, foundational
visuals), (b) interactive leaves (forms, filters, menus, motion), (c) first-paint/LCP-critical content. No render
matrix, no per-component tagging pass. The entity noun list itself is maintained by the IA (`ia`) — annotation covers
whatever nouns it defines.

## 5. Naming & the design-layer contract

These rules keep the Figma→code translation *honest over time* — so a component name or a token can't quietly drift between the design file and the codebase. They pair with the project outline's **structure map & name registry** step (derived before Figma component work) and its **two-layer standard**.

- ✅ **Names come from Figma / the registry verbatim.** A component's code name is its Figma name, transferred exactly (kebab-case, slash-grouped). A rename is a *design decision* — flag it and ask; never rename silently in code. This is the rule HES learned the hard way (`navbar` → `SiteNav` drift → a 34-commit refactor).
- ✅ **Kebab-case is enforced for component names only.** Figma variables and CSS tokens keep the `fig-conv` §6 rules (no in-segment dashes; `/` for hierarchy, `_` for word-join). Don't reuse a primitive's name for a composition built from it; name a component by what consumes it, not where it came from.
- ✅ **The name registry / manifest is the source of truth for "what exists and what it's called."** A generated
  inventory file lists every shared component and where it lives; new components are registered there. Both you and
  Claude check it before building, so nothing gets rebuilt under a second name. Born ~85% right from the structure-map
  step, not frozen — start-local, promote to shared on a second real reuse.
- ✅ **A living `/styleguide` route renders every shared component.** A hidden page on the site itself showing the components in one place — the visual counterpart to the manifest, and where a new shared component gets registered. (This is a code-side page, distinct from the Figma file.)
- 📎 **Check Figma Code Connect availability** (Dev-seat-gated as of June 2026). If unlocked, it maps Figma components to code names automatically, and the manifest becomes a backup rather than the whole defense.
- ✅ **The vocabulary-translation rule: design-vocabulary instructions are translated, not obeyed literally.** A Figma
  "component" means *reusable unit*; a code component is also a *decomposition chapter* (zero overhead, split for
  maintainability regardless of reuse) — obeying "no need to make each section a component" on the wrong axis is how
  HES got a 750-line homepage file. When a designer instruction touches **code structure**, translate the intent — and
  if in doubt, ask.
