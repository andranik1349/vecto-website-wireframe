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
  keep shadcn's names and roles; only their targets changed. The site ships both themes and opens in dark
  (`f2c` §2a), so both columns are design surfaces, dark first. Translation: `fig-map` §3.
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
  comp. Text on them stays the plain foreground. `sidebar-accent` equals `accent` in both themes, as in
  stock shadcn. The calendar follows the same split: the "today" marker is
  a passive marker, so `muted`; the band between two selected dates is a lasting selection, so
  `vecto/accent_strong` (stock uses `accent` for both). Accent is only ever a background: the kit's collapsed-sidebar tooltips borrowed the
  `sidebar-accent` pair inverted (text in `sidebar-accent`), which only worked while that was an opaque
  grey; they now use the Tooltip's own pair (`foreground` fill, `background` text), as shadcn's collapsed
  sidebar renders the standard Tooltip. Translation: `fig-map` §3, §8.
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
- ✅ **No colour is a hand-typed value** — the kit's last stored colours (dark `custom/destructive-ring`,
  dark `custom/tinted`, both `custom/tinted-hover`) now follow a base like every other tint: the ring is
  `destructive` at 40% (as light already was), dark `tinted` aliases `border` (as light already did), and
  `tinted-hover` is the border's palette step a notch stronger (18% light, 15% dark). Shadow colours follow
  `neutral/950` too (next entry). How to check none remain: `fig-map` §5.
- ✅ **Fields have a visible resting outline** — Luma draws inputs, textareas, selects and combobox
  triggers borderless; ours use shadcn's standard `border-input`, the way six of the kit's eight styles
  and Luma's own OTP input already do, so a form reads as fillable before anyone focuses it. Focus still
  swaps in the ring. Translation: `fig-map` §9.
- 🔧 **`vecto/scrim` — dims whatever is underneath** — untinted black (`colors/black`) at 16% in light and
  24% in dark. The kit's `alpha/*` steps are built on `background`, so they turn white in light mode and
  lighten rather than dim; the scrim darkens in both themes. Modal backdrops (sheets, drawers, dialogs)
  keep the kit's own `custom/overlay`, black at 30% in both themes; it is unchanged except that we scoped it
  to fills so it shows in pickers — the kit hides every `custom/*` token. Open: strengths by eye. Translation:
  `bg-black/16 dark:bg-black/24`, a utility pair rather than a CSS variable (`fig-map` §8).
- 🔧 **Softer, cool-tinted shadows** — the stock scale (Tailwind's `shadow-*`) drops a fairly dark,
  short shadow that reads as a grey lip under the edge. Ours keeps the scale's names and two-layer shape
  but re-values every size (`2xs`–`2xl`): a tight, faint contact shadow plus a wide, soft ambient one with
  a strong negative spread, so a raised layer reads as lifted rather than outlined — the approach Vercel's
  Geist and Radix Themes take, with the border doing the edge-definition. Colours are `neutral/950` (the
  cool near-black) at 5–20% instead of pure black, so shadows share the palette's hue. Every component
  shadow (surface, popover, overlay, the glass) aliases this scale and follows it; the stock chart
  tooltip's own literal values now alias the popover recipe. In dark mode shadows barely register, by
  design: there depth comes from the surface ladder and borders. Open: strengths by eye. Translation:
  `fig-conv` §6, `fig-map` §10.
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
  (logo, CTA, menu button) and `open` (a glass drawer: logo, utility controls and close in the top bar, the
  menu list, then the CTA full width at the foot). CTA placement per `ia` §Localization. Built only
  from kit parts: the menus are `NavigationMenu / Button`, the CTA is Button `cta`, the menu button a
  ghost icon Button. Menu order and dropdown-vs-link follow `ia` §"Primary navigation architecture".
  `Show Language` (off until a second language publishes) and `Show Theme Switch` (on: the site ships both
  themes) toggle the utility controls, leaving no gap. Height and side padding come from `VECTO Responsive`. Ported
  from the HES navigation. **The desktop bar starts at Tailwind's `xl` (1280px)**; below that the mobile
  bar and drawer are used, because logo, seven menus and CTA need about 1,150px and `lg` (1024px) leaves
  about 900. Open: the Resources and About dropdowns, and the language dropdown list, are not drawn
  yet. Translation: `fig-map` §9.
- 🔧 **Menus are built from two parts: a column header and a menu link.** Every megamenu and dropdown in
  the prototype (`_nav.html`) reduces to these two, so there is no per-panel component vocabulary.
  - **`NavigationMenu / Column Header`** (new) — `Type=Label` is a grouping label with no page behind it
    (a service stage, "By company stage", "Reference"); `Type=Link` is a header that is itself a
    destination ("By industry", "Our Process"), with `State=Default | Hover`. Both types share one look —
    small uppercase, the new `component/navigation-menu-label` text style — so a row of headers stays
    level; a link header is set apart by foreground text (labels are muted), a trailing arrow, and the
    accent wash on hover. The prototype marks it with accent-red text instead; our red measures 2.8:1 on
    the dark card, under the 4.5:1 small text needs, and colour alone should not be what marks a link.
    `Show Description` adds the tagline some headers carry. Which type a header gets follows the heading
    convention in `ia` §"Primary navigation architecture".
  - **The kit's `NavigationMenu / Menu Link` gains three things**: `Type=Emphasized` (semibold, for the
    parent service leading its group — the same row as its siblings, as the prototype's bold first link
    is), `State=Active` for the current page (`vecto/accent_strong`, like `NavigationMenu / Button`'s
    Active), and `Show Arrow`, a trailing arrow for links to an index page. Translation: `fig-map` §9.
