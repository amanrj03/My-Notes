with open("scratch/build_modules_14_to_18.py", 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find("def inject_module_14_tokens")
print(text[idx:idx+1500])
