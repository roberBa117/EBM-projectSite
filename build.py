# -*- coding: utf-8 -*-
import os
P = "https://lh3.googleusercontent.com/aida-public/"
IMG = {
 "logo": "assets/logo.png",
 "hero": P+"AB6AXuDxw5HojLv9qyta4Maou7BOgzqW4ud_5tdW9_CnpTmFq3OQkX-bcpnheYVWhgUTtjD6yjZce3Veob4veiWDNncvQ2OczSSRFS5-wmlDm-zBHvuNo1OddVfDn_rSpJDA1LuWIqgMM6_jj-oHw0c8LqwaicTobsA1TZw2D50aWs375DdSJhBt4GO4JMjdZYXAQNxm5BgeQG-We7SssyPOiaxKVqlSg9WIAAdtRO4mkeeLo1Vo8C9cYb4VHw",
 "gen": P+"AB6AXuA-bbKr31bzPtn24_tlm0J7lq4FuHURTt_yiq3SgW5auxa0nVijqVsrn9MpaYKL4ckmmBa3q40blUCacKrPCuHOOCbBzKDGd_hYIkcJC12iuf9S_us7SqIRB32g_5M3N9fxCvJacyENQP7gEPcs_a1aaHkV3LuPqum6jA2LlDS6JnHYeCpB8wEF8fTJLrR1kB2VVk5HcwmHf7kC_zTMbqQjwj55TToVILWpH_lZHx_jGayFX0dRFOdRqg",
 "aes": P+"AB6AXuDyjdFywKwG84QhK_VXdg4ogNwu6kerytfXz43z5KVEKTLEq2eyMUemYlcNFTUqwYoNUhGUHmiMTw-0Vq02GGUU5v5WZrqnBlMgASMk0iYQBN58yDUskTux5O09p4IrCcFTA3MM-0ISRtKPr3gTMZo_DTidmQKYA7RkUv_3zRL3nf8OhdETjLitUpewC42_X5rsBgvZ0PKjSCOyzGZWBkB3t7Pya40Shs_AlR71x9kxqTkuK9HVOFrmEQ",
 "imp": P+"AB6AXuBd9as4HCoy2hg9Hqjx19T41YJgfZDDb97btvvrNycGsdO_VIYnjNxhg7cxqbHa8oAJ6UGUJhzWbgBkjyL1mV14auU4EwD3F0i_v11YTKRXndx3_bmk3OtxBQM0y393DEChYfab2urvHq0yozdQO_PSXal_PgFDwbqSSj5Lhkx9QhfwT12cLq6d5BJDTJ0ly35iJhiBXRicnlv62MLfMGyurVQZ-JZ91gFu2llUsjHbvLfKsC6j6ZoLVw",
 "ort": P+"AB6AXuBGXAJUXuMiTGznFjzyi4wC5LJHjXhqeUKyV1XALuRfcZdB_l1f5Q0dtTltpqscpp2I6LZDSqxT1i6W57AUZ2iZ3kbiDOuADNxSZGW5rjVS6U4Y0A4r3mIqFA5y5SJFo1ptH6CnQN58q7Ga8AmK7hQvXt8cG4ptB8E954bU9bALehoQ_SFk0J5aX0cK5QXYT6_2DauVIq3xzetIJaGVJ67OEviPP-ayhH1PoOeKBSEBa-QxCdryPo0AvQ",
 "doc": P+"AB6AXuCk5YTjwRH1Wbzplk-xlchagn6YO80Xd67rEeuksRO6OFvGOuLB0xBOL463aX_tkL5AohTDmSs_xjpe5pCSXvZtikCHsJ7TxQYzyIe2KZ3WtSeU3gCIaPJvcJaaXde_MSfp_x19YAaAshWAjdAA19QdfbFYqjIXk-J2Ay1LbVWBOAoRZ34HAyO1_BgOP7UVEvhWQMZiBTMXCoSa__WgpSNRgN1upC_AIO4al391YQF3O2tv6wi5Nb--rA",
 "wait": P+"AB6AXuBCYuzh9fbgruyUnTn93HcaLtnFVBxdxhItA9bK98x66HK9RSRNBj-Vh49E5Dfk_WQnyDLcLIPsAeYdBU0wihLxw553AQ52EXsynhpDHCOKFf9p8B-IXoNESv7jwzfHi8rSFEnRA7K-g57LWrsYyWj2PdNEUECXZ2enRd1bfxy-dIOh0liSF8j-2zNiNxP7jtNXtZ-BMK6TrYPejpwMQbBrAyIForm1DtEBTYTFEjdEFFOrH4RcblF4dsy2BuoWQ5ENnlo",
}
TEL = "+34 912 345 678"; TELH = "tel:+34912345678"; MAIL = "info@ebmdental.com"
MAPS = "https://www.google.com/maps/search/?api=1&query=Calle+de+la+Cl%C3%ADnica+123%2C+28001+Madrid"
V = "?v=20260923"
PAGES = [("index.html", "Inicio"), ("servicios.html", "Servicios"), ("casos-de-exito.html", "Casos de éxito"), ("contacto.html", "Contacto")]

