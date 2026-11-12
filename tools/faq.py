# Genera la secció de preguntes freqüents de la portada i el seu JSON-LD (FAQPage).
# Executar: python3 tools/faq.py  (reescriu el bloc entre <!-- FAQ:INICI --> i <!-- FAQ:FI --> d'index.html)
import json, os, re, html
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

FAQ = [
 ('El joc', [
  ("Què és Nits de Misteri?", "Un joc de matemàtiques en català per a nens i nenes de primària, de 1r a 6è. Cada aventura dura 12 nits i cada nit hi ha un enigma de mates per resoldre. De dia, amb les peces guanyades, l'infant construeix el seu refugi i després el seu propi poblat, amb cases, animals i records de cada aventura."),
  ("Per a quines edats és?", "Per a infants de 6 a 12 anys, de 1r a 6è de primària. En crear el personatge es tria el curs, i el joc no posa mai reptes per sobre d'aquest curs."),
  ("Segueix el currículum de l'escola?", "Sí. Els continguts segueixen el currículum de matemàtiques de primària de Catalunya (Decret 175/2022): numeració i càlcul, mesura i diners, el rellotge, geometria i simetria, fraccions i decimals, sèries i patrons, i les primeres idees de probabilitat, cadascun en el curs que toca."),
  ("Quins tipus de reptes hi ha?", "Dotze: enigmes amb història, reptes de manipular (pagar amb monedes, repartir, construir nombres, la recta numèrica), càlcul ràpid, el pont dels nombres, la balança, el rellotge de la torre, les petjades (sèries), el reflex màgic (simetria), el sac de gemmes (probabilitat), l'escut màgic (fraccions), troba l'impostor i, a partir de 4t, el gran enigma de diversos passos. Els tens explicats a <a href=\"/reptes/\">Els reptes</a>."),
  ("Quant dura una partida?", "Una aventura de 12 nits dura uns 10-15 minuts. Es pot deixar a mitges: el joc la guarda i es continua on s'havia quedat."),
 ]),
 ('Com aprèn', [
  ("S'adapta al nivell de cada infant?", "Sí, i per habilitats. El rellotge, el càlcul, les fraccions o la geometria pugen o baixen de nivell per separat segons com respon: quan l'encerta diverses vegades sense ajuda, aquella habilitat puja; si s'hi equivoca, baixa. Així un infant que domina el càlcul però encara s'embolica amb les hores rep reptes a la seva mida en cada cosa."),
  ("Què passa quan s'equivoca?", "El joc no només diu que està malament: detecta quin error ha fet (per exemple, oblidar la desena que es porta, confondre l'àrea i el perímetre o llegir les agulles del rellotge al revés) i li explica com es fa. Després pot tornar-ho a provar amb un exercici semblant."),
  ("Què és el truc del mussol?", "Si el mateix error es repeteix, el mussol li ensenya un truc amb dibuixos i li proposa un parell d'exercicis per practicar-lo. Quan el supera, l'error queda marcat com a après al panell d'adults i al llibre d'encanteris de l'infant."),
  ("Pot ajudar amb les taules de multiplicar?", "Sí. Hi ha càlcul ràpid i enigmes de multiplicar adaptats al curs, i quan s'equivoca d'un grup el joc li ho fa veure amb dibuixos de grups iguals. A les <a href=\"/guies/taules-de-multiplicar/\">guies</a> hi ha consells per practicar-les a casa."),
  ("Té veu per als que encara no llegeixen bé?", "Sí. A 1r i 2n, el joc llegeix els enunciats en veu alta en català, i a tots els cursos hi ha un botó per escoltar-los. Fa servir la veu catalana del dispositiu; si n'hi ha una de millorada instal·lada, la tria."),
 ]),
 ('Per a les famílies', [
  ("Té anuncis?", "No. Ni anuncis, ni enllaços a altres apps, ni res que distregui de jugar i aprendre."),
  ("És gratuït?", "La descàrrega és gratuïta i la primera aventura completa es pot jugar sense pagar, amb tot el sistema d'aprenentatge (adaptació al nivell, explicació dels errors i trucs del mussol). Les altres aventures, el poblat complet i el joc per a diversos germans formaran part d'una subscripció familiar opcional, que es podrà provar 14 dies gratis. Les compres només es poden fer des del panell d'adults, protegit amb PIN."),
  ("Puc veure com avança el meu fill o la meva filla?", "Sí. El panell d'adults (amb PIN) mostra el nivell de cada habilitat, quins errors s'estan treballant i quins ja s'han superat. Si a casa hi ha diversos germans, es veuen tots alhora."),
  ("Es pot limitar el temps de joc?", "Sí. Al panell d'adults es pot posar un límit de minuts al dia. Quan s'acaba, el joc ho diu amb calma i es pot continuar l'endemà; si cal, s'hi poden afegir 15 minuts més."),
  ("Hi poden jugar diversos germans a la mateixa tauleta?", "Sí, fins a sis, cadascun amb el seu personatge, el seu poblat i el seu nivell."),
  ("Quines dades recull?", "El joc no envia dades a cap servidor: no hi ha comptes ni analítica. El nom (recomanem un sobrenom), el curs i el progrés es guarden al dispositiu. Ho expliquem a la <a href=\"/privacitat/\">política de privacitat</a>."),
 ]),
 ('Instal·lació', [
  ("On es pot descarregar?", "Serà a Google Play per a tauletes i mòbils Android. Ara mateix està en proves amb famílies; quan es publiqui, l'enllaç sortirà en aquesta pàgina."),
  ("Funciona en tauleta?", "Sí. Està pensat sobretot per a tauleta, i també s'adapta al mòbil."),
  ("Hi ha versió per a iPhone o iPad?", "De moment no. Primer surt per a Android; la versió per a iPhone i iPad està prevista més endavant."),
  ("Necessita connexió a internet?", "No. Un cop instal·lat, es pot jugar sense connexió."),
  ("Hi haurà versió en castellà?", "Sí, està prevista. Primer surt en català, i més endavant hi haurà la versió en castellà."),
 ]),
]

