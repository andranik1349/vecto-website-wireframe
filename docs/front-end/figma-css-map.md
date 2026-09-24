# VECTO — Figma ↔ CSS divergence map

**Purpose.** Where this Figma file's variables and shadcn's CSS disagree, and how each class of
disagreement translates. Read before transcribing the sketchpad (`fig-conv` §6) and before taking any
value off a kit component. **Doc-key: `fig-map` · Species: living reference.**

**Scope.** The translation itself. What to read and what to skip lives in `fig-conv` §6; code-side
rules in `f2c`; rationale in the decision log by ID. Corpus map: `docs/README.md`.

**Provenance.** Every structural claim below was read from the file with the Plugin API, not taken
from the kit vendor's documentation or the pinned skills — both of which are wrong about this file in
specific ways (§10). Re-verify before trusting any of it: the file is live and being edited.

**Status legend.** ✅ established · 🔧 decided in principle, spec pending · 📎 reference/context.

---

## 1. The one rule, and how to classify

✅ **Figma holds the values; shadcn holds the structure.** Which tokens exist, what they are named and
how light/dark is expressed are shadcn's to decide. Figma's variable names are not a schema — many
exist only because Figma models something differently, and transcribing them literally produces tokens
no component reads.

✅ Classify before translating. The class decides the treatment, and only Class A is emitted as-is: B
changes form (sometimes a token, often nothing), C is nothing until adopted, D is always nothing.

| Class | What it is | Treatment |
|---|---|---|
| **A · Mirrors** | Same concept, same name, both systems | Emit as a CSS token |
| **B · Mechanics** | Figma modelling something CSS expresses differently | Translate to the CSS form |
| **C · Kit extras** | Kit inventions with no shadcn counterpart | Ours only by decision — then a token we own |
| **D · Internals** | Kit plumbing with no CSS role here | Emit nothing |

## 2. What is actually in the file

✅ **Five variable collections**, not the four the vendor documents — the fifth is ours.

| Collection | Modes | Role | Class |
|---|---|---|---|
| `Tailwind` | `Value` | Palette and utility primitives, plus our own `vecto_colors` ramps and scale additions | ours (§8) / B (stock — §4, §6) |
| `Style` | `Luma-VECTO` · `Luma reference backup` | Theme source, type scale, radius ramp, shadows, per-component values | mixed |
| `Mode` | `Light` · `Dark` | The semantic switch designs bind to | A — emitted via `Style`'s base tokens (§3) |
| `Typeset` | `14px` · `15px` · `16px` · `18px` | The kit's long-form prose scale | D (opted out — §9) |
| `VECTO Responsive` | `Desktop` · `Desktop-wide` · `Mobile` | **Ours** (`brand` §4) — every value an alias into `Tailwind` or `Style`; **no colour** | ours (§8) |

✅ **`Mode` holds no values at all** — every one of its variables is a plain alias, verified across the
collection. Most alias their own `color/light|dark/*` pair; a few alias a *different* Mode token
because what they equal genuinely differs by theme. It is a switch, not a tier to transcribe.

📎 **`custom/*` throughout this doc means the kit's colour group** — tokens inside `Style`'s
`color/light|dark/` layer, mirrored in `Mode`. It is unrelated to `VECTO Responsive`, which holds no
colour at all.

## 3. Class A — the mirrors

✅ **The base semantic set matches shadcn exactly.** The names under `color/light/*` and `color/dark/*`
outside the `custom/` and `alpha/` subgroups are name-identical to shadcn's documented token set —
diffed in both directions, nothing unmatched either way. This is the part that translates without
thought, and it is most of what the read-out emits.

✅ **The light/dark split is a Figma mechanic, not two tokens.** A Figma variable carries one value per
mode of *its own* collection, and the light/dark axis lives in `Mode` — so the Style layer needs
`color/light/primary` and `color/dark/primary` as separate variables. In CSS that is **one token
defined twice**, under `:root` and again under `.dark`. Emitting `--primary-light` / `--primary-dark`
is the likeliest transcription error and shadcn components read neither.

