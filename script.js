// Video overlay
const overlay = document.getElementById('vOverlay');
function dismiss(){ overlay.classList.add('gone'); }
document.getElementById('vSkip').addEventListener('click', dismiss);
document.getElementById('vPlay').addEventListener('click', dismiss);
setTimeout(dismiss, 8000);

// Nav dark on dark sections
const nav = document.getElementById('mainNav');
const darkSects = ['cats','origins'];
window.addEventListener('scroll', () => {
  const y = window.scrollY + 30;
  let dark = false;
  darkSects.forEach(id => {
    const el = document.getElementById(id);
    if(el){ const t = el.offsetTop, b = t + el.offsetHeight; if(y > t && y < b) dark = true; }
  });
  nav.classList.toggle('dark', dark);
});

// Scroll reveal
const reveals = document.querySelectorAll('.reveal');
const io = new IntersectionObserver(entries => {
  entries.forEach((e,i) => { if(e.isIntersecting){ setTimeout(()=>e.target.classList.add('vis'), i*60); io.unobserve(e.target); } });
}, { threshold: 0.08 });
reveals.forEach(r => io.observe(r));
