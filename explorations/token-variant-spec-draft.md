# VECTO × shadcn — token & variant architecture (draft to muse over)

> Not a definitive doc. A sketch of how the home-highend exploration's flourish maps onto a shadcn base. The rule of thumb throughout: **shadcn owns behavior + the semantic token names; we own the values and a thin flourish layer on top.**

---

## 1 · Token layer

shadcn already defines a semantic token vocabulary (`--background`, `--foreground`, `--card`, `--primary`, `--border`, `--ring`, `--radius`, …). We don't invent a parallel one — we **assign our values to theirs**, then add a small **brand extension** namespace for things shadcn has no concept of (glow, glass, gradients).

### a) Map exploration vars → shadcn semantic tokens

| Exploration var | shadcn token | Notes |
|---|---|---|
| `--bg #08080A` | `--background` | page base |
| `--bg-2 #0D0E11` | — | keep as `--brand-surface-sunken` (media wells) |
| `--surface .025` | `--card`, `--popover` | glass fills sit *on top* via utility, not here |
| `--text #F6F6F8` | `--foreground`, `--card-foreground` | |
| `--text-2 / -3 / -4` | `--muted-foreground` (+ brand steps) | shadcn has one muted; we keep a 3-step ramp as `--brand-text-2/3/4` |
| `--red #CA1D00` | `--primary` | `--primary-foreground: #fff` |
| `--red-light #EB3213` | `--brand-accent-light` | hovers, gradient stops, glow |
| `--line .08 / .14` | `--border`, `--input` | hairlines |
| `--cyan #2BBAD6` | `--ring` | focus ring (already brand's focus color) |
| `--radius-*` | `--radius` (+ steps) | shadcn derives sm/md/lg from one `--radius`; we expose the full ladder |

Decision to make: shadcn's newer default is **OKLCH**; the exploration is hex/rgba. OKLCH makes the red→glow ramp and hover states easier to tune perceptually. Lean OKLCH for brand ramps, keep hex only where a value must match a spec exactly.

### b) Brand extension (things shadcn has no slot for)

```
--brand-glow:        <primary at ~55% a>     /* radial glow color */
--brand-glass:       rgba(255,255,255,.025)  /* card fill over dark */
--brand-hairline-hi: inset 0 1px 0 rgba(255,255,255,.08)  /* inset top highlight */
--ease:              cubic-bezier(.32,.72,0,1)
--ease-soft:         cubic-bezier(.4,.14,.2,1)
```

These are the only genuinely "new" tokens. Everything else is a value swap.

---

## 2 · Utility layer (keeps markup clean)

Rather than repeat arbitrary Tailwind values (`bg-[linear-gradient(...)]`) everywhere, define a handful of utilities/components so the flourish is named, not pasted:

- `.surface-glass` — glass fill + hairline border + inset highlight + optional `backdrop-blur` (fixed/sticky only, per perf guardrail)
- `.surface-gradient` — the subtle top-lit card gradient
- `.glow` / `.glow-band` — radial brand-glow, `pointer-events-none`, blurred
- `.hairline` — the `--border` divider treatment
- `.grain` — fixed noise overlay (once, globally)

Tailwind v4: express these as `@utility` (or `@layer components`) reading the tokens above, so they theme automatically.

---

## 3 · Button — extend, don't replace

Keep shadcn's `Button` (Radix `Slot`, `asChild`, sizes, disabled/focus states). Add variants via its CVA config:

| Variant | Purpose | Delta from shadcn |
|---|---|---|
| `primary` | main CTA | gradient fill (`--primary`→`--brand-accent-light`), glow shadow, inset highlight |
| `ghost` | secondary | glass fill + hairline, blur |
| `text` | inline link-btn | no chrome, accent on hover |
| `sizes` | `sm / md / lg` | pill radius (`rounded-full`), roomier padding than shadcn default |

**Button-in-button trailing icon** = a composed pattern, not a variant. A small `<ButtonIcon>` slot (`2em` circle, `bg-white/16`, inset highlight) that the `Button` renders when passed an `icon` prop / trailing child. Hover physics (icon translate + scale, whole-btn press-scale, magnetic move) live in the component, driven by `--ease`.

---

## 4 · Card — the double-bezel as one composed component

This is the workhorse. One `<Card>` with a `shell` (outer, `p-1.5`, big radius, glass, hairline) wrapping a `core` (inner, concentric smaller radius, gradient, inset highlight). Variants cover the exploration's uses:

- `default` — content card
- `feature-lead` — large bento cell (icon top, copy anchored bottom)
- `stat` — figure + label, divided band member
- `media` — image well + body (portfolio / blog)
- `interactive` — adds hover lift + border brighten (links/tiles)
- `glow-band` — full-width CTA/AI band with internal radial glow

Everything bespoke (megamenu shell, hero visual, stat band, chip rows) composes *from* Card + tokens + utilities — none of it needs a new primitive.

---

## 5 · Things to chew on

- **OKLCH vs hex** for the brand ramps (leaning OKLCH).
- **How many muted-text steps** to keep — shadcn's 1 vs our 3. Collapsing to 2 might be enough.
- **Where blur is allowed** — nav + overlays only; cards use static gradient, not live blur (perf).
- **Figma parity** — restyle the shadcn kit to these tokens, then Code Connect the primitives; bespoke compositions stay Figma-native, mapped by name.
- **Motion tokens** — should reveal/hover timings be tokenized (`--dur-*`) too, or left in components? Leaning: tokenize the eases, keep durations local.
