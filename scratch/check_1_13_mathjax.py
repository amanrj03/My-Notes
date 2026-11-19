import re

for m in range(1, 14):
    fname = f"blockchain-module-{m}.html"
    with open(fname, 'r', encoding='utf-8') as f:
        html = f.read()

    mj = re.search(r'MathJax\s*=\s*(\{.*?\});', html, re.DOTALL)
    if mj:
        cfg = mj.group(1)
        # Check if \[ \] is in displayMath
        has_bracket = r"'\['" in cfg or r'"\["' in cfg or r"'\\['" in cfg or r'"\\["' in cfg
        has_dollar = r"'$$'" in cfg or r'"$$"' in cfg
        print(f"{fname}: has_bracket={has_bracket}, has_dollar={has_dollar}")
    else:
        print(f"{fname}: NO MathJax found!")
