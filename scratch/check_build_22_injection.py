with open("scratch/build_maths_18_to_29.py", 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find("elif mod_num == 22:")
print(text[idx:idx+400])
