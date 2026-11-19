import os
import re

raw_dir = r"raw_notes/NumberTheory&Cryptography"

for i in range(18, 26):
    p = os.path.join(raw_dir, f"{i}.txt")
    with open(p, 'r', encoding='utf-8') as f:
        t = f.read()

    print(f"\n================ MODULE {i} ANSWER KEY / SOLUTIONS ================")
    m = re.findall(r'(?i)(?:answer\s*key|answers?|solutions?|explanations?)[^\n]*', t)
    print("Headings:", m)
    
    # Search for lines like "1. B" or "Answer: B" or "1. C"
    ans_lines = re.findall(r'(?m)^\s*(?:\d+[\.\)]\s*[A-D]\b|Answer:\s*[A-D]\b|[A-D]\s*[\-–]\s*.*)', t)
    print(f"Answer lines count: {len(ans_lines)}")
    for al in ans_lines[:15]:
        print("  ", al)
