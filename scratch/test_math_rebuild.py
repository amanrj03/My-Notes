import re
import markdown
import os

RAW_DIR = r"raw_notes/blockchain"

for mod_num in [14, 15, 16, 17, 18]:
    raw_path = os.path.join(RAW_DIR, f"{mod_num}.txt")
    with open(raw_path, 'r', encoding='utf-8') as f:
        body_raw = f.read()

    # Protect MathJax display math
    math_display = []
    def rep_disp(m):
        idx = len(math_display)
        content = m.group(1).strip()
        content = content.replace('₹', r'\text{₹}')
        math_display.append(content)
        return f"\n\nTOKEN_MATH_DISP_{idx}\n\n"

    body_raw = re.sub(r'\\+\[(.*?)\\+\]', rep_disp, body_raw, flags=re.DOTALL)
    body_raw = re.sub(r'\$\$(.*?)\$\$', rep_disp, body_raw, flags=re.DOTALL)

    math_inline = []
    def rep_inline(m):
        idx = len(math_inline)
        content = m.group(1).strip()
        content = content.replace('₹', r'\text{₹}')
        math_inline.append(content)
        return f"TOKEN_MATH_INL_{idx}"

    body_raw = re.sub(r'\\+\((.*?)\\+\)', rep_inline, body_raw)

    body_html = markdown.markdown(body_raw, extensions=['tables', 'fenced_code', 'nl2br'])

    for idx, content in enumerate(math_display):
        body_html = body_html.replace(f"<p>TOKEN_MATH_DISP_{idx}</p>", f'<div class="math-display">\\[{content}\\]</div>')
        body_html = body_html.replace(f"TOKEN_MATH_DISP_{idx}", f'<div class="math-display">\\[{content}\\]</div>')

    for idx, content in enumerate(math_inline):
        body_html = body_html.replace(f"<p>TOKEN_MATH_INL_{idx}</p>", f'<span class="math-inline">\\({content}\\)</span>')
        body_html = body_html.replace(f"TOKEN_MATH_INL_{idx}", f'<span class="math-inline">\\({content}\\)</span>')

    # Safety cleanup: remove any empty or stray paragraph backslashes
    body_html = re.sub(r'<p>\s*\\+\s*</p>', '', body_html)
    body_html = re.sub(r'<p>\s*\\+<div', '<div', body_html)
    body_html = re.sub(r'</div>\s*\\+</p>', '</div>', body_html)

    # Check results
    stray_bs = re.findall(r'<p>\s*\\', body_html)
    broken_dollars = re.findall(r'\\\$\$', body_html)
    math_divs = len(re.findall(r'class="math-display"', body_html))

    print(f"Mod {mod_num}: math-display count={math_divs}, stray_bs={len(stray_bs)}, broken_dollars={len(broken_dollars)}")
    if mod_num == 14:
        idx1 = body_html.find("Connection establishment")
        if idx1 != -1:
            print("--- Mod 14 sample output around message sequences ---")
            print(body_html[idx1:idx1+700])
