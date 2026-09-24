# VECTO — Skills Routing & the Session Ritual

**Purpose.** Which skills load, when, for every session type — Cowork and Code. Adopted from the
HES recipe. **Doc-key: `skills` · Species: living reference.**

**Posture: the failure mode is using too FEW skills, not too many.** (Andranik's standing
complaint, 2026-07-26, on HES: doc-hygiene was the only skill running consistently, despite a
dedicated skills memory.) Nothing in this doc should ever read as a reason to skip one.

---

## The ritual — every session, every type

1. **Step 1 of every session: declare the session type and load its skills** (map below). This
   binds planning, gap-audit, decision-brief, and close-out sessions — not just build/prompt
   sessions. (The HES miss was structural: the rule was titled for "the prompt-writing session,"
   so every other session type fell outside it. Most Cowork sessions are those other types.)
2. **Name the loaded skills at the top of the session report.** A report naming none means the
   rule was skipped, not that none applied.
3. **Subject matter overrides session type:** anything touching **auth, roles, RLS, credentials,
   or schema** pulls `secure-code-guardian`, regardless of what kind of session it is.
4. **Before designing any new mechanism or architecture, one research pass first**: does
   the framework/library/platform already ship this, and what do established tools or common
   practice in this space do (official docs, community references) — checked before proposing a
   bespoke solution, not after. Name what was checked in the session report, the same way loaded
   skills are named. A report with no research line on a design decision means the pass was
   skipped, not that none was needed. **The findings carry into the derivation even without a
   verbatim fit**: adapt the closest match where one exists; where none exists, name which
   constraints the research showed to be load-bearing vs incidental, and which known failure modes
   shaped the bespoke design instead — a bespoke solution built after research should visibly
   differ from one built without it. **Two checks harden this pass**: (a) name the
   recency/version of what was found, not just the source — an undated doc/answer doesn't satisfy
   the check; (b) before adopting or adapting a researched pattern, name whether its
   scale/team-size/operational assumptions match VECTO's actual constraints (solo non-engineer
   operator, low editor count, no 3am failure mode — DL-04) — a pattern built for materially larger
   scale is a flag to adapt down or reject, not copy as-is.

## Session-type map — Cowork

| Session type | Load |
|---|---|
| any doc / plan / spec / prompt edit | `doc-hygiene` (binding) |
| gap audit · red-teaming unspecified scope · unfinishable gates | `the-fool` |
| shaping a stage that has no spec yet | `engineering:architecture` **or** `architecture-designer` — not both |
| any Figma work (read or write) | the matching `figma:*` prerequisite skill — `figma-use` before any `use_figma` call, `figma-generate-design`/`figma-generate-library` for building, `figma-design-to-code` before implementing a design (their descriptions mark them MANDATORY prerequisites) |
| memory consolidation | `consolidate-memory` |
| test strategy | `playwright-expert`, plus ONE of the `testing-strategy` / `test-master` family |
| reader-testing a doc | a zero-context cold-reader subagent (the doc-hygiene Reader Testing instrument) |
| auth · roles · RLS · credentials · schema — *any* session | `secure-code-guardian` |

## Session-type map — Code (written into the repo `CLAUDE.md` at scaffold, `fe-arch` §4)

- **Always-on:** `react-architecture-conventions` (all code work, admin included; wins on conflict
  with any older house style) + `doc-hygiene` (all long-lived docs).
- **Task-routed:** `react-expert` (component work) · `nextjs-developer` (anything Next-touching —
  verify version-sensitive claims by web search, Next moves fast) · `fullstack-guardian`
  (cross-stack DB→API→UI stages) · `secure-code-guardian` (per the subject-matter override; on
  VECTO that means the whole Phase 8 admin/RBAC/RLS track) · the first-party **shadcn skill** for
  component sourcing/CLI under two guardrails: never let it touch the token layer; never
  blind-merge upstream into customized primitives · `playwright-expert` for automating the SSG
  outcome checks.
- Everything off-stack in the skills plugin (Angular/Django/mobile/ML/…) is filtered out.

## Decision-support: banned only for re-litigating settled calls

Re-opening a settled decision (anything with a D-ID) is drift. But **red-teaming work that was
never specified is exactly what `the-fool` is for** — a blanket "decision-support is benched after
kickoff" reading left HES's planning gaps sitting open while the skill that catches them sat
unused. Same qualification for the architecture skills: benched for settled architecture,
legitimate for shaping genuinely unspecced stages.

## Design skills: Impeccable is the sanctioned one; the rest stay suppressed

- ✅ **Impeccable (`/impeccable …`) is the design skill for all DS-conforming work** — page builds,
  production components, refinement passes. It is sanctioned where the others are not because it is
  pointed at *our* system rather than carrying its own: `/impeccable document` derives `DESIGN.md`
  from what ships, and the detector's `design-system-font` / `-color` / `-radius` / `-font-size`
  rules then flag literal values falling outside our palette, type scale and radii. That makes it a
  mechanical guard on `f2c` §2a's semantic-tokens-only rule, which is what a repeatedly-violated
  prose rule is supposed to become.
  - ⚠️ **Those four rules are silent without a current `DESIGN.md`** — design-system checks are
    skipped when it is absent or lacks the values. Running `document` is therefore part of adopting
    the skill, not an optional extra; without it only the generic slop checks fire.
  - ✅ **A check that contradicts a deliberate decision gets an ignore with a `--reason`, recorded in
    the committed `.impeccable/config.json`** — never an argument, and never a silent workaround.
    The designer outranks the detector; the reason is what makes that reviewable.
- **`frontend-design` and `high-end-visual-design` remain suppressed for all DS-conforming build
  work** (wireframe maintenance, production components, page builds). They are greenfield
  "roll-the-dice, never repeat" skills: each injects its own aesthetic system — card
  architectures, nav-pattern bans, font choices — which contradicts a project where **the token
  stack is the source of truth for styling** (`fig-conv` §1) and exists specifically to converge
  on one language and kill drift. *(VECTO scoping note: exploratory concept work in the
  project-root `explorations/` folder — pre-DS by definition — was and remains a legitimate use;
  the suppression binds anything meant to conform to the design system.)*
- **`design-taste-frontend` is superseded by Impeccable.** Its one advantage was an audit-first,
  preserve-the-existing-system mode; its disqualifying gap was that it cannot detect a bespoke
  internal component layer and needs setup pointing it at ours. Impeccable has the first and closes
  the second, so there is no case left for running both.
