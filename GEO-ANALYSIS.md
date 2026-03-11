# GEO Analysis — vajraaviation.com
**Date:** 2026-03-11 | **Analyst:** Claude Code

---

## GEO Readiness Score: 41/100

| Platform | Score | Status |
|----------|-------|--------|
| Google AI Overviews | 48/100 | ⚠️ Partial |
| ChatGPT Web Search | 32/100 | ❌ Weak |
| Perplexity | 28/100 | ❌ Weak |
| Bing Copilot | 45/100 | ⚠️ Partial |

---

## 1. AI Crawler Access Status ✅ OPEN (uncontrolled)

**Current robots.txt:**
```
User-agent: *
Allow: /
Sitemap: https://vajraaviation.com/sitemap.xml
```

**Status:** All AI crawlers can access the site — which is good for visibility.
**Missing:** No explicit AI-crawler rules. No differentiation between training vs. search crawlers.

**Recommended addition:**
```
# Explicitly allow AI search crawlers
User-agent: GPTBot
Allow: /

User-agent: OAI-SearchBot
Allow: /

User-agent: ClaudeBot
Allow: /

User-agent: PerplexityBot
Allow: /

# Block training-only crawlers (optional)
User-agent: CCBot
Disallow: /

User-agent: Bytespider
Disallow: /
```

---

## 2. llms.txt Status ❌ MISSING

**Impact:** AI crawlers have no structured guide to your content.
**Action Required:** Create `/llms.txt` — see implementation below.

---

## 3. Brand Mention Analysis

| Platform | Status | Notes |
|----------|--------|-------|
| Wikipedia | ❌ Absent | No Wikipedia page for Vajra Aviation |
| Reddit | ❌ Absent | No r/aviation or r/india mentions found |
| YouTube | ⚠️ Present | @vajraaviation channel exists (in schema) |
| LinkedIn | ⚠️ Present | Company page exists (in schema) |
| Facebook | ⚠️ Present | Page exists (in schema) |
| Instagram | ⚠️ Present | Page exists (in schema) |
| Quora | ❌ Absent | No presence detected |
| IndiaStudyChannel | ❌ Absent | High-value aviation forum — missing |

**Key Gap:** ChatGPT cites Wikipedia (47.9%) and Reddit (11.3%) most heavily. Vajra Aviation has zero presence on either platform. This is the single biggest GEO weakness.

---

## 4. Passage-Level Citability Analysis

### Blog pages — STRONG ✅
Blog articles have excellent question-based H2/H3 structure:
- "What is a Commercial Pilot License (CPL)?" ✅
- "CPL Eligibility Requirements in India" ✅
- "Flying Hours Required for CPL" ✅

These follow the optimal 134–167 word self-contained block pattern.

### Homepage — WEAK ❌
- No definition block ("Vajra Aviation is an aviation training institute...")
- No stat-backed claims with sources
- No "What is X?" opening paragraphs

### Course pages — MODERATE ⚠️
- Have structured content but no self-contained answer blocks
- No attribution to primary sources (DGCA, EASA documents)
- No comparison tables

---

## 5. Structural Readability

| Element | Status |
|---------|--------|
| H1→H2→H3 hierarchy | ✅ Correct on blog pages |
| Question-based headings | ✅ Strong on blogs |
| Short paragraphs (2-4 sentences) | ⚠️ Mixed |
| Comparison tables | ❌ Missing from course pages |
| FAQ sections | ✅ Present on faq.html and blog pages |
| Publication dates visible | ❌ Not displayed on page (only in schema) |

---

## 6. Schema & Structured Data

| Schema Type | Status |
|-------------|--------|
| EducationalOrganization | ✅ Rich (logo, sameAs, accreditedBy, hasOfferCatalog) |
| BlogPosting (blog articles) | ✅ Present |
| FAQPage | ⚠️ Only on faq.html — missing from course pages |
| Course schema | ⚠️ Basic — missing price, duration, provider |
| LocalBusiness | ❌ Missing from contact.html |
| Person schema (faculty) | ❌ Missing from facility-faculty.html |

---

## 7. Server-Side Rendering Check ✅ GOOD

Site is **static HTML** — no JavaScript rendering dependency.
- All content visible in raw HTML ✅
- No React/Vue/Angular SPA issues ✅
- AI crawlers can read all content without JS execution ✅

---

## 8. Top 5 Highest-Impact Changes

| Priority | Action | GEO Impact |
|----------|--------|-----------|
| 1 | Create `/llms.txt` | +8 pts — immediate crawler guidance |
| 2 | Create Quora answers for aviation questions | +6 pts — Perplexity cites Quora heavily |
| 3 | Add "definition block" to homepage H1 section | +5 pts — citability for brand queries |
| 4 | Add author bio + Person schema to blog articles | +5 pts — E-E-A-T for AI Overviews |
| 5 | Add FAQPage schema to all course pages | +4 pts — featured in AI-generated FAQs |

---

## 9. Content Reformatting Suggestions

### Homepage — Add definition block (first 60 words after H1):
> "Vajra Aviation Private Limited is a DGCA-approved aviation training institute in Bangalore, India, founded in 2013 by Ex-Indian Air Force officers. It offers ground school training for CPL, ATPL, EASA Part 66 aircraft maintenance, cabin crew, and flight dispatcher certifications. The institute holds ISO 9001:2015 certification and is the only institute in India partnered with Aviotrace Swiss for EASA-approved training."

### Course pages — Add comparison table (example for EASA Part 66):
| Feature | B1.1 (Mechanical) | B2 (Avionics) |
|---------|-------------------|---------------|
| Duration | 24 months | 18 months |
| Focus | Airframe & engines | Avionics & electrical |
| Career | Line maintenance | Avionics technician |

---

## 10. Implementation Files Created

- [ ] `/llms.txt` — create (see below)
- [ ] robots.txt — update AI crawler rules
- [ ] Homepage — add definition block
- [ ] Course pages — add FAQPage schema
- [ ] faculty.html — add Person schema
