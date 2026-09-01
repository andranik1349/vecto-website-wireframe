# VECTO Docs Refactor — Plan v2 (hygiene fixes + corpus restructure, one pass)

> **⚑ EXECUTED & ARCHIVED 2026-07-17.** All six phases ran to completion the same day (decisions
> D-08/D-09/D-10; change report delivered). Kept as historical record per Andranik's call —
> the plan itself said "delete when done," archiving supersedes that. The living corpus and its
> map: `docs/README.md`.

**What this is.** The plan for a one-time reorganization of the project's documentation: the
doc-hygiene fixes from plan v1 (decision **D-07**) **plus** the tiered corpus restructure agreed
with Andranik on 2026-07-17 — executed as a single pass so no file is edited twice. This is a
**snapshot**: written to steer this one cleanup, not maintained afterward. **Delete this file once
the plan is executed and verified** — its lasting outputs are the new corpus, `docs/README.md`,
`wireframe/docs/`, and the new decision-log entries.

**Supersedes:** plan v1 (2026-07-15, this same file). v1's Phase A (deleting the dead snapshot
`vecto-session-findings-2026-07-10.md`) is already done — verify in Phase 0. Everything else from
v1 is folded in below.

**Audience.** Andranik (non-engineer) + the session that executes this. Plain language throughout.

**Scope fence.** Touches: the non-legacy contents of `docs/`, plus updates `wireframe/CLAUDE.md`'s
stale source-doc pointers. Does NOT touch: `docs/legacy/**` (fully frozen — nothing moves out of
it, per Andranik 2026-07-17), the wireframe HTML/CSS/JS itself, any code, or the claude.ai
project memory (memory updates are listed as a follow-up, not an edit here).

---

## Locked decisions (Andranik, 2026-07-15 + 2026-07-17)

1. **Convert the two HTML docs to markdown** (v1 decision — markdown is what future sessions can
   grep, diff, and safely rewrite).
2. **IA history goes to the central decision log** (v1 decision — the ~31 dated trails).
3. **Tiered corpus** per the target tree below; `VECTO-Build-Plan` is renamed and split — the
   top tier becomes **`project-outline.md`** (locked decisions, workflow, contracts), with
   per-area architecture docs beneath it.
4. **Two corpora, physically separated.** `docs/` = the production-build corpus (moves to the
   production repo when the build starts). **Future wireframe-maintenance artifacts live in
   `wireframe/docs/`, inside the wireframe repo** (folder created at first need, not now) — each
   corpus travels with the codebase it describes. Nothing wireframe-maintenance-scoped may sit in
   the production corpus. The already-archived wireframe docs **stay in `docs/legacy/` untouched**
   (Andranik, 2026-07-17); `wireframe/CLAUDE.md` gets its pointers fixed to aim there.
5. **README and Project Outline are two docs.** `README.md` = the corpus map (who owns what,
   doc-keys, maintenance rules). `project-outline.md` = content (locked decisions one line each
   citing D-IDs, workflow, phase spine, standing contracts).
6. **Species rules per tier (the anti-290KB rule).** A *build plan* holds one row per feature —
   slug ID, one-line scope, status, pointer to its spec — plus ONE sequence/dependency block;
   nothing else. Each *feature spec + code prompt* is its own snapshot file in `specs/`, archived
   when consumed. *Why* goes to the decision log. Stage IDs are content slugs, never sequential
   letters/numbers.
7. **IA ↔ wireframe fact split.** The **IA md owns structure** (routes, nav, per-page block
   tables, the taxonomy lists — the citable home). The **wireframe owns full placeholder copy and
   rendered UX**. Nuance: the IA keeps its block-level copy *directives* (hero headlines, FAQ
   question lists, CTA labels — they are part of the block spec); what it never carries is full
   body copy. Arbitration: IA wins on structure, wireframe wins on copy/interaction detail; any
   mismatch is a bug to fix, not a fork to live with. Structural changes must land in both —
   an encoding-sweep obligation.
8. **No empty scaffolds.** Planned-but-unwritten docs (`page-building-guide.md`, `tokens.md`,
   the `specs/` contents) are NOT created as empty files. `README.md` lists them as planned
   homes with their creation trigger.
