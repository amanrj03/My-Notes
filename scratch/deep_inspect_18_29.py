import os
import re

raw_dir = r"raw_notes/NumberTheory&Cryptography"

for i in range(18, 30):
    path = os.path.join(raw_dir, f"{i}.txt")
    with open(path, 'r', encoding='utf-8') as f:
        text = f.read()

    lines = [l.strip() for l in text.splitlines() if l.strip()]
    first_20 = lines[:20]
    
    print(f"\n==================== MODULE {i} ====================")
    for l in first_20[:8]:
        print("  ", l)
    
    # Extract all top-level sections
    sections = re.findall(r'^(?:#|##)\s+(.*)', text, re.MULTILINE)
    print(f"  Total sections/headings: {len(sections)}")
    for s in sections[:10]:
        print("    ->", s)
