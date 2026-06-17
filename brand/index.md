--
layout: none
permalink: /brand/
---
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Brand · Dew Monday</title>
  <meta name="description" content="The Dew Monday brand guide — who we are, what we're building, and how we build it.">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=DM+Serif+Display:ital@0;1&family=Inter:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500;700&display=swap" rel="stylesheet">
  <style>
    :root {
      --bg:#F5F2EC; --bg-white:#FFFFFF; --primary:#2D5A27; --primary-dark:#1E3D1A;
      --primary-mid:#3D7A35; --primary-light:#E8F0E7; --accent:#6BA3BE;
      --accent-light:#E8F2F8; --gold:#D4A847; --gold-light:#FDF6E3;
      --text:#1C1C1C; --text-muted:#6B6B6B; --border:#D8D4C8; --border-light:#EAE6DC;
      --font-display:'DM Serif Display',serif;
      --font-body:'Inter',sans-serif;
      --font-mono:'JetBrains Mono',monospace;
      --radius:14px; --shadow:0 4px 24px rgba(30,61,26,0.09);
    }
    *,*::before,*::after{box-sizing:border-box;margin:0;padding:0;}
    html{scroll-behavior:smooth;}
    body{font-family:var(--font-body);background:var(--bg);color:var(--text);line-height:1.6;}

    /* ===== NAV ===== */
    .nav{position:sticky;top:0;z-index:200;background:rgba(255,255,255,0.97);backdrop-filter:blur(16px);border-bottom:1px solid var(--border);display:flex;align-items:center;justify-content:space-between;padding:0 48px;height:68px;box-shadow:0 1px 12px rgba(30,61,26,0.06);}
    .nav-left{display:flex;align-items:center;gap:32px;}
    .nav-logo{font-family:var(--font-display);font-size:1.3rem;color:var(--primary-dark);text-decoration:none;white-space:nowrap;}
    .nav-logo span{color:var(--accent);}
    .nav-dropdown{position:relative;}
    .nav-dropdown-trigger{display:flex;align-items:center;gap:6px;font-size:0.85rem;font-weight:600;color:var(--text);background:none;border:none;cursor:pointer;padding:6px 10px;border-radius:8px;transition:background 0.15s,color 0.15s;}
    .nav-dropdown-trigger:hover,.nav-dropdown.open .nav-dropdown-trigger{background:var(--primary-light);color:var(--primary);}
    .nav-dropdown-trigger .chevron{width:14px;height:14px;transition:transform 0.2s;}
    .nav-dropdown.open .chevron{transform:rotate(180deg);}
    .nav-dropdown-menu{display:none;position:absolute;top:calc(100% + 8px);left:0;background:#fff;border:1.5px solid var(--border);border-radius:16px;padding:8px;min-width:290px;box-shadow:0 12px 40px rgba(30,61,26,0.13);animation:menuIn 0.18s ease;z-index:300;}
    .nav-dropdown.open .nav-dropdown-menu{display:block;}
    @keyframes menuIn{from{opacity:0;transform:translateY(-6px);}to{opacity:1;transform:translateY(0);}}
    .nav-menu-item{display:flex;align-items:center;gap:12px;padding:10px 12px;border-radius:10px;text-decoration:none;color:var(--text);transition:background 0.15s;}
    .nav-menu-item:hover{background:var(--primary-light);}
    .nav-menu-item.active{background:var(--primary-light);color:var(--primary);}
    .nav-menu-emoji{font-size:1.1rem;width:24px;text-align:center;}
    .nav-menu-title{font-size:0.85rem;font-weight:600;line-height:1.2;}
    .nav-menu-desc{font-size:0.75rem;color:var(--text-muted);margin-top:1px;}
    .nav-menu-divider{height:1px;background:var(--border-light);margin:4px 0;}
    .nav-cta{background:var(--primary);color:#fff;font-size:0.82rem;font-weight:600;padding:8px 18px;border-radius:9px;text-decoration:none;transition:background 0.15s;}
    .nav-cta:hover{background:var(--primary-mid);}

    /* ===== HERO ===== */
    .hero{background:linear-gradient(135deg,var(--primary-dark) 0%,var(--primary) 60%,var(--primary-mid) 100%);padding:80px 48px 72px;text-align:center;position:relative;overflow:hidden;}
    .hero::before{content:'';position:absolute;inset:0;background:radial-gradient(ellipse at 70% 40%,rgba(107,163,190,0.18) 0%,transparent 60%);pointer-events:none;}
    .hero-badge{display:inline-flex;align-items:center;gap:8px;background:rgba(255,255,255,0.12);border:1px solid rgba(255,255,255,0.22);border-radius:999px;padding:5px 14px;margin-bottom:24px;}
    .hero-badge-dot{width:7px;height:7px;border-radius:50%;background:#6EE880;animation:pulse 2s infinite;}
    @keyframes pulse{0%,100%{opacity:1;transform:scale(1);}50%{opacity:0.6;transform:scale(1.3);}}
    .hero-badge-text{font-family:var(--font-mono);font-size:0.72rem;color:rgba(255,255,255,0.85);text-transform:uppercase;letter-spacing:0.1em;}
    .hero h1{font-family:var(--font-display);font-size:3.2rem;line-height:1.1;color:#fff;margin-bottom:18px;max-width:640px;margin-left:auto;margin-right:auto;}
    .hero h1 em{font-style:italic;color:rgba(255,255,255,0.78);}
    .hero-sub{font-size:1.05rem;color:rgba(255,255,255,0.72);max-width:520px;margin:0 auto 36px;}
    .hero-stats{display:flex;justify-content:center;gap:40px;flex-wrap:wrap;}
    .hero-stat{text-align:center;}
    .hero-stat-num{font-family:var(--font-display);font-size:2rem;color:#fff;line-height:1;}
    .hero-stat-label{font-family:var(--font-mono);font-size:0.7rem;color:rgba(255,255,255,0.55);text-transform:uppercase;letter-spacing:0.1em;margin-top:4px;}

    /* ===== LAYOUT ===== */
    .page-layout{display:grid;grid-template-columns:240px 1fr;gap:0;max-width:1180px;margin:0 auto;padding:48px 32px;}
    @media(max-width:768px){.page-layout{grid-template-columns:1fr;}.sidebar{display:none;}}
    .sidebar{position:sticky;top:84px;height:fit-content;padding-right:32px;}
    .sidebar-nav{display:flex;flex-direction:column;gap:4px;}
    .sidebar-link{font-size:0.84rem;font-weight:500;color:var(--text-muted);text-decoration:none;padding:7px 12px;border-radius:8px;border-left:2px solid transparent;transition:all 0.15s;}
    .sidebar-link:hover{color:var(--primary);background:var(--primary-light);border-left-color:var(--primary);}
    .sidebar-link.active{color:var(--primary);font-weight:600;border-left-color:var(--primary);}
    .sidebar-label{font-family:var(--font-mono);font-size:0.68rem;text-transform:uppercase;letter-spacing:0.1em;color:var(--text-muted);padding:8px 12px 4px;margin-top:8px;}

    /* ===== ACCORDION ===== */
    .accordion-section{border:1.5px solid var(--border);border-radius:var(--radius);margin-bottom:16px;overflow:hidden;background:var(--bg-white);box-shadow:var(--shadow);}
    .accordion-header{display:flex;align-items:center;justify-content:space-between;padding:22px 28px;cursor:pointer;user-select:none;transition:background 0.15s;}
    .accordion-header:hover{background:var(--primary-light);}
    .accordion-header-left{display:flex;align-items:center;gap:14px;}
    .accordion-icon{font-size:1.3rem;}
    .accordion-title{font-family:var(--font-display);font-size:1.2rem;color:var(--primary-dark);}
    .accordion-chevron{width:18px;height:18px;color:var(--text-muted);transition:transform 0.25s;}
    .accordion-section.open .accordion-chevron{transform:rotate(180deg);}
    .accordion-body{display:none;padding:0 28px 28px;}
    .accordion-section.open .accordion-body{display:block;}

    /* ===== CONTENT STYLES ===== */
    .content-prose{font-size:0.95rem;color:var(--text);line-height:1.75;}
    .content-prose p{margin-bottom:14px;}
    .content-prose h3{font-family:var(--font-display);font-size:1.1rem;color:var(--primary-dark);margin:24px 0 8px;}
    .content-prose h4{font-size:0.85rem;font-weight:700;text-transform:uppercase;letter-spacing:0.06em;color:var(--text-muted);margin:20px 0 6px;}
    .content-prose ul{padding-left:20px;margin-bottom:14px;}
    .content-prose li{margin-bottom:5px;}
    .content-prose strong{color:var(--primary-dark);}
    .divider{height:1px;background:var(--border-light);margin:20px 0;}

    /* color swatches */
    .swatch-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(160px,1fr));gap:12px;margin:16px 0;}
    .swatch{border-radius:10px;overflow:hidden;border:1px solid var(--border);}
    .swatch-color{height:56px;}
    .swatch-info{padding:8px 10px;background:#fff;}
    .swatch-name{font-size:0.8rem;font-weight:600;}
    .swatch-hex{font-family:var(--font-mono);font-size:0.72rem;color:var(--text-muted);}

    /* font specimens */
    .font-specimen{border:1px solid var(--border);border-radius:10px;padding:16px 18px;margin-bottom:10px;background:#fff;}
    .font-specimen-label{font-family:var(--font-mono);font-size:0.68rem;text-transform:uppercase;letter-spacing:0.1em;color:var(--text-muted);margin-bottom:6px;}
    .font-specimen-sample{line-height:1.3;}

    /* scorecard table */
    .scorecard-table{width:100%;border-collapse:collapse;font-size:0.85rem;margin-top:12px;}
    .scorecard-table th{font-family:var(--font-mono);font-size:0.7rem;text-transform:uppercase;letter-spacing:0.06em;color:var(--text-muted);padding:8px 10px;border-bottom:2px solid var(--border);text-align:left;}
    .scorecard-table td{padding:10px 10px;border-bottom:1px solid var(--border-light);vertical-align:middle;}
    .scorecard-table tr:last-child td{border-bottom:none;}
    .score-pill{display:inline-block;font-family:var(--font-mono);font-size:0.72rem;font-weight:700;padding:2px 8px;border-radius:99px;}
    .score-5{background:#d1fae5;color:#065f46;}
    .score-4{background:#dbeafe;color:#1e40af;}
    .score-3{background:#fef3c7;color:#92400e;}
    .score-2{background:#fee2e2;color:#991b1b;}
    .score-total{font-family:var(--font-display);font-size:1rem;color:var(--primary-dark);}

    /* interview questions */
    .q-group{margin-bottom:20px;}
    .q-group-title{font-family:var(--font-mono);font-size:0.72rem;text-transform:uppercase;letter-spacing:0.1em;color:var(--primary);background:var(--primary-light);display:inline-block;padding:3px 10px;border-radius:99px;margin-bottom:10px;}
    .q-list{list-style:none;padding:0;}
    .q-list li{padding:7px 0 7px 20px;border-bottom:1px solid var(--border-light);position:relative;font-size:0.9rem;}
    .q-list li::before{content:'→';position:absolute;left:0;color:var(--primary);font-size:0.8rem;}
    .q-list li:last-child{border-bottom:none;}

    /* component preview */
    .component-row{display:flex;flex-wrap:wrap;gap:8px;margin-bottom:12px;}
    .chip{font-family:var(--font-mono);font-size:0.72rem;padding:4px 12px;border-radius:99px;border:1.5px solid var(--border);background:#fff;color:var(--text);}
    .chip.active{background:var(--primary);border-color:var(--primary);color:#fff;}
    .badge{font-family:var(--font-mono);font-size:0.68rem;padding:3px 9px;border-radius:6px;background:var(--primary-light);color:var(--primary);font-weight:600;}

    /* ===== CTA ===== */
    .cta{background:linear-gradient(135deg,var(--primary-dark),var(--primary));padding:72px 48px;text-align:center;margin-top:0;}
    .cta h2{font-family:var(--font-display);font-size:2.2rem;color:#fff;margin-bottom:12px;}
    .cta p{color:rgba(255,255,255,0.72);margin-bottom:28px;font-size:1rem;}
    .cta-btn{display:inline-block;background:#fff;color:var(--primary-dark);font-weight:700;padding:14px 36px;border-radius:10px;text-decoration:none;font-size:0.95rem;transition:opacity 0.15s;}
    .cta-btn:hover{opacity:0.9;}

    /* ===== FOOTER ===== */
    .footer{background:var(--primary-dark);color:rgba(255,255,255,0.6);padding:48px;display:flex;flex-wrap:wrap;gap:32px;justify-content:space-between;}
    .footer-logo{font-family:var(--font-display);font-size:1.1rem;color:#fff;}
    .footer-logo span{color:var(--accent);}
    .footer-links{display:flex;flex-wrap:wrap;gap:12px 24px;}
    .footer-links a{color:rgba(255,255,255,0.55);text-decoration:none;font-size:0.83rem;transition:color 0.15s;}
    .footer-links a:hover{color:#fff;}
    .footer-copy{width:100%;font-family:var(--font-mono);font-size:0.7rem;color:rgba(255,255,255,0.3);margin-top:24px;padding-top:24px;border-top:1px solid rgba(255,255,255,0.1);}
  </style>
</head>
<body>

<!-- NAV -->
<nav class="nav">
  <div class="nav-left">
    <a href="/dewmonday/" class="nav-logo">Dew<span>Monday</span></a>

    <!-- Concepts dropdown -->
    <div class="nav-dropdown" id="dd-concepts">
      <button class="nav-dropdown-trigger" onclick="toggleDD('dd-concepts')">
        Concepts
        <svg class="chevron" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"/></svg>
      </button>
      <div class="nav-dropdown-menu">
        <a href="/dewmonday/concepts/creator-hub/" class="nav-menu-item">
          <span class="nav-menu-emoji">✍️</span>
          <div><div class="nav-menu-title">Creator Hub</div><div class="nav-menu-desc">The newsletter itself</div></div>
        </a>
        <div class="nav-menu-divider"></div>
        <a href="/dewmonday/concepts/art-dropshipping/" class="nav-menu-item">
          <span class="nav-menu-emoji">🖼️</span>
          <div><div class="nav-menu-title">Art Drops</div><div class="nav-menu-desc">Independent artist spotlights</div></div>
        </a>
        <a href="/dewmonday/concepts/camera-dropshipping/" class="nav-menu-item">
          <span class="nav-menu-emoji">📷</span>
          <div><div class="nav-menu-title">Camera Drops</div><div class="nav-menu-desc">Curated creator gear</div></div>
        </a>
        <a href="/dewmonday/concepts/little-makers/" class="nav-menu-item">
          <span class="nav-menu-emoji">🎈</span>
          <div><div class="nav-menu-title">Little Makers</div><div class="nav-menu-desc">Kids craft activities</div></div>
        </a>
        <a href="/dewmonday/concepts/tutorial-app/" class="nav-menu-item">
          <span class="nav-menu-emoji">🎨</span>
          <div><div class="nav-menu-title">Tutorial App</div><div class="nav-menu-desc">Video lesson platform</div></div>
        </a>
        <a href="/dewmonday/concepts/art-tutorial-app/" class="nav-menu-item">
          <span class="nav-menu-emoji">🖌️</span>
          <div><div class="nav-menu-title">Art Tutorial App</div><div class="nav-menu-desc">Structured art education</div></div>
        </a>
      </div>
    </div>

    <!-- Brand dropdown -->
    <div class="nav-dropdown" id="dd-brand">
      <button class="nav-dropdown-trigger" onclick="toggleDD('dd-brand')" style="color:var(--primary);background:var(--primary-light);">
        Brand
        <svg class="chevron" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"/></svg>
      </button>
      <div class="nav-dropdown-menu">
        <a href="/dewmonday/brand/#overview" class="nav-menu-item active">
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
  <a href="/dewmonday/signup/" class="nav-cta">Get Early Access</a>
</nav>

<!-- HERO -->
<section class="hero">
  <div class="hero-badge">
    <span class="hero-badge-dot"></span>
    <span class="hero-badge-text">Brand Hub</span>
  </div>
  <h1>Everything Dew Monday <em>is.</em></h1>
  <p class="hero-sub">Voice, design, positioning, and the scorecards we use to decide what to build next.</p>
  <div class="hero-stats">
    <div class="hero-stat">
      <div class="hero-stat-num">6</div>
      <div class="hero-stat-label">Concepts</div>
    </div>
    <div class="hero-stat">
      <div class="hero-stat-num">1</div>
      <div class="hero-stat-label">Newsletter</div>
    </div>
    <div class="hero-stat">
      <div class="hero-stat-num">6am</div>
      <div class="hero-stat-label">Every Monday</div>
    </div>
    <div class="hero-stat">
      <div class="hero-stat-num">Free</div>
      <div class="hero-stat-label">Always</div>
    </div>
  </div>
</section>

<!-- PAGE LAYOUT -->
<div class="page-layout">

  <!-- SIDEBAR -->
  <aside class="sidebar">
    <div class="sidebar-label">Sections</div>
    <nav class="sidebar-nav">
      <a href="#overview" class="sidebar-link">📖 Overview</a>
      <a href="#brand-identity" class="sidebar-link">🎯 Brand Identity</a>
      <a href="#design-system" class="sidebar-link">🎨 Design System</a>
      <a href="#interview-guide" class="sidebar-link">🗣️ Interview Guide</a>
      <a href="#validation-scorecard" class="sidebar-link">📊 Concept Scorecard</a>
    </nav>
  </aside>

  <!-- MAIN CONTENT -->
  <main>

    <!-- 1. OVERVIEW -->
    <div class="accordion-section open" id="overview">
      <div class="accordion-header" onclick="toggleAccordion(this)">
        <div class="accordion-header-left">
          <span class="accordion-icon">📖</span>
          <span class="accordion-title">Overview</span>
        </div>
        <svg class="accordion-chevron" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"/></svg>
      </div>
      <div class="accordion-body">
        <div class="content-prose">
          <p>Dew Monday is a build-in-public creator newsletter. One email, every Monday at 6am ET, tracking six different business concepts simultaneously. Free, always. No ads, no sponsored content, no editorial pretending.</p>
          <h3>What it is</h3>
          <p>Each week I write about what I'm actually doing across six concepts — what worked, what didn't, what I'm trying next. Real decisions, real numbers. The newsletter is the product. The six concepts are the subject matter.</p>
          <h3>The six concepts</h3>
          <div class="component-row" style="flex-direction:column;gap:6px;margin-bottom:0;">
            <div style="display:flex;align-items:center;gap:10px;padding:8px 0;border-bottom:1px solid var(--border-light);">
              <span style="font-size:1.1rem;">✍️</span>
              <div><strong>Creator Hub</strong> — <span style="color:var(--text-muted);font-size:0.88rem;">The newsletter itself. Where everything connects.</span></div>
            </div>
            <div style="display:flex;align-items:center;gap:10px;padding:8px 0;border-bottom:1px solid var(--border-light);">
              <span style="font-size:1.1rem;">🖼️</span>
              <div><strong>Art Drops</strong> — <span style="color:var(--text-muted);font-size:0.88rem;">Independent artist spotlights. Discovery platform, not a sales channel.</span></div>
            </div>
            <div style="display:flex;align-items:center;gap:10px;padding:8px 0;border-bottom:1px solid var(--border-light);">
              <span style="font-size:1.1rem;">📷</span>
              <div><strong>Camera Drops</strong> — <span style="color:var(--text-muted);font-size:0.88rem;">Curated creator gear. Honest reviews, no affiliate pressure.</span></div>
            </div>
            <div style="display:flex;align-items:center;gap:10px;padding:8px 0;border-bottom:1px solid var(--border-light);">
              <span style="font-size:1.1rem;">🎈</span>
              <div><strong>Little Makers</strong> — <span style="color:var(--text-muted);font-size:0.88rem;">Craft activities for kids. Maker-minded, parent-friendly.</span></div>
            </div>
            <div style="display:flex;align-items:center;gap:10px;padding:8px 0;border-bottom:1px solid var(--border-light);">
              <span style="font-size:1.1rem;">🎨</span>
              <div><strong>Tutorial App</strong> — <span style="color:var(--text-muted);font-size:0.88rem;">Video lesson platform for creators who want to teach.</span></div>
            </div>
            <div style="display:flex;align-items:center;gap:10px;padding:8px 0;">
              <span style="font-size:1.1rem;">🖌️</span>
              <div><strong>Art Tutorial App</strong> — <span style="color:var(--text-muted);font-size:0.88rem;">Structured art education. Technique-first, beginner-friendly.</span></div>
            </div>
          </div>
          <h3>The model</h3>
          <p>Build in public means the newsletter readers see everything — including the experiments that go nowhere. The goal is to find which of the six concepts has real product-market fit before committing to building any of them fully. The newsletter is how I document the process and grow an audience at the same time.</p>
          <p><strong>Monday, 6am ET. Free. No exceptions.</strong></p>
        </div>
      </div>
    </div>

    <!-- 2. BRAND IDENTITY -->
    <div class="accordion-section" id="brand-identity">
      <div class="accordion-header" onclick="toggleAccordion(this)">
        <div class="accordion-header-left">
          <span class="accordion-icon">🎯</span>
          <span class="accordion-title">Brand Identity</span>
        </div>
        <svg class="accordion-chevron" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"/></svg>
      </div>
      <div class="accordion-body">
        <div class="content-prose">
          <h3>Voice</h3>
          <p>Honest, unpolished, direct. First person throughout. No hype language. Numbers reported accurately — including the bad ones. The reader is treated like someone who's building their own thing and doesn't have time for vague inspiration.</p>
          <h4>What we say</h4>
          <ul>
            <li>"Here's what I tried and what actually happened."</li>
            <li>"I don't know yet — here's my current thinking."</li>
            <li>"This didn't work. Here's why I think it failed."</li>
          </ul>
          <h4>What we don't say</h4>
          <ul>
            <li>Game-changing, revolutionary, disruptive</li>
            <li>Passive income, hustle, grind, scale to the moon</li>
            <li>Vague encouragement with no specific content</li>
          </ul>
          <div class="divider"></div>
          <h3>Tone by context</h3>
          <p><strong>Newsletter content:</strong> Conversational, first-person, candid. Like a weekly update to a group of people who are also building something.</p>
          <p><strong>Concept pages:</strong> Slightly more structured, but same voice. Still honest about where each concept is in development.</p>
          <p><strong>Spotlights (Art Drops):</strong> Observational, specific, not promotional. Write about the work like someone who actually looked at it.</p>
          <div class="divider"></div>
          <h3>Positioning</h3>
          <p>Not a marketing newsletter. Not a productivity newsletter. A build-in-public newsletter that documents the honest attempt to find and build something that works — across six very different directions.</p>
          <h3>Audience</h3>
          <ul>
            <li>Creators who are also trying to build a business</li>
            <li>People interested in the indie product / side project space</li>
            <li>Art and craft communities (through Art Drops and Little Makers)</li>
            <li>Early-stage founders who want to watch a real process unfold</li>
          </ul>
          <div class="divider"></div>
          <h3>Art Drops — critical positioning rule</h3>
          <p>Art Drops is a <strong>spotlight and discovery platform only.</strong> Dew Monday does not sell other artists' work, take commissions, or use affiliate links for artist sales. The model is: find the artist, write about the work, send people directly to the artist's own shop. That's it.</p>
          <p>Only Renny's own work can be sold through the platform.</p>
        </div>
      </div>
    </div>

    <!-- 3. DESIGN SYSTEM -->
    <div class="accordion-section" id="design-system">
      <div class="accordion-header" onclick="toggleAccordion(this)">
        <div class="accordion-header-left">
          <span class="accordion-icon">🎨</span>
          <span class="accordion-title">Design System</span>
        </div>
        <svg class="accordion-chevron" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"/></svg>
      </div>
      <div class="accordion-body">
        <div class="content-prose">
          <h3>Typography</h3>

          <div class="font-specimen">
            <div class="font-specimen-label">DM Serif Display — Headings, hero text, card titles, stat numbers</div>
            <div class="font-specimen-sample" style="font-family:'DM Serif Display',serif;font-size:2rem;color:var(--primary-dark);">Dew Monday</div>
          </div>
          <div class="font-specimen">
            <div class="font-specimen-label">Inter — Body text, buttons, descriptions, UI labels</div>
            <div class="font-specimen-sample" style="font-family:'Inter',sans-serif;font-size:1rem;">Real decisions, real numbers, every Monday at 6am.</div>
          </div>
          <div class="font-specimen">
            <div class="font-specimen-label">JetBrains Mono — Badges, tags, eyebrows, mono labels</div>
            <div class="font-specimen-sample" style="font-family:'JetBrains Mono',monospace;font-size:0.82rem;color:var(--text-muted);">ARTIST SPOTLIGHT · 001 · JUNE 2026</div>
          </div>

          <div class="divider"></div>
          <h3>Color Tokens — Per Concept</h3>
          <div class="swatch-grid">
            <div class="swatch">
              <div class="swatch-color" style="background:#2D5A27;"></div>
              <div class="swatch-info"><div class="swatch-name">Brand / Creator Hub</div><div class="swatch-hex">#2D5A27</div></div>
            </div>
            <div class="swatch">
              <div class="swatch-color" style="background:#2A5F7A;"></div>
              <div class="swatch-info"><div class="swatch-name">Art Drops</div><div class="swatch-hex">#2A5F7A</div></div>
            </div>
            <div class="swatch">
              <div class="swatch-color" style="background:#9A4E20;"></div>
              <div class="swatch-info"><div class="swatch-name">Camera Drops</div><div class="swatch-hex">#9A4E20</div></div>
            </div>
            <div class="swatch">
              <div class="swatch-color" style="background:#2A7A6A;"></div>
              <div class="swatch-info"><div class="swatch-name">Little Makers</div><div class="swatch-hex">#2A7A6A</div></div>
            </div>
            <div class="swatch">
              <div class="swatch-color" style="background:#6B4FA0;"></div>
              <div class="swatch-info"><div class="swatch-name">Tutorial App</div><div class="swatch-hex">#6B4FA0</div></div>
            </div>
            <div class="swatch">
              <div class="swatch-color" style="background:#7A3A5A;"></div>
              <div class="swatch-info"><div class="swatch-name">Art Tutorial App</div><div class="swatch-hex">#7A3A5A</div></div>
            </div>
          </div>

          <div class="divider"></div>
          <h3>Component Patterns</h3>
          <h4>Filter Chips</h4>
          <div class="component-row">
            <span class="chip active">All</span>
            <span class="chip">Spotlights</span>
            <span class="chip">New Drops</span>
            <span class="chip">Behind the Work</span>
          </div>

          <h4>Badges / Tags</h4>
          <div class="component-row">
            <span class="badge">SPOTLIGHT 001</span>
            <span class="badge" style="background:var(--accent-light);color:var(--accent);">NEW DROP</span>
            <span class="badge" style="background:var(--gold-light);color:#92400e;">JUNE 2026</span>
          </div>

          <h4>Navigation</h4>
          <ul>
            <li>Sticky nav, 64–68px height, glassmorphism background (backdrop-filter: blur 12–16px)</li>
            <li>Logo: DM Serif Display, primary-dark color, accent-colored span</li>
            <li>Dropdowns: open on click, chevron rotates 180°, menu animates in from top</li>
            <li>CTA button: right side, primary bg, white text</li>
          </ul>

          <h4>Spacing & Radius</h4>
          <ul>
            <li>Default border-radius: 14px (cards, dropdowns, inputs)</li>
            <li>Large radius: 20px (hero elements, featured cards)</li>
            <li>Pills: 999px (chips, badges, tags)</li>
            <li>Page horizontal padding: 40–48px desktop, 20px mobile</li>
            <li>Card padding: 20–28px</li>
          </ul>

          <h4>Shadows</h4>
          <ul>
            <li>Card: <code style="font-family:var(--font-mono);font-size:0.78rem;">0 4px 24px rgba(primary-dark, 0.09)</code></li>
            <li>Dropdown: <code style="font-family:var(--font-mono);font-size:0.78rem;">0 12px 40px rgba(primary-dark, 0.13)</code></li>
            <li>Nav: <code style="font-family:var(--font-mono);font-size:0.78rem;">0 1px 12px rgba(primary-dark, 0.07)</code></li>
          </ul>
        </div>
      </div>
    </div>

    <!-- 4. INTERVIEW GUIDE -->
    <div class="accordion-section" id="interview-guide">
      <div class="accordion-header" onclick="toggleAccordion(this)">
        <div class="accordion-header-left">
          <span class="accordion-icon">🗣️</span>
          <span class="accordion-title">Customer Interview Guide</span>
        </div>
        <svg class="accordion-chevron" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"/></svg>
      </div>
      <div class="accordion-body">
        <div class="content-prose">
          <p>25 questions for concept validation. Run these in a 30–45 minute conversation. Don't read them verbatim — use them as a guide. The goal is to understand the problem space, not to pitch the concept.</p>
          <div class="divider"></div>

          <div class="q-group">
            <div class="q-group-title">Warm-Up (5 questions)</div>
            <ol class="q-list">
              <li>Tell me a bit about what you're working on or building right now.</li>
              <li>How long have you been doing this? What made you start?</li>
              <li>What does a typical week look like for you in this space?</li>
              <li>What tools or resources do you rely on most?</li>
              <li>What newsletters, podcasts, or communities do you follow related to your work?</li>
            </ol>
          </div>

          <div class="q-group">
            <div class="q-group-title">Problem Discovery (7 questions)</div>
            <ol class="q-list" start="6">
              <li>What's the hardest part of [concept-specific problem area] right now?</li>
              <li>Tell me about the last time you got stuck on this. What happened?</li>
              <li>How much time per week do you spend dealing with this problem?</li>
              <li>What have you tried to fix it so far?</li>
              <li>What was the result? Did it actually help?</li>
              <li>Is this a problem that gets worse over time or stays about the same?</li>
              <li>Who else on your team or in your life is affected by this?</li>
            </ol>
          </div>

          <div class="q-group">
            <div class="q-group-title">Current Solutions (5 questions)</div>
            <ol class="q-list" start="13">
              <li>What are you using right now to solve this? Walk me through it.</li>
              <li>What do you like about what you're currently using?</li>
              <li>What's missing or frustrating about it?</li>
              <li>Have you looked for alternatives? What stopped you from switching?</li>
              <li>If this tool or approach disappeared tomorrow, what would you do?</li>
            </ol>
          </div>

          <div class="q-group">
            <div class="q-group-title">Willingness to Pay (4 questions)</div>
            <ol class="q-list" start="18">
              <li>Are you currently paying for anything to help with this problem? What?</li>
              <li>What would need to be true for you to pay for a solution?</li>
              <li>If something solved this completely, what would that be worth to you per month?</li>
              <li>What would make you NOT pay, even if it solved the problem?</li>
            </ol>
          </div>

          <div class="q-group">
            <div class="q-group-title">Concept Reaction (4 questions)</div>
            <ol class="q-list" start="22">
              <li>Let me tell you what I'm thinking about building. [Explain concept in one sentence.] What's your first reaction?</li>
              <li>What part sounds most useful to you?</li>
              <li>What part sounds least useful, or like it wouldn't matter?</li>
              <li>Who else do you know who has this same problem? Would you introduce me?</li>
            </ol>
          </div>

          <p style="color:var(--text-muted);font-size:0.85rem;margin-top:8px;">Bonus: Always ask for a referral at the end. If they can't name someone else with the problem, that's a signal worth noting.</p>
        </div>
      </div>
    </div>

    <!-- 5. CONCEPT VALIDATION SCORECARD -->
    <div class="accordion-section" id="validation-scorecard">
      <div class="accordion-header" onclick="toggleAccordion(this)">
        <div class="accordion-header-left">
          <span class="accordion-icon">📊</span>
          <span class="accordion-title">Concept Validation Scorecard</span>
        </div>
        <svg class="accordion-chevron" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"/></svg>
      </div>
      <div class="accordion-body">
        <div class="content-prose">
          <p>Each concept scored 1–5 across five dimensions. Scores reflect current understanding — these will be updated as validation work continues.</p>
          <p style="font-size:0.83rem;color:var(--text-muted);">Dimensions: <strong>Problem Clarity</strong> · <strong>Market Demand</strong> · <strong>Creator Fit</strong> · <strong>Revenue Potential</strong> · <strong>Execution Simplicity</strong></p>
          <div style="overflow-x:auto;margin-top:16px;">
            <table class="scorecard-table">
              <thead>
                <tr>
                  <th>Concept</th>
                  <th>Problem</th>
                  <th>Demand</th>
                  <th>Fit</th>
                  <th>Revenue</th>
                  <th>Execution</th>
                  <th>Total</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td><strong>✍️ Creator Hub</strong></td>
                  <td><span class="score-pill score-5">5</span></td>
                  <td><span class="score-pill score-4">4</span></td>
                  <td><span class="score-pill score-5">5</span></td>
                  <td><span class="score-pill score-3">3</span></td>
                  <td><span class="score-pill score-5">5</span></td>
                  <td><span class="score-total">22</span></td>
                </tr>
                <tr>
                  <td><strong>🖼️ Art Drops</strong></td>
                  <td><span class="score-pill score-5">5</span></td>
                  <td><span class="score-pill score-4">4</span></td>
                  <td><span class="score-pill score-5">5</span></td>
                  <td><span class="score-pill score-3">3</span></td>
                  <td><span class="score-pill score-5">5</span></td>
                  <td><span class="score-total">22</span></td>
                </tr>
                <tr>
                  <td><strong>📷 Camera Drops</strong></td>
                  <td><span class="score-pill score-4">4</span></td>
                  <td><span class="score-pill score-4">4</span></td>
                  <td><span class="score-pill score-4">4</span></td>
                  <td><span class="score-pill score-4">4</span></td>
                  <td><span class="score-pill score-3">3</span></td>
                  <td><span class="score-total">19</span></td>
                </tr>
                <tr>
                  <td><strong>🎈 Little Makers</strong></td>
                  <td><span class="score-pill score-4">4</span></td>
                  <td><span class="score-pill score-3">3</span></td>
                  <td><span class="score-pill score-4">4</span></td>
                  <td><span class="score-pill score-3">3</span></td>
                  <td><span class="score-pill score-4">4</span></td>
                  <td><span class="score-total">18</span></td>
                </tr>
                <tr>
                  <td><strong>🎨 Tutorial App</strong></td>
                  <td><span class="score-pill score-4">4</span></td>
                  <td><span class="score-pill score-4">4</span></td>
                  <td><span class="score-pill score-3">3</span></td>
                  <td><span class="score-pill score-5">5</span></td>
                  <td><span class="score-pill score-2">2</span></td>
                  <td><span class="score-total">18</span></td>
                </tr>
                <tr>
                  <td><strong>🖌️ Art Tutorial App</strong></td>
                  <td><span class="score-pill score-4">4</span></td>
                  <td><span class="score-pill score-3">3</span></td>
                  <td><span class="score-pill score-5">5</span></td>
                  <td><span class="score-pill score-4">4</span></td>
                  <td><span class="score-pill score-2">2</span></td>
                  <td><span class="score-total">18</span></td>
                </tr>
              </tbody>
            </table>
          </div>
          <div class="divider"></div>
          <h3>Notes on Art Drops score</h3>
          <p>Art Drops was re-scored after changing the model from dropshipping to discovery/spotlight. Execution simplicity jumped from 2 to 5 — removing inventory management, supplier coordination, and margin pressure makes this one of the simplest concepts to run. The revenue potential is lower (3) because Dew Monday isn't taking a cut of artist sales, but the creator fit is the highest of any concept.</p>
          <p style="font-size:0.83rem;color:var(--text-muted);">Scores are updated as validation work happens. Current scores reflect June 2026 understanding.</p>
        </div>
      </div>
    </div>

  </main>
</div>

<!-- CTA -->
<section class="cta">
  <h2>Six concepts. One newsletter.</h2>
  <p>Every Monday at 6am ET — free, honest, built in public.</p>
  <a href="/dewmonday/signup/" class="cta-btn">Get Early Access →</a>
</section>

<!-- FOOTER -->
<footer class="footer">
  <div>
    <div class="footer-logo">Dew<span>Monday</span></div>
    <div style="font-size:0.8rem;margin-top:6px;">Built in public. Monday 6am ET.</div>
  </div>
  <div class="footer-links">
    <a href="/dewmonday/">Home</a>
    <a href="/dewmonday/concepts/creator-hub/">Creator Hub</a>
    <a href="/dewmonday/concepts/art-dropshipping/">Art Drops</a>
    <a href="/dewmonday/concepts/camera-dropshipping/">Camera Drops</a>
    <a href="/dewmonday/concepts/little-makers/">Little Makers</a>
    <a href="/dewmonday/concepts/tutorial-app/">Tutorial App</a>
    <a href="/dewmonday/concepts/art-tutorial-app/">Art Tutorial App</a>
    <a href="/dewmonday/brand/">Brand</a>
    <a href="/dewmonday/signup/">Sign Up</a>
  </div>
  <div class="footer-copy">© 2026 Dew Monday. Built in public in Livonia, MI.</div>
</footer>

<script>
  function toggleDD(id) {
    const all = document.querySelectorAll('.nav-dropdown');
    all.forEach(el => { if (el.id !== id) el.classList.remove('open'); });
    document.getElementById(id).classList.toggle('open');
  }
  document.addEventListener('click', e => {
    if (!e.target.closest('.nav-dropdown')) {
      document.querySelectorAll('.nav-dropdown').forEach(el => el.classList.remove('open'));
    }
  });
  function toggleAccordion(header) {
    const section = header.closest('.accordion-section');
    section.classList.toggle('open');
  }
  // Sidebar active state on scroll
  const sections = document.querySelectorAll('.accordion-section[id]');
  const sidebarLinks = document.querySelectorAll('.sidebar-link');
  window.addEventListener('scroll', () => {
    let current = '';
    sections.forEach(s => {
      if (window.scrollY >= s.offsetTop - 100) current = s.id;
    });
    sidebarLinks.forEach(l => {
      l.classList.toggle('active', l.getAttribute('href') === '#' + current);
    });
  });
</script>
</body>
</html>