9. **Doc-keys.** Every corpus doc registers a short citation key in `README.md`
   (`outline`, `ia`, `fig-conv`, `f2c`, `fe-arch`, `fe-plan`, `be-arch`, `be-plan`, `log`).
   Cross-doc references use doc-key + locator (`fe-arch §3`), per doc-hygiene rule 5.
10. **IA reconciliation ID alias.** The 2026-07-03 set is cited as **`IA-D1…IA-D18`** (living in
    `docs/legacy/plan-ia-update-audit.md`), resolving the `D-04` vs `D4` collision.

## Target end state

```
docs/                          ← production corpus (→ production repo at build start)
  README.md                    corpus map, doc-keys, maintenance rules      [living]
  project-outline.md           locked decisions (cite D-IDs), workflow,
                               phase spine, standing contracts,
                               verification instruments                     [living]
  decision-log.md              unchanged in role                            [append-only]
  ia.md                        site structure — from vecto-master-ia-revised.html,
                               de-archaeologied                             [living]
  front-end/
    figma-conventions.md       variables, token authoring/sync, naming,
                               file organization        (f2c §1–5, §10)     [living]
    figma-to-code.md           handoff: prop mapping, text/effect styles,
                               typeface, content-model annotation scheme,
                               naming contract           (f2c §6–8, §12)    [living]
    architecture.md            shadcn customization, setup/tooling,
                               SSG/portability rules, structural lessons,
                               FSD structure              (f2c §9, §11, §13
                               + Build Plan Phases 4–6 rules)               [living]
    page-building-guide.md     (planned — created when page patterns stabilize)
    tokens.md                  (planned — created when the token spec is authored;
                               seed material: explorations/token-variant-spec-draft.md)
    build-plan.md              FE stage table + sequence block              [living]
    specs/                     (planned — one snapshot per feature: spec + code prompt)
  back-end/
    architecture.md            Supabase CMS, admin, entry lifecycle,
                               editor-created template pages
                               (Build Plan Phases 7–8b + backend section)   [living]
    build-plan.md              BE stage table + sequence block              [living]
    specs/                     (planned — same pattern as front-end)
  legacy/                      fully frozen — nothing moves in or out

wireframe/docs/                ← home for FUTURE wireframe-maintenance artifacts (plans,
                               prompt sets, ledgers), inside the wireframe repo. Created at
                               first need. Existing archived wireframe docs stay in
                               docs/legacy/; wireframe/CLAUDE.md points at them there.
```

Home-of-fact map (the one-home-per-fact assignments — final version lives in `README.md`):

| Doc-key | Owns | Points to, never restates |
|---|---|---|
| `log` | the story of every decision (what/why/superseded) | — |
| `readme` | the corpus map itself, doc-keys, maintenance rules | every other doc |
| `outline` | locked top-level decisions (one-liners), workflow, phase spine, standing contracts, verification instruments | D-IDs; area docs for detail |
| `ia` | site structure: routes, nav, per-page blocks, taxonomy lists, entity nouns | D-IDs for "why changed"; wireframe for full copy |
| `fig-conv` | how the Figma file is authored: variables, naming, token sync discipline | — |
| `f2c` | how Figma translates to code: prop mapping, annotation scheme, typeface, naming contract | `fig-conv` for authoring rules |
| `fe-arch` | how the front-end is built: shadcn customization, SSG/portability, FSD, setup | `f2c`; D-IDs |
| `be-arch` | how the backend/CMS/admin is built | `fe-arch` for shared primitives; D-IDs |
| `fe-plan` / `be-plan` | stage rows + the sequence block; nothing else | `specs/` per stage |
| wireframe (repo + its docs) | full placeholder copy, rendered UX, prototype conventions | `ia` for structure |

## Findings this resolves (from v1, updated)

