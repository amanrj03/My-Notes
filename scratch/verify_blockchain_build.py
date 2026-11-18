# -*- coding: utf-8 -*-
"""
Verification script for all 18 Blockchain modules and syllabus hub.
"""

import os
import re

def verify():
    errors = []
    
    # Check blockchain.html
    if not os.path.exists('blockchain.html'):
        errors.append("blockchain.html missing!")
    else:
        with open('blockchain.html', 'r', encoding='utf-8') as f:
            bc_text = f.read()
        for i in range(1, 19):
            if f'data-mod="{i}"' not in bc_text:
                errors.append(f"blockchain.html missing card for module {i}!")
        for u in range(1, 5):
            if f'id="unit-{u}"' not in bc_text:
                errors.append(f"blockchain.html missing unit-{u} partition!")
        print("✓ blockchain.html verified: all 18 module cards & 4 unit partitions present.")

    # Check modules 1 to 18
    for i in range(1, 19):
        fname = f"blockchain-module-{i}.html"
        if not os.path.exists(fname):
            errors.append(f"{fname} missing!")
            continue
        
        with open(fname, 'r', encoding='utf-8') as f:
            content = f.read()
            
        size = len(content)
        if size < 30000:
            errors.append(f"{fname} file size suspicious: {size} bytes")

        # Check for unreplaced placeholders
        if '___MATH_' in content or '_MATH_' in content:
            errors.append(f"{fname} contains unresolved math placeholder!")

        # Check shared assets
        if 'shared.css' not in content:
            errors.append(f"{fname} missing shared.css link")
        if 'shared.js' not in content:
            errors.append(f"{fname} missing shared.js link")
        if 'MathJax' not in content:
            errors.append(f"{fname} missing MathJax config")

        # Check prev-next links
        if i == 1:
            if 'href="blockchain.html"' not in content:
                errors.append(f"{fname} missing link back to hub")
            if 'href="blockchain-module-2.html"' not in content:
                errors.append(f"{fname} missing link to module 2")
        elif i == 18:
            if 'href="blockchain-module-17.html"' not in content:
                errors.append(f"{fname} missing link to module 17")
            if 'href="blockchain.html"' not in content:
                errors.append(f"{fname} missing link to hub")
        else:
            if f'href="blockchain-module-{i-1}.html"' not in content:
                errors.append(f"{fname} missing link to module {i-1}")
            if f'href="blockchain-module-{i+1}.html"' not in content:
                errors.append(f"{fname} missing link to module {i+1}")

        # For modules 14-18, check diagrams and quiz
        if i in (14, 15, 16, 17, 18):
            if 'class="diagram-box"' not in content:
                errors.append(f"{fname} missing diagram-box!")
            if 'class="quiz-section-wrap"' not in content:
                errors.append(f"{fname} missing quiz-section-wrap!")
            if 'class="quiz-question-box"' not in content:
                errors.append(f"{fname} missing quiz-question-box!")
            
        print(f"✓ {fname} verified: {size:,} bytes")

    # Check index.html
    with open('index.html', 'r', encoding='utf-8') as f:
        idx_text = f.read()
    for i in range(1, 19):
        if f'blockchain-module-{i}.html' not in idx_text:
            errors.append(f"index.html searchData missing module {i}!")
    print("✓ index.html verified: all 18 blockchain modules in searchData.")

    if errors:
        print("\n❌ ERRORS FOUND:")
        for e in errors:
            print("  -", e)
    else:
        print("\n🎉 ALL VERIFICATION CHECKS PASSED WITH 100% SUCCESS!")

if __name__ == '__main__':
    verify()
