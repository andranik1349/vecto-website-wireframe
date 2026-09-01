# VECTO Website — Project Outline

**Purpose.** The top tier of the corpus: the locked decisions (one line each, citing the decision
log), the workflow, the phase spine, the standing contracts, and the verification instruments.
**Doc-key: `outline` · Species: living reference.**

**Scope.** The "what happens, in what order, under which contracts" home. Detail lives in the
area docs — `ia` (structure), `fig-conv`/`f2c`/`fe-arch` (front-end), `be-arch` (backend) — and
rationale lives in the decision log, cited by ID. Corpus map: `docs/README.md`.

---

## The project in one paragraph

A greenfield **Next.js** app, **fully statically generated** (build-time content reads,
rebuild-on-publish), with a **hand-built CMS on Supabase** and a **custom shadcn admin at
`/admin`**, deployed to **Vercel** — decision **DL-04**. The design system is rebuilt in React on
shadcn, with the VECTO brand applied at the variable/token layer (**DL-01**, Radix base
included). Rendering is static-first by cadence (**DL-03**). Editors can create new pages from
code-owned templates (**DL-05**); the entry lifecycle keeps a private draft behind every published
entry and gates publish on mandatory fields (**DL-06**). It's the proven **HES** loop applied end
to end (HES: the comparable client-site project built just before this one, on the same stack and
workflow — its shipped decisions and retrospective lessons seed VECTO's contracts throughout
these docs): **design in Figma → build in Claude Code → sync via GitHub → wire the CMS and
admin** — one
stack, one set of hands, no integration seam owned by anyone else. Andranik owns every step;
Claude is technical advisor and typist, per-component verification before each piece advances.

**Zero interdependency with HES, ever.** Separate repo, separate schema; no VECTO requirement may
ever appear in the HES CMS schema, and vice versa. Whether any HES *admin/backend* code is
literally copied over remains an open call (the front-end is built fresh regardless) — but if a
copy happens, it diverges permanently from the moment of copy; no synchronization in either
direction. What transfers from HES is architecture, contracts, and lessons — never live code
coupling.

## The through-line: one content-model decision, four expressions

A component's content model is decided **once, at design time** — which parts are editable, their
types, cardinality, empty states — and carried forward instead of re-made at each stage:

1. **Annotation** — field type, static-vs-dynamic, cardinality marked on the Figma component (`f2c` §4)
2. **TypeScript type** — each content entity typed: the schema in embryo (`fe-arch` §5)
3. **Content schema** — Supabase tables generated to match the types (`be-arch` §3)
4. **Admin form** — the field type implies the control: text, rich text, image, toggle (`be-arch` §5)

Get the model right once in Figma and it carries itself to the editor's publish button. Proactive
CMS wiring during the component build is what turns the final backend step from a rebuild into a
connection.

## Standards & working method

The disciplines that bind the build from the very first commit — cited in every brief, not
adopted halfway. HES's retrospective is unambiguous: skipping these is what turned clean work
into rework.

### The two-layer standard (both required from the scaffold commit)

- **Code-architecture layer** — the `react-architecture-conventions` rules, bound in the repo's `CLAUDE.md` (`fe-arch` §4 carries the summary).
- **Design layer** — the token stack as single source of truth (Figma-mirrored, `VariableID · path` anchor comments,
  never auto-synced — `fig-conv` §6); customize in the order token → primitive → composition; single-source class
  recipes in `shared/constants/`; a living `/styleguide` route rendering every shared component; and a generated
  **build manifest** as the component list of record and name registry (`f2c` §5).

Doing one without the other recreates HES's gap in mirror image.

### Standing contracts — every brief cites the ones it touches

- `react-architecture-conventions` binds every code task — the admin included.
- **Security by default** — RLS (row-level security: the database refuses reads/writes unless a rule explicitly allows
  them) on every content table, deny-by-default; service keys never reach the client. The admin's access model is
  **full RBAC** — non-negotiable: code-owned roles, runtime user management (creation, role assignment, manual
  credential provisioning) by the (super)admin — decisions DL-11/DL-12 (`be-arch` §5).
- **Stable slugs as keys, never display text** — renaming a visible title never breaks a link or relation.
- **Anything countable derives from data at build time** — never hardcode a count; count the data.
- **Locale × publish-status live in the schema from day one** — never bolted on later.
- **Entry lifecycle & publish validation are schema-level** (DL-06), decided at the pattern-setter stage and never re-invented per collection.
- **Verbatim strings** — content is moved, never silently reworded; the drift detector arbitrates.
- **One zod schema per boundary, shared** — a single validated shape where data enters, reused on both sides.
- **Component names come from the manifest registry** — a rename is a design decision, flagged and asked, never silent (`f2c` §5).
- **All schema changes as versioned migrations** — never console-applied; publish → deploy-hook → rebuild.
- **Structural control is CMS-editable, not code-fixed** — nav/menu order & visibility, page-level publish (an
  independent gate from content-completeness, applying uniformly since every page carries CMS content), and
  section placement/visibility are operator-controlled at runtime, never redeploy-only — decision **DL-21**
  (`be-arch` §7).

