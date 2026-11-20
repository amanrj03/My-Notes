import os
import glob
import re

print("=== CHECKING FOR SHORT/FLATTENED PARAGRAPHS IN ALL HTML FILES ===")

for path in sorted(glob.glob("*.html")):
    with open(path, 'r', encoding='utf-8') as f:
        html = f.read()

    # Find consecutive paragraphs that have <= 5 characters each
    # e.g. <p><strong>O</strong></p>\n<p><strong>R</strong></p>
    p_tags = re.findall(r'<p>(?:<strong>)?([A-Za-z0-9_\-\s]{1,4})(?:</strong>)?</p>', html)
    
    # search directly for patterns in html: 3 or more consecutive <p>...single char...</p>
    matches = list(re.finditer(r'(?:<p>(?:<strong>)?([A-Za-z0-9_]{1,3})(?:</strong>)?</p>\s*){3,}', html))
    if matches:
        print(f"\n[HTML FILE] {path}:")
        for m in matches:
            sub = m.group(0).replace('\n', ' ')
            # get surrounding text
            start = max(0, m.start() - 60)
            end = min(len(html), m.end() + 60)
            print(f"  Pos {m.start()}: {sub[:100]}...")
            print(f"    Context: {html[start:end][:160]}...")
