#!/usr/bin/env python3
"""
inject-week4-css.py
Adds Drop card, Kit total, and Scorecard CSS to _layouts/default.html
Run from repo root: python3 inject-week4-css.py
"""
import re, os, sys

LAYOUT_FILE = "_layouts/default.html"

WEEK4_CSS = """
    /* ===== WEEK 4 — DROP CARDS ===== */
    .dm-drop-grid {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
      gap: 18px;
      margin: 28px 0;
    }
    .dm-drop-card {
      background: #FFFFFF;
      border: 1.5px solid #E2DDD6;
      border-radius: 14px;
      padding: 20px 20px 18px;
      display: flex;
      flex-direction: column;
      gap: 10px;
      transition: transform 0.18s, box-shadow 0.18s;
    }
    .dm-drop-card:hover { transform: translateY(-2px); box-shadow: 0 6px 20px rgba(0,0,0,0.07); }
    .dm-drop-card.dm-drop-hero { border-top: 4px solid #2D5A27; grid-column: 1 / -1; display: grid; grid-template-columns: 56px 1fr; grid-template-rows: auto auto auto auto; column-gap: 16px; }
    .dm-drop-card-top { display: flex; justify-content: space-between; align-items: center; grid-column: 1 / 3; }
    .dm-drop-badge {
      font-family: 'JetBrains Mono', monospace; font-size: 0.7rem; font-weight: 700;
      text-transform: uppercase; letter-spacing: 0.06em;
      background: #E8F0E7; color: #2D5A27;
      padding: 3px 10px; border-radius: 20px;
    }
    .dm-drop-badge--audio { background: #E8F2F8; color: #3A7299; }
    .dm-drop-badge--light { background: #FFF3E0; color: #C0783A; }
    .dm-drop-badge--support { background: #F0EEF8; color: #7B6FA0; }
    .dm-drop-badge--storage { background: #E6F4F1; color: #3A8A7B; }
    .dm-drop-badge--hero { background: #2D5A27; color: white; }
    .dm-drop-price {
      font-family: 'JetBrains Mono', monospace; font-size: 0.9rem; font-weight: 700;
      color: #2D5A27;
    }
    .dm-drop-emoji { font-size: 2rem; line-height: 1; grid-column: 1; grid-row: 2; align-self: start; padding-top: 4px; }
    .dm-drop-name { font-family: 'DM Serif Display', serif; font-size: 1.1rem; color: #1C1C1C; line-height: 1.2; grid-column: 2; }
    .dm-drop-why { font-size: 0.85rem; color: #555; line-height: 1.6; grid-column: 2; }
    .dm-drop-card:not(.dm-drop-hero) .dm-drop-emoji { font-size: 1.8rem; }
    .dm-drop-card:not(.dm-drop-hero) .dm-drop-name { font-size: 1rem; }
    .dm-drop-specs {
      display: flex; flex-wrap: wrap; gap: 6px; margin-top: 4px;
      grid-column: 1 / 3;
    }
    .dm-drop-specs span {
      font-family: 'JetBrains Mono', monospace; font-size: 0.68rem;
      background: #F5F0E8; color: #6B6B6B;
      padding: 2px 8px; border-radius: 8px;
    }

    /* ===== KIT TOTAL BOX ===== */
    .dm-kit-total {
      background: #FFFFFF;
      border: 1.5px solid #E2DDD6;
      border-radius: 12px;
      overflow: hidden;
      margin: 28px 0;
    }
    .dm-kit-line {
      display: flex; justify-content: space-between; align-items: center;
      padding: 11px 20px;
      font-size: 0.88rem; color: #3A3A3A;
      border-bottom: 1px solid #F0ECE6;
    }
    .dm-kit-line:last-of-type { border-bottom: none; }
    .dm-kit-divider { height: 3px; background: linear-gradient(90deg, #2D5A27, #3D7035); }
    .dm-kit-total-row { font-weight: 700; font-size: 0.95rem; color: #1C1C1C; }
    .dm-kit-note {
      padding: 12px 20px;
      font-size: 0.78rem; color: #6B6B6B; line-height: 1.55;
      background: #FAF8F4;
      border-top: 1px solid #F0ECE6;
    }

    /* ===== SCORECARD TABLE ===== */
    .dm-scorecard {
      border: 1.5px solid #E2DDD6;
      border-radius: 12px;
      overflow: hidden;
      margin: 28px 0;
    }
    .dm-score-row {
      display: grid;
      grid-template-columns: 1fr repeat(5, 56px) 64px;
      align-items: center;
      gap: 4px;
      padding: 10px 16px;
      border-bottom: 1px solid #F0ECE6;
      font-size: 0.85rem;
    }
    .dm-score-row:last-child { border-bottom: none; }
    .dm-score-header {
      background: #1E3D1A;
      color: rgba(255,255,255,0.7);
      font-family: 'JetBrains Mono', monospace;
      font-size: 0.68rem;
      text-transform: uppercase;
      letter-spacing: 0.06em;
      font-weight: 600;
      padding: 10px 16px;
    }
    .dm-score-rank-1 { background: #F0F7EE; }
    .dm-score-rank-2 { background: #FAFAF8; }
    .dm-score-rank-3 { background: #FAFAF8; }
    .dm-score-concept { font-weight: 500; color: #1C1C1C; display: flex; align-items: center; gap: 8px; flex-wrap: wrap; }
    .dm-score-col { text-align: center; }
    .dm-score-total { text-align: center; font-weight: 700; }
    .dm-score-total--num { font-family: 'JetBrains Mono', monospace; font-size: 1rem; color: #2D5A27; }
    .dm-score-pill {
      display: inline-block; font-family: 'JetBrains Mono', monospace;
      font-size: 0.78rem; font-weight: 700;
      padding: 2px 8px; border-radius: 8px; min-width: 32px; text-align: center;
    }
    .dm-score-pill.high { background: #E8F0E7; color: #2D5A27; }
    .dm-score-pill.mid  { background: #FFF3E0; color: #C0783A; }
    .dm-score-pill.low  { background: #FAEEE6; color: #C0503A; }
    .dm-rank-badge {
      font-family: 'JetBrains Mono', monospace; font-size: 0.68rem; font-weight: 700;
      padding: 2px 8px; border-radius: 10px;
      background: #2D5A27; color: white;
      white-space: nowrap;
    }
    .dm-rank-badge--2 { background: #6BA3BE; }
    .dm-rank-badge--3 { background: #8A7B6A; }
    .dm-rank-badge--4 { background: #B0ADA8; color: #3A3A3A; }

    @media (max-width: 640px) {
      .dm-drop-card.dm-drop-hero { grid-template-columns: 1fr; }
      .dm-drop-card.dm-drop-hero .dm-drop-emoji { grid-column: 1; }
      .dm-drop-card.dm-drop-hero .dm-drop-name,
      .dm-drop-card.dm-drop-hero .dm-drop-why,
      .dm-drop-card.dm-drop-hero .dm-drop-specs { grid-column: 1; }
      .dm-score-row { grid-template-columns: 1fr repeat(3, 44px) 52px; font-size: 0.75rem; }
      .dm-score-row .dm-score-col:nth-child(4),
      .dm-score-row .dm-score-col:nth-child(5) { display: none; }
      .dm-score-header .dm-score-col:nth-child(4),
      .dm-score-header .dm-score-col:nth-child(5) { display: none; }
    }
    /* ===== END WEEK 4 ===== */
"""

def main():
    if not os.path.exists(LAYOUT_FILE):
        print(f"ERROR: {LAYOUT_FILE} not found. Run from repo root.")
        sys.exit(1)

    with open(LAYOUT_FILE, "r", encoding="utf-8") as f:
        content = f.read()

    if "dm-drop-grid" in content:
        print("Week 4 CSS already present. Nothing to do.")
        return

    match = re.search(r'(</style>)', content)
    if not match:
        print("ERROR: Could not find </style> tag.")
        sys.exit(1)

    insert_pos = match.start()
    new_content = content[:insert_pos] + WEEK4_CSS + "\n" + content[insert_pos:]

    with open(LAYOUT_FILE, "w", encoding="utf-8") as f:
        f.write(new_content)

    print(f"✅ Week 4 CSS injected into {LAYOUT_FILE}")

if __name__ == "__main__":
    main()
