# VECTO — Figma Design Conventions

**Purpose.** What the VECTO Figma file is, how its variables resolve, and exactly which of them are
read out at the handoff to code. **Doc-key: `fig-conv` · Species: living reference.**

**Scope.** The Figma side only: the file's state, its token architecture, and the read-out contract.
How the values *translate* once in code (prop mapping, theme modes, typeface, naming contract) lives
in `f2c`; how the front-end is built lives in `fe-arch`; decision rationale lives in the decision
log, cited by ID. Corpus map: `docs/README.md`.

**Status legend.** ✅ established · 🔧 decided in principle, spec pending · 📎 reference/context.

---

## 1. Foundational stance

- ✅ **Figma is authoritative for foundations until the handoff; code is afterwards** (decision DL-26).
  Palette, type and radius character are settled visually in Figma, then read out into the production CSS
  per §6. From then on the code is the source of truth for styling: where the two disagree, the code is
  right. Figma stays useful for sketching — a frame is sometimes the quickest way to show Claude Code what
  is wanted — but a sketch is input to a change, not a spec the code has to keep matching.
- ✅ **`/styleguide` is what designs are proofread against** — the rendered token sheet and component
  inventory in the real browser, with the real font and colour space (`f2c` §5). It replaces the Figma
  file as the thing you look at to judge the system, because it shows what actually ships: motion, shader
  surfaces, optical sizing and per-glyph multilingual fallback, none of which Figma renders faithfully.
- ✅ **shadcn Luma is the substrate, not the visual identity** (decision DL-01). Reasons: (1) smooth design→code handoff — Figma and code speak the same vocabulary; (2) don't reinvent primitives (inputs, selects, validation, alerts, tooltips, dialogs). The VECTO brand is applied *on top*, at the variable/token layer.
- ✅ **Luma is the file's only style.** The other stock styles were pruned (§2), so its roomier spacing, pill buttons and larger default type are the starting point we brand away from — not a look we are keeping.
- ✅ **Always enumerate tokens via the full Figma Plugin API** (`getLocalVariableCollectionsAsync` + `getLocalVariablesAsync`, `valuesByMode` across every mode, resolving aliases). Never `get_variable_defs` for authoring/auditing — it is node-scoped and single-mode, so it hides multi-mode collections and alias chains.

## 2. The Figma file (as-is)

- ✅ Source-of-truth file: **`jgKesgYlBNElvkPiyWS8US`** — our own copy of the shadcn/ui kit for Figma. It is
  **self-contained**: no other Figma file subscribes to it as a library, so writing into its stock variables breaks
  nothing downstream.
- ✅ Kit version lives in `Style` → `meta/version`. Read it before any token work — the kit's variable model changed
  materially between 2.x and 3.0, and the skill pinned at `docs/shadcn-design-figma/` branches on it.
- ✅ **The `Style` collection is pruned to Luma, in two modes:** `Luma-VECTO` (the collection default, and the working
  column) and `Luma reference backup` (kept pristine as the rollback source). Finding what has been branded: `brand` §1.
- ✅ **Brand values overwrite `Luma-VECTO` in place; we do not add a mode.** This departs deliberately from the
  `shadcn-design-apply-brand` skill, whose add-a-mode rule exists to protect *subscribing* files — which we have none
  of. The backup column supplies the rollback that rule would otherwise provide, and overwriting also skips the
  skill's whole-collection clone step, its most failure-prone operation.
- ✅ **Icon libraries are pruned to Lucide and Tabler**, switched by the `icon-library/*` booleans in `Style`; the
  libraries we ruled out are deleted along with their pages. Which library is active is a per-mode value — read it.
- ✅ Contents: the full shadcn registry as component pages, the official and Pro block libraries, icon sets, text
  styles, effect styles, and the variable collections. **For current contents and counts, enumerate the file live via
  the Plugin API — do not trust any cached numbers in a doc.**

## 3. Token architecture (how the file resolves)

✅ Five variable collections — the kit's four plus ours. Color resolves through a **3-tier alias chain**, and the
semantic tier's names are shadcn's CSS variables 1:1:

