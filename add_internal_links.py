import re, sys
sys.stdout.reconfigure(encoding='utf-8')

# ── CTA BOX HTML ──────────────────────────────────────────────────────────────
def cta_box(primary_href, primary_label, related=None):
    related_html = ''
    if related:
        links = ' &nbsp;|&nbsp; '.join(f'<a href="{h}">{l}</a>' for h, l in related)
        related_html = f'<p style="margin:8px 0 0;font-size:14px;color:#666;">Also explore: {links}</p>'
    return f'''
<div style="background:linear-gradient(135deg,#0B2D52,#163d6e);border-radius:12px;padding:24px 28px;margin:32px 0;color:#fff;">
  <p style="margin:0 0 6px;font-size:13px;color:#C8943A;font-weight:700;text-transform:uppercase;letter-spacing:1px;">Vajra Aviation — Bangalore</p>
  <p style="margin:0 0 14px;font-size:18px;font-weight:700;color:#fff;">Interested in this career? Enquire about our course.</p>
  <a href="{primary_href}" style="display:inline-block;background:#C8943A;color:#fff;padding:10px 24px;border-radius:6px;font-weight:700;font-size:14px;text-decoration:none;">View {primary_label} Course &rarr;</a>
  {related_html}
</div>'''

# ── HELPER: replace first occurrence not already inside <a> tag ───────────────
def replace_first(text, phrase, url, anchor=None):
    if anchor is None:
        anchor = phrase
    pos = 0
    while True:
        idx = text.find(phrase, pos)
        if idx == -1:
            return text
        before = text[:idx]
        open_a  = len(re.findall(r'<a\b', before))
        close_a = len(re.findall(r'</a>', before))
        in_tag  = bool(re.search(r'<[^>]*$', before))   # inside an HTML tag attribute
        if open_a == close_a and not in_tag:
            return text[:idx] + f'<a href="{url}">{anchor}</a>' + text[idx+len(phrase):]
        pos = idx + 1
    return text

# ── APPLY LINKS + CTA TO ARTICLE BODY ─────────────────────────────────────────
def patch(content, replacements, cta_html, insert_after_h2=1):
    """
    replacements: list of (phrase, url, anchor_or_None)
    insert_after_h2: insert CTA after the Nth </h2> in article body
    """
    m = re.search(r'(<article class="article-content">)(.*?)(</article>)', content, re.DOTALL)
    if not m:
        print('  WARNING: article-content not found')
        return content

    body = m.group(2)

    # --- contextual in-text links ---
    for phrase, url, anchor in replacements:
        body = replace_first(body, phrase, url, anchor)

    # --- insert CTA box after Nth </h2> ---
    h2_positions = [m2.end() for m2 in re.finditer(r'</h2>', body)]
    if len(h2_positions) >= insert_after_h2:
        insert_pos = h2_positions[insert_after_h2 - 1]
        body = body[:insert_pos] + cta_html + body[insert_pos:]

    return content[:m.start()] + m.group(1) + body + m.group(3) + content[m.end():]


# ══════════════════════════════════════════════════════════════════════════════
# PER-FILE RULES
# ══════════════════════════════════════════════════════════════════════════════

