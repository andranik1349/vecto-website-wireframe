# VECTO Wireframe ↔ Master IA — Drift Report

**Date:** 2026-06-27
**Compared:** the completed `wireframe/` build against `docs/vecto-master-ia-revised.html` (39 page specs + nav/megamenu/footer spec).
**Method:** per-page structural + key-copy comparison (block/section inventory, mandated order, CTAs, nav & footer contents, hero headlines, FAQ questions, IA-verbatim copy). Body-copy wording was not diffed sentence-by-sentence.

## How to read this
Findings are grouped into the three requested categories, each item given a stable ID (`C#` contradictions, `M#` missing-from-build, `E#` extra-in-build) plus an `II#` section for inconsistencies that live **inside the IA itself** (surfaced during the build). Each item has a **severity** and a blank **Resolution** field to fill during the reconciliation pass — the decision being *update the IA to match the build* or *fix the build to match the IA*.

## What was treated as intentional (NOT drift)
By prior project decisions, these were excluded from findings: desktop-only (no mobile/hamburger/responsive); flattened design tokens; one representative example built per template family (siblings link to it); placeholder/believable copy where the IA gives none; Lucide icons + `.ph-figure`/`.media-ph` media placeholders; `.tmpl-banner` notices + placeholder-convention HTML comments on template pages; Service Areas/Country pages, Year pages, and the "Why VECTO" page being deferred/unbuilt; the AI-powered estimator standing in as a hard-wired prototype stub.

## Scorecard
The build is a high-fidelity match to the IA. Across all 43 built pages, every page's full IA block set is present and in mandated order, with hero headlines, FAQ questions, engagement-model sets, process steps/anchors, and the company-stage list all matching. Drift is concentrated in: (1) the homepage Industries block, (2) two stage cards on the Services hub, (3) the Our Work filter facets, (4) a handful of nav/footer additions, and (5) two IA-internal inconsistencies the build had to resolve.

| Category | Count | Highest severity |
|---|---|---|
| Contradictions | 6 | medium |
| In IA, missing from build | 4 | medium |
| In build, not in IA | 16 (3 med, rest low/placeholder) | medium |
| IA-internal inconsistencies | 2 | — |

---

## 1. Contradictions — IA and build openly disagree

**C1 — Homepage Industries block: grid vs editorial, count, and order** · *severity: medium*
IA homepage block 7 mandates a "13-cell grid with small icons," each tile linking to its Industry page, in the IA's Tech-first order. Build (`index.html`, "Depth in the industries we know best.") renders an editorial layout: 2 featured cards (Healthcare, Finance) + a 10-item index = **12 tiles**, with Healthcare & Finance promoted ahead of Tech. (Tied to II1 — the IA's own industry count is inconsistent.)
*Resolution:* **Split decision.** Layout → **update IA**: rewrite block 7 to describe the editorial 2-featured + index treatment (drop the literal "13-cell grid"); the Healthcare/Finance featured ordering is accepted as an editorial choice. Count → **fix build** to 13 (see II1). Net build change: homepage shows 13 tiles, splitting Travel/Hospitality and Retail/E-commerce.

**C2 — Services hub "Build" card collapses the sub-service taxonomy** · *severity: low*
IA Software Development taxonomy (spec 05) lists 11 distinct Build sub-services; the hub Build card (`services/index.html`) shows 8, merging three pairs into single links ("CRM / ERP Development", "Bot & Game Development", "SPA / PWA Development"). The hub's own design rationale says sub-services are listed "so the page also functions as a comprehensive index," which the collapse undercuts.
*Resolution:* **Canonical sub-service count = 11.** (a) **Fix build + update IA** — the Services **megamenu** MUST list all 11 Build sub-services separately (split CRM/ERP, Bot/Game, SPA/PWA); the IA megamenu spec currently shows the combined 8 and must be updated to 11. (b) **Update IA** — the services **hub** Build card may keep a narrowed/curated selection; reword the hub rationale to drop "comprehensive index" and frame the card as a representative selection (full list lives on the service page + footer). No build change to the hub card.

**C3 — Services hub "Grow" card collapses the marketing taxonomy** · *severity: low*
IA Marketing taxonomy (spec 07) lists 11 sub-services; the hub Grow card shows 8, combining items ("SEO · GEO · ASO", "PPC · SMM"). Same comprehensive-index concern as C2.
*Resolution:* Same as C2. **Fix build + update IA** megamenu to list all 11 Grow/Marketing sub-services separately (split SEO/GEO/ASO, PPC/SMM). Hub Grow card may keep a narrowed selection (update IA rationale wording).

