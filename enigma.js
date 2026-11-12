// "Repte per als pares": tres enigmes de mostra. Si t'equivoques, t'explica quin error has fet,
// tal com fa el joc amb els infants.
(() => {
  const box = document.getElementById('parentQuiz');
  if (!box) return;
  const Q = [
    {
      k: '3r de primària', q: 'El rellotge del campanar marca <b>tres quarts de sis</b>. Quina hora és?',
      ok: '17:45',
      opts: [['17:45', ''], ['18:45', "És l'error més habitual! En català es compten els quarts que han passat cap a l'hora que ve: tres quarts de sis vol dir que falta un quart per a les sis."], ['18:15', "Seria un quart de set. Tres quarts de sis és quan falta un quart per a les sis."], ['15:30', "Has llegit els nombres al revés. Tres quarts (45 minuts) camí de les sis: les 17:45."]],
    },
    {
      k: '5è de primària', q: 'Quin tros de pizza és més gran: <b>3/4</b> o <b>5/8</b>?',
      ok: '3/4',
      opts: [['5/8', "Els nombres són més grans, però els trossos són més petits. Passa-ho a vuitens: 3/4 = 6/8, i 6/8 és més que 5/8."], ['3/4', ''], ['Són iguals', "Gairebé: 3/4 = 6/8, així que hi ha un vuitè de diferència."], ['No es pot saber', "Sí que es pot! Es posen les dues fraccions amb el mateix denominador: 3/4 = 6/8, que és més que 5/8."]],
    },
    {
      k: '6è de primària', q: 'Quant fa <b>3 + 4 × 5</b>?',
      ok: '23',
      opts: [['35', "Has fet les operacions d'esquerra a dreta. Primer va la multiplicació (4 × 5 = 20) i després la suma."], ['23', ''], ['60', 'Has multiplicat tots tres nombres. És 3 + (4 × 5).'], ['27', 'Gairebé! Revisa la multiplicació: 4 × 5 = 20.']],
    },
  ];
  let i = 0, score = 0;
  const shuffle = (a) => a.map((x) => [Math.random(), x]).sort((p, q) => p[0] - q[0]).map((x) => x[1]);

  function render() {
    if (i >= Q.length) {
      if (typeof window.gtag === 'function') window.gtag('event', 'repte_pares', { encerts: score }); // només si s'han acceptat les galetes
      const msg = score === 3 ? "Perfecte! Podeu ajudar amb els deures… o deixar que ho faci el mussol."
        : score === 2 ? 'Molt bé! Un error és normal: per això el joc explica cada error.'
        : "Tranquil·litat: aquí s'aprèn equivocant-se. Igual que al joc.";
      box.innerHTML = `<p class="pq-k">Resultat</p><p class="pq-score">${score} de ${Q.length}</p><p class="pq-q">${msg}</p>
        <button type="button" class="pq-again">Torna-hi</button>`;
      box.querySelector('.pq-again').onclick = () => { i = 0; score = 0; render(); };
      return;
    }
    const it = Q[i];
    box.innerHTML = `<p class="pq-k">Enigma ${i + 1} de ${Q.length} · ${it.k}</p><p class="pq-q">${it.q}</p>
      <div class="pq-opts">${shuffle(it.opts).map(([t]) => `<button type="button">${t}</button>`).join('')}</div>
      <p class="pq-fb" aria-live="polite"></p>`;
    const fb = box.querySelector('.pq-fb');
    box.querySelectorAll('.pq-opts button').forEach((b) => {
      b.onclick = () => {
        const why = it.opts.find(([t]) => t === b.textContent)[1];
        box.querySelectorAll('.pq-opts button').forEach((x) => { x.disabled = true; if (x.textContent === it.ok) x.classList.add('ok'); });
        if (!why) { score++; b.classList.add('ok'); fb.innerHTML = '<b>Correcte!</b>'; }
        else { b.classList.add('ko'); fb.innerHTML = `<b>No és això.</b> ${why}`; }
        const n = document.createElement('button');
        n.type = 'button'; n.className = 'pq-next'; n.textContent = i < Q.length - 1 ? 'Següent enigma' : 'Veure el resultat';
        n.onclick = () => { i++; render(); };
        fb.after(n);
      };
    });
  }
  render();
})();
