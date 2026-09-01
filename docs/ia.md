# VECTO Digital — Master IA & Navigation

**Purpose.** The master IA reference for the VECTO Digital website: every page, every navigation
entry, and every relationship between them — the canonical structural reference for design,
copywriting, and development. **Doc-key: `ia` · Species: living reference.**

**Fact split.** This doc owns **structure**: routes, nav, per-page block tables,
the taxonomy lists, entity nouns — plus block-level copy *directives* (hero headlines, FAQ
question lists, CTA labels). The **wireframe** (`wireframe/` repo) owns the full placeholder copy
and rendered UX; this doc never carries full body copy. Arbitration: this doc wins on structure,
the wireframe wins on copy/interaction detail; any mismatch is a bug to fix, not a fork. Every
structural change lands in both.

**Provenance & change history.** This doc originated by merging the SEO-led "New website taxonomy"
sheet with the *IA Augmentation Proposal*, informed by the *Website Critique* — pre-project strategy
documents that live outside this corpus. All inline change-history was stripped at the markdown
conversion (dated decision trails, "per the augmentation/critique" attributions, origin-diff
framing); this doc states current structure only. The 2026-07-03 reconciliation history lives as
`IA-D1…IA-D18` + `E1–E7` in `docs/legacy/plan-ia-update-audit.md`. Corpus map: `docs/README.md`.

**Documentation levels.** Every page is documented at one of three levels: **full** treatment
(description, design rationale, block-by-block structure), **template** (reusable anatomy applied
to a class of pages), or **mention & placement** (named and located in the IA, structure not
detailed). Additional badges: **New** = the page does not exist on the current live site — no URL
to preserve; **Deferred** = parked in the Appendix, off all active surfaces — a pre-launch,
docs/code-level convention for content not yet built, distinct from the operator-facing runtime
page-hide capability that applies to any live page post-launch (decision DL-21, `be-arch` §7).

---

## Guiding principles

- **Non-technical founder first.** Every page, label, and CTA is written for a non-technical founder evaluating an outsource partner for the first time. Jargon is a conversion killer; plain language is non-negotiable.
- **Services grouped by transformation stage.** The site organises VECTO's offering into six stages of the digital
  transformation journey — **Discover & Validate, Design, Build, Grow, Scale, Maintain**. Each stage maps to one (or
  more) of the service categories. This grouping is the structural backbone of the megamenu, the Services hub, and the
  homepage Services section. URLs and underlying taxonomy are unchanged — the stages are a presentational layer that
  makes the end-to-end narrative legible at a glance.
- **Engagement process is a separate axis.** Distinct from the 6 service stages, the engagement process describes how
  any single project runs from start to finish: **Kickoff → Scoping → Execute → Launch → Iterate**. It applies
  regardless of which service is being delivered. Vocabulary is deliberately chosen to not overlap with the service
  stages (no "Discovery", no "Build", no "Support") so the two axes never blur in the reader's mind.
- **Build is the primary stage.** Of the six service stages, Build (Software Development + AI Transformation) is the most-requested by inbound leads. Where the IA gives weight, prominence, or default ordering — Build gets it.
- **Outcome-led, not capability-led.** Every hub and page leads with what changes for the client, not what category of work it represents.
- **SEO foundation preserved.** URLs, taxonomy depth, and on-page H1s remain unchanged. Improvements happen at the labelling, layout, and component level — never by destroying ranking surface.
- **Content may not contradict the positioning.** The search engine brings the reader; the reader
  decides whether to make contact. Content optimized for the first at the expense of the second is disqualified on
  positioning grounds — VECTO sells slop-free AI output and cannot sell it in slop, keyword-stuffed or generated.
  Discoverability and human credibility are not a trade-off here: the writing that earns a founder's trust is the
  writing Google's current guidance rewards. Binds every draft regardless of author — content/SEO, design, or
  contracted. Screening rules: `content-screen`; the published-guidance evidence behind them: `content-vocab`.
- **Process visibility everywhere.** "How we work" is referenced from the homepage, every service page, every industry page, and every case study — addressing the #1 founder objection pre-emptively.
- **Mid-funnel is the missing layer.** The Get an Estimate flow is the universal mid-funnel CTA, surfaced via sticky elements on service / industry / case study pages. Naming rule: everything reads **"Get an Estimate"** — the "Project Estimator" product/tool name returns only with the AI estimator (Appendix).
- **Non-destructive additions over restructures.** Every recommendation that can be additive is additive; restructures are reserved for problems that cannot be solved any other way.

## Localization

### Three languages, one structure

The site is multilingual: English (default) at launch; Armenian and Russian at or soon after launch. The structural rules are fixed now — retrofitting locale routing is expensive — while the translation scope (which pages go live in HY/RU first) is a content-ops plan made with the SEO team at translation time. The mechanism supports any page going live in any language independently.

- **URL scheme — bare English, prefixed translations.** EN lives at today's paths unchanged (existing pages like
  `/about/` keep their rankings untouched). Translations live at locale-prefixed paths: `/hy/…`, `/ru/…`. hreflang
  tags link each translation set. The case-study URL contract composes cleanly: `/projects/[project-name]` is the
  (verbatim-preserved) EN form; translations sit at `/hy/projects/…`.
- **Per-language publish, hidden when absent.** Every page and content entity publishes per language independently. A locale's nav, footer, and megamenus render only what is published in that locale — never English content under an `/hy/` URL, never a placeholder page.
- **Language switcher — visible only when it has a job.** Header utility area. Rendered only when more than one
  language is published: an English-only site shows no switcher at all (the HES rule). On a page whose translation
  doesn't exist, the switcher links to the nearest translated ancestor — usually the locale homepage — never a 404.
  Mobile: the switcher lives in the drawer; the Get an Estimate CTA keeps its persistent header spot.
- **Build consequence.** The route list multiplies per published language at build time; the site remains fully static. Adding a language is a publish action, not an engineering project.

## Primary navigation architecture

> **This section is the launch default, not a fixed structural fact.** Item order, submenu/megamenu
> composition, and hide/reveal are CMS-editable per locale at runtime (decision DL-21, `be-arch` §7);
> this doc's structure below is what the nav is seeded with, arbitrated here on structure.

### Top-level menu

Eight slots in the primary navigation: seven content menus + one primary CTA button. Order is left-to-right by
buyer-journey priority for a non-technical founder: **What you do (Services · Solutions) → Who you do it for → Proof →
How you work → Resources → About → Estimate CTA**. Solutions — VECTO's own B2B/SaaS products — is a direct link (no
dropdown) beside Services, the second half of "what we offer." To accommodate the eighth slot the CTA button may
render more compactly — acceptable because the sticky/floating estimate CTA on every page carries the mid-scroll
conversion load regardless.

> **Mobile note.** At mobile widths the megamenu collapses to a hamburger drawer. Order remains identical. The "Get an Estimate" CTA stays visible in the mobile header bar even when the menu is closed — it does not collapse into the hamburger.

> **Language switcher.** Lives in the header utility area, but only exists once a second language is published — see Localization. English-only launch renders no switcher.

> **Menu-heading convention — label by default, link only where the link adds a destination.** Dropdown/megamenu
column headings are **non-interactive labels by default**. A heading becomes a link only when **both** tests pass:
a real destination page exists for it, **and** that page is not already reachable from inside the same column or
from the menu's own top-level trigger. The second test is what stops a heading from restating a link sitting
directly beneath it — a stage heading pointing at its own first sub-service, a "Blog" heading pointing where
"Latest posts" already goes, an axis heading pointing where its own nav trigger already goes. Grouping labels with
no page behind them stay labels by the first test; headings whose link would be a duplicate stay labels by the
second. **No invented hub pages, no next-best-option targets.** Interactive and non-interactive headings must be
visually distinct: in the prototype, interactive heading text renders in the accent red (text colour only — not a
button/pill), non-interactive labels stay muted grey; the final treatment is a Figma/design-system task (a new
component pair: nav heading-link vs nav label). Which headings are links today is deliberately not listed here —
the built nav (`wireframe/prototype/_nav.html`) is the inventory. Related convention: **menu placement ≠
hierarchy** — the About menu links standalone pages (Schedule a Call, Contact) as nav convenience; their URLs and
breadcrumbs stay root-level.

### Services megamenu — transformation-stage panel

Instead of listing service categories side-by-side as equals, the megamenu organises the six delivery stages as a
sequential transformation journey. This makes the end-to-end narrative visible at a glance and explains why Marketing
belongs alongside Development — both are stages of a product's life. AI Transformation sits apart from the six stages
as a distinct, cross-cutting block: it is not a milestone in the journey but a competency that runs through every
stage. Each stage column is headed by its parent service-category as a clickable link to that category's hub page, and
every megamenu panel (Services, Who We Serve, How We Work) closes with a CTA strip — e.g. "Browse all case studies" or
"Get an Estimate" — as a conversion on-ramp.

Layout note: with AI broken out, the panel doesn't fit a clean six-column grid. Exact arrangement (e.g. six stages + a visually distinct AI band, or a 3×2 stage block beside an AI panel) is a UI design problem — the IA's job is to fix the *relationship*: six sequential stages, one cross-cutting competency.

Panel headline: **"From idea to live product — every stage covered."**

> **The stage lists below are NAV LABELS, not page names.** They are the short forms as they appear in
the menu, and they match the built nav exactly. Each sub-service's formal page name — the H1 and the URL
slug, which the SEO foundation holds fixed — lives in its category's **Sub-service pages** line under
§"Site structure — Services". The two registers differ on purpose ("Technical Support" in the menu,
"Technical Support & Maintenance" as the page), so neither list is a duplicate of the other and neither
may be deleted in favour of the other. What must always agree is the *membership and count* of the two
lists; `tools/check-ia-sync.py` asserts that, plus the nav labels against the built nav.

**Discover & Validate:** Market Analysis · Digital Transformation Strategy · Startup Ideation & Feasibility · Product Conceptualization · Financial Modelling · Technical Specification · Cost & Time Estimation

**Design:** UI Design · UX Design · Prototyping & Wireframing · User Testing · Customer Journey Mapping · Product Redesign

**Build:** Web Development · Mobile App Development · E-commerce Development · CRM Development · ERP Development · Bot Development · Game Development · SPA Development · PWA Development · 3rd Party Integrations · Platform Migration

**Grow:** Marketing Strategy · Full Digital Marketing · SEO · GEO · ASO · Lead Generation · PPC · SMM · Digital Branding · Copywriting · Graphic Design

**Scale:** Team Outsourcing · Staff Augmentation

**Maintain:** Technical Support · Audit & Troubleshooting · Security & Performance · Hosting & Infrastructure

> **Why AI Transformation stands apart.** AI is not listed inside the Build column. It has its own visually distinct
block within the panel, signalling it as a competency that permeates every stage rather than a sub-service of Build.
The block links directly to `/services/ai-transformation` and surfaces the AI sub-services. The six stage columns
carry only their native categories — Build holds all of Software Development's sub-services. How the AI block is
arranged relative to the six stages is a design-phase decision; the IA fixes only that AI is separate and
cross-cutting.

### Who We Serve megamenu — two-axis panel

