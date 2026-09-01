# VECTO typeface strategy — two fonts, one family name (seed for `tokens`)

> Not a definitive doc. A worked-out plan awaiting its real home in `front-end/tokens.md` (build
> Phase 1). Decided by Andranik 2026-07-01; the web-verified facts below carry that date and
> **must be re-checked by execution at install time** (DL-20) — package names, axis ranges, and
> licensing especially.

**The decision.** Main typeface is **Google Sans Flex**. In Figma it is anchored at variable
`2. Theme / font / font-sans = "Google Sans Flex"`. The site is multilingual: **English (default)
at launch, Armenian + Russian at or soon after launch.**

**The strategy: two fonts, one family name, per-glyph resolution by codepoint (browser-native).**

- **Google Sans Flex** → Latin + Latin-ext, with all six expressive axes.
- **Google Sans** → Cyrillic, Armenian, Greek, plus everything else outside RTL Middle Eastern and
  SE Asian scripts.
- Declare **both under one `@font-face` family name** (working name `'Vecto Sans'`), each scoped
  with `unicode-range`. Latin: `U+0000-00FF, U+0100-024F, U+1E00-1EFF, U+2000-206F`. Non-Latin:
  `U+0400-04FF` (Cyrillic), `U+0530-058F` (Armenian), `U+0370-03FF` (Greek). Point `--font-sans`
  at the unified family so it flows through every shadcn component.
- Slots into **Phase 1** (Figma variables) and **Phase 4** (tokens → CSS).

**Bonus perf win:** `unicode-range` gates the download, so the broad-script Google Sans file is
only fetched when an in-range glyph actually appears — all-English pages pay zero bytes for
multilingual support.

## Axis facts (verified 2026-07-01 — re-verify at install)

| | Google Sans Flex | Google Sans |
|---|---|---|
| Axes | weight 1–1000 · width 25–151 · **opsz 6–144** · slant −10–0 · grade 0–100 · ROND 0–100 | ital 0–1 · **opsz 17–18** · weight 400–700 · grade −50–200 |
| Scripts | Latin, Latin-ext | 20+ writing systems incl. Armenian, Cyrillic, Greek, Arabic, Devanagari, Hebrew |
| Variable package | `@fontsource-variable/google-sans-flex` (family `'Google Sans Flex Variable'`) | `@fontsource-variable/google-sans` (family `'Google Sans Variable'`) |

**Licensing — the whole plan depends on this.** Google Sans Flex reached Google Fonts in 2025;
**Google Sans was released under the SIL Open Font License on 2025-12-10**, the first time Google's
brand face became publicly self-hostable. Both are legal to self-host.

## Optical sizing — the axis Andranik cares most about

`font-optical-sizing: auto` is the **browser default**, so font-size auto-maps to opsz with no
per-style or per-breakpoint tuning. Do **not** set opsz in `font-variation-settings` — that
disables the automatic behaviour.

The ranges differ hugely: Flex's 6–144 is full optical sizing for Latin; Google Sans's 17–18 is
narrow. Glyph *shapes* barely change with size on non-Latin — but testing showed opsz still
auto-adjusts character spacing and metrics there, so mixed Latin/non-Latin runs stay balanced in
practice. **Net: keep auto-opsz on everywhere.** It fully optimises Latin and still helps non-Latin
spacing.

## Four things that would silently break it

1. **Use `@fontsource-variable/*`, never plain `@fontsource/*`.** The plain packages ship static
   weight instances (100–900) and drop every axis. This is the single change that would flatten the
   font without any visible error.
2. **Hand-author the `@font-face` blocks.** Fontsource's generated CSS declares each font under its
   own family name, so the cross-family unification needs custom `@font-face` pointing at the
   packages' variable `.woff2` (copied to `/public/fonts`). Use modern
   `format('woff2') tech(variations)`, not legacy `woff2-variations`. Source the **full** variable
   woff2, not the weight-only slice; control weight via `font-weight`, roundness and width via
   `font-variation-settings`, and leave opsz to auto.
3. **Keep a real fallback in the token:** `--font-sans: 'Vecto Sans', system-ui, sans-serif`.
   Glyphs outside both unicode-ranges — arrows, math, emoji, CJK — fall through and need it.
4. **Figma does not do per-glyph fallback.** That behaviour is browser-only, so Figma will not
   auto-swap to Google Sans for Armenian or Cyrillic: multilingual comps must set non-Latin text to
   Google Sans by hand or they render tofu. Document this in the DS.

## Design caveats

Expressive axes (width, roundness, slant) are **Latin-only**. Cyrillic and Armenian render at a
shared weight — stable, not shape-shifting — so **hierarchy must not depend on roundness or
width**. The weight axis *is* shared, so weights map consistently; but Flex's 1–1000 against Google
Sans's 400–700 means hairline and heavy weights (200/800/900) clamp on non-Latin. shadcn's 400–700
usage is safe. Google Sans has a true `ital` axis where Flex uses slant.

**Separate but related:** a custom **fluid type ramp** built on Tailwind is planned (Andranik to
supply an example); the Luma `problocks` heading tokens are discarded. See `fig-conv` §6 and `f2c`.
