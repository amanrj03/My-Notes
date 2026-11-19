import glob
import re
import os

print("=== CHECKING BLOCKCHAIN RAW NOTES ===")
for f in sorted(glob.glob('raw_notes/blockchain/*.txt'), key=lambda x: int(re.search(r'\d+', x).group())):
    with open(f, 'r', encoding='utf-8') as fp:
        t = fp.read()
    # Check for \\[, \[, \\(, \(
    double_bracket = len(re.findall(r'\\\\\[', t))
    single_bracket = len(re.findall(r'(?<!\\)\\\[', t))
    double_paren = len(re.findall(r'\\\\\(', t))
    single_paren = len(re.findall(r'(?<!\\)\\\(', t))
    double_dollars = len(re.findall(r'\$\$', t))
    print(f"{os.path.basename(f)}: \\\\[={double_bracket}, \\[={single_bracket}, \\\\(={double_paren}, \\(={single_paren}, $$={double_dollars}")

print("\n=== CHECKING ALL BLOCKCHAIN HTML FILES ===")
for f in sorted(glob.glob('blockchain-module-*.html'), key=lambda x: int(re.search(r'\d+', x).group())):
    with open(f, 'r', encoding='utf-8') as fp:
        html = fp.read()
    
    # Check for stray backslash in paragraph or inline
    stray_bs = re.findall(r'<p>\s*\\\s*<', html)
    stray_bs_lines = re.findall(r'<p>\s*\\\s*</p>', html)
    # Check for unrendered math delimiters in visible HTML (outside script tags)
    html_no_script = re.sub(r'<script.*?</script>', '', html, flags=re.DOTALL)
    unrendered_disp_math = re.findall(r'\$\$.*?\$\$', html_no_script)
    unrendered_brackets = re.findall(r'\\\[.*?\\\]', html_no_script)
    unrendered_slash_dollar = re.findall(r'\\\$\$', html_no_script)
    
    print(f"{f}: stray_bs={len(stray_bs)}, stray_bs_p={len(stray_bs_lines)}, unrendered_disp={len(unrendered_disp_math)}, slash_dollar={len(unrendered_slash_dollar)}, brackets={len(unrendered_brackets)}")
    if stray_bs or stray_bs_lines or unrendered_slash_dollar:
        for m in (stray_bs + stray_bs_lines + unrendered_slash_dollar)[:3]:
            print(f"   sample: {m}")

print("\n=== CHECKING MODULES 9 TO 13 DETAILS ===")
for m in range(9, 14):
    fname = f'blockchain-module-{m}.html'
    with open(fname, 'r', encoding='utf-8') as f:
        html = f.read()
    disp_divs = re.findall(r'<div class="math-display">.*?</div>', html, re.DOTALL)
    print(f"{fname}: math-display count={len(disp_divs)}")
    if disp_divs:
        print(f"   sample: {disp_divs[0]}")
    bs = re.findall(r'<p>\s*\\', html)
    print(f"{fname}: stray backslashes: {len(bs)}")

for f in sorted(glob.glob('raw_notes/maths/*.txt'), key=lambda x: int(re.search(r'\d+', x).group())):
    with open(f, 'r', encoding='utf-8') as fp:
        t = fp.read()
    double_bracket = len(re.findall(r'\\\\\[', t))
    single_bracket = len(re.findall(r'(?<!\\)\\\[', t))
    double_paren = len(re.findall(r'\\\\\(', t))
    single_paren = len(re.findall(r'(?<!\\)\\\(', t))
    double_dollars = len(re.findall(r'\$\$', t))
    if double_bracket or single_bracket or double_paren or single_paren or double_dollars:
        print(f"{os.path.basename(f)}: \\\\[={double_bracket}, \\[={single_bracket}, \\\\(={double_paren}, \\(={single_paren}, $$={double_dollars}")

print("\n=== CHECKING ALL MATHS HTML FILES ===")
for f in sorted(glob.glob('maths-module-*.html'), key=lambda x: int(re.search(r'\d+', x).group())):
    with open(f, 'r', encoding='utf-8') as fp:
        html = fp.read()
    html_no_script = re.sub(r'<script.*?</script>', '', html, flags=re.DOTALL)
    stray_bs = re.findall(r'<p>\s*\\\s*<', html)
    stray_bs_lines = re.findall(r'<p>\s*\\\s*</p>', html)
    unrendered_slash_dollar = re.findall(r'\\\$\$', html_no_script)
    # Check if maths modules use \\[ or $$ or \[
    brackets = re.findall(r'\\\[', html_no_script)
    parens = re.findall(r'\\\(', html_no_script)
    print(f"{f}: stray_bs={len(stray_bs)}, stray_bs_p={len(stray_bs_lines)}, slash_dollar={len(unrendered_slash_dollar)}, brackets={len(brackets)}, parens={len(parens)}")
