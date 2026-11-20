with open("scratch/build_maths_18_to_29.py", 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find("card_mod22_")
print("card_mod22_ in script:", idx)
idx2 = text.find("maths-module-22")
print("maths-module-22 in script:", idx2)