def ball(c, w, style):
    return f'<div class="ball" style="background:{c};width:{w};height:{w};{style}" aria-hidden="true"></div>'

def shell(fn, title, desc, body):
    nav = "".join(f'<a href="{h}"' + (' aria-current="page"' if h == fn else '') + f'>{t}</a>' for h, t in PAGES)
    dr = "".join(f'<a class="l" href="{h}">{t}</a>' for h, t in PAGES)
    return f'''<!DOCTYPE html>
<html lang="es"><head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>{title}</title><meta name="description" content="{desc}">
<meta name="theme-color" content="#1a73e8">
<script>document.documentElement.classList.add('js')</script>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Sora:wght@400;600;700;800&family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">
<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@24,400,0,0" rel="stylesheet">
<link rel="icon" href="{IMG['logo']}"><link rel="stylesheet" href="assets/styles.css{V}">
</head><body>
<a class="skip" href="#main">Saltar al contenido</a>
<header class="hd"><div class="hd-bar">
<a class="brand" href="index.html" aria-label="EBM Dental, inicio"><img src="{IMG['logo']}" alt="EBM Dental Odontología Integral"></a>
<nav class="nav" aria-label="Principal">{nav}</nav>
<div class="hd-act"><a class="btn btn-o btn-s hd-cta" href="contacto.html">Pedir cita <span class="icon" aria-hidden="true">arrow_outward</span></a>
<button class="menu-b" id="menuBtn" type="button" aria-expanded="false" aria-controls="drawer" aria-label="Abrir menú"><span class="icon" aria-hidden="true">menu</span></button></div>
</div></header>
<div class="drawer" id="drawer">{dr}
<a class="btn btn-o btn-b" style="margin-top:2rem" href="contacto.html">Pedir cita</a>
<div class="dot-row" aria-hidden="true"><i style="background:#fff"></i><i style="background:var(--wine)"></i><i style="background:var(--green)"></i><i style="background:var(--orange)"></i></div></div>
<main id="main">{body}</main>
<footer class="ft"><div class="wrap">
<p class="ft-big" aria-hidden="true">EBM DENTAL</p>
<div class="fg">
<div><img src="{IMG['logo']}" alt="EBM Dental" style="height:2.6rem;margin-bottom:1rem"><p class="muted" style="max-width:34ch">Odontología integral con tecnología de vanguardia y un equipo que te cuida de verdad.</p></div>
<div><h4>Contacto</h4>
<p class="r"><span class="icon" aria-hidden="true">location_on</span>Calle de la Clínica 123, 28001 Madrid, España</p>
<a class="r" href="{TELH}"><span class="icon" aria-hidden="true">call</span>{TEL}</a>
<a class="r" href="mailto:{MAIL}"><span class="icon" aria-hidden="true">mail</span>{MAIL}</a></div>
<div><h4>Horario</h4><p class="muted" style="font-size:.92rem">Lunes a viernes: 09:00–14:00 y 15:00–19:00<br>Sábados: 09:00–14:00<br>Urgencias: 24/7</p>
<a class="kicker" style="margin-top:1rem" href="{MAPS}" target="_blank" rel="noopener noreferrer">Cómo llegar <span class="icon" aria-hidden="true">north_east</span></a></div>
</div>
<div class="fb"><span>© 2026 EBM Dental. Todos los derechos reservados.</span><span><a href="#">Aviso legal</a> · <a href="#">Privacidad</a></span></div>
</div></footer>
<nav class="mbar" aria-label="Acciones rápidas">
<a href="{TELH}"><span class="icon" aria-hidden="true">call</span>Llamar</a>
<a class="w" href="https://wa.me/34912345678" target="_blank" rel="noopener noreferrer"><span class="icon" aria-hidden="true">chat</span>WhatsApp</a>
<a class="p" href="contacto.html"><span class="icon" aria-hidden="true">calendar_month</span>Pedir cita</a></nav>
<script src="assets/script.js{V}" defer></script>
</body></html>'''