### Verification instruments — trust outcomes, not green builds

- **Anonymous-role test suite in CI** — every table/bucket/operation attempted as a non-admin, expecting denial.
- **View-Source / link-preview test** — the shipped HTML literally contains the words; previews unfurl in Slack/X/LinkedIn. A passing build is not evidence; this is.
- **Byte-level DOM baselines** — a saved snapshot of the rendered page, so an unintended change announces itself.
- **A drift detector** — an AST string-extractor over the source → inventory JSON → diff after any content-touching change; doubles as the CMS field-map derivation tool.
- **Editor walkthroughs** — a human doing real admin tasks; the only reliable way to catch quiet failures. Include an *adversarial* pass per stage gate: deliberately produce nonsense (contradicting fields, set-then-unset leftovers, publishing half-filled entries) and check the **public render**, not just admin state.
- **Build-diff alerting** — a rebuild that changes pages it shouldn't says so.
- **Rollback tag before any mass change** — a git tag ahead of every refactor or sweeping edit, so any step reverts cleanly; byte-level DOM baselines are the parity gate for behavior-preserving refactors.

### The build method — brief → in-repo plan → build (DL-20)

- **One brief per stage, ending at a gate.** A brief is 1–2 pages, snapshot species: the goal and
  why, the standing contracts it touches (cited, not restated), what is out of scope, and
  **runnable acceptance checks**. If a check can't be stated runnably, the stage isn't ready.
- **Briefs carry decisions, never measurements.** No stored counts, no file:line citations, no
  inlined implementations, no unverified repo claims — the doc-hygiene skill's Prompt-artifacts
  rules bind. An unverifiable claim is written as a conditional or an open question; a brief
  accumulating many conditionals signals the thinking belongs in the repo, not that the
  conditionals should be firmed into confident prose.
- **Claude Code plans in-repo.** Plan mode against the live repo; parallel Explore subagents for
  the surface census; every load-bearing claim **verified by execution** (run the pattern through
  the real machinery, request the route, read the installed package) or written as a conditional.
  Questions to Andranik only at genuine forks, asked *after* reading the code they depend on.
  Andranik approves the plan before code.
- **Live code is truth** — docs trail the code, not the reverse; claims about what an artifact
  contains, does, or lacks come from opening or running it in the asserting session (full rules:
  the doc-hygiene skill, §Verification).
- **Cowork's lane:** product decisions, design direction, content, decision framing, and briefs —
  never binding technical claims about repo or runtime state (it cannot run the app).
- **Docs ride the change** — plan-row/doc updates land with the stage's own commit/PR; no
  separate close-out passes.
- **Model/mode matched to the work** — architectural stages plan-first on the strongest model;
  mechanical stages may run lighter.

The contracts cover the failures we can name. The unnamed ones are caught by **recurring expert
review** — two standing reviewers (front-end and backend) as scheduled gates, not one-time favors.

## Information architecture

The structure home is **`ia`**, validated by the clickable **wireframe** — which owns the full
placeholder copy and rendered UX (fact split: `ia` header §"Fact split"). The template families the
IA defines (services, cases, industries, who-we-serve, technologies/methodologies/tools, blog,
glossary, solutions…) are the same nouns that become the content schema. **Localization is an IA
dimension from day one:** EN at bare paths (existing URLs untouched), translations at `/hy`/`/ru`,
hreflang linking the set, per-language publish — full treatment in `ia`.

## The phase spine

Design (Figma) → Front-end (Claude Code) → Backend (Next + Supabase), all in one repo. Each phase
ends at a gate; the governing rules live in the doc each row points to.

