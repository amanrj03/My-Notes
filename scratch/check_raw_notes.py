import re

for mod_num in range(1, 18):
    p = f"raw_notes/NumberTheory&Cryptography/{mod_num}.txt"
    with open(p, "r", encoding="utf-8") as fp:
        t = fp.read()
    
    # Delimiter counts
    disp_open = len(re.findall(r'\\\[', t))
    disp_close = len(re.findall(r'\\\]', t))
    inl_open = len(re.findall(r'\\\(', t))
    inl_close = len(re.findall(r'\\\)', t))
    
    lt_escaped = len(re.findall(r'\\<', t))
    gt_escaped = len(re.findall(r'\\>', t))
    
    lt_raw = len(re.findall(r'(?<!\\)<', t))
    gt_raw = len(re.findall(r'(?<!\\)>', t))
    
    status = "OK"
    if disp_open != disp_close or inl_open != inl_close:
        status = "MISMATCH"
    
    print(f"Mod {mod_num:2d}: disp: {disp_open:3d}/{disp_close:3d} | inl: {inl_open:3d}/{inl_close:3d} | \\<: {lt_escaped:2d} | \\>: {gt_escaped:2d} | <: {lt_raw:2d} | >: {gt_raw:2d} | {status}")
