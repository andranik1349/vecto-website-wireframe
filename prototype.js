/* ════════════════════════════════════════════════════════════════════════
   prototype.js — PROTOTYPE-ONLY interactions. DO NOT PORT TO PRODUCTION.
   ────────────────────────────────────────────────────────────────────────
   This file exists purely to make the static wireframe feel clickable for
   stakeholder review. It is intentionally framework-free, un-optimised, and
   full of hard-wired demo data (estimator ranges, decision-tree outcomes).
   The production site will replace all of this with real components/back-end.

   DESKTOP-ONLY (hard constraint #1 / build-plan §6): there is deliberately NO
   mobile / hamburger / responsive-drawer logic here. The header hamburger is an
   inert ARIA-only affordance; this script never opens a mobile menu.

   Lucide: each page loads the icon library via CDN in its <head>:
       <script src="https://unpkg.com/lucide@latest"></script>
   and we call lucide.createIcons() once on DOMContentLoaded so every
   <i data-lucide="name"></i> renders as SVG. No emojis anywhere.

   Every feature below is guarded — if its markup isn't on the current page,
   the initialiser simply returns. One file is shared by all pages.
   ════════════════════════════════════════════════════════════════════════ */

(function () {
  'use strict';

  /* ── tiny helpers ──────────────────────────────────────────────────── */
  const $  = (sel, ctx = document) => ctx.querySelector(sel);
  const $$ = (sel, ctx = document) => Array.from(ctx.querySelectorAll(sel));


  /* ════════════════════════════════════════════════════════════════════
     0. LUCIDE ICONS — render all <i data-lucide> placeholders
     ════════════════════════════════════════════════════════════════════ */
  function initIcons() {
    if (window.lucide && typeof window.lucide.createIcons === 'function') {
      window.lucide.createIcons();
    } else {
      // CDN not reachable (e.g. opened offline via file://) — fail quietly.
      console.warn('[prototype] Lucide not loaded; icons will not render.');
    }
  }


  /* ════════════════════════════════════════════════════════════════════
     1. MEGAMENUS + DROPDOWNS
     Triggers: <button class="nav__link" aria-haspopup aria-expanded
               aria-controls="<panelId>"> inside a .nav__item.
     Panel: element with that id carrying [hidden].
     Opens on hover (with close-delay so the cursor can travel to a
     full-width panel that lives outside the .nav__item) AND on click;
     keyboard accessible (Esc closes + restores focus, Tab-out closes).
     ════════════════════════════════════════════════════════════════════ */
  function initMenus() {
    const triggers = $$('.nav__link[aria-controls]');
    if (!triggers.length) return;

    const entries = triggers
      .map((trigger) => {
        const panel = document.getElementById(trigger.getAttribute('aria-controls'));
        const item  = trigger.closest('.nav__item');
        return panel && item ? { trigger, panel, item } : null;
      })
      .filter(Boolean);

    function open(entry) {
      entries.forEach((e) => e !== entry && close(e));
      entry.trigger.setAttribute('aria-expanded', 'true');
      entry.item.classList.add('is-open');
      entry.panel.hidden = false;
    }

    function close(entry) {
      entry.trigger.setAttribute('aria-expanded', 'false');
      entry.item.classList.remove('is-open');
      entry.panel.hidden = true;
    }

    function closeAll() { entries.forEach(close); }

    entries.forEach((entry) => {
      const { trigger, panel, item } = entry;
      const isOpen = () => trigger.getAttribute('aria-expanded') === 'true';

      // Click-only open/close (no hover) — keyboard-accessible via the button.
      trigger.addEventListener('click', (e) => {
        e.preventDefault();
        isOpen() ? close(entry) : open(entry);
      });

      // Esc closes and returns focus to the trigger.
      panel.addEventListener('keydown', (e) => {
        if (e.key === 'Escape') { close(entry); trigger.focus(); }
      });
      trigger.addEventListener('keydown', (e) => {
        if (e.key === 'Escape') close(entry);
      });

      // Tab out of the whole item+panel closes it.
      [item, panel].forEach((el) => {
        el.addEventListener('focusout', (e) => {
          const to = e.relatedTarget;
          if (to && (item.contains(to) || panel.contains(to))) return;
          close(entry);
        });
      });
    });

    // Click anywhere outside any menu closes them all.
    document.addEventListener('click', (e) => {
      if (!e.target.closest('.nav__item') && !e.target.closest('.megamenu')) closeAll();
    });
  }


  /* ════════════════════════════════════════════════════════════════════
     2. ACTIVE NAV LINK (HES approach — resolved pathname, no false-match)
     Derives the current top-level section from the URL's first path segment
     and flags the matching primary-nav trigger/link. Normalising the path
     means /services/ and /services/index.html and /services/web-development
     all resolve to the "services" section without a deep-page false match.
     ════════════════════════════════════════════════════════════════════ */
  function initActiveNav() {
    const nav = $('.nav');
    if (!nav) return;

    // First non-empty path segment, e.g. "/services/web-development.html" → "services".
    const segs = location.pathname.split('/').filter(Boolean);
    let section = segs[0] || '';
    if (section.endsWith('.html')) section = ''; // a root-level page like index.html / contact.html

    // Map a URL section → the aria-controls id (megamenu) or href (direct link)
    // of the primary-nav element that represents it.
    const SECTION_TO_PANEL = {
      'services':       'mm-services',
      'who-we-serve':   'mm-who',
      'industries':     'mm-who',        // industries live under the Who We Serve axis
      'our-work':       null,            // direct link, matched by href below
      'how-we-work':    'mm-howwework',
      'blog':           'mm-resources',
      'glossary':       'mm-resources',
      'get-an-estimate':'mm-resources',
      'about':          'mm-about',
      'contact':        'mm-about',
      'schedule-a-call':'mm-about',
    };

    function flag(linkEl) {
      if (!linkEl) return;
      linkEl.classList.add('nav__link--current');
      linkEl.setAttribute('aria-current', 'page');
    }

    if (section && section in SECTION_TO_PANEL) {
      const panelId = SECTION_TO_PANEL[section];
      if (panelId) {
        flag($(`.nav__link[aria-controls="${panelId}"]`, nav));
      } else {
        // Direct link (Our Work): match by resolved pathname.
        $$('a.nav__link', nav).forEach((a) => {
          const linkSeg = new URL(a.href, location.href).pathname.split('/').filter(Boolean)[0] || '';
          if (linkSeg === section) flag(a);
        });
      }
    }
  }


  /* ════════════════════════════════════════════════════════════════════
     3. ACCORDION (FAQ toggle)
     Markup contract:
       <div class="accordion" data-accordion>
         <div class="accordion__item">
           <button class="accordion__trigger" aria-expanded="false"
                   aria-controls="faq-1">Question…</button>
           <div class="accordion__panel" id="faq-1" hidden>Answer…</div>
         </div> …
       </div>
     Add data-accordion="single" to auto-close siblings.
     ════════════════════════════════════════════════════════════════════ */
  function initAccordions() {
    const groups = $$('[data-accordion]');
    if (!groups.length) return;

    groups.forEach((group) => {
      const single   = group.dataset.accordion === 'single';
      const triggers = $$('.accordion__trigger', group);

      triggers.forEach((trigger) => {
        const panel = document.getElementById(trigger.getAttribute('aria-controls'));
        if (!panel) return;

        trigger.addEventListener('click', () => {
          const willOpen = trigger.getAttribute('aria-expanded') !== 'true';

          if (single && willOpen) {
            triggers.forEach((t) => {
              t.setAttribute('aria-expanded', 'false');
              const p = document.getElementById(t.getAttribute('aria-controls'));
              if (p) p.hidden = true;
            });
          }
          trigger.setAttribute('aria-expanded', String(willOpen));
          panel.hidden = !willOpen;
        });
      });
    });
  }


  /* ════════════════════════════════════════════════════════════════════
     4. STICKY ESTIMATOR CTA — show after scrolling past the hero,
        hide near the very top. Toggles .is-visible (styled in components.css).
     ════════════════════════════════════════════════════════════════════ */
  function initStickyEstimator() {
    const cta = $('.sticky-estimator');
    if (!cta) return;

    const SHOW_AFTER = 600; // px scrolled before it appears
    let ticking = false;

    function update() {
      cta.classList.toggle('is-visible', window.scrollY > SHOW_AFTER);
      ticking = false;
    }
    window.addEventListener('scroll', () => {
      if (!ticking) { window.requestAnimationFrame(update); ticking = true; }
    }, { passive: true });
    update();
  }


  /* ════════════════════════════════════════════════════════════════════
     5. PORTFOLIO FILTERING (client-side) + live result count
     Markup contract:
       <div data-filter-group>
         <button class="tag tag--button" data-filter="all">All</button>
         <button class="tag tag--button" data-filter="ai">AI</button> …
       </div>
       <span data-filter-count></span>
       <article data-portfolio-item data-tags="ai,fintech"> … </article> …
     ════════════════════════════════════════════════════════════════════ */
  function initPortfolioFilter() {
    const group = $('[data-filter-group]');
    const items = $$('[data-portfolio-item]');
    if (!group || !items.length) return;

    const buttons = $$('.tag--button', group);
    const countEl = $('[data-filter-count]');

    function apply(filter) {
      let shown = 0;
      items.forEach((item) => {
        const tags = (item.dataset.tags || '').split(',').map((t) => t.trim());
        const match = filter === 'all' || tags.includes(filter);
        item.hidden = !match;
        if (match) shown++;
      });
      if (countEl) {
        countEl.textContent = shown + (shown === 1 ? ' project' : ' projects');
      }
    }

    buttons.forEach((btn) => {
      btn.addEventListener('click', () => {
        buttons.forEach((b) => b.classList.remove('is-active'));
        btn.classList.add('is-active');
        apply(btn.dataset.filter || 'all');
      });
    });

    // Initialise from whichever chip is pre-marked active, else "all".
    const initial = $('.tag--button.is-active', group);
    apply(initial ? (initial.dataset.filter || 'all') : 'all');
  }


  /* ════════════════════════════════════════════════════════════════════
     6. ENGAGEMENT DECISION TREE (Q&A → recommended model)
     Markup contract:
       <div class="decision-tree" data-decision-tree>
         <div class="decision-question" data-question="start" hidden=false>
           <p class="decision-question__prompt">…</p>
           <div class="decision-answers">
             <button class="btn btn--ghost" data-goto="q2">…</button>
             <button class="btn btn--ghost" data-result="fixed">…</button>
           </div>
         </div> … more [data-question] …
         <div class="decision-result" data-result-panel>
           <span class="decision-result__label">We recommend</span>
           <p class="decision-result__model" data-result-model></p>
           <p class="decision-result__desc" data-result-desc></p>
           <button data-decision-restart>Start over</button>
         </div>
       </div>
     Buttons carry data-goto="<questionName>" (next question) OR
     data-result="<modelKey>" (final recommendation).
     ════════════════════════════════════════════════════════════════════ */
  function initDecisionTree() {
    const tree = $('[data-decision-tree]');
    if (!tree) return;

    const questions = $$('.decision-question', tree);
    const panel     = $('[data-result-panel]', tree);
    const modelEl   = $('[data-result-model]', tree);
    const descEl    = $('[data-result-desc]', tree);

    // Demo-only outcome copy (hard-wired; not a real recommendation engine).
    const MODELS = {
      'fixed':       { model: 'Fixed Price',     desc: 'Defined scope, fixed cost — best when requirements are clear and stable.' },
      'tm':          { model: 'Time & Material', desc: 'Flexible scope billed hourly — best when the build will evolve as you learn.' },
      'dedicated':   { model: 'Dedicated Team',  desc: 'A full team on our payroll, working only on your product over the long term.' },
      'outstaffing': { model: 'Outstaffing',     desc: 'Vetted engineers embedded into your existing team under your direction.' },
    };

    function showQuestion(name) {
      questions.forEach((q) => { q.hidden = q.dataset.question !== name; });
      if (panel) panel.classList.remove('is-visible');
    }

    function showResult(key) {
      const data = MODELS[key];
      if (!data || !panel) return;
      questions.forEach((q) => { q.hidden = true; });
      if (modelEl) modelEl.textContent = data.model;
      if (descEl)  descEl.textContent  = data.desc;
      panel.classList.add('is-visible');
    }

    tree.addEventListener('click', (e) => {
      const btn = e.target.closest('button');
      if (!btn || !tree.contains(btn)) return;

      if (btn.dataset.goto)            showQuestion(btn.dataset.goto);
      else if (btn.dataset.result)     showResult(btn.dataset.result);
      else if ('decisionRestart' in btn.dataset) {
        const first = questions[0];
        showQuestion(first ? first.dataset.question : '');
      }
    });

    // Start on the first question.
    if (questions[0]) showQuestion(questions[0].dataset.question);
  }


  /* ════════════════════════════════════════════════════════════════════
     7. ESTIMATOR WIDGET STUB (2-question mini → placeholder output card)
     Markup contract:
       <form class="estimator" data-estimator>
         <div class="estimator__input">
           <select data-estimator-field="type"> … </select>
           <select data-estimator-field="timeline"> … </select>
           <button type="submit" class="btn btn--main">See my estimate</button>
         </div>
         <div class="estimator__output" data-estimator-output hidden>
           <div class="estimator__metric"><span class="estimator__metric-label">Ballpark cost</span>
             <span class="estimator__metric-value estimator__metric-value--accent" data-estimate="cost"></span></div>
           <div class="estimator__metric"><span class="estimator__metric-label">Timeline</span>
             <span class="estimator__metric-value" data-estimate="time"></span></div>
           <div class="estimator__metric"><span class="estimator__metric-label">Suggested model</span>
             <span class="estimator__metric-value" data-estimate="model"></span></div>
         </div>
       </form>
     Hard-wired demo lookups — NOT a real calculator.
     ════════════════════════════════════════════════════════════════════ */
  function initEstimator() {
    const form = $('[data-estimator]');
    if (!form) return;

    const output = $('[data-estimator-output]', form);

    // Demo cost basis by project type, scaled by timeline urgency.
    const TYPE = {
      'mvp':        { base: '$30k – $60k',   model: 'Fixed Price' },
      'web':        { base: '$45k – $90k',   model: 'Time & Material' },
      'mobile':     { base: '$60k – $120k',  model: 'Time & Material' },
      'platform':   { base: '$120k – $250k', model: 'Dedicated Team' },
      'ai':         { base: '$80k – $180k',  model: 'Dedicated Team' },
    };
    const TIMELINE = {
      'asap':      '6 – 10 weeks (fast-track)',
      'quarter':   '3 – 4 months',
      'half-year': '5 – 7 months',
      'flexible':  'Scoped to fit your roadmap',
    };

    form.addEventListener('submit', (e) => {
      e.preventDefault();
      const type     = ($('[data-estimator-field="type"]', form)     || {}).value || 'web';
      const timeline = ($('[data-estimator-field="timeline"]', form) || {}).value || 'quarter';
      const t = TYPE[type] || TYPE.web;

      const set = (key, val) => { const el = $(`[data-estimate="${key}"]`, form); if (el) el.textContent = val; };
      set('cost',  t.base);
      set('time',  TIMELINE[timeline] || TIMELINE.quarter);
      set('model', t.model);

      if (output) {
        output.hidden = false;
        output.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
      }
    });
  }


  /* ════════════════════════════════════════════════════════════════════
     8. PROCESS STEP EXPANSION (Process page interactive diagram)
     Each <button class="process-step__toggle"> toggles .is-expanded on its
     parent .process-step, revealing the .process-step__detail.
     ════════════════════════════════════════════════════════════════════ */
  function initProcessSteps() {
    const steps = $$('.process-step');
    if (!steps.length) return;

    steps.forEach((step) => {
      const toggle = $('.process-step__toggle', step) || $('.process-step__num', step);
      const detail = $('.process-step__detail', step);
      if (!toggle || !detail) return;

      if (toggle.tagName === 'BUTTON') toggle.setAttribute('aria-expanded', 'false');
      toggle.style.cursor = 'pointer';

      toggle.addEventListener('click', () => {
        const open = step.classList.toggle('is-expanded');
        if (toggle.tagName === 'BUTTON') toggle.setAttribute('aria-expanded', String(open));
      });
    });
  }


  /* ════════════════════════════════════════════════════════════════════
     9. IN-PAGE ANCHOR NAV (services hub + process page)
     <nav class="anchor-nav"> <a class="anchor-nav__link" href="#stage-build">…
     Smooth-scrolls and highlights the link for the section currently in view.
     ════════════════════════════════════════════════════════════════════ */
  function initAnchorNav() {
    const nav = $('.anchor-nav');
    if (!nav) return;

    const links = $$('.anchor-nav__link', nav);
    const map = links
      .map((link) => {
        const id = (link.getAttribute('href') || '').replace(/^#/, '');
        const target = id && document.getElementById(id);
        return target ? { link, target } : null;
      })
      .filter(Boolean);
    if (!map.length) return;

    // Smooth scroll on click.
    map.forEach(({ link, target }) => {
      link.addEventListener('click', (e) => {
        e.preventDefault();
        target.scrollIntoView({ behavior: 'smooth', block: 'start' });
      });
    });

    // Highlight the section in view.
    function setActive(activeLink) {
      links.forEach((l) => l.classList.remove('anchor-nav__link--active'));
      if (activeLink) activeLink.classList.add('anchor-nav__link--active');
    }

    if ('IntersectionObserver' in window) {
      const byTarget = new Map(map.map(({ link, target }) => [target, link]));
      const observer = new IntersectionObserver((entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) setActive(byTarget.get(entry.target));
        });
      }, { rootMargin: '-40% 0px -55% 0px', threshold: 0 });
      map.forEach(({ target }) => observer.observe(target));
    } else {
      setActive(map[0].link);
    }
  }


  /* ════════════════════════════════════════════════════════════════════
     10. RAIL SCROLL AFFORDANCES (optional prev/next for .rail scrollers)
     If a .rail is wrapped in [data-rail] with prev/next buttons, wire them.
       <div data-rail>
         <button data-rail-prev>…</button>
         <div class="rail"> … .rail-item … </div>
         <button data-rail-next>…</button>
       </div>
     ════════════════════════════════════════════════════════════════════ */
  function initRails() {
    const wraps = $$('[data-rail]');
    if (!wraps.length) return;

    wraps.forEach((wrap) => {
      const rail = $('.rail', wrap);
      const prev = $('[data-rail-prev]', wrap);
      const next = $('[data-rail-next]', wrap);
      if (!rail) return;

      const step = () => Math.max(rail.clientWidth * 0.8, 280);
      if (prev) prev.addEventListener('click', () => rail.scrollBy({ left: -step(), behavior: 'smooth' }));
      if (next) next.addEventListener('click', () => rail.scrollBy({ left:  step(), behavior: 'smooth' }));
    });
  }


  /* ════════════════════════════════════════════════════════════════════
     BOOT
     ════════════════════════════════════════════════════════════════════ */
  function init() {
    initIcons();
    initMenus();
    initActiveNav();
    initAccordions();
    initStickyEstimator();
    initPortfolioFilter();
    initDecisionTree();
    initEstimator();
    initProcessSteps();
    initAnchorNav();
    initRails();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
