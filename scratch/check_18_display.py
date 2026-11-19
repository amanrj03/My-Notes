import re

with open('blockchain-module-18.html', 'r', encoding='utf-8') as f:
    h = f.read()

matches = re.findall(r'<div class="math-display">.*?</div>', h, re.DOTALL)
print('Count of math-display in 18.html:', len(matches))
for m in matches[:5]:
    print("   ", m)
