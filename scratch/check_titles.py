import re

for i in range(1, 30):
    filename = f"maths-module-{i}.html"
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            c = f.read()
            m = re.search(r'<h1 class="math-banner-title">(.*?)</h1>', c)
            badge = re.search(r'<div class="math-badge">(.*?)</div>', c)
            b_text = badge.group(1) if badge else ""
            t_text = m.group(1) if m else "NOT FOUND"
            print(f"Mod {i:02d}: {t_text} | Badge: {b_text}")
    except Exception as e:
        print(f"Mod {i:02d}: ERROR {e}")
