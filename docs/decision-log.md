# VECTO — Decision Log

**Role.** The project's append-only **why-archive**: what was decided, what was rejected, and what it
superseded — so a later session doesn't re-litigate a settled call or re-attempt a dead end. **Never a
source of truth.** An entry summarises what was decided and carries the story behind it, but is never
where a rule is stated for enforcement — the living doc named in **Encoded in** is. The log sits in no
mandated read path — open it on demand ("why is it this way?", tempted to reverse something, writing a
retrospective).

**HES** throughout is the comparable client-site project built immediately before this one, on the same
stack and workflow; its shipped decisions and post-mortems seed several entries here. Its own decision log
uses this same `DL-` shape, so citations to it are written **`HES DL-85`**, never bare.

**Admission test.** An entry needs both halves: blast radius beyond the thing being built, **and**
expensive or contentious to reverse. Everything else states its rule in its living doc and stops there.
Maintenance mechanics — append-only, correcting a claim vs overruling a decision, the length tell — are
owned by the **doc-hygiene skill** §"The decision log" and are not restated here.

**How to use.** Living docs state current truth and cite decisions by ID ("…resolved to canon, DL-04")
instead of retelling the rationale. The **Encoded in** line is the sweep checklist: it names every living
doc that must reflect the decision, so a later reviser knows what to touch.

**ID scheme.** `DL-NN` — project-wide, chronological, **never renumbered**. Numbers are
non-contiguous where entries were retired — §"Retired IDs" resolves every gap.

**Reading a stale `D-NN` citation.** Entries carried a bare `D-` prefix before 2026-08-31 (DL-22).
Surviving entries kept their numbers and changed prefix only, so a cited `D-04` is this log's `DL-04`. A
cited ID with no `DL-` counterpart was retired: §"Retired IDs" names where its rule went, and its rows
deliberately keep the old `D-NN` shape because that is the shape still loose in the corpus. Separately, the 2026-07-03
IA reconciliation keeps its own set, `IA-D1`…`IA-D18` (+ `E1`–`E7`), scoped inside
`docs/legacy/plan-ia-update-audit.md`; cite that doc for IA-item rationale. Corpus map: `docs/README.md`.

---

## DL-01 · 2026-06-30 · Design system rebuilt in React on shadcn; primitive base = Radix
**Decision:** Rebuild VECTO's design system in React on shadcn primitives (the "Luma" preset as an optional
head-start), with the VECTO brand applied on top at the variable/token layer — shadcn is the substrate, not
the visual identity. The primitive base is fixed at Radix (`--base radix`) at the `create` step.
**Why:** One shared vocabulary across Figma and code, and battle-tested primitives (inputs, selects,
validation, dialogs) instead of reinventing them; the brand identity is unchanged and layered on. Radix is
shadcn's default and the most reliable target for AI codegen in Claude Code. **Base UI (MUI) was the
considered alternative** — deferred as forward-looking, revisited only if admin form UX later justifies the
non-trivial switch.
**Supersedes:** the prior custom red/dark Figma design-system effort (archived to `docs/legacy/`).
**Encoded in:** `fig-conv` §1 · `f2c` · `fe-arch` · `outline`.

## DL-03 · 2026-07-01 · Rendering posture = static-first (SSG), rebuild-on-publish
**Decision:** Target static generation with rebuild-on-publish, not per-request SSR.
**Why:** Cadence. No live feeds; real updates arrive roughly biweekly (blog/SEO/case studies), new service
categories rarely, and the interactive surface is near-zero — so a static build plus an on-publish rebuild
fits and no live server runtime is needed. Carried forward by DL-04.
**Encoded in:** `fe-arch` §2 · `outline` Phase 9.

## DL-04 · 2026-07-10 · Backend & framework resolved to canon
**Decision:** A greenfield **Next.js** (App Router) app, **full SSG**, with a **hand-built CMS on Supabase**
and a **custom shadcn admin at `/admin`**, deployed to **Vercel**; provider services (Formspree / email) for
forms rather than a custom backend; a hired security review as a non-negotiable launch gate. No migration or
refactor phase — scaffolded as Next from day one, with the HES scaffold-time gotchas applied (`fe-arch` §1).
**Why:** HES — comparable scope, same workflow — shipped exactly this backend, and VECTO inherits it as canon
until further revision. The operator constraint drives it: Andranik runs the site alone, and static-on-CDN has
no 3am failure mode. Note the gap between advice and outcome: HES's own v2.5 recommendation was Next +
Payload, but what actually shipped was a hand-built Supabase CMS, so VECTO follows the shipped reality rather
than the recommendation.
**Supersedes:** the dual-path "backend fork / decide before Phase 7" framing (Lovable + Supabase vs Next +
Payload); the "framework TBD / Vite-vs-Next / Lovable-no-longer-certain" language in the pre-refactor
front-end docs; and the Vite-native SSR meta-framework option (React Router v7 / TanStack Start).
**Encoded in:** `be-arch` §1 · `fe-arch` §1–2 · `outline` · memory `vecto-react-shadcn-rebuild`.

