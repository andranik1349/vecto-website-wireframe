# VECTO — Back-End Architecture

**Purpose.** How the content layer is built: the Supabase CMS, the custom shadcn admin, the entry
lifecycle, and editor-created template pages. **Doc-key: `be-arch` · Species: living reference.**

**Scope.** Backend/CMS rules only. The phase sequence and cross-cutting contracts live in
`outline`; front-end build rules in `fe-arch`; the content-model annotation scheme in `f2c` §4;
decision rationale in the decision log, cited by ID. Corpus map: `docs/README.md`.
**Companion instrument:** before building the system and before each admin screen, run
`cms-checklist` (`back-end/cms-pre-build-question-checklist.md`) — it interrogates what this doc
settles and surfaces what it doesn't.

---

## 1. The settled architecture (decision DL-04)

| Dimension | Settled choice |
|---|---|
| Framework | Next.js (App Router), greenfield — scaffolded as Next from day one |
| Rendering | Full SSG — the public site reads published content at build time; rebuild-on-publish via a deploy hook. Nothing of ours runs at runtime except the admin. |
| Content schema | Hand-built CMS on Supabase (Postgres). Versioned migrations only; no console-applied schema. |
| Admin | Custom shadcn admin at `/admin` — composed from the site's own primitives |
| Hosting | Vercel |
| Forms / newsletter | Providers (Formspree / email provider), not custom backend. Resist edge functions. |

Rationale, what this superseded, and the HES lineage: **DL-04** in the decision log. The one
capability with no HES precedent — editors creating pages from templates — is **DL-05** (§6 below).

## 2. Repo, Vercel & Supabase wiring

- **GitHub is the single source of truth** — the whole app lives in one repo: front-end, the `/admin`, and `supabase/migrations`. This is the review surface and the portability guarantee.
- **Vercel project created from the repo** — per-branch previews come free; production deploys on merge.
- **Dedicated Supabase project** — direct DB access, point-in-time recovery, cost ownership from day one. Schema changes ship as versioned migrations, never console-applied; publish → deploy-hook → rebuild.
- **No platform-local copy to get trapped in** — because everything (migrations included) lives in the repo and deploys to Vercel, lock-in is prevented by construction.
- Confirm the app builds and renders on Vercel **before** any content wiring begins.

## 3. The content layer

- **Generate the Supabase schema from the TypeScript entity types** (`fe-arch` §5): collections become tables, relations become foreign keys, media becomes Storage + URL columns.
- **RLS deny-by-default from day one** — anon has zero DB access on content tables; roles gate the write paths via a `SECURITY DEFINER` role-check function. The role model is **full RBAC** (decisions DL-11, DL-12): code-owned roles, runtime user↔role assignment — see §5. Service keys never reach the client.
- **Swap the placeholder module for real queries** — the single swap point per content type; presentational components don't change.
- **Locale × publish status lives in the schema from the first table** — translation tables carrying a per-locale `missing → draft → published` status, with JSONB revisions per doc per locale. The switcher and nav render what the CMS says is live.
- **Confirm rendered data flow as an outcome** — published content reaches the prerendered HTML at build time (view-source, not build logs — `outline` verification instruments).

## 3a. Content-model doctrine (how the schema gets derived — and stays honest)

- **Authority order, declared up front: rendered site (FE code) → content map → schema → prompts/config.** Each layer conforms *upward*. A check of prompt-against-schema is consistency, not correctness — if the schema never got validated against the map, downstream verification just replicates the error with confidence.
- **The content map is a content model, not a string inventory.** Every field it lists carries a **structural kind** —
  per-row datum / per-locale shared constant / derived-at-render / code-owned — plus the FE file that reads it. The
  drift-detector extract (`outline` instruments) is the derivation tool; when condensing extract → map, classify every
  entry's kind and never summarize away *where a string lives in code* — the condensation step is where modeling
  errors are born.
