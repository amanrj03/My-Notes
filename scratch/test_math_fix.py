import re
import markdown

test_text = """
### **The most important message sequences**

Remember these three sequences:

**1. Connection establishment**

\\[ \\text{Version}\\rightarrow\\text{Verack} \\]

Both peers exchange version information and acknowledge the connection.

**2. Transaction or block exchange**

\\[ \\text{Inv}\\rightarrow\\text{Getdata}\\rightarrow\\text{Tx/Block} \\]

A node advertises information, another node requests the data, and the data is transferred.

**3. Peer discovery**

\\[ \\text{Getaddr}\\rightarrow\\text{Addr} \\]

A node requests information about peers and receives peer addresses.
"""

print("--- ORIGINAL RAW TEXT CHUNK ---")
print(test_text)

# Proposed regex:
math_display = []
def rep_disp(m):
    idx = len(math_display)
    content = m.group(1).strip()
    # Strip any accidental leading or trailing backslashes
    content = content.replace('₹', r'\text{₹}')
    math_display.append(content)
    return f"\n\nTOKEN_MATH_DISP_{idx}\n\n"

# Match 1 or 2 backslashes followed by [ and 1 or 2 backslashes followed by ]
cleaned = re.sub(r'\\{1,2}\[(.*?)\\{1,2}\]', rep_disp, test_text, flags=re.DOTALL)
print("--- AFTER TOKEN INJECTION ---")
print(cleaned)

html = markdown.markdown(cleaned, extensions=['tables', 'fenced_code', 'nl2br'])

for idx, content in enumerate(math_display):
    # Notice we clean up any <p> wrapping or whitespace
    html = html.replace(f"<p>TOKEN_MATH_DISP_{idx}</p>", f'<div class="math-display">\\[{content}\\]</div>')
    html = html.replace(f"TOKEN_MATH_DISP_{idx}", f'<div class="math-display">\\[{content}\\]</div>')

print("--- RESULTING HTML ---")
print(html)

# Check for stray backslashes
print("\nAny stray backslashes in HTML?", bool(re.search(r'<p>\s*\\', html)))
print("Any broken slash dollars in HTML?", bool(re.search(r'\\\$\$', html)))