⚠️ **Some base tokens carry opacity, and it is load-bearing.** Several dark-column base tokens are an
alias *plus a percentage*, not a solid colour — find them by value shape (`{ color, opacity }`), not by
name. Resolve each to `color-mix()` or an `oklch(… / <alpha>)` value — flattening to an opaque hex
changes the rendering.

## 4. Class B — mechanics, and what each becomes

| Figma does this | Because | In CSS it is |
|---|---|---|
| `custom/*` tokens | shadcn has no such token — the value is a *utility combination* | The utility string on the component (§5) |
| `alpha/*` tokens | Same, for constant-alpha overlays | An opacity modifier on the base fill |
| `ring-offset` in `Mode` — Mode-only: it aliases the `background` base pair, and `Style` has no `ring-offset` of its own | Figma needs a colour for the ring's gap | Nothing — shadcn v4 ships no ring-offset token |
| Eight independent `radius/*` numbers | Figma variables have no arithmetic | One `--radius`; CSS derives the scale (§6) |
| `text/{step}/lh` in pixels | Figma rejects unitless and percentage values | Nothing extra — each `text-*` utility already carries its paired line-height |
| `text/{step}/lh-tight…lh-loose` in pixels | Same | Tailwind's `leading-*` steps |
| Palette as sRGB hex | Figma has no OKLCH support | `oklch(…)`, as shadcn authors it (§6) |
| `spacing/*` as fixed pixels | No arithmetic, so no `calc()` | Tailwind's spacing scale — `spacing/4` is `p-4` |
| A drop shadow's "show behind transparent areas" | A Figma-only rendering option | Nothing — a CSS outer `box-shadow` is always clipped beneath its own box. Keep it off in the file so Figma renders as the browser does |

⚠️ **Stock Luma's `text/3xl/lh` and `text/4xl/lh` are off Tailwind** — 1.5× the size, where Tailwind v4
pairs `text-3xl` and `text-4xl` with tighter defaults (our correction: `brand` §3). Take line-heights from
Tailwind, never from a Luma column.

## 5. Class B in detail — `custom/*` is translated, never emitted

✅ **The mechanism is Figma's native alias-with-opacity**, stored as a colour whose value is
`{ color: <alias>, opacity: <percent> }`. It is *not* a `VARIABLE_EXPRESSION` / `COMPOSE_COLOR`
expression — this file contains none of those anywhere (§10). The practical consequence is the same
either way: re-point a base token and every tint on it follows, with nothing to recompute.

✅ **Each `custom/*` token packages a utility combination**, not a colour. shadcn builds states and
surfaces from utility strings — a disabled field is `disabled:bg-input/50 dark:disabled:bg-input/80` —
and the kit wraps each combination in one bindable variable so a designer needn't reproduce it. The CSS
equivalent is that utility string, applied on the component. A shadcn project has no `--field-disabled`,
and adding one puts us off the canonical token set for nothing.

✅ **The recipe lives in each variable's own Figma description**, which carries a `DERIVED FROM:` line
naming the shadcn source file and exact utility string, or `KIT EXTRA` where no derivation exists
(Class C). Read the description. Do not infer from the name, and **do not use the vendor's published
recipe table — it documents Nova and we are on Luma.**

⚠️ **Where Luma's resolved values contradict the published table.** Taken from our file, not the docs:

| Token | Published (Nova) | This file (Luma) |
|---|---|---|
| light `custom/field` | `dark:bg-input/30`, transparent in light | `input` at 50% — the field *is* filled in light |
| dark `custom/field` | `input/30` | `colors/white` at 8% |
| `custom/field-border` | `border-input` | aliases `colors/transparent`, both modes — Luma fields are borderless at rest |
| `custom/focus-ring` | `ring/50`, `/30` only for Mira and Sera | **`ring` at 30%** in light (both columns); in stock dark (the backup column) it skips `ring` for a palette step (below) — the description's per-style note matches neither |

