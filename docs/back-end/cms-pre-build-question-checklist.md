# Questions to force before building a CMS (or any admin tool)

**Doc-key: `cms-checklist` · Species: living reference (a reusable instrument, not a spec).**
**When it binds:** at the CMS/admin build (outline Phases 8–8b) — run once for the whole system,
once per screen before its build, then as a walkthrough lens while building. Not relevant to the
design/front-end phases. **Relation to the other docs:** this doc asks the questions; VECTO's
settled *answers* live in `be-arch` (§3a content-model doctrine, §4 lifecycle/autosave/gating,
§5 admin) and the `outline` verification instruments — where an answer already exists there, the
checklist's job is to verify it actually got built. A question with no settled answer is a
finding to take to the decision log.

*An interrogation checklist — **not** a spec. Run it once for the whole system and once per screen before the build
starts, then reuse it as a walkthrough lens while building. The goal isn't to write more; it's to force answers to the
questions specs quietly skip. **A question you can't answer yet is itself a finding — write it down.** It marks a
decision someone was about to make for you by default.*

*Why this instead of a longer spec: every gap that hurt HES was an interaction or ownership detail — the kind no amount of prose catches, because the wrongness doesn't register until your hands are on the tool. A spec three times longer would have missed most of them. These seven questions catch whole classes of that at once.*

---

### 1. States — what states can each thing be in, and what happens in each?
For every screen, field, and record, list the states and the moves between them.
- Empty · in-progress/draft · complete · published/live · live-with-unsaved-edits · invalid · deleted-but-still-referenced.
- What happens when you save, leave, and come back in each state?
- Which fields are required vs optional — and required *for what*: to save, or to go public?
- Is a half-finished thing allowed to just exist, or does the tool fight you?

*Catches: how autosave behaves, mandatory-vs-optional fields, "saved but not yet live," version history — three of HES's five gaps live here.*

### 2. Control — for everything visible, who can change it and how?
Walk the entire surface — every setting, image, label, list — and tag each: **owner-editable / admin-only / developer-only-forever.**
- Is anything the owner will *expect* to control actually locked to a script or a developer?
- Anything that looks editable but isn't — or looks fixed but should be theirs?
- Where do the easy-to-forget assets live: favicon, social-share image, error pages, email/notification text?

*Catches: the default social-share (OG) image being out of the owner's hands entirely.*

### 3. Navigation — does the tool's layout match how the owner thinks about their own site?
The menu should mirror the owner's mental picture of their product, not the database's structure.
- Could the owner find where to edit any given page without guessing?
- Are related things grouped the way *they'd* group them?
- Do the labels use the owner's words, or internal/technical ones?

*Catches: a sidebar organized by data model, so every item is a guessing game.*

### 4. Empty & extreme — what does it look like with nothing, with one, with too much, or half-done?
Demos are always seeded with tidy data. Ask about the states a demo hides.
- First run, zero content: is it obvious what to do?
- One item; then hundreds — does it still work and stay usable?
- Very long text, a missing image, a translation that's only half finished.

*Catches: bugs that appear only with real content — exactly what hands-on testing on a demo will never show you.*

### 5. Save, lose, recover — what's saved when, and how do you undo?
- Autosave or explicit save — and is that *consistent* across every screen, including "create new"?
- What can be lost: closed tab, crash, navigating away mid-edit?
- Can you undo, restore an earlier version, or discard changes — and is the history readable by a human?

*Catches: a create screen with no autosave while everything else has it; confusing version history.*

### 6. Live vs. draft — what's the difference between saved and public, and can something go live by accident?
- Can you preview exactly how something will look *before* the public sees it?
- Is it ever possible to publish something incomplete or unintended?
- When something does go live, what triggers it, and can it be reversed?

*Catches: edits silently going public the moment you type them.*

### 7. The stuff you can't click to find — how is the invisible layer checked?
The scary category — and the answer here is never "we'll test it by hand." For each, ask how it is checked **automatically**.
- Who can read or write the data directly — and is there a test that *tries to break in as a stranger and must fail*, run on every change?
- What happens on failure: a failed publish, a failed upload, a dropped connection? Does the live site stay up? Is the failure visible or silent?
- Data you can't delete because something else points at it — handled, or does it corrupt?
- Accessibility — keyboard, screen readers, contrast: specced, or an afterthought?

*Catches: the entire class no walkthrough will ever surface — security holes, data corruption, silent failures. This is the category to insist on, because it's the one your own eyes can't police.*

---

**Two rules for using it**
1. A blank answer is a finding, not a delay.
2. Pair the checklist with the two things that actually caught HES's gaps: **build one screen at a time and walk through it**, and put **automated checks on the invisible layer (§7)** so you're not trusting your eyes for what eyes can't see.
