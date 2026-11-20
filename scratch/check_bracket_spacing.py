import glob
import re

for f in sorted(glob.glob("*.html")):
    content = open(f, encoding='utf-8').read()
    m = re.findall(r'\\\\+\[\d+pt\]', content)
    if m:
        print(f"{f}: found {len(m)} occurrences of \\\\+[...pt] -> {m}")