1. ~~Dead snapshot in the corpus~~ — already deleted (verify Phase 0).
2. Living docs retell decisions instead of citing D-IDs (Build Plan + f2c §9/§11 narrate D-04).
3. ~31 dated annotation trails in the IA.
4. Hardcoded counts a list already answers ("13 industries", "~70 component pages", "309 text styles").
5. Two big docs are HTML.
6. No corpus map; `D-04` vs `D4` ID collision.
7. *(new)* The Build Plan is one doc holding five species — the HES-290KB failure shape.
8. *(new)* `VECTO-website-inheritance-brief.md` (self-declared "starting capital, not a living
   tracker") sits unplaced in the living corpus.
9. *(new)* `wireframe/CLAUDE.md` cites source docs at `../docs/` paths that moved to `legacy/`
   on 2026-06-30 — stale pointers in a binding doc.

## The plan, phase by phase

Before any editing starts, make ONE pre-refactor backup: copy the current `docs/` to a dated
backup folder Andranik can restore from. That single snapshot is the rollback path for the whole
refactor — no per-phase backups (git takes over versioning when the corpus moves to the repo).

### Phase 0 — Preflight *(direct)*
1. Back up `docs/` (dated copy). Verify v1's Phase A is complete: `vecto-session-findings-2026-07-10.md`
   absent, its substance present in D-04/D-05/D-06.
2. Draft the new decision-log entries (appended in Phase 1, cited everywhere after):
   - **D-08 — Tiered docs corpus & two-corpora separation** (the tree, species rules per tier,
     snapshot specs/prompts convention, doc-keys, IA-D alias, wireframe docs live in the
     wireframe repo, corpus moves to the production repo at build start).
   - **D-09 — IA ↔ wireframe fact split & arbitration** (locked decision 7 above).
   - The Phase 4 de-archaeology will add further entries (or fold minor ones into existing).

### Phase 1 — Skeleton *(direct)*
1. Append D-08, D-09 to `decision-log.md`.
2. Create `docs/front-end/`, `docs/back-end/`.
3. Write `docs/README.md`: corpus map table, doc-key registry, planned-homes list with creation
   triggers (including `wireframe/docs/` as the future wireframe-maintenance home), maintenance
   rules (species reminder + the D-07 encoding sweep), and the two-corpora rule.
4. Fix `wireframe/CLAUDE.md`'s source-doc pointers: its cited docs live at `../docs/legacy/…`
   (they were archived 2026-06-30; the pointers never followed). No files move.

### Phase 2 — Split `figma-to-code-decisions.md` *(review-first)*
1. Distribute sections per the target tree (§1–5, 10 → `fig-conv`; §6–8, 12 → `f2c`;
   §9, 11, 13 → `fe-arch`), folding in v1's Phase C fixes in the same motion: replace the §9/§11
   backend narration with one-line D-04 cites; delete the dead-option trail (already recorded in
   D-04 *Supersedes*); replace §2/§7 count enumerations with "enumerate live via the Plugin API";
   drop the manual "_Last updated_" line.
2. The original file is dissolved by the split. Leave nothing behind under the old name; sweep
   all references to `figma-to-code-decisions.md` (Build Plan text, wireframe CLAUDE.md, memory —
   memory flagged for follow-up, not edited here).
3. Present the proposed section-to-doc assignment before writing.

### Phase 3 — Split the Build Plan → outline + architecture docs *(review-first)*
1. Convert from HTML while splitting (one pass): TL;DR + workflow + standards/contracts +
   verification instruments + phase spine + pitfalls → `project-outline.md`; Phase 4–6 build
   rules → `fe-arch`; backend section + Phases 7–8b → `be-arch`; Phase rows that are genuinely
   plan-not-architecture → seed `fe-plan`/`be-plan` stage tables (slug IDs).
2. Replace every "settled 2026-07-10 / Lovable retired / Payload not adopted" retelling with
   D-04/D-05/D-06 cites. The outline keeps the architecture *description* one level deep;
   detail lives in the area docs.
3. Delete `VECTO-Build-Plan.html` after a fidelity diff (rendered text old vs. new corpus).
4. Present the proposed carve-up before writing.

### Phase 4 — IA: convert + de-archaeology *(review-first)*
1. `vecto-master-ia-revised.html` → `docs/ia.md`, preserving structure (headings, per-page block
   tables), in the same pass as the cleanup:
   - Sweep the ~31 dated trails; rewrite each sentence to current truth only.
   - For each stripped note: real structural decision → new `D-0x` entry; minor tweak → fold into
     the nearest existing entry or drop. Draft the entries.
   - Collapse internal count duplication (keep each list once; pointers elsewhere).
   - Cut the "Critique / Augmentation / original taxonomy" references from the living text
     (Andranik, 2026-07-17); one decision-log entry records those documents as the strategic
     origin of the IA. A cold reader has no access to them, so inline mentions are pure noise.
   - Apply the D-09 fact split: structure + block-level copy directives stay; anything that is
     full body copy points to the wireframe.
2. Present the full edit set + draft decision-log entries **before** touching the file.
3. Delete the old HTML after a fidelity diff.

### Phase 5 — Retire the inheritance brief *(review-first)*
1. Trace every VECTO-binding rule in `VECTO-website-inheritance-brief.md` to its new home
   (most already exist: outline contracts, `fe-arch` lessons, `be-arch` CMS doctrine, D-04–D-07).
   Anything homeless gets encoded now — likely candidates: the skills-routing filter (→ outline or
   the production repo's future CLAUDE.md), the §5 CMS/editor-experience doctrine (→ `be-arch`),
   the stage-ID rule (→ D-08 already).
2. Move the brief to `docs/legacy/` with a one-line header note ("mined into the corpus
   2026-07-17; see README map").
3. Present the trace table before moving.

### Phase 6 — Verify *(direct, mandatory)*
1. **Cold-read test:** fresh zero-context agent reads `README.md` → `project-outline.md` → one
   area doc chain; probe fact recall, retired-rule adherence, contradictions. Fix and re-test.
2. **Encoding sweep** over the corpus + `wireframe/CLAUDE.md`:
   grep for the changed terms — old filenames (`VECTO-Build-Plan`, `figma-to-code-decisions`,
   `vecto-master-ia-revised`), backend/Lovable/Payload retellings, the stripped IA phrases,
   count keywords, `D4`-style bare IDs. Classify every hit: updated / deliberately left.
3. **Report to Andranik:** what changed, what was deliberately left and why, new decision-log
   entries, and the follow-up list (memory files to update: `vecto-react-shadcn-rebuild`,
   `vecto-plan-ia-audit`, `use-doc-hygiene-skill` — all cite the old filenames).

## Verification greps

Run over `docs/` (excluding `legacy/`) + `wireframe/CLAUDE.md`:

- Old filenames: `grep -rn "VECTO-Build-Plan\|figma-to-code-decisions\|vecto-master-ia-revised" .`
  → zero hits outside `legacy/` and the decision log's Encoded-in lines (which are historical record).
- Stale language: `grep -rniE "SUPERSEDED|dual-path|Lovable|Payload|\bTBD\b|no longer certain" .`
  → only decision-log entries.
- Annotation trails: `grep -rnoiE "\((201|202)[0-9]-[0-9]{2}-[0-9]{2}[^)]*\)" docs/*.md docs/*/*.md`
  → near-zero outside `decision-log.md`.
- Bare counts: `grep -rn "13 industries\|11 subservices\|46 sub-service\|309 text styles\|~70 component" .`
  → only inside each list's single home.
- Unkeyed cross-references: spot-check that cross-doc cites use doc-key + locator.

## Risks & rollback

- `docs/` is not git-tracked → the single Phase 0 pre-refactor backup is the rollback path.
- Conversion fidelity (the 2,600-line IA) — convert, then diff rendered text before deleting HTML.
- Over-fragmentation — the tree adds files; the mitigation is the README map + doc-keys, and the
  no-empty-scaffolds rule. If a split doc turns out to be <1 screen of real content, merge it back
  and note it in the README.
- Faithfulness of Phase 2–5 rewrites — mitigated by the review-first gates.

## Resolved calls (Andranik, 2026-07-17 — no open questions remain)

1. **Legacy is fully frozen; nothing moves.** The archived wireframe docs stay in `docs/legacy/`;
   `wireframe/CLAUDE.md` pointers are fixed to aim there. `wireframe/docs/` is the home for
   *future* wireframe-maintenance artifacts only, created at first need.
2. **IA historical references are cut**, with one decision-log entry recording the
   Critique/Augmentation/original-taxonomy documents as the IA's strategic origin.
3. **The converted IA is named `ia.md`** (doc-key `ia`).

---

**Stop condition / done when:** the target tree exists and is populated; all findings resolved;
both corpora pass the verification greps; the cold-read test surfaces no new gaps; Andranik has
the change report + memory follow-up list. **Then delete this file.**