## DL-05 · 2026-07-10 · CMS creates pages from code-owned templates
**Decision:** Editors can create brand-new pages from pre-built, code-owned templates — templates stay design,
not editor-authorable; an instance only picks from the registered set and fills slots. Sequenced as its own
pattern-setter track after the simpler collections are proven. Mechanism: `be-arch` §6.
**Why:** VECTO carries a large, growing volume of SEO content, and this is the one capability with **no HES
stage to copy** — HES only field-edits fixed singletons and collections, so there is no prior implementation
to lean on and the stage has to prove itself.
**Encoded in:** `be-arch` §6 · `outline` Phase 8b.

## DL-06 · 2026-07-15 · CMS entry lifecycle, autosave & publish gating
**Decision:** Per entry, per locale, the lifecycle is `new → draft → published`; a published entry keeps a
separate private working draft that autosave writes to, and only an explicit publish promotes it. Publish is
blocked while any mandatory field is empty, with mandatory-vs-optional declared once per type in that type's
shared schema and enforced identically in the admin and on the server. Settled in the schema and proven at the
pattern-setter collection before anything copies it. Rules: `be-arch` §4.
**Why:** Building the HES CMS exposed two spec-level gaps. (1) With one row per translation, editing a
published entry wrote onto the live row — and because a rebuild fires on a debounced batch that any editor's
publish can trigger, one editor's in-progress edit could ship when someone else published something unrelated.
(2) The content path had no completeness contract, so every collection would reinvent "what's required before
publish" inconsistently.
**Encoded in:** `be-arch` §4 · `outline` standing contracts + Phases 8, 8b.

## DL-08 · 2026-07-17 · Tiered docs corpus & two-corpora separation
**Decision:** Restructure the production docs corpus into tiers with per-tier species rules, markdown
throughout, and doc-key + locator citations. Two corpora stay physically separate: `docs/` is the production
corpus and travels to the production repo at build start; wireframe-maintenance artifacts live in the
wireframe repo; `docs/legacy/` is fully frozen — nothing moves in or out. Structure and the doc-key registry:
`docs/README.md`.
**Why:** The HES build plan ballooned to ~290KB by holding five species in one file — plan, specs, prompts,
tracking, and decision history, each growing at its own rate and none of them prunable without risking
another. Tiering by species makes each doc's growth bounded by construction rather than by discipline.
Markdown is what future sessions can grep, diff, and safely rewrite; HTML fights every hygiene check. Separate
corpora keep wireframe-maintenance detail out of the production build's context, and each corpus travels with
the codebase it describes.
**Supersedes:** the single-doc `VECTO-Build-Plan.html` structure and the HTML form of the Build Plan and
master IA; v1 of the docs refactor plan (2026-07-15).
**Encoded in:** `docs/README.md` · `wireframe/CLAUDE.md`.

## DL-11 · 2026-07-17 · Admin ships with full RBAC
**Decision:** The admin's access model is full RBAC — what a signed-in user may see and do is determined by
their assigned role — as a non-negotiable requirement, enforced at the database layer (RLS + the role-check
path) and mirrored in the admin UI. As first specified, roles were **data**: their own tables with permission
grants, created and managed at runtime by a superadmin, with invitation-only account creation. **Narrowed the
same day by DL-12** — read that entry for what actually gets built.
**Why:** Stated by Andranik as a non-negotiable backend/admin requirement. The fixed two-role model inherited
from the HES-shaped baseline does not cover it.
**Supersedes:** the fixed `admin`/`editor` two-role assumption inherited from the HES-shaped baseline. (This
entry as first written also superseded the "admin-created accounts only" wording in favour of an invitation
flow; DL-12 reversed that the same day, so manual provisioning stands.)
**Encoded in:** `be-arch` §3, §5 · `outline` standing contracts + Phase 8 row.

