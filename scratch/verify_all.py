import os
import re

print("="*60)
print("AUDITING MATHEMATICS SUITE (17 MODULES + HUBS)")
print("="*60)

errors = 0
modules_checked = 0

for i in range(1, 18):
    fname = f"maths-module-{i}.html"
    fpath = os.path.join("d:/Blockchain HTML/Django HTML", fname)
    if not os.path.exists(fpath):
        print(f"[FAIL] Missing {fname}")
        errors += 1
        continue
    
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()
    
    size_kb = len(content) / 1024
    
    # Checks
    has_mathjax = "tex-mml-chtml.js" in content
    has_quiz = "checkMathQuiz" in content and "q-block" in content
    has_theme = "#7c3aed" in content or "math-theme" in content or "Imperial Oxford Amethyst" in content or "mod-badge" in content
    has_next_nav = f"maths-module-{i+1}.html" in content if i < 17 else True
    has_prev_nav = f"maths-module-{i-1}.html" in content if i > 1 else True
    
    # Bad tokens
    bad_tokens = re.findall(r'_MATH_[A-Z0-9_]+', content)
    
    status = "OK"
    if not has_mathjax or not has_quiz or bad_tokens:
        status = "WARN"
        errors += 1
    
    print(f"Mod {i:02d}: {fname:20s} | {size_kb:5.1f} KB | MathJax: {has_mathjax} | Quiz: {has_quiz} | BadTokens: {len(bad_tokens)} | {status}")
    modules_checked += 1

# Hub checks
maths_hub = "d:/Blockchain HTML/Django HTML/maths.html"
index_hub = "d:/Blockchain HTML/Django HTML/index.html"

with open(maths_hub, "r", encoding="utf-8") as f:
    mh_content = f.read()

maths_hub_ok = all(f"maths-module-{i}.html" in mh_content for i in range(1, 18))
print(f"maths.html: {len(mh_content)/1024:.1f} KB | All 17 module links present: {maths_hub_ok}")

with open(index_hub, "r", encoding="utf-8") as f:
    ih_content = f.read()

index_hub_ok = "maths.html" in ih_content and "Mathematics (17)" in ih_content and "maths-module-1.html" in ih_content
print(f"index.html: {len(ih_content)/1024:.1f} KB | Mathematics active dropdown & card present: {index_hub_ok}")

print("="*60)
if errors == 0 and maths_hub_ok and index_hub_ok:
    print("ALL AUDITS PASSED PERFECTLY (0 errors, 17/17 verified)!")
else:
    print(f"AUDIT FOUND {errors} ISSUES.")
