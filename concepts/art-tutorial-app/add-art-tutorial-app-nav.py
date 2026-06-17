#!/usr/bin/env python3
"""
add-art-tutorial-app-nav.py
Adds Art Tutorial App as the 6th entry in the Concepts nav dropdown
on all 5 existing concept pages.

Run from the repo root:
  python3 add-art-tutorial-app-nav.py

Files updated:
  concepts/creator-hub/index.html
  concepts/art-dropshipping/index.html
  concepts/camera-dropshipping/index.html
  concepts/little-makers/index.html
  concepts/tutorial-app/index.html
"""

import re, pathlib

FILES = [
    "concepts/creator-hub/index.html",
    "concepts/art-dropshipping/index.html",
    "concepts/camera-dropshipping/index.html",
    "concepts/little-makers/index.html",
    "concepts/tutorial-app/index.html",
]

# The new nav entry to inject (with divider)
NEW_ENTRY = '''          <div class="nav-menu-divider"></div>
          <a href="/dewmonday/concepts/art-tutorial-app/" class="nav-menu-item">
            <span class="nav-menu-emoji">🖌️</span>
            <div><div class="nav-menu-title">Art Tutorial App</div><div class="nav-menu-desc">Structured art education</div></div>
          </a>'''

# Pattern: the Tutorial App nav-menu-item block (last item before closing </div>)
# We look for the anchor tag that links to /concepts/tutorial-app/ and find its closing </a>
TUTORIAL_APP_PATTERN = re.compile(
    r'(<a[^>]*href=["\'](?:[^"\']*)/concepts/tutorial-app/["\'][^>]*class=["\']nav-menu-item["\'][^>]*>.*?</a>)',
    re.DOTALL
)

# Also handle the reverse attribute order: class before href
TUTORIAL_APP_PATTERN2 = re.compile(
    r'(<a[^>]*class=["\']nav-menu-item["\'][^>]*href=["\'](?:[^"\']*)/concepts/tutorial-app/["\'][^>]*>.*?</a>)',
    re.DOTALL
)

def process_file(path_str):
    p = pathlib.Path(path_str)
    if not p.exists():
        print(f"  ⚠️  NOT FOUND: {path_str}")
        return

    content = p.read_text(encoding="utf-8")

    # Skip if already patched
    if "/concepts/art-tutorial-app/" in content:
        print(f"  ✅ Already has Art Tutorial App entry: {path_str}")
        return

    # Try pattern 1
    match = TUTORIAL_APP_PATTERN.search(content)
    if not match:
        match = TUTORIAL_APP_PATTERN2.search(content)

    if not match:
        print(f"  ❌ Could not find Tutorial App nav entry in: {path_str}")
        return

    # Insert new entry right after the Tutorial App </a>
    insert_pos = match.end()
    new_content = content[:insert_pos] + "\n" + NEW_ENTRY + content[insert_pos:]
    p.write_text(new_content, encoding="utf-8")
    print(f"  ✅ Updated: {path_str}")

print("=== Adding Art Tutorial App to Concepts nav ===\n")
for f in FILES:
    process_file(f)

print("\n=== Done. Commit with: ===")
print("git add concepts/")
print('git commit -m "feat: add Art Tutorial App to nav dropdown on all concept pages"')
print("git push")