## DL-12 · 2026-07-17 · RBAC scope narrowed: code-owned roles, manual credential provisioning
**Decision:** Refines DL-11. Roles and per-role permissions are **code-owned** — defined in code, changed via
deploy, not editable at runtime. What stays runtime is **user management**: an admin creates users and
assigns or changes each user's role. No email verification and no email invites — credentials are provisioned
directly in the admin and delivered over a corporate channel. Seeding, forced first-login reset, and reset
mechanics: `be-arch` §3, §5. *Open for the Phase 8 spec: whether user creation is superadmin-only or
available to any admin — the docs say "(super)admin" throughout and have never resolved it.*
**Why:** A conscious cost/benefit call for an in-house product with a strictly limited number of users. At that
scale a code-owned role set covers the real need, so no role-editor UI and no permission-grant tables get
built, and the admin carries no email-sending dependency — DL-11's requirement is met with a code-owned role
model plus one user-management screen.
**Supersedes:** DL-11's "roles are data, created and managed at runtime" — role *definitions* move to code;
and DL-11's invitation flow — replaced by manual credential provisioning.
**Encoded in:** `be-arch` §3, §5 · `outline` standing contracts + Phase 8 row.

## DL-20 · 2026-08-10 · Adopt the brief method — briefs + in-repo planning replace the code-prompt method
**Decision:** A build stage starts from a 1–2 page brief (goal and why, the standing contracts it touches,
out-of-scope, runnable acceptance checks); **Claude Code plans in-repo** in plan mode against the live repo,
verifies every load-bearing claim by execution or writes it as a conditional, and Andranik approves the plan
before code. Cowork's lane is product decisions, design, content, and briefs — never binding technical claims
about repo or runtime state. The code-prompt method is retired before it was ever exercised here, and this log
is simultaneously demoted to a why-archive. Method: `outline` §"The build method".
**Why:** Adopted from `HES DL-85`, a post-mortem run before VECTO's build started — the cheapest possible
moment. HES measured the old pipeline: prompts authored without repo or execution access shipped confident
false claims that three cold-reader passes still missed, while in-repo plan mode neutralized the survivors in
minutes and built a full stage cleanly from nothing but the plan docs. Roughly half of all commits had become
documentation overhead. The receipts discipline survives and gets stronger — the apparatus around it existed
only because the prompt author couldn't verify, and that author role no longer exists.
**Supersedes:** `outline` §"The code-prompt method" (rewritten in place); the `specs/` full-spec-plus-prompt
convention (now `briefs/`); the claim-inventory apparatus (its receipts core stands, `README` rule 7); DL-08's
"feature spec + its code prompt" snapshot wording.
**Encoded in:** `outline` §"The build method" · `README` maintenance rules + registry · memory
`vecto-cowork-lane` · portable form: doc-hygiene skill.

## DL-21 · 2026-08-18 · CMS structural control: nav, page visibility, reusable sections
**Decision:** The CMS must give an operator three structural controls beyond content editing, high-level
pending the Phase 8 spec: reorder and hide/reveal nav and submenu items per locale; unpublish any page
independent of its content-completeness state; and treat page sections as reusable, independently toggleable
placements rather than blocks hardcoded into one page's component tree. Section internals stay code-owned —
deliberately short of a page builder, with no freeform layout and no operator-authored new sections.
Mechanism: `be-arch` §7.
**Why:** Stated by Andranik as a basic CMS-operator requirement. The docs framed nav order and page
composition as design-time facts, with hide/reveal handled only pre-launch through a docs/code change — not as
an operator-facing runtime control. Both the schema and the front-end's nav/section composition therefore have
to become data-driven (order and visibility read at build time, still static-first per DL-03), which makes
this an architecture consequence on both layers rather than an admin-UI feature.
**Supersedes:** nothing — the page-level visibility gate sits alongside DL-06's per-entry lifecycle, not in
place of it.
**Encoded in:** `be-arch` §7 · `fe-arch` §5 · `ia` (nav-architecture + documentation-levels notes) ·
`outline` standing contracts + Phase 8 row.

