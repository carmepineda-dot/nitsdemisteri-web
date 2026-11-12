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

  // Amb «reduir moviment», els vídeos no es reprodueixen sols
  if (reduce) document.querySelectorAll('video[autoplay]').forEach((v) => { v.removeAttribute('autoplay'); v.pause(); v.controls = true; });

  // Vídeo del poblat: alguns mòbils l'aturen (bucle, estalvi de bateria). Es torna a posar en marxa quan es veu.
  const pv = document.getElementById('poblatVid');
  if (pv && !reduce) {
    const go = () => { const pr = pv.play(); if (pr && pr.catch) pr.catch(() => {}); };
    pv.addEventListener('ended', () => { pv.currentTime = 0; go(); });
    if ('IntersectionObserver' in window) new IntersectionObserver((es) => es.forEach((e) => (e.isIntersecting ? go() : pv.pause())), { threshold: 0.25 }).observe(pv);
    setInterval(() => { if (!document.hidden && pv.paused && pv.getBoundingClientRect().top < innerHeight && pv.getBoundingClientRect().bottom > 0) go(); }, 2000);
  }

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
  // Melodia suau: notes greus i espaiades, atac lent, filtre que treu els aguts i un eco lleuger.
  let ctx = null, out = null, timer = null, on = false;
  const MEL = [64, null, 67, null, 69, null, 67, 64, null, 62, null, 60, null, null, 62, null]; // MIDI, null = silenci
  const PAD = [[48, 55, 60], [45, 52, 57], [41, 48, 53], [43, 50, 55]];
  const STEP = 0.75; // segons per pas (lent)
  const freq = (m) => 440 * Math.pow(2, (m - 69) / 12);
  function setup() {
    ctx = new (window.AudioContext || window.webkitAudioContext)();
    const lp = ctx.createBiquadFilter(); lp.type = 'lowpass'; lp.frequency.value = 1400; lp.Q.value = 0.3;
    const delay = ctx.createDelay(); delay.delayTime.value = 0.38;
    const fb = ctx.createGain(); fb.gain.value = 0.28;
    const wet = ctx.createGain(); wet.gain.value = 0.25;
    out = ctx.createGain(); out.gain.value = 0;
    out.connect(lp); lp.connect(ctx.destination);
    lp.connect(delay); delay.connect(fb); fb.connect(delay); delay.connect(wet); wet.connect(ctx.destination);
  }
  function note(m, t, len, vol, attack) {
    const o = ctx.createOscillator(), g = ctx.createGain();
    o.type = 'sine'; o.frequency.value = freq(m);
    g.gain.setValueAtTime(0, t);
    g.gain.linearRampToValueAtTime(vol, t + attack);
    g.gain.exponentialRampToValueAtTime(0.0001, t + len);
    o.connect(g).connect(out);
    o.start(t); o.stop(t + len + 0.1);
  }
  function bar() {
    const t0 = ctx.currentTime + 0.1;
    MEL.forEach((m, i) => { if (m) note(m, t0 + i * STEP, 2.2, 0.022, 0.12); });
    PAD.forEach((ch, i) => ch.forEach((m) => note(m, t0 + i * STEP * 4, STEP * 4.4, 0.012, 1.2)));
  }
  function start() {
    if (!ctx) setup();
    ctx.resume();
    out.gain.cancelScheduledValues(ctx.currentTime);
    out.gain.setValueAtTime(out.gain.value, ctx.currentTime);
    out.gain.linearRampToValueAtTime(1, ctx.currentTime + 2.5); // entra a poc a poc
    bar();
    timer = setInterval(bar, STEP * MEL.length * 1000);
  }
  function stop() {
    clearInterval(timer); timer = null;
    if (!ctx) return;
    out.gain.cancelScheduledValues(ctx.currentTime);
    out.gain.setValueAtTime(out.gain.value, ctx.currentTime);
    out.gain.linearRampToValueAtTime(0, ctx.currentTime + 0.8);
    setTimeout(() => { if (!on) ctx.suspend(); }, 900);
  }
  btn.addEventListener('click', () => {
    on = !on;
    on ? start() : stop();
    btn.setAttribute('aria-pressed', String(on));
    btn.setAttribute('aria-label', on ? 'Apaga la música' : 'Engega la música');
  });
  document.addEventListener('visibilitychange', () => { if (!ctx || !on) return; document.hidden ? ctx.suspend() : ctx.resume(); });
})();
