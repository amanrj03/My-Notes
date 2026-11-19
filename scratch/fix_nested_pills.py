import re

for m in range(9, 14):
    fname = f"blockchain-module-{m}.html"
    with open(fname, 'r', encoding='utf-8') as f:
        html = f.read()

    # Pattern: <span class="ref-pill">📄 Slides Reference: <span class="ref-pill">📄 Slides Reference: ([^<]+)</span></span>
    # Or variations
    original = html
    # Collapse double/nested ref-pill spans to a single clean span
    while re.search(r'<span class="ref-pill">(?:[^<]*\s*)<span class="ref-pill">(.*?)</span></span>', html):
        html = re.sub(
            r'<span class="ref-pill">(?:[^<]*\s*)<span class="ref-pill">(.*?)</span></span>',
            r'<span class="ref-pill">\1</span>',
            html
        )
    
    # Also clean up "teacher'<span class="ref-pill">...s PPT</span>"
    html = re.sub(r"teacher'<span class=\"ref-pill\">📄 Slides Reference: s ([^<]+)</span>",
                  r"<span class=\"ref-pill\">📄 Teacher's Slides Reference: \1</span>", html)

    if html != original:
        with open(fname, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f"✅ Fixed nested ref-pills in {fname}")
    else:
        print(f"No changes needed in {fname}")
