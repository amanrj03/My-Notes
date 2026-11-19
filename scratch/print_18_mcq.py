with open('raw_notes/NumberTheory&Cryptography/18.txt', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('Module 1 MCQ test')
print("=== MODULE 18 MCQ SECTION ===")
print(text[idx:idx+4000])
