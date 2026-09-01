# VECTO — Figma Design Conventions

**Purpose.** How the VECTO design-system Figma file is authored and kept in sync with code:
foundational stance, the file's token architecture, what to keep vs ignore, and the token
authoring & sync discipline. **Doc-key: `fig-conv` · Species: living reference.**

**Scope.** Authoring rules only. How Figma *translates* to code (prop mapping, typeface, naming
contract) lives in `f2c`; how the front-end is built lives in `fe-arch`; decision rationale lives
in the decision log, cited by ID. Corpus map: `docs/README.md`.

**Status legend.** ✅ established · 🔧 decided in principle, spec pending · 📎 reference/context.

---

## 1. Foundational stance

- ✅ **Figma is the source of truth for styling.** Code conforms to Figma, not the reverse.
- ✅ **shadcn Luma is the substrate, not the visual identity** (decision DL-01). Reasons: (1) smooth design→code handoff — Figma and code speak the same vocabulary; (2) don't reinvent primitives (inputs, selects, validation, alerts, tooltips, dialogs). The VECTO brand is applied *on top*, at the variable/token layer.
- ✅ **Luma is optional / nice-to-have.** It gives roomier spacing, pill buttons, and slightly larger type out of the box (less to tweak), but is not mandatory. If used, it's a starting point to brand — not the look.
- ✅ **Always enumerate tokens via the full Figma Plugin API** (`getLocalVariableCollectionsAsync` + `getLocalVariablesAsync`, `valuesByMode` across every mode, resolving aliases). Never `get_variable_defs` for authoring/auditing — it is node-scoped and single-mode, so it hides multi-mode collections and alias chains.

## 2. The Figma file (as-is)

- ✅ Source-of-truth file: **shadcn Luma UI kit**, file key `RsPzB1zvvyyZBq062lbYXz`. Currently stock (no VECTO branding yet).
- ✅ Contents: the full shadcn registry as component pages plus extras (Button Group, Field, Input Group, Item, Kbd,
  Empty, Spinner, Native Select, Data Table, Date Picker, Combobox, Typography), official + Pro block libraries, icon
  sets, text styles, effect styles, and the variable collections. **For current counts and contents, enumerate the
  file live via the Plugin API — do not trust any cached numbers in a doc.**
- 📎 The Figma variable collection *numbering* (e.g. `2. Theme` vs `3. Mode`) may drift as the file is reorganized — re-enumerate before building rather than trusting cached numbers.

## 3. Token architecture (how the file resolves)

✅ Color resolves through a **3-tier alias chain**, and the semantic tier's names are shadcn's CSS variables 1:1:

**`Mode` (semantic, Light/Dark) → `Theme` (explicit light/dark pairs) → `TailwindCSS` (raw primitives)**

| Collection | Modes | Role in code |
|---|---|---|
| `TailwindCSS` | single | Tailwind primitive scale — full color ramps, spacing, sizing, radius, border/stroke width, opacity, leading, breakpoints. |
| `Theme` | single | The `@theme` layer: color tokens as `-light`/`-dark` pairs, font families, font-weights, `text/*` size+line-height, radius, containers, shadow/blur parts. |
| `Mode` | **Light / Dark** | shadcn semantic tokens — `base/background`, `base/primary`, `base/destructive`, `base/border`, `base/input`, `base/ring`, `base/card`, `chart-*`, `sidebar-*`. **`base/primary` ↔ `--primary` ↔ `bg-primary`.** |
| `Custom` | **Desktop / Mobile** | Responsive layer (breakpoint-swapped values). |
| `Icon Library` | single | Icon-set switcher. |

- ✅ Example chain: `base/primary` → Light `Theme/primary-light` → `Tailwind/neutral/900` (`#171717`); Dark → `neutral/200` (`#e5e5e5`). = `--primary` under `:root` vs `.dark`.

## 4. What to keep vs. ignore in the file

- ✅ **Ignore the `problocks` groups** inside the **`Mode`** and **`Custom`** collections. They are Figma-limitation workarounds + Pro-blocks bonus content (e.g. the `custom/*` alpha entries in Mode; the `heading-*` / `container-padding` / `section-padding` tokens in Custom). Quarantined, not deleted. We do not use them.
- ✅ **Ignore the `problocks` typography styles.**
- ✅ **Keep the `tailwind default` typography group** as ad-hoc utilities (still occasionally useful).
- ✅ We replace the ignored content with **our own custom variable system + fluid type ramp** (§5).