**C4 — Services hub hero CTA count** · *severity: low*
IA block 1 specifies a single "CTA to Estimator." Build ships a dual-CTA hero ("Get an Estimate" + "See our work"). (Note: dual hero CTAs are the IA-sanctioned pattern on the homepage; the question is whether the hub should match.)
*Resolution:* **Update IA** — block 1 to specify a dual CTA ("Get an Estimate" + "See our work"), matching the homepage pattern. No build change.

**C5 — Our Work filter facets diverge from the mandated set** · *severity: medium*
IA block 2 names 8 facets: "Service · Industry · **Stage** · Technology · Platform · Country · Company size · **Outcome story**." Build (`our-work/index.html`) has 7 facets: Industry, Technology, Service, Sub-services, Platform, Country, Company size. The IA-named **Stage** and **Outcome story** facets are absent as filter chips; a **Sub-services** facet is present that block 2 doesn't list (though the design-rationale prose endorses "Service with subs"). See also M3, M4.
*Resolution:* **Mixed.** (1) Stage/Company-size → single facet: **fix build** (rename "Company size" chip → "Company stage") + **update IA** (drop the duplicate "Stage" entry). See M3. (2) Outcome story → **update IA**: describe outcome as the 4 on-page groupings, not a filter chip; no build change. See M4. (3) Sub-services → **update IA**: add it to the block-2 facet list (already endorsed by the rationale). No build change.

**C6 — Industries hub FAQ heading hard-codes a count** · *severity: low*
`industries/index.html` heading reads "Two questions we hear a lot." Both IA-specified prompts are present, so this is cosmetic, but the hard-coded "Two" will break if a question is ever added.
*Resolution:* **Fix build** — change heading to "Questions we hear a lot." (drop the count). Trivial edit; IA unaffected.

---

## 2. In the IA, missing from the wireframe

**M1 — Homepage industries: one cell short** · *severity: medium*
Build shows 12 industry tiles where the IA homepage block says "13-cell." Same root as C1 / II1.
*Resolution:* **Fix build** — show 13 industries (canonical count per II1). Resolved jointly with C1.

**M2 — AI Transformation hero CTA lacks the pre-filter** · *severity: low*
IA `services/ai-transformation` block 1: "See our AI work → (/our-work, **AI tag pre-filtered**)." Build links to plain `../our-work/index.html` with no filter parameter, so the destination isn't pre-scoped to AI work.
*Resolution:* **Fix build** — deep-link the CTA to Our Work with the AI/Technology filter pre-applied (query param/anchor the filter JS reads on load); small enhancement to `initFacetFilter` to honor a deep-link. IA intent satisfied as written.

**M3 — Our Work "Stage" facet absent** · *severity: low*
IA block 2 lists "Stage" as a facet distinct from "Company size." Build offers only "Company size" (which carries overlapping stage values). Part of C5.
*Resolution:* **One facet.** Rename build's "Company size" chip to "Company stage" (build change) and drop the duplicate "Stage" facet from the IA (update IA). Same axis, not a true omission.

**M4 — Our Work "Outcome story" facet absent** · *severity: low*
IA block 2 names "Outcome story" as a filter chip, on top of the 4 outcome groupings (block 3). Build surfaces outcome only as section groupings, not as a facet. Part of C5.
*Resolution:* **Update IA** — keep the 4 outcome groupings as the implementation; reword block 2 so "outcome" is a grouping, not a filter chip. No build change.

*(No other IA-specified blocks, list items, CTAs, FAQ questions, process steps, engagement models, or cross-links are missing — all verified present across the 43 pages.)*

---

## 3. In the wireframe, not accounted for in the IA

