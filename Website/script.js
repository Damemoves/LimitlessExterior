// Navbar scroll effect
window.addEventListener('scroll', () => {
  document.getElementById('navbar').classList.toggle('scrolled', window.scrollY > 50);
});

// Animated water drips in fallback
const fallback = document.getElementById('heroFallback');
const video = document.querySelector('.hero-video');

// Check if video fails to load
video.addEventListener('error', showFallback);
video.addEventListener('loadeddata', () => { fallback.style.display = 'none'; });

function showFallback() {
  fallback.style.display = 'flex';
  for (let i = 0; i < 30; i++) {
    const d = document.createElement('div');
    d.className = 'droplet';
    d.style.left = Math.random() * 100 + '%';
    d.style.height = (40 + Math.random() * 80) + 'px';
    d.style.animationDuration = (3 + Math.random() * 5) + 's';
    d.style.animationDelay = (Math.random() * 5) + 's';
    fallback.appendChild(d);
  }
}

// Show fallback immediately as placeholder until video loads
showFallback();

// Scroll reveal
const observer = new IntersectionObserver((entries) => {
  entries.forEach((entry, i) => {
    if (entry.isIntersecting) {
      setTimeout(() => entry.target.classList.add('visible'), i * 100);
    }
  });
}, { threshold: 0.1 });

document.querySelectorAll('.service-card, .testimonial-card').forEach(el => observer.observe(el));

// Time slot selection
function selectSlot(el) {
  document.querySelectorAll('.time-slot').forEach(s => s.classList.remove('selected'));
  el.classList.add('selected');
}

// Zone selection
function selectZone(el) {
  document.querySelectorAll('.zone-btn').forEach(z => z.classList.remove('selected'));
  el.classList.add('selected');
}

// Set min date to today
const dateInput = document.getElementById('bookDate');
const today = new Date().toISOString().split('T')[0];
dateInput.min = today;

// Submit booking
function submitBooking() {
  const firstName = document.getElementById('firstName').value;
  const phone = document.getElementById('phone').value;
  const email = document.getElementById('email').value;
  const zone = document.querySelector('.zone-btn.selected');
  const slot = document.querySelector('.time-slot.selected');
  const date = document.getElementById('bookDate').value;
  const windows = document.getElementById('windowCount').value;

  if (!firstName || !phone || !email || !zone || !slot || !date || !windows) {
    alert('Please fill in all fields and select a time slot and zone.');
    return;
  }

  const successMsg = document.getElementById('successMsg');
  successMsg.style.display = 'block';
  successMsg.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
}
