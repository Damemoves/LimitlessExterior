// Mobile menu
const toggle = document.querySelector('.menu-toggle');
const nav = document.getElementById('site-nav');
if (toggle && nav) {
  toggle.addEventListener('click', () => {
    const open = nav.classList.toggle('open');
    toggle.setAttribute('aria-expanded', open);
  });
  nav.querySelectorAll('a').forEach(a => a.addEventListener('click', () => {
    nav.classList.remove('open');
    toggle.setAttribute('aria-expanded', 'false');
  }));
}

// Hero video: crossfade between clips (skipped when reduced motion is on)
const vids = document.querySelectorAll('.hero-media video');
const reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
if (vids.length === 2 && !reduce) {
  let cur = 0;
  vids[0].play().catch(() => {});
  vids.forEach((v, i) => v.addEventListener('ended', () => {
    if (i !== cur) return;
    const next = 1 - cur;
    vids[next].currentTime = 0;
    vids[next].play().catch(() => {});
    vids[next].style.opacity = 1;
    vids[cur].style.opacity = 0;
    cur = next;
  }));
} else if (reduce) {
  vids.forEach(v => { v.removeAttribute('autoplay'); v.pause(); });
}

// Booking calendar: mark the current month
const months = document.querySelectorAll('.cal-months b');
if (months.length === 12) {
  const now = new Date();
  months[now.getMonth()].classList.add('now');
  const pct = ((now.getMonth() + now.getDate() / 31) / 12) * 100;
  document.querySelectorAll('.cal-track').forEach(t => {
    const line = document.createElement('span');
    line.className = 'cal-now';
    line.style.left = pct + '%';
    t.appendChild(line);
  });
}

// Quote form → Netlify Forms
document.querySelectorAll('form[data-quote]').forEach(form => {
  const status = form.querySelector('.form-status');
  const btn = form.querySelector('button[type=submit]');
  const params = new URLSearchParams(location.search);
  const pre = params.get('service');
  if (pre) form.querySelectorAll('input[name=service]').forEach(c => { if (c.value === pre) c.checked = true; });

  form.addEventListener('submit', async e => {
    e.preventDefault();
    status.className = 'form-status';
    const picked = [...form.querySelectorAll('input[name=service]:checked')].map(c => c.value);
    if (!picked.length) {
      status.textContent = 'Pick at least one service so we can quote it.';
      status.classList.add('err');
      return;
    }
    if (!form.checkValidity()) { form.reportValidity(); return; }
    form.querySelector('input[name=services]').value = picked.join(', ');

    const data = new FormData(form);
    data.delete('service');
    btn.disabled = true;
    btn.textContent = 'Sending…';
    try {
      const res = await fetch('/', {
        method: 'POST',
        headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
        body: new URLSearchParams(data).toString()
      });
      if (!res.ok) throw new Error(res.status);
      form.reset();
      status.textContent = 'Request sent. We\'ll get back to you today with a price.';
      status.classList.add('ok');
      btn.textContent = 'Request sent';
    } catch {
      status.innerHTML = 'That didn\'t send. Call or text <a href="tel:+16478075919">(647) 807-5919</a> and we\'ll quote you right away.';
      status.classList.add('err');
      btn.disabled = false;
      btn.textContent = 'Get my free quote';
    }
  });
});
