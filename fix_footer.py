import re, sys
sys.stdout.reconfigure(encoding='utf-8')

STANDARD_FOOTER = '''<!-- ===== FOOTER ===== -->
<footer class="footer">
  <div class="container">
    <div class="footer-grid">
      <div class="footer-brand">
        <a href="/" class="logo">
          <img src="/images/logo-footer.png" alt="Vajra Aviation" class="logo-img" style="height:60px;" width="180" height="60" onerror="this.style.display='none'" />
          <div class="logo-text">
            <span class="brand-name">VAJRA</span>
            <span class="brand-sub">Aviation Private Limited</span>
          </div>
        </a>
        <p class="footer-desc">Vajra Aviation Private Limited — Bangalore\'s premier aviation training institute founded by Ex-IAF officers. ISO 9001:2015 certified. Shaping the next generation of aviation professionals since 2014.</p>
        <div class="footer-social">
          <a href="https://facebook.com/vajraaviation" target="_blank" aria-label="Facebook"><i class="fab fa-facebook-f"></i></a>
          <a href="https://instagram.com/vajraaviation" target="_blank" aria-label="Instagram"><i class="fab fa-instagram"></i></a>
          <a href="https://linkedin.com/company/vajraaviation" target="_blank" aria-label="LinkedIn"><i class="fab fa-linkedin-in"></i></a>
          <a href="https://wa.me/918111086614" target="_blank" aria-label="WhatsApp"><i class="fab fa-whatsapp"></i></a>
        </div>
      </div>
      <div>
        <h4 class="footer-heading">Our Courses</h4>
        <ul class="footer-links">
          <li><a href="/course-cpl"><i class="fas fa-plane-departure"></i> CPL Ground School</a></li>
          <li><a href="/course-atpl"><i class="fas fa-plane"></i> ATPL Ground School</a></li>
          <li><a href="/course-easa-part-66"><i class="fas fa-tools"></i> EASA Part 66</a></li>
          <li><a href="/course-flight-dispatcher"><i class="fas fa-broadcast-tower"></i> Flight Dispatcher</a></li>
          <li><a href="/course-cabin-crew"><i class="fas fa-user-tie"></i> Cabin Crew Training</a></li>
          <li><a href="/course-dgca-ame"><i class="fas fa-cog"></i> DGCA AME Training</a></li>
          <li><a href="/courses"><i class="fas fa-th-list"></i> View All Courses</a></li>
        </ul>
      </div>
      <div>
        <h4 class="footer-heading">Quick Links</h4>
        <ul class="footer-links">
          <li><a href="/about"><i class="fas fa-info-circle"></i> About Us</a></li>
          <li><a href="/facility-faculty"><i class="fas fa-chalkboard-teacher"></i> Our Faculty</a></li>
          <li><a href="/placements"><i class="fas fa-briefcase"></i> Placements</a></li>
          <li><a href="/blog"><i class="fas fa-blog"></i> Blog &amp; Articles</a></li>
          <li><a href="/faq"><i class="fas fa-question-circle"></i> FAQ</a></li>
          <li><a href="/contact"><i class="fas fa-envelope"></i> Contact Us</a></li>
          <li><a href="/privacy"><i class="fas fa-shield-alt"></i> Privacy Policy</a></li>
        </ul>
      </div>
      <div>
        <h4 class="footer-heading">Contact Us</h4>
        <div class="footer-contact-item"><i class="fas fa-phone"></i><a href="tel:+918111086614">8111086614 (Admissions)</a></div>
        <div class="footer-contact-item"><i class="fab fa-whatsapp"></i><a href="https://wa.me/918111086614" target="_blank">8111086614 (WhatsApp)</a></div>
        <div class="footer-contact-item"><i class="fas fa-phone"></i><a href="tel:+919840920090">9840920090</a></div>
        <div class="footer-contact-item"><i class="fas fa-envelope"></i><a href="mailto:info@vajraaviation.com">info@vajraaviation.com</a></div>
        <div class="footer-contact-item"><i class="fas fa-map-marker-alt"></i><span>NO.95, Third Floor, G R Arcade, Sector-C, Amrutha Nagar, Amruthalli, Bangalore – 560092</span></div>
        <div class="footer-contact-item"><i class="fas fa-clock"></i><span>Mon–Sat: 9:00 AM – 6:00 PM</span></div>
        <div style="margin-top:16px;">
          <h4 class="footer-heading">Our Partners</h4>
          <ul class="footer-links">
            <li><a href="https://aviotrace.com" target="_blank" rel="noopener"><i class="fas fa-handshake"></i> Aviotrace Swiss</a></li>
            <li><a href="https://www.ianzl.com" target="_blank" rel="noopener"><i class="fas fa-handshake"></i> IANZL – New Zealand</a></li>
          </ul>
        </div>
      </div>
    </div>
    <div class="footer-bottom">
      <p>&copy; 2025 Vajra Aviation Private Limited. All Rights Reserved. | ISO 9001:2015 Certified</p>
      <div class="footer-bottom-links">
        <a href="/privacy">Privacy Policy</a>
        <a href="/contact">Contact</a>
        <a href="/sitemap">Sitemap</a>
      </div>
    </div>
  </div>
</footer>'''

files = [
    'blog-flight-dispatcher-career.html',
    'blog-cabin-crew-training-india.html',
    'blog-cpl-ground-school-guide.html',
    'blog-dgca-ame-training-guide.html',
]

for fname in files:
    with open(fname, 'r', encoding='utf-8') as f:
        content = f.read()

    # Replace entire footer block (from <footer to </footer>)
    new_content = re.sub(
        r'<!-- ===== FOOTER ===== -->\s*<footer.*?</footer>',
        STANDARD_FOOTER,
        content,
        flags=re.DOTALL
    )
    # Also handle footer without the comment
    if new_content == content:
        new_content = re.sub(
            r'<footer class="footer">.*?</footer>',
            STANDARD_FOOTER.replace('<!-- ===== FOOTER ===== -->\n', ''),
            content,
            flags=re.DOTALL
        )

    if new_content != content:
        with open(fname, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f'Fixed: {fname}')
    else:
        print(f'No change: {fname}')