A single panel with two distinct columns — answering both "are you in my industry?" and "are you at my stage?" in one look. Heading behavior: "By industry" links `/industries`; "By company stage" is a non-interactive label — `/who-we-serve` is a legitimate hub, but it is exactly where the "Who We Serve" trigger itself goes, so a heading link would only restate it. The two axes therefore do not read symmetrically; making that deliberate is a design task.

**By company stage:** Early-stage Startup — pre-revenue, building MVP · Scale-up — product-market fit, growing fast · Small Business — established, modernising · Midsize Business — multi-team, accelerating · Enterprise — complex stack, regulated

**By industry:** Tech · Finance · Healthcare · Travel · Hospitality · Retail · Education · Manufacturing · Media & Entertainment · Sport · Professional Services · Non-Profit · Beauty & Wellness

### Our Work — direct link (no megamenu)

Our Work is a single top-level link straight to the portfolio hub (`/our-work`) — no dropdown, no megamenu. The portfolio hub already does the work a megamenu panel would attempt: filter chips, the featured section, and the full project grid live on the page itself. A dropdown would only duplicate that one click early, at the cost of nav weight and an extra hover surface.

> **Why no dropdown.** The discovery affordances a portfolio panel would offer (featured cases + browse-by-filter chips) belong on the portfolio hub, where they have room to breathe and stay in sync with the filter system.

### How We Work megamenu — three-column panel

A lightweight megamenu. The three columns answer a non-technical founder's two big questions and house the reference
material: *what's it like to work with you?* (Process), *what does it cost / what model fits me?* (Engagement Models),
and *what do you actually work with?* (the Technologies / Methodologies / Tools reference hubs). Why VECTO is parked
in the Appendix, off this menu. Heading behavior: "Our Process" and "Engagement Models" head real pages and are links;
"Reference" is a non-interactive label — no reference hub page exists and none is warranted (UX- or SEO-wise); its
three items are the links.

**Our Process:** 1 · Kickoff → 2 · Scoping → 3 · Execute → 4 · Launch → 5 · Iterate

**Engagement Models:** Fixed Price — defined scope, fixed cost · Time & Material — flexible scope, hourly · Dedicated Team — your team, our payroll · Outstaffing — engineers into your team

**Reference:** Technologies — full stack index → · Methodologies — how we run delivery → · Tools — what we work in day-to-day →

### Resources menu — simple dropdown

Lightweight dropdown grouping the content marketing assets. Not a megamenu — these aren't conversion-critical entry
points for a non-technical founder, and a smaller footprint is honest about that. Two columns. (A Tools column entry
returns with the AI estimator — Appendix; a standing Tools entry would be redundant with the Get an Estimate CTA in
the same bar.) Both column headings are non-interactive labels, for the same reason: a "Blog" heading link would
duplicate "Latest posts" and "By topic", and a "Glossary" heading link would duplicate "Browse A–Z". "Tech terms,
explained for founders" is the Glossary tagline, not a link.

**Blog** *(label)*: Latest posts · By topic · Authors

**Glossary** *(label + tagline)*: Browse A–Z →

### About menu — simple dropdown

The About headline itself is clickable and links to the `/about` hub; the panel deep-links the sub-pages — Company,
Team, Careers, Testimonials — plus Schedule a Call and Contact. The expected journey is that most visitors skip the
hub and go straight to a sub-page. Security & Compliance is on hold — off all visible surfaces, parked in the
Appendix. Heading behavior: "The company" and "The team" head real pages and are links; "Get in touch" is a
non-interactive label. Schedule a Call and Contact are standalone pages (root-level URLs) — their presence here is
menu placement, not hierarchy.

**The company:** Company — history, mission & vision, partners

**The team:** Team — leadership & specialists · Careers — open roles

**Get in touch** *(label)*: Testimonials · Schedule a Call · Contact

### Get an Estimate — primary CTA

Visually distinct button (highlighted background, contrasting colour), always present in the navigation bar, links directly to the Get an Estimate page. The single highest-impact navigation element for the primary persona.

> **Visual treatment.** Button-shaped, filled background (brand accent), high contrast against the dark nav bar. Stays anchored at the right edge of the nav. Mobile: persists in the header even when the hamburger menu is closed.

### Footer navigation

The footer carries the deeper, less buyer-facing portion of the IA — long-tail SEO assets that don't earn megamenu space but still need crawlable links from every page.

| # | Column | Contents |
|---|---|---|
| 1 | Services & Solutions | Top-level service categories (AI Transformation + the stage categories) + "All services →" · Solutions (own products) + the individual solution pages |
| 2 | Industries & Stage | Every industry + every company stage — full lists, no truncation |
| 3 | Service Areas | Country pages — footer-only. Pure SEO surface. |
| 4 | Resources | Blog · Glossary · Get an Estimate · Engagement Models · Process · Technologies · Methodologies · Tools · Year pages (year-in-review / annual content) |
| 5 | Company | About · Company · Team · Careers · Testimonials · Partners · Press · Contact |
| — | Utility row | Logo · Privacy · Terms · Cookies · Sitemap · Social links · Copyright |

> **Footer carries the SEO long-tail surface.** Country and Year pages are footer-only — retaining their ranking
surface without occupying buyer-facing primary nav. The same logic applies to the Technologies, Methodologies, and
Tools reference hubs: living under How We Work rather than top-level nav, they still need crawlable links from every
page, so they surface in the Resources footer column. The non-technical founder isn't hunting for them in the header;
search crawlers and technical evaluators still reach them.

---

## Site structure — Homepage

### Homepage · `/` · **full**

**Description.** The primary entry point for every persona, and the first impression for the non-technical founder. Designed to answer four questions in the first 10 seconds: *Is this for someone like me? · Can they build what I'm trying to build? · Will I be in good hands? · How much will it cost and how long will it take?*

**Design rationale.** Section ordering mirrors the primary navigation's narrative order — Services → Who We Serve →
  Our Work → How We Work → Resources → About/Contact — so the homepage reads as a scrollable version of the menu's
  story. The arc: *identify (hero + trust) → what we do (services + AI) → who it's for (industries + stage) → proof
  (portfolio + reviews) → how we work (process + engagement) → learn more (blog) → convert (FAQ + contact)*. Trust
  signals stay above the fold. Industries and the Who-We-Serve strip sit adjacent so the two halves of "who we serve"
  stay together. Process sits after proof, per the menu narrative — its role is "here's how it works, now that you're
  interested," not "reassure immediately." Engagement models are de-emphasized into a narrow strip beside Process,
  since the model decision isn't a first-visit concern. The Estimate entry sits near the end as a conversion on-ramp;
  the sticky nav CTA covers the mid-scroll catch.

