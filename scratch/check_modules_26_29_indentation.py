import re

for mod in [26, 27, 28, 29]:
    html_path = f"maths-module-{mod}.html"
    raw_path = f"raw_notes/NumberTheory&Cryptography/{mod}.txt"
    
    print(f"\n================ MODULE {mod} ================")
    try:
        html = open(html_path, encoding='utf-8').read()
        code_blocks = re.findall(r'<pre><code>(.*?)</code></pre>', html, flags=re.DOTALL)
        print(f"[{html_path}] Found {len(code_blocks)} <pre><code> blocks:")
        for idx, cb in enumerate(code_blocks):
            clean = cb.strip().replace('\n', ' ')
            print(f"  Block #{idx+1} ({len(cb)} chars): {clean[:140]}...")
    except Exception as e:
        print(f"Error reading {html_path}: {e}")

    try:
        raw = open(raw_path, encoding='utf-8').read()
        # Find lines starting with 4 or more spaces that are not empty
        indented_lines = []
        for line_num, line in enumerate(raw.splitlines()):
            if re.match(r'^(?: {4,}|\t+)[^\s]', line):
                indented_lines.append((line_num+1, line))
        print(f"[{raw_path}] Found {len(indented_lines)} lines with 4+ spaces/tabs indentation:")
        for ln, l in indented_lines[:15]:
            print(f"  L{ln}: {repr(l[:80])}")
        if len(indented_lines) > 15:
            print(f"  ... and {len(indented_lines)-15} more indented lines")
    except Exception as e:
        print(f"Error reading {raw_path}: {e}")
