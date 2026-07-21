# 🌿 Dew Monday — Design & Layout Template

> **A full reference for the Dew Monday site design system** — copy this to reproduce the exact look, page structure, components, and interactive modules used across `https://raiin-boop.github.io/dewmonday/`.

Dew Monday is a creator-focused newsletter platform built on **Jekyll + GitHub Pages**. Every page is a **self-contained standalone HTML file** with no shared layouts, no CSS frameworks, and no JavaScript libraries. Everything below documents what was actually built so you can copy it exactly.

---

## 📋 Table of Contents

1. [Architecture Rules](#1-architecture-rules)
2. [Repo File Structure](#2-repo-file-structure)
3. [Design System](#3-design-system)
   - [Fonts](#31-fonts)
   - [CSS Variables](#32-css-variables)
   - [Per-Concept Color Themes](#33-per-concept-color-themes)
4. [Page Types](#4-page-types)
   - [Type 1 — Concept Hub Page](#41-type-1--concept-hub-page)
   - [Type 2 — Sub-Page (Spotlight / Drop Detail)](#42-type-2--sub-page-spotlight--drop-detail)
   - [Type 3 — Brand Hub Page](#43-type-3--brand-hub-page)
   - [Type 4 — Utility Page (Sign-up, Activities)](#44-type-4--utility-page-sign-up-activities)
5. [Component Library](#5-component-library)
   - [Sticky Nav (Dual Dropdown)](#51-sticky-nav-dual-dropdown)
   - [Hero Section](#52-hero-section)
   - [Filter Bar](#53-filter-bar)
   - [Content / Issue Cards](#54-content--issue-cards)
   - [Accordion](#55-accordion)
   - [Build Log Timeline](#56-build-log-timeline)
   - [Resource List](#57-resource-list)
   - [Tool Grid](#58-tool-grid)
   - [Breadcrumb](#59-breadcrumb)
   - [Article + Sidebar Layout](#510-article--sidebar-layout)
   - [Artist Card](#511-artist-card)
   - [Piece Grid](#512-piece-grid)
   - [Gear Card](#513-gear-card)
   - [Pull Quote](#514-pull-quote)
   - [Editorial Callout](#515-editorial-callout)
   - [Notice Box](#516-notice-box)
   - [Sidebar Cards & Series Nav](#517-sidebar-cards--series-nav)
   - [Bottom CTA](#518-bottom-cta)
   - [Footer](#519-footer)
6. [Interactive Modules (JavaScript)](#6-interactive-modules-javascript)
7. [Jekyll URL Rules](#7-jekyll-url-rules)
8. [Deployment Workflow](#8-deployment-workflow)
9. [Agent Instructions — Replicate This Design in Any Repo](#9-agent-instructions--replicate-this-design-in-any-repo)
   - [What You Are Replicating](#91-what-you-are-replicating)
   - [Industry Substitution Map](#92-industry-substitution-map)
   - [Step-by-Step: Build a New Site](#93-step-by-step-build-a-new-site-with-this-design)
   - [Common Mistakes Agents Make](#94-common-mistakes-agents-make)
   - [Minimal Viable Page Template](#95-minimal-viable-page-template)
   - [Quick Industry Color Palettes](#96-quick-industry-color-starter-palettes)
   - [Font Pairing Alternatives](#97-font-pairing-alternatives)
10. [What NOT to Build](#10-what-not-to-build)

---

## 1. Architecture Rules

Every page in this site follows the same three rules:

| Rule | Detail |
|------|--------|
| **Standalone HTML** | Every page is a single `.html` file with `layout: none` in front matter |
| **Inline everything** | All CSS, fonts, and JavaScript live inside the file — no external stylesheets or shared JS |
| **No frameworks** | Vanilla CSS and vanilla JavaScript only. Google Fonts is the only CDN dependency |

```yaml
# Required front matter on every concept/brand/utility page
---
layout: none
permalink: /concepts/your-concept-name/
---
```

> **Why?** This makes every page self-sufficient and avoids Jekyll layout inheritance bugs on GitHub Pages subpaths.

---

## 2. Repo File Structure

```
dewmonday/
├── index.html                              ← Homepage (Type 1 layout, green theme)
├── signup.html                             ← Signup utility page
├── brand/
│   └── index.html                          ← Brand hub (Type 3, accordion sections)
├── concepts/
│   ├── creator-hub/
│   │   └── index.html                      ← Concept hub (Type 1, green theme)
│   ├── art-dropshipping/
│   │   ├── index.html                      ← Concept hub (Type 1, blue theme)
│   │   └── drops/
│   │       └── 001-solitude-series/
│   │           └── index.html              ← Spotlight sub-page (Type 2)
│   ├── camera-dropshipping/
│   │   ├── index.html                      ← Concept hub (Type 1, orange theme)
│   │   └── drops/
│   │       └── 001-creator-starter-kit/
│   │           └── index.html              ← Gear drop sub-page (Type 2)
│   ├── little-makers/
│   │   ├── index.html                      ← Concept hub (Type 1, teal theme)
│   │   └── activities.html                 ← Activity browser (Type 4 with filter pills)
│   ├── tutorial-app/
│   │   └── index.html                      ← Concept hub (Type 1, purple theme)
│   ├── art-tutorial-app/
│   │   └── index.html                      ← Concept hub (Type 1, rose theme)
│   └── creation-bundle/
│       └── index.html                      ← Concept hub (Type 1)
├── _config.yml
├── _layouts/
│   └── default.html                        ← Legacy only — do not use for new pages
└── README.md
```

**⚠️ Folder names are exact — do not abbreviate:**
- `concepts/art-dropshipping/` ✅ — not `art-drops/`
- `concepts/camera-dropshipping/` ✅ — not `camera-drops/`

---

## 3. Design System

### 3.1 Fonts

Always import all three families. Never substitute.

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=DM+Serif+Display:ital@0;1&family=Inter:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500;700&display=swap" rel="stylesheet">
```

| Role | Family | CSS Variable | Used on |
|------|--------|-------------|---------|
| Display | DM Serif Display | `--font-display` | h1, h2, hero text, card titles, stat numbers, logo wordmark |
| Body | Inter | `--font-body` | All body text, buttons, descriptions, nav links |
| Mono | JetBrains Mono | `--font-mono` | Badges, tags, eyebrows, labels, issue numbers, week indicators |

### 3.2 CSS Variables

Paste this `:root` block at the top of every `<style>` tag. Change the color values per concept (see § 3.3), keep everything else identical.

```css
:root {
  /* Backgrounds */
  --bg: #F5F2EC;           /* Page background — warm tint */
  --bg-white: #FFFFFF;     /* Card and panel backgrounds */

  /* Primary palette — unique per concept */
  --primary: #2D5A27;       /* Buttons, active states, links */
  --primary-dark: #1E3D1A;  /* Hero gradient start, footer background */
  --primary-mid: #3D7A35;   /* Hero gradient end (optional) */
  --primary-light: #E8F0E7; /* Hover backgrounds, chip fills, active nav items */

  /* Accent — secondary highlight color */
  --accent: #6BA3BE;
  --accent-light: #E8F2F8;

  /* Typography */
  --text: #1C1C1C;
  --text-muted: #6B6B6B;

  /* Borders */
  --border: #D8D4C8;
  --border-light: #EAE6DC;

  /* Font stacks */
  --font-display: 'DM Serif Display', serif;
  --font-body: 'Inter', sans-serif;
  --font-mono: 'JetBrains Mono', monospace;

  /* Shape & shadow */
  --radius: 14px;
  --shadow: 0 4px 24px rgba(30, 61, 26, 0.09);
}
```

**Global resets (paste after `:root`):**
```css
*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
html { scroll-behavior: smooth; }
body { font-family: var(--font-body); background: var(--bg); color: var(--text); line-height: 1.6; }
```

### 3.3 Per-Concept Color Themes

| Concept | `--bg` | `--primary` | `--primary-dark` | `--primary-light` | `--accent` | `--border` |
|---------|--------|------------|-----------------|-------------------|-----------|---------|
| Creator Hub | `#F5F2EC` | `#2D5A27` | `#1E3D1A` | `#E8F0E7` | `#6BA3BE` | `#D8D4C8` |
| Art Drops | `#F0F4F8` | `#2A5F7A` | `#1A3A50` | `#E0EBF3` | `#7BAFD4` | `#C8D8E4` |
| Camera Drops | `#FAF4EE` | `#9A4E20` | `#6A2E0A` | `#FAF0E8` | `#D4803A` | `#E0CEBA` |
| Little Makers | `#EEF8F6` | `#2A7A6A` | `#1A5040` | `#E0F2EE` | `#5ABFAA` | `#C8E0DA` |
| Tutorial App | `#F5F0F8` | `#6B4FA0` | `#3D2060` | `#F0EEF8` | `#C47FD4` | `#D8D0E8` |
| Art Tutorial App | `#F8F2F5` | `#7A3A5A` | `#4A1A35` | `#F5E8EF` | `#C47A9A` | `#DCC8D4` |
| Homepage / Brand | `#F5F0E8` | `#2D5A27` | `#1E3D1A` | `#E8F0E7` | `#6BA3BE` | `#E2DDD6` |

---

## 4. Page Types

### 4.1 Type 1 — Concept Hub Page

**Examples:** `concepts/creator-hub/index.html`, `concepts/art-dropshipping/index.html`, `index.html`

Every concept hub page includes these sections in order:

| # | Section | Required | Notes |
|---|---------|----------|-------|
| 1 | Front matter | ✅ | `layout: none` + correct `permalink:` |
| 2 | `<head>` with inline `<style>` | ✅ | Fonts, `:root`, all component CSS |
| 3 | Sticky dual-dropdown nav | ✅ | Mark current concept `active` — see § 5.1 |
| 4 | Hero gradient section | ✅ | Badge, h1, subtext, CTAs, stat row — see § 5.2 |
| 5 | Filter bar | ✅ if filterable | Chip buttons — see § 5.3 |
| 6 | Content grid | ✅ | Cards — see § 5.4 |
| 7 | Accordion section | ✅ | FAQs or sub-topics — see § 5.5 |
| 8 | Build log (optional) | ➕ | For Creator Hub — see § 5.6 |
| 9 | Resource/Tool sections (optional) | ➕ | See § 5.7–5.8 |
| 10 | Bottom CTA | ✅ | Links to `/signup/` — see § 5.18 |
| 11 | Footer | ✅ | All concept links — see § 5.19 |
| 12 | `<script>` blocks | ✅ | `toggleDD`, `filterContent`, accordion JS |

### 4.2 Type 2 — Sub-Page (Spotlight / Drop Detail)

**Examples:** `concepts/art-dropshipping/drops/001-solitude-series/index.html`, `concepts/camera-dropshipping/drops/001-creator-starter-kit/index.html`

| # | Section | Required | Notes |
|---|---------|----------|-------|
| 1 | Front matter | ✅ | Full permalink including sub-path |
| 2 | Inline CSS — **parent concept colors** | ✅ | Copy `:root` values from parent exactly |
| 3 | Dual-dropdown nav | ✅ | Mark **parent** concept `active` |
| 4 | Breadcrumb bar | ✅ | Home › Parent › Page — see § 5.9 |
| 5 | Hero gradient | ✅ | Same gradient as parent, editorial headline |
| 6 | Article + Sidebar layout | ✅ | Two-column grid — see § 5.10 |
| 7 | Sidebar (sticky) | ✅ | Issue metadata, TOC, links — see § 5.17 |
| 8 | Editorial content in article | ✅ | Long-form text, piece grids, gear cards |
| 9 | Bottom CTA | ✅ | |
| 10 | Footer | ✅ | |

**Permalink pattern:**
```yaml
permalink: /concepts/art-dropshipping/drops/001-solitude-series/
```

### 4.3 Type 3 — Brand Hub Page

**Example:** `brand/index.html`

All brand content lives in a **single file** at `/brand/`. Sections are accordion panels with `id` anchors that the Brand nav dropdown links to.

| # | Section | Required | Notes |
|---|---------|----------|-------|
| 1 | Front matter | ✅ | `permalink: /brand/` |
| 2 | Inline CSS — green/Creator Hub palette | ✅ | Same as Creator Hub |
| 3 | Dual-dropdown nav | ✅ | Brand dropdown items point to `#anchor` on this page |
| 4 | Hero gradient | ✅ | Brand-focused headline |
| 5 | Two-column layout: left sidebar nav + right content | ✅ | Sidebar has sticky anchor links |
| 6 | Accordion sections with `id` anchors | ✅ | One `.accordion-section` per topic |
| 7 | Bottom CTA + Footer | ✅ | |

> **Never** create sub-pages like `/brand/design-system/`. Everything is accordion sections in one file.

### 4.4 Type 4 — Utility Page (Sign-up, Activities)

**Examples:** `signup.html`, `concepts/little-makers/activities.html`

Utility pages use a simplified nav (logo + back link only — no dropdowns) and a compact hero. The main content is task-specific (sign-up form, or filterable activity cards with sticky controls bar).

---

## 5. Component Library

### 5.1 Sticky Nav (Dual Dropdown)

The nav is **identical across every page**. Only the `.active` class on the current concept item changes.

```html
<nav class="nav">
  <div class="nav-left">
    <a href="/dewmonday/" class="nav-logo">Dew<span>Monday</span></a>

    <!-- CONCEPTS DROPDOWN -->
    <div class="nav-dropdown" id="dd-concepts">
      <button class="nav-dropdown-trigger" onclick="toggleDD('dd-concepts')">
        Concepts
        <svg class="chevron" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
          <polyline points="6 9 12 15 18 9"/>
        </svg>
      </button>
      <div class="nav-dropdown-menu">
        <a href="/dewmonday/concepts/creator-hub/" class="nav-menu-item">
          <span class="nav-menu-emoji">✍️</span>
          <div>
            <div class="nav-menu-title">Creator Hub</div>
            <div class="nav-menu-desc">Newsletter & build log</div>
          </div>
        </a>
        <a href="/dewmonday/concepts/art-dropshipping/" class="nav-menu-item">
          <span class="nav-menu-emoji">🖼️</span>
          <div>
            <div class="nav-menu-title">Art Drops</div>
            <div class="nav-menu-desc">Independent artist spotlights</div>
          </div>
        </a>
        <a href="/dewmonday/concepts/camera-dropshipping/" class="nav-menu-item">
          <span class="nav-menu-emoji">📷</span>
          <div>
            <div class="nav-menu-title">Camera Drops</div>
            <div class="nav-menu-desc">Curated creator gear kits</div>
          </div>
        </a>
        <a href="/dewmonday/concepts/little-makers/" class="nav-menu-item">
          <span class="nav-menu-emoji">🎈</span>
          <div>
            <div class="nav-menu-title">Little Makers</div>
            <div class="nav-menu-desc">Screen-free activities for kids</div>
          </div>
        </a>
        <div class="nav-menu-divider"></div>
        <a href="/dewmonday/concepts/tutorial-app/" class="nav-menu-item">
          <span class="nav-menu-emoji">🎨</span>
          <div>
            <div class="nav-menu-title">Tutorial App</div>
            <div class="nav-menu-desc">Creator skills platform</div>
          </div>
        </a>
        <a href="/dewmonday/concepts/art-tutorial-app/" class="nav-menu-item">
          <span class="nav-menu-emoji">🖌️</span>
          <div>
            <div class="nav-menu-title">Art Tutorial App</div>
            <div class="nav-menu-desc">Structured art education</div>
          </div>
        </a>
      </div>
    </div>

    <!-- BRAND DROPDOWN -->
    <div class="nav-dropdown" id="dd-brand">
      <button class="nav-dropdown-trigger" onclick="toggleDD('dd-brand')">
        Brand
        <svg class="chevron" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
          <polyline points="6 9 12 15 18 9"/>
        </svg>
      </button>
      <div class="nav-dropdown-menu">
        <a href="/dewmonday/brand/#overview" class="nav-menu-item">
          <span class="nav-menu-emoji">📖</span>
          <div>
            <div class="nav-menu-title">Overview</div>
            <div class="nav-menu-desc">What Dew Monday is</div>
          </div>
        </a>
        <a href="/dewmonday/brand/#brand-identity" class="nav-menu-item">
          <span class="nav-menu-emoji">🎯</span>
          <div>
            <div class="nav-menu-title">Brand Identity</div>
            <div class="nav-menu-desc">Voice, tone, audience</div>
          </div>
        </a>
        <a href="/dewmonday/brand/#design-system" class="nav-menu-item">
          <span class="nav-menu-emoji">🎨</span>
          <div>
            <div class="nav-menu-title">Design System</div>
            <div class="nav-menu-desc">Fonts, colors, components</div>
          </div>
        </a>
        <a href="/dewmonday/brand/#interview-guide" class="nav-menu-item">
          <span class="nav-menu-emoji">🗣️</span>
          <div>
            <div class="nav-menu-title">Interview Guide</div>
            <div class="nav-menu-desc">25 validation questions</div>
          </div>
        </a>
        <a href="/dewmonday/brand/#validation-scorecard" class="nav-menu-item">
          <span class="nav-menu-emoji">📊</span>
          <div>
            <div class="nav-menu-title">Concept Scorecard</div>
            <div class="nav-menu-desc">All 6 concepts rated</div>
          </div>
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

**Mark the active page:** add `class="nav-menu-item active"` to the item that matches the current page.

**Nav CSS:**
```css
.nav {
  position: sticky; top: 0; z-index: 200;
  background: rgba(255, 255, 255, 0.96);
  backdrop-filter: blur(12px);
  border-bottom: 1px solid var(--border);
  display: flex; align-items: center; justify-content: space-between;
  padding: 0 48px; height: 68px;
  box-shadow: 0 1px 12px rgba(0, 0, 0, 0.07);
}
.nav-left { display: flex; align-items: center; gap: 32px; }
.nav-logo { font-family: var(--font-display); font-size: 1.3rem; color: var(--primary-dark); text-decoration: none; white-space: nowrap; }
.nav-logo span { color: var(--accent); }

.nav-dropdown { position: relative; }
.nav-dropdown-trigger {
  display: flex; align-items: center; gap: 6px;
  font-size: 0.85rem; font-weight: 600; color: var(--text);
  background: none; border: none; cursor: pointer;
  padding: 6px 10px; border-radius: 8px;
  transition: background 0.15s, color 0.15s;
}
.nav-dropdown-trigger:hover,
.nav-dropdown.open .nav-dropdown-trigger { background: var(--primary-light); color: var(--primary); }
.nav-dropdown-trigger .chevron { width: 14px; height: 14px; transition: transform 0.2s; }
.nav-dropdown.open .chevron { transform: rotate(180deg); }

.nav-dropdown-menu {
  display: none; position: absolute; top: calc(100% + 8px); left: 0;
  background: #fff; border: 1.5px solid var(--border);
  border-radius: 16px; padding: 8px; min-width: 290px;
  box-shadow: 0 12px 40px rgba(0, 0, 0, 0.13);
  animation: menuIn 0.18s ease; z-index: 300;
}
.nav-dropdown.open .nav-dropdown-menu { display: block; }
@keyframes menuIn { from { opacity: 0; transform: translateY(-6px); } to { opacity: 1; transform: translateY(0); } }

.nav-menu-item {
  display: flex; align-items: center; gap: 12px;
  padding: 10px 12px; border-radius: 10px;
  text-decoration: none; color: var(--text);
  transition: background 0.15s;
}
.nav-menu-item:hover { background: var(--primary-light); }
.nav-menu-item.active { background: var(--primary-light); color: var(--primary); }
.nav-menu-emoji { font-size: 1.1rem; width: 24px; text-align: center; flex-shrink: 0; }
.nav-menu-title { font-size: 0.85rem; font-weight: 600; line-height: 1.2; }
.nav-menu-desc { font-size: 0.75rem; color: var(--text-muted); margin-top: 1px; }
.nav-menu-divider { height: 1px; background: var(--border-light); margin: 4px 0; }

.nav-right { display: flex; align-items: center; gap: 14px; }
.nav-home-link { font-size: 0.85rem; color: var(--text-muted); text-decoration: none; transition: color 0.15s; }
.nav-home-link:hover { color: var(--primary); }
.nav-subscribe-btn {
  padding: 8px 18px; background: var(--primary); color: #fff;
  border-radius: 20px; font-size: 0.82rem; font-weight: 700;
  text-decoration: none; transition: background 0.2s, transform 0.15s; white-space: nowrap;
}
.nav-subscribe-btn:hover { background: var(--primary-dark); transform: translateY(-1px); }
```

---

### 5.2 Hero Section

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
      <a href="/dewmonday/signup/" class="hero-btn-primary">Subscribe free →</a>
      <a href="#content" class="hero-btn-secondary">Browse issues ↓</a>
    </div>
    <div class="hero-stats">
      <div>
        <span class="hero-stat-num">6am</span>
        <span class="hero-stat-label">Every Monday</span>
      </div>
      <div>
        <span class="hero-stat-num">6</span>
        <span class="hero-stat-label">Concepts tracked</span>
      </div>
      <div>
        <span class="hero-stat-num">Free</span>
        <span class="hero-stat-label">Always</span>
      </div>
      <div>
        <span class="hero-stat-num">4</span>
        <span class="hero-stat-label">Issues live</span>
      </div>
    </div>
  </div>
</section>
```

**Hero CSS:**
```css
.hero {
  background: linear-gradient(135deg, var(--primary-dark) 0%, var(--primary) 55%, var(--primary-mid, var(--primary)) 100%);
  padding: 80px 48px 72px;
  position: relative; overflow: hidden;
}
.hero::before {
  content: ''; position: absolute; inset: 0;
  background: radial-gradient(ellipse at 70% 40%, rgba(255,255,255,0.07) 0%, transparent 60%);
  pointer-events: none;
}
.hero-inner { max-width: 900px; margin: 0 auto; position: relative; z-index: 1; }

.hero-badge {
  display: inline-flex; align-items: center; gap: 8px;
  background: rgba(255, 255, 255, 0.12); border: 1px solid rgba(255, 255, 255, 0.2);
  padding: 5px 14px; border-radius: 999px;
  font-family: var(--font-mono); font-size: 0.68rem;
  letter-spacing: 0.1em; text-transform: uppercase;
  color: rgba(255, 255, 255, 0.75); margin-bottom: 24px;
}
.hero-badge-dot {
  width: 6px; height: 6px; border-radius: 50%;
  background: rgba(255, 255, 255, 0.75);
  animation: pulse 2s infinite;
}
@keyframes pulse { 0%, 100% { opacity: 1; } 50% { opacity: 0.3; } }

.hero h1 {
  font-family: var(--font-display); font-size: 3.6rem;
  line-height: 1.07; color: #fff; margin-bottom: 18px; max-width: 680px;
}
.hero h1 em { font-style: italic; color: rgba(255, 255, 255, 0.65); }
.hero-sub {
  font-size: 1rem; color: rgba(255, 255, 255, 0.72);
  margin-bottom: 36px; max-width: 520px; line-height: 1.65;
}

.hero-actions { display: flex; gap: 12px; flex-wrap: wrap; margin-bottom: 52px; }
.hero-btn-primary {
  padding: 13px 28px; background: #fff; color: var(--primary-dark);
  border-radius: 12px; font-weight: 700; font-size: 0.92rem;
  text-decoration: none; box-shadow: 0 4px 18px rgba(0,0,0,0.15);
  transition: transform 0.15s, box-shadow 0.15s;
}
.hero-btn-primary:hover { transform: translateY(-2px); box-shadow: 0 8px 28px rgba(0,0,0,0.22); }
.hero-btn-secondary {
  padding: 12px 24px; border: 1.5px solid rgba(255, 255, 255, 0.3);
  color: rgba(255, 255, 255, 0.85); border-radius: 12px;
  font-weight: 600; font-size: 0.92rem; text-decoration: none;
  transition: background 0.15s, border-color 0.15s;
}
.hero-btn-secondary:hover { background: rgba(255,255,255,0.1); border-color: rgba(255,255,255,0.6); }

.hero-stats { display: flex; gap: 40px; flex-wrap: wrap; }
.hero-stat-num {
  font-family: var(--font-display); font-size: 2.4rem;
  color: rgba(255, 255, 255, 0.88); display: block;
}
.hero-stat-label {
  font-family: var(--font-mono); font-size: 0.62rem;
  text-transform: uppercase; letter-spacing: 0.1em;
  color: rgba(255, 255, 255, 0.4);
}
```

---

### 5.3 Filter Bar

```html
<div class="filter-bar">
  <button class="filter-chip active" onclick="filterContent('all', this)">All</button>
  <button class="filter-chip" onclick="filterContent('dispatch', this)">📬 Dispatch</button>
  <button class="filter-chip" onclick="filterContent('deep-dive', this)">🔍 Deep Dive</button>
  <button class="filter-chip" onclick="filterContent('tools', this)">🔧 Tools</button>
</div>
```

Each filterable card gets a `data-cat` attribute:
```html
<div class="issue-card" data-cat="dispatch">…</div>
```

**Filter CSS:**
```css
.filter-bar { display: flex; gap: 8px; flex-wrap: wrap; margin-bottom: 28px; }
.filter-chip {
  padding: 7px 16px; border-radius: 20px;
  border: 1.5px solid var(--border); background: var(--bg-white);
  font-size: 0.8rem; font-weight: 500; color: var(--text-muted);
  cursor: pointer; transition: all 0.18s; white-space: nowrap;
  font-family: var(--font-body);
}
.filter-chip:hover { border-color: var(--primary); color: var(--primary); }
.filter-chip.active { background: var(--primary); border-color: var(--primary); color: #fff; }
```

---

### 5.4 Content / Issue Cards

```html
<div class="issue-grid">
  <div class="issue-card" data-cat="dispatch">
    <div class="issue-thumb" style="background: linear-gradient(135deg, var(--primary-dark), var(--primary));">
      ✍️
      <span class="issue-num">Issue 001</span>
    </div>
    <div class="issue-body">
      <div class="issue-tag">Dispatch</div>
      <div class="issue-title">Why I'm Building Five Things at Once</div>
      <div class="issue-desc">The reasoning behind running five parallel concepts and what that means for how Dew Monday works.</div>
      <div class="issue-meta">
        <span class="issue-date">Jun 2, 2026</span>
        <span class="issue-read">5 min read</span>
      </div>
    </div>
  </div>
</div>
```

**Card CSS:**
```css
.issue-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(272px, 1fr)); gap: 16px; }
.issue-card {
  background: var(--bg-white); border: 1.5px solid var(--border);
  border-radius: var(--radius); overflow: hidden;
  transition: transform 0.18s, box-shadow 0.18s;
  display: flex; flex-direction: column;
}
.issue-card:hover { transform: translateY(-3px); box-shadow: var(--shadow); }
.issue-card.hidden { display: none; }

.issue-thumb {
  height: 120px; display: flex; align-items: center;
  justify-content: center; font-size: 2.8rem; position: relative;
}
.issue-num {
  position: absolute; top: 10px; left: 10px;
  font-family: var(--font-mono); font-size: 0.62rem; font-weight: 700;
  text-transform: uppercase; letter-spacing: 0.06em;
  padding: 3px 9px; border-radius: 10px;
  background: rgba(255,255,255,0.15); color: rgba(255,255,255,0.9);
}
.issue-body { padding: 16px 18px; flex: 1; display: flex; flex-direction: column; gap: 6px; }
.issue-tag {
  font-family: var(--font-mono); font-size: 0.65rem; font-weight: 700;
  text-transform: uppercase; letter-spacing: 0.08em; color: var(--primary);
}
.issue-title { font-weight: 700; font-size: 0.95rem; color: var(--text); line-height: 1.35; }
.issue-desc { font-size: 0.78rem; color: var(--text-muted); line-height: 1.55; flex: 1; }
.issue-meta {
  display: flex; align-items: center; justify-content: space-between;
  margin-top: 12px; padding-top: 12px; border-top: 1px solid var(--border-light);
}
.issue-date { font-family: var(--font-mono); font-size: 0.68rem; color: var(--text-muted); }
.issue-read { font-size: 0.72rem; color: var(--primary); font-weight: 600; }
```

---

### 5.5 Accordion

```html
<div class="accordion">
  <button class="accordion-trigger" onclick="this.closest('.accordion').classList.toggle('open')">
    <div class="accordion-trigger-left">
      <span class="accordion-icon">📬</span>
      <div>
        <div class="accordion-label">Section Title</div>
        <div class="accordion-sublabel">Short description of what's inside</div>
      </div>
    </div>
    <svg class="accordion-chevron" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
      <path d="M6 9l6 6 6-6"/>
    </svg>
  </button>
  <div class="accordion-body">
    <p>Content goes here.</p>
  </div>
</div>
```

**Accordion CSS:**
```css
.accordion {
  border: 1.5px solid var(--border); border-radius: var(--radius);
  overflow: hidden; margin-bottom: 12px; background: var(--bg-white);
}
.accordion-trigger {
  width: 100%; display: flex; align-items: center; justify-content: space-between;
  padding: 20px 24px; background: none; border: none;
  cursor: pointer; text-align: left; transition: background 0.15s;
}
.accordion-trigger:hover { background: var(--primary-light); }
.accordion.open .accordion-trigger {
  background: var(--primary-light); border-bottom: 1px solid var(--border);
}
.accordion-trigger-left { display: flex; align-items: center; gap: 14px; }
.accordion-icon { font-size: 1.3rem; }
.accordion-label { font-weight: 700; font-size: 0.95rem; color: var(--text); }
.accordion-sublabel { font-size: 0.75rem; color: var(--text-muted); margin-top: 2px; }
.accordion-chevron {
  width: 18px; height: 18px; color: var(--text-muted);
  transition: transform 0.25s; flex-shrink: 0;
}
.accordion.open .accordion-chevron { transform: rotate(180deg); color: var(--primary); }
.accordion-body { display: none; padding: 24px; }
.accordion.open .accordion-body { display: block; }
```

---

### 5.6 Build Log Timeline

```html
<div class="build-log">
  <div class="log-entry">
    <div class="log-week">Week 1</div>
    <div>
      <div class="log-title">Picked a name, bought the domain</div>
      <div class="log-desc">Spent three hours on Namecheap. Ended up with dewmonday.com. The dot-com was gone so this lives on GitHub Pages for now.</div>
      <div class="log-tags">
        <span class="log-tag">Setup</span>
        <span class="log-tag">Domain</span>
      </div>
    </div>
  </div>
</div>
```

**Build log CSS:**
```css
.build-log { display: flex; flex-direction: column; gap: 0; }
.log-entry {
  display: flex; gap: 16px; padding: 16px 0;
  border-bottom: 1px solid var(--border-light);
}
.log-entry:last-child { border-bottom: none; padding-bottom: 0; }
.log-week {
  font-family: var(--font-mono); font-size: 0.68rem; font-weight: 700;
  color: var(--primary); background: var(--primary-light);
  padding: 4px 10px; border-radius: 8px;
  height: fit-content; white-space: nowrap; flex-shrink: 0; margin-top: 2px;
}
.log-title { font-weight: 700; font-size: 0.88rem; color: var(--text); margin-bottom: 4px; }
.log-desc { font-size: 0.8rem; color: var(--text-muted); line-height: 1.6; }
.log-tags { display: flex; gap: 6px; margin-top: 8px; flex-wrap: wrap; }
.log-tag {
  font-size: 0.65rem; padding: 2px 8px; border-radius: 8px;
  background: var(--border-light); color: var(--text-muted);
  font-family: var(--font-mono);
}
```

---

### 5.7 Resource List

```html
<div class="resource-list">
  <div class="resource-item">
    <span class="resource-icon">📄</span>
    <div>
      <div class="resource-title">Resource Title</div>
      <div class="resource-desc">Short description of what this resource is and why it matters.</div>
      <span class="resource-tag">Free</span>
    </div>
  </div>
</div>
```

**Resource CSS:**
```css
.resource-list { display: flex; flex-direction: column; gap: 12px; }
.resource-item {
  display: flex; align-items: flex-start; gap: 14px;
  padding: 14px 16px; background: var(--bg);
  border-radius: 10px; border: 1px solid var(--border-light);
}
.resource-icon { font-size: 1.4rem; flex-shrink: 0; margin-top: 2px; }
.resource-title { font-weight: 700; font-size: 0.88rem; margin-bottom: 3px; }
.resource-desc { font-size: 0.78rem; color: var(--text-muted); line-height: 1.6; }
.resource-tag {
  display: inline-block; font-family: var(--font-mono); font-size: 0.62rem;
  padding: 2px 8px; background: var(--primary-light); color: var(--primary);
  border-radius: 8px; margin-top: 6px;
}
```

---

### 5.8 Tool Grid

```html
<div class="tool-grid">
  <div class="tool-card">
    <span class="tool-emoji">🎨</span>
    <div class="tool-name">Canva</div>
    <div class="tool-desc">Quick graphics, thumbnails, and social posts</div>
    <span class="tool-badge free">Free tier</span>
  </div>
  <div class="tool-card">
    <span class="tool-emoji">✂️</span>
    <div class="tool-name">CapCut</div>
    <div class="tool-desc">Video editing on mobile and desktop</div>
    <span class="tool-badge free">Free</span>
  </div>
</div>
```

**Tool grid CSS:**
```css
.tool-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(180px, 1fr)); gap: 12px; }
.tool-card {
  background: var(--bg); border: 1.5px solid var(--border);
  border-radius: 12px; padding: 16px 14px; text-align: center;
}
.tool-emoji { font-size: 1.8rem; margin-bottom: 8px; display: block; }
.tool-name { font-weight: 700; font-size: 0.82rem; margin-bottom: 4px; }
.tool-desc { font-size: 0.72rem; color: var(--text-muted); line-height: 1.5; }
.tool-badge {
  display: inline-block; font-family: var(--font-mono); font-size: 0.6rem;
  padding: 2px 7px; border-radius: 8px; margin-top: 6px;
}
.tool-badge.free { background: var(--primary-light); color: var(--primary); }
.tool-badge.paid { background: #FDF6E3; color: #8A6010; }
```

---

### 5.9 Breadcrumb

Used on all Type 2 sub-pages. Sits between the nav and the hero.

```html
<div class="breadcrumb">
  <a href="/dewmonday/">Home</a>
  <span class="breadcrumb-sep">›</span>
  <a href="/dewmonday/concepts/art-dropshipping/">Art Drops</a>
  <span class="breadcrumb-sep">›</span>
  <span>Spotlight 001 — Solitude Series</span>
</div>
```

**Breadcrumb CSS:**
```css
.breadcrumb {
  background: var(--primary-light); border-bottom: 1px solid var(--border);
  padding: 12px 48px; display: flex; align-items: center; gap: 8px;
  font-size: 0.8rem; color: var(--text-muted); flex-wrap: wrap;
}
.breadcrumb a { color: var(--primary); text-decoration: none; font-weight: 500; }
.breadcrumb a:hover { text-decoration: underline; }
.breadcrumb-sep { color: var(--border); }
```

---

### 5.10 Article + Sidebar Layout

Used on all Type 2 sub-pages. The sidebar is sticky on desktop, stacks above the article on mobile.

```html
<div class="layout">
  <article class="article">
    <!-- Long-form content: h2 headings, paragraphs, piece grids, gear cards, pull quotes -->
    <h2>About the Work</h2>
    <p>Editorial text goes here…</p>
    <hr class="divider">
    <h2>The Pieces</h2>
    <!-- piece-grid or gear-card components -->
  </article>

  <aside class="sidebar">
    <!-- sidebar-card components — see § 5.17 -->
  </aside>
</div>
```

**Layout CSS:**
```css
.layout {
  display: grid; grid-template-columns: 1fr 300px;
  gap: 48px; max-width: 1100px; margin: 0 auto; padding: 56px 48px;
  align-items: start;
}
@media (max-width: 860px) {
  .layout { grid-template-columns: 1fr; }
  .sidebar { order: -1; }
}
.article h2 {
  font-family: var(--font-display); font-size: 1.7rem;
  color: var(--primary-dark); margin: 40px 0 12px;
}
.article h2:first-child { margin-top: 0; }
.article p { font-size: 0.97rem; color: var(--text); line-height: 1.78; margin-bottom: 14px; }
.article strong { color: var(--primary-dark); }
.divider { height: 1px; background: var(--border-light); margin: 32px 0; border: none; }
```

---

### 5.11 Artist Card

Used on Art Drops spotlight pages.

```html
<div class="artist-card">
  <div class="artist-card-label">Artist Profile</div>
  <div class="artist-card-name">Mara Voss</div>
  <div class="artist-card-handle">@maravoss.art</div>
  <div class="artist-card-body">
    Mara is a Berlin-based oil pastel and digital artist. Her work centers on quiet domestic spaces and the emotional residue they hold.
  </div>
  <div class="artist-card-quote">"I'm not painting rooms. I'm painting what it felt like to be in them."</div>
</div>
```

**Artist card CSS:**
```css
.artist-card {
  background: var(--bg-white); border: 1.5px solid var(--border);
  border-radius: var(--radius); padding: 24px; margin-bottom: 28px; box-shadow: var(--shadow);
}
.artist-card-label {
  font-family: var(--font-mono); font-size: 0.68rem; text-transform: uppercase;
  letter-spacing: 0.12em; color: var(--primary); margin-bottom: 10px;
}
.artist-card-name { font-family: var(--font-display); font-size: 1.3rem; color: var(--primary-dark); margin-bottom: 4px; }
.artist-card-handle { font-family: var(--font-mono); font-size: 0.78rem; color: var(--text-muted); margin-bottom: 14px; }
.artist-card-body { font-size: 0.88rem; color: var(--text); line-height: 1.7; }
.artist-card-quote {
  font-family: var(--font-display); font-style: italic;
  color: var(--primary); margin-top: 14px; padding-top: 14px;
  border-top: 1px solid var(--border-light); font-size: 0.95rem; line-height: 1.5;
}
```

---

### 5.12 Piece Grid

Used on Art Drops spotlight pages for individual artworks.

```html
<div class="piece-grid">
  <div class="piece-card">
    <div class="piece-emoji">🖼️</div>
    <div class="piece-name">The Reading Chair</div>
    <p class="piece-desc">Oil pastel on toned paper. A single armchair in afternoon light — no occupant, just the impression of one.</p>
    <div class="piece-specs">
      <span class="piece-spec">Oil Pastel</span>
      <span class="piece-spec">A3</span>
      <span class="piece-spec">£220</span>
    </div>
  </div>
</div>
```

**Piece grid CSS:**
```css
.piece-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 16px; margin: 24px 0; }
@media (max-width: 600px) { .piece-grid { grid-template-columns: 1fr; } }
.piece-card {
  background: var(--bg-white); border: 1.5px solid var(--border);
  border-radius: var(--radius); padding: 20px;
  transition: box-shadow 0.2s, transform 0.2s;
}
.piece-card:hover { box-shadow: 0 8px 32px rgba(0,0,0,0.1); transform: translateY(-2px); }
.piece-emoji { font-size: 1.8rem; margin-bottom: 10px; }
.piece-name { font-family: var(--font-display); font-size: 1.1rem; color: var(--primary-dark); margin-bottom: 6px; }
.piece-desc { font-size: 0.84rem; color: var(--text); line-height: 1.65; margin-bottom: 10px; }
.piece-specs { display: flex; flex-wrap: wrap; gap: 5px; }
.piece-spec {
  font-family: var(--font-mono); font-size: 0.68rem;
  padding: 2px 8px; border-radius: 6px;
  background: var(--primary-light); color: var(--primary);
}
```

---

### 5.13 Gear Card

Used on Camera Drops kit pages. Each card represents one piece of gear.

```html
<div class="gear-card">
  <div class="gear-card-top">
    <div class="gear-card-left">
      <span class="gear-emoji">🎙️</span>
      <div>
        <div class="gear-name">Blue Yeti USB Microphone</div>
        <div class="gear-type">Condenser Mic · USB</div>
      </div>
    </div>
    <div>
      <div class="gear-price">$129</div>
      <div class="gear-price-note">approx. retail</div>
    </div>
  </div>
  <div class="gear-specs">
    <span class="gear-spec">Plug-and-play</span>
    <span class="gear-spec">4 polar patterns</span>
    <span class="gear-spec">Gain control</span>
  </div>
  <p class="gear-desc">The most recommended beginner USB mic for a reason. Works on Mac and PC with zero driver setup.</p>
  <div class="gear-why">
    <div class="gear-why-label">Why this one</div>
    No setup friction. Sounds good enough to be taken seriously from day one.
  </div>
</div>
```

**Gear card CSS:**
```css
.gear-card {
  background: var(--bg-white); border: 1.5px solid var(--border);
  border-radius: var(--radius); padding: 24px 28px; margin-bottom: 20px;
  box-shadow: var(--shadow); transition: box-shadow 0.2s, transform 0.2s;
}
.gear-card:hover { box-shadow: 0 8px 32px rgba(0,0,0,0.12); transform: translateY(-2px); }
.gear-card-top { display: flex; align-items: flex-start; justify-content: space-between; gap: 16px; margin-bottom: 14px; flex-wrap: wrap; }
.gear-card-left { display: flex; align-items: center; gap: 14px; }
.gear-emoji { font-size: 2rem; }
.gear-name { font-family: var(--font-display); font-size: 1.25rem; color: var(--primary-dark); }
.gear-type { font-family: var(--font-mono); font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.1em; color: var(--text-muted); margin-top: 2px; }
.gear-price { font-family: var(--font-display); font-size: 1.5rem; color: var(--primary); white-space: nowrap; }
.gear-price-note { font-size: 0.72rem; font-family: var(--font-mono); color: var(--text-muted); }
.gear-specs { display: flex; flex-wrap: wrap; gap: 6px; margin-bottom: 12px; }
.gear-spec {
  font-family: var(--font-mono); font-size: 0.7rem;
  padding: 3px 9px; border-radius: 6px;
  background: var(--primary-light); color: var(--primary-dark); font-weight: 500;
}
.gear-desc { font-size: 0.88rem; color: var(--text-muted); line-height: 1.65; margin-bottom: 14px; }
.gear-why {
  background: var(--accent-light); border-left: 3px solid var(--accent);
  border-radius: 0 10px 10px 0; padding: 12px 16px;
  font-size: 0.86rem; color: var(--primary-dark);
}
.gear-why-label {
  font-family: var(--font-mono); font-size: 0.65rem;
  text-transform: uppercase; letter-spacing: 0.1em;
  color: var(--accent); margin-bottom: 4px;
}
```

---

### 5.14 Pull Quote

```html
<blockquote class="pull-quote">
  "The work is about what's left in a room after someone leaves."
</blockquote>
```

```css
.pull-quote {
  font-family: var(--font-display); font-style: italic; font-size: 1.2rem;
  color: var(--primary); border-left: 3px solid var(--accent);
  padding: 14px 20px; margin: 28px 0;
  background: var(--primary-light);
  border-radius: 0 var(--radius) var(--radius) 0;
  line-height: 1.45;
}
```

---

### 5.15 Editorial Callout

```html
<div class="editorial">
  <div class="editorial-label">Editor's Note</div>
  <div class="editorial-title">Why I picked this artist</div>
  <ul>
    <li>Work that makes you slow down and actually look</li>
    <li>Prices that don't require a second mortgage</li>
    <li>An active practice — she's making new work constantly</li>
  </ul>
</div>
```

```css
.editorial {
  background: var(--accent-light); border: 1.5px solid var(--border);
  border-radius: var(--radius); padding: 24px; margin: 28px 0;
}
.editorial-label {
  font-family: var(--font-mono); font-size: 0.68rem; text-transform: uppercase;
  letter-spacing: 0.12em; color: var(--accent); margin-bottom: 10px;
}
.editorial-title { font-family: var(--font-display); font-size: 1.1rem; color: var(--primary-dark); margin-bottom: 10px; }
.editorial ul { padding-left: 18px; }
.editorial li { font-size: 0.88rem; margin-bottom: 7px; color: var(--text); }
```

---

### 5.16 Notice Box

```html
<div class="notice">
  <span class="notice-icon">ℹ️</span>
  <span>All purchase links go directly to the artist's own shop. Dew Monday takes no commission and processes no payments.</span>
</div>
```

```css
.notice {
  background: var(--accent-light); border: 1px solid var(--border);
  border-radius: var(--radius); padding: 16px 20px;
  font-size: 0.85rem; color: var(--primary-dark); margin: 24px 0;
  display: flex; gap: 10px;
}
.notice-icon { font-size: 1rem; flex-shrink: 0; margin-top: 1px; }
```

---

### 5.17 Sidebar Cards & Series Nav

Used in the Article + Sidebar layout (Type 2 pages). The sidebar stacks vertically; each card is its own component. The series nav card has an inverted dark style.

```html
<aside class="sidebar">
  <!-- Metadata card -->
  <div class="sidebar-card">
    <div class="sidebar-card-label">Issue</div>
    <div class="sidebar-card-title">Spotlight 001</div>
  </div>

  <!-- Quick links card -->
  <div class="sidebar-card">
    <div class="sidebar-card-label">Quick Links</div>
    <div class="sidebar-links">
      <a href="https://maravoss.art" class="sidebar-link-item" target="_blank">
        Artist's shop
        <span class="arrow">→</span>
      </a>
      <a href="#pieces" class="sidebar-link-item">
        See the pieces
        <span class="arrow">↓</span>
      </a>
    </div>
  </div>

  <!-- Series navigation (dark card) -->
  <div class="series-nav-card">
    <div class="series-nav-label">Art Drops Series</div>
    <div class="series-nav-title">Next: Portrait Studies</div>
    <div class="series-nav-sub">Spotlight 002 — coming soon</div>
    <a href="/dewmonday/concepts/art-dropshipping/" class="series-nav-btn">Back to Art Drops</a>
  </div>
</aside>
```

**Sidebar CSS:**
```css
.sidebar { display: flex; flex-direction: column; gap: 16px; position: sticky; top: 88px; }
.sidebar-card {
  background: var(--bg-white); border: 1.5px solid var(--border);
  border-radius: var(--radius); padding: 20px; box-shadow: var(--shadow);
}
.sidebar-card-label {
  font-family: var(--font-mono); font-size: 0.68rem; text-transform: uppercase;
  letter-spacing: 0.1em; color: var(--text-muted); margin-bottom: 12px;
}
.sidebar-card-title { font-family: var(--font-display); font-size: 1rem; color: var(--primary-dark); margin-bottom: 6px; }
.sidebar-links { display: flex; flex-direction: column; gap: 6px; }
.sidebar-link-item {
  display: flex; align-items: center; justify-content: space-between;
  padding: 9px 12px; border-radius: 9px;
  background: var(--bg); border: 1px solid var(--border-light);
  text-decoration: none; color: var(--text); font-size: 0.84rem; font-weight: 500;
  transition: background 0.15s, border-color 0.15s;
}
.sidebar-link-item:hover { background: var(--primary-light); border-color: var(--border); }
.sidebar-link-item .arrow { color: var(--text-muted); font-size: 0.8rem; }

.series-nav-card { background: var(--primary-dark); border-radius: var(--radius); padding: 20px; }
.series-nav-label {
  font-family: var(--font-mono); font-size: 0.68rem; text-transform: uppercase;
  letter-spacing: 0.1em; color: rgba(255,255,255,0.5); margin-bottom: 10px;
}
.series-nav-title { font-family: var(--font-display); font-size: 1.05rem; color: #fff; margin-bottom: 4px; }
.series-nav-sub { font-size: 0.8rem; color: rgba(255,255,255,0.6); margin-bottom: 14px; }
.series-nav-btn {
  display: block; text-align: center; background: var(--accent); color: #fff;
  text-decoration: none; font-size: 0.82rem; font-weight: 600;
  padding: 9px 0; border-radius: 8px; transition: opacity 0.15s;
}
.series-nav-btn:hover { opacity: 0.88; }
```

---

### 5.18 Bottom CTA

Every page ends with this section, linked to `/signup/`.

```html
<section class="bottom-cta">
  <div class="bottom-cta-inner">
    <div class="bottom-cta-badge">Free · Every Monday</div>
    <h2>Follow the build <em>every week</em></h2>
    <p>Get the honest version — what's working, what failed, and what's next across all six concepts.</p>
    <div class="bottom-cta-actions">
      <a href="/dewmonday/signup/" class="cta-btn-primary">Get early access →</a>
      <a href="/dewmonday/" class="cta-btn-ghost">See all concepts</a>
    </div>
  </div>
</section>
```

**Bottom CTA CSS:**
```css
.bottom-cta {
  background: linear-gradient(135deg, var(--primary-dark), var(--primary));
  padding: 80px 48px; text-align: center;
}
.bottom-cta-inner { max-width: 640px; margin: 0 auto; }
.bottom-cta-badge {
  display: inline-block; font-family: var(--font-mono); font-size: 0.68rem;
  font-weight: 700; letter-spacing: 0.12em; text-transform: uppercase;
  padding: 5px 14px; border-radius: 999px;
  background: rgba(255,255,255,0.12); color: rgba(255,255,255,0.7);
  border: 1px solid rgba(255,255,255,0.2); margin-bottom: 20px;
}
.bottom-cta h2 { font-family: var(--font-display); font-size: 2.6rem; color: #fff; margin-bottom: 14px; line-height: 1.12; }
.bottom-cta h2 em { font-style: italic; color: rgba(255,255,255,0.65); }
.bottom-cta p { color: rgba(255,255,255,0.68); font-size: 0.95rem; margin-bottom: 32px; line-height: 1.65; }
.bottom-cta-actions { display: flex; gap: 12px; justify-content: center; flex-wrap: wrap; }
.cta-btn-primary {
  padding: 13px 28px; background: #fff; color: var(--primary-dark);
  border-radius: 12px; font-weight: 700; font-size: 0.9rem; text-decoration: none;
  transition: transform 0.15s, box-shadow 0.15s;
}
.cta-btn-primary:hover { transform: translateY(-2px); box-shadow: 0 6px 20px rgba(0,0,0,0.2); }
.cta-btn-ghost {
  padding: 12px 24px; border: 1.5px solid rgba(255,255,255,0.3);
  color: rgba(255,255,255,0.85); border-radius: 12px;
  font-weight: 600; font-size: 0.9rem; text-decoration: none;
  transition: background 0.15s;
}
.cta-btn-ghost:hover { background: rgba(255,255,255,0.1); }
```

---

### 5.19 Footer

```html
<footer>
  <a href="/dewmonday/" class="footer-logo">Dew<span>Monday</span></a>
  <div class="footer-links">
    <a href="/dewmonday/concepts/creator-hub/">Creator Hub</a>
    <a href="/dewmonday/concepts/art-dropshipping/">Art Drops</a>
    <a href="/dewmonday/concepts/camera-dropshipping/">Camera Drops</a>
    <a href="/dewmonday/concepts/little-makers/">Little Makers</a>
    <a href="/dewmonday/concepts/tutorial-app/">Tutorial App</a>
    <a href="/dewmonday/concepts/art-tutorial-app/">Art Tutorial App</a>
    <a href="/dewmonday/signup/">Subscribe</a>
  </div>
  <p class="footer-copy">© 2026 Dew Monday · Built in public</p>
</footer>
```

**Footer CSS:**
```css
footer {
  background: var(--primary-dark); padding: 40px 48px;
  display: flex; flex-wrap: wrap; align-items: center;
  justify-content: space-between; gap: 20px;
}
.footer-logo { font-family: var(--font-display); font-size: 1.1rem; color: rgba(255,255,255,0.75); text-decoration: none; }
.footer-logo span { color: var(--accent); }
.footer-links { display: flex; gap: 24px; flex-wrap: wrap; }
.footer-links a { font-size: 0.78rem; color: rgba(255,255,255,0.4); text-decoration: none; transition: color 0.15s; }
.footer-links a:hover { color: rgba(255,255,255,0.8); }
.footer-copy { font-family: var(--font-mono); font-size: 0.65rem; color: rgba(255,255,255,0.22); }
```

---

## 6. Interactive Modules (JavaScript)

All JavaScript is vanilla. No libraries. Paste each block once per page, just before `</body>`.

### 6.1 Nav Dropdown Toggle

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

### 6.2 Filter Chips (Content Grid)

Wire to `data-cat` on each card. The active chip gets the `.active` class; other cards are hidden.

```javascript
<script>
function filterContent(cat, btn) {
  document.querySelectorAll('.filter-chip').forEach(c => c.classList.remove('active'));
  btn.classList.add('active');
  document.querySelectorAll('[data-cat]').forEach(card => {
    card.classList.toggle('hidden', cat !== 'all' && card.dataset.cat !== cat);
  });
}
</script>
```

### 6.3 Accordion Toggle (Alternative JS version)

The simplest pattern uses an inline `onclick` directly on the trigger button (see § 5.5). If you prefer a single listener:

```javascript
<script>
document.querySelectorAll('.accordion-trigger').forEach(trigger => {
  trigger.addEventListener('click', () => {
    trigger.closest('.accordion').classList.toggle('open');
  });
});
</script>
```

### 6.4 Sticky Controls Bar Offset (Activities / Utility Pages)

When a page has both a sticky nav AND a sticky controls bar, offset the second bar's `top` to equal the nav height:

```css
.controls-bar {
  position: sticky;
  top: 64px; /* matches nav height */
  z-index: 90;
}
```

---

## 7. Jekyll URL Rules

The site lives at the subpath `/dewmonday/`. All internal links must account for this.

**Option A — Liquid filter (preferred, processes at build time):**
```html
<a href="{{ '/concepts/creator-hub/' | relative_url }}">Creator Hub</a>
```

**Option B — Hardcoded prefix (for sub-pages where Liquid may not fully process):**
```html
<a href="/dewmonday/concepts/creator-hub/">Creator Hub</a>
```

**Never use bare paths like `/concepts/creator-hub/`** — they will 404 in production.

**Font preconnect must always come before the font `<link>` tag:**
```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?…" rel="stylesheet">
```

---

## 8. Deployment Workflow

```bash
# Standard page change or content update
git add -A
git commit -m "feat: brief description of what changed"
git push
```

GitHub Actions triggers a Jekyll build automatically. Live at `https://raiin-boop.github.io/dewmonday/` in ~60 seconds.

**If a page 404s after deploy:**
1. Check `permalink:` in the file's front matter
2. Confirm the file is `index.html` inside a concept folder, not a flat `.html` at root (except `signup.html` and `index.html`)
3. Confirm `layout: none` is set — missing it wraps the page in the legacy default layout and breaks standalone pages
4. Verify all internal links use `| relative_url` or the `/dewmonday/` prefix

**`_config.yml` — do not modify unless:**
- Adding a new Jekyll collection
- Changing `baseurl` (currently `/dewmonday`)
- Modifying global permalink structure

---

## 9. Agent Instructions — Replicate This Design in Any Repo

> **For AI agents, Copilot, and any automated assistant:** This section gives you everything you need to clone this exact design system into a brand-new project for any industry — food, fitness, SaaS, education, retail, or anything else — without access to the original Dew Monday files.

---

### 9.1 What You Are Replicating

This design system is built on six principles. Never violate them, regardless of industry:

| Principle | What it means |
|-----------|---------------|
| **Standalone HTML** | Every page is one self-contained `.html` file. No shared CSS files, no `_includes`, no JS imports. |
| **Inline everything** | All `<style>` and `<script>` tags live inside the same file as the HTML. |
| **CSS custom properties** | Every value that varies between sections (color, spacing, type) is a CSS variable in `:root`. Never hardcode a brand color directly in a selector. |
| **Three-font system** | Display serif (headings), humanist sans (body), monospace (labels). Always all three. Never fewer. |
| **Glassmorphism nav** | Sticky, `backdrop-filter: blur()`, dual dropdown, close on outside click. |
| **Gradient heroes** | Every page opens with a full-bleed gradient hero — dark-to-mid using `--primary-dark` → `--primary`. |

---

### 9.2 Industry Substitution Map

Every Dew Monday concept maps directly to a generic equivalent. Use this table to translate when building for a different industry.

| Dew Monday term | Generic equivalent | Example (SaaS) | Example (Food) | Example (Fitness) |
|---|---|---|---|---|
| "Concept" | Section / Product line / Category | Feature area | Menu section | Training program |
| "Issue" | Entry / Post / Item | Changelog entry | Recipe | Workout |
| "Spotlight" | Detail / Feature / Profile | Case study | Chef profile | Athlete profile |
| "Drop" | Release / Launch / Edition | Version release | Seasonal menu | Monthly challenge |
| "Creator Hub" | Home / Dashboard section | Product overview | Brand story | Community hub |
| "Art Drops" | Content showcase | Feature highlights | Recipe collection | Workout library |
| "Camera Drops" | Product / Gear / Tools | Integrations list | Equipment guide | Gear reviews |
| "Little Makers" | Beginner / Starter section | Getting started | Cooking basics | Beginner plans |
| "Build log" | Changelog / Progress log | Release notes | Development journal | Training diary |
| "Subscribe free →" | Primary CTA | Start free trial | Join the list | Get the plan |

---

### 9.3 Step-by-Step: Build a New Site With This Design

Follow these steps in order. Do not skip steps or reorder them.

#### Step 1 — Define Your Color Palette

Choose one primary color per major section of your site. Each section gets its own `:root` theme. Rules:

- **`--primary`**: A rich mid-tone (the main brand color for this section). Examples: deep teal, burnt orange, indigo, forest green.
- **`--primary-dark`**: 15–25% darker than `--primary`. Used for hero gradient start and footer background.
- **`--primary-light`**: A very pale tint of `--primary` (5–10% saturation). Used for chip fills, hover states, active nav items.
- **`--accent`**: A contrasting secondary color. Should be from a different hue family than `--primary`.
- **`--bg`**: Off-white with a very faint warm or cool tint (never pure `#FFFFFF`).
- **`--border`**: A muted mid-tone 20–25% darker than `--bg`.

**Minimum viable palette per section:**
```css
:root {
  --bg: #F5F2EC;
  --bg-white: #FFFFFF;
  --primary: /* your color */;
  --primary-dark: /* 20% darker */;
  --primary-light: /* 90% lighter tint */;
  --accent: /* contrasting hue */;
  --text: #1C1C1C;
  --text-muted: #6B6B6B;
  --border: /* muted mid-tone */;
  --border-light: /* very light */;
  --font-display: 'DM Serif Display', serif;
  --font-body: 'Inter', sans-serif;
  --font-mono: 'JetBrains Mono', monospace;
  --radius: 14px;
  --shadow: 0 4px 24px rgba(0, 0, 0, 0.08);
}
```

#### Step 2 — Set Up Jekyll (or Static Site)

```yaml
# _config.yml minimum viable config
remote_theme: just-the-docs/just-the-docs@v0.10.0   # or omit if not using JTD
title: "Your Site Name"
baseurl: "/your-repo-name"
url: "https://your-username.github.io"
exclude:
  - "*.sh"
  - Gemfile
  - vendor/
plugins:
  - jekyll-seo-tag
```

> **If not using Jekyll:** any static site host works. Replace `{{ '/path/' | relative_url }}` with hardcoded absolute paths (`/your-repo-name/path/`).

#### Step 3 — Create Your File Structure

```
your-repo/
├── index.html                    ← Homepage (always Type 1)
├── signup.html                   ← Signup / contact utility page
├── brand/
│   └── index.html                ← About / brand reference (Type 3)
├── sections/                     ← Rename from "concepts/" to fit your domain
│   ├── section-one/
│   │   ├── index.html            ← Section hub (Type 1)
│   │   └── items/
│   │       └── 001-first-item/
│   │           └── index.html    ← Item detail page (Type 2)
│   └── section-two/
│       └── index.html
└── _config.yml
```

**Front matter for every standalone page:**
```yaml
---
layout: none
permalink: /sections/section-one/
---
```

#### Step 4 — Build the Nav (Do This First, Once)

The nav is the most complex component. Build it correctly once, then copy-paste to every page.

**Checklist before you copy the nav to any page:**
- [ ] Both dropdowns present: primary navigation dropdown AND secondary (brand/about) dropdown
- [ ] `toggleDD()` JS function present at bottom of file
- [ ] Outside-click-closes listener present
- [ ] Correct item marked `.active` for the current page
- [ ] All links use `/your-repo-name/` prefix or `| relative_url` filter
- [ ] Logo text uses `--font-display`, accent span uses `--accent` color

**Adapting the Concepts dropdown to your domain:**

Replace every `<a class="nav-menu-item">` entry with your own sections. The structure is always:
```html
<a href="/your-repo/section/name/" class="nav-menu-item">
  <span class="nav-menu-emoji">EMOJI</span>
  <div>
    <div class="nav-menu-title">Section Name</div>
    <div class="nav-menu-desc">One-line description</div>
  </div>
</a>
```

**Adapting the Brand/About dropdown:**

Use anchor links to sections within your `/brand/` or `/about/` page:
```html
<a href="/your-repo/brand/#section-id" class="nav-menu-item">…</a>
```

#### Step 5 — Build Each Page Type

**For every Type 1 (Hub) page, in order:**
```
1. <head> with Google Fonts + inline <style> containing full :root + all component CSS
2. <nav> — dual dropdown, correct .active item
3. <section class="hero"> — gradient, badge, h1, subtext, stat row
4. <div class="content"> wrapping:
   a. Filter bar (if content is filterable)
   b. Content grid (cards, items, entries)
   c. At least one accordion section
5. Bottom CTA → /your-repo/signup/
6. <footer>
7. <script> blocks: toggleDD, filterContent, accordion listeners
```

**For every Type 2 (Detail) page, in order:**
```
1. <head> — same :root colors as parent section
2. <nav> — parent section marked .active
3. <div class="breadcrumb"> — Home › Parent Section › Page Title
4. <section class="hero"> — same gradient as parent section
5. <div class="layout"> grid containing:
   a. <article class="article"> — editorial long-form content
   b. <aside class="sidebar"> — metadata cards, quick links, series nav
6. Bottom CTA
7. <footer>
8. <script> blocks: toggleDD
```

**For the Type 3 (Brand/About) page:**
```
1. <head> — use your primary/default color theme
2. <nav>
3. <section class="hero">
4. <div class="page-layout"> two-column grid:
   a. Left: sticky sidebar with anchor links to each section
   b. Right: accordion sections, each with an id anchor
5. Bottom CTA
6. <footer>
7. <script> blocks: toggleDD, accordion listeners, scroll-spy (optional)
```

#### Step 6 — Adapt Content to Your Industry

Replace Dew Monday-specific content with your own while keeping the **component structure identical**:

| Dew Monday component | Replace content with |
|---|---|
| Hero badge "Building in public · Concept 01" | Your tagline badge, e.g. "New arrivals · Season 3" or "Free tool · Version 2" |
| Hero h1 with `<em>` italic span | Your headline. The `<em>` span always gets `color: rgba(255,255,255,0.65)` — use it on the most evocative word |
| Hero stat row | Any 4 numbers relevant to your site: users, items, lessons, recipes, etc. |
| Filter chip labels | Your category names. Keep the same `data-cat` + JS pattern |
| Issue cards → any content cards | Products, recipes, lessons, articles, case studies — same `.issue-card` HTML |
| `Issue NNN` badge inside thumb | Your numbering/labeling system |
| Build log timeline | Changelog, recipe development journal, version history, training log |
| Artist card | Any profile: chef, athlete, contributor, client, team member |
| Piece grid | Any collection of items with name, description, and specs |
| Gear card with "Why this one" callout | Any product review or recommendation with reasoning |
| "Subscribe free →" CTA | Your primary conversion: signup, download, purchase, book |

#### Step 7 — Validate Every Page Before Committing

Run through this checklist for each file:

- [ ] `layout: none` in front matter
- [ ] `permalink:` is set and correct
- [ ] Google Fonts `<link>` tags present (preconnect + stylesheet)
- [ ] `:root` has all required variables (see § 3.2)
- [ ] Colors use correct section theme (see § 3.3 or your custom palette)
- [ ] Dual-dropdown nav present (primary + secondary dropdown)
- [ ] Correct item marked `.active` in the primary dropdown
- [ ] All internal links use site prefix or `| relative_url`
- [ ] Hero section has: badge, h1, subtext, CTA buttons, stat row
- [ ] Bottom CTA links to `/your-repo/signup/` (or your equivalent)
- [ ] Footer includes links to all major sections
- [ ] `toggleDD()` JS is present exactly once per file
- [ ] `filterContent()` JS is present if the page has a filter bar
- [ ] No inline `style=""` attributes using hardcoded colors — all colors via CSS vars
- [ ] No `<link rel="stylesheet">` pointing to external CSS files you authored
- [ ] No `<script src="…">` tags for your own JS files — all scripts inline

---

### 9.4 Common Mistakes Agents Make

Avoid these patterns — they break the design:

| Mistake | Why it breaks | Correct approach |
|---------|--------------|-----------------|
| Using `<link rel="stylesheet" href="styles.css">` | External stylesheet defeats standalone architecture | Paste all CSS inline inside `<style>` |
| Hardcoding `#2D5A27` in selectors | Color won't update when theme changes | Always reference `var(--primary)` |
| Using only one dropdown in the nav | Breaks visual symmetry and navigation depth | Always two dropdowns: primary sections + brand/about |
| Omitting the hero's `::before` radial gradient overlay | Hero looks flat | Add the `radial-gradient` pseudo-element for depth |
| Putting `position: relative` on `.sidebar` instead of `sticky` | Sidebar scrolls with page on desktop | Use `position: sticky; top: 88px;` |
| Using `display: none` on accordion body without `.open` toggle | Accordion never opens | The `.accordion.open .accordion-body { display: block; }` rule is required |
| Forgetting the outside-click-closes listener for dropdowns | Dropdown stays open forever | Always include the `document.addEventListener('click', …)` listener |
| Using `href="/sections/name/"` without site prefix | 404 on GitHub Pages subpaths | Always `/your-repo/sections/name/` or `| relative_url` |
| Creating a new CSS file for a shared component | Breaks page independence | Every component's CSS lives inside the page that uses it |
| Writing nav with `display: flex` but no `position: sticky; top: 0` | Nav scrolls away | Nav always needs `position: sticky; top: 0; z-index: 200` |

---

### 9.5 Minimal Viable Page Template

This is the smallest correct implementation of a Type 1 page. Copy it, replace the placeholder text, and build up from here.

```html
---
layout: none
permalink: /your-section/
---
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Section Name · Your Site</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=DM+Serif+Display:ital@0;1&family=Inter:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500;700&display=swap" rel="stylesheet">
  <style>
    :root {
      --bg: #F5F2EC; --bg-white: #FFFFFF;
      --primary: #2D5A27; --primary-dark: #1E3D1A; --primary-light: #E8F0E7;
      --accent: #6BA3BE; --accent-light: #E8F2F8;
      --text: #1C1C1C; --text-muted: #6B6B6B;
      --border: #D8D4C8; --border-light: #EAE6DC;
      --font-display: 'DM Serif Display', serif;
      --font-body: 'Inter', sans-serif;
      --font-mono: 'JetBrains Mono', monospace;
      --radius: 14px; --shadow: 0 4px 24px rgba(0,0,0,0.08);
    }
    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
    html { scroll-behavior: smooth; }
    body { font-family: var(--font-body); background: var(--bg); color: var(--text); line-height: 1.6; }

    /* === NAV === */
    .nav { position: sticky; top: 0; z-index: 200; background: rgba(255,255,255,0.96); backdrop-filter: blur(12px); border-bottom: 1px solid var(--border); display: flex; align-items: center; justify-content: space-between; padding: 0 48px; height: 68px; box-shadow: 0 1px 12px rgba(0,0,0,0.07); }
    .nav-left { display: flex; align-items: center; gap: 32px; }
    .nav-logo { font-family: var(--font-display); font-size: 1.3rem; color: var(--primary-dark); text-decoration: none; }
    .nav-logo span { color: var(--accent); }
    .nav-dropdown { position: relative; }
    .nav-dropdown-trigger { display: flex; align-items: center; gap: 6px; font-size: 0.85rem; font-weight: 600; color: var(--text); background: none; border: none; cursor: pointer; padding: 6px 10px; border-radius: 8px; transition: background 0.15s, color 0.15s; }
    .nav-dropdown-trigger:hover, .nav-dropdown.open .nav-dropdown-trigger { background: var(--primary-light); color: var(--primary); }
    .nav-dropdown-trigger .chevron { width: 14px; height: 14px; transition: transform 0.2s; }
    .nav-dropdown.open .chevron { transform: rotate(180deg); }
    .nav-dropdown-menu { display: none; position: absolute; top: calc(100% + 8px); left: 0; background: #fff; border: 1.5px solid var(--border); border-radius: 16px; padding: 8px; min-width: 290px; box-shadow: 0 12px 40px rgba(0,0,0,0.13); animation: menuIn 0.18s ease; z-index: 300; }
    .nav-dropdown.open .nav-dropdown-menu { display: block; }
    @keyframes menuIn { from { opacity: 0; transform: translateY(-6px); } to { opacity: 1; transform: translateY(0); } }
    .nav-menu-item { display: flex; align-items: center; gap: 12px; padding: 10px 12px; border-radius: 10px; text-decoration: none; color: var(--text); transition: background 0.15s; }
    .nav-menu-item:hover { background: var(--primary-light); }
    .nav-menu-item.active { background: var(--primary-light); color: var(--primary); }
    .nav-menu-emoji { font-size: 1.1rem; width: 24px; text-align: center; }
    .nav-menu-title { font-size: 0.85rem; font-weight: 600; line-height: 1.2; }
    .nav-menu-desc { font-size: 0.75rem; color: var(--text-muted); }
    .nav-menu-divider { height: 1px; background: var(--border-light); margin: 4px 0; }
    .nav-right { display: flex; align-items: center; gap: 14px; }
    .nav-home-link { font-size: 0.85rem; color: var(--text-muted); text-decoration: none; transition: color 0.15s; }
    .nav-home-link:hover { color: var(--primary); }
    .nav-subscribe-btn { padding: 8px 18px; background: var(--primary); color: #fff; border-radius: 20px; font-size: 0.82rem; font-weight: 700; text-decoration: none; transition: background 0.2s, transform 0.15s; }
    .nav-subscribe-btn:hover { background: var(--primary-dark); transform: translateY(-1px); }

    /* === HERO === */
    .hero { background: linear-gradient(135deg, var(--primary-dark) 0%, var(--primary) 60%); padding: 80px 48px 72px; position: relative; overflow: hidden; }
    .hero::before { content: ''; position: absolute; inset: 0; background: radial-gradient(ellipse at 70% 40%, rgba(255,255,255,0.07) 0%, transparent 60%); pointer-events: none; }
    .hero-inner { max-width: 900px; margin: 0 auto; position: relative; z-index: 1; }
    .hero-badge { display: inline-flex; align-items: center; gap: 8px; background: rgba(255,255,255,0.12); border: 1px solid rgba(255,255,255,0.2); padding: 5px 14px; border-radius: 999px; font-family: var(--font-mono); font-size: 0.68rem; letter-spacing: 0.1em; text-transform: uppercase; color: rgba(255,255,255,0.75); margin-bottom: 24px; }
    .hero-badge-dot { width: 6px; height: 6px; border-radius: 50%; background: rgba(255,255,255,0.75); animation: pulse 2s infinite; }
    @keyframes pulse { 0%, 100% { opacity: 1; } 50% { opacity: 0.3; } }
    .hero h1 { font-family: var(--font-display); font-size: 3.6rem; line-height: 1.07; color: #fff; margin-bottom: 18px; max-width: 680px; }
    .hero h1 em { font-style: italic; color: rgba(255,255,255,0.65); }
    .hero-sub { font-size: 1rem; color: rgba(255,255,255,0.72); margin-bottom: 36px; max-width: 520px; line-height: 1.65; }
    .hero-actions { display: flex; gap: 12px; flex-wrap: wrap; margin-bottom: 52px; }
    .hero-btn-primary { padding: 13px 28px; background: #fff; color: var(--primary-dark); border-radius: 12px; font-weight: 700; font-size: 0.92rem; text-decoration: none; box-shadow: 0 4px 18px rgba(0,0,0,0.15); transition: transform 0.15s, box-shadow 0.15s; }
    .hero-btn-primary:hover { transform: translateY(-2px); box-shadow: 0 8px 28px rgba(0,0,0,0.22); }
    .hero-btn-secondary { padding: 12px 24px; border: 1.5px solid rgba(255,255,255,0.3); color: rgba(255,255,255,0.85); border-radius: 12px; font-weight: 600; font-size: 0.92rem; text-decoration: none; transition: background 0.15s; }
    .hero-btn-secondary:hover { background: rgba(255,255,255,0.1); }
    .hero-stats { display: flex; gap: 40px; flex-wrap: wrap; }
    .hero-stat-num { font-family: var(--font-display); font-size: 2.4rem; color: rgba(255,255,255,0.88); display: block; }
    .hero-stat-label { font-family: var(--font-mono); font-size: 0.62rem; text-transform: uppercase; letter-spacing: 0.1em; color: rgba(255,255,255,0.4); }

    /* === CONTENT === */
    .content { max-width: 960px; margin: 0 auto; padding: 0 48px; }
    .section { padding: 56px 0; }
    .section-eyebrow { font-family: var(--font-mono); font-size: 0.7rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.12em; color: var(--primary); margin-bottom: 8px; }
    .section-title { font-family: var(--font-display); font-size: 1.9rem; color: var(--text); margin-bottom: 8px; }
    .section-sub { font-size: 0.9rem; color: var(--text-muted); max-width: 500px; line-height: 1.65; }

    /* === FILTER BAR === */
    .filter-bar { display: flex; gap: 8px; flex-wrap: wrap; margin-bottom: 28px; }
    .filter-chip { padding: 7px 16px; border-radius: 20px; border: 1.5px solid var(--border); background: var(--bg-white); font-size: 0.8rem; font-weight: 500; color: var(--text-muted); cursor: pointer; transition: all 0.18s; font-family: var(--font-body); }
    .filter-chip:hover { border-color: var(--primary); color: var(--primary); }
    .filter-chip.active { background: var(--primary); border-color: var(--primary); color: #fff; }

    /* === CARDS === */
    .content-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(272px, 1fr)); gap: 16px; }
    .card { background: var(--bg-white); border: 1.5px solid var(--border); border-radius: var(--radius); overflow: hidden; transition: transform 0.18s, box-shadow 0.18s; display: flex; flex-direction: column; }
    .card:hover { transform: translateY(-3px); box-shadow: var(--shadow); }
    .card.hidden { display: none; }
    .card-thumb { height: 120px; display: flex; align-items: center; justify-content: center; font-size: 2.8rem; position: relative; }
    .card-num { position: absolute; top: 10px; left: 10px; font-family: var(--font-mono); font-size: 0.62rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.06em; padding: 3px 9px; border-radius: 10px; background: rgba(255,255,255,0.15); color: rgba(255,255,255,0.9); }
    .card-body { padding: 16px 18px; flex: 1; display: flex; flex-direction: column; gap: 6px; }
    .card-tag { font-family: var(--font-mono); font-size: 0.65rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.08em; color: var(--primary); }
    .card-title { font-weight: 700; font-size: 0.95rem; color: var(--text); line-height: 1.35; }
    .card-desc { font-size: 0.78rem; color: var(--text-muted); line-height: 1.55; flex: 1; }
    .card-meta { display: flex; align-items: center; justify-content: space-between; margin-top: 12px; padding-top: 12px; border-top: 1px solid var(--border-light); }
    .card-date { font-family: var(--font-mono); font-size: 0.68rem; color: var(--text-muted); }
    .card-action { font-size: 0.72rem; color: var(--primary); font-weight: 600; text-decoration: none; }

    /* === ACCORDION === */
    .accordion { border: 1.5px solid var(--border); border-radius: var(--radius); overflow: hidden; margin-bottom: 12px; background: var(--bg-white); }
    .accordion-trigger { width: 100%; display: flex; align-items: center; justify-content: space-between; padding: 20px 24px; background: none; border: none; cursor: pointer; text-align: left; transition: background 0.15s; }
    .accordion-trigger:hover { background: var(--primary-light); }
    .accordion.open .accordion-trigger { background: var(--primary-light); border-bottom: 1px solid var(--border); }
    .accordion-trigger-left { display: flex; align-items: center; gap: 14px; }
    .accordion-icon { font-size: 1.3rem; }
    .accordion-label { font-weight: 700; font-size: 0.95rem; color: var(--text); }
    .accordion-sublabel { font-size: 0.75rem; color: var(--text-muted); margin-top: 2px; }
    .accordion-chevron { width: 18px; height: 18px; color: var(--text-muted); transition: transform 0.25s; flex-shrink: 0; }
    .accordion.open .accordion-chevron { transform: rotate(180deg); color: var(--primary); }
    .accordion-body { display: none; padding: 24px; }
    .accordion.open .accordion-body { display: block; }

    /* === BOTTOM CTA === */
    .bottom-cta { background: linear-gradient(135deg, var(--primary-dark), var(--primary)); padding: 80px 48px; text-align: center; }
    .bottom-cta-inner { max-width: 640px; margin: 0 auto; }
    .bottom-cta-badge { display: inline-block; font-family: var(--font-mono); font-size: 0.68rem; font-weight: 700; letter-spacing: 0.12em; text-transform: uppercase; padding: 5px 14px; border-radius: 999px; background: rgba(255,255,255,0.12); color: rgba(255,255,255,0.7); border: 1px solid rgba(255,255,255,0.2); margin-bottom: 20px; }
    .bottom-cta h2 { font-family: var(--font-display); font-size: 2.6rem; color: #fff; margin-bottom: 14px; line-height: 1.12; }
    .bottom-cta h2 em { font-style: italic; color: rgba(255,255,255,0.65); }
    .bottom-cta p { color: rgba(255,255,255,0.68); font-size: 0.95rem; margin-bottom: 32px; line-height: 1.65; }
    .bottom-cta-actions { display: flex; gap: 12px; justify-content: center; flex-wrap: wrap; }
    .cta-btn-primary { padding: 13px 28px; background: #fff; color: var(--primary-dark); border-radius: 12px; font-weight: 700; font-size: 0.9rem; text-decoration: none; transition: transform 0.15s, box-shadow 0.15s; }
    .cta-btn-primary:hover { transform: translateY(-2px); box-shadow: 0 6px 20px rgba(0,0,0,0.2); }
    .cta-btn-ghost { padding: 12px 24px; border: 1.5px solid rgba(255,255,255,0.3); color: rgba(255,255,255,0.85); border-radius: 12px; font-weight: 600; font-size: 0.9rem; text-decoration: none; transition: background 0.15s; }
    .cta-btn-ghost:hover { background: rgba(255,255,255,0.1); }

    /* === FOOTER === */
    footer { background: var(--primary-dark); padding: 40px 48px; display: flex; flex-wrap: wrap; align-items: center; justify-content: space-between; gap: 20px; }
    .footer-logo { font-family: var(--font-display); font-size: 1.1rem; color: rgba(255,255,255,0.75); text-decoration: none; }
    .footer-logo span { color: var(--accent); }
    .footer-links { display: flex; gap: 24px; flex-wrap: wrap; }
    .footer-links a { font-size: 0.78rem; color: rgba(255,255,255,0.4); text-decoration: none; transition: color 0.15s; }
    .footer-links a:hover { color: rgba(255,255,255,0.8); }
    .footer-copy { font-family: var(--font-mono); font-size: 0.65rem; color: rgba(255,255,255,0.22); }

    /* === RESPONSIVE === */
    @media (max-width: 640px) {
      .nav { padding: 0 20px; } .nav-left { gap: 16px; }
      .hero { padding: 56px 24px 52px; } .hero h1 { font-size: 2.3rem; }
      .content { padding: 0 20px; }
      .bottom-cta { padding: 52px 24px; }
      footer { padding: 24px 20px; flex-direction: column; align-items: flex-start; }
    }
  </style>
</head>
<body>

<nav class="nav">
  <div class="nav-left">
    <a href="/your-repo/" class="nav-logo">Your<span>Brand</span></a>

    <div class="nav-dropdown" id="dd-sections">
      <button class="nav-dropdown-trigger" onclick="toggleDD('dd-sections')">
        Sections
        <svg class="chevron" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"/></svg>
      </button>
      <div class="nav-dropdown-menu">
        <a href="/your-repo/sections/section-one/" class="nav-menu-item active">
          <span class="nav-menu-emoji">✨</span>
          <div><div class="nav-menu-title">Section One</div><div class="nav-menu-desc">Short description</div></div>
        </a>
        <a href="/your-repo/sections/section-two/" class="nav-menu-item">
          <span class="nav-menu-emoji">🔥</span>
          <div><div class="nav-menu-title">Section Two</div><div class="nav-menu-desc">Short description</div></div>
        </a>
      </div>
    </div>

    <div class="nav-dropdown" id="dd-about">
      <button class="nav-dropdown-trigger" onclick="toggleDD('dd-about')">
        About
        <svg class="chevron" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"/></svg>
      </button>
      <div class="nav-dropdown-menu">
        <a href="/your-repo/brand/#overview" class="nav-menu-item">
          <span class="nav-menu-emoji">📖</span>
          <div><div class="nav-menu-title">Overview</div><div class="nav-menu-desc">What this is</div></div>
        </a>
        <a href="/your-repo/brand/#mission" class="nav-menu-item">
          <span class="nav-menu-emoji">🎯</span>
          <div><div class="nav-menu-title">Mission</div><div class="nav-menu-desc">Why we built it</div></div>
        </a>
      </div>
    </div>
  </div>
  <div class="nav-right">
    <a href="/your-repo/" class="nav-home-link">Home</a>
    <a href="/your-repo/signup/" class="nav-subscribe-btn">Get started →</a>
  </div>
</nav>

<section class="hero">
  <div class="hero-inner">
    <div class="hero-badge">
      <span class="hero-badge-dot"></span>
      Your tagline badge here
    </div>
    <h1>Your compelling headline with an <em>italic emphasis</em></h1>
    <p class="hero-sub">Supporting text — one or two sentences max. Speak to the reader's situation, not your features.</p>
    <div class="hero-actions">
      <a href="/your-repo/signup/" class="hero-btn-primary">Primary CTA →</a>
      <a href="#content" class="hero-btn-secondary">Secondary CTA ↓</a>
    </div>
    <div class="hero-stats">
      <div><span class="hero-stat-num">4</span><span class="hero-stat-label">Stat label</span></div>
      <div><span class="hero-stat-num">Free</span><span class="hero-stat-label">Stat label</span></div>
      <div><span class="hero-stat-num">100+</span><span class="hero-stat-label">Stat label</span></div>
      <div><span class="hero-stat-num">Weekly</span><span class="hero-stat-label">Stat label</span></div>
    </div>
  </div>
</section>

<div class="content">
  <section class="section" id="content">
    <p class="section-eyebrow">Section Label</p>
    <h2 class="section-title">Section Heading</h2>
    <p class="section-sub">Supporting description for this section of content.</p>

    <div class="filter-bar" style="margin-top: 24px;">
      <button class="filter-chip active" onclick="filterContent('all', this)">All</button>
      <button class="filter-chip" onclick="filterContent('category-a', this)">Category A</button>
      <button class="filter-chip" onclick="filterContent('category-b', this)">Category B</button>
    </div>

    <div class="content-grid">
      <div class="card" data-cat="category-a">
        <div class="card-thumb" style="background: linear-gradient(135deg, var(--primary-dark), var(--primary));">
          ✨<span class="card-num">Item 001</span>
        </div>
        <div class="card-body">
          <div class="card-tag">Category A</div>
          <div class="card-title">Card Title Here</div>
          <div class="card-desc">Short description of this card's content. Keep it to 2–3 sentences.</div>
          <div class="card-meta">
            <span class="card-date">Jul 2026</span>
            <a href="#" class="card-action">View →</a>
          </div>
        </div>
      </div>
    </div>
  </section>

  <section class="section">
    <p class="section-eyebrow">FAQ</p>
    <h2 class="section-title">Common questions</h2>
    <div style="margin-top: 24px;">
      <div class="accordion">
        <button class="accordion-trigger" onclick="this.closest('.accordion').classList.toggle('open')">
          <div class="accordion-trigger-left">
            <span class="accordion-icon">❓</span>
            <div>
              <div class="accordion-label">Question goes here?</div>
              <div class="accordion-sublabel">Brief hint about the answer</div>
            </div>
          </div>
          <svg class="accordion-chevron" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M6 9l6 6 6-6"/></svg>
        </button>
        <div class="accordion-body">
          <p>Answer goes here. Write in first person, keep it honest and direct.</p>
        </div>
      </div>
    </div>
  </section>
</div>

<section class="bottom-cta">
  <div class="bottom-cta-inner">
    <div class="bottom-cta-badge">Free · No spam</div>
    <h2>Your CTA headline with <em>emphasis</em></h2>
    <p>Supporting sentence that reinforces the value of the action you're asking for.</p>
    <div class="bottom-cta-actions">
      <a href="/your-repo/signup/" class="cta-btn-primary">Primary CTA →</a>
      <a href="/your-repo/" class="cta-btn-ghost">Back to home</a>
    </div>
  </div>
</section>

<footer>
  <a href="/your-repo/" class="footer-logo">Your<span>Brand</span></a>
  <div class="footer-links">
    <a href="/your-repo/sections/section-one/">Section One</a>
    <a href="/your-repo/sections/section-two/">Section Two</a>
    <a href="/your-repo/brand/">About</a>
    <a href="/your-repo/signup/">Sign up</a>
  </div>
  <p class="footer-copy">© 2026 Your Brand · Built with care</p>
</footer>

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
function filterContent(cat, btn) {
  document.querySelectorAll('.filter-chip').forEach(c => c.classList.remove('active'));
  btn.classList.add('active');
  document.querySelectorAll('[data-cat]').forEach(card => {
    card.classList.toggle('hidden', cat !== 'all' && card.dataset.cat !== cat);
  });
}
</script>
</body>
</html>
```

---

### 9.6 Quick Industry Color Starter Palettes

Plug any of these directly into your `:root` to get a complete working theme.

**SaaS / Tech — Deep Indigo**
```css
--bg: #F4F3FA; --bg-white: #FFFFFF;
--primary: #4B3FA0; --primary-dark: #2A1F6A; --primary-light: #EEEDF8;
--accent: #7EC8E3; --accent-light: #E8F7FC;
--border: #D4D0E8; --border-light: #E8E6F4;
--shadow: 0 4px 24px rgba(42, 31, 106, 0.09);
```

**Food / Recipe — Warm Terracotta**
```css
--bg: #FAF5F0; --bg-white: #FFFFFF;
--primary: #C05A2A; --primary-dark: #7A2E0A; --primary-light: #FAEDE5;
--accent: #6BA89A; --accent-light: #E6F4F1;
--border: #E8D4C4; --border-light: #F2E8DE;
--shadow: 0 4px 24px rgba(122, 46, 10, 0.09);
```

**Health / Fitness — Deep Teal**
```css
--bg: #EEF8F6; --bg-white: #FFFFFF;
--primary: #1E7A6A; --primary-dark: #0F4A3E; --primary-light: #D8F0EC;
--accent: #F0A040; --accent-light: #FEF4E4;
--border: #BED8D2; --border-light: #D8EDEA;
--shadow: 0 4px 24px rgba(15, 74, 62, 0.09);
```

**Education / Courses — Royal Purple**
```css
--bg: #F5F0FA; --bg-white: #FFFFFF;
--primary: #6B3FA0; --primary-dark: #3A1A60; --primary-light: #EEE8FA;
--accent: #E07A5F; --accent-light: #FAEEE8;
--border: #D4C8E8; --border-light: #EAE4F4;
--shadow: 0 4px 24px rgba(58, 26, 96, 0.09);
```

**Retail / E-commerce — Slate Navy**
```css
--bg: #F0F2F8; --bg-white: #FFFFFF;
--primary: #2A3F7A; --primary-dark: #141E4A; --primary-light: #E0E6F8;
--accent: #E8A030; --accent-light: #FDF4E0;
--border: #C8D0E8; --border-light: #DDE4F4;
--shadow: 0 4px 24px rgba(20, 30, 74, 0.09);
```

**Sustainability / Nature — Forest Moss**
```css
--bg: #F2F5EE; --bg-white: #FFFFFF;
--primary: #4A7A3A; --primary-dark: #224A14; --primary-light: #E4EEDC;
--accent: #D4A040; --accent-light: #FDF4E0;
--border: #C8D8BE; --border-light: #DDE8D4;
--shadow: 0 4px 24px rgba(34, 74, 20, 0.09);
```

---

### 9.7 Font Pairing Alternatives

If you cannot use Google Fonts (offline builds, self-hosted, corporate restrictions), these system font stacks maintain the same visual hierarchy:

| Role | Google Fonts original | System stack fallback |
|------|-----------------------|-----------------------|
| Display | DM Serif Display | `Georgia, 'Times New Roman', serif` |
| Body | Inter | `-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif` |
| Mono | JetBrains Mono | `'SF Mono', 'Fira Code', 'Courier New', monospace` |

```css
/* System font fallback :root */
--font-display: Georgia, 'Times New Roman', serif;
--font-body: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
--font-mono: 'SF Mono', 'Fira Code', Consolas, 'Courier New', monospace;
```

---

## 10. What NOT to Build

These are hard constraints, not preferences.

| ❌ Don't | Reason |
|----------|--------|
| Add a checkout, cart, or payment flow to Art Drops | Art Drops is a spotlight model — all purchases go directly to the artist's own external shop |
| Add affiliate or referral tracking links | Against the content philosophy |
| Use Bootstrap, Tailwind, or any CSS framework | Hand-written inline CSS only |
| Create shared CSS or JS files | All styles and scripts stay inline per page |
| Create a page at `/brand/section-name/` | All Brand content is accordion sections in `brand/index.html` |
| Create `concepts/art-drops/` or `concepts/camera-drops/` | Correct folder names are `art-dropshipping` and `camera-dropshipping` |
| Use `_layouts/default.html` for new pages | Legacy only — it produces sidebar-wrapped pages not matching the current design |
| Add analytics, tracking pixels, or 3rd-party scripts | Without explicit approval |
| Build a nav with only the Concepts dropdown | Both Concepts AND Brand dropdowns are required on every full page |

---

## 📄 License

Documentation and templates in this repository are licensed under the [MIT License](./LICENSE).

---

*Started June 2026 · Built in public · One Monday at a time.*
