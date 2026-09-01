# Build Plan & Master IA — Update Audit

**Purpose.** `VECTO-Build-Plan.html` and `vecto-master-ia-revised.html` were written on the Vite + Lovable + Supabase assumptions. This audit checks both against the current state of affairs and proposes per-item updates. Reconcile each item, then apply the approved edits to the two HTML docs.

**Inputs.** `figma-to-code-decisions.md` (esp. §9–11) · the "VECTO design system React rebuild" conversation · `HES-selfbuild-migration-plan-v2.md` (2026-07-03, contingency) · project memory · **UX changes from internal testing (Andranik, 2026-07-03 — Part E)**.

**Format.** Mirrors the wireframe drift-report: each item has a finding, a proposed update, and a **Resolution** line to fill during reconciliation. Items marked ⚖️ need Andranik's call; ✏️ are mechanical once approved. Items marked **🔧WF** also require changes to the interactive wireframe (`wireframe/`) — these are tracked in the **Part F ledger** and handled as a separate Claude Code prompting task after doc reconciliation is done.

_Compiled 2026-07-03._

---

## Part A — The state-of-affairs shifts driving this audit

1. **Backend/CMS is TBD; Lovable is no longer certain.** Root cause is HES: the self-build plan v2 (contingency, pending the leads' conversation) exits Lovable and recommends **Next.js + Payload v3 embedded + Vercel + provider forms + rebuild-on-publish** — and explicitly names the company website as reusing that same assembly. HES is the proving run for VECTO's architecture.
2. **Rendering direction is effectively settled by cadence: static-first SSG / rebuild-on-publish.** No live feeds; ~biweekly publishes. Framework (Vite vs Next vs Vite-native SSR frameworks) stays open, but whatever wins only needs good static generation.
3. **Portability discipline exists and is spec'd** (figma-to-code-decisions §11): default + exceptions (CMS-by-default content, static-by-default render), island the exceptions, client enhancement wrappers for scroll motion, shader two-axis exception, no top-level browser APIs, prop-driven components, one data module, Link/Image/router/metadata wrappers, route-oriented structure, Tailwind-only.
4. **Portfolio filters are now URL-driven by design** (§11c): curated facets promoted to real, designed, prerenderable landing routes; long-tail combos as noindex query params. This is an IA-level change, not just a build convention.
5. **Radix is the decided primitive base**; Figma is the source of truth for styling; token authoring/sync discipline is spec'd (§10).
6. **The site is multilingual** (EN at launch; HY + RU at/soon after) — and neither document carries a localization dimension. HES v2's lesson: retrofitting locale routing is miserable; the route list multiplies per language from day one.

---

## Part B — Build Plan findings

### B1. ⚖️ The third act ("Backend — Lovable", P7–P10) presumes a decided backend
**Now:** Sidebar, workflow rail, TL;DR, tags, and P7–P10 all name Lovable as the settled owner; P7 is "Sync into Lovable via GitHub"; the doc is tagged "Final plan".
**Changed:** Backend owner is an open fork: **(a) Lovable + dedicated Supabase + custom shadcn admin** (the original plan) vs **(b) the HES v2 assembly — Next + Payload embedded + Vercel** (admin generated from code-defined schema). Cadence favors SSG either way.
**Proposed:** Keep the phase *skeleton* — P7 "sync repo → backend environment", P8 "content layer + admin", P9 "SEO/rendering verification", P10 "QA & launch" are already destination-neutral goals. Rewrite the phase *bodies* dual-path: shared steps first, then per-path notes (Lovable-path / self-build-path). Retitle the act "Backend — owner TBD (decision gate before P7)". Update TL;DR, tags ("Final plan" → "Living plan · backend fork open"), sidebar, and workflow rail (4th step becomes "Backend env (Lovable or Next+Payload)"). Add a "watch item": the HES leads' decision is the proving run — VECTO's fork likely resolves when HES's does.
**Resolution:** ✅ **Option 1 (dual-path rewrite), 2026-07-03.** Frame applied: act retitled, new "Backend fork — decide before Phase 7" section (paths table + gate-timing callout + HES watch item), TL;DR fork paragraph, tags/subtitle/sidebar/workflow-rail/footer updated, owner chips → "Backend (TBD)", P7 retitled. Per-phase dual-path bodies land with B3 (P8), B4 (gates), B5 (P9), B11 (P7 checklist). D1 closed; D2 partially answered in the gate callout (HES = strongest input) — explicit default still open.

### B2. ✏️ The content-model through-line survives — restate it backend-agnostically
**Now:** "…generated as Supabase tables in Lovable, and surfaced as shadcn admin forms."
**Changed:** Only the last two expressions are path-dependent. Path (a): Supabase tables + custom shadcn admin. Path (b): Payload collection configs (code-defined — arguably an even cleaner fit for the TS-types-first discipline) + Payload's generated admin.
**Proposed:** Reword the through-line: annotation → TypeScript types → **content schema (Supabase tables or Payload collections)** → **admin (custom shadcn or Payload-generated)**. The "field type does double duty" callout survives verbatim in spirit — field type implies column/field type *and* admin control on both paths.
**Resolution:** ✅ **Applied as proposed, 2026-07-03.** TL;DR sentence + tl-chain nodes reworded backend-agnostic; added the Payload-schema-is-TypeScript note to the through-line box. (P2's "field type does double duty" callout untouched here — B3/B10 territory.)

### B3. ⚖️ P8's "build the custom admin" is path-dependent work that may evaporate
**Now:** P8 devotes half its body to composing a custom shadcn admin (CRUD, publish/draft, admin/public namespace boundary).
**Changed:** On the Payload path the admin is generated from schema; bespoke work shrinks to config + the odd custom field. The admin/public boundary callout becomes moot (admin lives at `/admin` inside the app or as Payload's own surface).
**Proposed:** Present the admin as the fork's biggest scope swing: path (a) = the current text; path (b) = "define Payload collections; admin comes for free; budget only for custom fields/branding". Keep the editorial dry-run (P10) as the acceptance test on both paths.
**Resolution:** ✅ **Applied, 2026-07-03.** P8 rewritten: shared content-layer steps (schema-from-types dual-phrased, placeholder swap, rendered-data-flow check), admin section forked with the scope-swing framing, boundary callout scoped to path (a) with the path-(b) dissolution note. Per-language publish hook deliberately left to B8. Editorial dry-run untouched in P10.

### B4. ✏️ Dev gates are Supabase-specific
**Now:** Gate 1 = "schema, indexes & RLS"; P8 callout likewise.
**Changed:** RLS is a Supabase concept. Path (b)'s equivalents: Payload access-control config, admin exposure, secrets handling — HES v2 §8's bounded expert reviews (CMS/auth setup before content migration; security pass before launch; DNS cutover).
**Proposed:** Generalize Gate 1 to "content-layer security review (RLS on Supabase / access control + admin exposure on Payload)". Keep gates 2 (SSR/SEO verification) and 3 (periodic codebase review) unchanged.
**Resolution:** ✅ **Applied, 2026-07-03.** P8 dev callout + Gate 1 generalized dual-path; HES v2's "bounded one-time review, not a retainer" framing added. Gates 2–3 untouched. (Path-b launch security pass + DNS cutover to be noted at P10 during B12.)

### B5. ✏️ P9 (SEO & rendering) is written entirely around Lovable's SSR story
**Now:** "Lovable's rendering/SEO story matured in May 2026… confirm SSR is active…"
**Changed:** Rendering target is SSG/rebuild-on-publish regardless of path; the Lovable-SSR caveats only matter on path (a).
**Proposed:** Rewrite P9 rendering-agnostic: (1) state the SSG/rebuild-on-publish target and why (cadence); (2) keep the verification discipline — it's the strongest part — and extend it with HES v2's correction: *CSR is degraded/unreliable for Google and dead for link-preview bots; pre-built HTML solves both* → add "link previews unfurl (Slack/X/LinkedIn/iMessage)" to the verification checklist alongside view-source and Search Console; (3) per-page metadata authored behind the metadata abstraction (§11b.4), expressed via whichever mechanism the framework provides; (4) demote the Lovable-specific bullets to path-(a) notes.
**Resolution:** ✅ **Applied as proposed, 2026-07-03.** P9 body rewritten target-first (SSG/rebuild-on-publish + webhook flow), preview-bot correction added, metadata bullet rides §11b, verification checklist extended, Lovable specifics demoted to a path-(a) note + path-(b) one-liner. HES precedent callout retained.

### B6. ✏️ P4's CLAUDE.md brief bakes in the dead assumption
**Now:** "…this is a React/Vite/shadcn front-end destined for a Lovable + Supabase backend."
**Changed:** Framework and backend are TBD; portability is the actual convention to encode.
**Proposed:** Reword to "a React/shadcn front-end, framework and backend intentionally late-binding — built to the portability provisions of figma-to-code-decisions §11." Add the §11b rules to the CLAUDE.md content list: no top-level `window`/`document`; `"use client"` only on own interactive leaves; wrappers for Link/Image/router/metadata; one data module; route-oriented structure; Tailwind-only. Also: the Build Plan currently never references `figma-to-code-decisions.md` — add it as the named companion spec for P1/P2/P4/P5.
**Resolution:** ✅ **Applied, 2026-07-03.** CLAUDE.md bullet reworded late-binding; §11b rules added as a P4 bullet; "Companion spec" callout added to P4 naming figma-to-code-decisions.md (§10 + §11) as the binding reference — "this plan states the phases; that doc states the rules."

### B7. ✏️ P5 conventions: extend with the settled §11 patterns
**Now:** P5 already has presentational-components, placeholder module, SSR+animation trap — all still right.
**Proposed additions:** (1) static-by-default render, island the exceptions (forms/filters/menus + motion wrappers + shaders) — explicitly *not* per-component tagging; (2) scroll motion as client enhancement **wrapper** (`<Reveal>`/`<Stagger>`/`<Parallax>` around server-rendered visible-by-default children) — upgrades the existing trap callout into the positive pattern; (3) shader = two-axis exception, never gating LCP; (4) HES v2's quiet-failure list as named pitfalls: content fetched in `useEffect`, render-nothing-until-mounted guards, `ssr:false` on content — the habits that silently empty prerendered HTML; (5) first-paint/LCP-critical flags.
**Resolution:** ✅ **Applied, 2026-07-03.** New P5 subsection "Render conventions — default + exceptions" (islands, LCP flags, shader two-axis) + quiet-failures warn callout; SSR-trap callout upgraded to the wrapper pattern under "Motion & effects". CMS-wiring conventions untouched.

### B8. ⚖️ Localization is absent from the Build Plan
**Now:** No phase carries EN/HY/RU. The font strategy (two fonts, one family, unicode-range) exists in the decisions doc but the plan never mentions multilingual.
**Changed:** Locale routing multiplies the route list and is miserable to retrofit (HES v2 §7); per-language publish shapes the CMS model; the switcher is a nav component.
**Proposed:** Thread localization through existing phases rather than adding a new one: P0/IA — fix the URL scheme (locale-prefixed paths + hreflang; default language prefixed or not — a convention call) — see C2; P2 — content model carries locale + per-language publish state; P3 — design the language switcher + acknowledge text-expansion (HY/RU run longer); P5/P6 — locale-aware routing and route generation from day one, non-Latin font fallback per the font strategy; P8 — per-language publish in the CMS (built into Payload; needs a design on Supabase path); P10 — QA includes a second-language dry-run even if HY/RU content lands post-launch. ⚖️ decision: URL scheme convention.
**Resolution:** ✅ **Applied, 2026-07-03. D3 decided: bare-EN default** — EN stays at existing paths untouched (SEO equity on live pages like `/about/` preserved); HY/RU at locale-prefixed paths + hreflang. Threaded: P0 (locale note + wireframe equal-weight fix + "content schema" wording), P2 (locale checklist row), P3 (switcher + text-expansion + Figma non-Latin gotcha), P6 (route × language from day one), P8 (per-language publish, path-dependent), P10 (second-language dry-run; editorial dry-run de-Lovabled). **Spawned C8** (existing-slug preservation for case studies).

### B9. ✏️ P1: record the decided specifics
**Now:** P1 lists colors/typography/breakpoints generically; warns on Plugin-API enumeration (keep).
**Proposed:** Add pointers to the now-settled specifics: Radix as primitive base (`--base radix`, Luma preset `b1VlIttI`, install commands in decisions §9); Luma = optional substrate, Figma = source of truth for styling; VECTO colors under `1. TailwindCSS / vecto_colors` with the §10 authoring rules (no in-segment dashes, `_` word-join, export whole group live, variable-ID CSS comments); fluid type ramp is our own (Luma problocks discarded); typeface = Google Sans Flex + Google Sans unified family. One line each + reference to the decisions doc — don't duplicate the spec.
**Resolution:** ✅ **Applied, 2026-07-03.** P1 bullets enriched (vecto_colors + §10 rules, own fluid ramp, typeface line, Radix/Luma/Figma-SoT bullet) + companion-spec callout pointing at decisions §5/§8/§9/§10. Plugin-API warning untouched.

### B10. ✏️ P2 annotation scheme: add the two exception lists, not a render matrix
**Now:** P2 annotation covers content model only (correct, keep).
**Proposed:** Add one short note: per the default+exceptions decision, annotation also marks only the *exceptions* — (a) hardcoded design-language content (shaders, foundational visuals), (b) interactive leaves (forms/filters/menus/motion), (c) first-paint-critical content. No per-component render tagging. Also add the new content entities the IA changes introduce: facet landing pages (C1) as small CMS entities (slug, title, intro, SEO fields), and locale fields (B8).
**Resolution:** ✅ **Applied, 2026-07-03.** P2 callout added: annotation-marks-exceptions rule + "entity noun list is maintained by the IA doc" (so the plan doesn't chase every new entity; facet landings/testimonials/jobs/solutions/CTA fields named as current examples). Locale row landed earlier under B8.

### B11. ✏️ P7 checklist is Lovable-shaped
**Now:** "Dedicated Supabase (not Lovable Cloud)", "GitHub sync", "build runs in Lovable".
**Proposed:** Shared step: GitHub stays the source of truth and the lock-in escape hatch on *both* paths. Path (a): dedicated Supabase + Lovable GitHub sync as-is. Path (b): Vercel project + Payload embedded; the "dedicated project" concern dissolves (everything is in the repo); a Postgres host is a component-level pick (Vercel Postgres / Neon / Supabase-as-database).
**Resolution:** ✅ **Applied, 2026-07-03.** P7 restructured: shared checklist + per-path checklists; day-one-toggles callout scoped to path (a) with the by-construction note for path (b).

### B12. ✏️ Pitfalls list: re-scope and extend
**Proposed:** Mark "credit-based cost model" and "SSR still settling" as path-(a)-only. Add: locale retrofit (B8); quiet SPA habits emptying prerendered HTML (B7); facet-route SEO trap (promote curated facets only; combos stay noindex — C1); the estimator as the one true runtime dependency (C3).
**Resolution:** ✅ **Applied, 2026-07-03.** Three pitfalls scoped path-(a) (incl. admin/public boundary); four added (quiet SPA habits, locale retrofit, facet-route trap, AI-estimator's-return — reworded post-E4). P10 gained the "launch mechanics" bullet (DNS cutover + security pass), closing B4's leftover.

### B13. ⚖️ Decision-gate timing statement
**Proposed:** Add a short "when must the fork close?" note: P0–P3 (design) are unaffected; P4–P6 proceed under the §11 provisions regardless; the backend fork must close **before P7**, and the framework choice ideally before P5 (it's cheap to keep late-binding but cheapest to know). Note the HES dependency explicitly. ⚖️ Andranik: do we also want a stated default (e.g. "if HES lands on Next+Payload, VECTO follows unless the leads object")?
**Resolution:** ✅ **Decided + applied, 2026-07-03: no stated default (D2 = Option 2).** HES is a *soft* dependency — strongest input, not an automatic inheritance; VECTO's fork is decided on its own merits before P7. Gate-timing language landed with B1; fork callout updated to say "soft dependency" explicitly.

---

## Part C — Master IA findings

### C1. ⚖️ Portfolio facet landing pages — new template class + curation decision (the big one)
**Now:** `/our-work` does everything in-page: sticky filter strip (Service · Sub-services · Industry · Technology · Platform · Country · Company stage), outcome groupings, JS filtering. Cross-links elsewhere point at "pre-filtered views" of it.
**Changed:** §11c — filter state is URL-driven; curated single facets become real, designed, prerenderable landing routes; long-tail combos stay query params (noindex, canonicalized).
**Proposed IA edits:**
- **New template: "Facet landing page"** (tag: Template + New) under Our Work, with its anatomy: unique H1/header, editorial intro slot, filtered grid, breadcrumbs, empty/low-count state, own metadata (title/description/OG), the filter strip reflecting the active facet.
- **Namespace facet types** in the URL to prevent slug collisions — e.g. `/our-work/industry/<slug>` vs `/our-work/service/<slug>` (exact scheme = design/SEO call). ⚖️
- **⚖️ Curate the promoted set.** Natural candidates from the existing taxonomy: 13 industries, 7 service categories + AI Transformation (whose "AI tag pre-filtered" links already behave like a landing page in waiting). Second ring, decide explicitly: 5 company stages (they already have `/who-we-serve/` pages — promote a work-facet too, or deep-link the chips to query params?), technologies (33 — probably too thin; the tech pages already list filtered cases), platform/country (probably not).
- **Repoint the existing pre-filtered deep-links** to the promoted routes where they exist: homepage AI band "See it in practice →", AI Transformation hero "See our AI work →", Who We Serve chips, megamenu CTA strips, glossary-entry "See [term] in our work" (terms are *not* promoted facets → those stay query-param links, noindex). Each becomes a named real URL in the IA instead of "pre-filtered view".
- **Content model note:** each promoted facet = small CMS entity (slug, title, intro, SEO fields) — feeds P2/P8.
- **Sitemap/footer:** decide whether promoted facet routes get footer or hub crawl links (probably hub-level "browse by industry/service" links on `/our-work` suffice). ⚖️ light.
**Resolution:** ✅ **Decided + applied, 2026-07-03 (amended same day).** D6: promote industries + service categories + AI Transformation; **the facet set is CMS-driven, never hardcoded — 13+7+1 is launch content, not a constant** (new CMS facet entry → new landing page at next rebuild). Everything else stays query params (noindex). D7: namespaced URLs as proposed. **Amendment (Andranik): the one-way-door model** — facet landings are *entry pages*, not filter states. On-hub filtering is pure query-param state (dropdowns compose freely, never navigate, no page-shape shifts); facet landings are the canonical link targets everywhere *except* the hub's filter controls (industry/service page cross-links, megamenu browse links, marketing deep-links, ads/search/sitemap); on a landing, touching the filter strip moves into hub query filtering; matching query states canonicalize to the landing. Applied: new Facet landing template (7-block spec, one-way-door + content-model/cross-link notes), sidebar entry, hub filter-strip block rewritten, deep-links repointed (homepage AI band + AI hero → `/our-work/service/ai-transformation`; WWS megamenu strip; glossary CTA marked query-param/noindex). Outcome-grouping reference in the strip removed en passant (E1 will remove block 3 itself).

### C2. ⚖️ Localization is absent from the IA
**Now:** No language dimension anywhere: no URL scheme, no hreflang note, no switcher in the 7-slot nav spec, no per-language-publish behavior.
**Changed:** EN launch, HY+RU at/soon after; per-language publish means sections/pages can exist in EN only for a while.
**Proposed IA edits:** Add a "Localization" foundation section fixing: (1) URL pattern — locale-prefixed paths (`/hy/...`, `/ru/...`), ⚖️ default-EN prefixed vs unprefixed; (2) hreflang between translations; (3) the language switcher's home in the nav (header utility area — and its mobile behavior alongside the persistent Estimator CTA), hidden until a second language is live; (4) per-language publish rule: what nav/footer/megamenus show when a page isn't yet translated (fall back to EN vs hide — ⚖️); (5) which surfaces are launch-translated vs EN-first (blog/glossary are the obvious EN-first candidates — ⚖️ with SEO team). Note the route-multiplication consequence for the build (~all full+template pages × languages).
**Resolution:** ✅ **Decided + applied, 2026-07-03.** D4: **hide per-locale** — locale surfaces render only what's published in that locale; switcher fallback = nearest translated ancestor, never 404/mixed-language. **Switcher exists only when >1 language is published** (HES rule) — EN-only launch renders no switcher at all. D5: **deferred by design** — IA fixes the mechanism; scope is a content-ops/SEO plan at translation time. Applied: new "Localization" foundation section (URL scheme incl. `/hy/projects/…` composition with the C8 contract, per-language publish, switcher rules, build consequence), sidebar link, switcher impact-note in nav-architecture. D3 was decided under B8.

### C3. ✏️ The Estimator runtime dependency — SUPERSEDED by E4 (AI estimator deferred)
**Now:** Described as "AI-powered project calculator (currently in active in-house development)" with dynamically populated comparable case studies; embedded mini-version on the homepage (block 13).
**Changed:** Originally flagged here as the site's one genuine runtime dependency under SSG. **E4 defers the AI estimator to a later release** — the launch estimator is a simple provider-backed form. Consequence worth stating loudly: **the launch site now has zero runtime dependencies** — fully static + provider endpoints, on either backend path.
**Proposed:** Fold into E4's edits. Keep one forward-looking note in the IA: when the AI estimator ships, it returns as a **client island backed by its own API/runtime** (separate from the site backend; prerendered page shell; must not gate first paint; designed no-JS/error fallback) — so the simple form's page is designed as the slot it drops into.
**Resolution:** ✅ **Merged into E4, 2026-07-03.** No separate edit; the runtime note lands with the estimator-page rewrite.

### C4. ✏️ Forms and third-party surfaces: annotate the provider/island pattern
**Now:** Contact form, newsletter signup (blog hub block 8), Schedule-a-Call booking widget are described as features with no architecture note.
**Changed:** HES v2 §6 pattern: provider-backed endpoints (Formspree-style form, email-marketing provider, booking embed) mean these need zero custom backend on either path.
**Proposed:** One impact-note (probably on the Contact page entry, referenced from the others): forms post to provider endpoints; booking is an embedded third-party widget (client island); newsletter is a provider form. All are client leaves inside static pages. Not strictly IA, but it prevents these from being scoped as "backend work" later.
**Resolution:** ✅ **Applied, 2026-07-03.** Single architecture note on the Contact page entry covering all forms site-wide (incl. job applications, anticipating E3b) + the booking widget; explicitly marked as the single source for the pattern.

### C5. ⚖️ Extend the URL-driven-filter principle to the blog
**Now:** Blog hub block 4: "Recent posts grid — paginated, filterable by category and author." Categories exist as topic clusters; author pages already have routes.
**Changed:** Same logic as C1: category (and author — already done) filter states should be real routes for SEO; ad-hoc combinations stay client-side.
**Proposed:** Make topic/category pages explicit routes in the IA (e.g. `/blog/category/<topic>` or `/blog/<topic>` — scheme ⚖️), one line each in the Resources branch; pagination under SSG = prerendered page routes or client-side load-more (⚖️ light, can defer to design).
**Resolution:** ✅ **Decided + applied with E2, 2026-07-03.** D8: `/blog/category/[topic]` (namespaced). **Key nuance vs the portfolio:** blog categories are single-select, so the hub's category chips ARE the navigation (real links to category routes) — no composition conflict, no one-way door, no tiered nav on the hub. D9: finalized in the wireframe; instinct = "load more" over numbered pagination. New Blog category template entry (Mention+New) + sidebar link added.

### C6. ✏️ Search surfaces: note the static pattern
**Now:** Industries hub hero has an industry search field; Glossary has search/filter + A–Z.
**Proposed:** One-line notes: these are client-side search over a build-time index (the HES pattern) — no search backend implied. Prevents accidental scope creep.
**Resolution:** ✅ **Applied, 2026-07-03, + one addition from Andranik:** the portfolio filter strip's Service/Sub-services and Industry dropdowns get **client-side keyword filters** (combobox pattern — 13 industries / 46 sub-services need type-to-narrow). Notes added to Industries-hub search, Glossary search, and the hub filter-strip block. 🔧WF: dropdown keyword filters added to Part F.

### C8. ⚖️ Existing case-study URLs must keep ranking (new, from D3 discussion)
**Requirement (Andranik, 2026-07-03):** projects that exist in the current live portfolio keep their slugs — e.g. `https://vecto.digital/projects/sentigraph-ai/`.
**Conflict:** the IA puts case studies at `/our-work/[client-slug]` — the *slug* survives but the *base path* changes (`/projects/…` → `/our-work/…`).
**Two readings:** **(a) full-path preservation** — case study detail pages live at `/projects/<slug>` unchanged (zero redirects, zero risk); hub stays at `/our-work`; slight base-path asymmetry between hub and detail pages. **(b) slug-only preservation + 301s** — details move to `/our-work/<slug>`, every existing `/projects/*` URL 301-redirects (the technologies-hub precedent, where the IA accepted a known migration with redirects); cleaner hierarchy, small transitional ranking risk.
**Also check while in there:** other live URL families worth the same audit — do current service/industry/blog URLs match the IA's paths? (The IA principle says "URLs unchanged," but the technologies relocation already broke it once, knowingly.) Worth one pass over the live sitemap vs the IA before the design phase locks URLs.
**Resolution:** ✅ **Decided + applied, 2026-07-03: full-path preservation.** Case study detail pages live at `/projects/[project-name]`; existing projects keep their live URLs verbatim (zero redirects) — detail URLs are where exactness matters. The hub + facet/filter pages follow their own consistent base; the exact name (`/our-work` vs `/portfolio`) is a pre-launch naming call (→ D18). IA updated: case-study template URL + "URL contract" impact-note; URL note on the Our Work hub. Live-sitemap-vs-IA sweep still recommended (kept as a pre-P3 to-do). 🔧WF: case-study example page path/breadcrumb should reflect `/projects/` — added to Part F.

### C7. ✏️ Micro-items
- Our Work hero counters ("[N] projects…") and the live filter-result count: computed at build time / client-side respectively — one-line note so nobody scopes a stats endpoint.
- Technologies URL-migration impact-note (301s) — unaffected but add "redirects configured at the host level" since there's no server of ours under SSG.
- Estimator output "email me the result / share link / PDF" — flag as part of the estimator runtime scope (C3), not site backend.
**Resolution:** ✅ **Applied, 2026-07-03.** Hero counters → build-time note; filter count → client-side note; technologies 301s → hosting-layer note. Estimator save/share item skipped as moot — it parks with the AI-estimator spec under E4.

---

## Part E — UX changes from internal testing (2026-07-03)

Changes decided by Andranik after team-internal user testing; independent of the tech shifts in Part A but with content-model and Build Plan ripples noted per item.

### E1. ✏️ Portfolio: remove outcome groupings
**Now:** `/our-work` block 3 = four collapsible outcome-story sections; the design rationale is built around "outcome-grouped showcase replaces the flat grid"; the filter-strip note says outcome is "surfaced via the outcome groupings"; **homepage block 9** is also outcome-grouped ("Built from 0 to 1 / Scaled to enterprise / …").
**Proposed:** Delete block 3 and rewrite the Our Work rationale (filter-led + curated/featured, no outcome axis). Homepage block 9 needs a replacement organizing idea — ⚖️ curated featured grid is the obvious default (design call). Remove the filter-strip note's outcome reference. 🔧WF: wireframe shows outcome groupings on both Our Work and homepage — see Part F.
**Ripples:** none on content model (outcome tags were never entity fields — the metric feature was already retired).
**Resolution:** ✅ **Decided + applied, 2026-07-03.** New structural reference: **miiind.co/portfolio** — header + filters → featured section → asymmetric grid on three aspect-ratio presets (1:1, 2:3, 3:2). Our Work: rationale rewritten filter-led; block 3 → Featured projects (CMS flag + order); block 4 → asymmetric grid with per-project aspect preset. D14: homepage block 9 = curated featured grid (CMS-flagged, 6–8, "Browse all work →"), layout to the wireframe. **Content-model ripples after all:** `featured` flag + order, `aspect_preset` enum per project, three image-constraint sets → P2/P8.

### E2. ✏️ Blog: two-tier categorization
**Now:** Categories = topic clusters "Build · Design · AI · Founder advice · Engineering · Industry insights"; post template says posts are "tagged with topic and (where relevant) service / industry / technology."
**Changed:** Two explicit tiers. **Primary:** standard thematic blog tags (tech news, company updates, insights, etc.) — the navigational/routable taxonomy. **Secondary:** first-class relations into the site's own IA — related **projects**, related **services**, related **technologies** — powering cross-discovery modules, not navigation.
**Proposed:** Rewrite the blog hub Categories block + post template tagging note around the two tiers. Per the C5/§11c principle: primary categories = prerendered landing routes; secondary relations = related-content modules on both ends (post ↔ service page, post ↔ case study, post ↔ technology page), never routes. ⚖️ final primary category list (with content/SEO team). Note: the old list's "AI / Industry insights" straddle both tiers — resolve in that pass. Also confirm: is *industry* still a relation (was in the IA, absent from the new list)?
**Ripples:** BlogPost entity gains relation fields (projects[], services[], technologies[]) — P2 annotation + P8 schema; relations are exactly what the typed-entity discipline handles well on both backend paths.
**Resolution:** ✅ **Decided + applied with C5, 2026-07-03.** Two-tier model in the hub (chips block) + post template: exactly one primary category (routable) + secondary relations — **industry kept as the 4th relation** (projects, services, technologies, industries), both-directions cross-discovery, never routes. Primary list ships as a marked placeholder (Tech News · Company Updates · Insights · Guides) pending D15. BlogPost entity: category + 4 relation arrays → P2/P8.

### E3. About section restructure
**a) ✏️ Split 'About VECTO' into two pages.** Now a single page with megamenu anchor links. Becomes: **(1)** About — history, mission & vision (+ partners, trust signals); **(2)** Team — leadership, specialists, careers callout. ⚖️ URLs: `/about` + `/about/team` suggested. Update the About megamenu (columns currently point at anchors), footer Company column, and the IA's About page entry (split into two page specs).
**b) ⚖️ Standalone job list page + application form.** New page(s): job listings, each **tagged per the Technologies taxonomy** (another IA relation — jobs ↔ tech pages); application form (provider-backed per C4). Decisions: URL (`/about/careers` vs `/careers`); job *detail* pages vs in-page expansion (detail pages = SEO surface + shareable links, recommended); one general application form vs per-job. **Ripples:** new Job entity (title, description, technology tags, status/open-closed) — needs publish/unpublish; another argument for the CMS handling collections well.
**c) ✏️ Security & Compliance — on hold.** Remove from the About megamenu, footer Company column, About page cross-link block, and the Contact page's procurement/InfoSec path. Move the full page spec to the Appendix as "parked, not deleted" (same treatment as Why VECTO). The IA section itself stays in the doc, re-tagged Deferred.
**d) ✏️ Testimonials page — create the missing spec.** Referenced today from the About menu and homepage block 10 ("link to the dedicated Testimonials page") but has **no page entry in the IA**. Add a full spec. **Content rule (Andranik):** all testimonials/reviews live **on-site in the CMS** — fields: author, company, testimonial text, link to source (Google/Clutch/etc.). Homepage Reviews block therefore renders CMS testimonials (with source links), not embedded third-party widgets. **Ripples:** new Testimonial entity; homepage block 10 + trust strip copy adjust; review-platform badges can stay as static trust marks.
**Resolution (a–d):** ✅ **Decided + applied, 2026-07-03.** `/about` becomes a **hub** (deliberately simple; nav-consistency destination for the clickable About headline; most visitors skip it) with sub-pages: `/about/company` (history, mission/vision, partners, trust signals), `/about/team` (leadership, specialists, careers callout), `/about/careers` (job list + "don't see your role?" general form) + `/about/careers/[job-slug]` **job posting template** (per-job provider-backed application form, tech tags → technology pages), `/about/testimonials` (full spec; CMS-hosted testimonials: author, company, text, source link — no embedded widgets). **S&C removed from all visible surfaces** (About menu, footer, cross-links, Contact path 7) and parked verbatim in the Appendix. About megamenu rebuilt around the new pages; footer Company column updated (+Testimonials); homepage Reviews block → CMS-testimonials wording; Job entity content-model note added. D16 closed.

### E4. ⚖️ Simplify the estimate / contact / schedule pipeline
**Now:** Three-path Contact page + AI-powered Estimator page (widget, output card, accuracy note, dynamic comparable cases, save/share) + standalone Schedule a Call. Internal user testing found the pipeline overcomplicated.
**Changed:** Launch flow = **Get an Estimate: simple form → fill → submit → optional Schedule a Call step.** The AI-assisted on-site estimation generator is **deferred to a later release**.
**Proposed:**
- Rewrite the `/get-an-estimate` spec: hero + simple project form (provider-backed) + success state offering the optional scheduling step + reassurance copy ("what happens after you submit"). Park the AI-estimator spec (blocks 2–7: widget, output card, accuracy, dynamic comparables, save/share) in the Appendix, parked-not-deleted, with the C3 note about how it returns (client island + own API).
- Homepage block 13: mini-estimator embed → simple CTA block (or shortened form) — design call.
- **Copy sweep:** every "ballpark in 90 seconds" promise (homepage, megamenu strips, hub CTAs, estimator hero) assumed the AI tool — reword to the form reality (e.g. "tell us about your project — get a ballpark from the team"). ✏️ but touches many blocks in both docs.
- ⚖️ Contact page: does the three-path structure survive? Proposal: simplify to **two paths** (Get an Estimate · Send a question) + direct contacts, with scheduling reached through the estimate flow (and kept as a standalone page for the About menu link + direct bookings). Alternative: keep all three but visually de-escalate. Needs Andranik's read of the testing.
- ⚖️ Homepage block 16 (triple CTA close): follows the Contact decision — likely becomes dual CTA.
- Schedule a Call page itself: keep as-is (it's the optional step's destination), demote its prominence.
**Ripples:** strengthens B12/C3 — launch site has zero runtime dependencies; estimate form = provider endpoint (C4 pattern). Build Plan P2/P8: form submissions may not even need CMS entities (provider inbox) — ⚖️ decide if estimate requests should be stored in the CMS for pipeline tracking or live in the provider/email only.
**Resolution:** ✅ **Decided + applied, 2026-07-03.** D12: **two paths** on Contact (Get an Estimate · Send a question); scheduling = optional step in the estimate success state, page kept but demoted (About menu + direct bookings); homepage block 16 → dual CTA. D13: **email/provider only at launch** — no CMS storage; CRM is the upgrade path if volume justifies. Applied: `/get-an-estimate` fully rewritten (form + "what happens after" + success state + curated comparables + forward-slot note); AI-estimator spec parked in Appendix (incl. the homepage mini-version); homepage block 13 → Estimate CTA block; Contact + Schedule pages updated; "90 seconds" copy sweep done (3 instances — the surviving one lives only inside the parked appendix spec).

### E5. ⚖️ SOLUTIONS — new site concept
**What:** Mini-portfolio of VECTO's own small B2B/SaaS products (onemall, onesocial, quickoffer, plugins). Main page = intro text + listing of available solutions; each solution gets a dedicated page **similar to the case study template**.
**Proposed IA additions:** new branch — `/solutions` hub (Full) + "Solution page template" (Template + New; case-study anatomy adapted: what it is, who it's for, features/screens, tech stack, pricing/plans if applicable, external CTA per E6, related case studies/services). **Ripples:** new Solution entity (own template family → own collection in P8; another P0 noun).
**Key ⚖️ decision — nav placement.** The 7-slot nav (6 menus + CTA) is full. Options: **(a)** 8th top-level item "Solutions" (most honest to its "entirely new concept" status; costs nav weight); **(b)** inside the Services megamenu as a distinct band (like the AI band — "productized solutions" vs services); **(c)** under Our Work — but Our Work is deliberately a direct link, and mixing client work with own products muddies both. Also decide: footer placement (likely column 1 or 4) and whether Solutions gets a homepage block.
**Secondary flags:** does the blog's "related projects" relation (E2) cover solutions too, or is "related solutions" a fourth relation? Do solutions appear in the portfolio filter facets, or stay fully separate? (Recommend: fully separate surfaces, cross-linked.)
**Resolution:** ✅ **Decided + applied, 2026-07-03.** D10: **8th top-level nav item**, direct link, placed beside Services ("what we offer" pair); the main CTA button may compact to fit — acceptable since the sticky/floating estimate CTA carries every page regardless. Rejected: Services-megamenu band (Services already overcrowded — the AI band barely fits). D11: footer column 1 → "Services & Solutions"; compact homepage Solutions strip (block 10a, proof cluster); blog "related solutions" relation NOT front-loaded; solutions fully separate from /our-work (cross-linked, never mixed). Applied: nav paragraph (8 slots) + all megamenu mock bars, new Solutions branch (hub spec + solution template with E6 CTA baked in + Solution entity note), sidebar, homepage net-new note updated.

### E6. ✏️ External CTA on case study + solution templates
**What:** Both templates get a "launch website / download app / try now" CTA linking out to the live product.
**Proposed:** Add a block row to the case study template (and bake into the E5 solution template): external product CTA — placement a design call (hero-adjacent or post-outcomes). **Content model:** optional `cta_label` + `cta_url` on CaseStudy and Solution entities; **hidden when absent** (not every case study has a public product) — exactly the empty-state discipline P2/P5 already require; exercise the absent case in placeholder data.
**Resolution:** ✅ **Applied, 2026-07-03.** Case study template: CTA in hero (+ repeated in closing CTA row) with the hidden-when-absent + placeholder-data note; solution template had it from E5. Placement hero-adjacent by default, adjustable in design/wireframe.

### E7. Menu-heading convention + estimator naming retirement (post-reconciliation addendum, 2026-07-03)
**Origin:** the item-7 prompts-review discussion surfaced a can of worms: the wireframe's "dropdown headings are links" rule forced pointless targets (HWW "Reference" → how-we-work hub; About "Trust & contact" → the deleted S&C page; Resources "Glossary" heading duplicating "Browse A–Z"; Resources Tools → Project Estimator redundant with the adjacent nav CTA).
**Decided (Andranik):**
- **New convention: headings are non-interactive labels by default; a heading is a link only when a real destination page exists.** Interactive vs non-interactive visually distinct — prototype: accent-red *text* (not a pill) vs muted grey; final treatment = Figma/DS task (new component pair). Applied as a five-menu sweep: links = Services stage headings, HWW Process/Engagement Models, Resources Blog, WWS "By company stage" → /who-we-serve + "By industry" → /industries (legit hubs), About The company/The team; labels = HWW "Reference", Resources "Glossary" (tagline + single Browse A–Z link), About "Trust & contact".
- **Resources Tools column deleted** (menu only; footer keeps the entry, relabeled). E4 hadn't accounted for all consequences of deferring the AI estimator: the "tool" framing was its artifact. **"Project Estimator" naming retired everywhere until the AI estimator returns** — page + all references read "Get an Estimate"; the appendix notes the Tools entry + tool naming return with the AI estimator.
- **Menu placement ≠ hierarchy** noted in the IA: Schedule a Call + Contact stay standalone root-level pages; their About-menu presence is nav convenience. Pages stay distinct (estimate = conversion landing for ads/deep-links; contact = everything else) — the convergence is resolved at the menu/label layer, not by merging pages.
**Applied:** IA — nav-convention impact-note, Resources menu rebuilt (2 cols), HWW/About/WWS heading notes, footer col 4 + all "Project Estimator" references relabeled, blog-hub block 7 reframed, appendix note. Prompts — P1 step 3 rewritten (convention + 3a About + 3b five-menu sweep + footer relabel + verify), canonical-facts bullets, P9 naming-sweep step, P12 grep extended.
**Resolution:** ✅ done 2026-07-03.

---

## Part D — Decision roll-up (⚖️ items needing Andranik)

| # | Decision | Options / leaning |
|---|---|---|
| D1 | ~~Build Plan act 3 restructure (B1)~~ | ✅ **Decided 2026-07-03: dual-path rewrite** (Option 1) |
| D2 | ~~Stated default for the fork (B13)~~ | ✅ **Decided 2026-07-03: no stated default** — HES outcome is a soft dependency; fork decided on its own merits before P7 |
| D3 | ~~Locale URL scheme (B8/C2)~~ | ✅ **Decided 2026-07-03: bare-EN** (existing URLs untouched), `/hy/` + `/ru/` prefixed, hreflang |
| D17 | ~~Case-study URL preservation (C8)~~ | ✅ **Decided 2026-07-03: full-path** — `/projects/[project-name]` verbatim for existing projects |
| D18 | Portfolio hub/facet base name (C8) | `/our-work` vs `/portfolio` — consistent pattern required now, exact name decidable any time before launch |
| D4 | ~~Untranslated-page behavior (C2)~~ | ✅ **Decided 2026-07-03: hide per-locale**; switcher → nearest translated ancestor; switcher rendered only when >1 language published |
| D5 | ~~Launch translation scope (C2)~~ | ✅ **Closed 2026-07-03: deferred by design** — mechanism in IA; scope with SEO team at translation time |
| D6 | ~~Promoted facet set (C1)~~ | ✅ **Decided 2026-07-03:** industries + service categories + AI; CMS-driven set (13+7+1 at launch, never hardcoded); stages/technologies/platform/country = query params |
| D7 | ~~Facet URL namespacing (C1)~~ | ✅ **Decided 2026-07-03:** namespaced — `[hub-base]/industry/<slug>` + `[hub-base]/service/<slug>` |
| D8 | ~~Blog category route scheme (C5)~~ | ✅ **Decided 2026-07-03:** `/blog/category/[topic]`; hub chips = real links (single-select, no one-way door needed) |
| D9 | ~~Pagination pattern (C5)~~ | ✅ **Closed 2026-07-03: to the wireframe**; instinct = load-more over numbered pagination |
| D10 | ~~Solutions nav placement (E5)~~ | ✅ **Decided 2026-07-03: 8th top-level item** beside Services; CTA may compact (sticky CTA covers) |
| D11 | ~~Solutions extras (E5)~~ | ✅ **Decided 2026-07-03:** footer col 1; compact homepage strip (10a); no blog relation yet; fully separate from /our-work |
| D12 | ~~Contact page shape (E4)~~ | ✅ **Decided 2026-07-03: two paths**; scheduling demoted to estimate success state + About menu; homepage CTA → dual |
| D13 | ~~Estimate submissions storage (E4)~~ | ✅ **Decided 2026-07-03: email/provider only** at launch |
| D14 | ~~Homepage portfolio module replacement (E1)~~ | ✅ **Decided 2026-07-03: curated featured grid** (CMS-flagged); portfolio reference = miiind.co/portfolio |
| D15 | Primary blog category list (E2) | final "usual suspects" set — with content/SEO team; industry-relation yes/no |
| D16 | ~~About/Careers URLs & depth (E3a/b)~~ | ✅ **Decided 2026-07-03:** `/about` hub + `/about/company` + `/about/team` + `/about/careers` + `/about/careers/[slug]` + `/about/testimonials`; job detail pages yes; per-job forms + general fallback form |

## Part F — Wireframe update ledger (🔧WF)

**Principle: the wireframe and the IA doc are equal-weight sources of truth and must stay as close to a 1:1 match as possible.** The wireframe exists to validate IA/UX decisions in a realistic interactive environment — paper-sense ≠ good UX, as the wireframe has already proven. So **every IA-visible change reconciled above gets built into the wireframe by default**; the ledger tracks scope and sequencing, not whether. Executed after doc reconciliation as its own Claude Code prompting task (sequenced prompts, drift-fixes style).

| Src | Wireframe change | Confirmed |
|---|---|---|
| E1 | Our Work rebuilt to the miiind.co structure: header + filters → featured section → asymmetric grid (1:1 / 2:3 / 3:2 presets); outcome groupings removed | confirmed |
| E1/D14 | Homepage portfolio module: outcome groups → curated featured grid, layout validated here | confirmed |
| E3a | About area rebuild: `/about` hub (simple) + Company + Team pages; About megamenu + footer re-propagated to every page | confirmed |
| E3b | Careers list page + one example job posting page (per-job application form) | confirmed |
| E3c | Remove Security & Compliance from About menu + footer + About/Contact cross-links; drop the page | confirmed |
| E3d | New Testimonials page; homepage Reviews block → CMS-testimonial cards with source links | confirmed |
| E4 | Estimator page: simple form + "what happens after" + success state w/ schedule step; homepage block 13 → Estimate CTA block | confirmed |
| E4/D12 | Contact page: two paths (Estimate · Send a question); homepage block 16 → dual CTA; Schedule page demoted | confirmed |
| E4 | Copy sweep: "90 seconds" / instant-ballpark promises across homepage/menus/hub CTAs → form-reality copy | confirmed |
| E5 | New Solutions hub + one example solution page; 8-slot nav (Solutions after Services, compacted CTA) re-propagated to every page; homepage Solutions strip (10a) | confirmed |
| E6 | Case study example page: external product CTA in hero + closing (one example with, consider absent-state on another) | confirmed |
| C1 | One example facet landing page (new template → wireframe gets its representative, per the one-per-template rule) + Our Work filter strip reflecting the active facet | _tbc_ |
| C8 | Case-study example page: URL/breadcrumb reflects `/projects/[project-name]` (hub links unchanged) | confirmed |
| C2 | Language switcher UI in nav — placement + drawer behavior need interactive validation; note the visibility rule means the wireframe must simulate a "2nd language published" state to show it at all | _tbc_ |
| C5 | Blog: category chips as real links to category routes; one example category page; pagination pattern (load-more instinct) validated here | confirmed |
| C6 | Keyword filters inside the portfolio Service/Sub-services + Industry dropdowns (combobox pattern) | confirmed |
| E7 | Menu-heading label/link sweep (all five menus, red-vs-grey distinction); Resources Tools column deleted; "Project Estimator" → "Get an Estimate" naming sweep | confirmed (P1/P9) |

B-series items are doc/code-convention changes only — no wireframe impact expected.

## Suggested edit streams (after reconciliation)

- **Stream 1 — Build Plan** (B1–B13 + Part E ripples: new entities Testimonial, Job, Solution, blog relations, external-CTA fields): one editing pass; the dual-path rewrite of P7–P10 is the bulk of it.
- **Stream 2 — Master IA** (C1–C7, E1–E6): facet-landing template + localization section; About restructure + Testimonials spec + Solutions branch; estimator/pipeline rewrite + copy sweep; deep-link repointing; Appendix parking for Security & Compliance and the AI estimator.
- **Stream 3 — wireframe (Part F):** after doc reconciliation — confirmed 🔧WF items turned into sequenced Claude Code prompts (drift-fixes style), run against `wireframe/`.
- **Stream 4 — deferred:** anything hinging on D2 (HES outcome) or the SEO/content-team consults (D5, D8, D15).
