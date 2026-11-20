import re

with open("raw_notes/blockchain/18.txt", 'r', encoding='utf-8') as f:
    text = f.read()

# Find all display math in 18.txt
math_blocks = re.findall(r'\\\[(.*?)\\\]', text, flags=re.DOTALL)
print(f"Total display math blocks in 18.txt: {len(math_blocks)}")
for i, m in enumerate(math_blocks):
    print(f"[{i}]: {m.strip()[:60]}")