✅ **A few `custom/*` tokens are flat literals with no base to follow, and they are the only ones a
re-brand has to recompute by hand.** Find them rather than trusting a list: scan the colour layer for
values carrying an `r` key, which is what separates a stored colour from an alias or an
alias-with-opacity. Where one has a base it plainly should follow, re-express it as that base plus a
percentage so it stops needing hand recomputation (ours: `brand` §2); compare `Luma-VECTO` with the
backup to see which the brand pass has reached. The apply-brand skill's list of them is the stock kit's,
not this file's.

✅ **A few stock dark tints skip their base token and alias a palette step directly**, so they would not
follow a re-brand either. The cause is a Figma limit: stock dark `ring` is itself an alias-with-opacity,
and Figma accepts a tint of a tint but resolves it to the *inner* opacity alone — the outer percentage is
silently dropped (checked with `resolveForConsumer`) — so the kit pointed the tint at the palette instead.
CSS has no such limit (`color-mix()` composes), so this constrains the Figma file only: **never alias a
tint onto a base token that already carries an opacity.** Where a base gains one, its tints are
re-pointed at that base's own target with the opacities multiplied (ours: `brand` §2). Find
them by scanning `custom/*` and `alpha/*` for aliases whose target is a `colors/*` step — the amber
`warning-*` set does this deliberately (Class C) and stays. What we re-pointed: `brand` §2.

⚠️ A flat literal can carry its own alpha (dark `destructive-ring` is 40%). That is a different thing
from an alias-with-opacity and resolves differently: the alpha is baked into the stored colour and
follows nothing.

⚠️ One `custom/*` token ships with no description, so its recipe cannot be read from the file. Treat an
undescribed token as unresolved and find the component that binds it rather than guessing.

## 6. The two silent-corruption traps

⚠️ **Radius arithmetic.** shadcn derives the whole scale from one `--radius`: `sm` ×0.6, `md` ×0.8,
`lg` ×1, `xl` ×1.4, `2xl` ×1.8, `3xl` ×2.2, `4xl` ×2.6. Figma stores eight independent numbers, and the
pinned apply-brand skill tells you to derive them **additively** (base−4, base−2, base+4, +8/+12/+16).
The two agree only at a base of 10 — the stock Luma value, which is why the error hides. **Transcribe
`radius/lg` only** and let CSS derive the rest. To check the file at any time: every step should equal
`radius/lg` × its multiplier, with `radius/xs` outside the ramp.

⚠️ **Colour space.** Figma stores each palette step as the sRGB hex of Tailwind v4's OKLCH definition
(spot-checked: `colors/red/500` is `#fb2c36`, matching Tailwind v4). Transcribing that hex into a file
shadcn authors in OKLCH loses the definition. For Tailwind steps take the value from Tailwind; for
**our `vecto_colors` ramps**, which exist in no palette, convert hex → OKLCH deliberately and record
that the conversion happened.

## 7. Class C — kit extras

✅ Tokens whose description reads `KIT EXTRA` have **no shadcn derivation** — the kit invented them for
something shadcn expresses differently or does not ship. Warning colours are the clearest case: shadcn
has no warning token, so the kit supplies amber values.

✅ **A kit extra is not automatically ours.** Adopting one makes it a token we define and own, added the
way shadcn documents adding tokens — declared under `:root` and `.dark`, exposed through `@theme
inline` — and it belongs in the token spec (`tokens`, when authored), not smuggled in as a kit artifact.
Not adopting it means it translates to nothing.

## 8. Our own layers

✅ **Our layers sit outside the four classes, which sort *kit* content.** Each has its own treatment below.

✅ **`vecto_colors`** (inside `Tailwind`): transcribed 1:1 as our ramps, converted hex → OKLCH per §6.

✅ **The `vecto/*` colour group** (a `color/light|dark/vecto/*` pair in `Style`, switched by `Mode`
`vecto/*`; what it holds: `brand` §5). Every entry is an alias-with-opacity on a base token or
`colors/white`, so none is a new colour: each becomes a named utility reading its base (`bg-gloss`,
`shadow-glow`, `shadow-inset-hi`) or into a component part's styles (`ButtonIcon`), and each token's description names its utility.
The one exception is `vecto/accent_strong`: a semantic colour components select by name, so it becomes a
token beside `--accent` (`--accent-strong`, defined under `:root` and `.dark`, exposed through `@theme
inline`, the way shadcn documents adding tokens). The `vecto/*` effect styles are
those shadows' geometry; only their colours are bound, and each style becomes one shadow utility.