def cta(h, p, btn="Pedir cita"):
    return f'''<section class="wrap" style="padding-top:var(--gap)"><div class="cta reveal">
{ball("#ffffff22","22rem","top:-8rem;right:-6rem")}{ball("#f57c0055","14rem","bottom:-6rem;left:30%")}
<div><h2 class="d2">{h}</h2><p style="opacity:.9;margin-top:.8rem;max-width:44ch">{p}</p></div>
<div class="btn-row"><a class="btn btn-w" href="contacto.html">{btn} <span class="icon" aria-hidden="true">arrow_outward</span></a>
<a class="btn" style="border:1.5px solid #fff8;color:#fff" href="{TELH}"><span class="icon" aria-hidden="true">call</span>{TEL}</a></div></div></section>'''

def case(cat, chip, tone, img, alt, title, txt, dur, svc, d=0):
    return f'''<article class="reveal case" data-cat="{cat}" style="--d:{d}s"><div class="im"><img src="{img}" alt="{alt}" loading="lazy"></div>
<div class="bd"><span class="chip {tone}">{chip}</span><h3 class="d3">{title}</h3><p>{txt}</p>
<div class="meta"><span class="icon" aria-hidden="true" style="font-size:1rem">schedule</span>Duración: {dur}</div>
<a class="lk" href="contacto.html?service={svc}">Quiero un caso así <span class="icon" aria-hidden="true">arrow_forward</span></a></div></article>'''

# ---------------- INICIO ----------------
def tile(cls, span, ico, h, p, svc, img=None):
    im = f'<img src="{img}" alt="" loading="lazy">' if img else ''
    ph = ' ph' if img else ''
    return f'''<a class="reveal tile {cls}{ph} {span}" href="contacto.html?service={svc}">{im}<span class="go" aria-hidden="true"><span class="icon" style="color:var(--ink);font-size:1.3rem">arrow_forward</span></span>
<span class="icon" aria-hidden="true">{ico}</span><div><h3 class="d3">{h}</h3><p>{p}</p></div></a>'''

def ticker():
    items = [("Odontología general","#f57c00"),("Ortodoncia","#2e7d32"),("Implantes","#8ab8ff"),("Estética dental","#f0a3ae"),("Prótesis","#f57c00"),("Urgencias 24/7","#7fdc84")]
    row = "".join(f'<span style="--c:{c}">{t}</span>' for t, c in items)
    return f'<div class="mq" aria-hidden="true"><div class="mq-t">{row*2}{row*2}</div></div>'

