/* reubs.link live content: posts from Typefully + latest YouTube episode.
   Every section keeps its static content as a fallback if the API is unavailable. */
(function () {
  var BASE = document.body.getAttribute('data-base') || '';
  var ONLINE = /^https?:$/.test(location.protocol) && !/claude/i.test(location.hostname);
  if (!ONLINE) return;

  var AUTHORS = {
    reubs_btc: { name: 'reubs', handle: '@reubs_btc', img: 'assets/me.png' },
    tenero_io: { name: 'Tenero', handle: '@tenero_io', img: 'assets/tenero.png' },
    LeoCoinSTX: { name: 'LEO', handle: '@LeoCoinSTX', img: 'assets/leo.png' },
    StackedUpStream: { name: 'Stacked Up', handle: '@StackedUpStream', img: 'assets/stackedup.png' }
  };
  var MONTHS = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];

  function esc(s) { return String(s).replace(/[&<>"']/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]; }); }
  function hl(s) { return esc(s).replace(/(@[A-Za-z0-9_]+|\$[A-Za-z][A-Za-z0-9_]*)/g, '<span class="hl">$1</span>'); }
  function fmtDate(iso) { var d = new Date(iso); return MONTHS[d.getUTCMonth()] + ' ' + d.getUTCDate(); }
  function clip(t, n) {
    t = t.replace(/https?:\/\/\S+/g, '').replace(/\n{3,}/g, '\n\n').trim();
    if (t.length <= n) return t;
    var cut = t.slice(0, n); var sp = cut.lastIndexOf(' ');
    return cut.slice(0, sp > n * 0.6 ? sp : n).replace(/[\s,.;:-]+$/, '') + '…';
  }
  function card(p) {
    var a = AUTHORS[p.account] || AUTHORS.reubs_btc;
    return '<a class="post" href="' + esc(p.url) + '" target="_blank" rel="noopener">' +
      '<div class="post-head"><img src="' + BASE + a.img + '" alt=""><div><b>' + esc(a.name) + '</b><span>' + a.handle + ' · ' + fmtDate(p.date) + '</span></div><svg><use href="#i-x"/></svg></div>' +
      '<p>' + hl(clip(p.text, 240)) + '</p><span class="post-more">Read on X →</span></a>';
  }
  function isRecap(p) { return /stacked\s?up\s*(ep\.?|episode)\s*\d+/i.test(p.text); }
  function isGm(p) { return p.text.replace(/\s+/g, ' ').trim().length < 40; }

  function getJSON(u) { return fetch(u).then(function (r) { if (!r.ok) throw r.status; return r.json(); }); }

  var postsP = getJSON('/api/posts').catch(function () { return null; });
  var ytP = document.querySelector('[data-live-episode]') ? getJSON('/api/youtube').catch(function () { return null; }) : Promise.resolve(null);

  postsP.then(function (data) {
    if (!data || !data.accounts) return;
    var acc = data.accounts;

    // Generic feeds: <div class="posts" data-live="reubs_btc" data-count="4" data-filter="stacks" data-tabs>
    document.querySelectorAll('[data-live]').forEach(function (el) {
      var accounts = el.getAttribute('data-live').split(',');
      var n = +el.getAttribute('data-count') || 4;
      var filter = el.getAttribute('data-filter');
      var render = function (accountsNow) {
        var list = [];
        accountsNow.forEach(function (a) { list = list.concat(acc[a] || []); });
        list = list.filter(function (p) { return !isGm(p); });
        if (filter === 'stacks') list = list.filter(function (p) { return !isRecap(p) && /stacks|\$stx|\bstx\b|sbtc|btc staking|bitcoin staking|bond|muneeb|capital markets/i.test(p.text); });
        else list = list.filter(function (p) { return !isRecap(p); });
        list.sort(function (a, b) { return new Date(b.date) - new Date(a.date); });
        list = list.slice(0, n);
        if (list.length >= Math.min(n, 3)) {
          el.innerHTML = list.map(card).join('');
          var sec = el.closest('[data-hide-empty]'); if (sec) sec.hidden = false;
        }
      };
      render(accounts);
      // Tabs: <div class="tabs" data-tabs-for="id">
      var tabs = document.querySelector('[data-tabs-for="' + el.id + '"]');
      if (tabs) {
        tabs.hidden = false;
        tabs.querySelectorAll('button').forEach(function (b) {
          var a = b.getAttribute('data-acct');
          if (!(acc[a] || []).length) { b.style.display = 'none'; return; }
          b.addEventListener('click', function () {
            tabs.querySelectorAll('button').forEach(function (x) { x.classList.remove('on'); });
            b.classList.add('on'); render([a]);
          });
        });
      }
    });

    // Episode count stat (highest EP number seen in recap posts)
    var maxEp = 0;
    (acc.reubs_btc || []).concat(acc.StackedUpStream || []).forEach(function (p) {
      var m = p.text.match(/stacked\s?up\s*(?:ep\.?|episode)\s*(\d+)/i); if (m) maxEp = Math.max(maxEp, +m[1]);
    });
    document.querySelectorAll('[data-live-stat="episodes"]').forEach(function (s) { if (maxEp > +s.textContent) s.textContent = maxEp; });

    // Stacked Up episode archive built from recap posts
    var eps = document.getElementById('eps');
    if (eps && window.STATIC_EPISODES) {
      var byNum = {};
      window.STATIC_EPISODES.forEach(function (e) { byNum[e.num] = e; });
      (acc.reubs_btc || []).concat(acc.StackedUpStream || []).forEach(function (p) {
        var m = p.text.match(/stacked\s?up\s*(?:ep\.?|episode)\s*(\d+)/i);
        if (!m || /live tomorrow|is live,? tomorrow/i.test(p.text)) return;
        var num = m[1]; if (byNum[num] && byNum[num].static) return;
        var all = p.text + '\n' + (p.thread || '');
        var yt = (all.match(/(?:youtu\.be\/|youtube\.com\/watch\?v=)([\w-]{11})/) || [])[1];
        var bullets = p.text.split('\n').filter(function (l) { return /^\s*→/.test(l); }).map(function (l) { return l.replace(/^\s*→\s*/, ''); }).slice(0, 4);
        byNum[num] = { num: num, date: fmtDate(p.date) + ', ' + new Date(p.date).getUTCFullYear(), yt: yt ? 'https://youtu.be/' + yt : null, recap: p.url, bullets: bullets };
      });
      var nums = Object.keys(byNum).map(Number).sort(function (a, b) { return b - a; });
      eps.innerHTML = nums.map(function (k, i) {
        var e = byNum[k]; var vid = e.yt ? e.yt.split('/').pop() : null;
        var thumb = vid ? ' style="background-image:url(\'https://i.ytimg.com/vi/' + vid + '/hqdefault.jpg\')"' : '';
        var watch = e.yt ? '<a class="chip" href="' + e.yt + '" target="_blank" rel="noopener"><svg><use href="#i-yt"/></svg>Watch</a>'
          : '<a class="chip" href="' + e.recap + '" target="_blank" rel="noopener"><svg><use href="#i-x"/></svg>Watch on X</a>';
        return '<div class="ep"><div class="ep-thumb"' + thumb + '><span class="tag">EP.' + e.num + '</span></div><div class="ep-body"><div class="ep-date">' + esc(e.date) + '</div><ul>' +
          e.bullets.map(function (b) { return '<li>' + hl(b) + '</li>'; }).join('') + '</ul><div class="ep-links">' + watch +
          '<a class="chip" href="' + e.recap + '" target="_blank" rel="noopener"><svg><use href="#i-x"/></svg>Recap</a></div></div></div>';
      }).join('');
    }
  });

  // Latest YouTube episode (skips Shorts)
  ytP.then(function (yt) {
    if (!yt || !yt.videos) return;
    var v = yt.videos.filter(function (x) { return !x.short; })[0];
    if (!v) return;
    document.querySelectorAll('[data-live-episode]').forEach(function (box) {
      var facade = box.querySelector('.facade');
      if (!facade || facade.getAttribute('data-video') === v.id) return;
      facade.setAttribute('data-video', v.id);
      facade.href = 'https://www.youtube.com/watch?v=' + v.id;
      var img = new Image();
      img.onload = function () {
        var url = img.naturalWidth > 200 ? img.src : 'https://i.ytimg.com/vi/' + v.id + '/hqdefault.jpg';
        facade.style.backgroundImage = "url('" + url + "')";
      };
      img.src = 'https://i.ytimg.com/vi/' + v.id + '/maxresdefault.jpg';
      var t = document.querySelector('[data-live-episode-title]');
      if (t) t.textContent = v.title;
    });
  });

  // Click-to-play for any facade (uses data-video, falls back to link)
  document.addEventListener('click', function (e) {
    var f = e.target.closest && e.target.closest('.facade[data-video]');
    if (!f) return;
    e.preventDefault();
    var box = f.parentElement;
    var ifr = document.createElement('iframe');
    ifr.src = 'https://www.youtube-nocookie.com/embed/' + f.getAttribute('data-video') + '?autoplay=1&rel=0';
    ifr.allow = 'accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture';
    ifr.allowFullscreen = true;
    box.innerHTML = ''; box.appendChild(ifr);
  });
})();
