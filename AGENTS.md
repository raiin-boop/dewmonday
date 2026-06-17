# Dew Monday — GitHub Agents Instructions

> **Scope:** These instructions tell GitHub Copilot Agents, Codespaces AI, and any automated assistant how to build, edit, and extend the Dew Monday site. Follow them precisely to produce output consistent with what has already been built.

---

## 1. Project Overview

**Dew Monday** is a creator-focused newsletter platform hosted on **Jekyll + GitHub Pages** at `https://raiin-boop.github.io/dewmonday/`.

The site contains six "concept" pages built in public, each with its own standalone HTML file, its own visual theme, and its own content focus. The newsletter (`/concepts/creator-hub/`) is the connective tissue — everything links to and from it.

**Repository:** `github.com/raiin-boop/dewmonday`
**Base URL:** `https://raiin-boop.github.io/dewmonday/`
**Deployment:** Push to `main` → GitHub Actions builds Jekyll → Live in ~60s

---

## 2. Architecture Rules

### 2.1 Page Architecture — CRITICAL
Every concept page is a **standalone self-contained HTML file** with `layout: none` in its front matter. This means:

- **No** shared Jekyll layouts (`_layouts/default.html` is legacy — do not use it for new pages)
- **No** `{% include %}` partials — all CSS, nav, and footer are inline in the file
- **No** external JS frameworks — vanilla JavaScript only
- **No** CDN dependencies except Google Fonts

```yaml
# REQUIRED front matter for every concept page
---
layout: none
permalink: /concepts/your-concept-name/
---
```

### 2.2 File Naming & Folder Conventions

| Concept | Folder path | Filename | Permalink |
|---------|------------|----------|-----------|
| Creator Hub | `concepts/creator-hub/` | `index.html` | `/concepts/creator-hub/` |
| Art Drops | `concepts/art-dropshipping/` | `index.html` | `/concepts/art-dropshipping/` |
| Camera Drops | `concepts/camera-dropshipping/` | `index.html` | `/concepts/camera-dropshipping/` |
| Little Makers | `concepts/little-makers/` | `index.html` | `/concepts/little-makers/` |
| Tutorial App | `concepts/tutorial-app/` | `index.html` | `/concepts/tutorial-app/` |
| Art Tutorial App | `concepts/art-tutorial-app/` | `index.html` | `/concepts/art-tutorial-app/` |

**⚠️ NEVER create these folders — they are wrong:**
- `concepts/art-drops/` ← WRONG (must be `art-dropshipping`)
- `concepts/camera-drops/` ← WRONG (must be `camera-dropshipping`)

### 2.3 Jekyll URL Rules
Because the site is deployed at a GitHub Pages subpath (`/dewmonday/`), all internal links MUST use one of:

**Option A — Liquid filter (preferred for standalone pages):**
```html
<a href="{{ '/concepts/creator-hub/' | relative_url }}">Creator Hub</a>
```

