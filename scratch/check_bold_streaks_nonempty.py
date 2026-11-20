import glob
import re

for num in range(1, 30):
    path = f"raw_notes/NumberTheory&Cryptography/{num}.txt"
    try:
        with open(path, 'r', encoding='utf-8') as f:
            lines = [l.strip() for l in f.readlines() if l.strip()]
    except:
        continue
        
    # Check for consecutive lines with bold letters or single words
    bold_lines = []
    for idx, l in enumerate(lines):
        if re.match(r'^\*\*[A-Za-z0-9\s]{1,10}\*\*$', l) or re.match(r'^[A-Za-z0-9\s]{1,3}$', l):
            bold_lines.append((idx+1, l))
        else:
            if len(bold_lines) >= 3:
                print(f"Mod {num} - Streak of {len(bold_lines)} lines around non-empty line {bold_lines[0][0]}:")
                for bl in bold_lines[:15]:
                    print(f"    {bl[1]}")
                if len(bold_lines) > 15:
                    print(f"    ... and {len(bold_lines)-15} more")
            bold_lines = []
    if len(bold_lines) >= 3:
        print(f"Mod {num} - Streak of {len(bold_lines)} lines around non-empty line {bold_lines[0][0]}:")
        for bl in bold_lines[:15]:
            print(f"    {bl[1]}")
