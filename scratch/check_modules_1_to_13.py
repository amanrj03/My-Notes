import re

for m in range(1, 14):
    fname = f"blockchain-module-{m}.html"
    with open(fname, 'r', encoding='utf-8') as f:
        html = f.read()

    # Find MathJax config
    mj = re.search(r'MathJax = \{.*?\};', html, re.DOTALL)
    mj_cfg = mj.group(0) if mj else "NO MATHJAX"
    
    # Check if this module actually has math
    math_divs = len(re.findall(r'class="math-display"', html))
    inline_math = len(re.findall(r'class="math-inline"', html))
    dollar_math = len(re.findall(r'\$\$', html))
    bracket_math = len(re.findall(r'\\\[', html))
    
    print(f"{fname}: MathJax={bool(mj)}, math-display={math_divs}, math-inline={inline_math}, $$={dollar_math}, \\\[={bracket_math}")
