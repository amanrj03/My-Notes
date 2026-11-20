with open("raw_notes/NumberTheory&Cryptography/22.txt", 'r', encoding='utf-8') as f:
    text = f.read()

import re

# search for all headings and see what follows them
headings = re.findall(r'(##+ [^\n]+)', text)
for h in headings:
    print(h)