- 🔧 **The megamenu panels** — `Navbar / Megamenu · Services`, `· Who We Serve` and `· How We Work`, full
  width under the scrolled navbar on the same glass, each following its prototype panel. Shared calls:
  every column is header, separator, then its links in their own group, so a column reads as a labelled
  block; link rows are compact (32px single-line, the kit's menu link with its vertical padding at `spacing/1-5`,
  or `spacing/2` for title-plus-description rows) so panels fit under the navbar on a laptop; each ends
  in an optional footer link (`Show Footer`), with the prototype's duplicate Get an Estimate buttons
  dropped because the navbar CTA is always visible. Services adds three more: the AI Transformation band
  is a quiet banner (a foreground wash with a border, a red-rimmed sparkles pod, the inverted `secondary`
  Button as its affordance) rather than a red block, so the navbar CTA stays the only red-filled action;
  Scale and Maintain share one column, giving five columns wide enough to read at 1280px; and it is the
  one panel tall enough to test fit — it clears a 1280×720 viewport (a 1280×800 laptop minus browser
  chrome) with the footer on. Column proportions and the industries grid use Figma's grid layout, matching
  the prototype's CSS grid. Open: weights and banner tint by eye. Translation: `fig-map` §9.
- ✅ **`NavigationMenu / Button` gains Open and Active** — the kit drew "hover" as the open menu; ours
  separates them the way shadcn's code does: Hover is the highlight only, Open adds the panel and flips
  the chevron, and Link gets Active for the current page (`vecto/accent_strong`). Translation: `fig-map`
  §9.
- ✅ **`Theme Switch`** — a light/dark toggle wrapping a Button (outline, icon-sm) with a sun or moon.
  Shown in the navbar: the site opens in dark and this is how a visitor picks light (`f2c` §2a). Translation: `fig-map` §9.
- ✅ **The logo follows the theme** — its dark parts bind to `foreground` (they sat on
  `accent-foreground`), its red mark to `primary`.
- 🔧 **Tabs get a `Size` axis** — `default` is the stock compact control (admin density); `lg` is sized
  to sell: a 48px active pill (the default Button's height), base text, 20px icons, in a 56px track whose
  radius stays concentric. On both the track (`Tabs`) and its segments (`Tabs / Trigger`), every
  variant and orientation, built on `component/tabs/size-lg/*` in the kit's own size-variable pattern.
  The active pill fills with `popover`, the top of the surface ladder, so it reads lifted on the page, on
  a card and on glass (stock fills it with `background`, which on our ladder sits below `card` and looked
  pressed in). Translation: `fig-map` §9.
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
- 🔧 **Card `State=Hover` — for a card that is one clickable surface** (shadcn ships none). Hover lifts the
  card one step on every axis we already have, rather than washing it in accent, which would tint a whole
  surface of content red: the fill steps up the surface ladder (`card` → `popover`; glass: the popover
  colour at 80%, `vecto/card_glass_hover`), the border strengthens (`foreground` at 20%,
  `vecto/card_border_hover`; the glass rim goes full white in light, `vecto/card_glass_border_hover`), and
  the shadow steps from the surface shadow to the popover one (`vecto/glass_hover` for glass). The footer's
  own fill is cleared in the hover variants so the lifted surface shows through, as on glass. A red rim
  (`custom/primary-border`) is drawn beside it on the Draft board as an alternative. Open: the focus state,
  and the choice of rim. Translation: `fig-map` §9.