def strip(t): return re.sub(r'<[^>]+>', '', t)

# Preguntes que surten també a la portada (la resta, a /preguntes/)
HOME = ["Què és Nits de Misteri?", "Què passa quan s'equivoca?", "És gratuït?", "Té anuncis?", "On es pot descarregar?"]
ALL = {q: a for _, items in FAQ for q, a in items}

def details(q, a): return f'    <details><summary>{html.escape(q)}</summary><p>{a}</p></details>'

# ---- Pàgina /preguntes/ (totes, amb FAQPage) ----
gen = open(f'{ROOT}/tools/generar-guies.py').read()
ns = {}
exec(gen[:gen.index("for g in GUIES:")].replace("ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))", f"ROOT = {ROOT!r}"), ns)
HEAD, FOOT, CTA = ns['HEAD'], ns['FOOT'], ns['CTA']
ld = {"@context": "https://schema.org", "@type": "FAQPage", "inLanguage": "ca", "url": "https://nitsdemisteri.cat/preguntes/",
      "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": strip(a)}} for q, a in ALL.items()]}
out = HEAD.format(title='Preguntes freqüents sobre el joc de mates Nits de Misteri', desc="Preguntes i respostes sobre Nits de Misteri, el joc de matemàtiques en català per a primària: edats, currículum, com s'adapta al nivell, errors, preu, dades, tauleta i més.", path='preguntes/', ogtype='website', ld='<script type="application/ld+json">' + json.dumps(ld, ensure_ascii=False) + '</script>')
out += '<nav class="crumbs" aria-label="Ruta"><a href="/">Inici</a> › Preguntes freqüents</nav>\n<h1>Preguntes freqüents</h1>\n<p>Tot el que les famílies ens pregunten sobre Nits de Misteri, el joc de mates en català per a primària.</p>\n'
for title, items in FAQ:
    out += f'<h2 class="faq-g">{title}</h2>\n' + '\n'.join(details(q, a) for q, a in items) + '\n'
out += CTA + FOOT
os.makedirs(f'{ROOT}/preguntes', exist_ok=True)
open(f'{ROOT}/preguntes/index.html', 'w').write(out)

# ---- Portada: només les principals + enllaç ----
p = f'{ROOT}/index.html'
s = open(p).read()
if '<!-- FAQ:INICI -->' not in s:
    a = s.index('<h2 class="center">Preguntes</h2>') + len('<h2 class="center">Preguntes</h2>')
    b = s.index('  </div>\n</section>\n</main>')
    s = s[:a] + '\n<!-- FAQ:INICI -->\n<!-- FAQ:FI -->\n' + s[b:]
body = '\n'.join(details(q, ALL[q]) for q in HOME) + '\n    <p class="center faq-more"><a href="/preguntes/">Totes les preguntes freqüents →</a></p>'
s = re.sub(r'<!-- FAQ:INICI -->.*?<!-- FAQ:FI -->', lambda m: '<!-- FAQ:INICI -->\n' + body + '\n<!-- FAQ:FI -->', s, flags=re.S)
s = s.replace('<a href="#preguntes">Preguntes</a>', '<a href="/preguntes/">Preguntes</a>')
open(p, 'w').write(s)

# ---- Sitemap ----
sm = open(f'{ROOT}/sitemap.xml').read()
if '/preguntes/' not in sm:
    sm = sm.replace('  <url><loc>https://nitsdemisteri.cat/reptes/', '  <url><loc>https://nitsdemisteri.cat/preguntes/</loc><lastmod>2026-11-12</lastmod></url>\n  <url><loc>https://nitsdemisteri.cat/reptes/')
    open(f'{ROOT}/sitemap.xml', 'w').write(sm)
print('preguntes', len(ALL))