index = f'''
<section class="hero">
{ball("var(--blue-t)","34rem","top:-12rem;left:-10rem;position:absolute;filter:blur(20px);opacity:.8")}
<div class="wrap hero-g">
<div class="stack">
<span class="pill"><i></i>Odontología integral · Madrid</span>
<h1 class="d1" data-split>Diseñamos sonrisas que te devuelven la <mark>confianza</mark> de mirar de frente.</h1>
<p class="lede reveal" style="--d:.3s">Tecnología de última generación con un trato cercano y humano. Evaluamos tu salud bucal en conjunto para tratamientos duraderos, estéticos y sin sorpresas.</p>
<div class="btn-row reveal" style="--d:.4s"><a class="btn btn-o" href="contacto.html">Pedir cita <span class="icon" aria-hidden="true">arrow_outward</span></a><a class="btn btn-g" href="{TELH}"><span class="icon" aria-hidden="true" style="color:var(--blue)">call</span>Llamar ahora</a></div>
<div class="proof reveal" style="--d:.5s"><div class="faces" aria-hidden="true"><i style="background:var(--blue)">A</i><i style="background:var(--green)">M</i><i style="background:var(--orange)">L</i><i style="background:var(--wine)">+</i></div><p><b>20k+ sonrisas</b> transformadas · 4.9/5 de valoración</p></div>
</div>
<div class="art reveal" style="--d:.15s">
{ball("var(--wine)","46%","top:0;left:-2%")}{ball("var(--green)","38%","bottom:8%;left:-8%")}{ball("var(--orange)","34%","top:14%;right:-6%")}
<div class="arch"><img src="{IMG['hero']}" alt="Recepción luminosa y moderna de EBM Dental"></div>
<div class="chipf fl" style="left:-4%;bottom:-2%"><span class="ico g"><span class="icon" aria-hidden="true">verified</span></span><span><b>25+ años</b>de experiencia clínica</span></div>
<div class="chipf fl2" style="right:-2%;bottom:24%"><span class="ico r"><span class="icon" aria-hidden="true">emergency</span></span><span><b>24/7</b>urgencias dentales</span></div>
</div></div></section>
{ticker()}

<section class="sec"><div class="wrap">
<div class="reveal" style="max-width:40rem;margin-bottom:3rem"><span class="kicker">Especialidades</span><h2 class="d2" style="margin-top:.6rem">Todo lo que tu sonrisa necesita, <mark class="g">bajo un mismo techo.</mark></h2></div>
<div class="bento">
{tile("blue","s3 r2","medical_services","Odontología general","Revisiones, limpiezas profundas y empastes para mantener tu salud dental al día, sin dolor y sin prisas.","limpieza",IMG["gen"])}
{tile("orange","s3","mood","Ortodoncia","Brackets ligeros y alineadores casi invisibles.","ortodoncia")}
{tile("green","s3","hardware","Implantes dentales","Titanio biocompatible y carga inmediata.","implantes")}
{tile("wine","s2","auto_awesome","Estética dental","Carillas, diseño de sonrisa y blanqueamiento.","blanqueamiento")}
{tile("sky","s2","precision_manufacturing","Prótesis dental","Fijas y removibles, hechas a medida.","otro")}
{tile("red","s2","emergency","Urgencias 24/7","Atención prioritaria cuando más la necesitas.","urgencia")}
</div>
<div class="reveal" style="margin-top:2rem"><a class="kicker" href="servicios.html">Ver todos los servicios <span class="icon" aria-hidden="true">arrow_forward</span></a></div>
</div></section>

<section class="dark sec"><div class="wrap">
{ball("#1a73e844","26rem","top:-10rem;right:-8rem;position:absolute")}{ball("#f57c0033","20rem","bottom:-9rem;left:-6rem;position:absolute")}
<div style="position:relative">
<div class="reveal" style="max-width:40rem"><span class="kicker" style="color:#ffb15c">Nuestros logros</span><h2 class="d2" style="margin-top:.6rem">Resultados que <mark>hablan solos.</mark></h2></div>
<div class="stats">
<div class="reveal stat"><b data-count="25" data-suffix="+">25+</b><span>años de experiencia</span></div>
<div class="reveal stat" style="--d:.08s"><b data-count="20" data-suffix="k+">20k+</b><span>sonrisas transformadas</span></div>
<div class="reveal stat" style="--d:.16s"><b data-count="99" data-suffix="%">99%</b><span>satisfacción de pacientes</span></div>
<div class="reveal stat" style="--d:.24s"><b data-count="4.9" data-suffix="/5">4.9/5</b><span>valoración media</span></div>
<div class="reveal stat" style="--d:.32s"><b>24/7</b><span>atención de urgencias</span></div>
</div>
<div class="steps">
<div class="reveal step"><div class="n">1</div><h3 class="d3">Valoración gratuita</h3><p>Te escuchamos, revisamos tu boca con radiología digital 3D y resolvemos tus dudas.</p></div>
<div class="reveal step" style="--d:.1s"><div class="n">2</div><h3 class="d3">Plan a tu medida</h3><p>Diseñamos un tratamiento claro, con tiempos y opciones explicadas sin tecnicismos.</p></div>
<div class="reveal step" style="--d:.2s"><div class="n">3</div><h3 class="d3">Tu nueva sonrisa</h3><p>Te acompañamos con sedación consciente si la necesitas y seguimiento después.</p></div>
</div></div></div></section>

<section class="sec"><div class="wrap">
<div class="reveal" style="max-width:40rem;margin-bottom:3rem"><span class="kicker">Casos de éxito</span><h2 class="d2" style="margin-top:.6rem">Sonrisas reales, <mark class="b">cambios reales.</mark></h2></div>
<div class="cases">
{case("carillas","Estética dental","w",IMG["aes"],"Sonrisa tras rehabilitación estética completa","Rehabilitación estética completa","Diseño de sonrisa con 10 carillas de porcelana de alta estética.","3 semanas","blanqueamiento")}
{case("implantologia","Implantología","g",IMG["imp"],"Antes y después de un implante dental","Implante de carga inmediata","Función y estética recuperadas en 24 horas.","1 día","implantes",.08)}
{case("ortodoncia","Ortodoncia","o",IMG["ort"],"Dientes alineados tras ortodoncia","Corrección de alineación severa","Brackets de titanio ligeros para un tratamiento eficiente.","14 meses","ortodoncia",.16)}
</div>
<div class="reveal" style="margin-top:2rem"><a class="kicker" href="casos-de-exito.html">Ver todos los casos <span class="icon" aria-hidden="true">arrow_forward</span></a></div>
</div></section>

<section class="wrap"><div class="doc reveal">
<div class="stack" style="display:grid;gap:1.3rem"><span class="kicker">Dirección médica</span><h2 class="d2">Dr. Erick Bahena Martínez</h2>
<p class="muted">Con más de una década dedicada a la implantología y la estética dental, el Dr. Bahena lidera el equipo de EBM Dental. Su enfoque combina empatía y precisión técnica para que cada paciente reciba el tratamiento que realmente necesita.</p>
<blockquote class="q">“Mi mayor satisfacción es ver cómo un paciente recupera la confianza al sonreír de nuevo.”</blockquote>
<div class="tags"><span class="chip b">Implantología</span><span class="chip w">Estética avanzada</span><span class="chip g">Prótesis dentales</span></div>
<div><a class="btn btn-p" href="contacto.html">Agenda con el Dr. Bahena <span class="icon" aria-hidden="true">arrow_outward</span></a></div></div>
<div class="ph">{ball("var(--orange)","55%","top:-6%;right:-10%")}{ball("var(--green)","40%","bottom:2%;left:-10%")}<img src="{IMG['doc']}" alt="Dr. Erick Bahena Martínez, dirección médica de EBM Dental" loading="lazy"></div>
</div></section>
{cta("¿Empezamos a cuidar tu sonrisa?","Completa el formulario y te contactamos por WhatsApp el mismo día hábil para confirmar tu cita.","Solicitar cita")}
'''

