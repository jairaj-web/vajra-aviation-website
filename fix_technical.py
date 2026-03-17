import re, glob, sys
sys.stdout.reconfigure(encoding='utf-8')

all_html = glob.glob('*.html')

# ── 1. Fix author @type Organization → Person on 2 blog files ─────────────────
for fname in ['blog-cabin-crew-training-india.html', 'blog-cpl-ground-school-guide.html']:
    txt = open(fname, encoding='utf-8').read()
    new = txt.replace(
        '"author": {"@type": "Organization", "name": "Wt Off Bansode (Retd)"}',
        '"author": {"@type": "Person", "name": "Wt Off Bansode (Retd)", "worksFor": {"@id": "https://vajraaviation.com/#organization"}}'
    ).replace(
        '"author": {"@type": "Organization", "name": "Sqn Ldr I C Isaac (Retd)"}',
        '"author": {"@type": "Person", "name": "Sqn Ldr I C Isaac (Retd)", "worksFor": {"@id": "https://vajraaviation.com/#organization"}}'
    )
    if new != txt:
        open(fname, 'w', encoding='utf-8').write(new)
        print(f'Fixed author @type: {fname}')

# ── 2. Fix R. Sharma → Wg Cdr V Sundaram in dgca-ground-school-exams ─────────
fname = 'blog-dgca-ground-school-exams.html'
txt = open(fname, encoding='utf-8').read()
new = txt.replace('Wg Cdr (Retd) R. Sharma', 'Wg Cdr V Sundaram (Retd)')
if new != txt:
    open(fname, 'w', encoding='utf-8').write(new)
    print(f'Fixed R. Sharma → Wg Cdr V Sundaram: {fname}')

# ── 3. Fix footer copyright 2025 → 2026 on ALL pages ─────────────────────────
count = 0
for fname in all_html:
    txt = open(fname, encoding='utf-8').read()
    new = txt.replace(
        '© 2025 Vajra Aviation Private Limited. All Rights Reserved.',
        '© 2026 Vajra Aviation Private Limited. All Rights Reserved.'
    ).replace(
        '&copy; 2025 Vajra Aviation Private Limited. All Rights Reserved.',
        '&copy; 2026 Vajra Aviation Private Limited. All Rights Reserved.'
    )
    if new != txt:
        open(fname, 'w', encoding='utf-8').write(new)
        count += 1
print(f'Fixed copyright 2025→2026: {count} files')

# ── 4. Add og:image:width/height to 7 pages missing them ─────────────────────
og_missing = [
    'blog-cabin-crew-training-india.html',
    'blog-cpl-ground-school-guide.html',
    'blog-dgca-ame-training-guide.html',
    'blog-flight-dispatcher-career.html',
    'blog-how-to-become-commercial-pilot-india.html',
    'easa-exam-coaching-bangalore.html',
    'faq.html',
]
for fname in og_missing:
    txt = open(fname, encoding='utf-8').read()
    if 'og:image:width' in txt:
        continue
    # Add width/height after og:image line
    new = re.sub(
        r'(<meta property="og:image" content="[^"]*" />)',
        r'\1\n  <meta property="og:image:width" content="1200" />\n  <meta property="og:image:height" content="630" />',
        txt, count=1
    )
    if new != txt:
        open(fname, 'w', encoding='utf-8').write(new)
        print(f'Added og:image dims: {fname}')

# ── 5. Fix blog.html schema datePublished (stagger to match real articles) ─────
fname = 'blog.html'
txt = open(fname, encoding='utf-8').read()
date_fixes = {
    '"url": "https://vajraaviation.com/blog-how-to-become-commercial-pilot-india", "datePublished": "2026-03-11"':
        '"url": "https://vajraaviation.com/blog-how-to-become-commercial-pilot-india", "datePublished": "2025-12-03"',
    '"url": "https://vajraaviation.com/blog-easa-part-66-b1-vs-b2", "datePublished": "2026-03-11"':
        '"url": "https://vajraaviation.com/blog-easa-part-66-b1-vs-b2", "datePublished": "2025-10-08"',
    '"url": "https://vajraaviation.com/blog-dgca-ame-vs-easa-part-66", "datePublished": "2026-03-11"':
        '"url": "https://vajraaviation.com/blog-dgca-ame-vs-easa-part-66", "datePublished": "2025-10-22"',
    '"url": "https://vajraaviation.com/blog-dgca-ground-school-exams", "datePublished": "2026-03-11"':
        '"url": "https://vajraaviation.com/blog-dgca-ground-school-exams", "datePublished": "2024-12-15"',
    '"url": "https://vajraaviation.com/blog-cabin-crew-training-india", "datePublished": "2026-03-11"':
        '"url": "https://vajraaviation.com/blog-cabin-crew-training-india", "datePublished": "2026-01-21"',
    '"url": "https://vajraaviation.com/blog-cpl-ground-school-guide", "datePublished": "2026-03-11"':
        '"url": "https://vajraaviation.com/blog-cpl-ground-school-guide", "datePublished": "2025-12-17"',
    '"url": "https://vajraaviation.com/blog-dgca-ame-training-guide", "datePublished": "2026-03-11"':
        '"url": "https://vajraaviation.com/blog-dgca-ame-training-guide", "datePublished": "2025-11-05"',
    '"url": "https://vajraaviation.com/blog-flight-dispatcher-career", "datePublished": "2026-03-11"':
        '"url": "https://vajraaviation.com/blog-flight-dispatcher-career", "datePublished": "2026-01-07"',
}
new = txt
for old, rep in date_fixes.items():
    new = new.replace(old, rep)