✅ **Additions to stock `Tailwind` groups come in two kinds**, told apart by diffing the group against
Tailwind v4's default theme:
- **A step Tailwind generates on its own** — v4 spacing accepts any multiple of its 0.25rem base, so a
  `spacing/18` Figma lacked is plain `p-18`. Emit nothing.
- **A step past the end of a Tailwind scale** — `max-width/max-w-8xl`, aliasing `Style` `container/8xl`.
  Ours, so adopted by definition: one `@theme` entry (`--container-8xl`; `@theme` is
  Tailwind v4's CSS block for defining new utility values) so the `max-w-8xl` utility exists, and a line in
  `tokens`. Its `container/8xl` target stays on the no-emit list; the entry is keyed off the addition.

✅ **`VECTO Responsive` holds no values of its own — resolve through, never emit the path.** Each
variable aliases `Tailwind` or `Style`; follow the alias for the number, and leave the groups it passes
through (`text/*`, `font-weight/*`, `container/*`) on `fig-conv` §6's no-emit list.

✅ **Its modes are sample points, not breakpoints.** Mobile ≈ unprefixed (Tailwind is mobile-first: an
unprefixed utility applies at every width until a prefix overrides it), Desktop ≈ `lg:`, Desktop-wide ≈
`2xl:` — at Tailwind's own `lg` / `2xl` widths, which the file's `breakpoint/*` variables mirror (if they
ever differ, Tailwind wins). Translate to Tailwind's own breakpoints; never
mint breakpoints from mode names. A value identical in all three modes is just its Tailwind utility; one
that varies becomes a **responsive recipe** — a prefixed utility string such as `py-12 lg:py-16`, applied
where the value is used.

✅ **A type role (`brand` §3) translates as one unit.** It is the triple `text_size/<role>` +
`line_height/<role>` + `font_weight/<role>_<default|strong>`. Each size variable's description carries its utility
recipe (`text-5xl lg:text-6xl 2xl:text-7xl` shape); the line-height is the one that size already pairs
with, so no `leading-*` is emitted; the weight knobs resolve to `font-weight/*` steps, i.e. `font-*`
utilities. 🔧 Stepped recipes versus a fluid `clamp()` between a role's Mobile and Desktop-wide values
is a `tokens` decision (`clamp()` scales a value smoothly with viewport width between a minimum and a
maximum, instead of jumping at breakpoints). `tokens` is planned, not yet written (`docs/README.md`).

✅ **The `vecto/*` text styles are Figma conveniences built from those variables.** Their descriptions
restate the recipe for whoever is designing; they produce no CSS — text styles are never read out.

## 9. Class D — internals

✅ `component/*`, `pro-blocks/*`, `icon-library/*` and `meta/*` produce no CSS. `component/*` is the
largest group in the file and the most tempting to transcribe: it exists because Figma has no equivalent
of a class recipe, so every per-style value needs its own variable. Its colour entries are pure aliases
into `Mode`. Its numeric entries mostly alias a `Tailwind` step, so each reads directly as a utility
(`→ spacing/12` is `h-12`); the few stored as raw numbers are worth a look, because they mark where the
kit left the 4px grid or holds a value no utility names.

✅ **A `component/*` edit of ours is a sketch of a `cva` change, not a token.** Where we resize a
component in Figma (ours: `brand` §5), the edit re-points `component/*`
variables to other `Tailwind` steps and, where text size changes, swaps the variant's text style —
the kit binds component text straight to `text/*`, so a new size gets its own `component/*` text style
in the kit's own pattern (`component/button-xs` → `component/button-md`, `-lg`). Finding them:
`brand` §1. In code the result lands in the component's `cva` size variants, never as CSS
variables. A variant we add follows the same rule: Button's `cta` (its `component/button/variant-cta/*`
bindings, label padding and icon pods) describes one new `cta` entry in the `cva` variants, limited to
the sizes `brand` §5 names, plus a `ButtonIcon` part for the pods. Card's `Surface=glass` likewise
describes a `surface` variant on Card (`solid` the default), with the footer's own background dropped
in the glass case. The Dialog/Sheet close swap (`brand` §5) needs no code change at all: shadcn's style
bases already render that close as `<Button variant="ghost" size="icon-sm">`; only the older
`new-york-v4` registry has the ad-hoc version, and the kit's `component/dialog|sheet/close-*` variables
it leaves behind are unbound and emit nothing. `Navbar` and `Theme Switch` are compositions, not tokens:
in code they are components assembled from NavigationMenu and Button, with the navbar's surface taken
from the `vecto/card_glass*` tokens. NavigationMenu's added states are the ones shadcn already styles:
Open is `data-[state=open]`, Active is `aria-current` / `data-active`.

