import os
import re
import json
from extract_questions_18_29 import parse_module_questions

raw_dir = r"raw_notes/NumberTheory&Cryptography"

for m in range(18, 26):
    p = os.path.join(raw_dir, f"{m}.txt")
    with open(p, 'r', encoding='utf-8') as f:
        t = f.read()
    qs = parse_module_questions(t)
    print(f"\n================ MODULE {m} QUESTIONS ({len(qs)}) ================")
    for q in qs:
        print(f"Q{q['num']}: {q['text']}")
        for idx, o in enumerate(q['options']):
            print(f"   {'ABCD'[idx]}. {o}")