### Nav & footer (shared, appears on every page)
**E1 — AI Transformation band inside the Services megamenu** · *low* — IA places AI on the homepage as a separate band and explicitly keeps it out of the Services menu; the build adds an "AI Transformation — cross-cutting competency" band + CTA to the Services panel. *Resolution:* **Keep — update IA.** Document the AI band in the Services megamenu spec, and revise the IA rationale that said AI is homepage-only (it now appears in both places intentionally).
**E2 — Bold parent-category links prepended to each Services stage column** · *low* — IA stage lists contain sub-services only (no parent-category line item). *Resolution:* **Keep — update IA** to document the bold parent-category link heading each stage column.
**E3 — Closing CTA strips on all three megamenus** · *low* — Services ("Need it all? … Digital Transformation" + Get an Estimate), Who We Serve ("Browse all case studies"), How We Work ("Get a ballpark…" + Get an Estimate). IA panel specs define no such strips. *Resolution:* **Keep — update IA** to document the closing CTA strip on each of the three megamenu panels.
**E4 — Footer Services column has 8 entries** · *low* — AI Transformation + the 7 taxonomy categories + "All services →". IA footer spec says "Top-level service categories (7) + All services →." *Resolution:* **Keep — update IA** footer spec to 8 entries (AI Transformation + 7 categories + "All services →").

### Page bodies
**E5 — Technologies hub adds GitHub Actions + Nginx** · *low* — Infrastructure & DevOps card set; neither is in the IA's named list (tied to II2). *Resolution:* **Keep — update IA.** Add GitHub Actions + Nginx to the IA infra list (8→10), matching the IA's own "10-card" label and the 33 total. See II2.
**E6 — Process page "Tools we use" adds Notion + Linear** · *low* — beyond IA's "Slack, Jira, Figma, GitHub, etc." (the "etc." softens this). *Resolution:* **Keep as examples.** Within the IA's "etc." license; optionally note the list is illustrative. No build change.
**E7 — Tools hub names specific AI tools** · *info/placeholder* — GitHub Copilot, Claude, Cursor, where the IA gives only the category. Likely intentional placeholder fill. *Resolution:* **Keep as examples.** Note in IA that AI-tooling names are illustrative. No build change.
**E8 — Glossary index/hub page exists with no IA spec** · *medium* — `glossary/index.html` (hero + search, A–Z quick-jump, letter-grouped term index, closing CTA) has no full-page IA spec; the IA only has a glossary-**entry** "Mention." The footer/nav both link "Browse A–Z," so a hub is implied but never specified. *Resolution:* **Keep — update IA.** Add a first-class Glossary-hub page spec (Full tag, `/glossary`, block-by-block: hero + search, A–Z quick-jump index, closing CTA). No build change.
**E9 — Stage template shows concrete budget figures** · *low/placeholder* — `who-we-serve/early-stage-startup.html` block 5 lists priced tiers ($10–25k, $40–100k, from $8k/mo); IA says only "honest discussion of typical spend," no amounts. *Resolution:* **Keep** as placeholder concreteness. No IA change required (numbers are illustrative).
**E10 — Sticky Estimator CTA on the industry template** · *low* — `industries/healthcare.html` carries a `.sticky-estimator` bar attributed to build-plan §5, not the IA industry template's 9 blocks. *Resolution:* **Keep — update IA** industry template to document the sticky Estimator CTA.
**E11 — Extra named compliance standards on Healthcare** · *low/placeholder* — adds HITECH, HL7/FHIR, SOC 2 beyond the IA's HIPAA/GDPR examples. *Resolution:* **Keep** as appropriate industry-specific detail (placeholder). No IA change.
**E12 — Industries hub search empty-state** · *low* — "No match — but the practices usually transfer…" line; supports the IA-mandated search field. *Resolution:* **Keep** — supports the IA search field. No IA change.
**E13 — Get an Estimate hero trust strip** · *trivial/placeholder* — three reassurance chips ("~90 seconds · No email required · A recommended engagement model"). *Resolution:* **Keep** as supportive placeholder. No IA change.
**E14 — Get an Estimate second CTA "Prefer to write first?" → Contact** · *trivial* — IA block 8 specifies only the single Schedule-a-Call CTA. *Resolution:* **Keep** the secondary "Prefer to write first?" → Contact CTA. Minor; optionally note in IA. No build change.
**E15 — Schedule a Call added estimator cross-link block** · *low* — "Not ready to talk yet?" section; IA structure ends at block 6 ("What happens after"). *Resolution:* **Keep — update IA** Schedule-a-Call spec to add the "Not ready to talk yet?" estimator cross-link block.
**E16 — Schedule a Call per-specialist CTAs + live booking-summary card** · *trivial/placeholder* — "Book 15 min"/"Email me" + "Confirm 11:30" card go beyond IA block 3's "photos, names, roles, one-line bios." *Resolution:* **Keep** the per-specialist CTAs + booking-summary card as widget detailing. No IA change required.