- **Field checklist, once per collection at modeling time** (cheap here, expensive anywhere later):
  1. **Reader trace** — no FE reader → no field, no edit surface.
  2. **Derivability** — computable from another field → not editable data; derive at render.
  3. **Contradiction pairs** — two fields that must agree = one field or a reference, never a validation patch.
  4. **Dropdown audit** — each choice set is truly-fixed / free-text-in-disguise / operator-growable, and each of the three gets a different shape.
  5. **Lifecycle walk on paper** — create → partial → publish → unset → unpublish must leave nothing stale or contradictory visible on the public site.
- **Vocabularies are data (the taxonomy pattern).** Any status/category set an operator will grow lives in its own
  small collection — per-locale display text, normal publish workflow — and rows **reference** it by FK. A
  **truly-fixed** set keeps its enum with labels defined once in localized ui-strings. Never a hardcoded enum plus a
  per-row free-text label field — that drifts, goes stale, and gets re-typed per row per locale.

## 4. Entry lifecycle, autosave & publish gating (decision DL-06)

Settled in the schema and proven at the first (pattern-setter) collection, **before** other
collections or the §6 template pages copy the pattern — never re-invented per collection.

- **Three states per entry, per locale:** `new` (no row yet) → `draft` (saved, not live) → `published` (live).
- **A published entry keeps a separate, private working draft** — the load-bearing rule. Publishing does not collapse the entry to a single live row; the schema holds the live published version *and* an in-progress draft behind it, per locale (reusing the per-locale JSONB revisions).
- **Autosave:** editing an unpublished draft writes straight to the draft row; editing a published entry writes to the **private working draft, never the live row**. Only an explicit publish promotes the draft to live. (Why this matters under rebuild-on-publish — one editor's publish shipping another's half-finished sentence — is DL-06's story.)
- **Publish gating:** every entry type declares mandatory vs optional fields **once, in that type's shared zod schema** (the "one schema per boundary" contract). A draft may be partial; the completeness check runs at the draft → published transition. Enforced identically in the admin (publish disabled + a list of what's missing) and on the server.
- **One save model per form, no exceptions without a written case.** Autosave, explicit save, publish/unpublish, and draft-of-published are designed as ONE coherent contract at CMS-spec time; every form obeys it. Any control that must deviate gets argued for in the spec, not discovered in QA — an editor must always be able to tell what's saved.

## 5. The admin — a custom shadcn UI at `/admin`

A real publishing interface for the marketing team, not a raw database view — composed from the
same shadcn primitives as the public site, so it's intuitive and looks like VECTO.

- **Field type drives the control** — the admin form for each content type is implied by the Figma field annotations (`f2c` §4): text inputs, rich-text editors, image uploads to Storage, selects, toggles, date pickers.
- **CRUD + publish/draft workflow + revisions** — per entity, per locale, on the §4 lifecycle.
- **Full RBAC — non-negotiable (decisions DL-11, DL-12).** RBAC = role-based access control: what each signed-in user
  may see and do is determined by their assigned role. **Roles and per-role permissions are code-owned** — defined in
  code, changed via deploy (tentative set: `superadmin`, `admin`, `editor`; extended in code if needed). **User
  management is runtime:** the (super)admin creates users and assigns/changes each user's role from the admin.
  Enforcement lives in the database (RLS + the §3 role-check path) and is mirrored in the admin UI, so the two layers
  can't disagree. The permission granularity (which collections/actions each role gates) is specced at the
  pattern-setter stage via the `cms-checklist` §2 control walk; the anonymous-role test suite (`outline` verification
  instruments) extends to *every* role — each role's attempted overreach must fail in CI.
- **Auth & credential provisioning:** email + password, JWT sessions; **no self-signup, no email verification, no
  email invites.** The (super)admin creates the credential pair (email + password) in the admin and delivers it to the
  person over a corporate channel; **first login forces a password reset**. Password resets are handled **manually by
  the (super)admin** (exact mechanics TBD at the Phase 8 spec). No 2FA at launch; a seeder creates the first
  superadmin.
