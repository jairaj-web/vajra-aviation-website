document.addEventListener('DOMContentLoaded', () => {
const hamburger     = document.getElementById('hamburgerBtn');
const mobileMenu    = document.getElementById('mobileMenu');
const mobileOverlay = document.getElementById('mobileOverlay');
const mobileClose   = document.getElementById('mobileClose');
function openMenu() {
mobileMenu?.classList.add('open');
mobileOverlay?.classList.add('show');
hamburger?.classList.add('active');
document.body.style.overflow = 'hidden';
}
function closeMenu() {
mobileMenu?.classList.remove('open');
mobileOverlay?.classList.remove('show');
hamburger?.classList.remove('active');
document.body.style.overflow = '';
}
hamburger?.addEventListener('click', openMenu);
mobileClose?.addEventListener('click', closeMenu);
mobileOverlay?.addEventListener('click', closeMenu);
document.querySelectorAll('.mobile-nav-link[data-submenu]').forEach(link => {
link.addEventListener('click', function(e) {
e.preventDefault();
const id  = this.dataset.submenu;
const sub = document.getElementById(id);
this.classList.toggle('open');
sub?.classList.toggle('open');
});
});
const header = document.querySelector('.header');
window.addEventListener('scroll', () => {
header?.classList.toggle('scrolled', window.scrollY > 50);
}, { passive: true });
const backTop = document.getElementById('backTop');
window.addEventListener('scroll', () => {
backTop?.classList.toggle('show', window.scrollY > 400);
}, { passive: true });
backTop?.addEventListener('click', () => window.scrollTo({ top: 0, behavior: 'smooth' }));
const animEls = document.querySelectorAll('.fade-in, .fade-in-left, .fade-in-right');
const animObserver = new IntersectionObserver((entries) => {
entries.forEach((entry, i) => {
if (entry.isIntersecting) {
setTimeout(() => entry.target.classList.add('visible'), i * 80);
animObserver.unobserve(entry.target);
}
});
}, { threshold: 0.12 });
animEls.forEach(el => animObserver.observe(el));
const counters = document.querySelectorAll('.counter');
const counterObserver = new IntersectionObserver((entries) => {
entries.forEach(entry => {
if (entry.isIntersecting) {
animateCounter(entry.target);
counterObserver.unobserve(entry.target);
}
});
}, { threshold: 0.5 });
counters.forEach(c => counterObserver.observe(c));
function animateCounter(el) {
const target   = parseInt(el.dataset.target);
const suffix   = el.dataset.suffix || '';
const prefix   = el.dataset.prefix || '';
const duration = 1800;
const step     = target / (duration / 16);
let current    = 0;
const timer = setInterval(() => {
current += step;
if (current >= target) { current = target; clearInterval(timer); }
el.textContent = prefix + Math.floor(current) + suffix;
}, 16);
}
document.querySelectorAll('.accordion-header').forEach(h => {
h.addEventListener('click', function() {
const body   = this.nextElementSibling;
const isOpen = this.classList.contains('active');
document.querySelectorAll('.accordion-header').forEach(x => {
x.classList.remove('active');
x.nextElementSibling?.classList.remove('open');
});
if (!isOpen) {
this.classList.add('active');
body?.classList.add('open');
}
});
});
document.querySelectorAll('.faq-question').forEach(q => {
q.addEventListener('click', function() {
const answer = this.nextElementSibling;
const isOpen = this.classList.contains('active');
document.querySelectorAll('.faq-question').forEach(x => {
x.classList.remove('active');
x.nextElementSibling?.classList.remove('open');
});
if (!isOpen) {
this.classList.add('active');
answer?.classList.add('open');
}
});
});
document.querySelectorAll('.contact-form').forEach(form => {
form.addEventListener('submit', function(e) {
e.preventDefault();
const btn      = this.querySelector('.btn-submit');
const original = btn.textContent;
btn.textContent = 'Sending...';
btn.disabled    = true;
setTimeout(() => {
btn.textContent       = '✓ Message Sent!';
btn.style.background  = '#2ECC71';
setTimeout(() => {
btn.textContent      = original;
btn.style.background = '';
btn.disabled         = false;
form.reset();
}, 3000);
}, 1200);
});
});
document.querySelector('.hero-bg')?.classList.add('loaded');
const page = window.location.pathname.split('/').pop() || 'index.html';
document.querySelectorAll('.nav-link, .mobile-nav-link').forEach(link => {
const href = link.getAttribute('href');
if (href === page || (page === '' && href === 'index.html')) {
link.classList.add('active');
}
});
document.querySelectorAll('a[href^="#"]').forEach(a => {
a.addEventListener('click', function(e) {
const target = document.querySelector(this.getAttribute('href'));
if (target) {
e.preventDefault();
target.scrollIntoView({ behavior: 'smooth', block: 'start' });
closeMenu();
}
});
});
});