import glob
import re

print("=== CHECKING ALL HTML FILES FOR ANOMALIES ===")

for f in sorted(glob.glob("*.html")):
    content = open(f, encoding='utf-8').read()
    
    # 1. Check for token leaks or corrupted math divs
    leaks = re.findall(r'</div>\d+</p>|TOKEN_[A-Z0-9_]+|MATHDISPTOKEN\d+END', content)
    if leaks:
        print(f"[{f}] LEAKS: {leaks}")
        
    # 2. Check for broken math tags like \$$ or <p>\</p>
    bad_math = re.findall(r'<p>\s*\\+\s*</p>|[^\\]\\\$\$', content)
    if bad_math:
        print(f"[{f}] BAD MATH: {bad_math}")
        
    # 3. Check for raw pipe tables outside pre/code/table
    no_code = re.sub(r'<pre.*?</pre>', '', content, flags=re.DOTALL)
    no_code = re.sub(r'<code.*?</code>', '', no_code, flags=re.DOTALL)
    no_code = re.sub(r'<table.*?</table>', '', no_code, flags=re.DOTALL)
    pipes = re.findall(r'(\|[^\n<]+\|[^\n<]+\|\s*<br\s*/?>\s*\|[\s:-]+\|)', no_code)
    if pipes:
        print(f"[{f}] RAW PIPES: {len(pipes)}")
        
    # 4. Check for 4+ consecutive short paragraphs
    short_ps = re.findall(r'(?:<p>(?:<strong>)?(?:[A-Za-z0-9_\-\s]{1,4})(?:</strong>)?</p>\s*){4,}', no_code)
    if short_ps:
        print(f"[{f}] SHORT PARAS: {len(short_ps)}")
