import os
import glob
import re

print("=== CHECKING FOR FLATTENED SINGLE-LETTER LINES & ARTIFACTS ===")

# Check for patterns like consecutive lines with just single characters or short items
for path in sorted(glob.glob("raw_notes/**/*.txt", recursive=True)):
    with open(path, 'r', encoding='utf-8') as f:
        lines = [line.strip() for line in f.readlines()]
    
    # check for streaks of single bold characters or single characters
    streak = []
    found_streaks = []
    for i, line in enumerate(lines):
        # matches **X** or single letter or digit
        m = re.match(r'^\*{0,2}([A-Za-z0-9])\*{0,2}$', line)
        if m:
            streak.append((i+1, m.group(1), line))
        else:
            if len(streak) >= 4:
                found_streaks.append(streak)
            streak = []
    if len(streak) >= 4:
        found_streaks.append(streak)
        
    if found_streaks:
        print(f"\n[RAW NOTE] {path}:")
        for s in found_streaks:
            letters = "".join([x[1] for x in s])
            print(f"  Line {s[0][0]}-{s[-1][0]} (len {len(s)}): {letters} -> {[x[2] for x in s[:6]]}...")

    # Check for keywords like "Blue row", "Green row", table fragments
    content = "\n".join(lines)
    for kw in ["Blue row", "Green row", "Plaintext\n\nBlue", "Row 1", "Row 2", "Column 1"]:
        if kw.lower() in content.lower():
            print(f"  Keyword '{kw}' found in {path}")
