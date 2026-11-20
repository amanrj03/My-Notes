import glob
import re

for f in sorted(glob.glob("blockchain-module-*.html")):
    content = open(f, encoding='utf-8').read()
    m = re.findall(r'</div>\d+</p>', content)
    if m:
        print(f"{f}: found {len(m)} corrupted closing divs!")
    m2 = re.findall(r'</span>\d+', content)
    if m2:
        print(f"{f}: found {len(m2)} corrupted inline spans!")
