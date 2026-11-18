import re

for i in (14, 15, 17, 18):
    path = f'raw_notes/blockchain/{i}.txt'
    with open(path, encoding='utf-8') as f:
        text = f.read()
    brackets = re.findall(r'\\\[[^]]+\\\]', text)
    print(f"Mod {i} sample brackets:", brackets[:5])
