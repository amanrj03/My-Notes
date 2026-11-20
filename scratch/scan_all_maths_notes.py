import glob
import re

for txt_path in sorted(glob.glob("raw_notes/NumberTheory&Cryptography/*.txt")):
    with open(txt_path, 'r', encoding='utf-8') as f:
        text = f.read()
    
    # Check for keywords that indicate table copy-paste
    suspicious = []
    for pattern in [r'\b(?:Blue|Green|Red|Yellow)\s+row\b', r'\b(?:Row|Column)\s+\d\b', r'\bAlignment\b', r'\bPlaintext\b.*?\bCiphertext\b']:
        matches = re.findall(pattern, text, re.IGNORECASE)
        if matches:
            suspicious.append(f"{pattern}: {len(matches)}")
            
    # Check for short line clusters (lines with <= 3 chars, appearing consecutively >= 3 times)
    lines = text.splitlines()
    short_cluster = []
    clusters = []
    for idx, line in enumerate(lines):
        s = line.strip()
        if s and len(s) <= 4 and not s.startswith('#') and not s.startswith('-') and not s.startswith('*'):
            short_cluster.append((idx+1, s))
        else:
            if len(short_cluster) >= 3:
                clusters.append(short_cluster)
            short_cluster = []
    if len(short_cluster) >= 3:
        clusters.append(short_cluster)
        
    if clusters or suspicious:
        print(f"\n=== {txt_path} ===")
        if suspicious:
            print("  Suspicious keywords:", suspicious)
        if clusters:
            for c in clusters:
                print(f"  Short cluster lines {c[0][0]}-{c[-1][0]} ({len(c)} items): {[x[1] for x in c]}")