## DL-22 · 2026-08-31 · Log cut to ten entries; IDs renamed to `DL-NN`
**Decision:** Eleven entries retired into the living docs that bind their rules, and the ID prefix changed
from `D-NN` to `DL-NN` with numbers unchanged and never renumbered. Admission now requires both halves of
the test in this header; the surviving entries are the ones holding a story a future session needs in order
to not reverse or re-litigate the call. Retirements and their new homes: §"Retired IDs".
**Why:** The log had reached 21 entries before a line of production code was written, and ten of those were
about how the project documents and prompts itself rather than about the product — the rate signal for a
why-archive drifting into a session diary. Most of the retired entries were standing live rules whose only
full statement had migrated here, which had made the log a source of truth it is explicitly not: `ia`
pointed *at* an entry for a provenance fact the entry owned, and `skills` step 4 duplicated a rule three
entries also stated. The prefix change removes a collision the corpus had been carrying from the start —
`D-18` sits one letter from the `IA-D18` reconciliation set, and both were live citations.
**Supersedes:** this header's former "decisions only, ~30 lines each" cap — a project fork of a portable
rule, where the real diet is the admission test and the real check is the entry rate.
**Encoded in:** this header · §"Retired IDs" · `README` maintenance rules + ownership table · `ia` header
§"Provenance & change history" + §"Guiding principles" · `skills` §"The ritual" · `outline` · `be-arch` ·
`fe-arch` · `content-screen` · `content-vocab` · `wireframe/CLAUDE.md` · memory `vecto-decision-log-ids`.

---

## DL-23 · 2026-09-01 · Docs corpus moved inside the wireframe repo; one repo until the FE repo exists
**Decision:** the production-build corpus (`docs/`) now lives inside the wireframe repo and is git-tracked
there. It migrates to the front-end repo when that repo is created, and not before. The reservation for
wireframe-maintenance artifacts moves from `wireframe/docs/` to `notes/` at the repo root. DL-08's *content*
separation is unchanged — wireframe-maintenance material still never sits in the production corpus.
**Why:** the corpus had no version control at all. Three manual `docs-backup-<date>/` folders at the project
root were serving as its history, alongside 14 orphaned FUSE saves of half-written docs; both are the
symptom of editing a load-bearing corpus with no undo. The trigger was an approved ~45% cut of `ia` (menu
listings that duplicate the doc's own site-structure sections, and per-page block enumerations that restate
rendered layout) — a deletion of that size is not safe unversioned. Standing up a second repo for one folder
was rejected as more ceremony than the separation is worth: the front-end repo will be new either way, so the
corpus travels once, at a moment already on the phase spine, rather than being born in a repo of its own.
**Supersedes:** DL-08's repo boundary (a corpus in its own tree, sibling to `wireframe/`) and its
`wireframe/docs/` path reservation. Nothing else in DL-08 changes; `docs/legacy/` paths that describe the
sibling layout are frozen history, not drift to fix.
**Encoded in:** `README` §"The two corpora" + the `tokens` seed pointer · `wireframe/CLAUDE.md` repo-layout
note + maintenance-artifact reservation + source-doc paths · `prototype/README.md` source-docs table · repo
`.gitignore` (`.fuse_hidden*`).

---

## Retired IDs

Retired in the 2026-08-31 sweep (DL-22). **No decision here was reversed.** Ten of these were standing live
rules whose only full statement had drifted into this log; the rule now lives where it binds and nothing was
left for a why-archive to hold. `D-02` is the one merge rather than a relocation — it failed the admission
test on its own and its content, including its rejected alternative, sits inside DL-01. Note the criterion
that kept DL-11 alive while these went: an entry whose *decision* was later overruled survives as the record
of the abandoned approach; an entry that never met the admission test does not.

Rows keep the old `D-NN` shape, because that is the shape still loose in the corpus — in the frozen
`docs/legacy/` set, in dated review snapshots, and in older memory files, all species that are never
maintained.

| Retired ID | Was | Where the rule lives now |
|---|---|---|
| `D-02` | Primitive base = Radix | folded into **DL-01** (with its rejected alternative) |
| `D-07` | Adopt doc-hygiene as a standing rule | `README` maintenance rules · `skills` Cowork map (binding row) |
| `D-09` | IA ↔ wireframe fact split & arbitration | `ia` header §"Fact split" · `README` ownership table |
| `D-10` | IA converted to markdown; provenance | `ia` header §"Provenance & change history" · badge definitions at `ia` §"Documentation levels" |
| `D-13` | Skill-usage ritual & routing map | `skills` §"The ritual" steps 1–3 (including the HES failure story) |
| `D-14` | Claim-verification discipline | `README` maintenance rule 7 · doc-hygiene skill §Verification |
| `D-15` `D-16` `D-17` | Research before designing, and its two hardening checks | `skills` §"The ritual" step 4 · `README` maintenance rule 8 |
| `D-18` `D-19` | Content integrity as a positioning requirement | `ia` §"Guiding principles" · criteria: `content-screen` · evidence: `content-vocab` · the 2026-08-05 incident: `content/reviews/2026-08-05-seo-content-review.md` |

Surviving entries kept their numbers and changed prefix only (`D-04` → `DL-04`), so a legacy `D-NN` citation
to a surviving entry resolves by prefix substitution.
