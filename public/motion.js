/* reubs.link motion: fade-up on scroll + stat count-up. Skipped for reduced-motion users. */
(function () {
  if (!('IntersectionObserver' in window)) return;
  if (window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches) return;
  document.documentElement.classList.add('motion');

  // Fade-up reveal, staggered within each group
  var SEL = 'section h2, section .label, .card, .post, .stat, .bounty, .ep, .pillar, .tl-item, .c-item, .cmc-card, .episode, .bridge, .pod, .feature';
  var els = document.querySelectorAll(SEL);
  var io = new IntersectionObserver(function (entries) {
    entries.forEach(function (e) {
      if (!e.isIntersecting) return;
      var t = e.target;
      t.classList.add('in');
      io.unobserve(t);
      // hand control back to normal hover styles once revealed
      setTimeout(function () { t.classList.remove('rv', 'in'); t.style.transitionDelay = ''; }, 1300);
    });
  }, { rootMargin: '0px 0px -8% 0px', threshold: 0.08 });
  els.forEach(function (el) {
    var sib = Array.prototype.indexOf.call(el.parentElement.children, el);
    el.classList.add('rv');
    el.style.transitionDelay = Math.min(sib, 6) * 70 + 'ms';
    io.observe(el);
  });

  // Count-up for stat numbers like 2.5M, 11.9K, 5,500, 20%+
  function countUp(el) {
    var node = el.firstChild;
    if (!node || node.nodeType !== 3) return;
    var m = node.nodeValue.match(/^(\s*)([\d,]*\.?\d+)(.*)$/);
    if (!m) return;
    var raw = m[2], target = parseFloat(raw.replace(/,/g, ''));
    if (!(target > 0) || (/^(19|20)\d\d$/.test(raw))) return; // leave years alone
    var dec = (raw.split('.')[1] || '').length, comma = raw.indexOf(',') > -1;
    var t0 = null, dur = 1300;
    function fmt(v) {
      var s = v.toFixed(dec);
      return comma ? Number(s).toLocaleString('en-US', { minimumFractionDigits: dec }) : s;
    }
    function step(ts) {
      if (!t0) t0 = ts;
      var k = Math.min(1, (ts - t0) / dur), e = 1 - Math.pow(1 - k, 3);
      node.nodeValue = m[1] + fmt(target * e) + m[3];
      if (k < 1) requestAnimationFrame(step); else node.nodeValue = m[1] + raw + m[3];
    }
    node.nodeValue = m[1] + fmt(0) + m[3];
    requestAnimationFrame(step);
  }
  var cio = new IntersectionObserver(function (entries) {
    entries.forEach(function (e) {
      if (!e.isIntersecting) return;
      countUp(e.target);
      cio.unobserve(e.target);
    });
  }, { threshold: 0.4 });
  document.querySelectorAll('.stat .num').forEach(function (el) { cio.observe(el); });
})();
