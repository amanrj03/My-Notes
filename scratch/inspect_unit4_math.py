import re

for m in range(14, 19):
    fname = f"raw_notes/blockchain/{m}.txt"
    with open(fname, 'r', encoding='utf-8') as f:
        text = f.read()

    # Find all \\[ ... \\] or \[ ... \]
    display_math = re.findall(r'\\{1,2}\[(.*?)\\{1,2}\]', text, re.DOTALL)
    inline_math = re.findall(r'\\{1,2}\((.*?)\\{1,2}\)', text, re.DOTALL)
    double_dollars = re.findall(r'\$\$(.*?)\$\$', text, re.DOTALL)
    
    print(f"=== Module {m} Raw Math ({fname}) ===")
    print(f"  display brackets: {len(display_math)}")
    for idx, d in enumerate(display_math):
        print(f"    [{idx}] {d.strip()}")
    print(f"  inline parens: {len(inline_math)}")
    for idx, im in enumerate(inline_math):
        print(f"    ({idx}) {im.strip()}")
    print(f"  double dollars: {len(double_dollars)}")
    for idx, dd in enumerate(double_dollars):
        print(f"    $${idx}$$ {dd.strip()}")