**Option B — Hardcoded prefix (if Liquid doesn't process correctly):**
```html
<a href="/dewmonday/concepts/creator-hub/">Creator Hub</a>
```

Never use bare paths like `/concepts/creator-hub/` — they will 404 in production.

---

## 3. Design System

### 3.1 Font Stack
Always import all three families from Google Fonts. Never substitute.

```html
<link href="https://fonts.googleapis.com/css2?family=DM+Serif+Display:ital@0;1&family=Inter:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500;700&display=swap" rel="stylesheet">
```

| Role | Family | CSS var | Used for |
|------|--------|---------|----------|
| Display | DM Serif Display | `--font-display` | h1, h2, hero text, card titles, stat numbers, logo |
| Body | Inter | `--font-body` | All body text, buttons, descriptions, nav links |
| Mono | JetBrains Mono | `--font-mono` | Badges, tags, eyebrows, labels, issue numbers, week indicators |

### 3.2 CSS Variable Pattern
Every standalone concept page defines its own `:root` block. The variable names are **identical across all pages** — only the values change per theme.

```css
:root {
  /* Backgrounds */
  --bg: #F5F2EC;          /* Page background — light, tinted */
  --bg-white: #FFFFFF;    /* Card/panel backgrounds */

  /* Primary palette — unique per concept */
  --primary: #2D5A27;      /* Buttons, active states, links */
  --primary-dark: #1E3D1A; /* Hero gradient start, footer bg */
  --primary-light: #E8F0E7;/* Hover states, active nav items, chip bg */

  /* Accent — secondary color for highlights */
  --accent: #6BA3BE;
  --accent-light: #E8F2F8;

  /* Typography */
  --text: #1C1C1C;
  --text-muted: #6B6B6B;

  /* Borders */
  --border: #D8D4C8;
  --border-light: #EAE6DC;

  /* Fonts */
  --font-display: 'DM Serif Display', serif;
  --font-body: 'Inter', sans-serif;
  --font-mono: 'JetBrains Mono', monospace;

  /* Spacing & effects */
  --radius: 14px;
  --shadow: 0 4px 24px rgba(30,61,26,0.09);
}
```

### 3.3 Per-Concept Color Themes

| Concept | `--primary` | `--primary-dark` | `--primary-light` | `--accent` | `--bg` |
|---------|------------|-----------------|-------------------|-----------|--------|
| Creator Hub | `#2D5A27` | `#1E3D1A` | `#E8F0E7` | `#6BA3BE` | `#F5F2EC` |
| Art Drops | `#2A5F7A` | `#1A3A50` | `#E0EBF3` | `#7BAFD4` | `#F0F4F8` |
| Camera Drops | `#9A4E20` | `#6A2E0A` | `#FAF0E8` | `#D4803A` | `#FAF4EE` |
| Little Makers | `#2A7A6A` | `#1A5040` | `#E0F2EE` | `#5ABFAA` | `#EEF8F6` |
| Tutorial App | `#6B4FA0` | `#3D2060` | `#F0EEF8` | `#C47FD4` | `#F5F0F8` |
| Art Tutorial App | `#7A3A5A` | `#4A1A35` | `#F5E8EF` | `#C47A9A` | `#F8F2F5` |
| Homepage / Brand | `#2D5A27` | `#1E3D1A` | `#E8F0E7` | `#6BA3BE` | `#F5F0E8` |

---

## 4. Component Patterns

Every standalone page uses the same set of components. Copy these patterns exactly — do not invent variations unless explicitly asked.

### 4.1 Navigation (Sticky, Glassmorphism) — DUAL DROPDOWN REQUIRED

**Every page must include BOTH the Concepts dropdown AND the Brand dropdown.** This is non-negotiable — single-dropdown nav is the old format and must not be used for any new pages or updates.

The nav is otherwise identical across all pages; only the `.active` class on the current concept changes. Use `toggleDD('dd-concepts')` and `toggleDD('dd-brand')` with the shared JS function below.

```html
<nav class="nav">
  <div class="nav-left">
    <a href="/dewmonday/" class="nav-logo">Dew<span>Monday</span></a>

    <!-- ① CONCEPTS DROPDOWN -->
    <div class="nav-dropdown" id="dd-concepts">
      <button class="nav-dropdown-trigger" onclick="toggleDD('dd-concepts')">
        Concepts
        <svg class="chevron" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"/></svg>
      </button>
      <div class="nav-dropdown-menu">
        <a href="/dewmonday/concepts/creator-hub/" class="nav-menu-item">
          <span class="nav-menu-emoji">✍️</span>
          <div><div class="nav-menu-title">Creator Hub</div><div class="nav-menu-desc">Newsletter & build log</div></div>
        </a>
        <a href="/dewmonday/concepts/art-dropshipping/" class="nav-menu-item">
          <span class="nav-menu-emoji">🖼️</span>
          <div><div class="nav-menu-title">Art Drops</div><div class="nav-menu-desc">Independent artist spotlights</div></div>
        </a>
        <a href="/dewmonday/concepts/camera-dropshipping/" class="nav-menu-item">
          <span class="nav-menu-emoji">📷</span>
          <div><div class="nav-menu-title">Camera Drops</div><div class="nav-menu-desc">Curated creator gear kits</div></div>
        </a>
        <a href="/dewmonday/concepts/little-makers/" class="nav-menu-item">
          <span class="nav-menu-emoji">🎈</span>
          <div><div class="nav-menu-title">Little Makers</div><div class="nav-menu-desc">Screen-free activities for kids</div></div>
        </a>
        <div class="nav-menu-divider"></div>
        <a href="/dewmonday/concepts/tutorial-app/" class="nav-menu-item">
          <span class="nav-menu-emoji">🎨</span>
          <div><div class="nav-menu-title">Tutorial App</div><div class="nav-menu-desc">Creator skills platform</div></div>
        </a>
        <a href="/dewmonday/concepts/art-tutorial-app/" class="nav-menu-item">
          <span class="nav-menu-emoji">🖌️</span>
          <div><div class="nav-menu-title">Art Tutorial App</div><div class="nav-menu-desc">Structured art education</div></div>
        </a>
      </div>
    </div>

    <!-- ② BRAND DROPDOWN -->
    <div class="nav-dropdown" id="dd-brand">
      <button class="nav-dropdown-trigger" onclick="toggleDD('dd-brand')">
        Brand
        <svg class="chevron" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"/></svg>
      </button>
      <div class="nav-dropdown-menu">
        <a href="/dewmonday/brand/#overview" class="nav-menu-item">
          <span class="nav-menu-emoji">📖</span>
          <div><div class="nav-menu-title">Overview</div><div class="nav-menu-desc">What Dew Monday is</div></div>
        </a>
        <a href="/dewmonday/brand/#brand-identity" class="nav-menu-item">
          <span class="nav-menu-emoji">🎯</span>
          <div><div class="nav-menu-title">Brand Identity</div><div class="nav-menu-desc">Voice, tone, audience</div></div>
        </a>
        <a href="/dewmonday/brand/#design-system" class="nav-menu-item">
          <span class="nav-menu-emoji">🎨</span>
          <div><div class="nav-menu-title">Design System</div><div class="nav-menu-desc">Fonts, colors, components</div></div>
        </a>
        <a href="/dewmonday/brand/#interview-guide" class="nav-menu-item">
          <span class="nav-menu-emoji">🗣️</span>
          <div><div class="nav-menu-title">Interview Guide</div><div class="nav-menu-desc">25 validation questions</div></div>
        </a>
        <a href="/dewmonday/brand/#validation-scorecard" class="nav-menu-item">
          <span class="nav-menu-emoji">📊</span>
          <div><div class="nav-menu-title">Concept Scorecard</div><div class="nav-menu-desc">All 6 concepts rated</div></div>
        </a>
      </div>
    </div>
  </div>

  <div class="nav-right">
    <a href="/dewmonday/" class="nav-home-link">Home</a>
    <a href="/dewmonday/signup/" class="nav-subscribe-btn">Subscribe free →</a>
  </div>
</nav>
```

**Required JS — add once per page, just before `</body>`:**
```javascript
<script>
function toggleDD(id) {
  document.querySelectorAll('.nav-dropdown').forEach(d => {
    if (d.id !== id) d.classList.remove('open');
  });
  document.getElementById(id).classList.toggle('open');
}
document.addEventListener('click', e => {
  if (!e.target.closest('.nav-dropdown')) {
    document.querySelectorAll('.nav-dropdown').forEach(d => d.classList.remove('open'));
  }
});
</script>
```

> **⚠️ Sidebar duplication bug:** If a page had a sidebar-style nav before the redesign, remove ALL old nav/sidebar HTML before adding the new dual-dropdown nav. Never let two nav elements coexist in the same file.

**Nav CSS (paste into `<style>` block):**
```css
.nav{position:sticky;top:0;z-index:200;background:rgba(255,255,255,0.96);backdrop-filter:blur(12px);border-bottom:1px solid var(--border);display:flex;align-items:center;justify-content:space-between;padding:0 40px;height:64px;box-shadow:0 1px 12px rgba(0,0,0,0.07);}
.nav-left{display:flex;align-items:center;gap:32px;}
.nav-logo{font-family:var(--font-display);font-size:1.25rem;color:var(--primary-dark);text-decoration:none;white-space:nowrap;}
.nav-logo span{color:var(--accent);}
.nav-dropdown{position:relative;}
.nav-dropdown-trigger{display:flex;align-items:center;gap:6px;font-size:0.85rem;font-weight:600;color:var(--text);background:none;border:none;cursor:pointer;padding:6px 10px;border-radius:8px;transition:background 0.15s,color 0.15s;}
.nav-dropdown-trigger:hover,.nav-dropdown.open .nav-dropdown-trigger{background:var(--primary-light);color:var(--primary);}
.nav-dropdown-trigger .chevron{width:14px;height:14px;transition:transform 0.2s;}
.nav-dropdown.open .chevron{transform:rotate(180deg);}
.nav-dropdown-menu{display:none;position:absolute;top:calc(100% + 8px);left:0;background:#fff;border:1.5px solid var(--border);border-radius:16px;padding:8px;min-width:290px;box-shadow:0 12px 40px rgba(0,0,0,0.13);animation:menuIn 0.18s ease;z-index:300;}
.nav-dropdown.open .nav-dropdown-menu{display:block;}
@keyframes menuIn{from{opacity:0;transform:translateY(-6px);}to{opacity:1;transform:translateY(0);}}
.nav-menu-item{display:flex;align-items:center;gap:12px;padding:10px 12px;border-radius:10px;text-decoration:none;color:var(--text);transition:background 0.15s;}
.nav-menu-item:hover{background:var(--primary-light);}
.nav-menu-item.active{background:var(--primary-light);}
.nav-menu-emoji{font-size:1.1rem;flex-shrink:0;}
.nav-menu-title{font-weight:600;font-size:0.87rem;color:var(--text);line-height:1.2;}
.nav-menu-desc{font-size:0.74rem;color:var(--text-muted);}
.nav-menu-divider{height:1px;background:var(--border-light);margin:5px 0;}
.nav-right{display:flex;align-items:center;gap:14px;}
.nav-home-link{font-size:0.85rem;color:var(--text-muted);text-decoration:none;transition:color 0.15s;}
.nav-home-link:hover{color:var(--primary);}
.nav-subscribe-btn{padding:8px 18px;background:var(--primary);color:#fff;border-radius:20px;font-size:0.82rem;font-weight:700;text-decoration:none;transition:background 0.2s,transform 0.15s;white-space:nowrap;}
.nav-subscribe-btn:hover{background:var(--primary-dark);transform:translateY(-1px);}
```

### 4.2 Hero Section

```html
<section class="hero">
  <div class="hero-inner">
    <div class="hero-badge">
      <span class="hero-badge-dot"></span>
      Building in public · Concept 01
    </div>
    <h1>The newsletter that <em>reports on itself</em></h1>
    <p class="hero-sub">One builder. Six concepts. Every decision tracked weekly.</p>
    <div class="hero-actions">
      <a href="{{ '/signup/' | relative_url }}" class="btn-primary">Subscribe free →</a>
      <a href="#content" class="btn-ghost">Browse issues ↓</a>
    </div>
    <div class="hero-stats">
      <div class="hero-stat">
        <span class="hero-stat-num">4</span>
        <span class="hero-stat-label">Issues live</span>
      </div>
      <!-- repeat for other stats -->
    </div>
  </div>
</section>
```

**Hero CSS:**
```css
.hero{background:linear-gradient(135deg, var(--primary-dark) 0%, var(--primary) 55%, var(--primary-mid, var(--primary)) 100%);padding:80px 48px 72px;position:relative;overflow:hidden;}
.hero-inner{max-width:900px;margin:0 auto;position:relative;z-index:1;}
.hero-badge{display:inline-flex;align-items:center;gap:8px;background:rgba(255,255,255,0.1);border:1px solid rgba(255,255,255,0.2);padding:5px 14px;border-radius:999px;font-family:var(--font-mono);font-size:0.68rem;letter-spacing:0.1em;text-transform:uppercase;color:rgba(255,255,255,0.7);margin-bottom:24px;}
.hero-badge-dot{width:6px;height:6px;border-radius:50%;background:rgba(255,255,255,0.75);animation:pulse 2s infinite;}
@keyframes pulse{0%,100%{opacity:1;}50%{opacity:0.3;}}
.hero h1{font-family:var(--font-display);font-size:3.6rem;line-height:1.07;color:#fff;margin-bottom:18px;max-width:680px;}
.hero h1 em{font-style:italic;color:rgba(255,255,255,0.65);}
.hero-sub{font-size:1rem;color:rgba(255,255,255,0.72);margin-bottom:36px;max-width:520px;line-height:1.65;}
.hero-actions{display:flex;gap:12px;flex-wrap:wrap;margin-bottom:52px;}
.btn-primary{padding:13px 28px;background:#fff;color:var(--primary-dark);border-radius:12px;font-weight:700;font-size:0.92rem;text-decoration:none;box-shadow:0 4px 18px rgba(0,0,0,0.15);transition:transform 0.15s,box-shadow 0.15s;}
.btn-primary:hover{transform:translateY(-2px);box-shadow:0 8px 28px rgba(0,0,0,0.22);}
.btn-ghost{padding:12px 24px;border:1.5px solid rgba(255,255,255,0.3);color:rgba(255,255,255,0.85);border-radius:12px;font-weight:600;font-size:0.92rem;text-decoration:none;transition:background 0.15s,border-color 0.15s;}
.btn-ghost:hover{background:rgba(255,255,255,0.1);border-color:rgba(255,255,255,0.6);}
.hero-stats{display:flex;gap:40px;flex-wrap:wrap;}
.hero-stat-num{font-family:var(--font-display);font-size:2.4rem;color:rgba(255,255,255,0.88);display:block;}
.hero-stat-label{font-family:var(--font-mono);font-size:0.62rem;text-transform:uppercase;letter-spacing:0.1em;color:rgba(255,255,255,0.4);}
```

### 4.3 Filter Bar (Chip Buttons)

```html
<div class="filter-bar">
  <button class="filter-chip active" onclick="filterContent('all', this)">All</button>
  <button class="filter-chip" onclick="filterContent('category-a', this)">Category A</button>
  <button class="filter-chip" onclick="filterContent('category-b', this)">Category B</button>
</div>
```

```css
.filter-bar{display:flex;gap:8px;flex-wrap:wrap;margin-bottom:32px;}
.filter-chip{padding:7px 16px;border:1.5px solid var(--border);border-radius:999px;background:var(--bg-white);color:var(--text-muted);font-size:0.8rem;font-weight:600;cursor:pointer;transition:all 0.15s;font-family:var(--font-body);}
.filter-chip:hover{border-color:var(--primary);color:var(--primary);background:var(--primary-light);}
.filter-chip.active{background:var(--primary);border-color:var(--primary);color:#fff;}
```

**Filter JS:**
```javascript
function filterContent(category, btn) {
  document.querySelectorAll('.filter-chip').forEach(c => c.classList.remove('active'));
  btn.classList.add('active');
  document.querySelectorAll('[data-category]').forEach(card => {
    card.style.display = (category === 'all' || card.dataset.category === category) ? 'flex' : 'none';
  });
}
```

### 4.4 Content Grid (Cards)

```html
<div class="content-grid">
  <div class="content-card" data-category="category-a">
    <div class="card-header">
      <div class="card-tag">Tag</div>
      <div class="card-date">Jun 2026</div>
    </div>
    <div class="card-emoji">📝</div>
    <h3 class="card-title">Card Title</h3>
    <p class="card-desc">Card description text here.</p>
    <a href="#" class="card-link">Read more →</a>
  </div>
</div>
```

```css
.content-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(300px,1fr));gap:20px;}
.content-card{background:var(--bg-white);border:1.5px solid var(--border);border-radius:var(--radius);padding:24px;display:flex;flex-direction:column;gap:10px;transition:transform 0.2s,box-shadow 0.2s,border-color 0.2s;}
.content-card:hover{transform:translateY(-3px);box-shadow:var(--shadow);border-color:var(--primary-light);}
.card-header{display:flex;align-items:center;justify-content:space-between;}
.card-tag{font-family:var(--font-mono);font-size:0.62rem;font-weight:700;text-transform:uppercase;letter-spacing:0.08em;padding:3px 9px;border-radius:8px;background:var(--primary-light);color:var(--primary);}
.card-date{font-size:0.75rem;color:var(--text-muted);}
.card-emoji{font-size:2rem;}
.card-title{font-family:var(--font-display);font-size:1.15rem;color:var(--text);}
.card-desc{font-size:0.84rem;color:var(--text-muted);line-height:1.6;flex:1;}
.card-link{font-size:0.82rem;font-weight:700;color:var(--primary);text-decoration:none;margin-top:auto;transition:opacity 0.15s;}
.card-link:hover{opacity:0.75;}
```

### 4.5 Accordion (Expandable Sections)

```html
<div class="accordion">
  <button class="accordion-trigger" onclick="this.parentElement.classList.toggle('open')">
    <span>Section Title</span>
    <svg class="accordion-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
      <path d="M6 9l6 6 6-6"/>
    </svg>
  </button>
  <div class="accordion-body">
    <p>Content goes here.</p>
  </div>
</div>
```

```css
.accordion{border:1.5px solid var(--border);border-radius:var(--radius);overflow:hidden;margin-bottom:10px;}
.accordion-trigger{width:100%;display:flex;align-items:center;justify-content:space-between;padding:16px 20px;background:var(--bg-white);border:none;cursor:pointer;font-family:var(--font-body);font-size:0.92rem;font-weight:600;color:var(--text);text-align:left;transition:background 0.15s;}
.accordion-trigger:hover{background:var(--primary-light);}
.accordion-icon{width:16px;height:16px;transition:transform 0.2s;flex-shrink:0;}
.accordion.open .accordion-icon{transform:rotate(180deg);}
.accordion-body{display:none;padding:16px 20px 20px;border-top:1px solid var(--border-light);font-size:0.88rem;color:var(--text-muted);line-height:1.7;}
.accordion.open .accordion-body{display:block;}
```

### 4.6 Bottom CTA Section

All concept pages end with a CTA that links to `/signup/`. Use the concept's primary gradient.

```html
<section class="bottom-cta">
  <div class="bottom-cta-inner">
    <div class="bottom-cta-badge">Free · Every Monday</div>
    <h2>Follow the build <em>every week</em></h2>
    <p>Get the honest version — what's working, what failed, and what's next across all six concepts.</p>
    <div class="bottom-cta-actions">
      <a href="{{ '/signup/' | relative_url }}" class="btn-primary">Get early access →</a>
      <a href="{{ '/' | relative_url }}" class="btn-ghost">See all concepts</a>
    </div>
  </div>
</section>
```

```css
.bottom-cta{background:linear-gradient(135deg, var(--primary-dark), var(--primary));padding:80px 48px;text-align:center;}
.bottom-cta-inner{max-width:640px;margin:0 auto;}
.bottom-cta-badge{display:inline-block;font-family:var(--font-mono);font-size:0.68rem;font-weight:700;letter-spacing:0.12em;text-transform:uppercase;padding:5px 14px;border-radius:999px;background:rgba(255,255,255,0.12);color:rgba(255,255,255,0.7);border:1px solid rgba(255,255,255,0.2);margin-bottom:20px;}
.bottom-cta h2{font-family:var(--font-display);font-size:2.6rem;color:#fff;margin-bottom:14px;line-height:1.12;}
.bottom-cta h2 em{font-style:italic;color:rgba(255,255,255,0.65);}
.bottom-cta p{color:rgba(255,255,255,0.68);font-size:0.95rem;margin-bottom:32px;line-height:1.65;}
.bottom-cta-actions{display:flex;gap:12px;justify-content:center;flex-wrap:wrap;}
```

### 4.8 Sub-Page Template (Spotlights & Drops)

Spotlight and drop detail pages (e.g., Art Drops 001 Solitude Series, Camera Drops 001 Creator Starter Kit) are **sub-pages of their parent concept**. They follow the same standalone HTML architecture but use a two-column article + sidebar layout and inherit the parent concept's color theme exactly.

**Rules for all sub-pages:**
- Inherit the parent concept's `:root` variables without change
- Show a **breadcrumb** at the top of the content area (below the nav, before the hero)
- Use an **article + sidebar layout** (roughly 65% / 35% split on desktop, stacked on mobile)
- The hero uses the same gradient as the parent concept page
- Sidebar contains: issue metadata, quick-links / table of contents, key stats
- Mark the parent concept as `active` in the Concepts nav dropdown
- All internal links must use `/dewmonday/` prefix

**Breadcrumb pattern:**
```html
<div class="breadcrumb">
  <a href="/dewmonday/">Home</a>
  <span class="breadcrumb-sep">›</span>
  <a href="/dewmonday/concepts/art-dropshipping/">Art Drops</a>
  <span class="breadcrumb-sep">›</span>
  <span>Spotlight 001 — Solitude Series</span>
</div>
```

```css
.breadcrumb{display:flex;align-items:center;gap:8px;font-size:0.78rem;color:var(--text-muted);padding:14px 48px;border-bottom:1px solid var(--border-light);background:var(--bg-white);flex-wrap:wrap;}
.breadcrumb a{color:var(--primary);text-decoration:none;font-weight:500;}
.breadcrumb a:hover{text-decoration:underline;}
.breadcrumb-sep{color:var(--border);}
```

**Article + Sidebar layout:**
```html
<div class="article-layout">
  <article class="article-body">
    <!-- Main content: hero, editorial text, drop grid, etc. -->
  </article>
  <aside class="article-sidebar">
    <div class="sidebar-card">
      <div class="sidebar-label">Issue</div>
      <div class="sidebar-value">Spotlight 001</div>
    </div>
    <div class="sidebar-card">
      <div class="sidebar-label">Published</div>
      <div class="sidebar-value">June 2026</div>
    </div>
    <!-- TOC, key links, stats -->
  </aside>
</div>
```

```css
.article-layout{display:grid;grid-template-columns:1fr 320px;gap:40px;max-width:1200px;margin:0 auto;padding:48px 48px 80px;align-items:start;}
@media(max-width:900px){.article-layout{grid-template-columns:1fr;}.article-sidebar{order:-1;}}
.article-body{min-width:0;}
.article-sidebar{position:sticky;top:88px;display:flex;flex-direction:column;gap:16px;}
.sidebar-card{background:var(--bg-white);border:1.5px solid var(--border);border-radius:var(--radius);padding:18px 20px;}
.sidebar-label{font-family:var(--font-mono);font-size:0.62rem;font-weight:700;text-transform:uppercase;letter-spacing:0.1em;color:var(--text-muted);margin-bottom:4px;}
.sidebar-value{font-family:var(--font-display);font-size:1.05rem;color:var(--text);}
```

**Sub-page folder structure:**
```
concepts/
  art-dropshipping/
    index.html                          ← concept hub (parent)
    drops/
      001-solitude-series/
        index.html                      ← spotlight sub-page
      002-next-artist/
        index.html
  camera-dropshipping/
    index.html
    drops/
      001-creator-starter-kit/
        index.html                      ← gear drop sub-page
```

**Front matter for a sub-page:**
```yaml
---
layout: none
permalink: /concepts/art-dropshipping/drops/001-solitude-series/
---
```

---

### 4.7 Footer

```html
<footer>
  <a href="{{ '/' | relative_url }}" class="footer-logo">Dew<span>Monday</span></a>
  <div class="footer-links">
    <a href="{{ '/concepts/creator-hub/' | relative_url }}">Creator Hub</a>
    <a href="{{ '/concepts/art-dropshipping/' | relative_url }}">Art Drops</a>
    <a href="{{ '/concepts/camera-dropshipping/' | relative_url }}">Camera Drops</a>
    <a href="{{ '/concepts/little-makers/' | relative_url }}">Little Makers</a>
    <a href="{{ '/concepts/tutorial-app/' | relative_url }}">Tutorial App</a>
    <a href="{{ '/concepts/art-tutorial-app/' | relative_url }}">Art Tutorial App</a>
    <a href="{{ '/signup/' | relative_url }}">Subscribe</a>
  </div>
  <p class="footer-copy">© 2026 Dew Monday · Built in public</p>
</footer>
```

```css
footer{background:var(--primary-dark);padding:40px 48px;display:flex;flex-wrap:wrap;align-items:center;justify-content:space-between;gap:20px;}
.footer-logo{font-family:var(--font-display);font-size:1.1rem;color:rgba(255,255,255,0.75);text-decoration:none;}
.footer-logo span{color:var(--accent);}
.footer-links{display:flex;gap:24px;flex-wrap:wrap;}
.footer-links a{font-size:0.78rem;color:rgba(255,255,255,0.4);text-decoration:none;transition:color 0.15s;}
.footer-links a:hover{color:rgba(255,255,255,0.8);}
.footer-copy{font-family:var(--font-mono);font-size:0.65rem;color:rgba(255,255,255,0.22);}
```

---

## 5. Content Philosophy — DO NOT VIOLATE

These are Renny's explicit product decisions. Never override them.

### 5.1 Art Drops — Spotlight Model ONLY
Art Drops is **not a sales channel** and must **never be built as one**.

- ✅ DO: Write about artists, their work, their story, and their practice
- ✅ DO: Link directly to the artist's own shop/site (external link, no tracking)
- ✅ DO: Describe what the work costs and where to buy it *on the artist's site*
- ❌ NEVER: Add a "Buy" or "Purchase" button that processes payment on Dew Monday
- ❌ NEVER: Add affiliate links or referral codes
- ❌ NEVER: Imply Dew Monday takes a commission or handles transactions
- ❌ NEVER: Sell artwork that isn't created by Renny herself

**Correct framing:** "Buy directly from [artist name] →" linking to their external shop.
**Wrong framing:** "Add to cart" / "Buy now" / "Get yours here" (implying Dew Monday sells it)

### 5.2 Brand Voice
- Honest, unpolished, direct — this is built in public, not a curated brand
- First person ("I shipped this", "Here's what broke") in newsletter content
- No hype language ("revolutionary", "game-changing", "the best")
- Numbers are honest — if something failed, say so and show the data
- Readers are creators, not consumers

### 5.3 The Monday Rule
Every piece of content should connect back to the question: **"What happened this week in the build?"** The newsletter is the primary delivery mechanism. Concept pages are documentation and depth — not replacements for the newsletter.

---

## 6. Building a New Concept Page

When asked to create a new concept page, follow this exact checklist:

### Step 1 — Folder & File
```bash
mkdir -p concepts/your-concept-name
touch concepts/your-concept-name/index.html
```

### Step 2 — Front Matter
```yaml
---
layout: none
permalink: /concepts/your-concept-name/
---
```

### Step 3 — CSS Variables
Define new `:root` variables with a unique `--primary` / `--primary-dark` / `--accent` palette. Choose a theme color that doesn't conflict with existing concepts (see § 3.3).

### Step 4 — Nav Dropdown
Copy the nav from any existing concept page. Add the new concept entry to the dropdown. Mark the new concept's `nav-menu-item` with `class="nav-menu-item active"`.

### Step 5 — Update ALL Other Pages
After adding a new concept, you must add it to the nav dropdown on every other concept page. Run the provided `add-[concept]-nav.py` pattern, or manually add it to:
- `concepts/creator-hub/index.html`
- `concepts/art-dropshipping/index.html`
- `concepts/camera-dropshipping/index.html`
- `concepts/little-makers/index.html`
- `concepts/tutorial-app/index.html`
- `concepts/art-tutorial-app/index.html`
- `index.html` (homepage)

### Step 6 — Hero Section
- Use `linear-gradient(135deg, var(--primary-dark), var(--primary))`
- Include a `.hero-badge` with a pulsing dot and "Building in public · Concept ##"
- Include `.hero-stats` with 4 stat blocks

### Step 7 — Content Sections
Include at minimum:
- Filter bar with chip buttons
- Content grid (cards, drops, activities, or courses — depends on concept)
- At least one accordion section for FAQs or sub-topics
- Bottom CTA → `/signup/`
- Footer with all concept links

### Step 8 — Test URLs
Verify the permalink, check all nav links use `| relative_url`, and confirm there are no bare `/concepts/` paths without the Jekyll filter or `/dewmonday/` prefix.

---

## 7. Adding a New Nav Entry Script Template

When a new concept is created, generate a Python patch script at the repo root:

```python
#!/usr/bin/env python3
"""
add-[concept]-nav.py
Adds [Concept Name] to the Concepts nav dropdown on all existing concept pages.

Run from repo root: python3 add-[concept]-nav.py
"""
import re, pathlib

FILES = [
    "concepts/creator-hub/index.html",
    "concepts/art-dropshipping/index.html",
    "concepts/camera-dropshipping/index.html",
    "concepts/little-makers/index.html",
    "concepts/tutorial-app/index.html",
    "concepts/art-tutorial-app/index.html",
    "index.html",
]

NEW_ENTRY = '''          <div class="nav-menu-divider"></div>
          <a href="{{ '/concepts/your-concept-name/' | relative_url }}" class="nav-menu-item">
            <span class="nav-menu-emoji">EMOJI</span>
            <div>
              <div class="nav-menu-title">Concept Name</div>
              <div class="nav-menu-desc">Short tagline here</div>
            </div>
          </a>'''

# Find the last nav-menu-item (art-tutorial-app link) and insert after it
LAST_ITEM_PATTERN = re.compile(
    r'(<a[^>]*href=["\'][^"\']*art-tutorial-app[^"\']*["\'][^>]*>.*?</a>)',
    re.DOTALL
)

def process_file(path_str):
    p = pathlib.Path(path_str)
    if not p.exists():
        print(f"  ⚠️  NOT FOUND: {path_str}")
        return
    content = p.read_text(encoding="utf-8")
    if "/concepts/your-concept-name/" in content:
        print(f"  ✅ Already patched: {path_str}")
        return
    match = LAST_ITEM_PATTERN.search(content)
    if not match:
        print(f"  ❌ Anchor not found: {path_str}")
        return
    new_content = content[:match.end()] + "\n" + NEW_ENTRY + content[match.end():]
    p.write_text(new_content, encoding="utf-8")
    print(f"  ✅ Updated: {path_str}")

print("=== Adding [Concept Name] to nav dropdown ===\n")
for f in FILES:
    process_file(f)
print("\nDone. Run: git add -A && git commit -m 'feat: add [Concept Name] nav entry' && git push")
```

---

## 8. Deployment Workflow

### Standard deploy (any file change):
```bash
git add -A
git commit -m "feat: [brief description]"
git push
```
GitHub Actions handles the rest. Live in ~60 seconds at `https://raiin-boop.github.io/dewmonday/`.

### New concept page deploy:
```bash
# 1. Create the file
mkdir -p concepts/your-concept-name
# (create index.html per § 6)

# 2. Patch nav on all other pages
python3 add-your-concept-nav.py

# 3. Commit everything together
git add -A
git commit -m "feat: add [Concept Name] concept page and nav updates"
git push
```

### Jekyll config (`_config.yml`) — do not modify unless:
- Adding a new collection
- Changing the baseurl (currently `/dewmonday`)
- Modifying permalink structure

### If a page 404s after deploy:
1. Check the `permalink:` value in the front matter
2. Confirm the file is saved as `index.html` inside the concept folder (not `concept-name.html` at root)
3. Confirm `layout: none` is set (missing this causes Jekyll to wrap the file in the default layout, breaking standalone pages)
4. Verify all internal links use `| relative_url` or the `/dewmonday/` hardcoded prefix

---

## 9. File Delivery Notes

**Renny works on iOS.** When generating new HTML files for the site:

1. Export the file in `.txt` format (Renny drags `.txt` into Codespace and renames to `.html`)
2. Never export as `.html` directly unless specifically asked — iOS Codespaces can have issues with direct HTML drops
3. Do not zip files — deliver each file individually
4. Name the `.txt` file clearly: e.g., `index-homepage.txt`, `tutorial-app-index.txt`

---

## 10. Mandatory Page Standard — The Redesign IS the Default

> **This section overrides any older examples or legacy patterns you may encounter in the repo. When in doubt, follow this section.**

### 10.1 The Standalone HTML Redesign Is the Required Format

All new pages — concept hubs, sub-pages, spotlights, drops, brand sections, and any other content page — **must** follow the standalone HTML redesign format. This is not optional and applies to every file created or updated going forward.

**What this means in practice:**
- Every page is a single self-contained `.html` file with `layout: none` front matter
- All CSS, nav, and footer are inline in the file — no shared partials
- Every page includes the **dual-dropdown nav** (Concepts + Brand) — see § 4.1
- Every page has a **hero gradient section**, a **filter bar** (if content is filterable), **content cards**, and a **bottom CTA** linking to `/signup/`
- Every page ends with the **footer** (all concept links + copyright)
- Vanilla JS only — no frameworks

**What is deprecated (do not use for new content):**
- Markdown files (`.md`) with `layout: default` — these use the old sidebar-based format
- `_layouts/default.html` — legacy, do not reference in new pages
- Single-dropdown nav (Concepts only, no Brand dropdown) — old format
- Pages without a hero gradient — old format
- Pages without a bottom CTA — old format

### 10.2 Three Canonical Page Types

Every new page falls into one of three canonical types. Each type has a defined structure. Never invent a hybrid unless Renny explicitly asks.

#### Type 1 — Concept Hub Page
*Examples: `concepts/creator-hub/index.html`, `concepts/art-dropshipping/index.html`*

| Section | Required? | Notes |
|---------|-----------|-------|
| Front matter (`layout: none`, permalink) | ✅ | Always |
| Inline CSS with concept-specific `:root` | ✅ | See § 3.2–3.3 |
| Dual-dropdown sticky nav (Concepts + Brand) | ✅ | See § 4.1; mark current concept `active` |
| Hero gradient with badge, h1, sub, stats | ✅ | See § 4.2 |
| Filter bar (chip buttons) | ✅ if content is filterable | See § 4.3 |
| Content grid (cards / issues / drops) | ✅ | See § 4.4 |
| Accordion section (FAQs or sub-topics) | ✅ | See § 4.5 |
| Bottom CTA → `/signup/` | ✅ | See § 4.6 |
| Footer (all concept links) | ✅ | See § 4.7 |
| `toggleDD` JS for nav dropdowns | ✅ | See § 4.1 |

#### Type 2 — Spotlight / Drop Detail Page
*Examples: `concepts/art-dropshipping/drops/001-solitude-series/index.html`, `concepts/camera-dropshipping/drops/001-creator-starter-kit/index.html`*

| Section | Required? | Notes |
|---------|-----------|-------|
| Front matter (`layout: none`, full permalink) | ✅ | Always |
| Inline CSS — **inherit parent concept's color theme** | ✅ | Copy parent `:root` values exactly |
| Dual-dropdown sticky nav | ✅ | Mark **parent** concept `active` in Concepts dropdown |
| Breadcrumb (Home › Parent Concept › Page Title) | ✅ | See § 4.8 |
| Hero gradient (same gradient as parent concept) | ✅ | Narrower, editorial tone |
| Article + Sidebar two-column layout | ✅ | See § 4.8 for CSS |
| Sidebar: issue metadata, TOC, key links | ✅ | Sticky on desktop |
| Editorial content in article body | ✅ | Long-form, spotlight writing |
| Bottom CTA → `/signup/` | ✅ | See § 4.6 |
| Footer | ✅ | See § 4.7 |

> **Art Drops specifically:** Spotlight pages NEVER include buy buttons, cart flows, or affiliate links. All purchase links go directly to the artist's own external site. See § 5.1.

#### Type 3 — Brand Hub Sections
*Example: `brand/index.html` with accordion sections for Overview, Brand Identity, Design System, Interview Guide, Concept Scorecard*

| Section | Required? | Notes |
|---------|-----------|-------|
| Front matter (`layout: none`, `/brand/`) | ✅ | Always |
| Inline CSS — use green/homepage palette (`#2D5A27`) | ✅ | Same as Creator Hub |
| Dual-dropdown sticky nav | ✅ | Brand dropdown links to `#anchor` sections within the same page |
| Hero gradient | ✅ | Brand-focused headline |
| Accordion container with one `.accordion` per section | ✅ | See § 4.5 |
| Each accordion section has an `id` anchor | ✅ | e.g., `id="overview"`, `id="brand-identity"` — these are what the Brand nav links to |
| Bottom CTA | ✅ | See § 4.6 |
| Footer | ✅ | See § 4.7 |

> **Adding a new Brand section:** Add a new `.accordion` block inside `brand/index.html` and add the corresponding anchor link to the Brand dropdown in § 4.1. Do NOT create a separate page at `/brand/new-section/` — all brand content lives in a single file.

### 10.3 Page Update Checklist

Before delivering any new or updated page, verify:

- [ ] `layout: none` in front matter
- [ ] Correct `permalink:` set
- [ ] `:root` variables use correct concept color theme (see § 3.3)
- [ ] Dual-dropdown nav present (both Concepts AND Brand)
- [ ] Correct concept marked `active` in nav
- [ ] All internal links use `/dewmonday/` prefix
- [ ] No bare `/concepts/` paths without prefix
- [ ] Hero gradient matches concept theme
- [ ] Bottom CTA links to `/dewmonday/signup/`
- [ ] Footer includes all six concept links
- [ ] `toggleDD` JS is present and not duplicated
- [ ] No old sidebar nav remnants (sidebar duplication bug — see § 4.1 warning)
- [ ] File exported as `.txt` for Renny (see § 11)

---

## 11. What NOT to Build

Unless Renny explicitly asks, never:

- Add a payment processor or checkout flow to Art Drops
- Add affiliate tracking links to Camera Drops
- Use Bootstrap, Tailwind, or any CSS framework — hand-written CSS only
- Create shared CSS/JS files — all styles stay inline per page
- Delete or modify `_layouts/default.html` (legacy, may still be used by Markdown files)
- Create a `concepts/art-drops/` or `concepts/camera-drops/` folder — they are `art-dropshipping` and `camera-dropshipping`
- Add any tracking pixels, analytics, or third-party scripts without Renny's explicit approval
- Replace the Monday 6am delivery cadence with anything else in newsletter content
- Build a nav with only the Concepts dropdown — the Brand dropdown is also required (see § 4.1)
- Create a separate page at `/brand/section-name/` — all Brand content is accordion sections in `brand/index.html`

---

## 12. Quick Reference — All Concept Pages

| # | Name | Folder | Emoji | Primary | Hero gradient direction |
|---|------|--------|-------|---------|------------------------|
| 01 | Creator Hub | `concepts/creator-hub/` | ✍️ | `#2D5A27` | `#1E3D1A → #2D5A27` |
| 02 | Art Drops | `concepts/art-dropshipping/` | 🖼️ | `#2A5F7A` | `#1A3A50 → #2A5F7A` |
| 03 | Camera Drops | `concepts/camera-dropshipping/` | 📷 | `#9A4E20` | `#6A2E0A → #9A4E20` |
| 04 | Little Makers | `concepts/little-makers/` | 🎈 | `#2A7A6A` | `#1A5040 → #2A7A6A` |
| 05 | Tutorial App | `concepts/tutorial-app/` | 🎨 | `#6B4FA0` | `#3D2060 → #6B4FA0` |
| 06 | Art Tutorial App | `concepts/art-tutorial-app/` | 🖌️ | `#7A3A5A` | `#4A1A35 → #7A3A5A` |
| — | Homepage | `index.html` | — | `#2D5A27` | `#1E3D1A → #2D5A27` |
| — | Sign-up | `signup.html` | — | `#2D5A27` | `#1E3D1A → #2D5A27` |