# ---------------- SERVICIOS ----------------
def svc(cls, rev, n, ico, chip, tone, h, p, items, img, key):
    li = "".join(f'<li><span class="icon" aria-hidden="true">check_circle</span><span>{i}</span></li>' for i in items)
    return f'''<article class="reveal svc {cls}{' rev' if rev else ''}"><div class="svc-im"><img src="{img}" alt="{h}" loading="lazy"></div>
<div><div style="display:flex;gap:.8rem;align-items:center"><span class="num">0{n}</span><span class="chip {tone}">{chip}</span></div>
<h2 class="d2" style="font-size:clamp(1.6rem,1.2rem + 1.6vw,2.4rem);margin:.8rem 0"><span class="icon" aria-hidden="true" style="margin-right:.4rem">{ico}</span>{h}</h2>
<p class="muted">{p}</p><ul class="checks" style="margin-top:.8rem">{li}</ul>
<a class="btn btn-p btn-s" style="margin-top:1.4rem" href="contacto.html?service={key}">Pedir cita para esto <span class="icon" aria-hidden="true">arrow_forward</span></a></div></article>'''

faq = [
 ("¿Los tratamientos duelen?","Trabajamos con anestesia moderna y, si lo necesitas, sedación consciente. Nuestro objetivo es que la visita sea tranquila de principio a fin."),
 ("¿Cuánto dura una primera valoración?","Alrededor de 30 a 45 minutos. Revisamos tu boca, hacemos radiología digital si hace falta y te explicamos las opciones."),
 ("¿Atienden urgencias fuera de horario?","Sí. Contamos con atención de urgencias 24/7: llámanos o escríbenos por WhatsApp y te indicamos cómo proceder."),
 ("¿Puedo ver mi sonrisa antes de empezar?","En tratamientos estéticos hacemos un diseño digital previo para que veas el resultado esperado antes de comenzar."),
]
faqh = "".join(f'<details class="faq reveal"><summary>{q}</summary><p>{a}</p></details>' for q, a in faq)

