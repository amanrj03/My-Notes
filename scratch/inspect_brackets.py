import re

for mod_num in range(1, 18):
    p = f"raw_notes/NumberTheory&Cryptography/{mod_num}.txt"
    with open(p, "r", encoding="utf-8") as fp:
        lines = fp.readlines()
    
    for idx, l in enumerate(lines):
        if "<" in l or ">" in l:
            # show line safe
            safe_l = l.strip()[:90].encode('ascii', errors='replace').decode('ascii')
            print(f"Mod {mod_num:2d}:{idx+1:4d} | {safe_l}")
