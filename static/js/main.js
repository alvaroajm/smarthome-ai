/* =========================================================================
   SmartHome-AI — JavaScript do site (sem dependências)
   ========================================================================= */
(function () {
  'use strict';

  var doc = document;
  var $ = function (sel, ctx) { return (ctx || doc).querySelector(sel); };
  var $$ = function (sel, ctx) { return Array.prototype.slice.call((ctx || doc).querySelectorAll(sel)); };

  /* ------------------------------------------------------------- tema -- */
  var themeBtn = $('#theme-toggle');
  if (themeBtn) {
    themeBtn.addEventListener('click', function () {
      var next = doc.documentElement.getAttribute('data-theme') === 'light' ? 'dark' : 'light';
      doc.documentElement.setAttribute('data-theme', next);
      try { localStorage.setItem('sha-theme', next); } catch (e) {}
    });
  }

  /* ------------------------------------------- relógio (America/Fortaleza) -- */
  var clock = $('#clock');
  if (clock) {
    var intl = doc.body.getAttribute('data-intl') || 'pt-BR';
    var fData = new Intl.DateTimeFormat(intl, {
      timeZone: 'America/Fortaleza', weekday: 'long', day: 'numeric',
      month: 'long', year: 'numeric'
    });
    var fHora = new Intl.DateTimeFormat(intl, {
      timeZone: 'America/Fortaleza', hour: '2-digit', minute: '2-digit',
      second: '2-digit', hour12: false
    });
    var tick = function () {
      var agora = new Date();
      clock.innerHTML = fData.format(agora) +
        ' <span aria-hidden="true">·</span> <b>' + fHora.format(agora) + '</b>';
    };
    tick();
    setInterval(tick, 1000);
  }

  /* ---------------------------------------------------- menu (mobile) -- */
  var menuBtn = $('#menu-btn');
  var menu = $('#menu');
  if (menuBtn && menu) {
    menuBtn.addEventListener('click', function () {
      var open = menu.classList.toggle('open');
      menuBtn.setAttribute('aria-expanded', String(open));
    });
    $$('a', menu).forEach(function (a) {
      a.addEventListener('click', function () {
        menu.classList.remove('open');
        menuBtn.setAttribute('aria-expanded', 'false');
      });
    });
  }

  /* --------------------------------------------- copiar blocos de código -- */
  $$('pre').forEach(function (pre) {
    var btn = doc.createElement('button');
    btn.className = 'copy-btn';
    btn.type = 'button';
    btn.textContent = 'copiar';
    btn.addEventListener('click', function () {
      var code = pre.querySelector('code');
      var text = code ? code.innerText : pre.innerText;
      var done = function () {
        btn.textContent = 'copiado ✓';
        setTimeout(function () { btn.textContent = 'copiar'; }, 1600);
      };
      if (navigator.clipboard && navigator.clipboard.writeText) {
        navigator.clipboard.writeText(text).then(done, function () { btn.textContent = 'erro'; });
      } else {
        var ta = doc.createElement('textarea');
        ta.value = text; doc.body.appendChild(ta); ta.select();
        try { doc.execCommand('copy'); done(); } catch (e) { btn.textContent = 'erro'; }
        doc.body.removeChild(ta);
      }
    });
    pre.appendChild(btn);
  });

  /* ------------------------------------------------- sumário destacado -- */
  var tocLinks = $$('.toc a');
  if (tocLinks.length && 'IntersectionObserver' in window) {
    var map = {};
    tocLinks.forEach(function (a) {
      var id = decodeURIComponent((a.getAttribute('href') || '').slice(1));
      if (id) map[id] = a;
    });
    var obs = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          tocLinks.forEach(function (a) { a.classList.remove('active'); });
          var link = map[entry.target.id];
          if (link) link.classList.add('active');
        }
      });
    }, { rootMargin: '-90px 0px -70% 0px' });
    Object.keys(map).forEach(function (id) {
      var el = doc.getElementById(id);
      if (el) obs.observe(el);
    });
  }

  /* ------------------------------------ progresso de leitura e topo -- */
  var progress = $('#progress');
  var toTop = $('#to-top');
  if (progress || toTop) {
    var onScroll = function () {
      var y = window.scrollY || doc.documentElement.scrollTop;
      if (progress) {
        var alcance = doc.documentElement.scrollHeight - window.innerHeight;
        progress.style.width = (alcance > 0 ? Math.min(100, (y / alcance) * 100) : 0) + '%';
      }
      if (toTop) toTop.classList.toggle('show', y > 600);
    };
    window.addEventListener('scroll', onScroll, { passive: true });
    onScroll();
  }
  if (toTop) {
    toTop.addEventListener('click', function () {
      window.scrollTo({ top: 0, behavior: 'smooth' });
    });
  }

  /* -------------------------------------------------------------- busca -- */
  var modal = $('#search-modal');
  var input = $('#search-input');
  var results = $('#search-results');
  var openBtn = $('#search-open');
  var index = null;
  var sel = -1;

  function loadIndex() {
    if (index) return Promise.resolve(index);
    return fetch(doc.body.getAttribute('data-search-index') || '/search-index.json')
      .then(function (r) { return r.json(); })
      .then(function (data) { index = data; return index; })
      .catch(function () { index = []; return index; });
  }

  function openSearch() {
    if (!modal) return;
    modal.hidden = false;
    loadIndex().then(function () { search(input.value); });
    setTimeout(function () { input.focus(); input.select(); }, 20);
  }

  function closeSearch() {
    if (!modal) return;
    modal.hidden = true;
    sel = -1;
  }

  function norm(s) {
    return (s || '').toLowerCase().normalize('NFD').replace(/[̀-ͯ]/g, '');
  }

  function escapeHtml(s) {
    return (s || '').replace(/[&<>"]/g, function (c) {
      return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c];
    });
  }

  function snippet(text, terms) {
    var n = norm(text);
    var pos = -1;
    for (var i = 0; i < terms.length && pos < 0; i++) pos = n.indexOf(terms[i]);
    if (pos < 0) pos = 0;
    var start = Math.max(0, pos - 45);
    var frag = escapeHtml(text.slice(start, start + 150).trim());
    terms.forEach(function (t) {
      if (!t) return;
      frag = frag.replace(new RegExp('(' + t.replace(/[.*+?^${}()|[\]\\]/g, '\\$&') + ')', 'ig'), '<mark>$1</mark>');
    });
    return (start > 0 ? '… ' : '') + frag + '…';
  }

  function search(q) {
    var terms = norm(q).split(/\s+/).filter(Boolean);
    if (!terms.length) {
      var sugestoes = (index || []).slice(0, 6);
      if (!sugestoes.length) {
        results.innerHTML = '<li class="search-empty">' + (doc.body.getAttribute('data-search-empty') || '') + '</li>';
        return;
      }
      results.innerHTML = '<li class="search-hint">' + (doc.body.getAttribute('data-search-suggest') || '') + '</li>' +
        sugestoes.map(function (p, i) {
          return '<li' + (i === 0 ? ' class="sel"' : '') + '><a href="' + p.u + '">' +
            '<strong>' + escapeHtml(p.t) + '</strong><small>' + escapeHtml(p.c) + '</small></a></li>';
        }).join('');
      sel = 0;
      return;
    }
    var hits = (index || []).map(function (p) {
      var hayTitle = norm(p.t + ' ' + p.c);
      var hayBody = norm(p.d + ' ' + p.x);
      var score = 0;
      terms.forEach(function (t) {
        if (hayTitle.indexOf(t) >= 0) score += 8;
        if (hayBody.indexOf(t) >= 0) score += 2;
      });
      return { p: p, score: score };
    }).filter(function (h) { return h.score > 0; })
      .sort(function (a, b) { return b.score - a.score; })
      .slice(0, 8);

    if (!hits.length) {
      results.innerHTML = '<li class="search-empty">' + (doc.body.getAttribute('data-search-none') || '') + '</li>';
      return;
    }
    results.innerHTML = hits.map(function (h, i) {
      return '<li' + (i === 0 ? ' class="sel"' : '') + '><a href="' + h.p.u + '">' +
        '<strong>' + escapeHtml(h.p.t) + '</strong>' +
        '<small>' + snippet(h.p.d + ' ' + h.p.x, terms) + '</small></a></li>';
    }).join('');
    sel = 0;
  }

  function move(delta) {
    var items = $$('li', results).filter(function (li) { return li.querySelector('a'); });
    if (!items.length) return;
    items.forEach(function (li) { li.classList.remove('sel'); });
    sel = (sel + delta + items.length) % items.length;
    items[sel].classList.add('sel');
    items[sel].scrollIntoView({ block: 'nearest' });
  }

  if (openBtn) openBtn.addEventListener('click', openSearch);
  if (modal) {
    $$('[data-close]', modal).forEach(function (el) { el.addEventListener('click', closeSearch); });
    input.addEventListener('input', function () { loadIndex().then(function () { search(input.value); }); });
    input.addEventListener('keydown', function (e) {
      if (e.key === 'ArrowDown') { e.preventDefault(); move(1); }
      else if (e.key === 'ArrowUp') { e.preventDefault(); move(-1); }
      else if (e.key === 'Enter') {
        var a = $('li.sel a', results);
        if (a) { e.preventDefault(); window.location.href = a.getAttribute('href'); }
      }
    });
  }

  doc.addEventListener('keydown', function (e) {
    var tag = (e.target.tagName || '').toLowerCase();
    if (e.key === 'Escape') closeSearch();
    if (e.key === '/' && tag !== 'input' && tag !== 'textarea') { e.preventDefault(); openSearch(); }
    if ((e.metaKey || e.ctrlKey) && e.key.toLowerCase() === 'k') { e.preventDefault(); openSearch(); }
  });
})();
