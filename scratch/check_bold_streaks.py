import glob
import re

for num in range(18, 30):
    path = f"raw_notes/NumberTheory&Cryptography/{num}.txt"
    try:
        with open(path, 'r', encoding='utf-8') as f:
            lines = [l.strip() for l in f.readlines()]
    except:
        continue
        
    print(f"\n--- Checking Module {num} ---")
    
    # Check for consecutive lines with bold letters or words
    bold_lines = []
    for idx, l in enumerate(lines):
        if re.match(r'^\*\*[A-Za-z0-9\s]{1,10}\*\*$', l):
            bold_lines.append((idx+1, l))
        else:
            if len(bold_lines) >= 3:
                print(f"  Streak of bold lines {bold_lines[0][0]}-{bold_lines[-1][0]} ({len(bold_lines)} items):")
                for bl in bold_lines[:15]:
                    print(f"    {bl[0]}: {bl[1]}")
                if len(bold_lines) > 15:
                    print(f"    ... and {len(bold_lines)-15} more")
            bold_lines = []
    if len(bold_lines) >= 3:
        print(f"  Streak of bold lines {bold_lines[0][0]}-{bold_lines[-1][0]} ({len(bold_lines)} items):")
        for bl in bold_lines[:15]:
            print(f"    {bl[0]}: {bl[1]}")

    # Check for "Plaintext" followed closely by single letters or lines
    for idx, l in enumerate(lines):
        if "plaintext" in l.lower() and idx + 5 < len(lines):
            sub = lines[idx:idx+8]
            # check if subsequent lines are single words or letters
            short_sub = [x for x in sub[1:6] if x and len(x) <= 8 and not x.startswith('#')]
            if len(short_sub) >= 3:
                print(f"  Plaintext followed by short lines at {idx+1}: {sub[:6]}")
