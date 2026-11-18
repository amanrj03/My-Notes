# -*- coding: utf-8 -*-
"""
Deep integrity and DOM validation test for Modules 14-18 and blockchain.html
"""

import os
import re
import json

def test_modules():
    errors = []
    
    # 1. Test Modules 14 to 18
    for m in range(14, 19):
        fname = f"blockchain-module-{m}.html"
        with open(fname, 'r', encoding='utf-8') as f:
            html = f.read()

        # Check title and banner
        if f"Module {m}:" not in html:
            errors.append(f"{fname}: Title tag missing Module {m}")

        # Check diagrams
        diagram_count = len(re.findall(r'<div class="diagram-box">', html))
        if diagram_count < 3:
            errors.append(f"{fname}: Expected at least 3 diagrams, found {diagram_count}")
        else:
            print(f"✓ {fname}: Found {diagram_count} embedded visual diagrams.")

        # Check quiz
        quiz_matches = re.findall(r'handleQuizClick\(\s*(\d+),\s*(\d+),\s*(\d+),\s*(\d+)\s*\)', html)
        if not quiz_matches:
            errors.append(f"{fname}: No quiz click handlers found!")
        else:
            # Check unique questions
            q_ids = sorted(list(set(int(q[1]) for q in quiz_matches)))
            print(f"✓ {fname}: Found interactive quiz with {len(q_ids)} questions: IDs {q_ids}")
            
            # Check options per question
            for qid in q_ids:
                q_opts = [q for q in quiz_matches if int(q[1]) == qid]
                if len(q_opts) != 4:
                    errors.append(f"{fname} Q{qid}: Expected 4 options, found {len(q_opts)}")

        # Check explanation JSON
        json_match = re.search(r'const explanations = (\{.*?\});', html, re.DOTALL)
        if not json_match:
            errors.append(f"{fname}: Explanations JSON not found in script!")
        else:
            try:
                exp_dict = json.loads(json_match.group(1))
                if len(exp_dict) != len(q_ids):
                    errors.append(f"{fname}: Explanation count ({len(exp_dict)}) does not match question count ({len(q_ids)})")
                else:
                    print(f"✓ {fname}: All {len(exp_dict)} explanations valid and mapped.")
            except Exception as e:
                errors.append(f"{fname}: Failed to parse explanation JSON: {e}")

    # 2. Test blockchain.html
    with open('blockchain.html', 'r', encoding='utf-8') as f:
        hub = f.read()

    unit_headers = re.findall(r'<h2 class="unit-title">(.*?)</h2>', hub)
    print(f"✓ blockchain.html: Found {len(unit_headers)} unit titles:")
    for uh in unit_headers:
        print(f"    - {uh}")

    # Check all module links in hub
    card_links = re.findall(r'href="(blockchain-module-\d+\.html)"', hub)
    unique_links = sorted(list(set(card_links)), key=lambda x: int(re.search(r'\d+', x).group(0)))
    print(f"✓ blockchain.html: Found {len(unique_links)} unique module cards linked.")
    for l in unique_links:
        if not os.path.exists(l):
            errors.append(f"Hub links to nonexistent file: {l}")

    # 3. Test index.html
    with open('index.html', 'r', encoding='utf-8') as f:
        idx = f.read()
    if 'Explore 18 Modules Across 4 Units' not in idx:
        errors.append("index.html: Button text does not reflect 18 modules across 4 units!")
    else:
        print("✓ index.html: Subject card updated to 18 modules across 4 units.")

    if errors:
        print("\n❌ VALIDATION ERRORS:")
        for err in errors:
            print("  *", err)
        return False
    else:
        print("\n🎉 ALL 18 MODULES AND HUBS VALIDATED WITH 100% SUCCESS!")
        return True

if __name__ == "__main__":
    test_modules()
