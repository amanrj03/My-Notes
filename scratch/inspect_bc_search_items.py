with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
bc_items = re.findall(r'\{[^{}]*?"subj":\s*"Blockchain"[^{}]*?\}', text)
print(f"Total Blockchain search items in index.html: {len(bc_items)}")
for it in bc_items:
    print("  ", it[:80])