⚠️ **`Typeset` is Class D by our decision, not by nature.** It mirrors shadcn's own `typeset.css`, which
is real and shipping — so it *does* have a CSS counterpart, unlike the rest of this section. We have
opted out (`fig-conv` §4). If that reverses, note the divergence: shadcn's typeset derives everything
from three controls (`--typeset-size`, `--typeset-leading`, `--typeset-flow`) while the Figma collection
pre-computes every heading size and spacing step per mode — so the translation is to the three controls,
never a step-by-step transcription.

## 10. Where the skills and vendor docs are wrong about this file

📎 Recorded because each was believed and acted on during authoring, and each is checkable.

- **The `COMPOSE_COLOR` expression shape.** The pinned apply-brand skill states that kit 3.0 stores
  tints as `{type:'VARIABLE_EXPRESSION', expressionFunction:'COMPOSE_COLOR', …}`. This file contains no
  variable expressions at all; tints are `{ color: <alias>, opacity: <percent> }`. Any script written
  against the expression shape will fail to recognise a tint and misclassify it as a literal.
- **"Shadow colours are literal black at an opacity."** Most are literals, but a meaningful minority are
  aliases. Classify them, don't assume — though it matters only if shadows are ever adopted as tokens;
  today `shadow/*` is on `fig-conv` §6's no-emit list.
- **The vendor's per-token recipe table documents Nova.** Four Luma values contradict it (§5).
- **`helpers.js` hardcodes Lucide.** The pinned script's `setIcon` targets the `Lucide Icon#…` swap
  property, but this file runs **Tabler**. Calling it swaps a hidden instance and changes nothing
  visible.

## 11. Keeping the sketchpad translatable

- ✅ **Bind `Mode` tokens; never `Style` or `Tailwind` variables directly.** Mode carries shadcn's exact
  CSS names, so anything bound to it has an obvious counterpart.
- ✅ **Never enter a raw colour anywhere in the chain.** A colour absent from the palette gets added to
  `Tailwind` first and aliased from there — which is how `vecto_colors` is structured.
- ✅ **Express a tint as an alias with opacity, never a flattened hex.** A flattened tint stops following
  its base, breaking both the Figma restyle and the translation to an opacity modifier.
- ✅ **Prefer a `custom/*` token over stacking an `alpha/*` overlay** where one exists — a `custom/*`
  token translates to a named recipe, a stacked overlay has to be reverse-engineered.

## 12. Verifying a transcription

- ✅ **Generate, then diff — at handoff.** The read-out contract (`fig-conv` §6) is runnable: generate from it and
  diff against the committed CSS. Any difference is an intended change or a transcription error.
- ✅ **Check the emitted token set against shadcn's, not against Figma's.** A transcription that produced
  `--primary-light`, `--field-disabled`, `--ring-offset`, or a `--radius-*` per step emitted Figma's
  structure instead of shadcn's — the failure this doc exists to prevent.
- ✅ **Classify by value shape, not by name.** A checker that only recognises `VARIABLE_ALIAS` will report
  every tint in the file as a literal (§10).
- ✅ **Judge the rendered result.** `/styleguide` (`f2c` §5) is where a transcription is accepted — real
  renderer, real font, real colour space.