servicios = f'''
<section class="ph-hero">{ball("var(--orange-t)","30rem","top:-10rem;right:-8rem;position:absolute")}{ball("var(--green-t)","18rem","bottom:-6rem;left:-4rem;position:absolute")}
<div class="wrap" style="max-width:52rem"><span class="kicker">Excelencia clínica</span>
<h1 class="d1" style="margin:.7rem 0 1rem" data-split>Servicios dentales <mark class="g">integrales</mark> para toda la familia.</h1>
<p class="lede reveal" style="--d:.3s">Cinco especialidades, un mismo equipo coordinado alrededor de tu caso. Tu sonrisa está en manos expertas.</p>
<div class="btn-row reveal" style="margin-top:1.5rem;--d:.4s"><a class="btn btn-o" href="contacto.html">Agenda tu valoración <span class="icon" aria-hidden="true">arrow_outward</span></a></div></div></section>
<section class="wrap">
{svc("b",0,1,"medical_services","Prevención","b","Odontología general","Cuidado fundamental para mantener una salud bucal óptima: limpiezas profundas, revisiones periódicas y prevención de caries.",["Revisión y diagnóstico completo","Limpieza dental profesional","Obturaciones y prevención de caries"],IMG["gen"],"limpieza")}
{svc("o",1,2,"mood","Estética","o","Ortodoncia","Alinea tu sonrisa de forma discreta, con alineadores cómodos y ligeros o brackets de titanio.",["Alineadores transparentes a medida","Brackets de titanio ligeros","Seguimiento fotográfico del progreso"],IMG["ort"],"ortodoncia")}
{svc("g",0,3,"hardware","Cirugía","g","Implantes dentales","Soluciones fijas y duraderas con implantes de titanio biocompatible de máxima calidad.",["Titanio biocompatible de alta gama","Carga inmediata disponible","Planificación guiada por imagen 3D"],IMG["imp"],"implantes")}
{svc("w",1,4,"auto_awesome","Cosmética","w","Estética dental","Diseñamos tu sonrisa ideal con carillas de porcelana, blanqueamiento y contorneado estético.",["Carillas de porcelana de alta estética","Blanqueamiento profesional supervisado","Diseño de sonrisa digital previo"],IMG["aes"],"blanqueamiento")}
{svc("k",0,5,"precision_manufacturing","Rehabilitación","b","Prótesis dental","Prótesis a medida para recuperar función y estética con un ajuste perfecto y natural.",["Prótesis fijas y removibles","Ajuste a medida en varias citas","Materiales de alta durabilidad"],IMG["wait"],"otro")}
</section>
<section class="sec"><div class="wrap" style="max-width:52rem"><div class="reveal" style="margin-bottom:2rem"><span class="kicker">Preguntas frecuentes</span><h2 class="d2" style="margin-top:.6rem">Lo que casi todos preguntan.</h2></div>{faqh}</div></section>
{cta("¿No sabes qué tratamiento necesitas?","Agenda una valoración gratuita: analizamos tu caso y te recomendamos la mejor opción.","Agendar valoración")}
'''

# ---------------- CASOS ----------------
def fb(v, t, on=False):
    return f'<button type="button" class="fbtn" data-filter="{v}" aria-pressed="{"true" if on else "false"}">{t}</button>'

