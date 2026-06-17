#!/usr/bin/env python3
"""
add-brand-nav.py
Adds the Brand dropdown to the nav on all existing standalone pages.

Run from the repo root:
  python3 add-brand-nav.py

Files updated (8 total):
  index.html
  signup.html
  concepts/creator-hub/index.html
  concepts/art-dropshipping/index.html
  concepts/camera-dropshipping/index.html
  concepts/little-makers/index.html
  concepts/tutorial-app/index.html
  concepts/art-tutorial-app/index.html
"""

import re, pathlib

FILES = [
    "index.html",
    "signup.html",
    "concepts/creator-hub/index.html",
    "concepts/art-dropshipping/index.html",
    "concepts/camera-dropshipping/index.html",
    "concepts/little-makers/index.html",
    "concepts/tutorial-app/index.html",
    "concepts/art-tutorial-app/index.html",
]

# The Brand dropdown HTML to inject
BRAND_DROPDOWN = '''          <div class="nav-dropdown" id="dd-brand">
            <button class="nav-dropdown-trigger" onclick="toggleDD('dd-brand')">
              Brand
              <svg class="chevron" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"/></svg>
            </button>
            <div class="nav-dropdown-menu">
              <a href="/dewmonday/brand/#overview" class="nav-menu-item">
                <span class="nav-menu-emoji">ð</span>
                <div><div class="nav-menu-title">Overview</div><div class="nav-menu-desc">What Dew Monday is</div></div>
              </a>
              <a href="/dewmonday/brand/#brand-identity" class="nav-menu-item">
                <span class="nav-menu-emoji">ð¯</span>
                <div><div class="nav-menu-title">Brand Identity</div><div class="nav-menu-desc">Voice, tone, audience</div></div>
              </a>
              <a href="/dewmonday/brand/#design-system" class="nav-menu-item">
                <span class="nav-menu-emoji">ð¨</span>
                <div><div class="nav-menu-title">Design System</div><div class="nav-menu-desc">Fonts, colors, components</div></div>
              </a>
              <a href="/dewmonday/brand/#interview-guide" class="nav-menu-item">
                <span class="nav-menu-emoji">ð£ï¸</span>
                <div><div class="nav-menu-title">Interview Guide</div><div class="nav-menu-desc">25 validation questions</div></div>
              </a>
              <a href="/dewmonday/brand/#validation-scorecard" class="nav-menu-item">
                <span class="nav-menu-emoji">ð</span>
                <div><div class="nav-menu-title">Concept Scorecard</div><div class="nav-menu-desc">All 6 concepts rated</div></div>
              </a>
            </div>
          </div>'''

# Also need to ensure the JS toggleDD function exists.
# Pattern to find: the existing Concepts dropdown closing </div> tag inside nav-left,
# just before the nav CTA button / end of nav-left.
# Strategy: find the nav-cta anchor tag and inject the Brand dropdown just before it.

# Pattern 1: nav-cta as <a ...class="nav-cta"...>
NAV_CTA_PATTERN = re.compile(
    r'(<a[^>]*class=["\'][^"\']*nav-cta[^"\']*["\'][^>]*>)',
    re.DOTALL
)

# Pattern 2: nav-cta class in different order
NAV_CTA_PATTERN2 = re.compile(
    r'(<a[^>]*nav-cta[^>]*href[^>]*>)',
    re.DOTALL
)

# JS toggleDD function â needed on pages that might use older JS pattern
TOGGLE_DD_JS = """
  function toggleDD(id) {
    const dd = document.getElementById(id);
    const isOpen = dd.classList.contains('open');
    document.querySelectorAll('.nav-dropdown.open').forEach(d => d.classList.remove('open'));
    if (!isOpen) dd.classList.add('open');
  }
  document.addEventListener('click', function(e) {
    if (!e.target.closest('.nav-dropdown')) {
      document.querySelectorAll('.nav-dropdown.open').forEach(d => d.classList.remove('open'));
    }
  });"""

def process_file(path_str):
    p = pathlib.Path(path_str)
    if not p.exists():
        print(f"  â ï¸  NOT FOUND: {path_str}")
        return

    content = p.read_text(encoding="utf-8")

    # Skip if already patched
    if "dd-brand" in content or "/dewmonday/brand/#overview" in content:
        print(f"  â Already has Brand dropdown: {path_str}")
        return

    # Try to find the nav-cta anchor to inject before it
    match = NAV_CTA_PATTERN.search(content)
    if not match:
        match = NAV_CTA_PATTERN2.search(content)

    if not match:
        print(f"  â Could not find nav-cta anchor in: {path_str}")
        return

    # Inject Brand dropdown just before the nav-cta anchor
    insert_pos = match.start()
    new_content = content[:insert_pos] + BRAND_DROPDOWN + "\n          " + content[insert_pos:]

    # Also ensure toggleDD JS is present (some older pages may use different JS)
    if "toggleDD" not in new_content:
        # Find closing </script> tag in the body area
        script_close = new_content.rfind("</script>")
        if script_close != -1:
            new_content = new_content[:script_close] + TOGGLE_DD_JS + "\n" + new_content[script_close:]
        else:
            # Append script before </body>
            new_content = new_content.replace(
                "</body>",
                f"<script>{TOGGLE_DD_JS}\n</script>\n</body>"
            )

    p.write_text(new_content, encoding="utf-8")
    print(f"  â Updated: {path_str}")


print("=== Adding Brand dropdown to nav on all pages ===\n")
for f in FILES:
    process_file(f)

print("\n=== Done. Commit with: ===")
print("git add .")
print('git commit -m "feat: add Brand dropdown to nav on all pages"')
print("git push")
