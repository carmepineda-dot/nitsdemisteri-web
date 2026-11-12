// Efectes de la web: aparició suau en fer scroll, cuques de llum i música opcional.
// La música mai no sona sola: només si es prem el botó (els navegadors bloquegen el so automàtic i molesta).
(() => {
  const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;

  // Aparició en fer scroll
  const els = document.querySelectorAll('.reveal');
  if (!reduce && 'IntersectionObserver' in window) {
    const io = new IntersectionObserver((entries) => {
      for (const e of entries) if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); }
    }, { rootMargin: '0px 0px -8% 0px' });
    els.forEach((el) => io.observe(el));
  } else els.forEach((el) => el.classList.add('in'));

  // Cuques de llum a la portada
  const hero = document.querySelector('.hero');
  if (hero && !reduce) {
    const box = document.createElement('div');
    box.className = 'flies';
    box.setAttribute('aria-hidden', 'true');
    for (let i = 0; i < 14; i++) {
      const f = document.createElement('i');
      f.style.left = `${(i * 53) % 100}%`;
      f.style.top = `${40 + ((i * 37) % 55)}%`;
      f.style.animationDelay = `${(i % 7) * -1.3}s, ${(i % 5) * -0.9}s`;
      f.style.animationDuration = `${9 + (i % 5) * 2}s, ${2.4 + (i % 4) * 0.6}s`;
      box.appendChild(f);
    }
    hero.prepend(box);
  }

  // Música (Web Audio, sense fitxers): una melodia nocturna suau en bucle.
  const btn = document.getElementById('musicBtn');
  if (!btn) return;
  let ctx = null, timer = null, on = false;
  const NOTES = [57, 60, 64, 67, 64, 60, 62, 65, 69, 65, 62, 59, 55, 59, 62, 64]; // MIDI
  const freq = (m) => 440 * Math.pow(2, (m - 69) / 12);
  function note(m, t, len, vol) {
    const o = ctx.createOscillator(), g = ctx.createGain();
    o.type = 'sine'; o.frequency.value = freq(m);
    g.gain.setValueAtTime(0, t);
    g.gain.linearRampToValueAtTime(vol, t + 0.04);
    g.gain.exponentialRampToValueAtTime(0.0001, t + len);
    o.connect(g).connect(ctx.destination);
    o.start(t); o.stop(t + len + 0.05);
  }
  function bar() {
    const t0 = ctx.currentTime + 0.05, step = 0.42;
    NOTES.forEach((m, i) => note(m + 12, t0 + i * step, 1.1, 0.05));
    [45, 48, 43, 47].forEach((m, i) => note(m, t0 + i * step * 4, step * 4.2, 0.035));
  }
  function start() {
    ctx = ctx || new (window.AudioContext || window.webkitAudioContext)();
    ctx.resume();
    bar();
    timer = setInterval(bar, 0.42 * 16 * 1000);
  }
  function stop() { clearInterval(timer); timer = null; ctx?.suspend(); }
  btn.addEventListener('click', () => {
    on = !on;
    on ? start() : stop();
    btn.setAttribute('aria-pressed', String(on));
    btn.setAttribute('aria-label', on ? 'Apaga la música' : 'Engega la música');
  });
  document.addEventListener('visibilitychange', () => { if (!ctx || !on) return; document.hidden ? ctx.suspend() : ctx.resume(); });
})();
