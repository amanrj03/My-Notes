import glob
import re

print("=== CHECKING FOR ANY FLATTENED ARTIFACTS IN RAW NOTES ===")

for txt in sorted(glob.glob("raw_notes/**/*.txt", recursive=True)):
    with open(txt, 'r', encoding='utf-8') as f:
        lines = [l.strip() for l in f.readlines()]
    
    # Check for words like "row", "column", "table", "alignment"
    # followed by strange short sequences
    for i, line in enumerate(lines):
        if any(w in line.lower() for w in ["alignment", "row", "column"]):
            # look ahead 10 lines
            ahead = [x for x in lines[i+1:i+15] if x]
            if len(ahead) >= 4 and all(len(x) <= 15 for x in ahead[:4]):
                print(f"[{txt}] Line {i+1}: '{line}' followed by short lines:")
                for a in ahead[:6]:
                    print(f"    {a}")
