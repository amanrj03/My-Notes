with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
matches = [m.start() for m in re.finditer(r'Blockchain', text)]
print(f"Total Blockchain matches in index.html: {len(matches)}")
for m in matches[:5]:
    print(text[max(0, m-50):min(len(text), m+200)].replace('\n', ' '))