| Phase | What happens | Governed by |
|---|---|---|
| **0.5 · Structure map & name registry** | *Before any Figma component work:* derive the FSD feature map + name grammar from the validated wireframe — details below. | `f2c` §5 |
| **1 · Brand shadcn at the variable level** | The token spine: `vecto_colors` (the "lit darkness" palette, `#ca1d00` accent), fluid type ramp, typeface, breakpoint modes — authored as Figma variables. Enumerate via the full Plugin API, never `get_variable_defs`. | `fig-conv`; `tokens` (when authored); `f2c` §3 (typeface) |
| **2 · Custom components from shadcn primitives** | Compose the brand component set, bound to the Phase 1 variables. Content-model annotation starts here, at the smallest unit. | `f2c` §1, §4 |
| **3 · Page layouts** | Full-fidelity responsive layouts per template family (one representative per family, as the wireframe established). Section-level content-model notes carry up; design the language switcher; check key layouts against HY/RU text expansion (Figma won't auto-fallback non-Latin — `f2c` §3). | `ia`; `f2c` |
| **4 · Tokens → CSS** | First code step: Figma variables become CSS custom properties + Tailwind theme; shadcn configured against them so primitives come out on-brand. Establish the production `CLAUDE.md`. | `fig-conv` §6; `fe-arch` §4 |
| **5 · React components, proactive CMS wiring** | The heart of the build: presentational, typed, fed from one placeholder module; motion & effects fold in. Per-component verification loop. | `fe-arch` §5 |
| **6 · Page templates** | Assemble verified components into the family templates; routes × language from day one. | `fe-arch` §5; `ia` |
| **7 · Repo, Vercel & Supabase** | One repo (front-end + admin + migrations), Vercel from the repo, dedicated Supabase. Build renders on Vercel before any content wiring. | `be-arch` §2 |
| **8 · CMS wiring & custom admin** | Schema generated from the types; RLS deny-by-default; placeholder → queries (the single swap point); entry lifecycle proven at the pattern-setter collection — details below. | `be-arch` §3–5; `cms-checklist`; DL-06, DL-11 |
| **8b · Editor-created pages from templates** | The net-new-vs-HES track, sequenced after the simpler collections are proven. | `be-arch` §6; DL-05 |
| **9 · SEO & rendering verification** | Confirm the static build outcome with real tools: view-source shows content, link previews unfurl, Search Console URL Inspection, social validators. Per-page metadata, sitemap/robots/structured data at build time. A green build is not evidence. | `fe-arch` §2; verification instruments above |
| **10 · QA & launch** | Cross-device QA, Core Web Vitals (bundle + hydration + shader budgets on real devices), content population, **editorial dry-run** (a non-technical editor publishes end to end), **second-language dry-run** (one HY page: translate → publish → route + hreflang + switcher), DNS cutover + pre-launch security pass. | `be-arch` §5 (security gate) |

Phase 0.5 detail (FSD = "feature-sliced design", organising the front-end by feature rather
than by file type): feature slices, shared-tier candidates, a group→location table, the naming
card. The Figma library is organized per the map; code later mirrors the names verbatim.
Accuracy expectation + start-local/promote rule: `f2c` §5. Deliverable: a one-pager every later
brief cites. Check Figma Code Connect availability (Dev-seat-gated as of June 2026).

Phase 8 detail: the shadcn admin ships full RBAC (code-owned roles, runtime user management +
manual credential provisioning, DL-11/DL-12) and the nav/page-visibility/section-placement controls
(DL-21, `be-arch` §7). The `cms-checklist` interrogation runs here: once for the system, once per
admin screen.

When the build starts, these phases decompose into slug-ID stages in `fe-plan` / `be-plan`
(created then — see `docs/README.md`), with one brief per stage in `briefs/`.

## Developer review gates

No handoff — Andranik owns the build end to end. A Supabase/React-literate developer shows up at
three scheduled gates (easy to skip, which is exactly why they're scheduled):

1. **Content-layer security review (Phase 8)** — schema, indexes & RLS on the write paths, admin exposure, secrets. A hired review here is a **non-negotiable launch gate**.
2. **SSR/SEO verification (Phase 9)** — crawlers receive rendered HTML, confirmed with real inspection tools.
3. **Periodic codebase review (Phase 5 onward, via GitHub)** — catch AI-codebase drift before it compounds; the biggest long-term risk at this size.

## Pitfalls to watch

- **Lock-in by default** — everything in the repo + dedicated Supabase; no platform-local copy (`be-arch` §2).
- **Skipping the CMS-wiring conventions** — components that fetch or inline content turn Phase 8 into surgery (`fe-arch` §5).
- **Generated schema & RLS** — missing indexes bite under load; RLS needs a real audit on write paths (gate 1).
- **Autosave onto live content** — the draft-behind-published rule, in the schema at the pattern-setter stage (DL-06).
- **Publishing incomplete entries** — mandatory-field gating declared once per type in the shared schema (DL-06).
- **SSR + animation hidden-content trap** — visible-by-default children, motion via client wrappers only (`fe-arch` §2a).
- **Quiet SPA habits that empty prerendered HTML** — `useEffect` content fetches, render-nothing-until-mounted, `ssr:false` on content; only the Phase 9 outcome checks catch these (`fe-arch` §5).
- **Locale retrofit** — the route × language dimension exists from day one, even while only EN content exists.
- **Facet-route SEO trap** — only curated facet landings are indexed; multi-facet combos stay noindex query params (`fe-arch` §2c).
- **The AI estimator's return** — when it ships (post-launch) it arrives as a client island with its own API, never a reason to un-static the site (`ia`, appendix).
- **Large-codebase drift** — tight `CLAUDE.md`, per-component verification, GitHub review, periodic refactor passes: mandatory at this size.
- **Admin/public boundary drift** — admin components stay namespaced (`be-arch` §5).
- **Template-instance scope** — the 8b track is net-new and touches every layer; own pattern-setter stage, never folded into the collections (DL-05).
