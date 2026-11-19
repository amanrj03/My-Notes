import os
import re
import json

raw_dir = r"raw_notes/NumberTheory&Cryptography"

def parse_module_questions(text):
    # Regex to capture question blocks: **1. Question?** followed by A. B. C. D.
    # Or 1. Question? followed by A. B. C. D.
    q_blocks = []
    
    # Split text into lines
    lines = text.splitlines()
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        # Look for question number: **1. ...** or 1. ... or Q1. ...
        qm = re.match(r'^(?:\*\*)?(?:Q\s*)?(\d+)[\.\)]\s*(.*?)(?:\*\*)?$', line)
        if qm:
            q_num = int(qm.group(1))
            q_text = qm.group(2).strip()
            
            # Now look ahead for options A, B, C, D
            opts = []
            j = i + 1
            while j < len(lines):
                opt_line = lines[j].strip()
                om = re.match(r'^(?:\*\*)?([A-D])[\.\)]\s*(.*?)(?:\*\*)?$', opt_line)
                if om:
                    opts.append(om.group(2).strip())
                    if len(opts) == 4:
                        break
                elif opt_line.startswith('Submit') or opt_line.startswith('##') or re.match(r'^(?:\*\*)?\d+[\.\)]', opt_line):
                    # Reached next question or section
                    break
                j += 1
            
            if len(opts) == 4:
                q_blocks.append({
                    "num": q_num,
                    "text": q_text,
                    "options": opts
                })
                i = j
        i += 1
    return q_blocks

for m in range(18, 30):
    p = os.path.join(raw_dir, f"{m}.txt")
    with open(p, 'r', encoding='utf-8') as f:
        t = f.read()
    qs = parse_module_questions(t)
    print(f"Module {m}: parsed {len(qs)} questions")
    if qs:
        print(f"   Q1: {qs[0]['text']}")
        print(f"   Opts: {qs[0]['options']}")