casos = f'''
<section class="ph-hero">{ball("var(--wine-t)","28rem","top:-9rem;left:-8rem;position:absolute")}{ball("var(--blue-t)","20rem","top:2rem;right:-6rem;position:absolute")}
<div class="wrap" style="max-width:56rem"><span class="kicker"><span class="icon" aria-hidden="true">workspace_premium</span>Resultados reales</span>
<h1 class="d1" style="margin:.7rem 0 1rem" data-split>Transformando sonrisas, <mark>cambiando vidas.</mark></h1>
<p class="lede reveal" style="--d:.3s">Cada sonrisa cuenta una historia de precisión y compromiso con la salud y la estética de nuestros pacientes.</p>
<div style="display:flex;flex-wrap:wrap;gap:1rem 3rem;margin-top:2rem" class="reveal"><div><b class="d2" data-count="25" data-suffix="+">25+</b><p class="muted" style="font-size:.85rem">años de experiencia</p></div><div><b class="d2" data-count="20" data-suffix="k+">20k+</b><p class="muted" style="font-size:.85rem">sonrisas transformadas</p></div><div><b class="d2" data-count="99" data-suffix="%">99%</b><p class="muted" style="font-size:.85rem">satisfacción</p></div></div></div></section>
<section class="wrap"><div class="filters reveal" role="group" aria-label="Filtrar casos por especialidad">{fb("todos","Todos",True)}{fb("implantologia","Implantología")}{fb("ortodoncia","Ortodoncia")}{fb("carillas","Carillas dentales")}</div>
<div class="cases">
{case("carillas","Carillas de porcelana","w",IMG["aes"],"Sonrisa tras rehabilitación estética completa","Rehabilitación estética completa","Transformación integral mediante diseño de sonrisa y 10 carillas de porcelana altamente estéticas.","3 semanas","blanqueamiento")}
{case("implantologia","Implantología avanzada","g",IMG["imp"],"Antes y después de un implante dental","Implante de carga inmediata","Sustitución de una pieza con técnica de carga inmediata: función y estética recuperadas en 24 horas.","1 día","implantes",.08)}
{case("ortodoncia","Ortodoncia","o",IMG["ort"],"Dientes alineados tras ortodoncia","Corrección de alineación severa","Corrección de apiñamiento severo con brackets de titanio ligeros y resistentes.","14 meses","ortodoncia",.16)}
</div></section>
<section class="sec"><div class="wrap reveal" style="max-width:52rem;text-align:center"><span class="icon" aria-hidden="true" style="font-size:3.5rem;color:var(--orange)">format_quote</span>
<p style="font:600 clamp(1.25rem,1rem + 1.2vw,1.9rem)/1.4 var(--f-head);margin:1rem 0">“Nunca pensé que volvería a sonreír con tanta confianza. El equipo de EBM Dental no solo restauró mis dientes, me devolvió la seguridad en mí misma. El proceso fue indoloro y superó mis expectativas.”</p>
<p style="font-weight:700">María G.</p><p class="muted" style="font-size:.9rem">Paciente de rehabilitación completa</p></div></section>
{cta("¿Listo para tu propio caso de éxito?","Reserva una valoración gratuita. Analizaremos tu caso y diseñaremos la sonrisa que siempre has deseado.","Agendar valoración gratuita")}
'''

# ---------------- CONTACTO ----------------
def irow(tone, ico, h, t):
    return f'<div class="inforow"><span class="ico {tone}"><span class="icon" aria-hidden="true">{ico}</span></span><div><h3 class="d3" style="font-size:1.02rem">{h}</h3><p class="muted">{t}</p></div></div>'

def fld(label, ico, inner, err=None, hint=""):
    e = f'<p class="err">{err}</p>' if err else ''
    return f'<div class="field"><label for="{inner[0]}">{label} <span class="hint">{hint}</span></label><div class="iw"><span class="icon" aria-hidden="true">{ico}</span>{inner[1]}</div>{e}</div>'

