import os
import re

raw_dir = r"raw_notes/NumberTheory&Cryptography"

for i in range(18, 30):
    p = os.path.join(raw_dir, f"{i}.txt")
    with open(p, 'r', encoding='utf-8') as f:
        t = f.read()

    # Find where the MCQ section begins
    mcq_start = None
    for pattern in [r'##\s+\*\*\d+\.\d+\s+Module\s+\d+\s+MCQ test\*\*', r'MCQ test', r'Multiple Choice Questions', r'Test your understanding']:
        m = re.search(pattern, t, re.IGNORECASE)
        if m:
            mcq_start = m.start()
            break
    
    print(f"\n================ MODULE {i} MCQ INSPECTION ================")
    if mcq_start:
        snippet = t[mcq_start:mcq_start+1500]
        print(snippet[:1000])
    else:
        print("No standard MCQ test heading found. Inspecting tail 1000 chars:")
        print(t[-1000:])
