# VECTO — Front-End Architecture

**Purpose.** How the front-end is built: project setup & tooling, the SSG/portability provisions
the repo enforces, and the structural primitive lessons re-applied from HES. **Doc-key: `fe-arch`
· Species: living reference.**

**Scope.** Build rules only. Figma authoring lives in `fig-conv`; Figma→code translation in
`f2c`; the workflow/phases/contracts in `outline`; backend/CMS in `be-arch`; decision rationale
in the decision log, cited by ID. Corpus map: `docs/README.md`.

**Status legend.** ✅ established · 🔧 decided in principle, spec pending · 📎 reference/context.

---

## 1. Project setup & tooling

- ✅ **Framework, rendering & backend are settled — decision DL-04:** Next.js (App Router), full SSG, hand-built CMS on Supabase, custom shadcn admin at `/admin`, Vercel. The §2 portability provisions are what keep the SSG build clean — they're *realized on Next*, not kept open against a framework choice. The Luma install `--template` is therefore `next`.
- ✅ **HES gotchas applied at scaffold time** (greenfield — no migration phase, decision DL-04): `rsc: true`; no top-level `window`/`document`/`localStorage`; the no-flash inline-script theme pattern; `dynamic = 'error'` + `dynamicParams = false` guards; fresh-canvas-per-mount for the shader background (§3).
- ✅ **Primitive base: Radix UI** — decision DL-01 (the shadcn `--base radix` option; also selectable in the Luma preset
  at ui.shadcn.com/create). The safe, shadcn-default, AI-codegen-reliable choice for a production launch. **Base UI**
  (MUI team) is the deferred alternative, revisited only if the admin's form UX later justifies the non-trivial switch
  (different APIs: `asChild` vs render prop, different packages) — which is why this was fixed at the
  `create`/`--base` step. The documented conventions themselves are base-agnostic (on paper only the primitive imports
  differ); the swap cost lives in the built code, not in these docs.
- ✅ **Luma install (if used) is a shadcn preset, not a theme.** Preset code `b1VlIttI` (from ui.shadcn.com/create).
  - Fresh (pnpm): `pnpm dlx shadcn@latest init --preset b1VlIttI --template next --pointer`
  - Fresh (npm): `npx shadcn@latest init --preset b1VlIttI --template next --pointer`
  - Existing project (pnpm): `pnpm dlx shadcn@latest apply b1VlIttI` (optionally `--only theme` / `--only font`); (npm): `npx shadcn@latest apply b1VlIttI`
  - Inspect first (pnpm): `pnpm dlx shadcn@latest preset decode b1VlIttI --json`; (npm): `npx shadcn@latest preset decode b1VlIttI --json`
- ✅ **The shadcn MCP cannot install Luma** — its theme tools cover only TweakCN themes. Use the MCP for components/blocks. (This was the earlier "couldn't install Luma" trouble: it was being treated as a theme, not a preset.)
- ✅ **Do not run installs from the Cowork sandbox** (ephemeral, network-restricted, not the real repo). Run in Claude Code / local terminal during real setup.

## 2. Portability & SSG-safety provisions

**Rendering posture: static-first (SSG), rebuild-on-publish — decision DL-03** (publish cadence
and near-zero interactive surface; no per-request SSR). Framework and backend: **decision DL-04.**
These provisions describe *how the settled Next SSG build stays clean* — SSR-safe, portable,
static-by-default — and keep any future migration cheap. Routing and static-vs-CMS content follow
the IA (`ia`).

### 2a. Figma / design-stage provisions
- ✅ **Default + exceptions, NOT per-component tagging.** No render matrix needed — shadcn's interactive primitives already ship their own `"use client"`, so the boundary largely tags itself. Two defaults + short exception lists:
  - **Content:** CMS by default. Hardcode only the "design-language" foundations (shader backgrounds, foundational visuals). Mark just the exceptions.
  - **Render:** static/prerendered by default. Exceptions to watch: **forms (validation/interaction state), filters, menus/nav, scroll motion (parallax / staggered reveal)** — plus **shaders** (client because they need GPU/canvas, not because of user state).
- ✅ **The one discipline to keep: island the exceptions.** Keep each interactive/client bit a small separable leaf inside an otherwise static page (filter control inside a server-rendered grid; form as a leaf; menu disclosure as a leaf) so it doesn't "clientize" its whole page. This is a handful of components, not a pass over all of them.
- ✅ **Shader background = the one genuine two-axis exception** — hardcoded (not CMS) *and* a client leaf (WebGL) *and* must not block first paint. Client island behind static content, with an SSR-safe fallback; never part of the prerendered HTML that gates LCP.
- ✅ **Flag first-paint / LCP-critical content** (hero, above-the-fold) — matters for SSR/SSG initial HTML.
- ✅ **Scroll motion (parallax / staggered reveal) = client enhancement *wrapper*, not a client block.** The APIs are
  browser-only (IntersectionObserver / scroll / GSAP ScrollTrigger) so the *wiring* is client — but the revealed
  **content stays server-rendered and visible by default**: a client `<Reveal>` / `<Stagger>` / `<Parallax>` wrapper
  receives server-rendered `children` and only *adds* motion. The behavior is a hardcoded design-layer property,
  **never CMS** (you can't author a scroll effect in the CMS; at most a preset on/off). Build SSR-safe (visible by
  default, JS adds motion, honor `prefers-reduced-motion`) — never retrofit the hidden-content trap.

