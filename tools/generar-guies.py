# Genera les guies per a famílies de nitsdemisteri.cat
import os
import os, json, html
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATE = '2026-11-12'

GUIES = [
 dict(slug='taules-de-multiplicar', title='Com aprendre les taules de multiplicar (sense memoritzar a cegues)',
  short='Les taules de multiplicar',
  desc="Guia per a famílies: com ajudar els infants de primària a aprendre les taules de multiplicar entenent-les, amb trucs per a cada taula i 5 minuts al dia.",
  cursos='2n a 4t de primària',
  body='''
<p>Les taules de multiplicar s'aprenen millor si primer s'entén què volen dir i després es practiquen una mica cada dia. Memoritzar-les de cop, com una cançó, funciona a curt termini, però l'infant s'encalla quan n'oblida una i no sap com refer-la.</p>

<h2>1. Primer, entendre què és multiplicar</h2>
<p>Multiplicar és <b>sumar grups iguals</b>. 3 × 4 vol dir «3 grups de 4»: 4 + 4 + 4 = 12. Abans de memoritzar res, val la pena fer grups amb coses que tingueu a casa (botons, cigrons, peces de construcció) i comptar-les.</p>
<p>Una bona imatge és la <b>graella</b>: 3 files de 4 punts. Si la gireu, són 4 files de 3 punts, i n'hi ha els mateixos. Així l'infant descobreix que <b>3 × 4 = 4 × 3</b>, i que les taules «tenen la meitat de feina».</p>

<h2>2. L'ordre que funciona millor</h2>
<ol>
  <li><b>× 2, × 5 i × 10</b>: són les més fàcils. La del 2 és el doble; la del 10 afegeix un zero; la del 5 és la meitat de la del 10.</li>
  <li><b>× 4</b>: el doble del doble (4 × 7 = doble de 14 = 28).</li>
  <li><b>× 3 i × 6</b>: la del 6 és el doble de la del 3.</li>
  <li><b>× 9</b>: és la del 10 menys una vegada (9 × 7 = 70 − 7 = 63).</li>
  <li><b>× 8</b>: el doble de la del 4.</li>
  <li><b>× 7</b>: la que menys resultats nous té, perquè la majoria ja els sap per altres taules (7 × 3 = 3 × 7).</li>
</ol>

<h2>3. Trucs que ajuden</h2>
<ul>
  <li><b>La taula del 9 amb els dits</b>: amb les mans obertes, s'abaixa el dit que toca (per a 9 × 4, el quart dit). Els dits de l'esquerra són les desenes i els de la dreta, les unitats: 3 i 6, és a dir, 36.</li>
  <li><b>En la del 9, les xifres sumen 9</b>: 18, 27, 36, 45… Serveix per comprovar.</li>
  <li><b>Si n'oblida una, que la refaci</b> a partir d'una que sí que sap: «no sé 6 × 7, però sé 5 × 7 = 35, i n'hi afegeixo un 7: 42».</li>
</ul>

<h2>4. Poca estona, cada dia</h2>
<p>Cinc minuts al dia funcionen més que una hora el cap de setmana. Feu preguntes salteades (no sempre en ordre), al cotxe o mentre pareu taula. Quan s'equivoqui, no cal dir-li la resposta: pregunteu-li com la podria trobar.</p>

<h2>5. Errors típics</h2>
<ul>
  <li><b>Saltar-se un grup o posar-ne un de més</b> (dir 6 × 7 = 48). Torneu a la imatge dels grups: quants grups de 7 hi ha?</li>
  <li><b>Confondre multiplicar i sumar</b> (dir 6 × 7 = 13). Recordeu-li que multiplicar és «grups de».</li>
</ul>
'''),
 dict(slug='aprendre-el-rellotge', title="Com aprendre a llegir el rellotge d'agulles (i els quarts en català)",
  short="Llegir el rellotge",
  desc="Guia per a famílies: com ensenyar a llegir el rellotge d'agulles a primària, de les hores en punt als quarts del sistema català.",
  cursos='1r a 3r de primària',
  body='''
<p>Llegir el rellotge d'agulles costa als infants perquè han de mirar dues coses alhora i, a més, en català fem servir el sistema de <b>quarts</b>, que s'ha d'entendre bé. Ajuda molt anar pas a pas.</p>

<h2>1. Les dues agulles</h2>
<p>La <b>curta</b> marca l'hora i la <b>llarga</b>, els minuts. És l'error més freqüent: llegir-les canviades. Un truc: «la curta és la important, la que diu quina hora és; la llarga corre més perquè ha de fer tota la volta».</p>

<h2>2. L'ordre recomanat</h2>
<ol>
  <li><b>Hores en punt</b>: la llarga a dalt de tot, al 12. «Són les tres en punt.»</li>
  <li><b>I mitja</b>: la llarga a baix, al 6. La curta queda entre dos números.</li>
  <li><b>Els quarts</b>: quan ja domina les anteriors (normalment a partir de 2n).</li>
  <li><b>Els minuts de 5 en 5</b> i, més endavant, el rellotge digital i les hores de 24 (les 15:00 són les 3 de la tarda).</li>
</ol>

<h2>3. Els quarts, el sistema català</h2>
<p>En català es diu l'hora pensant en <b>la que ve</b>. L'hora es divideix en 4 quarts de 15 minuts:</p>
<ul>
  <li>2:15 → <b>un quart de tres</b></li>
  <li>2:30 → <b>dos quarts de tres</b> (també «les dues i mitja»)</li>
  <li>2:45 → <b>tres quarts de tres</b></li>
  <li>3:00 → <b>les tres</b></li>
</ul>
<p>Una imatge que ajuda és una pizza tallada en 4 trossos: cada tros que passa la llarga és un quart, i ens hi acostem a les tres.</p>

<h2>4. Com practicar-ho a casa</h2>
<ul>
  <li>Tingueu un rellotge d'agulles visible i pregunteu l'hora en moments reals: «quina hora és? Falten quants quarts per sopar?».</li>
  <li>Feu servir un rellotge de joguina o de cartró per posar-hi hores vosaltres i que les llegeixi, i al revés.</li>
  <li>Quan s'equivoqui, pregunteu-li primer on és l'agulla curta.</li>
</ul>
'''),
 dict(slug='fraccions-primaria', title='Les fraccions a primària: com explicar-les perquè les entenguin',
  short='Les fraccions',
  desc="Guia per a famílies: com explicar les fraccions a primària amb pizzes, la recta numèrica i errors típics, de 3r a 6è.",
  cursos='3r a 6è de primària',
  body='''
<p>Les fraccions són un dels primers continguts on molts infants s'encallen, perquè contradiuen el que han après dels nombres: <b>1/8 és més petit que 1/4</b>, encara que 8 sigui més gran que 4. Entendre això és la clau de tot.</p>

<h2>1. Què vol dir una fracció</h2>
<p>Una fracció parla de <b>trossos iguals</b> d'una cosa. A 3/4, el 4 (a sota) diu en quants trossos iguals es parteix, i el 3 (a dalt), quants en prenem. Comenceu sempre amb coses reals: una pizza, una pastanaga, una rajola de xocolata.</p>

<h2>2. Més trossos vol dir trossos més petits</h2>
<p>És l'error més comú. Si una pizza es parteix entre 8 persones, a cadascú li toca menys que si es parteix entre 4. Per això <b>1/8 &lt; 1/4</b>. Ho podeu fer amb dos fulls iguals: un el pleguen en 4 i l'altre en 8, i comparen un tros de cada.</p>

<h2>3. Fraccions iguals que semblen diferents</h2>
<p>1/2, 2/4 i 4/8 són la mateixa quantitat: mitja pizza. Si es plega un full per la meitat i després per la meitat una altra vegada, es veu molt clar. Això prepara per a les fraccions equivalents i, més endavant, per sumar fraccions.</p>

<h2>4. Les fraccions a la recta numèrica</h2>
<p>A partir de 4t ajuda molt situar les fraccions en una recta del 0 a l'1, partida en trossos iguals. On va el 3/4? Comptant 3 trossos de 4 des del 0. Així l'infant veu que una fracció també és un nombre, no només un tros de pizza.</p>

<h2>5. Fraccions i decimals</h2>
<p>A 5è i 6è es relacionen amb els decimals i els percentatges: 1/2 = 0,5 = 50 %, 1/4 = 0,25 = 25 %. Els diners són un bon exemple: mig euro són 50 cèntims.</p>

<h2>6. Errors típics</h2>
<ul>
  <li><b>Pensar que 1/8 és més gran que 1/4</b>: torneu a les pizzes.</li>
  <li><b>Sumar dalt i baix</b> (1/2 + 1/4 = 2/6): primer cal que els trossos siguin de la mateixa mida.</li>
  <li><b>Trossos que no són iguals</b>: una fracció només té sentit si totes les parts són iguals.</li>
</ul>
'''),
 dict(slug='ajudar-amb-les-mates-a-casa', title='Com ajudar el teu fill o la teva filla amb les mates a casa (sense discussions)',
  short='Ajudar amb les mates a casa',
  desc="Consells per a famílies de primària: com acompanyar els infants amb les matemàtiques a casa, què fer quan s'equivoquen i com fer que hi agafin gust.",
  cursos='1r a 6è de primària',
  body='''
<p>No cal ser bo en mates per ajudar un fill o una filla amb les mates. El que més influeix és com acompanyem: la paciència, com reaccionem als errors i fer que les matemàtiques apareguin en la vida de cada dia.</p>

<h2>1. L'error és part d'aprendre</h2>
<p>Quan s'equivoca, el més útil és entendre <b>quin error ha fet</b>, no només dir-li que està malament. Sovint hi ha una lògica: ha confós la suma i la resta, s'ha saltat una desena o ha llegit les agulles del rellotge al revés. Pregunteu-li «com ho has pensat?» abans de corregir.</p>

<h2>2. Millor preguntar que donar la resposta</h2>
<ul>
  <li>«Què et demanen exactament?»</li>
  <li>«Ho podries dibuixar?»</li>
  <li>«Hi ha alguna cosa semblant que ja sàpigues fer?»</li>
  <li>«Té sentit aquest resultat?» (si compres dues coses de 3 €, no et poden tornar 15 € de canvi).</li>
</ul>

<h2>3. Mates de cada dia</h2>
<ul>
  <li><b>A la compra</b>: quant costa en total, quant ens tornaran, què surt més a compte.</li>
  <li><b>A la cuina</b>: mesures, meitats i quarts, el temps de cocció.</li>
  <li><b>Al cotxe</b>: quants quilòmetres falten, a quina hora arribarem.</li>
  <li><b>Jocs de taula</b>: daus, cartes i jocs de comptar treballen el càlcul mental sense que ho semblin.</li>
</ul>

<h2>4. Poca estona i sovint</h2>
<p>Deu minuts tranquils cada dia són més útils que una hora llarga i tensa. Si és un mal moment (cansament, enuig), val més parar i tornar-hi un altre moment.</p>

<h2>5. Compte amb les frases que fan mal</h2>
<p>Frases com «jo tampoc no era bo en mates» o «això és molt fàcil» poden fer pensar a l'infant que no hi ha res a fer o que el problema és seu. Millor valorar l'esforç: «ho has intentat de dues maneres, molt bé».</p>

<h2>6. Pantalles, sí, però amb criteri</h2>
<p>Un joc educatiu pot ajudar si s'adapta al nivell de l'infant, li explica els errors i no està ple d'anuncis o de premis que el fan jugar per jugar. Posar un límit de temps i parlar-ne amb l'infant, del que ha après, el fa més útil.</p>
'''),
]