**`Mode` (semantic, Light/Dark) → `Style` (per-style light/dark pairs) → `Tailwind` (raw primitives)**

| Collection | Modes | Role in code |
|---|---|---|
| `Tailwind` | single (`Value`) | Tailwind primitive scale — color ramps, spacing, radius, border/stroke/ring widths, breakpoints, opacity. Extended by us (`brand` §2, §4). |
| `Style` | `Luma-VECTO` · `Luma reference backup` | The style layer, and where branding lands: `color/{light,dark}/*`, `radius/*`, `font/family/*`, `font-weight/*`, `text/*`, `container/*`, `shadow/*`, per-component `component/*`, plus `pro-blocks/*`, `icon-library/*` and `meta/*`. |
| `Mode` | **Light / Dark** | shadcn semantic tokens — `background`, `primary`, `destructive`, `border`, `input`, `ring`, `card`, `chart-*`, `sidebar-*`. **`primary` ↔ `--primary` ↔ `bg-primary`.** |
| `Typeset` | 14 / 15 / 16 / 18px | The kit's long-form typography scale. Not used (§4). |
| `VECTO Responsive` *(ours — §5)* | Desktop · Desktop-wide · Mobile | Ours — numeric only, **no colour** (`brand` §4). Distinct from the kit's `custom/*` colour group. |

- ✅ Style-layer token paths take the shape `color/light/primary` — a flat `light`/`dark` split, with `custom/*` and
  `alpha/*` subgroups sitting beside the base tokens. Paths move between kit versions; enumerate before citing one.
- ✅ **`Mode` is set per frame, not only per page.** A section frame can carry an explicit `Mode` override and render
  opposite the page around it — the Figma half of the inverted-section contract (`f2c` §2a). Figma has no "opposite
  of the parent" concept, so an inverted section on a surface that ships both themes is drawn in both comps with the
  override set explicitly in each. Keep inversions rare: it is the loudest contrast move the system has, and nothing
  downstream enforces restraint.
- ✅ **Mode verification runs from the file's own base mode.** The pinned skill's `dark-check.js` duplicates a
  finished *light* frame to Dark; marketing comps here are dark-based, so the check runs the other way. The tell is
  the same in either direction: anything that doesn't move was hand-painted instead of bound to a variable.
- ✅ **Tints follow their base token automatically.** Under kit 3.0 most `custom/*` and `alpha/*` entries are
  aliases-with-opacity (an alias plus a percentage — not Figma variable expressions) pointing at a base token rather
  than stored colors, so hovers, washes, tints and focus rings restyle when their base changes. **Never flatten one to
  a literal** — that severs the link, which is the precise bug the 3.0 model removed. The exceptions — genuine
  literals, and stock tints aliasing a palette step directly — are found by reading value shapes, never from a list
  (`fig-map` §5).

## 4. What to keep vs. ignore in the file

- ✅ **Pro Blocks are not used** — not the block components, not their `pro-blocks/*` variables in `Style`, not their
  text styles. Quarantined, not deleted: leave them where they are.
- ✅ **The `Typeset` collection is not used.** Our own type roles replace it (`brand` §3).
- ✅ **Ignoring and deleting are different dispositions.** Ignore kit content we may yet want (Pro Blocks, Typeset);
  delete only what we have positively ruled out, as with the unused icon libraries (§2).

## 5. What we settle in Figma before transcribing (decided; spec to come)

📎 What has actually been built, customization by customization: `brand`. This section holds only the
rules our additions are authored under.

- ✅ **New colours are ramps in the `Tailwind` collection**, in a group of our own beside the stock
  `colors/*` families, named under the §6 rules. `Style` base tokens alias into them.
- ✅ **No baked-alpha primitives.** Translucent values are never pre-composited into a ramp. Opacity is
  expressed at the style layer as a base token plus a percentage (§3), so a translucent surface keeps
  following its base through every restyle instead of freezing one set of brand values into a primitive.
- ✅ **Brand colours the kit has no slot for** — glows, sheens, translucent surfaces — are authored the
  same way, as a `color/light|dark/*` pair in `Style` switched by a `Mode` token, in a group of our own.