contacto = f'''
<section class="ph-hero">{ball("var(--blue-t)","30rem","top:-10rem;right:-9rem;position:absolute")}{ball("var(--orange-t)","16rem","bottom:-4rem;left:-3rem;position:absolute")}
<div class="wrap"><div class="cgrid">
<div><span class="kicker">Pedir cita</span>
<h1 class="d1" style="margin:.7rem 0 1rem;font-size:clamp(2.2rem,1.2rem + 3.6vw,4rem)" data-split>Estamos aquí para cuidar <mark>tu sonrisa.</mark></h1>
<p class="lede reveal" style="--d:.3s">Cuéntanos qué necesitas y te escribimos por WhatsApp para confirmar tu primera visita.</p>
<div class="reveal" style="margin-top:2rem">{irow("b","location_on","Ubicación","Calle de la Clínica 123<br>28001 Madrid, España")}{irow("g","call","Teléfono",TEL)}{irow("o","mail","Correo",MAIL)}{irow("w","schedule","Horario","Lun–vie 09:00–14:00 y 15:00–19:00 · Sáb 09:00–14:00")}</div>
<div class="altc reveal"><a href="{TELH}"><span class="ico b"><span class="icon" aria-hidden="true">phone_in_talk</span></span>Llámanos directo</a><a href="https://wa.me/34912345678" target="_blank" rel="noopener noreferrer"><span class="ico g"><span class="icon" aria-hidden="true">chat</span></span>Chat por WhatsApp</a></div>
</div>
<div class="reveal" style="--d:.1s"><div class="panel">
<h2 class="d2" style="font-size:1.7rem;margin-bottom:1.5rem">Solicitar cita</h2>
<form id="contactForm" novalidate>
{fld("Nombre completo","person",("fullName",'<input class="inp" id="fullName" name="fullName" type="text" placeholder="Ej. Ana García" autocomplete="name" required>'),"Escribe tu nombre completo.")}
<div class="grid2">
{fld("Teléfono de contacto","call",("phone",'<input class="inp" id="phone" name="phone" type="tel" placeholder="Ej. 555-123-4567" autocomplete="tel" required>'),"Indica un teléfono de contacto.")}
{fld("Correo electrónico","mail",("email",'<input class="inp" id="email" name="email" type="email" placeholder="ana@ejemplo.com" autocomplete="email">'),None,"(opcional)")}
</div>
{fld("Servicio de interés","medical_services",("service",'<select class="inp" id="service" name="service" required><option disabled selected value="">Selecciona un servicio</option><option value="limpieza">Limpieza dental profesional</option><option value="blanqueamiento">Blanqueamiento</option><option value="ortodoncia">Consulta de ortodoncia</option><option value="implantes">Evaluación para implantes</option><option value="urgencia">Urgencia dental</option><option value="otro">Otro (especificar en notas)</option></select>'),"Selecciona un servicio.")}
<div class="field"><label for="notes">Notas adicionales</label><textarea class="inp" id="notes" name="notes" rows="4" placeholder="¿Hay algún dolor específico o preferencia de horario?"></textarea></div>
<button class="btn btn-o btn-b" type="submit"><span class="icon" aria-hidden="true">chat</span>Enviar solicitud por WhatsApp</button>
<p class="note"><span class="icon" aria-hidden="true" style="font-size:1rem">lock</span>Se abrirá WhatsApp con tus datos listos para enviar. No guardamos tu información.</p>
</form>
<div id="success" class="ok" hidden tabindex="-1" role="status"><div class="bdg"><span class="icon" aria-hidden="true" style="font-size:2.4rem">check_circle</span></div>
<h3 class="d3">¡Casi listo!</h3><p class="muted" style="margin:.6rem 0 1.2rem">Abrimos WhatsApp con tu mensaje. Solo pulsa enviar y el equipo te responderá para confirmar tu cita.</p>
<a id="waLink" class="btn btn-p" href="#" target="_blank" rel="noopener noreferrer">¿No se abrió? Abrir WhatsApp</a>
<div><button type="button" class="btn btn-g" style="margin-top:.8rem" onclick="resetForm()">Enviar otra solicitud</button></div></div>
</div></div></div></div></section>
'''

out = os.path.dirname(os.path.abspath(__file__))
pages = {
 "index.html": ("EBM Dental — Odontología integral en Madrid", "Clínica dental con tecnología de vanguardia y trato cercano: odontología general, ortodoncia, implantes y estética dental en Madrid.", index),
 "servicios.html": ("Servicios — EBM Dental", "Odontología general, ortodoncia, implantes, estética y prótesis dental en EBM Dental, Madrid.", servicios),
 "casos-de-exito.html": ("Casos de éxito — EBM Dental", "Casos reales de implantología, ortodoncia y carillas dentales con resultados duraderos.", casos),
 "contacto.html": ("Pedir cita — EBM Dental", "Solicita tu cita en EBM Dental: completa el formulario y te contactamos por WhatsApp.", contacto),
}
for fn, (t, d, b) in pages.items():
    open(os.path.join(out, fn), "w", encoding="utf-8").write(shell(fn, t, d, b))
print("ok")
