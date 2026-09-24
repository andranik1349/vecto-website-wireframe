# VECTO — the brand layer on shadcn / Luma

**Purpose.** What VECTO has changed or added on top of shadcn's Luma style, each in a few lines: what it
is, which established convention it extends, and where it lives. **Doc-key: `brand` · Species: living
reference.**

**Scope.** Descriptions only. How each customization translates to CSS lives in `fig-map` (cited per
entry); how the file's variables resolve lives in `fig-conv`; building it in code is Claude Code's, via
briefs (DL-20). Corpus map: `docs/README.md`.

**Status legend.** ✅ established · 🔧 built, still being tuned · 📎 reference/context.

---

## 1. How the layer is built

- ✅ **Luma is the substrate; the brand is applied on top** (DL-01). Every customization extends a
  shadcn, Tailwind or kit convention in that convention's own pattern — a new variant in the existing
  variant property, a token in the existing alias chain, a text style in the kit's own naming — never a
  parallel system beside it.
- ✅ **Authored under `fig-conv` §5's rules** — new colours as ramps, translucent ones as a base token
  plus a percentage, our numbers in `VECTO Responsive` — so a rebrand carries every entry below.
- ✅ **Finding our changes in the file:** diff `Style`'s `Luma-VECTO` column against `Luma reference
  backup` (the pristine kit values); variables we added or re-pointed carry a description naming the
  change and the utility it stands for. Our own groups are named `vecto…` / `VECTO …`.

## 2. Colour

- 🔧 **`vecto_colors` ramps** — neutral, red and cyan 50–950 plus `error`, extending the `Tailwind`
  collection beside the stock families. The neutral is VECTO's cool "lit darkness" grey; red carries
  the `#ca1d00` accent; cyan is the focus colour. Some steps are anchors from the old VECTO file, the rest
  generated in OKLCH and still open to tuning by eye. Translation: `fig-map` §8, §6.
- ✅ **shadcn's semantic slots re-pointed at those ramps** — `background`, `primary`, `ring` and the rest
  keep shadcn's names and roles; only their targets changed. The site is dark-based, so the dark column
  is the primary design surface. Translation: `fig-map` §3.
- ✅ **Dark `ring` is a solid cyan**, and the kit tints that skipped it (focus rings, one muted wash) now
  follow their base token. Why and how to spot the pattern: `fig-map` §5.
- ✅ **Muted is alpha-based** — `muted-foreground` is `foreground` at 64% and `muted` is `foreground` at a
  low percentage, so dimmed text and washes take on whatever surface sits beneath them (cards, glass,
  imagery) instead of painting a flat grey. shadcn's names and roles are unchanged, and `muted` stays a
  wash that sits on a surface — never a surface itself. The kit tints built on `muted` were re-pointed to
  keep rendering correctly (`fig-map` §5). Translation: `fig-map` §3.
- 🔧 **A surface ladder** — shadcn ships `background`, `card` and `popover` as one colour; ours step
  apart so UI layers separate by depth: light `neutral/100` → `neutral/50` → white, dark `neutral/950`
  → `neutral/900` → `neutral/800`. Translation: `fig-map` §3.