- ✅ **Our numeric variables get a collection of their own** (`VECTO Responsive`), whose modes are the
  responsive axis; every value aliases a `Tailwind` or `Style` variable rather than storing a number.
- ✅ **Dark/light is authored as token modes** in `Mode` — never retrofitted later.

The exact token structure and the branded/semantic/translucent/glow/gradient definitions for code will
live in their own spec doc — **`tokens` (`front-end/tokens.md`), created when the spec is authored**
(seed material: `token-variant-spec-draft.md` in the project-root `explorations/` folder). Not defined
here.

## 6. The handoff (read-out contract)

Run at the start of the token phase, when authority passes from Figma to code (§1).

- ✅ **Figma is the source of truth for *values*; shadcn is the source of truth for *structure*.** Which
  tokens exist, what they are named, and how light/dark is expressed all come from shadcn. A transcription
  that invents a CSS token because Figma has a variable of that name has failed, however faithful it looks.
- ✅ **Enumerate via the full Plugin API** (§1) and read exactly these:
  - the base tokens in `color/light/*` and `color/dark/*` — the ones whose names match shadcn's CSS
    variables — collapsed into **one** CSS token per name, defined under `:root` and again under `.dark`.
  - `radius/lg` → `--radius`, **and only that one.** Code derives the rest of the scale itself; Figma's
    other seven radius variables are never transcribed (`fig-map` §6 has the arithmetic and why it bites).
  - `font/family/*` → the font variables.
  - our `vecto_colors` group → our ramps, 1:1. **Read the group's current contents; never match a fixed
    list.** Include entries that don't fit a tidy `<name>/<step>` pattern rather than dropping them.
  - our additions to stock `Tailwind` groups → nothing where Tailwind already generates the step, one `@theme`
    entry where it extends a scale (`fig-map` §8).
  - our `VECTO Responsive` collection → responsive utility recipes for spacing, layout and the type roles, plus a
    CSS variable only where `tokens` decides one is needed. Its Desktop · Desktop-wide · Mobile modes are read as
    samples at Tailwind breakpoints, not as breakpoints of their own (`fig-map` §8).
- ✅ **Emit no CSS variable for anything else:** `component/*`, `custom/*`, `alpha/*`, `text/*`,
  `font-weight/*`, `container/*`, `breakpoint/*`, `shadow/*`, `inset-shadow/*`, `drop-shadow/*`, `blur/*`,
  `focus-ring/*`, `pro-blocks/*`, `icon-library/*`, `meta/*`, and the whole `Typeset` collection. This list
  is the scope fence — a read-out pointed at the file without it emits tokens no component will consume.
  **Not emitting a group is not skipping it:** our own variables alias into several of these groups, so the
  read-out follows each alias to its number and emits only at our end (`fig-map` §8).
- ⚠️ **"No CSS variable" is not the same as "no meaning".** `custom/*` and `alpha/*` are packaged utility
  combinations, and they translate to utility strings on the component rather than to tokens; each carries
  its exact recipe in its own Figma description. The other groups above genuinely translate to nothing.
  **`fig-map` is the full divergence map** — the four classes, the Luma-specific recipe deviations, and the
  radius and colour-space traps. Read it before transcribing.
- ✅ **Color source split.** Default Tailwind palettes (slate, gray, zinc, neutral, stone, red, blue, …) install
  **directly from the Tailwind source** — do NOT clone or overwrite them from Figma. Only VECTO's own colors come
  from the file. So: defaults ← Tailwind repo; VECTO colors ← Figma, once.
- ✅ **No dashes (`-`) inside the segments of variables we author** (stock kit names keep theirs). Use `/` for hierarchy and `_` for word-join within a
  segment: on read-out both `/` and `-` collapse to `-` in CSS, so a dash inside a segment becomes
  indistinguishable from a hierarchy boundary and there is no delimiter swap that fixes it afterwards.
  - Good: `vecto_colors/red/500`, `vecto_colors/red_alpha/5`
  - Bad: `vecto_colors/red-alpha/500`
- ✅ **The read-out is runnable, so run it as the handoff check.** Generate from the contract above and diff against
  the committed CSS; a difference is either an intended change or a transcription error. After the handoff there is
  no parity to keep, so the diff has no standing role.
