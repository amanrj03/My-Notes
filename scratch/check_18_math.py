import re

with open('raw_notes/blockchain/18.txt', 'r', encoding='utf-8') as f:
    text = f.read()

single_bracket = re.findall(r'(?<!\\)\\\[(.*?)(?<!\\)\\\]', text, re.DOTALL)
print(f"18.txt single bracket matches: {len(single_bracket)}")
if single_bracket:
    for idx, sb in enumerate(single_bracket[:5]):
        print(f"  {idx}: {sb.strip()}")

# Also check blockchain-module-18.html
with open('blockchain-module-18.html', 'r', encoding='utf-8') as f:
    html = f.read()

unrendered = re.findall(r'\\\[|\\\]|\$\$|\$', html)
print(f"18.html unrendered math occurrences: {len(unrendered)}")
# Search for \\\[ or \\\] in 18.html
in_html = re.findall(r'(?:<p>)?\\\[.*?(?:\\\])?(?:</p>)?', html)
print(f"18.html matches for \\[: {len(in_html)}")
for h in in_html[:5]:
    print("  sample HTML:", h)