HEAD = '''<!doctype html>
<html lang="ca">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} · Nits de Misteri</title>
<meta name="description" content="{desc}">
<meta name="theme-color" content="#0d1526">
<link rel="canonical" href="https://nitsdemisteri.cat/{path}">
<meta property="og:type" content="{ogtype}">
<meta property="og:site_name" content="Nits de Misteri">
<meta property="og:locale" content="ca_ES">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="https://nitsdemisteri.cat/{path}">
<meta property="og:image" content="https://nitsdemisteri.cat/img/og-icona.jpg">
<meta name="twitter:card" content="summary">
<link rel="icon" href="/favicon.png" type="image/png">
<link rel="icon" href="/img/icona.svg" type="image/svg+xml">
<link rel="stylesheet" href="/site.css">
<script src="/consent.js" defer></script>
{ld}
</head>
<body>
<header class="top"><div class="wrap"><a class="brand" href="/"><img src="/img/icona-192.png" alt="" width="36" height="36">Nits de Misteri</a><nav aria-label="Seccions"><a href="/#com-funciona">Com funciona</a><a href="/reptes/">Els reptes</a><a href="/guies/">Guies</a><a href="/#preguntes">Preguntes</a></nav></div></header>
<main class="doc">
'''
FOOT = '''</main>
<footer><div class="wrap"><span>© 2026 Carme Pineda · Nits de Misteri</span><nav aria-label="Informació legal"><a href="/reptes/">Els reptes</a><a href="/guies/">Guies</a><a href="/privacitat/">Privacitat</a><a href="/galetes/">Galetes</a><a href="/avis-legal/">Avís legal</a></nav></div></footer>
</body>
</html>
'''
CTA = '''<aside class="cta-box">
<h2>Practicar-ho jugant</h2>
<p>A <b>Nits de Misteri</b>, cada nit hi ha un enigma de mates en català, de 1r a 6è. Si l'infant s'equivoca, el joc li explica quin error ha fet i, si es repeteix, li ensenya un truc amb dibuixos. Sense anuncis.</p>
<p><a href="/">Coneix el joc →</a></p>
</aside>
'''

