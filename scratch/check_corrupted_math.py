import glob
import re

for f in sorted(glob.glob("*.html")):
    content = open(f, encoding='utf-8').read()
    # Check for placeholder leaks like \]0 or \]\d+
    m = re.findall(r'\\\]\s*\d+', content)
    if m:
        print(f"[CORRUPTED MATH DELIMITER] {f}: found {m}")
    m2 = re.findall(r'\$\$\s*\d+', content)
    if m2:
        # filter out valid math where $$ is followed by a number like $$5x$$
        # we check if $$ is preceded by </div>
        pass
    m3 = re.findall(r'</div>\s*\d+\s*</p>', content)
    if m3:
        print(f"[CORRUPTED CLOSING DIV] {f}: found {m3}")
