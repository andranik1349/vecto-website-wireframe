# VECTO Docs — Corpus Map

**Role.** The living map of this documentation corpus: which doc owns which facts, the doc-key
citation registry, and the maintenance rules. Read this first in any session that touches docs.
Corpus structure and rules: decision **DL-08**. IA↔wireframe fact split: `ia` header §"Fact split".

## The two corpora

- **`docs/` (this folder)** — the production-build corpus, now git-tracked inside the wireframe
  repo (decision DL-23). It migrates to the front-end repo when that repo is created; until then
  the wireframe repo is its version control. Co-location does not make it wireframe documentation:
  it is the build contract for the production site, and it outlives the prototype.
- **`notes/`** (repo root, created at first need) — wireframe-maintenance artifacts (plans, prompt
  sets, ledgers). Wireframe-maintenance material never sits in this corpus, and never travels to
  the front-end repo.
- **`docs/legacy/`** — fully frozen reference. Nothing moves in or out; nothing in it is edited.
  Its paths describe the pre-DL-23 layout, where this corpus was a sibling of `wireframe/`; read
  those as history, not as current paths.

## Who owns what (one home per fact)

| Doc-key | File | Species | Owns | Points to, never restates |
|---|---|---|---|---|
| `log` | `decision-log.md` | append-only | the story of every decision: what, why, what it superseded | — |
| `readme` | `README.md` | living | this map, the doc-keys, the maintenance rules | every other doc |
| `outline` | `project-outline.md` | living | locked top-level decisions (one-liners citing D-IDs), the Figma→Code→GitHub→Vercel workflow, the phase spine, standing contracts, verification instruments | D-IDs for why; area docs for detail |
| `ia` | `ia.md` | living | site structure: routes, nav, per-page block tables, taxonomy lists, entity nouns; block-level copy directives | D-IDs for "why changed"; wireframe for full copy |
| `fig-conv` | `front-end/figma-conventions.md` | living | how the Figma file is authored: variables, token authoring & sync discipline, naming rules, what to keep/ignore in the file | — |
| `f2c` | `front-end/figma-to-code.md` | living | how Figma translates to code: component-property → cva mapping, text/effect styles, typeface, content-model annotation scheme, the verbatim-naming contract | `fig-conv` for authoring rules |
| `fe-arch` | `front-end/architecture.md` | living | how the front-end is built: setup/tooling, SSG & portability rules, production repo conventions, component/template build conventions, structural primitive lessons (the FSD map itself is a build-Phase-0.5 deliverable) | `f2c`; D-IDs |
| `guide` | `front-end/page-building-guide.md` *(planned — created when page patterns stabilize, ~Phase 6 of the build)* | living | the common contracts applicable to all pages | `fe-arch` |
| `tokens` | `front-end/tokens.md` *(planned — created when the token spec is authored, build Phase 1; seeds: `token-variant-spec-draft.md` and `font-strategy.md` in the repo-root `explorations/` folder)* | living | the VECTO token spec: branded ramps, semantic utilities, fluid type | `fig-conv` for sync discipline |
| `fe-plan` | `front-end/build-plan.md` *(planned — created at build kickoff, when the outline's phases decompose into slug-ID stages)* | living | FE stage table (slug · one-line scope · status · brief pointer) + ONE sequence block — nothing else | `front-end/briefs/` per stage |
| `be-arch` | `back-end/architecture.md` | living | Supabase CMS, custom admin, entry lifecycle/autosave/publish gating, editor-created template pages | `fe-arch` for shared primitives; D-IDs |
| `be-plan` | `back-end/build-plan.md` *(planned — created at build kickoff, same trigger as `fe-plan`)* | living | BE stage table + sequence block — same rules as `fe-plan` | `back-end/briefs/` per stage |
| `cms-checklist` | `back-end/cms-pre-build-question-checklist.md` | living | the pre-build interrogation checklist for the CMS/admin (HES-derived gotcha classes) — binds at Phases 8–8b, per system + per screen | `be-arch` / `outline` for the settled answers it verifies |
| `content-screen` | `content/seo-deliverable-screening.md` | living | the content acceptance criteria (B-1…B-6, C-1…C-16) — their only home — plus the diagnostic tells for briefs, drafted copy, and on-page recommendations. Author-agnostic: binds in-house and contracted drafts alike | `ia` for structure and the industry/Service-Areas rules; `content-vocab` for the evidence |
| `content-vocab` | `content/seo-pushback-vocabulary.md` | living | the published-guidance basis for those criteria: the positioning/AI-slop case plus the Google citations, each with its recency stated. A criterion untraceable here gets changed, not enforced | `content-screen` for the criteria; `ia` §"Guiding principles" for the principle |
| — | `content/reviews/` | snapshots | one file per dated review of content drafts: findings as `content-screen` criterion IDs + verbatim evidence. Written once, never maintained | `content-screen` for the criteria; `ia` for structure |
| `skills` | `skills-routing.md` | living | the skill-usage ritual (declare session type → load → name in report), the research-before-design pass, how its findings carry into a bespoke build, and its recency/scale-fit checks, the Cowork/Code routing maps, subject-matter override, design-skill suppressions | `fe-arch` §4 for the scaffold-time encoding |
| — | `front-end/briefs/`, `back-end/briefs/` *(planned — created with the first brief)* | snapshots | one 1–2 page brief per stage (DL-20): goal, constraints cited, out-of-scope, runnable acceptance checks — decisions inlined, measurements never; moved to a `briefs/archive/` when consumed | — |
| — | the wireframe (`wireframe/` repo) | living artifact | full placeholder copy, rendered UX, prototype conventions (its own `CLAUDE.md`) | `ia` for structure |

Dissolved/retired in the 2026-07-17 refactor: `figma-to-code-decisions.md` → `fig-conv` / `f2c` /
`fe-arch`; `VECTO-Build-Plan.html` → `outline` / `fe-arch` / `be-arch`;
`vecto-master-ia-revised.html` → `ia`; `VECTO-website-inheritance-brief.md` → mined into the
corpus, archived in `legacy/`.

## Citation grammar

- Cross-doc references are **doc-key + locator**: `fe-arch §3`, `ia §"Services hub"`, `outline
  §"Standing contracts"`. Locators name a real numbered section or an unambiguous heading (a
  unique leading fragment is fine). A bare `§N` is legal only within the same document.
- Decisions are cited by ID (`DL-08`), never retold. The 2026-07-03 IA reconciliation set is cited
  as **`IA-D1…IA-D18`** and lives in `docs/legacy/plan-ia-update-audit.md`.
- Stage/feature IDs in build plans are **content slugs** (`estimate-form`, `facet-landings`) —
  stable, citable, incapable of implying order. Sequence lives only in the plan's sequence block.

## Maintenance rules (the short version — full rules: the doc-hygiene skill)

1. **Species first** — decide living / append-only / snapshot before writing; each has opposite
   maintenance rules (doc-hygiene skill, §species — the single home of the portable rules).
2. **One home per fact** — a fact that would force an edit here when it changes, where here isn't
   its home, becomes a pointer (skill rule 1).
3. **No counts/lists a source can answer — in any species** (skill rule 2). VECTO's live sources:
   the directory tree, the Figma Plugin API, the data itself. A dated measurement is still a
   measurement.
4. **Rewrite, don't annotate** (skill rule 3) — history goes to the decision log by ID.
5. **Build plans never balloon.** One row per feature + brief pointer; the brief is a separate
   snapshot file in `briefs/`. This is the anti-290KB rule (DL-08), and skill rule 7's size
   budgets (no line >~400 chars, living files <~1,500 lines) now back it mechanically.
6. **The encoding sweep rides the change** (skill ritual): grep scope proportional to the
   change, classify every hit, report — landing in the same commit/session as the change itself,
   never as a separate close-out pass.
7. **Receipts for provenance AND capability claims.** A claim about what an
   artifact contains, does, or lacks comes from opening or running it in the asserting session —
   or is written as a conditional. Negative claims need two independent probes. Full mechanics:
   the doc-hygiene skill §Verification; the build-method consequences: `outline` §"The build
   method".
8. **Research before designing.** Before designing any mechanism, architecture,
   or non-trivial technical approach, one research pass first — does the framework/platform
   already ship this, what do established tools or common practice do — named in the session
   report with recency/version, and checked for scale-fit against VECTO's actual constraints
   before adopting. Repo-reading answers "how does this code work," never "has this been solved
   before"; only the latter question justifies skipping a bespoke build. Ritual step: `skills`
   §"The ritual".