| # | Block | Description |
|---|---|---|
| 1 | Hero | Outcome-led headline naming the target client; sub-headline with a quantified proof point; dual CTA — primary "Get an Estimate", secondary "See our work". |
| 2 | Trust strip | Consolidated above-the-fold signal: client logos (only big names) + numerical proof (years, projects, retention rate, NPS) + review platform badges (Clutch, GoodFirms, G2). |
| 3 | Small intro | 2-3 sentences framing what VECTO does, written for the non-technical founder ("we turn your idea into a product your users love"). |
| 4 | Services overview | The six-stage transformation grid (Discover · Design · Build · Grow · Scale · Maintain). AI is not shown inside Build — consistent with the Services megamenu, it surfaces as the distinct cross-cutting AI band immediately below. Maps to the Services menu. |
| 5 | AI positioning band | Single editorial band (not card/column-based) creating visual contrast against the surrounding grid-heavy sections, giving AI its own cross-cutting moment. *(detail below.)* |
| 6 | Benefits section | 3-5 outcome-led benefits ("Ship faster" / "Avoid the wrong build" / "Scale without hiring" / etc.) with founder-recognisable language. Closes the "what we do" portion before the page turns to "who it's for." |
| 7 | Industries grid | Editorial layout — 2 featured industry cards (highest-demand verticals, e.g. Healthcare + Finance) plus a compact index of the remaining industries — not a uniform card grid, consistent with the homepage's Tier-1 editorial treatment. All industries are represented; each tile/row links to its Industry page. Maps to the Who We Serve menu (industry axis). |
| 8 | Who we serve strip | Filter-chip row: "Built for [Early-stage / Scale-up / SMB / Mid-market / Enterprise]" — chip labels are display shorthand; the canonical stage nouns and slugs stay Small Business / Midsize Business (see Who We Serve). *(detail below.)* |
| 9 | Portfolio module | Curated featured grid (6-8 highlighted projects) — hand-picked via the CMS featured flag + order, editorial Tier-1 layout echoing the portfolio's asymmetric aspect-preset grid, closing with "Browse all work →". Layout validated in the wireframe. Maps to the Our Work menu. |
| 10 | Reviews | Featured testimonials rendered from the on-site CMS (author, company, text, link to source — Clutch/GoodFirms/Google), not embedded platform widgets; link to `/about/testimonials`. Clustered with Portfolio as the combined proof block. |
| 10a | Solutions strip | Compact strip: "Products we build and run" — the solutions mini-portfolio (onemall · onesocial · quickoffer · plugins) linking to `/solutions`. Deliberately lighter than the portfolio module above; sits with the proof cluster (own products are proof too). Maps to the Solutions nav item. |
| 11 | Process strip | 5-step horizontal visual (*Kickoff → Scoping → Execute → Launch → Iterate*) linking to the Process page. Describes how every engagement runs as a project — distinct from the Services stages above. Maps to the How We Work menu. Positioned to follow the menu narrative: it explains the working relationship once the visitor is interested, rather than pre-emptively. |
| 12 | Engagement strip | Deliberately narrow / de-emphasized — sits immediately after Process to reflect their real-world connection (how an engagement runs ↔ how it's structured commercially). *(detail below.)* |
| 13 | Estimate CTA block | "Tell us about your project — get a ballpark from the team." CTA to `/get-an-estimate`. Positioned late as a conversion on-ramp before the closing blocks; the sticky nav CTA carries it earlier in the scroll. (An embedded mini-estimator rides with the deferred AI estimator — Appendix.) |
| 14 | Blog teaser | 3 latest posts with thumbnail, title, author, date. Maps to the Resources menu. |
| 15 | FAQ | 5-7 founder-facing questions: "How long will it take?" / "What does it cost?" / "Who owns the IP?" / "Where are your engineers based?" / "What if we want to bring it in-house later?" |
| 16 | Contact / CTA section | Dual CTA — Get an Estimate · Send a question (Contact form). Scheduling is offered inside the estimate flow's success state rather than as a third competing door (and stays directly bookable via the About menu). |
| 17 | Footer | See Footer navigation above. |

Row detail (moved out of the table for line length; same authority as the rows above):

- **Row 5 · AI positioning band:** Headline: "AI expertise, earned in practice." Body: "The AI landscape is loud and
  hard to read — genuine capability sits alongside hype, and telling them apart takes time most founders don't have.
  We've done that work. We use AI across every project we run to ship faster and cut costs, and we can help you
  integrate it into your product or business the right way." Two CTAs: *How we implement AI →*
  (`/services/ai-transformation`) · *See it in practice →* (`/our-work/service/ai-transformation` — the AI facet
  landing).
- **Row 8 · Who we serve strip:** Each chip links to the corresponding stage page or a pre-filtered case study view.
  Sits directly with the Industries grid so the two halves of "who we serve" (industry × company stage) are
  semantically connected; the Who We Serve hub is the canonical destination.
- **Row 12 · Engagement strip:** One line: "Flexible ways to work together — Fixed Price · T&M · Dedicated Team ·
  Outstaffing," linking to the full Engagement Models page. The only takeaway needed here is "options exist, we're
  flexible." Visual treatment to be resolved in design.

## Site structure — Services

### Services hub · `/services` · **full**

**Description.** Presents the full breadth of VECTO's offering as a transformation journey rather than a flat catalogue. For a non-technical founder, this is the page where they orient themselves: "what stage am I at, and which of these services do I actually need right now?"

**Design rationale.** Same six-stage grouping as the megamenu (Discover → Design → Build → Grow → Scale → Maintain),
  giving structural consistency across the buyer's primary navigation surface and the page they land on. Every service
  category has a visible card showing a representative selection of its sub-services; the full sub-service taxonomy
  lives on the individual service pages and in the footer (the hub card is a curated entry point, not an exhaustive
  index). Consistent with the megamenu, AI Transformation is not folded into the Build card — it gets its own distinct
  section on the page, reflecting its positioning as a cross-cutting competency.

| # | Block | Description |
|---|---|---|
| 1 | Hero | "From idea to live product — every stage covered." Sub-headline names the transformation arc; dual CTA — primary "Get an Estimate", secondary "See our work" (matching the homepage hero pattern). |
| 2 | Stage navigation strip | Sticky horizontal nav linking to anchors for each of the 6 stages on the page. Lets a buyer jump directly to the stage that applies to them. |
| 3 | Discover & Validate card | IT Consulting category. Headline outcome ("Validate before you build"), 2-sentence description, list of sub-services, "Learn more" → `/services/it-consulting`. |
| 4 | Design card | Product Design category. Same anatomy. |
| 5 | Build card | Software Development category only. Visually largest of the six stage cards given the primary-stage principle. AI is not part of this card — it has its own section (5a). |
| 5a | AI Transformation section | Distinct section sitting apart from the six stage cards (visual treatment to be resolved in design — e.g. a full-width band or a highlighted panel), mirroring how the Services megamenu breaks AI out. *(detail below.)* |
| 6 | Grow card | Marketing category. Same anatomy. |
| 7 | Scale card | Outsourcing & Outstaffing category. Same anatomy. |
| 8 | Maintain card | Support & Maintenance category. Same anatomy. |
| 9 | Engagement models snapshot | 4-card module mirroring the homepage version, link to full Engagement Models page. |
| 10 | Featured case studies | 3-4 cases spanning multiple stages, demonstrating end-to-end capability. |
| 11 | FAQ | Service-spanning questions: "Can I start with one stage and add others?" / "Do you handle the transition between stages?" / "What if my project doesn't fit any single stage?" |
| 12 | Estimator + Schedule CTA strip | Dual CTA closing the page. |

Row detail (moved out of the table for line length; same authority as the rows above):

- **Row 5a · AI Transformation section:** Headline frames AI as the cross-cutting competency; short body echoes the
  homepage positioning; surfaces the AI sub-services; primary CTA "Explore AI Transformation →" →
  `/services/ai-transformation`.

### Sub-service page template · `/services/[category]/[sub-service]` · **template**

Applied to every sub-service page across the service categories (the stage lists in the megamenu section are the roster). Same anatomy as the top-level service page but more granular and with concrete artefacts where possible. Each sub-service page must include a breadcrumb back to its parent service.

| # | Block | Description |
|---|---|---|
| 1 | Breadcrumb | Home › Services › [Parent service] › [This sub-service] |
| 2 | Hero | Outcome promise specific to this sub-service. Plain English, founder-recognisable. |
| 3 | What you get | Concrete deliverables: artefacts, documentation, code, hand-off materials. |
| 4 | Sample work | Where allowed by NDA: before/after screenshots, anonymised artefacts, demo videos. |
| 5 | Mini-process | 4-5 step flow scoped to this sub-service. |
| 6 | Tech stack | Specific technologies typical for this sub-service. |
| 7 | Typical timeline & team | Range of duration, typical FTE count, roles involved. |
| 8 | Case studies | 2-3 cases tagged to this specific sub-service. |
| 9 | Engagement models | Subset that fits this sub-service. |
| 10 | FAQ | 3-5 sub-service-specific questions. |
| 11 | Talk to a specialist | The lead practitioner for this sub-service area. |
| 12 | Related sub-services | 3-4 sub-services often combined or sequenced with this one. |
| 13 | Sticky Estimator CTA | Persistent throughout scroll. |

### AI Transformation · `/services/ai-transformation` · **full**

**Description.** Top-level service page covering the AI capability area. Picks up from the homepage AI positioning
  band and develops the full argument. For the non-technical founder, this page answers two questions: "can you help
  me figure out what AI actually makes sense for my product?" and "can you build it without it becoming a research
  project?" Frames AI as a practitioner competency, not a trend the agency is chasing.

**Design rationale.** Hero continues the level-headed, experience-led tone established on the homepage band — no hype,
  no doom, just earned confidence. The two value props (helping clients implement AI correctly, using AI internally to
  deliver better) are separated into distinct benefit cards so neither dilutes the other. The sub-services list
  explicitly distinguishes integration work from custom model development — a non-technical founder cannot tell these
  apart without help. Case studies carry the credibility weight; the page points to them early and often.

| # | Block | Description |
|---|---|---|
| 1 | Hero | Headline: "Build AI into your product — with a clear idea of what you're actually getting." Sub-headline: "The promise around AI is still louder than the reality. *(detail below.)* |
| 2 | What's included | Sub-service cards — each links to the corresponding sub-service page. Cards explicitly distinguish integration work (AI Integration, AI Prompt Engineering) from build work (Generative AI Development, ML Engineering) and data work (Data Analytics). |
| 3 | Benefits | 3 founder-facing benefits mapping to the two positioning value props. (1) "Know what you're integrating before you commit" — we match the right tools and models to the specific problem, not the ones currently trending. *(detail below.)* |
| 4 | Mini-process | Service-scoped 4-step process (Audit → Pilot → Integrate → Operate), link to full Process page. |
| 5 | Tech stack | Relevant slice of the Technologies taxonomy: AI/ML stack, integration tools, data infrastructure. |
| 6 | Case studies | 2-3 cases tagged AI Transformation, pulled from the case study system. Placeholders until projects are documented. Each case study should foreground the client's starting point and the specific AI problem framing — not just the technical output. |
| 7 | Engagement models available | Subset of models that fit AI work (typically T&M and Dedicated Team). |
| 8 | FAQ | 5 questions addressing the sceptical founder: "Do we need a large dataset to get started?" (not necessarily — off-the-shelf models often suffice before custom training becomes relevant) — remaining questions in the row detail below. |
| 9 | Talk to a specialist | Named photo + role of the AI practice lead, with "Email me" / "Book 15 min" CTAs. |
| 10 | Related services | Software Development (AI lives inside products), Data Analytics (often paired), IT Consulting (validate AI use case first). |
| 11 | Sticky Estimator CTA | Persistent floating CTA throughout scroll. |

Row detail (moved out of the table for line length; same authority as the rows above):

- **Row 1 · Hero:** We've worked through that gap: integrating models, building pipelines, and learning where AI earns
  its place in a product and where it doesn't. That's the experience we bring to every AI engagement." Dual CTA: *Get
  an estimate →* · *See our AI work →* (`/our-work/service/ai-transformation` — the AI facet landing). Tone
  deliberately less punchy than the homepage band — reassurance over hook.
- **Row 3 · Benefits:** (2) "Ship AI features that hold up in production" — a working demo and a production-ready
  feature are different things; we've built both and know what it takes. (3) "Faster delivery, lower cost — by design"
  — we use AI across our own development process (testing, code review, iteration); that efficiency feeds directly
  into client timelines and budgets. Benefit 3 sits last deliberately — AI-as-internal-tool should not read as the
  primary pitch.

- **Row 8 · FAQ (remaining questions):** "How do you avoid vendor lock-in?" (architecture is not built on any single
  provider's stack by default) · "How do you measure whether an AI feature is actually working?" (success metrics
  defined before build, not after — accuracy, latency, cost per inference) · "What if the AI landscape shifts after
  we've built something?" (components are modular so models can be swapped without rebuilding everything around them)
  · "We've heard AI can hallucinate or behave unpredictably — how do you handle that?" (failure modes are designed
  for: human review layers, fallback logic, confidence thresholds).
**Sub-service pages** *(formal page names — H1 + URL slug; menu labels are shorter, see §"Services megamenu")*: AI Integration · Generative AI Development · ML Engineering · Data Analytics · AI Prompt Engineering

### Software Development · `/services/software-development` · **full**

**Description.** The flagship service category for the non-technical founder persona. This is where most first-time visitors will end up — the page that needs to do the heaviest conversion work on the site.

**Design rationale.** Hero leads with the founder's mental model: "turn your idea into a product." Sub-service breadth is presented as capability not menu — the page reassures the visitor that whatever shape their idea takes (web, mobile, e-commerce, internal tool), VECTO can build it. Process visibility is elevated relative to other service pages; this is where founder anxiety peaks.

| # | Block | Description |
|---|---|---|
| 1 | Hero | "Turn your idea into a product your users love." Dual CTA: Estimator + Schedule a Call. |
| 2 | What's included | One card per sub-service, in 3 visual groupings: Customer-facing apps · Business systems · Specialised builds. |
| 3 | Benefits | Ship faster, build it right the first time, future-proof architecture, retain IP. |
| 4 | Mini-process | Same 5-step process as the global Process page, scoped to a build engagement. More detail than other service pages given founder anxiety. |
| 5 | Tech stack | Frontend + Backend + Infrastructure — the full technology roster (see the Technologies hub). Presented as "we use what's right for your project, not what we sell." |
| 6 | Case studies | 5-7 cases tagged Software Development — featuring at least 2 first-time founder clients. |
| 7 | Engagement models available | All four models. Each annotated with "best when..." for this service. |
| 8 | FAQ | "Who owns the code?" / "What if we want to bring it in-house later?" / "How do you handle scope creep?" / "Can you work with my existing tech stack?" / "What happens if we need to change direction mid-build?" |
| 9 | Talk to a specialist | Engineering lead with photo, name, "Email me" / "Book 15 min." |
| 10 | Related services | Product Design (precedes build), AI Transformation (often integrated), Support & Maintenance (after build). |
| 11 | Sticky Estimator CTA | Persistent throughout scroll. |

**Sub-service pages** *(formal page names — H1 + URL slug; menu labels are shorter, see §"Services megamenu")*: Web Development · Mobile App Development · Bot Development · Game Development · E-commerce Development · CRM Development · ERP Development · PWA Development · SPA Development · 3rd Party Integrations · Platform Migration Services

### Product Design · `/services/product-design` · **full**

**Description.** Top-level service page for the Design stage. Frames design not as decoration but as risk reduction — for a founder, the cheapest mistake to fix is the one made before development starts.

**Design rationale.** Hero positions design as the step that prevents wasted dev budget, not as polish. Sub-services are sequenced from research-led (UX, Customer Journey) through validation (Prototyping, User Testing) to execution (UI, Redesign) — matching the order a founder would naturally engage them.

| # | Block | Description |
|---|---|---|
| 1 | Hero | "Design that earns users, not just admiration." Sub-headline names the validation-before-build benefit. |
| 2 | What's included | One card per sub-service, in research → validation → execution sequence. |
| 3 | Benefits | Avoid the wrong build, validate before you spend, ship faster after design, design that scales. |
| 4 | Mini-process | Design-specific process: Discover → Frame → Design → Test → Hand-off. |
| 5 | Tech stack | Tooling: Figma, prototyping, research platforms. Lighter section here. |
| 6 | Case studies | 3-5 cases tagged Product Design with before/after framing where possible. |
| 7 | Engagement models available | Fixed Price (sprint), T&M (ongoing), Dedicated Designer (embedded). |
| 8 | FAQ | "Can you work without a brief?" / "What if we already have designs?" / "How do you handle our brand guidelines?" / "Do you do user research with our actual customers?" |
| 9 | Talk to a specialist | Design lead with photo and direct CTA. |
| 10 | Related services | IT Consulting (validate the idea first), Software Development (then build), Marketing (then grow). |
| 11 | Sticky Estimator CTA | Persistent throughout scroll. |

**Sub-service pages** *(formal page names — H1 + URL slug; menu labels are shorter, see §"Services megamenu")*: UI Design · UX Design · Product Redesign · User Testing · Prototyping & Wireframing · Customer Journey Development

### Marketing · `/services/marketing` · **full**

**Description.** Top-level service page for the Grow stage. Treated identically to all other service categories: full anatomy, all sub-services, equal positioning.

**Design rationale.** Hero frames Marketing not as a separate offering but as the natural continuation of building — "you've built it, now let's make sure people find it." Sub-services are grouped into three pillars: Strategy & Branding · Acquisition & Lead Gen · Content & Creative — clearer than a flat list.

| # | Block | Description |
|---|---|---|
| 1 | Hero | "Built it? Now let's make sure people find it." Sub-headline names the marketing-meets-development advantage. |
| 2 | What's included | One card per sub-service, in 3 pillars: Strategy & Branding · Acquisition & Lead Gen · Content & Creative. |
| 3 | Benefits | Marketing that knows your tech, attribution from day one, content that converts, no agency-handoff gaps. |
| 4 | Mini-process | Marketing-specific: Audit → Strategy → Execute → Measure → Iterate. |
| 5 | Tech stack | Marketing platforms, analytics, CRM integrations. |
| 6 | Case studies | 3-5 cases showing marketing outcomes, ideally for products VECTO also built. |
| 7 | Engagement models available | Retainer (most common), T&M, project-based. |
| 8 | FAQ | "Do you only do marketing for products you built?" / "How do you measure success?" / "Can you take over from another agency?" |
| 9 | Talk to a specialist | Marketing lead with photo and direct CTA. |
| 10 | Related services | Software Development (build), IT Consulting (market analysis), Product Design (conversion-led design). |
| 11 | Sticky Estimator CTA | Persistent throughout scroll. |

**Sub-service pages** *(formal page names — H1 + URL slug; menu labels are shorter, see §"Services megamenu")*: Marketing Strategy Development · Full Digital Marketing · SEO · GEO · ASO · Lead Generation · SMM · Graphic Design · PPC · Copywriting · Digital Branding

### IT Consulting · `/services/it-consulting` · **full**

**Description.** Top-level service page for the Discover & Validate stage. Critical for the non-technical founder — this is the page where they realise they don't have to commit to a build before knowing if the idea makes sense.

**Design rationale.** Hero explicitly addresses the founder's biggest fear: starting a build that turns out to be wrong. Sub-services are sequenced from idea-validation through to technical specification — matching the order in which a founder would commission them. Cross-link prominence to Engagement Models (Discovery is typically Fixed Price).

| # | Block | Description |
|---|---|---|
| 1 | Hero | "Validate before you build." Sub-headline names the cost of skipping this step. |
| 2 | What's included | One card per sub-service, in idea → spec sequence. |
| 3 | Benefits | Avoid wasted build budget, get investor-ready, build what users actually need, hard numbers before commitment. |
| 4 | Mini-process | Discovery-specific: Brief → Research → Frame → Validate → Specify. |
| 5 | Tech stack | Lighter section. Research and modelling tools. |
| 6 | Case studies | 2-3 cases where the consulting work shaped the eventual build (or correctly recommended not to build). |
| 7 | Engagement models available | Typically Fixed Price for the discovery phase. |
| 8 | FAQ | "What if your analysis says don't build?" / "Can you do this without us committing to a build with you?" / "How long does discovery take?" |
| 9 | Talk to a specialist | Discovery lead with photo and direct CTA. |
| 10 | Related services | Product Design (after validation), Software Development (after specification). |
| 11 | Sticky Estimator CTA | Persistent throughout scroll. |

**Sub-service pages** *(formal page names — H1 + URL slug; menu labels are shorter, see §"Services megamenu")*: Market Analysis · Digital Transformation Strategy · Startup Ideation & Feasibility Analysis · Product Conceptualization · Financial Model Development · Technical Specification Development · Product Development Cost & Time Estimation

### Support & Maintenance · `/services/support-maintenance` · **full**

**Description.** Top-level service page for the Maintain stage. Often overlooked by founders pre-launch but increasingly critical post-launch. Page also serves visitors who inherited a product (acquired, departed founder, etc.) and need a maintenance partner.

**Design rationale.** Hero acknowledges the two distinct buyers: post-launch founders and inheritors of an existing system. Sub-services lead with what most clients need first (audit) before promising ongoing relationship (technical support).

| # | Block | Description |
|---|---|---|
| 1 | Hero | "Keep what we built running, evolving, and secure." Two-buyer sub-headline (post-launch founders + inheritors of legacy systems). |
| 2 | What's included | One card per sub-service. |
| 3 | Benefits | Sleep through the night, predictable cost, no engineer hire required, security as standard. |
| 4 | Mini-process | Maintenance-specific: Audit → SLA agreement → Onboard → Operate → Improve. |
| 5 | Tech stack | Monitoring, observability, hosting platforms. |
| 6 | Case studies | 2-3 cases including at least one inherited / migrated system. |
| 7 | Engagement models available | Retainer (most common), T&M for ad-hoc work. |
| 8 | FAQ | "Will you maintain a system you didn't build?" / "What's the SLA?" / "What if our codebase is a mess?" / "Can you migrate us off legacy infrastructure?" |
| 9 | Talk to a specialist | Operations lead with photo and direct CTA. |
| 10 | Related services | Software Development (the original build), Outsourcing & Outstaffing (extend the team). |
| 11 | Sticky Estimator CTA | Persistent throughout scroll. |

**Sub-service pages** *(formal page names — H1 + URL slug; menu labels are shorter, see §"Services megamenu")*: Technical Support & Maintenance · Audit and Troubleshooting · Security, Performance Enhancements and Updates · Hosting and Infrastructure Support

### Outsourcing & Outstaffing · `/services/outsourcing-outstaffing` · **full**

**Description.** Top-level service page for the Scale stage. Primarily serves the secondary persona (Scale-up Product Lead) but also relevant to non-technical founders post-MVP who realise they need a team rather than a project.

**Design rationale.** Hero distinguishes between the two sub-services upfront — most buyers don't know the difference.
  Cross-links to Engagement Models prominently because the model decision is the buying decision here. **Terminology
  mapping (stated once, here):** the two Scale sub-services correspond to two engagement models — *Team Outsourcing ↔
  Dedicated Team* (we run the team) and *Staff Augmentation ↔ Outstaffing* (you run it, we provide the engineers).
  Service taxonomy and commercial model are different axes that happen to pair 1:1 on this page.

| # | Block | Description |
|---|---|---|
| 1 | Hero | "Plug expert engineers into your team — fast." Sub-headline distinguishes Outsourcing (we run the team) from Outstaffing (you run, we provide). |
| 2 | What's included | The two sub-service cards with a clear comparison table. |
| 3 | Benefits | Speed-to-team, flexible capacity, no recruitment overhead, EU/CIS time-zone alignment. |
| 4 | Mini-process | Scale-specific: Brief → Match → Onboard → Run → Adjust. |
| 5 | Tech stack | The same technology roster as Software Development — emphasises depth of available talent. |
| 6 | Case studies | 2-3 cases featuring team-extension stories with retention numbers. |
| 7 | Engagement models available | Dedicated Team and Staff Augmentation only — directly maps to the two sub-services. |
| 8 | FAQ | "How fast can you spin up a team?" / "Who manages day-to-day?" / "How do you handle people leaving?" / "What about IP and contracts?" |
| 9 | Talk to a specialist | Talent / delivery lead with photo and direct CTA. |
| 10 | Related services | Software Development (the work the team does), Support & Maintenance (when the team's role is ongoing). |
| 11 | Sticky Estimator CTA | Persistent throughout scroll. |

**Sub-service pages** *(formal page names — H1 + URL slug; menu labels are shorter, see §"Services megamenu")*: Team Outsourcing · Staff Augmentation

## Site structure — Solutions

### Solutions hub · `/solutions` · **full · new**

**Description.** The mini-portfolio of VECTO's own small B2B/SaaS products — at launch: onemall, onesocial, quickoffer, plugins. Categorically distinct from Services (custom work) and Our Work (client proof): this is what VECTO builds and runs for itself and sells ready-made. Eighth top-level nav item, direct link, beside Services.

**Design rationale.** Intro text does the concept-framing work ("we don't just build for clients — we ship our own products"), then a clean listing carries the visitor to the individual solution pages, which do the selling. Deliberately separate from the client-work portfolio — solutions never appear in the `/our-work` grid or its facets; the two surfaces cross-link instead.

| # | Block | Description |
|---|---|---|
| 1 | Hero + intro | Concept framing: own products, built and run by VECTO. |
| 2 | Solutions listing | Card per solution: name, one-line value proposition, category/status, visual. CMS-driven list — adding a solution in the CMS adds a card and a page. |
| 3 | "Why we build products" | Short editorial band — the practitioner-credibility angle (products sharpen the same team that builds for clients). |
| 4 | Closing CTA | Estimate + Contact dual CTA. |

### Solution page template · `/solutions/[solution-slug]` · **template · new**

Dedicated page per solution, structurally similar to the case study template but selling a product rather than telling an engagement story.

| # | Block | Description |
|---|---|---|
| 1 | Breadcrumb | Home › Solutions › [Solution] |
| 2 | Hero | Name, tagline, product visual. External product CTA — "Launch website / Try now / Download app" (optional CMS field pair `cta_label` + `cta_url`; hidden when absent). |
| 3 | What it is / who it's for | Plain-language value proposition and target user. |
| 4 | Features & screens | Feature highlights with product screenshots. |
| 5 | Tech stack | Technology badges linking to technology pages. |
| 6 | Pricing / plans | Optional, per product. |
| 7 | Related case studies & services | Cross-links into the client-work and services surfaces. |
| 8 | Closing CTA | External product CTA repeated + Contact. |

> **Content model.** Solution entity: name, slug, tagline, value-prop copy, features, screenshots, tech tags (relation), pricing (optional), external CTA label + URL (optional, hidden when absent), status. Blog "related projects" relation covers case studies only — a "related solutions" relation is deliberately not front-loaded; add later if editorial use appears.

## Site structure — Who We Serve

### Who We Serve hub · `/who-we-serve` · **full**

**Description.** The hub page that backs the Who We Serve megamenu. For a non-technical founder, this is where they confirm "yes, agencies like VECTO have built things for companies like mine." Two-axis structure mirrors the megamenu: company stage × industry.

**Design rationale.** The hub is the canonical "who we serve" destination; the homepage carries a filter-chip strip linking here. Each company stage and each industry has its own dedicated page accessed from this hub.

| # | Block | Description |
|---|---|---|
| 1 | Hero | "Who we work with — and why we work that way." |
| 2 | By company stage | One card per stage, in a row: Early-stage Startup · Scale-up · Small Business · Midsize · Enterprise. Each links to its dedicated page. |
| 3 | By industry | Grid with icons, one cell per industry. Each cell links to the corresponding Industry page. |
| 4 | Featured cross-cutting case studies | 4-6 cases that span the matrix — e.g. an early-stage Healthcare client, an enterprise Fintech client. |
| 5 | Process strip | Cross-segment reassurance — same process applies regardless of stage or industry. |
| 6 | FAQ | "Do you only work with [stage]?" / "What if my industry isn't listed?" / "How do you adapt your process by stage?" |
| 7 | Estimator + Schedule CTA | Dual CTA closing the page. |

**Stage pages** *(one per stage · each follows the company stage template)*: Early-stage Startup `/who-we-serve/early-stage-startup` · Scale-up Startup `/who-we-serve/scale-up` · Small Business `/who-we-serve/small-business` · Midsize Business `/who-we-serve/midsize-business` · Enterprise `/who-we-serve/enterprise`

### Company stage page template · `/who-we-serve/[stage]` · **template**

Applied to every company stage page. Each page must speak to the specific anxieties, budgets, and decision-making processes of that stage.

| # | Block | Description |
|---|---|---|
| 1 | Hero | Stage-specific framing. Early-stage: "From napkin to product launch." Enterprise: "Modernise without disrupting what already works." |
| 2 | Pain points common to this stage | 3-5 specific anxieties: cash burn, hiring pace, technical debt, procurement, etc. |
| 3 | Services prioritised for this stage | Different stages need different services first. |
| 4 | Engagement models that work | Different stages can support different commercial models. Early-stage usually needs Fixed Price predictability; enterprise can run Dedicated Team. |
| 5 | Budget framing | Honest discussion of typical spend for this stage. Reduces wasted leads from mis-matched budgets. |
| 6 | Featured case studies at this stage | 3-5 cases of clients at the same stage at engagement start. |
| 7 | Process adaptations for this stage | How the standard 5-step process adapts (e.g. compressed Kickoff for early-stage; extended Scoping for enterprise). |
| 8 | Stage-specific FAQ | Questions unique to this stage's decision-making. |
| 9 | Talk to a specialist | Account lead with experience at this stage. |
| 10 | Estimator + Schedule CTA | Dual CTA closing the page. |

## Site structure — Industries

### Industries hub · `/industries` · **full**

**Description.** Index page for the industry pages. Functions as a directory rather than a marketing page — visitors who land here usually arrived via search and want to find their specific industry quickly.

**Design rationale.** Lighter treatment than other hubs. The work is done by individual Industry pages; this hub just helps visitors get to them. Search box prominent for the visitor whose industry isn't immediately visible in the grid.

| # | Block | Description |
|---|---|---|
| 1 | Hero | "Industry-specific expertise across [N] verticals" — [N] computed at build time. Search field for industry — client-side keyword filter over the rendered grid; no search backend. |
| 2 | Industry grid | One card per industry: icon, industry name, one-line summary of relevant capability. |
| 3 | Cross-industry case studies | 3-4 featured cases. |
| 4 | FAQ | "What if my industry isn't here?" / "Do you have compliance experience for [regulated vertical]?" |
| 5 | Estimator CTA | Closing CTA. |

**Industry pages** *(one per industry · each follows the industry template)*: Tech `/industries/tech` · Travel
  `/industries/travel` · Hospitality `/industries/hospitality` · Finance `/industries/finance` · Healthcare
  `/industries/healthcare` · Manufacturing `/industries/manufacturing` · Retail `/industries/retail` · Education
  `/industries/education` · Sport `/industries/sport` · Media & Entertainment `/industries/media-entertainment` ·
  Professional Services `/industries/professional-services` · Non-Profit Organizations `/industries/non-profit` ·
  Beauty & Wellness `/industries/beauty-wellness`

### Industry page template · `/industries/[industry]` · **template**

Applied to every industry page. Critical: each page must be substantively different — pulling from the case study system and the Technologies taxonomy so the page is rich content, not thin SEO bait.

| # | Block | Description |
|---|---|---|
| 1 | Hero | Industry-specific challenge framing. Not "we work in [industry]" — "the [industry] problems we solve." |
| 2 | Common pain points | 3-5 issues seen repeatedly in this vertical. Each with a one-line "how we address it." |
| 3 | Services optimised for [industry] | The subset of VECTO services most relevant — not all categories apply equally to all industries. |
| 4 | Compliance & standards | HIPAA, PCI-DSS, FERPA, GDPR-specific notes for regulated verticals. For non-regulated industries, this block is replaced with "Industry-specific quality standards." |
| 5 | Featured case studies | 3-5 cases pulled from the case study system, filtered to this industry. |
| 6 | Tech stack typically used | Filtered slice of the Technologies taxonomy. |
| 7 | Industry-specific FAQ | Distinct from the homepage FAQ — questions specific to this vertical. |
| 8 | Talk to a specialist | The team member with deepest experience in this vertical. |
| — | Sticky Estimator CTA | Persistent floating Estimator CTA throughout scroll — industry pages are Tier-2 conversion surfaces. Mirrors the sticky Estimator on Our Work and the service pages. |
| 9 | Estimator + Schedule CTA | Dual CTA closing the page. |

## Site structure — Our Work / Portfolio

### Our Work / Portfolio · `/our-work` · **full**

**Description.** The single most important page after the homepage for the non-technical founder. Where doubt becomes confidence — or doesn't.

**Design rationale.** Filter-led, editorial rhythm without grouping machinery. Structural reference:
  miiind.co/portfolio — header + filters, then a featured section, then an asymmetric project grid built on three
  aspect-ratio presets (1:1, 2:3, 3:2). Curation lives in the featured section and grid ordering; discovery lives in
  the URL-driven filters and the facet entry pages. Filter facets: Industry, Technology, Service with sub-services,
  Platform, Country, Company stage.

| # | Block | Description |
|---|---|---|
| 1 | Hero | "[N] projects. [N] industries. [N] outcomes that mattered." Counter-driven proof of scale — counts computed at build time from the content, never hardcoded. |
| 2 | Filter strip | Sticky horizontal filter bar: Service · Sub-services · Industry · Technology · Platform · Country · Company stage ("Company stage" is the single company-lifecycle facet). *(detail below.)* |
| 3 | Featured projects | Curated section ahead of the grid — hand-picked via a CMS featured flag + order; larger editorial cards. |
| 4 | Asymmetric project grid | All projects, each card using one of three aspect-ratio presets (1:1, 2:3, 3:2) set per project in the CMS — which also means three image-constraint sets in the content model. Card: thumbnail + client + industry tag + service tag. Cards lead on client + tags rather than a quantified result (the headline-metric feature is parked). |
| 5 | Filter result count | Live count of projects matching current filters — client-side; no stats endpoint. |
| 6 | Sticky Estimator CTA | Persistent throughout scroll. |
| 7 | Closing CTA | "Want a project like one of these? Get an estimate →" |

Row detail (moved out of the table for line length; same authority as the rows above):

- **Row 2 · Filter strip:** On-hub filtering is pure query-param state: dropdowns compose freely (service + industry +
  anything), never navigate, all filter views noindex. Facet landing pages exist as separate entry pages (see the
  facet landing template) — the hub's filter controls do not link to them. Filter state lives in the URL (shareable,
  reflected in the controls); query states matching a promoted facet carry a canonical tag to its landing page. The
  Service/Sub-services and Industry dropdowns include a client-side keyword filter (combobox pattern) — with this many
  industries and sub-services, type-to-narrow beats scrolling.

> **URL note.** Case study detail pages live under `/projects/`, preserved verbatim from the live site (see the case study template's URL contract). The hub and its facet/filter URLs share a consistent base of their own — the exact name (`/our-work` vs `/portfolio`) is a pre-launch naming call, not a structural one.

### Case study page template · `/projects/[project-name]` · **template**

Applied to every individual case study — the conversion-critical asset of the site. For non-technical founders, foreground the client's starting point ("non-technical founder, pre-revenue, idea on a napkin"), not just the technical output.

| # | Block | Description |
|---|---|---|
| 1 | Hero | Client name, industry tag, services tag, hero image / product visual. External product CTA where a live product exists — "Launch website / Try now / Download app" (optional CMS field pair `cta_label` + `cta_url`; hidden when absent — exercise the absent case in placeholder data). *(detail below.)* |
| 2 | Client snapshot | Who they were at engagement start: stage, size, industry, technical maturity. Critical for founder-persona case studies. |
| 3 | Challenge | What the client was trying to solve, in their own language where possible. The fear, not just the brief. |
| 4 | Approach | How VECTO framed the work. What was ruled in / out. Key decisions and their rationale. |
| 5 | Tech stack used | Surfaces the Technologies taxonomy with badges linking to technology pages. |
| 6 | Timeline & team composition | Engagement model, duration, FTE count, roles. |
| 7 | Outcomes | Quantified, ideally with before/after framing. Multiple metrics where possible. |
| 8 | Testimonial | Named, with role and company. Specific to one outcome. |
| 9 | What's next for this client | Optional: ongoing relationship, what they're building now. Signals long-term partnership. |
| 10 | Related case studies | Pulled from same industry, service, technology, or company stage tags. |
| 11 | CTA | "Run your numbers" (Estimator) + "Talk to the team that built this" (Schedule, with the actual delivery lead pre-selected) + the external product CTA repeated where present. |

Row detail (moved out of the table for line length; same authority as the rows above):

- **Row 1 · Hero:** No headline outcome metric in the hero (parked feature); the quantified results live in the
  Outcomes block (7).

> **URL contract — verbatim preservation.** Case study pages live at `/projects/[project-name]`. For every project
that exists in the current live portfolio, the full URL is preserved verbatim (e.g. `/projects/sentigraph-ai/`) —
these are ranking pages; zero redirects, zero slug changes. The portfolio hub and its facet/filter URLs follow their
own consistent base (`/our-work` vs `/portfolio` — a naming call decidable any time before launch); only the
case-study detail URLs demand exactness.

### Facet landing page template · `/our-work/industry/[industry]` · `/our-work/service/[service]` · **template · new**

Promoted single-facet filter states of the portfolio, realized as real, prerendered, indexed landing pages (per
`fe-arch` §2c). Launch set: the industries + the service categories + AI Transformation — but the set is CMS-driven,
never hardcoded: creating a facet entry in the CMS creates its landing page at the next rebuild, with no code change.
Facet types are namespaced in the URL (`/industry/` vs `/service/`) so slugs can never collide; the hub base itself
(`/our-work` vs `/portfolio`) is a pre-launch naming call.

| # | Block | Description |
|---|---|---|
| 1 | Breadcrumb | Home › Our Work › [Facet name] |
| 2 | Facet header | The designed landing state: unique H1 + editorial intro (CMS-fed), replacing the generic hub hero. This is what makes the page a landing page rather than a filter view. |
| 3 | Filter strip | Same strip as the hub, with the active facet shown as selected. Any interaction moves the visitor into normal hub query-param filtering (the one-way door) — the strip never navigates between landing pages. |
| 4 | Filtered project grid | Same card grid as the hub, filtered to the facet. Pagination as on the hub. |
| 5 | Empty / low-count state | Designed state for 0–2 projects — a facet can exist before projects are tagged to it. |
| 6 | Metadata | Own title, description, OG image per facet — CMS fields. |
| 7 | Closing CTA | Same as hub: "Want a project like one of these? Get an estimate →" |

> **Entry pages, not filter states — the one-way door.** Facet landings are where visitors *arrive*; the hub is where
they *explore*. They are the canonical link targets everywhere except the hub's filter controls: industry/service page
cross-links ("See all Healthcare projects →"), megamenu browse links, marketing deep-links (homepage AI band), ads,
search, sitemap. The hub's own filter UI never navigates to them — on-hub filtering stays pure query-param state, so
dropdowns compose freely with no page-shape shifts mid-filtering. On a facet landing the filter strip works normally:
touching it moves the visitor into hub query-param filtering (the one-way door). Query states that match a promoted
facet canonicalize to its landing page. A visitor browsing from the homepage may never see a facet landing — by design
— yet the pages sit fully inside the internal link graph.

> **Content model & cross-linking.** One small CMS entity per promoted facet: facet type, slug, title, editorial intro, SEO fields. Each industry page and service category page links to its facet landing from its case-studies block ("See all [facet] projects →") — internal links that feed both discovery and ranking.

## Site structure — How We Work

### How We Work hub · `/how-we-work` · **full · new**

**Description.** The umbrella page for the "How We Work" top-level nav item. For a non-technical founder, this is
  where the agency goes from "broad capability" to "trustworthy partner." Five sub-areas live underneath: Process and
  Engagement Models (the buyer-facing reassurance pages), plus the three reference hubs — Technologies, Methodologies,
  and Tools (they serve the secondary persona and SEO long-tail rather than the first-visit founder — which is why
  they live here, not in primary nav). Why VECTO is parked in the Appendix, off this hub.

**Design rationale.** The hub functions as a "menu of reassurances" — each section answers a specific founder objection. Process visualisation gets the most space because process visibility is the highest-leverage trust signal for this persona.

| # | Block | Description |
|---|---|---|
| 1 | Hero | "How we work — the part that matters more than the tech." |
| 2 | Process snapshot | Visual 5-step strip with 1-line summary of each. Link to full Process page. |
| 3 | Engagement models snapshot | 4-card module. Link to full Engagement Models page. |
| 4 | Reference hubs | Three entry cards — Technologies (the full stack we build with), Methodologies (how we run delivery — Agile, CI/CD, etc.), Tools (what we work in day-to-day). Each links to its hub. Lighter visual weight than Process/Engagement — these are reference surfaces, not conversion drivers. |
| 5 | Process FAQ | "How much of my time will this take?" / "Who do I talk to day-to-day?" / "What happens when we disagree?" / "How do you handle bad news?" |
| 6 | Estimator + Schedule CTA | Dual CTA closing the page. |

### Process page · `/how-we-work/process` · **full · new**

**Description.** Dedicated page mapping the full five-step engagement journey: *Kickoff → Scoping → Execute → Launch →
  Iterate*. The single highest-leverage page on the site for the non-technical founder persona — pre-emptively answers
  the #1 objection ("what's it like to work with you?"). Distinct from the 6-stage transformation journey used in the
  Services taxonomy: this describes how a single engagement is run, regardless of which service is being delivered.

**Design rationale.** Each stage gets equal visual weight even though their durations differ. For each: duration, deliverables, who's involved on both sides, communication rituals, and what the client should prepare. A "Sample first 30 days" timeline at the bottom makes the abstract concrete.

| # | Block | Description |
|---|---|---|
| 1 | Hero | "From first conversation to live product — every step, no surprises." |
| 2 | Process visualisation | Large interactive 5-step diagram, each step expandable. |
| 3 | Stage 1 — Kickoff | Duration, deliverables, who's involved, what client prepares, sample artefact. |
| 4 | Stage 2 — Scoping | Same anatomy. |
| 5 | Stage 3 — Execute | Same anatomy. More detail given founder anxiety. |
| 6 | Stage 4 — Launch | Same anatomy. |
| 7 | Stage 5 — Iterate | Same anatomy. Cross-link to Support & Maintenance for clients who want a longer-term operating partner. |
| 8 | Sample first 30 days | Concrete timeline showing what week 1, 2, 3, 4 look like. |
| 9 | Communication cadence | Standups, demos, retros, escalation paths. |
| 10 | Tools we use | Slack, Jira, Figma, GitHub, etc. — practical transparency. |
| 11 | FAQ | Process-specific deep questions. |
| 12 | Estimator + Schedule CTA | Dual CTA closing the page. |

### Engagement Models page · `/how-we-work/engagement-models` · **full · new**

**Description.** Side-by-side comparison of the four commercial models VECTO offers. Critical for the non-technical founder who has never hired an agency — they don't know what these terms mean, why they cost differently, or which fits them. Every term defined in plain English.

**Design rationale.** Decision-tree-led, not catalogue-led. Visitor enters the page with a question ("which model is right for me?") and the page is structured to answer it. Comparison table is secondary, after the decision tree.

| # | Block | Description |
|---|---|---|
| 1 | Hero | "Four ways to work with us — pick the one that fits where you are." |
| 2 | Decision tree | Interactive Q&A: "Do you know exactly what you want? · Do you have a fixed budget? · Will scope likely change? · Do you have your own engineers?" → recommends a model. |
| 3 | Fixed Price | What it is (plain English), best when..., risks, cost mechanism, control mechanism, real example. |
| 4 | Time & Material | Same anatomy. |
| 5 | Dedicated Team | Same anatomy. |
| 6 | Staff Augmentation / Outstaffing | Same anatomy. |
| 7 | Comparison table | All four side-by-side: cost predictability, scope flexibility, control, speed-to-start, fit-for-stage, typical duration. |
| 8 | FAQ | "Can we change models mid-engagement?" / "What's included in the rate?" / "How do you handle scope creep on Fixed Price?" |
| 9 | Estimator + Schedule CTA | Dual CTA closing the page. |

### Technologies hub · `/how-we-work/technologies` · **full**

**Description.** Reference hub primarily serving the secondary persona (Scale-up Product Lead) and SEO long-tail
  traffic. Functions as a credibility check — "do you know what we use?" — and as an entry point for technically-led
  searches. Lives under How We Work rather than top-level nav: the non-technical founder isn't digging through a tech
  stack on a first or second visit. Deliberately a glorified index with minimal marketing fluff.

**Design rationale.** Three-group structure: Frontend / Backend / Infrastructure & DevOps. For each technology, a brief plain-English explanation of what it is and why it matters — addresses both audiences (founders skimming, technical readers verifying). Each technology links to its dedicated page following the technology template.

| # | Block | Description |
|---|---|---|
| 1 | Hero | "The technical foundation behind every project we ship." Sub-headline frames depth without bragging. |
| 2 | Frontend technologies | Card grid, one per technology: React, React Native, Vue, Next.js, JavaScript, TypeScript, Tailwind, Ant Design, Elementor, WordPress. |
| 3 | Backend technologies | Card grid, one per technology: Node.js, C#, .NET, PHP, Laravel, WooCommerce, PostgreSQL, Redis, Elastic Search, Kafka, Microservices, Cloud Transcoding, AI. |
| 4 | Infrastructure & DevOps | Card grid, one per technology: AWS, Docker, Kubernetes, Terraform, Cloud, Grafana, Sentry, Mapbox, GitHub Actions, Nginx. |
| 5 | Featured case studies | 3-4 projects with prominent stack badges, demonstrating these technologies in production. |
| 6 | FAQ | "What if our stack isn't here?" / "Do you specialise in any of these?" / "How do you choose what to use for a new project?" |
| 7 | Estimator CTA | Closing CTA. |

> **URL migration — flag for dev/SEO.** Every technology page URL changes from `/technologies/[tech]` to
`/how-we-work/technologies/[tech]`, and the hub from `/technologies` to `/how-we-work/technologies`. These are
existing ranking surfaces: **301 redirects from every old URL to its new path are required**, plus a sitemap update
and internal-link sweep. The SEO hit is accepted knowingly (the technical long-tail is not the primary persona's entry
path), but the redirects must be in place at launch to preserve what equity exists. Under the static-first
architecture, redirects are configured at the hosting layer — there is no server of ours to write them into.

**Cross-references that still point here.** Several other pages surface "a filtered slice of the Technologies taxonomy" — the Software Development tech stack, Industry page tech stacks, case study stack badges, the AI Transformation tech stack. All of those references resolve to `/how-we-work/technologies/[tech]`. No content change to those pages beyond the URL base.

### Technology page template · `/how-we-work/technologies/[tech-name]` · **template**

Applied to every technology page *(one per technology, across the 3 groups above)*. Dual audience: non-technical founders (skim for "do you know this?") and technical readers (verify depth). Plain-English explanation upfront, technical depth below the fold.

| # | Block | Description |
|---|---|---|
| 1 | Hero | Technology name, logo, one-line plain-English summary ("React is what your product's interface is built with"). |
| 2 | What it is | 2 paragraphs: plain-English explanation, then technical detail. |
| 3 | Why we use it | VECTO's POV on this technology — when it's the right choice, when we'd recommend something else. |
| 4 | Where we use it | Services and industries where this tech regularly appears. |
| 5 | Case studies built with this tech | 3-5 cases from the case study system, filtered to this technology tag. |
| 6 | Related technologies | Frequently paired tech (e.g. React → TypeScript → Next.js). |
| 7 | FAQ | Common questions about this tech: maturity, ecosystem, cost implications. |
| 8 | Estimator CTA | "Building with [tech]? Get an estimate." |

### Methodologies hub · `/how-we-work/methodologies` · **full · new**

**Description.** Reference hub, sibling to Technologies and Tools under How We Work. Indexes the delivery
  methodologies VECTO works by — the "how we run the work" layer that sits beneath the client-facing 5-step Process.
  Like Technologies, a reference surface rather than a conversion page: it serves the technically-literate evaluator
  and captures SEO long-tail ("agile development agency", "CI/CD outsourcing", etc.).

**Design rationale.** Its own hub rather than folded into Technologies because methodologies are not technologies —
  conflating them would be a category error and muddy the index. Each methodology gets a plain-English explanation of
  what it is and what it means for the client (predictability, transparency, quality), then technical depth for the
  evaluator. Distinct from the Process page: Process is the buyer-facing engagement journey; Methodologies is the
  practitioner-level discipline that underpins it.

| # | Block | Description |
|---|---|---|
| 1 | Hero | "How we run the work — the disciplines behind reliable delivery." |
| 2 | Delivery methodologies | Card grid: Agile, Scrum, Kanban, and how VECTO actually applies them (not dogma). |
| 3 | Engineering practices | Card grid: CI/CD, TDD, code review, pair programming, trunk-based development. |
| 4 | Quality & reliability | Card grid: QA approach, automated testing, observability, incident response. |
| 5 | How this shows up for you | Plain-English: what these disciplines mean for a non-technical client — predictability, fewer surprises, maintainable output. |
| 6 | FAQ | "Do I need to understand any of this?" / "How rigidly do you follow Scrum?" / "What if my team works differently?" |
| 7 | Estimator CTA | Closing CTA. |

### Methodology page template · `/how-we-work/methodologies/[methodology]` · **template**

*(Representative set below · final list with the SEO team.)* Mirrors the technology page template. Dual audience: non-technical clients (skim for "what does this mean for me?") and technical evaluators (verify rigour). Plain-English upfront, practitioner detail below.

| # | Block | Description |
|---|---|---|
| 1 | Hero | Methodology name, one-line plain-English summary ("CI/CD is how we ship changes safely, many times a day"). |
| 2 | What it is | 2 paragraphs: plain-English explanation, then technical detail. |
| 3 | Why we use it | VECTO's POV — when it applies, how dogmatically we follow it, when we adapt. |
| 4 | What it means for you | Client-facing benefit: predictability, transparency, quality, speed. |
| 5 | How it works in practice | Concrete: cadences, artefacts, tooling that supports it. |
| 6 | Related methodologies & tools | Frequently paired practices and the tools that support them. |
| 7 | FAQ | Common questions about this methodology. |
| 8 | Estimator CTA | Closing CTA. |

**Roster** — Delivery: Agile · Scrum · Kanban — Engineering: CI/CD · TDD · Code Review · Trunk-based Development — Quality: Automated Testing · QA Process · Observability · Incident Response

### Tools hub · `/how-we-work/tools` · **full · new**

**Description.** Reference hub, sibling to Technologies and Methodologies under How We Work. Indexes the day-to-day tools VECTO works in — the practical delivery, collaboration, AI, and development tooling. Like its siblings, a reference surface for the technically-literate evaluator and an SEO long-tail capture, not a conversion page.

**Design rationale.** Its own hub for the same category-consistency reason as Methodologies: tools are not
  technologies and not methodologies. Honest framing in the copy — these are the tools we happen to work in well; the
  choice between, say, Slack and Teams is not a differentiator and the page shouldn't pretend it is. The value here is
  transparency (the client sees exactly how they'll collaborate with us) plus SEO surface, not persuasion.

| # | Block | Description |
|---|---|---|
| 1 | Hero | "The tools we work in — so you know exactly how we'll collaborate." |
| 2 | Collaboration & delivery | Card grid: Slack, Jira, Linear, Notion, Figma — the day-to-day surfaces a client touches. |
| 3 | Development & deployment | Card grid: GitHub, GitLab, CI runners, container/registry tooling. |
| 4 | AI tooling | Card grid: the AI/dev tools VECTO uses internally to ship faster — ties back to the AI positioning (we use AI in our own process). |
| 5 | How we work with your tools | Plain-English: we adapt to your stack where it makes sense; flexibility over dogma. |
| 6 | FAQ | "Can you use our tools instead?" / "Do we get access to project boards?" / "How do you handle tool sprawl?" |
| 7 | Estimator CTA | Closing CTA. |

### Tool page template · `/how-we-work/tools/[tool]` · **template**

*(Representative set above · final list with the SEO team.)* Mirrors the technology and methodology templates. Lightest of the three — most tool pages are thin by nature and exist mainly for SEO surface and transparency. Plain-English first. "Thin" means short and few blocks, not templated filler: the positioning principle above binds here too, so a page with nothing specific to say about a tool is better cut than padded.

| # | Block | Description |
|---|---|---|
| 1 | Hero | Tool name, one-line plain-English summary ("Jira is where we track the work so you can see it too"). |
| 2 | What it is | Short plain-English explanation. |
| 3 | How we use it | Where this tool sits in a VECTO engagement and what the client sees of it. |
| 4 | What it means for you | Visibility, collaboration, hand-off — the client-facing angle. |
| 5 | Related tools & methodologies | What it pairs with. |
| 6 | Estimator CTA | Closing CTA. |

## Site structure — Get an Estimate (standalone)

### Get an Estimate · `/get-an-estimate` · **full · new**

**Description.** The primary conversion page — the non-technical founder cannot scope their own project, so we scope
  it for them. Launch version: a simple estimate-request form. Flow: fill → submit → success state offers an optional
  Schedule a Call. Submissions arrive by email via the provider endpoint — no CMS storage at launch (a CRM is the
  correct upgrade if volume ever justifies one). The AI-assisted on-site estimation generator is a later release — its
  spec is parked in the Appendix, and this page is designed as the slot it drops into (same URL, same entry points).

**Design rationale.** Friction-minimal, plain-language form; no jargon dropdowns; the page sets the expectation of a fast human reply rather than promising instant output. Scheduling is offered after submission, when it's a natural next step, not as a competing entry path.

| # | Block | Description |
|---|---|---|
| 1 | Hero | "Tell us about your project — get a ballpark from the team." Sets the reply expectation (e.g. within one business day). No calls required, no commitment. |
| 2 | Estimate form | Plain-language fields: project description (free text, "describe it the way you would to a friend"), optional scope selectors (service interest, timeline, budget bracket), contact details. Provider-backed per the site-wide forms note (Contact section). |
| 3 | What happens after you submit | Three steps, honestly stated: we read it → you get a ballpark range by email → optional call if you want to talk it through. Absorbs the "how accurate is this?" reassurance. |
| 4 | Success state | The one designed post-submit moment: confirmation + optional Schedule a Call step ("want to talk it through sooner?"). |
| 5 | Comparable case studies | Editorially curated "projects like yours" teaser linking into the portfolio. (A dynamically-populated version rides with the AI estimator — Appendix.) |
| 6 | "Wondering which way to work with us?" | Cross-link to the Engagement Models page (helps the visitor weigh Fixed Price vs. Dedicated Team vs. Outstaffing, including the build-vs-extend-team question). (If Why VECTO is ever revived — Appendix — it's a natural cross-link to add here.) |

> **Forward slot — the AI estimator's return.** When the AI estimation generator ships (post-launch), it augments or
replaces the form on this same page as a client island backed by its own API/runtime — separate from the site backend,
inside a prerendered page shell, never gating first paint, with this form as its no-JS/error fallback. Until then the
launch site has zero runtime dependencies. Full parked spec: Appendix.

## Site structure — Schedule a Call (standalone)

### Schedule a Call · `/schedule-a-call` · **full · new**

**Description.** Calendly-style booking page for a 30-minute discovery call. Distinct from the generic Contact form — the warmest possible CTA for a qualified prospect. Adds a face to the agency by showing real human availability. Reached primarily from the estimate flow's success state and the About menu — not a peer path on the Contact page.

**Design rationale.** The page itself is mostly the calendar widget. Surrounding context reduces booking anxiety: who you'll speak to, what to expect from the call, what to bring, what happens after.

| # | Block | Description |
|---|---|---|
| 1 | Hero | "Book 30 minutes with someone who can actually answer your questions." |
| 2 | Booking widget | Calendar with real availability, named team members. |
| 3 | Who you'll meet | Photos, names, roles, and one-line bios of available scoping leads. |
| 4 | What to expect | Agenda for a typical first call: 10 min context, 15 min discussion, 5 min next steps. |
| 5 | What to bring | Optional: a one-line description of your project, any existing materials. |
| 6 | What happens after | "You'll get a written summary within 24 hours. No automatic sales follow-up. No commitment." |
| 7 | "Not ready to talk yet?" estimate cross-link | Soft secondary on-ramp below the booking content for prospects not ready to book — links to Get an Estimate ("Get a ballpark first →"). |

## Site structure — Resources / Blog

### Resources / Blog hub · `/blog` *(also reachable as /resources)* · **full**

**Description.** Top-of-funnel content hub. Less critical for direct conversion but important for SEO surface and for the "is this agency credible / thoughtful?" check. Houses Blog and Glossary, with a Get-an-Estimate cross-promo.

**Design rationale.** Lighter design treatment than conversion-focused pages. Function: index and discoverability. Featured posts module surfaces editorial picks; categories help directed visitors.

| # | Block | Description |
|---|---|---|
| 1 | Hero | "What we've learned, written up." |
| 2 | Featured posts | 3-4 editor's picks. |
| 3 | Category chips | Single-select chip row of the primary thematic categories (placeholder set, final list with the content/SEO team: Tech News · Company Updates · Insights · Guides). *(detail below.)* |
| 4 | Recent posts grid | Filterable via the category chips (navigate to category routes) and by author (author pages). Pagination pattern is a design call to validate in the wireframe — leaning "load more" over numbered pages; both are SSG-friendly. |
| 5 | Author spotlight | Featured author this month with their recent posts. |
| 6 | Glossary entry point | Card linking to the Glossary. |
| 7 | Cross-promo cards | Cards linking to Get an Estimate and Engagement Models. (A Tools entry returns with the AI estimator — Appendix.) |
| 8 | Newsletter signup | Optional opt-in. |

Row detail (moved out of the table for line length; same authority as the rows above):

- **Row 3 · Category chips:** Each chip is a real link to its prerendered category route `/blog/category/[topic]` —
  because categories are single-select there's no composition conflict, so the chips ARE the navigation; no separate
  tiered nav on the hub.

### Blog post template · `/blog/[post-slug]` · **mention**

Standard editorial article anatomy: title, author byline, date, body content, related posts, newsletter signup, share.
Author byline links to the author page. **Two-tier categorization:** each post carries exactly one primary thematic
category (routable — the post appears on its `/blog/category/[topic]` page) plus secondary **relations** into the
site's own IA — related *projects*, *services*, *technologies*, and *industries*. Relations power cross-discovery
modules in both directions (the post shows its related entities; service, technology, industry, and case-study pages
pull their related posts) and never create routes.

### Blog category page template · `/blog/category/[topic]` · **mention · new**

Prerendered landing page per primary category: own H1 (+ optional CMS intro), filtered post grid, own metadata. Mirrors the portfolio facet-landing logic, with one difference: reached directly from the hub's category chips (single-select — no one-way door needed). Category set is CMS-driven, never hardcoded.

### Author page template · `/blog/authors/[author-slug]` · **mention**

Author bio, photo, role at VECTO, areas of expertise, list of their posts, social links. Doubles as a low-stakes "named team" surface — makes the team visible without committing every team member to a Schedule a Call slot.

### Glossary hub · `/glossary` · **full**

**Description.** A–Z index of plain-English definitions of tech and delivery terms, written for the non-technical founder. A utilitarian Tier-3 reference surface reached from the Resources menu ("Browse A–Z") and the footer; its primary job is wayfinding to the individual glossary-entry pages and capturing long-tail SEO.

| # | Block | Description |
|---|---|---|
| 1 | Hero + search | Short framing line ("Tech terms, explained for founders") with a prominent search/filter field for finding a term fast — client-side search over a build-time index (the HES pattern); no search backend. |
| 2 | A–Z quick-jump nav | Sticky alphabet bar jumping to the letter-grouped sections; letters with no entries are disabled. |
| 3 | Letter-grouped term index | Terms grouped A–Z, each linking to its glossary-entry page with a one-line definition preview. |
| 4 | Closing CTA | Soft conversion nudge ("Still unsure what you need? Get an estimate →"). |

### Glossary entry template · `/glossary/[term]` · **mention**

Single-term definition page targeting long-tail SEO. Plain-English definition for the non-technical founder. Optional related terms list, related blog posts, and a single CTA at the bottom (typically "See [term] in our work" linking to a query-param filtered portfolio view — terms are not promoted facets, so these views stay noindex).

## Site structure — About

### About hub · `/about` · **full**

**Description.** Lightweight umbrella page for the company area, existing for nav consistency — the About megamenu headline is clickable and needs a destination. The expected journey is that most visitors skip the hub and deep-link from the menu straight to Company, Team, Careers, or Testimonials; the hub serves stragglers and direct-URL visitors. Deliberately unsophisticated design-wise.

| # | Block | Description |
|---|---|---|
| 1 | Hero | Short framing line — who VECTO is in two sentences. |
| 2 | Section cards | Four entry cards: Company · Team · Careers · Testimonials. |
| 3 | Contact strip | Schedule + Estimator dual CTA. |

### Company · `/about/company` · **full**

**Description.** The "humanise the agency" narrative page — the company's story and identity.

| # | Block | Description |
|---|---|---|
| 1 | Hero | Company-story framing. |
| 2 | History | Founding story, key milestones, where we are today. |
| 3 | Mission & Vision | Mission and vision statements. |
| 4 | Partners | Technology partners, certified partnerships. |
| 5 | Trust signals | Aggregate numbers: years, projects, retention, NPS, awards. |
| 6 | Team callout | Cross-link to `/about/team` — faces belong there. |
| 7 | Contact / CTA | Schedule + Estimator dual CTA. |

### Team · `/about/team` · **full**

**Description.** Where a founder decides whether these are people they want to work with. Named individuals make the leadership visible.

| # | Block | Description |
|---|---|---|
| 1 | Hero | "The team behind every project we ship." |
| 2 | Leadership grid | Named, photographed, role + bio. |
| 3 | Specialists grid | Named, photographed, role. Author-page cross-links where they write. |
| 4 | Careers callout | "Want to join them?" → `/about/careers`. |
| 5 | Contact / CTA | Schedule + Estimator dual CTA. |

### Careers · `/about/careers` · **full · new**

**Description.** Standalone job list page. Each listing is tagged per the Technologies taxonomy (the tags link to technology pages) and links to its own job posting page.

| # | Block | Description |
|---|---|---|
| 1 | Hero | Short "working at VECTO" framing. |
| 2 | Open roles list | Job cards: title, team, location/remote, technology tags. Each links to its posting page. Empty state designed ("no open roles right now — leave your CV"). |
| 3 | "Don't see your role?" | General application form (provider-backed, per the site-wide forms note). |

### Job posting template · `/about/careers/[job-slug]` · **template · new**

Detail page per open role — shareable link for job boards and social, plus an SEO surface. Application form lives on the page (provider-backed, per-job).

| # | Block | Description |
|---|---|---|
| 1 | Breadcrumb | Home › About › Careers › [Role] |
| 2 | Role hero | Title, team, location/remote, employment type. |
| 3 | About the role | What the person will do and with whom. |
| 4 | Responsibilities & requirements | Two lists. |
| 5 | Tech stack | Technology tags linking to technology pages. |
| 6 | Application form | Per-job, provider-backed: name, contact, CV upload, note. |
| 7 | Related roles | Other open postings. |

> **Content model.** Job entity: title, slug, team, location/type, description blocks, technology tags (relation), open/closed status. Publish/unpublish drives the list and the empty state.

### Testimonials · `/about/testimonials` · **full · new**

**Description.** The dedicated testimonials page. All testimonials and reviews live on-site in the CMS — fields: author, company, testimonial text, link to source (Google / Clutch / GoodFirms / etc.). No embedded third-party widgets.

| # | Block | Description |
|---|---|---|
| 1 | Hero | "What clients say" framing + aggregate trust numbers. |
| 2 | Featured testimonials | 2-3 editorially picked, larger treatment. |
| 3 | Full testimonial list | All CMS testimonials: author, company, text, source link. |
| 4 | Review-platform strip | Platform badges as static trust marks with outbound links to the profiles. |
| 5 | Closing CTA | Estimator + Schedule dual CTA. |

## Site structure — Contact (standalone)

### Contact · `/contact` · **full**

**Description.** Two intent-clear paths. Scheduling is not a peer path — it's the optional step offered after an estimate submission; the Schedule a Call page itself remains (About menu, direct bookings) without billing as a co-equal entry.

**Design rationale.** The form is the cost of doing business; the choice is the value — and two choices choose faster than three. Ready buyers take the estimate path; everyone else (general inquiries, partnerships, press) sends a question. Nobody is forced through the wrong funnel, and nobody stalls comparing three doors.

| # | Block | Description |
|---|---|---|
| 1 | Hero | "How would you like to start?" |
| 2 | Path 1 — Get an Estimate | Card with Estimate CTA. "Best when you have a project in mind and want numbers." |
| 3 | Path 2 — Send a question | Lightweight contact form. "Best for general inquiries, partnerships, press." |
| 4 | Office locations | Map + addresses where applicable. |
| 5 | Direct contacts | Email, phone, social channels. |

> **Architecture note — forms are provider-backed, site-wide.** All forms on the site (contact, estimate request,
newsletter signup, job applications) post to provider endpoints — Formspree-class form handling, an email-marketing
provider for newsletter — requiring zero custom backend on either path. The Schedule-a-Call booking widget is an
embedded third-party client island. Every one of these is a small client leaf inside an otherwise static page. **This
note is the single source for the pattern; individual page entries don't repeat it.**

## Mention & structural placement

### Static / legal pages · **mention**

| Page | URL | Placement |
|---|---|---|
| Privacy Policy | `/privacy` | Footer utility row |
| Terms of Use | `/terms` | Footer utility row |
| Cookie Policy | `/cookies` | Footer utility row |
| Sitemap (HTML) | `/sitemap` | Footer utility row |
| 404 / Error pages | — | Branded, with prominent search and links to top entry points |

### Country pages (Service Areas) · `/service-areas/[country]` · **mention**

Footer-only placement — the pages remain to preserve their SEO long-tail capture, without occupying primary nav real estate that belongs to buyer-facing entry points. Each country page follows a thin template (country-specific headline, services available, local case studies if any, currency & timezone notes, contact). Placement: Footer column 3.

### Year pages · `/[year]` · **mention**

Footer-only placement. Used for year-in-review or annual content; SEO-targeted long-tail. Placement: Footer column 4 (Resources). If these pages don't exist as customer-facing content yet, validate with the SEO team whether they're worth keeping at all (open question).

## Appendix — deferred features

### Why VECTO — parked, not deleted · **deferred**

The Why VECTO comparison page is not part of the active IA: absent from the How We Work hub, the How We Work megamenu,
the About area, and the footer. The outline is preserved here in case a future iteration revives it — for example, if
sales or analytics surface a need for an explicit "vs. the alternatives" page. If revived, the natural home is under
How We Work (`/how-we-work/why-vecto`), as a sixth sibling alongside Process, Engagement Models, Technologies,
Methodologies, and Tools. The outline below is the last approved version, retained verbatim.

**Description.** Comparison page contrasting VECTO with the realistic alternatives a buyer is weighing. For the non-technical founder, the comparison frame is not "agency vs. agency" — it's "outsource vs. hire a CTO vs. find a co-founder vs. buy no-code." This page addresses that real choice.

**Design rationale.** Honest comparison rather than dismissive. Each alternative gets credit for what it does well — the page argues for VECTO without trashing the alternatives. Each comparison ends with a real client story showing why they chose VECTO over that specific alternative.

| # | Block | Description |
|---|---|---|
| 1 | Hero | "You have options. Here's where we fit, and where we don't." |
| 2 | vs. Hire in-house | What in-house is good for · what it's not · case study of a founder who chose VECTO instead and why. |
| 3 | vs. Freelance marketplace | Same anatomy. |
| 4 | vs. Big-4 consultancy | Same anatomy. |
| 5 | vs. Commodity offshore | Same anatomy. |
| 6 | vs. No-code / off-the-shelf | For the non-technical founder specifically — when no-code is the right answer and when it isn't. |
| 7 | When VECTO is NOT the right fit | Honest disqualification: "if you need [X], here's who you should talk to instead." Builds trust through honesty. |
| 8 | Estimator + Schedule CTA | Dual CTA closing the page. |

### AI estimation generator — deferred to a later release · **deferred**

The AI-assisted on-site estimator (in-house development) is deferred; the launch `/get-an-estimate` page carries a
simple provider-backed form instead. When it ships, it returns to the same URL as a client island backed by its own
API — see the forward-slot note on the Get an Estimate page. Also parked with it: the "Project Estimator" tool naming
and the Resources-menu Tools entry — both return when the AI estimator does. The parked interaction spec, verbatim:

Plain-language inputs, not dropdowns of jargon. Visitor describes their project the way they would to a friend ("a marketplace for second-hand musical instruments with payments and a mobile app"). The AI parses, asks clarifying questions, returns a ballpark range with a recommended engagement model. Output is shareable as a hook for organic distribution.

| # | Block | Description |
|---|---|---|
| 1 | Hero | "Get a ballpark range in 90 seconds. No calls, no commitment." |
| 2 | Estimator widget | The interactive tool itself. Conversational input, structured clarifying questions, real-time output. |
| 3 | Output card | Cost range · timeline range · recommended engagement model · suggested next step (Schedule a Call / explore comparable case studies). |
| 4 | "How accurate is this?" | Honest answer about ranges, what makes them tighter or wider, what a real scoping conversation adds. |
| 5 | Comparable case studies | 3 case studies matching the estimator's interpretation of the project type, dynamically populated. |
| 6 | Save / share output | Email me the result, share link, download PDF. |
| 7 | Homepage mini-version | Optional 2-question embedded mini-estimator with "Continue to full estimate" CTA (slots into the homepage Estimate CTA block). |

### Security & Compliance — on hold, parked · **deferred**

Off all visible surfaces — the About menu, the footer Company column, the About-area cross-links, and the Contact page's procurement path. The page outline below is preserved verbatim for when the security-posture content is ready to stand behind. If revived, the natural home is under About (`/about/security-compliance`).

**Description.** Single page covering the agency's security posture. Primarily serves enterprise procurement and regulated-industry buyers — not the primary persona, but its absence is a deal-killer for a meaningful percentage of inbound enterprise leads.

**Design rationale.** Framed as "our security posture" — about practices and commitments, not just certifications. Even aspirational framing clears the bar for most buyers; silence does not. Certifications can be added as they're achieved.

| # | Block | Description |
|---|---|---|
| 1 | Hero | "How we protect your code, your data, and your IP." |
| 2 | Certifications | SOC 2 / ISO 27001 / GDPR / HIPAA — those held, with dates. Those in progress, with target dates. |
| 3 | NDA & IP ownership | Standard NDA process; clear IP-transfer policy; code escrow availability. |
| 4 | Data handling | Where data lives, who has access, retention, destruction. |
| 5 | Secure development practices | Code review, dependency scanning, secret management, deployment isolation. |
| 6 | Compliance experience | Industries in which we have delivered to compliance requirements (Finance, Healthcare). |
| 7 | Security review process | How we accommodate buyer-side security review and questionnaires. |
| 8 | Contact for security | Direct contact for procurement and InfoSec teams. |
