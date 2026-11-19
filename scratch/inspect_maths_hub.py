import re

with open('maths.html', 'r', encoding='utf-8') as f:
    text = f.read()

units = re.findall(r'<h2[^>]*class="unit-title"[^>]*>(.*?)</h2>', text)
print("Units in maths.html:", units)
if not units:
    units = re.findall(r'<h2[^>]*>(.*?)</h2>', text)
    print("All h2 in maths.html:", units)

modules = re.findall(r'href="(maths-module-\d+\.html)"[^>]*>.*?<h3>(.*?)</h3>', text, re.DOTALL)
print(f"Modules linked in maths.html: {len(modules)}")
for m, t in modules:
    print(f"  {m}: {t.strip()}")
