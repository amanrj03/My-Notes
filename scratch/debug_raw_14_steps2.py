import sys
sys.path.append("scratch")
from build_modules_14_to_18 import inject_module_14_tokens
import re

raw_path = "raw_notes/blockchain/14.txt"
with open(raw_path, 'r', encoding='utf-8') as f:
    text = f.read()

text_injected = inject_module_14_tokens(text)
idx = text_injected.find("6.13 Important messages")
print("After inject_module_14_tokens:")
print(repr(text_injected[idx:idx+250]))

# Next: math regex
# What does math regex do?
math_display = []
def rep_disp(m):
    idx = len(math_display)
    content = m.group(1).strip()
    math_display.append(content)
    return f"\n\nTOKEN_MATH_DISP_{idx}_END\n\n"
text_math = re.sub(r'\\+\[(.*?)\\+\]', rep_disp, text_injected, flags=re.DOTALL)
text_math = re.sub(r'\$\$(.*?)\$\$', rep_disp, text_math, flags=re.DOTALL)
idx_m = text_math.find("6.13 Important messages")
print("\nAfter math regex:")
print(repr(text_math[idx_m:idx_m+250]))
