// "Repte per als pares": tres enigmes de mostra. Si t'equivoques, t'explica quin error has fet,
// tal com fa el joc amb els infants.
(() => {
  const box = document.getElementById('parentQuiz');
  if (!box) return;
  const Q = [
    {
      k: '2n de primària', q: 'Al mercat compres una poma de <b>35 cèntims</b> i un pa de <b>48 cèntims</b>. Quant pagues?',
      ok: '83 cèntims',
      opts: [['83 cèntims', ''], ['73 cèntims', "T'has deixat la desena que es porta: 5 + 8 = 13, i aquella desena de més s'ha de sumar a les desenes."], ['713 cèntims', 'Has escrit 7 i 13 un al costat de l\'altre: les 13 unitats són 1 desena i 3 unitats.'], ['13 cèntims', 'Només has sumat les unitats (5 + 8). Falten les desenes: 30 + 40.']],
    },
    {
      k: '4t de primària', q: 'Quin tros de pizza és més gran: <b>1/4</b> o <b>1/8</b>?',
      ok: '1/4',
      opts: [['1/8', 'És l\'error més típic! Com més trossos fas de la pizza, més petit és cada tros: 1/8 és la meitat d\'1/4.'], ['1/4', ''], ['Són iguals', 'No: si parteixes la mateixa pizza en 4 o en 8, els trossos de 4 són el doble de grans.']],
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