### 2b. Code portability & SSG-safety provisions (enforced on Next SSG)
1. ✅ **shadcn primitives self-tag `"use client"`; you only tag your own interactive leaves** (forms/filters/menus/shaders). The universal guardrail regardless of framework: **no top-level `window`/`document`/`localStorage`** — browser APIs only in effects / behind the client boundary. This is what keeps SSG/SSR possible on a CSR codebase.
2. ✅ **Pure presentational components, data via props — no fetching inside components.** The master enabler: decouples components from where/when data loads (the only real CSR/SSR/SSG difference).
3. ✅ **One framework-agnostic data-access module** (plain async fns; placeholder → real CMS). Single swap point.
4. ✅ **Abstract framework-coupled primitives behind your own wrappers — highest leverage:** `<Link>`, `<Image>` (esp. `next/image`), router/navigation hooks, and head/metadata. Migration = swap adapter files, not every call site.
5. ✅ **Route-oriented folder structure**, thin page compositions → mechanical move into Next `app/`.
6. ✅ **Tailwind + CSS-vars only; no runtime CSS-in-JS** (fights RSC/SSR) — already our approach.

### 2c. Portfolio / Work filters as addressable URLs (design decision)
- ✅ **Filter state is URL-driven, not JS-only** — the URL is the source of truth for filter state (path or searchParams), so states are shareable, prerenderable, and framework-portable (rides the §2b.4 router abstraction).
- ✅ **Promote a curated set of high-value single facets to real path routes** — the namespaced facet-landing routes
  the IA defines: `/our-work/industry/[industry]`, `/our-work/service/[service]` (the hub base name, `/our-work` vs
  `/portfolio`, is a pre-launch call — `ia` owns the URL structure). Each is a **designed landing state**: unique
  H1/header, editorial intro slot, filtered grid, breadcrumbs, empty/low-count state, own metadata
  (title/description/OG). These prerender + index = SEO landing pages "for free."
- ✅ **Keep long-tail multi-facet combinations as query params** (`?industry=a&service=b`), client-filtered and **noindex / canonicalized** — avoids thin/duplicate content and crawl bloat.
- ✅ **Namespace facet types** to avoid slug collisions — the explicit `/industry/` vs `/service/` path segments.
- ✅ The filter UI must **reflect the active URL facet** (control state synced to the URL).
- **Content-model add:** each promoted facet landing = a small CMS entity (slug, title, intro/description, SEO fields).
- **Why now:** needs designed page states; far cheaper up front than retrofitting onto in-place JS filtering. (Full page structure: `ia`, facet landing template.)

## 3. Structural primitive lessons to re-apply (from HES — non-brand)

VECTO installs shadcn primitives **clean** — not copied from HES, whose kit customizations are brand-coupled leftovers to avoid. But a handful of HES's fixes were *structural*, not brand: real code gotchas worth re-applying on the fresh install. None of these carry HES's look; they just prevent known breakages.

