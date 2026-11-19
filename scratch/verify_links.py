import glob
import re
import os

html_files = sorted(glob.glob("*.html"))
all_file_set = set(html_files)

broken_links = []
for f in html_files:
    content = open(f, 'r', encoding='utf-8').read()
    links = re.findall(r'href="([^"#\?:]+\.html)"', content)
    for target in links:
        if target not in all_file_set:
            broken_links.append((f, target))

if not broken_links:
    print(f"✅ All internal HTML links across {len(html_files)} files resolve perfectly!")
else:
    print(f"❌ Found {len(broken_links)} broken links:")
    for src, tgt in broken_links[:20]:
        print(f"  In {src} -> {tgt}")
