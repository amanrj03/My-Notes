import glob
import re

for path in sorted(glob.glob("*.html")):
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # check for | --- or |:--- or | - |
    m = re.findall(r'\|[\s:-]+\|', content)
    # Check if inside a <table tag or raw text
    # remove all <table>...</table>
    no_tables = re.sub(r'<table.*?</table>', '', content, flags=re.DOTALL)
    m_outside = re.findall(r'\|[\s:-]+\|', no_tables)
    if m_outside:
        print(f"[UNPARSED TABLE OUTSIDE TABLE TAG] {path}: found {len(m_outside)} occurrences!")
        for raw in re.findall(r'(\|[^\n<]+\|[^\n<]+\|\s*<br\s*/?>\s*\|[\s:-]+\|)', no_tables):
            print(f"   Example: {raw[:80]}...")
