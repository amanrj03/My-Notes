import re

for i in range(14, 19):
    path = f'raw_notes/blockchain/{i}.txt'
    with open(path, encoding='utf-8') as f:
        text = f.read()
    dollars = re.findall(r'\$[^\$\n]+\$', text)
    parens = re.findall(r'\\\([^)]+\\\)', text)
    brackets = re.findall(r'\\\[[^]]+\\\]', text)
    print(f"Mod {i}: inline dollars={len(dollars)}, parens={len(parens)}, brackets={len(brackets)}")
    if dollars:
        print("  sample dollar:", dollars[:3])
    if parens:
        print("  sample paren:", parens[:3])
