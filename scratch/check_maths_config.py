import re

with open('maths.html', 'r', encoding='utf-8') as f:
    text = f.read()

print("Maths.html literal brackets samples:")
for m in re.findall(r'\\\[(.*?)\\\]', text)[:3]:
    print("   ", m)

print("Maths.html MathJax config:")
m = re.search(r'MathJax = \{.*?\};', text, re.DOTALL)
if m:
    print(m.group(0))
else:
    print("No MathJax in maths.html!")

with open('maths-module-1.html', 'r', encoding='utf-8') as f:
    text1 = f.read()
m1 = re.search(r'MathJax = \{.*?\};', text1, re.DOTALL)
if m1:
    print("maths-module-1.html MathJax config:")
    print(m1.group(0))
