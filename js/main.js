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
const backTop = document.getElementById('backTop');
let ticking = false;
window.addEventListener('scroll', () => {
if (!ticking) {
requestAnimationFrame(() => {
const y = window.scrollY;
header?.classList.toggle('scrolled', y > 50);
backTop?.classList.toggle('show', y > 400);
ticking = false;
});
ticking = true;
}
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
const FORM_ENDPOINT = 'https://script.google.com/macros/s/AKfycbx95tU3nQEgED-sU28aBeQj1_DM9cHgXAiV7iw7xUO_jTQBEVpvefRDwTAkx1mpFBI6/exec';
const WEB3FORMS_KEY = '65857148-d828-4d3a-a009-8aa7cf996f55';
document.querySelectorAll('.contact-form').forEach(form => {
form.addEventListener('submit', function(e) {
e.preventDefault();
const btn      = this.querySelector('.btn-submit');
const original = btn.innerHTML;
btn.innerHTML  = '<i class="fas fa-spinner fa-spin"></i> Sending...';
btn.disabled   = true;
const data = new FormData(this);
data.append('source', document.title);
// 1. Google Sheets (iframe GET)
const iframeName = 'gs_iframe_' + Date.now();
const iframe = document.createElement('iframe');
iframe.name = iframeName;
iframe.style.display = 'none';
document.body.appendChild(iframe);
const tempForm = document.createElement('form');
tempForm.method = 'GET';
tempForm.action = FORM_ENDPOINT;
tempForm.target = iframeName;
tempForm.style.display = 'none';
for (const [key, value] of data.entries()) {
const input = document.createElement('input');
input.type = 'hidden';
input.name = key;
input.value = value;
tempForm.appendChild(input);
}
document.body.appendChild(tempForm);
tempForm.submit();
setTimeout(() => {
document.body.removeChild(tempForm);
document.body.removeChild(iframe);
}, 5000);
// 2. Web3Forms (email notification)
const w3 = new FormData();
w3.append('access_key', WEB3FORMS_KEY);
w3.append('from_name', 'Vajra Aviation Website');
w3.append('subject', 'New Enquiry: ' + (data.get('course') || 'Vajra Aviation') + ' — ' + (data.get('name') || ''));
w3.append('name', data.get('name') || '');
w3.append('email', data.get('email') || '');
w3.append('message',
  'Name: '    + (data.get('name')    || '-') + '\n' +
  'Phone: '   + (data.get('phone')   || '-') + '\n' +
  'Email: '   + (data.get('email')   || '-') + '\n' +
  'Course: '  + (data.get('course')  || '-') + '\n' +
  'Message: ' + (data.get('message') || '-') + '\n' +
  'Page: '    + document.title
);
fetch('https://api.web3forms.com/submit', {method:'POST', body:w3});
btn.innerHTML      = '<i class="fas fa-check"></i> Message Sent!';
btn.style.background = '#2ECC71';
this.reset();
setTimeout(() => {
btn.innerHTML      = original;
btn.style.background = '';
btn.disabled       = false;
}, 4000);
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