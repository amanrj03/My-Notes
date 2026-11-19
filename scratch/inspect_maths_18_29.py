import os
import re

raw_dir = r"raw_notes/NumberTheory&Cryptography"

print("=== INSPECTING MODULES 18 TO 29 ===")
for i in range(18, 30):
    path = os.path.join(raw_dir, f"{i}.txt")
    if not os.path.exists(path):
        print(f"Missing: {i}.txt")
        continue
    with open(path, 'r', encoding='utf-8') as f:
        text = f.read()

    lines = [l.strip() for l in text.splitlines() if l.strip()]
    first_lines = lines[:5]
    title_match = re.search(r'^#\s+(?:Module\s+\d+[:\s—\-]+)?([^\n#]+)', text, re.IGNORECASE)
    title = title_match.group(1).strip() if title_match else first_lines[0]
    
    # Check sections / headings
    headings = re.findall(r'^(?:##?|###?)\s+(.*)', text, re.MULTILINE)
    
    # Check if quiz exists
    has_quiz = "test your understanding" in text.lower() or "practice mcq" in text.lower() or "quiz" in text.lower()
    
    # Check math delimiters
    single_brackets = len(re.findall(r'(?<!\\)\\\[(.*?)(?<!\\)\\\]', text, re.DOTALL))
    double_brackets = len(re.findall(r'\\\\\[(.*?)\\\\\]', text, re.DOTALL))
    inline_parens = len(re.findall(r'\\\((.*?)\\\)', text))
    
    print(f"\n--- Module {i}: {title} ({len(text)} chars) ---")
    print(f"   Headings count: {len(headings)}")
    for h in headings[:6]:
        print(f"     • {h}")
    print(f"   Quiz section: {has_quiz}")
    print(f"   Math: single_brackets={single_brackets}, double_brackets={double_brackets}, inline_parens={inline_parens}")
