import os
import re

raw_dir = r"raw_notes/NumberTheory&Cryptography"

for i in range(18, 30):
    path = os.path.join(raw_dir, f"{i}.txt")
    with open(path, 'r', encoding='utf-8') as f:
        text = f.read()

    # Find any exam / mcq / practice questions
    print(f"\n=== MODULE {i} END SECTIONS ===")
    matches = re.findall(r'(?:##?|###?)\s+([^\n]*(?:Exam|MCQ|Question|Revision|Practice|Summary|Checklist)[^\n]*)', text, re.IGNORECASE)
    print("  Matches:", matches)
    
    # Check last 500 characters
    print("  Tail:", repr(text[-300:]))
