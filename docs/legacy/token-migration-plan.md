> **⚠️ LEGACY — archived 2026-06-30.** This document belongs to the previous VECTO design-system effort (the custom red/dark Figma system). VECTO is now being rebuilt in React on a shadcn **Luma** baseline. Kept for historical reference only — not a current source of truth.

---

# VECTO Tokens — 3-Tier Migration Plan

_Working file: "VECTO Website" copy (`rL15HUTlFDPlG0iXiiaLVe`). Non-destructive migration of the color system to three collections. Companion to `design-system-conventions.md` (§1). Numbers collection is untouched — it stays the responsive layer._

## End state

| Collection | Modes | Contents | IDs |
|------------|-------|----------|-----|
| **T1 · primitives** | 1 (modeless) | Full raw palette, rebuilt fresh | new |
| **T2 · semantic** | `Dark` now (+ `Light` later) | Role tokens; each aliases T1. **The only collection with a theme mode.** | new |
| **T3 · component** | 1 (modeless) | The existing `variables - style` collection, renamed. All 62 `semantic colors/*` variables kept (IDs intact) + regrouped; re-aliased to T2. `base colors/*` deleted at the end. | preserved |

Resolution: **T3 → T2 → T1**. Theme is switched by setting the **T2** collection's mode on a frame/page; T1 and T3 pass through.

## The non-destructive principle (why this works)

A variable's node bindings live on its **ID**. Figma can't move a variable between collections without recreating it (new ID), so we **never move** the bound tokens. The 62 `semantic colors/*` variables are all bound to nodes → they stay put (the collection is simply renamed to T3) and we only change their **alias target** (raw value or `base/*` → `T2`), which preserves IDs and bindings. T1 and T2 are built fresh because nothing binds to them on a node — they're alias targets only.

## Binding reality (from the live scan, 2,849 nodes)

- All 62 semantic tokens are bound → all stay as T3. ✓
- 16 `base colors` show node bindings, but **12 are bound only in the `Colors`/`Typography` documentation frames** → disposable, delete outright.
- **4 primitives carry real product bindings** and need a scripted rebind before `base colors` can be deleted:

| Primitive (raw) | Real bindings | Components | Rebind target (T3) |
|---|---|---|---|
| `brand/primary-2` (#ca1d00) | ~46 | icon fills, input-slider | `icon/accent` (+ slider accent) |
| `light 1` (#cbcdd4) | ~8 | input-slider, dropdown | matching T3 applied token |
| `dark 2` (#222429) | ~5 | input field background | `input/bg_default` (exists) |
| `dark 6` (#696b70) | ~2 | icon fill | `icon/muted` |

> `primary-2` has **two kinds of reference to clear before it can be deleted**, unlike the other three (node bindings only): it is the alias target of five semantic tokens (`surface/accent`, `button/main-default`, `input/input-icon-default`, `border/brand-accent`, `text-generic/accented-darker`) — cleared in step 3 when those re-point to T2 — and it is bound to ~46 nodes — cleared in step 5. It is never renamed; the clean primitive is recreated in T1 (`brand/red`) and this raw one is deleted.

## Execution sequence

Each step is one or a few scripted `use_figma` calls, validated before the next.

**1 — Build T1 · primitives (fresh).**
Create collection `T1 · primitives` (modeless). Recreate the palette from current `base colors` values. Naming follows the delimiter rule (`/` = hierarchy, `_` = word-join, no hyphens):
`brand/red_strong` (#9e1300), `brand/red` (#ca1d00), `brand/red_bright` (#eb3213), `brand/red_alpha`, `brand/cyan_strong` (#2291a5), `brand/cyan` (#2bbad6), `brand/cyan_bright` (#64c7d8), `brand/cyan_alpha`, `neutral/dark_1…7`, `neutral/light_1…4`, `neutral/white`, `neutral/black`, `overlay/dark_1…3`, `overlay/light_1…3`, `overlay/neutral`, `error`. Scope to `FRAME_FILL, SHAPE_FILL, STROKE_COLOR, EFFECT_COLOR` (not `ALL_SCOPES`).

**2 — Build T2 · semantic (fresh, mode = `Dark`).**
Create collection `T2 · semantic`, rename its mode `Dark`. Create role tokens, each aliasing a T1 primitive. Proposed roles (delimiter rule applied):
- `surface/` — `canvas`, `default`, `raised`, `sunken`, `overlay`, `inverse`, `inverse_muted`
- `content/` — `primary`, `secondary`, `tertiary`, `accent`, `accent_strong`, `on_accent`, `on_inverse`, `error`, `disabled`
- `line/` — `default`, `subtle`, `strong`, `accent`, `focus`, `focus_muted`
- `action/` — `primary`, `primary_hover`, `neutral`, `neutral_hover`, `ghost_hover`, `accent`, `accent_hover`, `disabled`
- `scrim/` — `dark_1…3`, `light_1…3`, `modal`, `neutral`
Scope each to its purpose (`content/*`→`TEXT_FILL`+`SHAPE_FILL`, `line/*`→`STROKE_COLOR`, etc.).

**3 — Re-alias the existing T3 (`semantic colors`) tokens to T2.**
For each of the 62 tokens, repoint its alias from `base colors/*` (or its current raw hex) to the matching T2 role. IDs unchanged → every node binding keeps working. Also fixes the 4 current raw-value-in-semantic-layer violations (they become proper aliases). Scripted in batches; validate with a screenshot of representative components after each batch.

**4 — Rename + regroup T3.**
Rename collection `variables - style` → `T3 · component`. Strip the `semantic colors/` prefix and regroup per conventions: `surface/*`→`card/*` & generic `bg/*`/`fg/*` where appropriate, keep `button/*`, `input/*`, `tag/*`; add generic applied tokens (`bg/canvas`, `bg/surface`, `fg/primary`, `border/default`, `icon/accent`, `icon/muted`) aliasing T2. (Renames preserve IDs.)

**5 — Remediate the 4 real primitive bindings.**
Script-rebind the ~61 nodes in the table above from the raw primitive to the correct T3 applied token. Screenshot the slider, dropdown, input, and icon-bearing components before/after — expect **no visual change** (values are identical; only the binding source moves).

**6 — Delete `base colors`.**
With nothing aliasing them (step 3) and no real node bindings (step 5), delete the 12 doc-only primitives and the 4 now-rebound ones. The `base colors` group is gone; the collection is now pure T3.

**7 — Rebuild Foundations documentation (optional, recommended).**
Repoint the `Colors`/`Typography` swatch frames to T1 so the foundations page documents the real primitives.

**8 — Verify.**
- Re-run the binding scan: expect 0 nodes bound to any deleted variable.
- Screenshot Buttons, Inputs, Navigation, Cards — confirm unchanged.
- Theme smoke test: add a temporary `Light` mode to T2, give 3–4 `surface`/`content` tokens light values, flip a frame's T2 mode, confirm it reskins through T3 without touching components. Remove the temp values (or keep as the start of real Light mode).

## Risk notes

- Steps 1–4 are fully non-destructive (additive + rename + re-alias). Reversible.
- Step 5 is the only node-level change (~61 bindings); atomic per script, screenshot-verified, value-identical so visually safe.
- Do **not** delete `base colors` (step 6) until step 5's screenshots confirm clean — that's the one ordering that matters.
