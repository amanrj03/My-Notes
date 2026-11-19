import glob
import re

matches = []
for f in glob.glob("*.html"):
    try:
        txt = open(f, encoding='utf-8').read()
        if re.search(r'Mathematics \(\d+\)', txt):
            m = re.findall(r'Mathematics \(\d+\)', txt)
            matches.append((f, set(m)))
    except:
        pass

for f, m in matches:
    print(f"{f}: {m}")
