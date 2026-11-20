with open("scratch/build_modules_14_to_18.py", 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, l in enumerate(lines):
    if "TOKEN_MATH_DISP_" in l:
        print(f"Line {i+1}: {l.strip()}")
