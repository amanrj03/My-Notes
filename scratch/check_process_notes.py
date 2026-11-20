with open("scratch/build_modules_14_to_18.py", 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find("def process_raw_notes_for_module")
print(text[idx:idx+1500])