if new != txt:
    open(fname, 'w', encoding='utf-8').write(new)
    print(f'Fixed blog.html schema dates')

# ── 6. Fix blog-dgca-ground-school-exams schema (add missing fields) ──────────
fname = 'blog-dgca-ground-school-exams.html'
txt = open(fname, encoding='utf-8').read()
# Find the old minimal schema and replace with complete one
old_schema_match = re.search(r'\{"@context":"https://schema\.org","@type":"BlogPosting".*?\}(?=\s*</script>)', txt, re.DOTALL)
if old_schema_match:
    old_schema = old_schema_match.group(0)
    new_schema = '{"@context":"https://schema.org","@type":"BlogPosting","headline":"How to Prepare for DGCA Ground School Exams: The Complete Study Guide","datePublished":"2024-12-15","dateModified":"2026-01-10","author":{"@type":"Person","name":"Wg Cdr V Sundaram (Retd)","worksFor":{"@id":"https://vajraaviation.com/#organization"}},"publisher":{"@type":"Organization","name":"Vajra Aviation Private Limited","url":"https://vajraaviation.com","logo":{"@type":"ImageObject","url":"https://vajraaviation.com/images/logo.png"}},"description":"Subject-wise DGCA ground school exam preparation strategy from Ex-IAF instructors. CPL and ATPL study guide 2026 covering Air Navigation, Meteorology, Air Regulations and all DGCA papers.","image":"https://vajraaviation.com/images/hero-airplane2.webp","url":"https://vajraaviation.com/blog-dgca-ground-school-exams","mainEntityOfPage":{"@type":"WebPage","@id":"https://vajraaviation.com/blog-dgca-ground-school-exams"}}'
    new = txt.replace(old_schema, new_schema)
    if new != txt:
        open(fname, 'w', encoding='utf-8').write(new)
        print(f'Fixed schema completeness: {fname}')

# ── 7. Add Our Partners to footers of 17 pages missing it ─────────────────────
PARTNERS_HTML = '''        <div style="margin-top:16px;">
          <h4 class="footer-heading">Our Partners</h4>
          <ul class="footer-links">
            <li><span><i class="fas fa-handshake"></i> Aviotrace Swiss</span></li>
            <li><span><i class="fas fa-handshake"></i> IANZL \u2013 New Zealand</span></li>
          </ul>
        </div>'''

missing_partners = [
    'course-cpl.html','course-atpl.html','course-easa-part-66.html','course-dgca-ame.html',
    'course-cabin-crew.html','course-flight-dispatcher.html','course-radio-telephony.html',
    'course-ground-staff.html','course-airline-ticketing.html','course-graduate-engineering.html',
    'placements.html','easa-coaching-south-india.html','easa-exam-coaching-bangalore.html',
    'compare-aviation-institutes-bangalore.html','compare-easa-part-66-india.html',
    'blog-dgca-ground-school-exams.html','sitemap.html',
]
for fname in missing_partners:
    try:
        txt = open(fname, encoding='utf-8').read()
        if 'Our Partners' in txt or 'Aviotrace Swiss' in txt:
            continue
        # Insert before closing div of footer contact column
        # Find the footer-contact-item for clock/hours, insert after it
        new = re.sub(
            r'(<div class="footer-contact-item"><i class="fas fa-clock"></i><span>Mon[^<]*</span></div>)',
            r'\1' + '\n' + PARTNERS_HTML,
            txt
        )
        if new != txt:
            open(fname, 'w', encoding='utf-8').write(new)
            print(f'Added Our Partners: {fname}')
        else:
            print(f'  Pattern not found for Our Partners: {fname}')
    except FileNotFoundError:
        print(f'  File not found: {fname}')

print('\nAll fixes applied.')