## 5. Styling we will build on top (decided; spec to come)

🔧 A custom variable system validated across past VECTO projects. Extends Tailwind with:

- **VECTO branded colors** — authored in Figma under `1. TailwindCSS / vecto_colors`. This group is broader than plain hue ramps: it holds the 50–950 brand ramps **and** utility color variables with baked-in alpha (translucent values pre-composited to work around Figma's opacity handling), and may grow further. See §6 for the export rule.
- **Semantic utility color variables** — translucent surfaces, input-field border & fill variables, shadow/glow effects, gradients, and similar. Some translucent-surface values are realized as the alpha-baked entries in `vecto_colors`.
- 🔧 **A fluid type ramp built on Tailwind** (replaces Luma's problocks heading tokens).
- ✅ **Responsive breakpoint modes** — the modes the type and spacing scales respond across.
- ✅ **Dark/light, if in scope, is authored here as token modes** — never retrofitted later.

The exact token structure, naming conventions, and the branded/semantic/translucent/glow/gradient
definitions will live in their own spec doc — **`tokens` (`front-end/tokens.md`), created when the
spec is authored** (seed material: `token-variant-spec-draft.md` in the project-root
`explorations/` folder). Not defined here.

## 6. Token authoring & sync discipline

- ✅ **Color source split.** Default Tailwind palettes (slate, gray, zinc, neutral, stone, red, blue, …) install
  **directly from the Tailwind source** — do NOT clone or overwrite them from Figma. **VECTO's own colors live in
  Figma under `1. TailwindCSS / vecto_colors` and are written to CSS from the Figma values** (Figma is the source of
  truth for VECTO colors only). So: defaults ← Tailwind repo; VECTO colors ← Figma.
- ✅ **Export the *entire* `vecto_colors` group — enumerate it live, don't match a fixed list.** The group is more than
  the 50–950 brand ramps: it also contains **utility color variables with baked-in alpha** (pre-composited translucent
  values that work around how Figma stores opacity on variables), and it may include other custom color tokens now or
  later. When exporting, read the current contents of the `vecto_colors` group and write out **everything in it** — do
  not assume "VECTO colors = the numeric ramps" and do not skip entries that don't fit a tidy `<name>-<step>` pattern.
  If something in the group is unusual, include it and interpret from context rather than dropping it. (This note
  exists specifically so the export step isn't taken too literally and a whole sub-group of alpha/utility colors isn't
  missed.)
- ✅ **Stamp Figma variable IDs as comments** whenever a Figma variable — *especially any custom one* — is written to
  CSS as a token. Re-syncing after initial setup must key off the **variable ID, not the name**: token/variable-name
  syntax does not always translate 1:1 and is error-prone, whereas variable IDs are foolproof and stable **even after
  a variable is renamed** in Figma. Example: `--brand-500: #e11900; /* figma: VariableID:1234:5678 */`.
  - ⚠️ **CSS has no nested comments.** A literal `*/` inside another comment closes the OUTER comment early, spilling
    the rest into live CSS — Tailwind v4's parser then throws `Unterminated string`. The per-token ID comments are
    single, non-nested, so they're fine. The trap is a **header/docblock that documents the comment format by quoting
    it** (e.g. writing `/* figma: … */` *inside* a surrounding `/* … */` header). Don't quote a full comment inside a
    comment — describe the format without the literal closing `*/` (e.g. write it as `figma: VariableID:…` in a CSS
    comment), or keep the example out of a comment block entirely.
- ✅ **No dashes (`-`) inside Figma variable name segments.** Use `/` for hierarchy and `_` for word-join within a
  segment. **Why:** on export both `/` and `-` collapse to `-` in CSS, so a dash inside a segment becomes
  indistinguishable from a hierarchy boundary — there's no in-name delimiter swap that fixes it after the fact; the
  fix is to not put word-dashes in segments in the first place. This makes the (already unreliable) name→CSS
  translation worse. The variable ID stays the primary identifier regardless (see above), but keep the hierarchy
  clean.
  - Good: `vecto_colors/red/500`, `vecto_colors/red_alpha/5`
  - Bad: `vecto_colors/red-alpha/500`