for g in GUIES:
    path = f"guies/{g['slug']}/"
    ld = {"@context": "https://schema.org", "@type": "Article", "headline": g['title'], "description": g['desc'], "inLanguage": "ca",
          "datePublished": DATE, "dateModified": DATE, "author": {"@type": "Person", "name": "Carme Pineda"},
          "publisher": {"@type": "Person", "name": "Carme Pineda"}, "image": "https://nitsdemisteri.cat/img/og-icona.jpg",
          "mainEntityOfPage": f"https://nitsdemisteri.cat/{path}"}
    crumbs = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Inici", "item": "https://nitsdemisteri.cat/"},
        {"@type": "ListItem", "position": 2, "name": "Guies", "item": "https://nitsdemisteri.cat/guies/"},
        {"@type": "ListItem", "position": 3, "name": g['short'], "item": f"https://nitsdemisteri.cat/{path}"}]}
    ldtxt = f'<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>\n<script type="application/ld+json">{json.dumps(crumbs, ensure_ascii=False)}</script>'
    out = HEAD.format(title=html.escape(g['title']), desc=html.escape(g['desc']), path=path, ogtype='article', ld=ldtxt)
    out += f'''<nav class="crumbs" aria-label="Ruta"><a href="/">Inici</a> › <a href="/guies/">Guies</a> › {g['short']}</nav>
<article>
<h1>{g['title']}</h1>
<p class="small">Per a: {g['cursos']} · Actualitzat el 12 de novembre de 2026</p>
{g['body'].strip()}
</article>
{CTA}'''
    others = [o for o in GUIES if o is not g]
    out += '<nav class="more" aria-label="Altres guies"><h2>Altres guies</h2><ul>' + ''.join(f'<li><a href="/guies/{o["slug"]}/">{o["title"]}</a></li>' for o in others) + '</ul></nav>\n'
    out += FOOT
    os.makedirs(f"{ROOT}/{path}", exist_ok=True)
    open(f"{ROOT}/{path}index.html", 'w').write(out)

