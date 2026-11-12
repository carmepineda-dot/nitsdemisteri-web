// Analítica (Google Analytics 4) només amb consentiment previ.
// Sense resposta o amb "Rebutja", no es carrega res de Google ni es posa cap galeta.
(() => {
  const GA_ID = 'G-738EGQL3PH'; // ID de mesura de GA4 (Administració → Fluxos de dades)
  const KEY = 'nits-galetes'; // 'si' | 'no'
  const ready = /^G-[A-Z0-9]{6,}$/.test(GA_ID) && GA_ID !== 'G-XXXXXXXXXX';

  const get = () => { try { return localStorage.getItem(KEY); } catch (e) { return null; } };
  const set = (v) => { try { localStorage.setItem(KEY, v); } catch (e) { /* sense emmagatzematge */ } };

  function loadGA() {
    if (!ready || window.__gaLoaded) return;
    window.__gaLoaded = true;
    window.dataLayer = window.dataLayer || [];
    window.gtag = function () { window.dataLayer.push(arguments); };
    window.gtag('js', new Date());
    window.gtag('config', GA_ID);
    const s = document.createElement('script');
    s.async = true;
    s.src = `https://www.googletagmanager.com/gtag/js?id=${GA_ID}`;
    document.head.appendChild(s);
  }

  // Si es retira el consentiment, s'esborren les galetes de GA d'aquest domini.
  function clearGA() {
    for (const c of document.cookie.split(';')) {
      const name = c.split('=')[0].trim();
      if (/^_ga/.test(name)) {
        for (const d of ['', `; domain=${location.hostname}`, `; domain=.${location.hostname}`]) document.cookie = `${name}=; expires=Thu, 01 Jan 1970 00:00:00 GMT; path=/${d}`;
      }
    }
  }

  function banner() {
    if (!ready || document.getElementById('cookieBox')) return;
    const box = document.createElement('div');
    box.id = 'cookieBox';
    box.className = 'cookie';
    box.setAttribute('role', 'dialog');
    box.setAttribute('aria-label', 'Galetes');
    box.innerHTML = `<p>Fem servir galetes d'analítica (Google Analytics) per saber quantes persones visiten la web i millorar-la. Només s'activen si les acceptes. <a href="/galetes/">Més informació</a></p>
      <div class="cookie-btns"><button type="button" data-c="no">Rebutja</button><button type="button" data-c="si">Accepta</button></div>`;
    box.addEventListener('click', (e) => {
      const v = e.target.closest('button')?.dataset.c;
      if (!v) return;
      set(v);
      box.remove();
      if (v === 'si') loadGA();
      else { clearGA(); if (window.__gaLoaded) location.reload(); } // GA ja carregat: es recarrega perquè deixi de mesurar
    });
    document.body.appendChild(box);
  }

  // Enllaç del peu "Galetes": torna a preguntar.
  window.nitsGaletes = () => { document.getElementById('cookieBox')?.remove(); banner(); };

  const v = get();
  if (v === 'si') loadGA();
  else if (v !== 'no') (document.readyState === 'loading' ? document.addEventListener('DOMContentLoaded', banner) : banner());
})();
