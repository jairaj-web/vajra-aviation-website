import re, sys
sys.stdout.reconfigure(encoding='utf-8')

# ── Get standard nav from reference file ──────────────────────────────────────
ref = open('blog-flight-dispatcher-career.html', encoding='utf-8').read()
std_header = re.search(r'(<header class="header">.*?</header>)', ref, re.DOTALL).group(1)
std_mobile  = re.search(r'(<!-- MOBILE MENU.*?</div>\s*<!-- /MOBILE MENU -->)', ref, re.DOTALL)
std_mobile  = std_mobile.group(1) if std_mobile else ''

# Also get mobile menu from reference
ref_mobile = re.search(r'(<div class="mobile-menu".*?</div>\s*</div>)\s*\n\s*<!-- (?:Article|ARTICLE)', ref, re.DOTALL)
ref_mobile_html = ref_mobile.group(1) if ref_mobile else ''

def strip_html_from_meta(content):
    """Remove HTML tags from meta description content= attribute."""
    def clean(m):
        attr_val = m.group(1)
        # Remove <a ...>...</a> tags and their surrounding parens
        clean_val = re.sub(r'\s*\(<a[^>]*>[^<]*</a>\)', '', attr_val)
        clean_val = re.sub(r'<a[^>]*>([^<]*)</a>', r'\1', clean_val)
        clean_val = re.sub(r'<[^>]+>', '', clean_val)
        return f'<meta name="description" content="{clean_val.strip()}" />'
    return re.sub(r'<meta name="description" content="([^"]*(?:"(?!/)[^"]*)*)" />', clean, content)

def fix_nav(content):
    """Replace old dropdown-menu nav with mega-dropdown nav."""
    old_header = re.search(r'<header class="header">.*?</header>', content, re.DOTALL)
    if not old_header:
        return content
    # Check if already has mega-dropdown
    if 'mega-dropdown' in old_header.group(0):
        return content
    return content[:old_header.start()] + std_header + content[old_header.end():]

def fix_author(content, old_name, new_name):
    """Replace author name in article-meta-row span."""
    return content.replace(
        f'<i class="fas fa-user-tie"></i> {old_name}',
        f'<i class="fas fa-user-tie"></i> {new_name}'
    )

def fix_visible_date(content, old_date, new_date):
    """Replace visible published date in article hero."""
    return content.replace(old_date, new_date)

# ── FIXES PER FILE ─────────────────────────────────────────────────────────────
fixes = [
    # (filename, meta_fix, nav_fix, author_old, author_new, date_old, date_new)
    {
        'file': 'blog-cabin-crew-training-india.html',
        'meta': True,
        'nav':  True,
        'author_old': 'Vajra Aviation Faculty',
        'author_new': 'Wt Off Bansode (Retd)',
        'date_old': None,
        'date_new': None,
    },
    {
        'file': 'blog-cpl-ground-school-guide.html',
        'meta': True,
        'nav':  True,
        'author_old': 'Vajra Aviation Faculty',
        'author_new': 'Sqn Ldr I C Isaac (Retd)',
        'date_old': None,
        'date_new': None,
    },
    {
        'file': 'blog-dgca-ame-training-guide.html',
        'meta': True,
        'nav':  False,
        'author_old': None,
        'author_new': None,
        'date_old': None,
        'date_new': None,
    },
    {
        'file': 'blog-dgca-ground-school-exams.html',
        'meta': True,
        'nav':  False,
        'author_old': None,
        'author_new': None,
        'date_old': None,
        'date_new': None,
    },
    {
        'file': 'blog-easa-part-66-b1-vs-b2.html',
        'meta': False,
        'nav':  False,
        'author_old': None,
        'author_new': None,
        'date_old': 'March 11, 2026',
        'date_new': 'October 8, 2025',
    },
    {
        'file': 'blog-how-to-become-commercial-pilot-india.html',
        'meta': False,
        'nav':  False,
        'author_old': None,
        'author_new': None,
        'date_old': 'March 11, 2026',
        'date_new': 'December 3, 2025',
    },
]

for cfg in fixes:
    fname = cfg['file']
    content = open(fname, encoding='utf-8').read()
    original = content
    applied = []

    if cfg['meta']:
        content = strip_html_from_meta(content)
        applied.append('meta-desc cleaned')

    if cfg['nav']:
        content = fix_nav(content)
        applied.append('nav updated')

    if cfg['author_old']:
        content = fix_author(content, cfg['author_old'], cfg['author_new'])
        applied.append(f'author: {cfg["author_new"]}')

    if cfg['date_old']:
        content = fix_visible_date(content, cfg['date_old'], cfg['date_new'])
        applied.append(f'date: {cfg["date_new"]}')

    if content != original:
        open(fname, 'w', encoding='utf-8').write(content)
        print(f'FIXED {fname}: {", ".join(applied)}')
    else:
        print(f'  no change: {fname}')

print('\nDone.')
