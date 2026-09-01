# VECTO Website — Inheritance Brief (from the HES build)

> **⚑ RETIRED 2026-07-17 — mined into the corpus.** Every VECTO-binding rule in this brief was
> traced to a home in the living docs (`project-outline.md`, `front-end/*`, `back-end/*`,
> `README.md`, decisions D-01…D-10) during the docs refactor. This file is kept as historical
> reference only; where it disagrees with a living VECTO doc, the living doc wins. Corpus map:
> `docs/README.md`.

*Compiled 2026-07-08 inside the HES Cowork project, whose session memory does not carry over.
This doc is the portable seed: every VECTO-relevant decision, lesson, and working-method
instrument earned on HES, in one place. **Add it to the VECTO Website project's knowledge at
kickoff** so the first session starts with full context. It will go stale as VECTO develops its
own docs — treat it as the starting capital, not a living tracker.*

---

## 1. What's confirmed vs not settled (clarified 2026-07-08)

**CONFIRMED:**

1. **Same architecture**: Tailwind, shadcn, Next.js, SSG, custom headless CMS — on whatever
   architecture the HES CMS lands on (that call is with the HES backend lead as of writing).
2. **Same design principles** and **same Figma-to-code conversion contracts** (the §2 sequence
   + §3 two-layer standard below).
3. **Zero interdependency, ever** — whether anything is copied or not: separate repo, separate
   schema; no VECTO requirement may ever appear in the HES CMS schema, and vice versa. (Adopted
   at the HES decision meeting 2026-07-06 — this half of "fork, don't share" stands regardless
   of what happens to the other half.)
4. **Known VECTO requirements (superset of HES):** CMS-*created* template pages (HES only
   field-edits fixed layouts — a real scope difference), portfolio with tag/filter →
   prerendered tag pages, 3 languages, ~weekly publish cadence. Rebuild-on-publish works fine
   at weekly cadence.
5. **VECTO gets its own design system** (own tokens/brand); it inherits the *architecture* of
   HES's design layer, not its look.

**NOT SETTLED:**

