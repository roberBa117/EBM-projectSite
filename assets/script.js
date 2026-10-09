/* EBM Dental — comportamiento compartido (IIFE, sin módulos). */
(function () {
	'use strict';
	var WA_NUMBER = '34912345678';
	function safe(fn) { try { fn(); } catch (e) { if (window.console) console.warn(e); } }
	var $ = function (s, r) { return (r || document).querySelector(s); };
	var $$ = function (s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); };

	safe(function header() {
		var h = $('.hd'); if (!h) return;
		var f = function () { h.classList.toggle('sc', window.scrollY > 8); };
		f(); window.addEventListener('scroll', f, { passive: true });
	});

	safe(function menu() {
		var b = $('#menuBtn'), d = $('#drawer'); if (!b || !d) return;
		var ic = $('.icon', b);
		function set(o) {
			d.classList.toggle('open', o); b.setAttribute('aria-expanded', String(o));
			ic.textContent = o ? 'close' : 'menu'; document.body.style.overflow = o ? 'hidden' : '';
		}
		b.addEventListener('click', function () { set(!d.classList.contains('open')); });
		$$('a', d).forEach(function (a) { a.addEventListener('click', function () { set(false); }); });
		window.addEventListener('keydown', function (e) { if (e.key === 'Escape') set(false); });
	});

	safe(function split() {
		var i = 0;
		function walk(node) {
			Array.prototype.slice.call(node.childNodes).forEach(function (n) {
				if (n.nodeType === 3) {
					var frag = document.createDocumentFragment();
					n.textContent.split(/(\s+)/).forEach(function (t) {
						if (!t) return;
						if (/^\s+$/.test(t)) { frag.appendChild(document.createTextNode(' ')); return; }
						var w = document.createElement('span'); w.className = 'w';
						var s = document.createElement('span'); s.textContent = t; s.style.setProperty('--i', i++);
						w.appendChild(s); frag.appendChild(w);
					});
					node.replaceChild(frag, n);
				} else if (n.nodeType === 1) { walk(n); }
			});
		}
		$$('[data-split]').forEach(function (el) { i = 0; walk(el); el.classList.add('is-split'); });
	});

	safe(function reveal() {
		var els = $$('.reveal, [data-split]');
		var show = function (e) { e.classList.add('in'); };
		if (!('IntersectionObserver' in window)) { els.forEach(show); return; }
		var io = new IntersectionObserver(function (en) {
			en.forEach(function (x) { if (x.isIntersecting) { show(x.target); io.unobserve(x.target); } });
		}, { threshold: 0.05, rootMargin: '0px 0px -30px 0px' });
		els.forEach(function (e) { io.observe(e); });
		setTimeout(function () { els.forEach(show); }, 6000); // red de seguridad
	});

	safe(function counters() {
		var els = $$('[data-count]'); if (!els.length) return;
		function run(el) {
			var to = parseFloat(el.getAttribute('data-count')), dec = (String(to).split('.')[1] || '').length;
			var suf = el.getAttribute('data-suffix') || '', t0 = null, dur = 1600;
			function tick(t) {
				if (!t0) t0 = t; var p = Math.min((t - t0) / dur, 1), e = 1 - Math.pow(1 - p, 4);
				el.textContent = (to * e).toFixed(dec) + suf; if (p < 1) requestAnimationFrame(tick);
			}
			requestAnimationFrame(tick);
		}
		if (!('IntersectionObserver' in window)) return;
		var io = new IntersectionObserver(function (en) {
			en.forEach(function (x) { if (x.isIntersecting) { run(x.target); io.unobserve(x.target); } });
		}, { threshold: 0.3 });
		els.forEach(function (e) { io.observe(e); });
	});

	safe(function parallax() {
		var art = $('.art'); if (!art || !window.matchMedia('(hover:hover)').matches) return;
		var balls = $$('.ball', art);
		window.addEventListener('mousemove', function (e) {
			var x = (e.clientX / window.innerWidth - .5), y = (e.clientY / window.innerHeight - .5);
			balls.forEach(function (b, i) {
				var k = (i + 1) * 14; b.style.transform = 'translate(' + (x * k) + 'px,' + (y * k) + 'px)';
			});
		}, { passive: true });
	});

	safe(function filter() {
		var bs = $$('[data-filter]'), cs = $$('[data-cat]'); if (!bs.length) return;
		bs.forEach(function (b) {
			b.addEventListener('click', function () {
				bs.forEach(function (x) { x.setAttribute('aria-pressed', 'false'); });
				b.setAttribute('aria-pressed', 'true');
				var v = b.getAttribute('data-filter');
				cs.forEach(function (c) {
					var ok = v === 'todos' || c.getAttribute('data-cat') === v;
					c.style.display = ok ? '' : 'none';
					if (ok) { c.classList.remove('in'); void c.offsetWidth; c.classList.add('in'); }
				});
			});
		});
	});

	safe(function form() {
		var f = $('#contactForm'); if (!f) return;
		var qs = new URLSearchParams(window.location.search).get('service');
		var sel = $('#service');
		if (qs && sel && $$('option', sel).some(function (o) { return o.value === qs; })) sel.value = qs;

		f.addEventListener('submit', function (e) {
			e.preventDefault();
			var ok = true;
			$$('[required]', f).forEach(function (i) {
				var fld = i.closest('.field'), good = i.value.trim().length > 0;
				fld.classList.toggle('bad', !good); if (!good) ok = false;
			});
			if (!ok) { var b = $('.bad .inp', f); if (b) b.focus(); return; }

			var txt = sel.options[sel.selectedIndex].text;
			var email = $('#email').value.trim(), notes = $('#notes').value.trim();
			var msg = 'Hola, me gustaría solicitar una cita en EBM Dental.\n\n' +
				'*Nombre:* ' + $('#fullName').value.trim() + '\n' +
				'*Teléfono:* ' + $('#phone').value.trim() + '\n' +
				(email ? '*Correo:* ' + email + '\n' : '') +
				'*Servicio de interés:* ' + txt + '\n' +
				(notes ? '*Notas:* ' + notes + '\n' : '') + '\nGracias.';
			var url = 'https://wa.me/' + WA_NUMBER + '?text=' + encodeURIComponent(msg);
			$('#waLink').setAttribute('href', url);
			window.open(url, '_blank', 'noopener');
			f.hidden = true; var s = $('#success'); s.hidden = false; s.focus();
		});

		window.resetForm = function () {
			f.reset(); $$('.bad', f).forEach(function (x) { x.classList.remove('bad'); });
			$('#success').hidden = true; f.hidden = false;
		};
	});
})();