- **Admin-only components stay in a clear admin namespace** (folder convention, noted in the repo's `CLAUDE.md`) so they don't bleed into the public site's component set or bundle. The admin is the only part of ours that runs at request time.
- **Security is a launch gate, not a retainer:** before the admin goes live with an editor login, a Supabase-literate developer adds indexes and audits the RLS policies on the write paths; a hired security review is non-negotiable (`outline` review gates).

## 6. Editor-created pages from templates (decision DL-05)

The one capability with no HES stage to copy: editors create brand-new pages from pre-built,
**code-owned** templates (the site carries a large, growing volume of SEO content). Sequenced as
its own pattern-setter track **after** the simpler collections are proven — CRUD, locale×status,
autosave, and revisions all work before the template builder rides on top.

- **Schema:** a page-instance content type — template type · slug · per-locale status · per-slot content · SEO fields — on the same translation-table + lifecycle pattern, with slug uniqueness.
- **Routing:** a data-derived catch-all route — one page prerendered per published instance × locale; the prerender list comes from the data, never a hardcoded list.
- **Admin:** a template-instance editor — pick a template, fill its slots. Templates stay code-owned (they're design, not editor-authorable); an instance only picks from the registered set.
- **A template registry** — which templates exist and each one's slot schema, so the editor knows what to offer and how to validate.
- **Same lifecycle & gating as the collections** (§4) — including mandatory-*slot* validation per the registry entry. It inherits the contract; it does not reinvent it.
- Because this is where the SEO-content volume lives: per-instance meta/OG is first-class, and the build must handle a big, growing prerender list efficiently.

## 7. Structural control: nav, page publish, and reusable sections (decision DL-21)

A CMS-operator requirement, high-level pending the Phase 8 spec pass (`cms-checklist`) — extends the CMS's reach
from *content* to the site's own *structural shell* (nav, page existence, page composition).

- **Navigation is data, not hardcoded order.** The top nav's items, dropdown/megamenu columns, and each entry's
  order and visibility are CMS-editable per locale — a small ordered `nav_item` collection (label, target
  route/link, parent/column, order, visible flag, locale) the front-end reads at build time to compose the
  rendered menu. `ia`'s described order (§"Primary navigation architecture") is the launch default it seeds, not
  an immutable structural fact.
- **Pages can be hidden independent of their content-completeness state.** Every page already carries CMS content,
  and §4's lifecycle (`new → draft → published`) already gates whether that content is complete enough to be live.
  This adds an orthogonal, page-level visibility record (published/hidden, per locale) that gates the page's
  nav/menu appearance and whether its route resolves at all — independent of its content passing §4. A page can be
  content-complete and still hidden, or vice versa. Hiding a page never requires a code change or redeploy; the
  next rebuild-on-publish picks it up.
- **Sections are reusable, independently toggleable placements.** A page section (e.g. the homepage's "AI
  positioning band") is modeled as its own entity, placed onto one or more pages via a page↔section join carrying
  its own order + show/hide flag per placement — not a block hardcoded into that one page's component tree. The
  section's internal content/layout stays code-owned (`fe-arch` §5's presentational-component convention); only
  its placement, order, and visibility are CMS-controlled. Deliberately short of a page builder: no freeform
  layout, no operator-authored new sections — placement/visibility only.
- **Same field-checklist discipline applies** (§3a) to all three new entities — nav items, page-visibility
  records, section placements get the reader-trace / derivability / contradiction-pair / dropdown-audit /
  lifecycle-walk pass at modeling time. **Same RLS posture applies too** (§3) — deny-by-default, write access
  gated through the existing RBAC role-check path; this introduces no new admin/auth surface, just three more
  content tables under the rules already in force.
- **Open for the Phase 8 spec, not settled here:** whether a hidden page 404s, 410s, or soft-404s; whether nav
  item targets validate against real routes at publish time. (The `ia` Appendix "Deferred" convention is a
  separate, content-ops/PM concern — not an architecture question this section owns.)