- 🔧 **Muted is a backdrop, accent is interaction** — `muted` marks a passive area on a surface (tracks,
  wells, table header and footer, field fill); `accent` appears only because something is hovered,
  focused, open, selected or on. Luma split interactive states between the two by component; ours route
  every interactive state to accent. Accent is a VECTO-red wash in two strengths: `accent` for momentary
  states (hover, focus, open) and our `vecto/accent_strong` for lasting ones (selected, on). Both alias
  `red/500` directly in both themes, with slightly higher opacities in dark; deeper reds turned brown at
  low opacity over the dark neutrals, which contrast maths does not catch, so these were set by eye in the
  comp. Text on them stays the plain foreground. `sidebar-accent` uses the same recipe (dark currently at
  16% against `accent`'s 14% — open: align or keep). Translation:
  `fig-map` §3, §8.
- ✅ **Secondary is inverted and carries the brand red** — `secondary` takes the palette step
  `foreground` uses (white in dark, near-black in light) and its text is VECTO red, a shade lighter in
  light mode, so buttons read as black, red and white whichever way round — the high-contrast alternative
  to `primary` rather than a grey lost in the surface ladder. Both alias the palette directly, not the
  foreground/background tokens. Its hover is `primary`'s opacity recipe eased to `secondary` at 90%,
  replacing the kit's flat literal, so the red label keeps AA contrast at rest and on hover. Translation:
  `fig-map` §3, §5.
- 🔧 **Borders are opacity-based in both themes** — light `border` and `sidebar-border` mirror dark's
  (the foreground's palette step — 10% in dark, 12% in light), so a border reads the same on background,
  card and popover instead of vanishing on one and shouting on another. `input` works the same way (15% in
  both themes). The kit tints built on either were re-pointed to keep rendering correctly (`fig-map` §5).
  Translation: `fig-map` §3.
- ✅ **Fields have a visible resting outline** — Luma draws inputs, textareas, selects and combobox
  triggers borderless; ours use shadcn's standard `border-input`, the way six of the kit's eight styles
  and Luma's own OTP input already do, so a form reads as fillable before anyone focuses it. Focus still
  swaps in the ring. Translation: `fig-map` §9.
- ✅ **Shadows never show through translucent areas** — Figma's "show behind transparent areas" is off
  on every shadow in the file (the kit ships it on), so glass and translucent surfaces render as a
  browser will. Why: `fig-map` §4.

## 3. Shape and type

- ✅ **Radius base 12** (Luma ships 10), with the rest of the ramp derived by shadcn's multipliers.
  Translation: `fig-map` §6.
- ✅ **Typeface: Google Sans Flex**, set once in `font/family/*`. Multilingual strategy and optical
  sizing: `f2c` §3 (seed: `explorations/font-strategy.md`).
- 🔧 **Functional type roles instead of the stock `xs`–`9xl` picker** — titles (display, page, section,
  subsection, card), body (lead, default, small) and caption, each with a default and a strong weight
  (plus a caption eyebrow). Sizes follow Luma's Tailwind logic: titles step up across breakpoints the way
  Luma's own marketing headings do, and every role below them steps up one Tailwind step at the wide
  breakpoint — reading columns widen on large screens rather than sitting narrow and centred in empty
  space, so body copy grows with them to keep a comfortable line length. UI text inside components
  (buttons, fields, menus) keeps its own fixed size; where a tight card misbehaves as its text scales,
  that text swaps to a stock Tailwind size instead of a role. Weights are per-role knobs awaiting a
  tuning pass. They live as `vecto/*` text styles on top of `VECTO Responsive` variables. Translation:
  `fig-map` §8.
- ✅ **Tailwind's default line-heights at `text-3xl` / `text-4xl`**, where stock Luma is looser. Why:
  `fig-map` §4.

## 4. Responsive layer and scale extensions

- ✅ **`VECTO Responsive` collection** — our spacing, layout and type-role values across Desktop ·
  Desktop-wide · Mobile, every value an alias into Tailwind or the style layer. How the modes map to
  breakpoints: `fig-map` §8.
- ✅ **Tailwind scale additions** — spacing steps Tailwind generates anyway, and one step past the end
  of a scale (`max-w-8xl`, 1536px) for the wide content width. Translation: `fig-map` §8.

## 5. Components

- 🔧 **Buttons and fields sized for selling, not for dashboards.** Default Button and every field
  (input, input group, select, combobox trigger) share a 48px height; Button `lg` is 56px; field and
  button text moves up to `base` (`lg` on the large button), which also keeps iOS from zooming form
  fields. `xs` and `sm` buttons, labels, helper text and menu items keep Luma's sizes. Built by
  re-pointing the kit's own size variables to larger Tailwind steps. Open: `lg` at 64, a taller textarea.
  Translation: `fig-map` §9.
- 🔧 **Button `cta` variant** — the branded call-to-action: `primary` with a subtle top sheen, a glow in
  the brand colour, a 1px inner highlight, and optional translucent icon pods in the existing left/right
  icon slots. A variant beside shadcn's own, not a separate button, and used at `default` and `lg` only —
  the effect smears at smaller sizes. Built on the `vecto/*` colour tokens and `vecto/*` effect styles.
  Open: glow strength, and the magnetic hover, which exists only in code. Translation: `fig-map` §8, §9.
- 🔧 **`Navbar` — the site's top navigation** — a new component, since shadcn ships dashboard headers but
  no site navigation. Desktop `hero` (clear, over the hero) and `scrolled` (glass); mobile `closed`
  (logo, CTA, menu button — the CTA stays in the header per `ia`) and `open` (a glass drawer). Built only
  from kit parts: the menus are `NavigationMenu / Button`, the CTA is Button `cta`, the menu button a
  ghost icon Button. Menu order and dropdown-vs-link follow `ia` §"Primary navigation architecture".
  `Show Language` (off until a second language publishes) and `Show Theme Switch` (off on the main site)
  hide the utility controls. Height and side padding come from `VECTO Responsive`. Ported from the HES
  navigation. Open: at Tailwind's `lg` width (1024px) the seven menus do not fit one row.
  Translation: `fig-map` §9.
- ✅ **`NavigationMenu / Button` gains Open and Active** — the kit drew "hover" as the open menu; ours
  separates them the way shadcn's code does: Hover is the highlight only, Open adds the panel and flips
  the chevron, and Link gets Active for the current page (`vecto/accent_strong`). Translation: `fig-map`
  §9.
- ✅ **`Theme Switch`** — a light/dark toggle wrapping a Button (outline, icon-sm) with a sun or moon.
  Kit-level; the main site is dark-only and hides it. Translation: `fig-map` §9.
- ✅ **The logo follows the theme** — its dark parts bind to `foreground` (they sat on
  `accent-foreground`), its red mark to `primary`.
- 🔧 **Tabs get a `Size` axis** — `default` is the stock compact control (admin density); `lg` is sized
  to sell: a 48px active pill (the default Button's height), base text, 20px icons, in a 56px track whose
  radius stays concentric. On both the track (`Tabs`) and its segments (`Tabs / Trigger`), every
  variant and orientation, built on `component/tabs/size-lg/*` in the kit's own size-variable pattern.
  Open: the active pill fills with `background`, which sits below `card` on the surface ladder, so on a
  card the selected pill reads sunken rather than lifted. Translation: `fig-map` §9.
- ✅ **Dialog and Sheet close with a real Button** — the corner ✕ is an icon-only Button (`ghost`,
  `icon-sm`), not the kit's separate close-icon component with its own size and radius, so it can no longer
  drift from Button. This matches shadcn's current style bases (the older `new-york-v4` registry still
  ships the ad-hoc version, so code should build on the style base). Translation: `fig-map` §9.
- 🔧 **Card `Surface=glass`** — a translucent card: the card colour at about 72% over a background blur,
  with a lit rim (white in light, a faint foreground line in dark) and the inner highlight. A value of a
  new `Surface` property on shadcn's Card (`solid` is the stock card), not a separate component, and a
  surface in its own right — distinct from `muted`. Built on the `vecto/card_glass*` tokens and the
  `vecto/glass` effect style. The kit's footer strip paints an opaque card fill of its own, so on glass
  that fill is cleared and only its divider line stays. Open: blur strength and tint by eye. Translation:
  `fig-map` §8, §9.