# Índex
path = 'guies/'
ldtxt = '<script type="application/ld+json">' + json.dumps({"@context": "https://schema.org", "@type": "CollectionPage", "name": "Guies de mates per a famílies", "inLanguage": "ca", "url": "https://nitsdemisteri.cat/guies/"}, ensure_ascii=False) + '</script>'
out = HEAD.format(title='Guies de mates per a famílies de primària', desc="Guies breus en català per ajudar els infants de primària amb les matemàtiques: taules de multiplicar, rellotge, fraccions i com acompanyar-los a casa.", path=path, ogtype='website', ld=ldtxt)
out += '''<nav class="crumbs" aria-label="Ruta"><a href="/">Inici</a> › Guies</nav>
<h1>Guies de mates per a famílies</h1>
<p>Consells pràctics, en català, per acompanyar els infants de primària amb les matemàtiques a casa.</p>
<div class="guides">''' + ''.join(f'''
<a class="guide" href="/guies/{g['slug']}/"><span class="g-k">{g['cursos']}</span><h2>{g['title']}</h2><p>{g['desc']}</p></a>''' for g in GUIES) + '''
</div>
''' + FOOT
os.makedirs(f"{ROOT}/{path}", exist_ok=True)
open(f"{ROOT}/{path}index.html", 'w').write(out)