### Considered and cleared (not drift, logged for transparency)
**E17 — 404 page** — `404.html` is covered by the IA's "Static / legal pages" Mention ("404 / Error pages — branded, with prominent search and links to top entry points"); the build matches that description. No action.

---

## 4. IA-internal inconsistencies (surfaced by the build — resolve at the source)

**II1 — Industry count: 12 vs 13** · The Services-adjacent **megamenu** "By industry" lists **12** items (Travel & Hospitality combined; Retail · E-commerce combined). The **Industries-hub spec** and the **homepage block** both say **13** and the hub enumerates 13 separate pages (Travel and Hospitality split). The build consistently follows the **12**-item combined version (megamenu, homepage, industries hub all show 12). Reconciliation needs a single canonical answer (12 combined or 13 split), then align homepage, megamenu, industries hub, and footer. Drives C1 / M1.
*Resolution:* **Canonical = 13 separate** (Travel and Hospitality distinct; Retail · E-commerce distinct). Align all surfaces to 13: **fix build** megamenu (split combined cells) + homepage (→13 tiles); **update IA** megamenu spec from 12→13. Industries hub spec + footer already list 13 — verify build matches.

**II2 — Technologies "Infrastructure & DevOps" count vs list** · IA block 4 names **8** technologies but labels the grid "**10-card**." The build honored the count by adding two unlisted techs (GitHub Actions, Nginx). Decide whether canonical is 8 or 10, and which items. Drives E5.
*Resolution:* **Canonical = 10.** Update IA to list all 10 (the existing 8 + GitHub Actions + Nginx); the "10-card" label and 33 total stand. No build change.

---

## Reconciliation outcome (pass complete — 2026-06-27)
All items resolved. Work splits into two streams:

### A. Build fixes (wireframe — feed into Claude Code prompts)
1. **Homepage Industries → 13 tiles** (C1/M1/II1): split "Travel & Hospitality" and "Retail · E-commerce" into separate tiles; keep the editorial featured + index layout.
2. **Megamenu → 13 industries** (II1): split the combined cells so the "By industry" panel lists 13.
3. **Megamenu Build + Grow stages → all 11 sub-services each** (C2/C3): split CRM/ERP, Bot/Game, SPA/PWA, SEO/GEO/ASO, PPC/SMM. (Hub cards stay narrowed.)
4. **Our Work facet rename** (C5/M3): "Company size" → "Company stage".
5. **AI Transformation CTA pre-filter** (M2): deep-link "See our AI work" to Our Work with the AI/Technology filter pre-applied; add deep-link support to `initFacetFilter`.
6. **Industries hub FAQ heading** (C6): "Two questions we hear a lot." → "Questions we hear a lot."

### B. IA edits (`vecto-master-ia-revised.html`)
1. **Homepage block 7** (C1): replace "13-cell grid" with the editorial 2-featured + index treatment.
2. **Industry count → 13 canonical** (II1): update megamenu spec 12→13; verify hub + footer already at 13.
3. **Services megamenu spec → 11 sub-services** for Build & Grow (C2/C3); reword Services-hub rationale: hub cards are a "representative selection," full taxonomy on service pages + footer (drop "comprehensive index").
4. **Services hub block 1 → dual CTA** (C4).
5. **Our Work facets** (C5/M3/M4): drop duplicate "Stage"; add "Sub-services"; describe "outcome" as the 4 groupings, not a chip.
6. **Document nav/footer additions** (E1–E4): AI band in Services megamenu (+ revise the "AI homepage-only" rationale); parent-category links on stage columns; closing CTA strips on all 3 panels; footer Services column → 8 entries.
7. **Technologies infra list 8 → 10** (E5/II2): add GitHub Actions + Nginx.
8. **Add Glossary hub page spec** (E8): Full tag, `/glossary`, hero+search / A–Z index / CTA.
9. **Document template additions**: sticky Estimator on the industry template (E10); "Not ready to talk yet?" estimator block on Schedule-a-Call (E15).
10. **Note as illustrative** (E6/E7): process-page tool list and Tools-hub AI-tooling names are examples; optionally note the Estimate secondary CTA (E14).

### C. No change — accepted as placeholder/illustrative
E9 (budget figures), E11 (extra compliance standards), E12 (search empty-state), E13 (estimate trust strip), E16 (schedule per-specialist CTAs), E17 (404 — already covered by the Static/legal Mention).
