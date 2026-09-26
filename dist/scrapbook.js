/* Small, event-driven motion layer. No scroll interception or pointer capture. */
(() => {
  const hero = document.querySelector('.hero');
  const reduced = matchMedia('(prefers-reduced-motion: reduce)');
  function replayEntrance() {
    hero.classList.remove('is-entering');
    if (reduced.matches) return;
    // A single layout read restarts the finite entrance, never a per-frame loop.
    void hero.offsetWidth;
    hero.classList.add('is-entering');
  }
  document.querySelector('.replay-entrance').addEventListener('click', replayEntrance);
  reduced.addEventListener('change', () => {
    if (reduced.matches) hero.classList.remove('is-entering');
  });
  replayEntrance();

  const targets = document.querySelectorAll('.intro .section-heading, .next-edition, .partners-heading, .involved .heading-row, .faq h2');
  const observer = new IntersectionObserver(entries => {
    entries.forEach(entry => {
      if (!entry.isIntersecting) return;
      entry.target.classList.add('is-visible');
      observer.unobserve(entry.target);
    });
  }, {threshold: .12});
  targets.forEach(target => { target.classList.add('scrap-reveal'); observer.observe(target); });

  // Keep the small section menu tied to the chapter currently in view.
  const navLinks = [...document.querySelectorAll('.desktop-nav a[href^="#"], .mobile-nav a[href^="#"]')];
  const landmarks = [
    ['#experience', '#experience'], ['#tracks', '#experience'],
    ['#speakers', '#speakers'], ['.community-moment', '#speakers'],
    ['#editions', '#editions'], ['#partners', '#editions'],
    ['#involved', '#involved'], ['.faq', '#involved'], ['#join', '#involved']
  ].map(([selector, href]) => ({element: document.querySelector(selector), href})).filter(item => item.element);
  let scrollUpdatePending = false;
  function updateActiveNavigation() {
    scrollUpdatePending = false;
    const marker = document.querySelector('.site-header').getBoundingClientRect().bottom + 40;
    let activeHref = '';
    for (const landmark of landmarks) {
      if (landmark.element.getBoundingClientRect().top <= marker) activeHref = landmark.href;
    }
    navLinks.forEach(link => {
      const active = link.getAttribute('href') === activeHref;
      link.classList.toggle('is-active', active);
      if (active) link.setAttribute('aria-current', 'location');
      else link.removeAttribute('aria-current');
    });
  }
  function scheduleNavigationUpdate() {
    if (scrollUpdatePending) return;
    scrollUpdatePending = true;
    requestAnimationFrame(updateActiveNavigation);
  }
  window.addEventListener('scroll', scheduleNavigationUpdate, {passive: true});
  window.addEventListener('resize', scheduleNavigationUpdate, {passive: true});
  window.addEventListener('hashchange', scheduleNavigationUpdate);
  scheduleNavigationUpdate();

  const passport = document.querySelector('#passport');
  document.querySelectorAll('.track').forEach(track => {
    track.addEventListener('click', () => {
      if (reduced.matches || track.getAttribute('aria-pressed') !== 'true') return;
      passport.classList.remove('stamp-pop');
      void passport.offsetWidth;
      passport.classList.add('stamp-pop');
    });
  });
  passport.addEventListener('animationend', event => {
    if (event.target === passport) passport.classList.remove('stamp-pop');
  });
})();
