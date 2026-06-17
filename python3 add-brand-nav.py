#!/usr/bin/env python3
"""
add-brand-nav.py
Adds the Brand dropdown to nav-left on all standalone concept pages.

Run from repo root:
  python3 "add-brand-nav.py"

Files updated (6 concept pages):
  concepts/creator-hub/index.html
  concepts/art-dropshipping/index.html
  concepts/camera-dropshipping/index.html
  concepts/little-makers/index.html
  concepts/tutorial-app/index.html
  concepts/art-tutorial-app/index.html

Note: index.html and signup.html have different nav structures and are NOT updated by this script.
Sub-pages (drops/) already include the Brand dropdown.
"""

import re, pathlib

# Concept pages with standard nav structure
CONCEPT_PAGES = [
    "concepts/creator-hub/index.html",
    "concepts/art-dropshipping/index.html",
    "concepts/camera-dropshipping/index.html",
    "concepts/little-makers/index.html",
    "concepts/tutorial-app/index.html",
    "concepts/art-tutorial-app/index.html",
]

# Brand dropdown for pages that use {{ | relative_url }} Liquid syntax
BRAND_DROPDOWN_LIQUID = """
    <!-- Brand dropdown -->
    <div class="nav-dropdown" id="dd-brand">
      <button class="nav-dropdown-trigger" onclick="toggleDD('dd-brand')">
        Brand
        <svg class="chevron" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"/></svg>
      </button>
      <div class="nav-dropdown-menu">
        <a href="{{ '/brand/#overview' | relative_url }}" class="nav-menu-item">
          <span class="nav-menu-emoji">📖</span>
          <div><div class="nav-menu-title">Overview</div><div class="nav-menu-desc">What Dew Monday is</div></div>
        </a>
        <a href="{{ '/brand/#brand-identity' | relative_url }}" class="nav-menu-item">
          <span class="nav-menu-emoji">🎯</span>
          <div><div class="nav-menu-title">Brand Identity</div><div class="nav-menu-desc">Voice, tone, audience</div></div>
        </a>
        <a href="{{ '/brand/#design-system' | relative_url }}" class="nav-menu-item">
          <span class="nav-menu-emoji">🎨</span>
          <div><div class="nav-menu-title">Design System</div><div class="nav-menu-desc">Fonts, colors, components</div></div>
        </a>
        <a href="{{ '/brand/#interview-guide' | relative_url }}" class="nav-menu-item">
          <span class="nav-menu-emoji">🗣️</span>
          <div><div class="nav-menu-title">Interview Guide</div><div class="nav-menu-desc">25 validation questions</div></div>
        </a>
        <a href="{{ '/brand/#validation-scorecard' | relative_url }}" class="nav-menu-item">
          <span class="nav-menu-emoji">📊</span>
          <div><div class="nav-menu-title">Concept Scorecard</div><div class="nav-menu-desc">All 6 concepts rated</div></div>
        </a>
      </div>
    </div>"""

# Brand dropdown for pages that use hardcoded /dewmonday/ paths
BRAND_DROPDOWN_HARDCODED = """
      <!-- Brand dropdown -->
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
      </div>"""

# toggleDD JS function — added alongside existing dropdown JS
TOGGLE_DD_JS = """
  function toggleDD(id) {
    const dd = document.getElementById(id);
    const isOpen = dd.classList.contains('open');
    document.querySelectorAll('.nav-dropdown.open').forEach(d => d.classList.remove('open'));
    if (!isOpen) dd.classList.add('open');
  }"""


def process_file(path_str):
    p = pathlib.Path(path_str)
    if not p.exists():
        print(f"  ⚠️  NOT FOUND: {path_str}")
        return

    content = p.read_text(encoding='utf-8')

    # Skip if already patched
    if 'dd-brand' in content:
        print(f"  ✅ Already has Brand dropdown: {path_str}")
        return

    uses_liquid = "{{ '/" in content

    if uses_liquid:
        brand_html = BRAND_DROPDOWN_LIQUID
        # Pattern A: nav-left closes, then nav-right opens (with optional blank line)
        # Inject Brand dropdown inside nav-left, just before it closes
        pattern = re.compile(r'(\n  </div>\n\n?  <div class="nav-right">)')
        if not pattern.search(content):
            print(f"  ❌ Could not find nav-right pattern in: {path_str}")
            return
        new_content = pattern.sub(brand_html + r'\1', content, count=1)
    else:
        brand_html = BRAND_DROPDOWN_HARDCODED
        # Pattern B: nav-left closes, then nav-cta directly (art-tutorial-app style)
        # Inject Brand dropdown inside nav-left, just before it closes (4-space indent)
        pattern = re.compile(r'(\n    </div>\n    <a [^>]*class="nav-cta")')
        if not pattern.search(content):
            print(f"  ❌ Could not find nav-cta pattern in: {path_str}")
            return
        new_content = pattern.sub(brand_html + r'\1', content, count=1)

    # Add toggleDD function alongside existing dropdown JS
    if 'toggleDD' not in new_content:
        for fn_name in ['function toggleDropdown()', 'function toggleNav()']:
            if fn_name in new_content:
                new_content = new_content.replace(
                    f'\n  {fn_name}',
                    TOGGLE_DD_JS + f'\n  {fn_name}'
                )
                break

    p.write_text(new_content, encoding='utf-8')
    print(f"  ✅ Updated: {path_str}")


print("=== Adding Brand dropdown to concept pages ===\n")
for f in CONCEPT_PAGES:
    process_file(f)

print("\nDone.")
print("\nTo commit: git add -A && git commit -m 'feat: add Brand dropdown to concept pages' && git push")
