import re

regex = re.compile(r'\\+\[(.*?)\\+\]', re.DOTALL)

t1 = r'\[ 1\ BTC=₹50,00,000 \]'
m1 = regex.search(t1)
print("Single bracket test:", m1 is not None)
if m1:
    print("  content:", repr(m1.group(1)))

t2 = r'\\[ \text{Version}\rightarrow\text{Verack} \\]'
m2 = regex.search(t2)
print("Double bracket test:", m2 is not None)
if m2:
    print("  content:", repr(m2.group(1)))

t3 = r'\\( x + y = z \\)'
reg_inl = re.compile(r'\\+\((.*?)\\+\)')
m3 = reg_inl.search(t3)
print("Double paren test:", m3 is not None)
if m3:
    print("  content:", repr(m3.group(1)))

t4 = r'\( a = b \)'
m4 = reg_inl.search(t4)
print("Single paren test:", m4 is not None)
if m4:
    print("  content:", repr(m4.group(1)))
