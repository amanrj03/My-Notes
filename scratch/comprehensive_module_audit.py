import glob
import re

print("=== RUNNING DEEP COMPREHENSIVE AUDIT ACROSS ALL MODULES ===")

all_html = sorted(glob.glob("*.html"))
print(f"Total HTML files to inspect: {len(all_html)}")

findings = []

for f in all_html:
    with open(f, 'r', encoding='utf-8') as fp:
        html = fp.read()
    
    # Strip script and style
    body = re.sub(r'<script.*?</script>', '', html, flags=re.DOTALL)
    body = re.sub(r'<style.*?</style>', '', body, flags=re.DOTALL)
    
    # 1. Unparsed markdown pipe tables in body prose (not in <pre> or <code>)
    no_code = re.sub(r'<pre.*?</pre>', '', body, flags=re.DOTALL)
    no_code = re.sub(r'<code.*?</code>', '', no_code, flags=re.DOTALL)
    no_code = re.sub(r'<table.*?</table>', '', no_code, flags=re.DOTALL)
    
    pipe_tables = re.findall(r'(\|[^\n<]+\|[^\n<]+\|\s*<br\s*/?>\s*\|[\s:-]+\|)', no_code)
    if pipe_tables:
        findings.append((f, f"Unparsed markdown table in prose ({len(pipe_tables)} found)"))

    # 2. Consecutive short paragraphs (>= 3 paragraphs with <= 6 characters each)
    # e.g. <p>A</p><p>B</p><p>C</p>
    short_p_matches = re.findall(r'(?:<p>(?:<strong>)?(?:[A-Za-z0-9_\-\s]{1,6})(?:</strong>)?</p>\s*){3,}', no_code)
    if short_p_matches:
        for sm in short_p_matches:
            # check if it's not just some common list
            clean_sm = re.sub(r'\s+', ' ', sm)
            findings.append((f, f"Consecutive short paragraphs: {clean_sm[:120]}..."))

    # 3. Consecutive short bold paragraphs (>= 3)
    bold_p_matches = re.findall(r'(?:<p><strong>[^\n<]{1,10}</strong></p>\s*){4,}', no_code)
    if bold_p_matches:
        for bm in bold_p_matches:
            clean_bm = re.sub(r'\s+', ' ', bm)
            findings.append((f, f"Consecutive short bold paragraphs: {clean_bm[:120]}..."))

    # 4. Stray backslash before display math: e.g. <p>\</p> or <p>\</p><div class="math-display">
    stray_slash = re.findall(r'<p>\s*\\+\s*</p>', body)
    if stray_slash:
        findings.append((f, f"Stray backslash paragraphs: {len(stray_slash)}"))

    # 5. Raw LaTeX command visible in text without math delimiters
    # e.g. \rightarrow, \text{, \pmod, \frac outside of \( \) or \[ \] or $$ $$
    # let's remove all math blocks first
    no_math = re.sub(r'\\\(.*?\\\)', '', no_code, flags=re.DOTALL)
    no_math = re.sub(r'\\\[.*?\\\]', '', no_math, flags=re.DOTALL)
    no_math = re.sub(r'\$\$.*?\$\$', '', no_math, flags=re.DOTALL)
    no_math = re.sub(r'\$[^\$]+\$', '', no_math, flags=re.DOTALL)
    
    latex_leak = re.findall(r'(\\(?:rightarrow|leftarrow|text\{|pmod|frac\{|gcd|cdot|equiv|bmod|sum_)[^\s<]{0,30})', no_math)
    if latex_leak:
        findings.append((f, f"Unescaped/Leaked LaTeX outside math delimiters: {latex_leak[:5]}"))

print("\n=== SUMMARY OF FINDINGS ===")
if not findings:
    print("Zero issues found across all files!")
else:
    for f, msg in findings:
        print(f"[{f}]: {msg}")