- Whether the code is **literally forked** (copied over and refactored to VECTO's needs) at all.
- If it is, the fork is likely **admin panel + backend only** — NOT the front-end.

**Planning consequence:** do not assume a pre-named shared tier or `ui/` kit arrives for free.
The VECTO front-end is most plausibly built fresh — which means the §2 sequence (FSD map + name
registry before Figma) applies in FULL, with no inheritance shortcut. If the admin/backend fork
happens, what transfers there is the CMS schema patterns, RLS posture, ingest pipeline shape,
and admin components — refactored, then permanently divergent.

### 1.1 Front-end sharing granularity (Andranik, 2026-07-08 — the brands share little visual language; HES is a client brand, VECTO is our own)

| Piece | Shared? | How |
|---|---|---|
| Shader **engine** (host/lifecycle/compositing infra) | ✅ shared | carries the per-mount canvas pattern + `uInk` theming approach with it |
| The **shaders** themselves (GLSL variants) | ❌ | totally different — VECTO's own visual language |
| shadcn **primitives** | ✅ 100% (as a concept) | **clean install from the shadcn MCP, NOT copied** — HES's kit-customizations are brand-coupled leftovers to avoid; re-customize to VECTO's kit |
| Color/numeric **tokens** | architecture + principles only | same tiers/axes/`VariableID · path` anchor model + the full-enumeration sync playbook; **values re-exported from VECTO's Figma**, never matched against HES's CSS ("fight leftovers until the end of time") |
| Custom **navigation** elements | ❌ (likely similar, rebuilt) | similarity doesn't justify a wholesale FE fork |

**Structural (non-visual) primitive lessons to re-apply on the clean installs** — these are NOT
brand-coupled and will bite again if skipped: `extendTailwindMerge` registration for any custom
`text-*` utility groups (tailwind-merge silently drops them otherwise); exported CVAs in
`*.variants.ts` (Fast Refresh); input-group's textarea auto-detect; the `@layer base` button
`cursor: pointer` rule (Tailwind v4 preflight dropped v3's); fresh-canvas-per-mount for any
WebGL panel.

## 2. The build sequence (the single biggest retrospective lesson)

**Derive the structural map BEFORE designing components in Figma.** On HES the wireframe/IA had
~90% of the UI architecture before Figma component work started — the map was derivable and
nobody derived it; the cost was a 34-commit refactor and a naming drift (`navbar` silently became
`SiteNav` etc.).

Sequence for VECTO:

1. **Wireframe / IA first** (as HES did — this part worked).
2. **FSD map + name registry derived from it, before Figma**: feature slices, shared-tier
   candidates, a group→location table, and the name grammar. Cowork produces this as a
   one-pager.
3. **Figma library organized and named per the map.** Naming card (mechanical, no engineering
   taste required): kebab-case slash-groups (`group[/subgroup]/component` — the HES grammar,
   already FSD-shaped); don't reuse a shadcn primitive's name for a composition; name by
   *consumers, not origin* (Figma groups thematically — "where it's seen"; FSD places by "who
   uses it"; they usually agree, and the map says who wins when they don't).
4. **Codeprompts cite the map; code mirrors names VERBATIM.** Contract line for every prompt:
   *"Component names come from Figma/the registry verbatim. Never invent, translate, or
   'improve' a name. A rename is a design decision, not a build step — flag and ask."*
5. Calibration: the map is born ~85% right. Start-local-promote-on-2+-real-reuse stays the
   runtime rule (HES evidence: `ArticleShell` proved shared only when a second page copied the
   first; `CtaBand` looked shared and died on real divergence). The map prevents naming and
   placement drift; it does not decide everything upfront.
6. Check **Figma Code Connect** availability (was Dev-seat-gated in June 2026) — if unlocked, it
   attaches code identity to Figma nodes so MCP consumers receive the real component name
   instead of guessing; the registry then becomes its backup rather than the whole defense.

## 3. The two-layer standard (both required from the scaffold commit)

*(Plus a third, doc-side standard: the **`doc-hygiene` skill** — portable, authored 2026-07-15
from HES's drift lessons — binds every long-lived VECTO doc (plan/spec/tracker/CLAUDE.md) from
day one: doc species, point-don't-restate, rewrite-don't-annotate, the end-of-session encoding
sweep. Bind it in VECTO's CLAUDE.md at scaffold time, same as the conventions skill; starting
with clean docs is far cheaper than HES's retrofit — see `HES-doc-hygiene-reform-plan.md`.)*

- **Code architecture = the `react-architecture-conventions` skill, binding from day one.**
  Bind it in VECTO's `CLAUDE.md` at scaffold time so every session loads it — don't rely on
  memory. FSD placement, kebab-case files, arrow-const components, `type` props, `@/` imports,
  CVA in `*.variants.ts`, no casts at data boundaries (zod), single-source class recipes,
  ~250-line component ceiling, one config per tool. The shadcn `ui/*` kit and any vendored
  engines are exempt from its file conventions.
- **Design layer = the HES-style contract stack, rebuilt for VECTO's brand:** token layer as
  single source (Figma-mirrored, `VariableID · path` anchor comments as re-sync identity, never
  auto-sync), customize token→primitive→composition in that order, single-source class recipes
  in `shared/constants/`, a living `/styleguide` route registering every shared component, and a
  build manifest as component-inventory SoT + name registry.
- The skill covers only code architecture. HES's near-spotless design layer through two hostile
  audits came from the second stack. One without the other re-creates HES's gap in mirror image.

## 4. Working-method instruments that transfer (replicate, don't re-derive)

- **Cowork→Code method**: Cowork (advisory, docs, Figma inspection) crystallizes each unit of
  work into ONE self-contained codeprompt; Code builds; per-page/per-step spec docs; a
  page-building guide once patterns stabilize.
- **Stage IDs are names, not addresses — never let identity masquerade as order (added
  2026-07-16).** HES's build plan lettered its decomposition `2.c3a…2.c3l` as stable IDs
  *deliberately* decoupled from build order (a separate sequence block held the real order;
  insertions took the next free letter) — and the disclaimer never survived contact with a
  reader: ID shapes that look sequential get READ as a sequence, so "2.c3k builds right after
  2.c3c" parses as gibberish even where the dependency logic is sound. The letters ended up
  encoding nothing but accretion order while their shape lied about being a build order. Deep
  hierarchical IDs (`2.c3d2`) compound it — the depth freezes a decomposition that WILL change
  (HES's 2.c3 was decomposed after the fact, `d` split into `d1`/`d2`, `b` split again mid-build).
  For VECTO: stage IDs are short **content slugs** (`faq-entries`, `media-library`,
  `singleton-pattern-setter`) — citable, stable anchors (doc-hygiene needs those) that are
  *incapable* of implying order — plus ONE sequence/dependency block as the only ordering SoT.
  A numeric prefix for table sorting is allowed only as renumberable cosmetics; citations always
  use the slug.
- **Live code is truth**: re-check `git log` + the manifest at the start of every session; docs
  and memory trail the code. Stale-checklist drift bit HES twice.
- **Contracts cover NAMED failure modes; periodic expert review covers unnamed ones.** Recurring
  reviewer gates (HES converged on two named reviewers — FE + backend), not one-time. Skills
  reduce priors-drift but only for what their author named.
- **Vocabulary-translation rule**: design-vocabulary instructions must be translated, not obeyed
  literally. Figma "component" = reusable unit; code component = also a decomposition chapter
  (zero overhead, split for maintainability regardless of reuse). HES's 750-line homepage came
  from obeying "no need to make each section a component" on the wrong axis. When a designer
  instruction touches code structure — ask.
- **Drift detector**: an AST string-extractor over the source (HES: `hes-content-extractor.mjs`)
  → inventory JSON → diff after every change. Verified a 34-commit refactor changed zero copy.
  Rebuild one for VECTO early; it doubles as the CMS content-model derivation tool (HES derived
  its whole CMS field map from extraction — exhaustiveness by script, not memory).
  Improvements owed from HES experience: an `--out` flag (it overwrites its baseline) and
  test-file exclusion.
- **Refactor/verification hygiene**: rollback tag before any mass change; byte-level DOM
  baselines for behavior-preserving refactors; verification instruments must be rebuilt per
  layer (visual failures are loud — designer catches them; architecture/security failures are
  quiet — engineer/tests catch them). Budget instruments to where failure modes live: Figma
  fidelity for visual surfaces, acceptance tests + anonymous-role security suites for admin/CMS.
- **Quiet-risk guards for the SSG world** (identical stack, identical risks): content resolves
  at build time, never `useEffect`-fetched; the outcome test is literal — *View Source contains
  the words; link previews unfurl*; never trust a green build; WebGL/canvas panels use the
  fresh-canvas-per-mount pattern (StrictMode/HMR lost-context trap); theme pre-paint inline
  script against flash. Tailwind v4 preflight quirk: buttons need an explicit
  `cursor: pointer` base rule (v4 dropped v3's).
- **Counts/data rule**: anything countable derives from data at build time, never hardcoded
  (HES shipped wrong hardcoded counts for weeks). Keys are stable slugs, never display text.
- **Per-language content**: if VECTO mirrors HES's model — per-locale draft/publish status in
  the schema from day one, build-time fallback to the default language, one rule system-wide.
- **Skills routing (write the filter into VECTO's CLAUDE.md at scaffold time — HES added its
  filter late and paid in drift):** beyond the two always-on skills in §3 (conventions +
  doc-hygiene), the rest are task-routed, not ambient. Build phase: `react-expert` for component
  work; `nextjs-developer` for anything Next-touching (routing, metadata, draft mode, build
  behavior) — **verify its version-sensitive claims by web search, Next moves fast**;
  `fullstack-guardian` for cross-stack DB→API→UI stages; `secure-code-guardian` only where
  auth/forms are hand-rolled instead of provider-bought; the shadcn skill for component
  sourcing/CLI under the same two HES guardrails (never let it touch the token layer; never
  blind-merge upstream into customized primitives). Quality: `playwright-expert` to turn the
  SSG outcome tests (quiet-risk guards above) into automated checks; pick ONE review family
  (`testing-strategy` OR `test-master`/`code-reviewer`), never both in parallel.
  Decision-support (`the-fool`, `common-ground`) and `architecture-designer` get a kickoff
  cameo for genuinely NEW calls only (e.g. CMS-created template pages — VECTO's one real scope
  difference) and are benched once architecture freezes; write the bench-rule down or priors
  drift it back. `spec-miner` flagged 2026-07-16 as the closest fit for §5.2's
  reader-trace/map-authoring step — vet it against the §5.2 checklist before relying on it.
  The plugin ships ~90 personas; most are off-stack (Angular/Django/mobile/ML/…) — filter hard.

## 5. CMS lessons — editor experience + content modeling (added 2026-07-16)

*Source: HES's status/label modeling failure (HES decision log DL-21/DL-22, corrected at DL-23) and the mixed-save-model
autosave gaps, both caught by manual editor walkthroughs after the code had passed every automated
gate. HES absorbs its remaining instances as-they-come (accepted 2026-07-16 — no retro rework of
map/schema/plan); VECTO builds these in from day one, where they're nearly free.*

### 5.1 Editor-experience fundamentals — design the lifecycle ONCE, before any editor screen ships

- **Proper autosave, autosaved drafts, and publish logic designed as ONE coherent contract** at
  CMS-spec time: what autosaves, what needs an explicit save, what publish/unpublish does, what a
  draft-of-published is — then every form obeys the same contract. (HES bolted these per-stage;
  the seams show.)
- **One save model per form, no exceptions without a written case.** (HES: shared-settings
  dropdowns saved via their own "Save settings" button while sibling fields autosaved — an editor
  cannot tell what's saved. Any control that must deviate gets argued for in the spec, not
  discovered in QA.)

### 5.2 Content-model doctrine

- **Declare the authority order at kickoff: rendered site (FE code) → content map → schema →
  prompts/config.** Each layer conforms UPWARD; a check of prompt-against-schema is consistency,
  not correctness — if the schema never got validated against the map, downstream verification
  just replicates the error with confidence. (HES: `status_label` — a per-row column the site
  never read — passed every "all columns match" gate and shipped three bugs.)
- **The content map is a content model, not a string inventory.** Every field it lists carries a
  **structural kind** — per-row datum / per-locale shared constant / derived-at-render /
  code-owned — plus the FE file that reads it. (HES's map compressed a constant map into the
  parenthetical "labels per locale"; the schema resolved the ambiguity as a per-row field; wrong.)
- **Map-authoring hygiene from the extractor JSON:** the AST extract already records structural
  truth (a keyed constant map like `STUDY_STATUS_LABEL` is visibly different in the JSON from
  row data). When condensing extract → map, classify every entry's kind — never summarize away
  *where a string lives in code*. Every map field must be traceable back to named inventory
  entries. (§4's extractor is the derivation tool; this rule governs the condensation step that
  consumes its output — that step is where HES's error was born.)
- **Field checklist at map-authoring time** (once per collection, at modeling — cheap here,
  expensive anywhere later): **(1) reader trace** — no FE reader → no field, no edit surface
  (HES shipped two reader-less columns); **(2) derivability** — computable from another field →
  not editable data, derive at render; **(3) contradiction pairs** — two fields that must agree =
  one field or a reference, never a validation patch; **(4) dropdown audit** — each choice set is
  truly-fixed / free-text-in-disguise / operator-growable, and each of the three gets a different
  shape; **(5) lifecycle walk on paper** — create → partial → publish → unset → unpublish must
  leave nothing stale or contradictory visible on the public site.
- **Vocabularies are data (the taxonomy pattern).** Any status/category set an operator will grow
  lives in its own small collection — per-locale display text, normal publish workflow — and rows
  **reference** it by FK. Never a hardcoded enum plus a *per-row free-text label* field (HES DL-21 was
  that mistake; the fix — DL-23/DL-22 — splits by the item-(4) audit: a **truly-fixed** set keeps its
  enum with labels **defined once** in ui-strings/localized, an **operator-growable** set becomes its
  own collection referenced by FK — never a per-row label that drifts, goes stale, or is re-typed per
  row per locale).

### 5.3 Verification additions

- **Adversarial editor pass in every stage gate:** deliberately produce nonsense — contradicting
  field pairs, set-then-unset leftovers, publishing half-filled entries — and check the **public
  render**, not just admin state. (Both HES model bugs survived types, lint, 167 tests, RLS
  suite, and a happy-path manual walkthrough; a human trying to break it found them in minutes.)
- **Provenance citations in decision Whys:** any factual claim that justifies a decision cites
  its artifact — file + line, migration, commit. Sessions sometimes confabulate plausible origin
  stories with full confidence; a citation is checkable in seconds, an assertion costs an
  investigation. (HES: DL-21's Why encoded a false origin — "2.c3a invented the enum" — for a
  column actually born in the 2.a schema from the map's ambiguity; human skepticism was the only
  thing that caught it. DL-21 was later superseded by DL-23, whose Why cites the inventory directly.)

## 6. What NOT to carry over

- HES's tokens, copy, domain model, `library.json` pipeline specifics, and the orrery — HES-only.
- HES planning docs as authorities — VECTO writes its own (this brief just seeds them).
- The Lovable chapter — dead end, fully retired; VECTO starts on the self-build architecture.
- Any live schema/code sharing with HES — regardless of whether the literal copy happens.
  If code is copied (likely admin/backend only, unsettled), it diverges permanently from the
  moment of copy; no synchronization in either direction, ever.

---

*Provenance: distilled from the HES project's session memory + decision record
(`HES-selfbuild-migration-plan-v2.5.md` §9), the refactor aftercare record
(`HES-refactor-aftercare-checklist.md`), and the 2026-07-08 retrospective conversation
(naming contracts, FSD sequencing, vocabulary translation); §5 added from the 2026-07-16
content-modeling retrospective (HES DL-21/DL-22 + the autosave gaps). Where this brief and a
future VECTO doc disagree, the VECTO doc wins.*
