# Content acceptance criteria & draft screening

**Purpose.** The authoritative list of what content must satisfy before it ships to the VECTO site, plus the
diagnostic tells for reviewing a draft against it. Applies to every draft regardless of who wrote it — content/SEO,
design, or a contracted writer. The standing principle it enforces is `ia` §"Guiding principles";
`content-vocab` holds the published-guidance evidence behind the criteria, for when one is disputed.
**Doc-key: `content-screen` · Species: living reference.**

**§1 and §2 are the criteria — this doc is their only home.** Other docs and reviews cite them by ID (`C-4`, `B-5`) and never restate them. §3–§5 are diagnostic: each tell names the criterion it
violates, so a failed screen produces a criterion ID rather than an adjective.

**The one-line test behind all of it:** would this survive if you deleted the target keyword from the
brief entirely? Good content still makes sense and still helps the reader. Slop was built around the keyword and falls apart without it.

**The bar to compare against** is the wireframe (`wireframe/prototype/`), not an abstraction — the React technology page and the Healthcare industry page are the reference standard: plain-English explanation first, specific detail second, no repetition needed to make the point.

---

## 1. Brief criteria — B-1…B-6

A brief must satisfy all six *before* anyone writes to it. A brief that fails these produces copy
that fails §2 no matter who writes it.

| ID | Criterion | Test |
|---|---|---|
| **B-1** | Names the **search intent** in a sentence — what the person wants to find out or do. | Can you state, from the brief alone, what the reader came for? |
| **B-2** | Lists the **real questions and subtopics** the page must answer. | Is there anything to write about besides the keyword? |
| **B-3** | Points at the **IA block table** for the target URL and says which blocks the copy fills. | Does the brief reference `ia`, or was it written without the IA in hand? |
| **B-4** | States the **target URL, matching the IA route exactly** (including sub-service nesting). | Does the URL exist in `ia`? Paste-match it, don't eyeball it. |
| **B-5** | Contains **no density target, no repetition count, no mandated exact-match headings**. A word count, if present, is labelled an estimate of the output — never a requirement to hit. | Grep the brief for "density", "times", "word count". Any of these as a *requirement* fails. |
| **B-6** | Names 2–3 **reference pages to out-explain** — each defensible against §2 itself. | Would the reference page pass our own criteria? If not, it teaches the writer the wrong lessons (C-16). |

## 2. Page-content criteria — C-1…C-16

All sixteen are MUST. A deliverable failing any one is sent back with the ID named.

**Substance**

| ID | Criterion | Test |
|---|---|---|
| **C-1** | **Keyword-independent.** The page still makes sense and still helps the reader with the target phrase deleted throughout. | Delete it. Read it. Does it still say something? |
| **C-2** | **One non-transferable specific per section** — a number, a named technology, a named project, a real constraint, or a first-hand detail. | Could this section be pasted onto a competitor's site unchanged? If yes, it fails. |
| **C-3** | **No unsupported claim.** Any assertion about results, client sentiment, or scale is backed on the page or links to the evidence. | "Clients consistently highlight…" with no review attached is a fail. |
| **C-4** | **Non-commodity angle.** The page says something only someone who has done the work would know. | Google's own contrast: *"7 Tips for First-Time Homebuyers"* (commodity) vs *"Why We Waived the Inspection & Saved Money"* (non-commodity). Which is this closer to? |

**Structure**

| ID | Criterion | Test |
|---|---|---|
| **C-5** | **One idea per section; no two sections make the same claim.** | Summarise each section in one clause. Duplicate clauses get cut, not renamed. |
| **C-6** | **Headings answer a question a reader actually has.** The target phrase appears in a heading only where it is the natural wording. | Read the headings alone as a list. Do they read as a table of contents, or as a keyword being repeated? |
| **C-7** | **FAQ entries are distinct buyer objections.** No two questions ask about the same entity; no answer defines a term by restating it. | "What are X services?" answered with "X services are services that X" is a fail. |
| **C-8** | **Block structure matches the IA for that URL**; length is derived from what must be said. | Diff the section list against the `ia` block table. Missing blocks and invented blocks are both findings. |

**Voice**

| ID | Criterion | Test |
|---|---|---|
| **C-9** | **Survives reading aloud.** Every paragraph sounds like something a person would say to another person. | Read it out. Flag anything you'd never say. |
| **C-10** | **Plain language first**, technical depth second — per the `ia` "Non-technical founder first" principle. | Would a non-technical founder know what this means on first read? |
| **C-11** | **No sentence template repeated across sibling items.** | Line the siblings up. If the only variable is the nouns, rewrite them. |
| **C-12** | **Addressed to a person** — second person, specific, not a description of a market segment. | Count sentences whose subject is "businesses" rather than "you". |

**Hygiene**