# Sitemap
urls = ['', 'guies/'] + [f"guies/{g['slug']}/" for g in GUIES] + ['privacitat/', 'galetes/']
sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + ''.join(f'  <url><loc>https://nitsdemisteri.cat/{u}</loc><lastmod>{DATE}</lastmod></url>\n' for u in urls) + '</urlset>\n'
open(f"{ROOT}/sitemap.xml", 'w').write(sm)
print('ok', len(GUIES))

# ---------- Els reptes del joc ----------
REPTES = [
 ('Enigma', 'Resoldre un problema amb història.', "L'infant llegeix una situació (al mercat, al bosc, al castell…) i tria la resposta correcta entre diverses opcions.", "Comprensió lectora de problemes, triar l'operació adequada i càlcul. És el repte que més s'acosta als problemes de l'escola.", '1r a 6è'),
 ('Mans a la feina', 'Resoldre un repte manipulant, no triant.', "Pagar el preu just posant monedes i bitllets al moneder, plantar una bandera a la recta numèrica, repartir coses en cistells o construir un nombre amb plaques, barres i cubets.", "Diners, valor de posició (unitats, desenes, centenes), divisió com a repartiment i situar nombres, fraccions i decimals a la recta.", '1r a 6è'),
 ('Càlcul ràpid', 'Encertar una operació abans que s’apagui la foguera.', "Apareix una operació i l'infant escriu el resultat amb el teclat. Al panell d'adults es pot treure el temps.", "Càlcul mental i agilitat amb sumes, restes, multiplicacions i divisions, segons el curs.", '1r a 6è'),
 ('El pont trencat', 'Ordenar els taulons per poder creuar el riu.', "Cada tauló porta un nombre i s'han de col·locar de més petit a més gran (o al revés, segons diu el repte).", "Comparar i ordenar nombres naturals, decimals i fraccions.", '1r a 6è'),
 ('La balança', 'Deixar la balança equilibrada.', "A un plat hi ha un pes; l'infant tria pesos per a l'altre plat fins que pesen igual.", "Descompondre nombres i la idea d'igualtat, la base de l'àlgebra.", '1r a 6è'),
 ('El rellotge de la torre', "Posar l'hora que demana el repte.", "L'infant mou les agulles del rellotge fins a l'hora indicada.", "Llegir l'hora en rellotge d'agulles: en punt, i mitja, quarts i minuts, segons el curs.", '1r a 6è'),
 ('Les petjades', "Descobrir quin nombre falta a la sèrie.", "Hi ha una fila de petjades amb nombres que segueixen una regla, i una està esborrada.", "Trobar regularitats i patrons: el pensament algebraic.", '1r a 6è'),
 ('El reflex màgic', "Dibuixar el reflex al mirall.", "Mitja figura està pintada; l'infant pinta l'altra meitat de manera que quedi simètrica respecte de la línia del mig.", "Simetria i orientació espacial.", '1r a 6è'),
 ('El sac de gemmes', "Endevinar què pot sortir del sac.", "L'infant mira quines gemmes hi ha dins el sac i decideix si una de concreta sortirà segur, és possible o és impossible.", "Les primeres idees de probabilitat i el vocabulari de l'atzar.", '1r a 6è'),
 ("L'escut màgic", "Encendre la part de l'escut que demana l'encanteri.", "L'escut està partit en trossos iguals i l'infant n'encén els que toca: la meitat a 1r i 2n, i una fracció a partir de 3r.", "Entendre la meitat i les fraccions com a parts iguals d'un tot.", '1r a 6è'),
 ("Troba l'impostor", "Trobar la pedra que diu una mentida.", "Hi ha diverses pedres amb operacions resoltes; totes són certes menys una.", "Revisar càlculs i detectar errors: un hàbit molt útil per als deures i els exàmens.", '1r a 6è'),
 ('El gran enigma', "Resoldre un problema de diversos passos.", "Un problema més llarg que es pot fer de cop o pas a pas, amb ajuda per a cada pas si cal.", "Planificar la resolució d'un problema, organitzar les dades i encadenar operacions.", '4t a 6è'),
]
path = 'reptes/'
ld = {"@context": "https://schema.org", "@type": "WebPage", "name": "Els reptes de Nits de Misteri", "inLanguage": "ca", "url": "https://nitsdemisteri.cat/reptes/"}
out = HEAD.format(title='Els reptes del joc: objectiu, com es juga i per a què serveix', desc="Els 12 tipus de repte de Nits de Misteri, el joc de mates en català per a primària: què ha d'aconseguir l'infant, com es juga i quina part de les matemàtiques treballa.", path=path, ogtype='website', ld='<script type="application/ld+json">' + json.dumps(ld, ensure_ascii=False) + '</script>')
out += '''<nav class="crumbs" aria-label="Ruta"><a href="/">Inici</a> › Els reptes</nav>
<h1>Els reptes del joc</h1>
<p>Cada nit de l'aventura porta un repte de mates. N'hi ha de 12 tipus i tots s'adapten al curs i al nivell de cada infant. Aquí tens què ha d'aconseguir en cadascun, com es juga i per a què serveix.</p>
<div class="reptes">''' + ''.join(f'''
<section class="repte"><h2>{html.escape(n)}</h2><p class="g-k">{c}</p>
<dl><dt>Objectiu</dt><dd>{html.escape(o)}</dd><dt>Com es juga</dt><dd>{html.escape(h)}</dd><dt>Per a què serveix</dt><dd>{html.escape(s)}</dd></dl></section>''' for n, o, h, s, c in REPTES) + '''
</div>
<p>A més, cada aventura té <b>nits de repte</b> (tres enigmes seguits per guanyar la peça) i, al final, una <b>ràfega de la lluna</b> opcional amb càlculs ràpids.</p>
''' + CTA + FOOT
os.makedirs(f"{ROOT}/{path}", exist_ok=True)
open(f"{ROOT}/{path}index.html", 'w').write(out)
urls.insert(1, 'reptes/')
sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + ''.join(f'  <url><loc>https://nitsdemisteri.cat/{u}</loc><lastmod>{DATE}</lastmod></url>\n' for u in urls) + '</urlset>\n'
open(f"{ROOT}/sitemap.xml", 'w').write(sm)
print('reptes ok')