files = {

    'blog-flight-dispatcher-career.html': {
        'replacements': [
            # In step 2: "Vajra Aviation's programme is taught by..."
            ("Vajra Aviation's programme is taught by",
             '/course-flight-dispatcher',
             "Vajra Aviation's Flight Dispatcher course is taught by"),
            # In comparison table bottom line: "pursue a CPL"
            ('pursue a CPL',
             '/course-cpl',
             'pursue a <a href="/course-cpl">CPL</a>'),
            # ATPL mention if any
            ('ATPL ground school',
             '/course-atpl',
             'ATPL ground school'),
        ],
        'cta': cta_box(
            '/course-flight-dispatcher', 'Flight Dispatcher',
            [('/course-cpl', 'CPL Ground School'), ('/course-atpl', 'ATPL')]
        ),
        'insert_after_h2': 2,
    },

    'blog-cpl-ground-school-guide.html': {
        'replacements': [
            # First mention of ATPL
            ('ATPL examinations',
             '/course-atpl',
             'ATPL examinations'),
            ('ATPL ground school',
             '/course-atpl',
             'ATPL ground school'),
            # Flight dispatcher mention
            ('flight dispatcher',
             '/course-flight-dispatcher',
             'flight dispatcher'),
            # EASA Part 66 mention
            ('EASA Part 66',
             '/course-easa-part-66',
             'EASA Part 66'),
        ],
        'cta': cta_box(
            '/course-cpl', 'CPL Ground School',
            [('/course-atpl', 'ATPL Ground School'), ('/course-flight-dispatcher', 'Flight Dispatcher')]
        ),
        'insert_after_h2': 2,
    },

    'blog-cabin-crew-training-india.html': {
        'replacements': [
            # First mention of flight dispatcher
            ('flight dispatcher',
             '/course-flight-dispatcher',
             'flight dispatcher'),
            # First mention of CPL
            ('Commercial Pilot',
             '/course-cpl',
             'Commercial Pilot'),
            # Ground staff
            ('ground staff',
             '/course-ground-staff',
             'ground staff'),
            ('Ground Staff',
             '/course-ground-staff',
             'Ground Staff'),
        ],
        'cta': cta_box(
            '/course-cabin-crew', 'Cabin Crew Training',
            [('/course-ground-staff', 'Ground Staff'), ('/course-airline-ticketing', 'Airline Ticketing')]
        ),
        'insert_after_h2': 2,
    },

    'blog-dgca-ame-training-guide.html': {
        'replacements': [
            # EASA Part 66 mention
            ('EASA Part 66',
             '/course-easa-part-66',
             'EASA Part 66'),
            # Graduate engineering
            ('Graduate Engineering',
             '/course-graduate-engineering',
             'Graduate Engineering'),
            ('graduate engineering',
             '/course-graduate-engineering',
             'graduate engineering'),
        ],
        'cta': cta_box(
            '/course-dgca-ame', 'DGCA AME',
            [('/course-easa-part-66', 'EASA Part 66'), ('/course-graduate-engineering', 'Graduate Engineering')]
        ),
        'insert_after_h2': 2,
    },

    'blog-dgca-ame-vs-easa-part-66.html': {
        'replacements': [
            ('DGCA AME course',
             '/course-dgca-ame',
             'DGCA AME course'),
            ('EASA Part 66 course',
             '/course-easa-part-66',
             'EASA Part 66 course'),
            ('Graduate Engineering',
             '/course-graduate-engineering',
             'Graduate Engineering'),
        ],
        'cta': cta_box(
            '/course-dgca-ame', 'DGCA AME',
            [('/course-easa-part-66', 'EASA Part 66'), ('/course-graduate-engineering', 'Graduate Engineering')]
        ),
        'insert_after_h2': 2,
    },

    'blog-easa-part-66-b1-vs-b2.html': {
        'replacements': [
            ('DGCA AME',
             '/course-dgca-ame',
             'DGCA AME'),
            ('Graduate Engineering',
             '/course-graduate-engineering',
             'Graduate Engineering'),
            ('graduate engineering',
             '/course-graduate-engineering',
             'graduate engineering'),
        ],
        'cta': cta_box(
            '/course-easa-part-66', 'EASA Part 66',
            [('/course-dgca-ame', 'DGCA AME'), ('/course-graduate-engineering', 'Graduate Engineering')]
        ),
        'insert_after_h2': 2,
    },

    'blog-how-to-become-commercial-pilot-india.html': {
        'replacements': [
            ('ATPL ground school',
             '/course-atpl',
             'ATPL ground school'),
            ('Flight Dispatcher',
             '/course-flight-dispatcher',
             'Flight Dispatcher'),
            ('flight dispatcher',
             '/course-flight-dispatcher',
             'flight dispatcher'),
            ('EASA Part 66',
             '/course-easa-part-66',
             'EASA Part 66'),
        ],
        'cta': cta_box(
            '/course-cpl', 'CPL Ground School',
            [('/course-atpl', 'ATPL Ground School'), ('/course-flight-dispatcher', 'Flight Dispatcher')]
        ),
        'insert_after_h2': 2,
    },

    'blog-dgca-ground-school-exams.html': {
        'replacements': [
            ('ATPL',
             '/course-atpl',
             'ATPL'),
            ('Flight Dispatcher',
             '/course-flight-dispatcher',
             'Flight Dispatcher'),
            ('flight dispatcher',
             '/course-flight-dispatcher',
             'flight dispatcher'),
        ],
        'cta': cta_box(
            '/course-cpl', 'CPL Ground School',
            [('/course-atpl', 'ATPL Ground School'), ('/course-flight-dispatcher', 'Flight Dispatcher')]
        ),
        'insert_after_h2': 2,
    },
}

# ── RUN ────────────────────────────────────────────────────────────────────────
for fname, cfg in files.items():
    try:
        with open(fname, 'r', encoding='utf-8') as f:
            content = f.read()

        new_content = patch(
            content,
            cfg['replacements'],
            cfg['cta'],
            cfg.get('insert_after_h2', 2)
        )

        if new_content != content:
            with open(fname, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f'✓ Updated: {fname}')
        else:
            print(f'  No change: {fname}')
    except Exception as e:
        print(f'  ERROR {fname}: {e}')