- ✅ **`extendTailwindMerge` for custom `text-*` utility groups.** tailwind-merge silently drops utility classes it doesn't recognise; once we add our own `text-*` (fluid type) utilities, register them via `extendTailwindMerge` or they vanish when class lists are merged.
- ✅ **Export CVAs from `*.variants.ts`.** Keeping class recipes (cva) in their own exported module keeps React Fast Refresh working — a non-exported cva sitting in a component file breaks hot reload.
- ✅ **Input-group textarea auto-detect.** The input-group primitive must detect a textarea child to size correctly — re-apply the auto-detect fix.
- ✅ **The `@layer base` button `cursor: pointer` rule.** Tailwind v4 dropped v3's default pointer cursor on buttons; add it back in `@layer base` or buttons feel dead to the click.
- ✅ **Fresh-canvas-per-mount for any WebGL panel.** Mount a new canvas on each mount (don't reuse one across mounts) — avoids the React StrictMode / HMR lost-context trap on the shader background. Same rule the project outline flags at scaffold time.

## 4. Production repo conventions (`CLAUDE.md`, established at the first code phase)

✅ The production repo's `CLAUDE.md` encodes the durable conventions from the start, so every later session inherits them:

- This is a **Next.js/shadcn front-end built for static generation**, following the §2 portability provisions.
- The **`react-architecture-conventions` skill binds every code task** (the admin included) — FSD placement, kebab-case filenames, arrow-const components, `type` props, `@/` imports, CVA in `*.variants.ts`, zod at data boundaries, ~250-line component ceiling, one config per tool. shadcn's own `ui/*` primitives and vendored engines are exempt from the file conventions.
- The **content-model tagging scheme** and what the tags mean (`f2c` §4); how placeholder content is structured (§5 below); the static-vs-dynamic rule.
- The **doc-hygiene skill** binds every long-lived doc in the repo; the docs corpus moves into the repo at build start (decision DL-08).
- ✅ **The skills-routing map is written into `CLAUDE.md` at scaffold time** (HES added its filter late and paid in
  drift). The map itself — session ritual, Cowork + Code routing tables, the subject-matter override, the design-skill
  suppressions — lives in **`skills` (`docs/skills-routing.md`)** — the one home; the repo `CLAUDE.md`
  gets the compact Code-side routing table plus a pointer at `skills` for the ritual and rationale, never a verbatim
  copy (a copy ages at its own rate — doc-hygiene skill rule 1).

## 5. Component & template build conventions (the proactive CMS wiring)

These are the provisions that make the later CMS wiring a connection rather than a rebuild. Bake them in while
building, not after. **The loop, per component:** point Claude at the exact Figma node (leaf or section frame, not the
canvas root) → map its properties per `f2c` §1 → carry the content-model annotation into the prompt (`f2c` §4) →
verify visual fidelity + data-shape wiring before advancing.

- ✅ **Type every content entity now.** A `CaseStudy`, `BlogPost`, `ServiceCard` TypeScript interface per content type. These types are the Supabase schema in embryo — the CMS generates tables to match, and the components already expect that exact shape.
- ✅ **Components are presentational — data comes via props.** No data-fetching inside components. The Supabase query layer gets added at the wiring stage without touching component internals — the clean insertion point.
- ✅ **Centralize placeholder content in one typed module, never inline strings.** All placeholder titles, descriptions, and image references live in a single `content/placeholder.ts` (typed to the entity interfaces). At wiring time there's one swap point per content type — not scattered edits across dozens of components.
- ✅ **Mark dynamic content explicitly in code.** A consistent convention — a `// CMS:` comment, or simply sourcing from the placeholder module versus a static import — so it's unambiguous which props become Supabase fields and which are part of the design.
- ✅ **Exercise cardinality and empty states in the placeholder data.** Arrays that hit the min, the max, and the empty case, so each component handles them before real data arrives.
- ✅ **Images: URL prop + aspect-ratio constraint now, Storage URL later** — swapping a static import for a Supabase Storage URL is a one-line change.
- ✅ **Render conventions:** static by default, island the exceptions — the §2a/§2b rules; this is not a per-component tagging pass.
- ✅ **The three quiet SPA habits that empty prerendered HTML** — no compiler flags them; only outcome checks (view-source, link unfurls) catch them: content fetched after mount (`useEffect`), rendering nothing until mounted (the lazy fix for hydration warnings), and `ssr:false` imports on content (right for a WebGL canvas, content-deleting anywhere else).
- ✅ **Motion & effects fold into the component build** — staggered scroll-reveal (IntersectionObserver + GSAP),
  multi-layer parallax (ScrollTrigger), shader backgrounds (OGL), performance-budgeted, `prefers-reduced-motion`
  honoured, designed and tuned together (not one-shot generated). The SSR-safe reveal pattern is §2a's client-wrapper
  rule — reveals that start at `opacity: 0` get baked into prerendered HTML as hidden; the wrapper receives
  server-rendered, visible-by-default children and only adds motion.
- ✅ **The shader *engine* is shared from HES; the shaders are not.** The host/lifecycle/compositing infrastructure (carrying the fresh-canvas-per-mount pattern and the `uInk` theming approach) transfers as vendored infra; the GLSL shader variants themselves are VECTO's own visual language, written fresh.
- ✅ **Templates:** one per family (`ia` defines the families) — collection templates consume arrays of typed content,
  detail templates consume a single typed entity; wire to the placeholder module (swap to queries later); confirm
  responsive composition across breakpoint modes; **route generation carries the language dimension from day one**
  (bare-EN + `/hy` + `/ru` per published language, hreflang between them — cheap at build time, miserable to
  retrofit).
- 🔧 **Nav and page-section composition are CMS-driven order/visibility, not hardcoded JSX order** (decision DL-21).
  Render stays static-first (DL-03): order/visibility are read at build time like any other content, never fetched
  at request time. Nav items and section placements need their own typed content entities alongside the
  per-component placeholder module (§5 above) — a page assembles its section list from CMS-ordered, CMS-toggled
  placements instead of a fixed sequence of imports (`be-arch` §7).