| ID | Criterion | Test |
|---|---|---|
| **C-13** | **Taxonomy fidelity** — service, sub-service and industry names, counts, and groupings match `ia` exactly. | Paste-diff the lists. Invented or merged entries are a fail even when they read better. |
| **C-14** | **Metadata is human.** Title and description are sentences a person would click, unique per page, not truncated, not pipe-separated keyword lists. | Read the description aloud as a sentence. Does it end? |
| **C-15** | **Internal links resolve to real IA routes**, with naturally varied anchor text. | Paste-match every URL against `ia`. Exact-match anchor text everywhere is its own fail. |
| **C-16** | **Ships clean.** No production notes, placeholder text, reference links, competitor links, or unresolved TODOs in the body. Proofread. | Grep for "reference", "showcase", "integrate real", "http". |

---

## 3. Diagnostic tells — content briefs

Signs the brief is stuck in old-style SEO rather than how ranking actually works now:

- **A required repetition count or density target** — "use the phrase 6–8 times", "aim for 1.5%
  keyword density". There is no correct density number because it isn't how ranking works. This is the clearest single tell of a brief written for 2012. **(B-5)**
- **The exact-match phrase mandated in every H2/H3**, verbatim, regardless of whether it reads naturally there. **(B-5, C-6)**
- **No mention of search intent** — only "target keyword: X". Optimising for the string, not the
  person. **(B-1)**
- **No subtopics, questions, or entities to cover** — one keyword and a word count produces filler padded to length. **(B-2)**
- **A word-count minimum with no corresponding content requirement.** **(B-5)**
- **A URL that isn't in the IA**, or a flat URL where the IA nests the page under its parent service.
  A wrong URL in a brief becomes a wrong internal link and a wrong route at build time. **(B-4)**

## 4. Diagnostic tells — drafted copy

Read a paragraph out loud. If it doesn't sound like something a person would say to another person, it's a flag.

- **The same exact phrase repeated across paragraphs** where a person would naturally vary it.
  **(C-6)**
- **Sentences bent into unnatural word order to fit a keyword.** **(C-9)**
- **No specific claims** — no numbers, no named technology, no concrete example. Genericness is often a bigger tell than repetition. **(C-2)**
- **One sentence template applied across many entries** — "We [verb] [X], [Y], [Z] and [W] for/to
  [benefit]", nouns swapped. The entity-stuffing sibling of keyword repetition: breadth of related terms substituted for saying something. **(C-11)**
- **A trailing sentence per paragraph that adds nothing** — "This also improves consistency across all channels." Padding to reach a length target, visible as an identical rhythm in every
  paragraph. **(C-5, C-11)**
- **Headers that don't map to a real question.** **(C-6)**
- **Near-duplicate FAQ questions** asking about the same entity for keyword coverage, or a
  "what is X" answer that only restates X. **(C-7)**
- **Keyword-stuffed alt text or anchor text.** **(C-15)**
- **Claims of client sentiment with no review attached** — "clients consistently highlight…".
  **(C-3)**
- **Unremoved production notes or reference links in the body** — instructions to the writer, or a bare link to the competitor page the structure was lifted from. Both a proofreading failure and
  evidence the draft was built on someone else's template. **(C-16)**

## 5. Diagnostic tells — on-page / technical recommendations

- **Near-duplicate pages per city or keyword variant** — a doorway pattern (a thin page built only to rank, with nothing distinct for a visitor). The industry-page rule in `ia` exists to prevent
  this, and the Service Areas country pages (`ia` §"Country pages") are already the sanctioned
  version: thin by design, footer-only, not dressed as unique content. **(C-8)**
- **Exact-match anchor text on every internal link** instead of natural variation. **(C-15)**
- **Pipe-separated keyword-list titles or descriptions.** **(C-14)**
- **Changes that hurt the user flow to gain keyword placement** — pushing the hero CTA down for a keyword paragraph, dropping breadcrumbs to fit text. **(C-8, C-10)**
- **Content placed where the IA doesn't put it.** Relocating or expanding content onto a page whose blocks are already specced is a structural change: it goes through the IA, not around it. **(C-8)**

## 6. Questions worth asking of any draft or brief

- "What's the search intent for this page, and how does the brief address it beyond the keyword?"
- "What's your position on keyword density — do you set a target?" (Any target as a hard rule is the flag.)
- "What subtopics or entities does this page need to cover to be genuinely comprehensive?"
- "Would this page still make sense to a reader if I deleted the target phrase?"
- "Which IA blocks does this copy fill?" (Answers whether the IA was open while writing.)

---

**How to use this.** Screen against §1–§2 before anything gets near a page, and report failures as
criterion IDs — "fails C-2 and C-13", not "feels generic". When something fails, restate the *intent*
(what page, what query, what reader need) rather than only rejecting the output; the goal isn't less SEO effort, it's SEO that survives contact with a human reader. If a criterion itself is disputed, the published-guidance backing for it is in `content-vocab` — and a criterion that can't be defended from there should be changed, not enforced.
