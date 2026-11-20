import glob
import re

for f in sorted(glob.glob("*.html")):
    content = open(f, encoding='utf-8').read()
    m = re.findall(r'\\+\[\d+pt\\+\]', content)
    if m:
        print(f"{f}: found {m}")
    m2 = re.findall(r'\\+\[\s*\d+pt', content)
    if m2:
        print(f"{f} (m2): found {m2}")
