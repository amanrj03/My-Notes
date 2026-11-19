import glob
import re
import os

all_html = sorted(glob.glob("*.html"))
print(f"Total HTML files found: {len(all_html)}")

for fname in all_html:
    with open(fname, 'r', encoding='utf-8') as f:
        html = f.read()

    # Remove scripts to avoid false positives in JS code
    content_only = re.sub(r'<script.*?</script>', '', html, flags=re.DOTALL)

    # 1. Check for stray backslashes:
    # <p>\<div ...
    # <p>\</p>
    # <p>\
    # \<div
    stray_bs = re.findall(r'(?:<p>)?\s*\\\s*(?:<div|<span|<p|\\|$$|\$)', content_only)
    stray_bs_raw = re.findall(r'<p>\s*\\(?:\s*<br\s*/?>)?\s*</p>', content_only)
    stray_bs_div = re.findall(r'<p>\s*\\<div', content_only)

    # 2. Check for broken math delimiters:
    # \$$ or \$$</div>
    broken_dollar_close = re.findall(r'\\+\$\$', content_only)
    # $$ ... \$$
    # Or unrendered math with literal $$ or \[
    literal_brackets = re.findall(r'\\\[(.*?)\\\]', content_only, re.DOTALL)
    literal_parens = re.findall(r'\\\((.*?)\\\)', content_only, re.DOTALL)
    
    # 3. Check for \text without math mode or broken math
    raw_tex_in_html = re.findall(r'\\text\{[^}]+\}', content_only)
    # Check if inside math-display or math-inline or delimiters
    
    issues = []
    if stray_bs_div:
        issues.append(f"stray_bs_div: {len(stray_bs_div)}")
    if stray_bs_raw:
        issues.append(f"stray_bs_raw: {len(stray_bs_raw)}")
    if broken_dollar_close:
        issues.append(f"broken_dollar_close: {len(broken_dollar_close)}")
    if literal_brackets and not fname.startswith("maths-"):
        # (In maths modules, MathJax might configure \[ \])
        issues.append(f"literal_brackets: {len(literal_brackets)}")

    if issues:
        print(f"⚠️ {fname}: {', '.join(issues)}")
        # Print sample
        for m in (stray_bs_div + broken_dollar_close)[:2]:
            print(f"     Sample: {m}")
