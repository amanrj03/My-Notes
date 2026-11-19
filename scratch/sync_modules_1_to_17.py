import re
import os

MODULE_TITLES = {
    1: "1. Divisibility and the Division Algorithm",
    2: "2. Modular Arithmetic and Congruences",
    3: "3. Integer Representations and Base Expansions",
    4: "4. Octal, Hexadecimal & Fast Base Conversions",
    5: "5. Algorithms for Integer Operations",
    6: "6. Prime and Composite Numbers",
    7: "7. Fundamental Theorem of Arithmetic",
    8: "8. Trial Division and the Sieve of Eratosthenes",
    9: "9. Prime Number Theorem and Prime Distribution",
    10: "10. GCD, LCM and the Euclidean Algorithm",
    11: "11. GCD as a Linear Combination (Bézout's Theorem)",
    12: "12. Linear Congruences and Modular Inverses",
    13: "13. Chinese Remainder Theorem (CRT)",
    14: "14. Computer Arithmetic with Large Integers",
    15: "15. Fermat's Little Theorem (FLT)",
    16: "16. Applications of Congruences",
    17: "17. Mixed MCQ Mastery and Final Revision",
    18: "18. Introduction to Cryptography & Security Models",
    19: "19. Classical Cryptography & Substitution Ciphers",
    20: "20. Shift Cipher and Caesar Cipher",
    21: "21. Affine Cipher & Modular Inverses",
    22: "22. Vigenère Polyalphabetic Cipher & Tableau",
    23: "23. Hill Cipher & Matrix Cryptography",
    24: "24. Permutation & Transposition Ciphers",
    25: "25. Mathematical Cryptosystems & Attack Models",
    26: "26. Foundations of Public Key Cryptography & Fast Modular Exponentiation",
    27: "27. Diffie-Hellman Key Exchange & Discrete Logarithm Problem",
    28: "28. The RSA Cryptosystem: Key Generation, Encryption & Decryption",
    29: "29. The ElGamal Cryptosystem & Comprehensive Unit V Exam Mastery"
}

def generate_navbar():
    return '''    <header class="global-navbar">
        <div class="nav-container">
            <a href="index.html" class="nav-brand">
                <span class="nav-brand-icon">⚡</span>
                <span class="nav-brand-text">OmniCourse<span class="nav-brand-accent">.Hub</span></span>
            </a>
            <div class="nav-links">
                <a href="index.html" class="nav-link"><span class="icon">🏠</span> All Subjects</a>
                
                <div class="nav-dropdown">
                    <button class="nav-dropdown-btn active" style="color: #a78bfa;"><span class="icon">📐</span> Mathematics (29) ▾</button>
                    <div class="nav-dropdown-menu">
                        <a href="maths.html" class="nav-dropdown-header" style="background: linear-gradient(135deg, #7c3aed, #4c1d95); color: #fff;">📋 Mathematics Syllabus Hub (All 29)</a>
                        <div class="dropdown-section-title" style="font-size: 10.5px; font-weight: 700; color: #7c3aed; padding: 4px 14px; text-transform: uppercase; background: rgba(124, 58, 237, 0.08);">Unit I: Divisibility & Base Expansions</div>
<a href="maths-module-1.html">Module 1: Divisibility and the Division Algorithm</a>
<a href="maths-module-2.html">Module 2: Modular Arithmetic and Congruences</a>
<a href="maths-module-3.html">Module 3: Integer Representations and Base Expansions</a>
<a href="maths-module-4.html">Module 4: Octal, Hexadecimal & Fast Base Conversions</a>
<a href="maths-module-5.html">Module 5: Algorithms for Integer Operations</a>
<div class="dropdown-section-title" style="font-size: 10.5px; font-weight: 700; color: #7c3aed; padding: 4px 14px; text-transform: uppercase; background: rgba(124, 58, 237, 0.08);">Unit II: Primes, Divisibility Tests & GCD</div>
<a href="maths-module-6.html">Module 6: Prime and Composite Numbers</a>
<a href="maths-module-7.html">Module 7: Fundamental Theorem of Arithmetic</a>
<a href="maths-module-8.html">Module 8: Trial Division and the Sieve of Eratosthenes</a>
<a href="maths-module-9.html">Module 9: Prime Number Theorem and Prime Distribution</a>
<a href="maths-module-10.html">Module 10: GCD, LCM and the Euclidean Algorithm</a>
<a href="maths-module-11.html">Module 11: GCD as a Linear Combination (Bézout's Theorem)</a>
<div class="dropdown-section-title" style="font-size: 10.5px; font-weight: 700; color: #7c3aed; padding: 4px 14px; text-transform: uppercase; background: rgba(124, 58, 237, 0.08);">Unit III: Congruences, CRT & Fermat/Euler</div>
<a href="maths-module-12.html">Module 12: Linear Congruences and Modular Inverses</a>
<a href="maths-module-13.html">Module 13: Chinese Remainder Theorem (CRT)</a>
<a href="maths-module-14.html">Module 14: Computer Arithmetic with Large Integers</a>
<a href="maths-module-15.html">Module 15: Fermat's Little Theorem (FLT)</a>
<a href="maths-module-16.html">Module 16: Applications of Congruences</a>
<a href="maths-module-17.html">Module 17: Mixed MCQ Mastery and Final Revision</a>
<div class="dropdown-section-title" style="font-size: 10.5px; font-weight: 700; color: #7c3aed; padding: 4px 14px; text-transform: uppercase; background: rgba(124, 58, 237, 0.08);">Unit IV: Classical Cryptography & Ciphers</div>
<a href="maths-module-18.html">Module 18: Introduction to Cryptography & Security Models</a>
<a href="maths-module-19.html">Module 19: Classical Cryptography & Substitution Ciphers</a>
<a href="maths-module-20.html">Module 20: Shift Cipher and Caesar Cipher</a>
<a href="maths-module-21.html">Module 21: Affine Cipher & Modular Inverses</a>
<a href="maths-module-22.html">Module 22: Vigenère Polyalphabetic Cipher & Tableau</a>
<a href="maths-module-23.html">Module 23: Hill Cipher & Matrix Cryptography</a>
<a href="maths-module-24.html">Module 24: Permutation & Transposition Ciphers</a>
<a href="maths-module-25.html">Module 25: Mathematical Cryptosystems & Attack Models</a>
<div class="dropdown-section-title" style="font-size: 10.5px; font-weight: 700; color: #7c3aed; padding: 4px 14px; text-transform: uppercase; background: rgba(124, 58, 237, 0.08);">Unit V: Public Key Cryptography & Modern Protocols</div>
<a href="maths-module-26.html">Module 26: Foundations of Public Key Cryptography & Fast Modular Exponentiation</a>
<a href="maths-module-27.html">Module 27: Diffie-Hellman Key Exchange & Discrete Logarithm Problem</a>
<a href="maths-module-28.html">Module 28: The RSA Cryptosystem: Key Generation, Encryption & Decryption</a>
<a href="maths-module-29.html">Module 29: The ElGamal Cryptosystem & Comprehensive Unit V Exam Mastery</a>
                    </div>
                </div>

                <div class="nav-dropdown">
                    <button class="nav-dropdown-btn"><span class="icon">⛓️</span> Blockchain (18) ▾</button>
                    <div class="nav-dropdown-menu">
                        <a href="blockchain.html" class="nav-dropdown-header">📋 Blockchain Syllabus Hub (All 18)</a>
                        <div class="dropdown-section-title" style="font-size: 10.5px; font-weight: 700; color: #0284c7; padding: 4px 14px; text-transform: uppercase;">Unit I (Mods 1–4)</div>
                        <a href="blockchain-module-1.html">Module 1: History &amp; Bitcoin</a>
                        <a href="blockchain-module-2.html">Module 2: Distributed Systems</a>
                        <a href="blockchain-module-3.html">Module 3: Consensus Protocols</a>
                        <a href="blockchain-module-4.html">Module 4: Decentralization</a>
                        <div class="dropdown-section-title" style="font-size: 10.5px; font-weight: 700; color: #0284c7; padding: 4px 14px; text-transform: uppercase;">Unit II (Mods 5–8)</div>
                        <a href="blockchain-module-5.html">Module 5: Symmetric Crypto</a>
                        <a href="blockchain-module-6.html">Module 6: Public Key Crypto</a>
                        <a href="blockchain-module-7.html">Module 7: Digital Signatures</a>
                        <a href="blockchain-module-8.html">Module 8: SHA &amp; Hashes</a>
                        <div class="dropdown-section-title" style="font-size: 10.5px; font-weight: 700; color: #0284c7; padding: 4px 14px; text-transform: uppercase;">Unit III (Mods 9–13)</div>
                        <a href="blockchain-module-9.html">Module 9: Consensus Problem &amp; Design</a>
                        <a href="blockchain-module-10.html">Module 10: Paxos, Raft &amp; PBFT</a>
                        <a href="blockchain-module-11.html">Module 11: PoW, PoS &amp; Selection</a>
                        <a href="blockchain-module-12.html">Module 12: Bitcoin Keys &amp; UTXO</a>
                        <a href="blockchain-module-13.html">Module 13: Mining, Network &amp; Forks</a>
                        <div class="dropdown-section-title" style="font-size: 10.5px; font-weight: 700; color: #0284c7; padding: 4px 14px; text-transform: uppercase;">Unit IV (Mods 14–18)</div>
                        <a href="blockchain-module-14.html">Module 14: The Bitcoin Network</a>
                        <a href="blockchain-module-15.html">Module 15: Bitcoin Wallets</a>
                        <a href="blockchain-module-16.html">Module 16: Bitcoin Payments</a>
                        <a href="blockchain-module-17.html">Module 17: Advanced Protocols</a>
                        <a href="blockchain-module-18.html">Module 18: Bitcoin Investment</a>
                        <a href="blockchain_guide.html" class="nav-dropdown-special">📖 Full 8-Module Reader</a>
                    </div>
                </div>

                <div class="nav-dropdown">
                    <button class="nav-dropdown-btn"><span class="icon">🐍</span> Django Course (45) ▾</button>
                    <div class="nav-dropdown-menu">
                        <a href="django.html" class="nav-dropdown-header">📋 Django Syllabus Hub</a>
                        <a href="module-1.html">Module 1: Fundamentals</a>
                        <a href="module-7.html">Module 7: URL Routing</a>
                        <a href="module-12.html">Module 12: Templates</a>
                        <a href="module-21.html">Module 21: Forms</a>
                        <a href="module-25.html">Module 25: Models &amp; ORM</a>
                        <a href="module-37.html">Module 37: Authentication</a>
                        <a href="module-42.html">Module 42: Complete Revision</a>
                        <a href="django_guide.html" class="nav-dropdown-special">📖 Full 44-Module Reader</a>
                    </div>
                </div>
            </div>
            <div class="nav-actions">
                <button id="themeToggleBtn" class="theme-btn" title="Toggle Dark/Light Mode">🌙</button>
                <a href="maths.html" class="nav-action-pill" style="background: linear-gradient(135deg, #7c3aed, #4c1d95);" title="Return to Mathematics Hub">📋 Maths Hub</a>
            </div>
        </div>
    </header>'''

def generate_nav_panel(current_mod):
    items = []
    
    # Unit 1
    items.append('<div style="font-size: 11px; font-weight: 800; color: #7c3aed; text-transform: uppercase; margin: 10px 0 4px; padding-left: 6px; letter-spacing: 0.5px; break-inside: avoid;">Unit I (Mods 1–5)</div>')
    for i in range(1, 6):
        cls = 'nav-item current' if i == current_mod else 'nav-item'
        items.append(f'<a class="{cls}" href="maths-module-{i}.html">{MODULE_TITLES[i]}</a>')
        
    # Unit 2
    items.append('<div style="font-size: 11px; font-weight: 800; color: #7c3aed; text-transform: uppercase; margin: 10px 0 4px; padding-left: 6px; letter-spacing: 0.5px; break-inside: avoid;">Unit II (Mods 6–11)</div>')
    for i in range(6, 12):
        cls = 'nav-item current' if i == current_mod else 'nav-item'
        items.append(f'<a class="{cls}" href="maths-module-{i}.html">{MODULE_TITLES[i]}</a>')
        
    # Unit 3
    items.append('<div style="font-size: 11px; font-weight: 800; color: #7c3aed; text-transform: uppercase; margin: 10px 0 4px; padding-left: 6px; letter-spacing: 0.5px; break-inside: avoid;">Unit III (Mods 12–17)</div>')
    for i in range(12, 18):
        cls = 'nav-item current' if i == current_mod else 'nav-item'
        items.append(f'<a class="{cls}" href="maths-module-{i}.html">{MODULE_TITLES[i]}</a>')
        
    # Unit 4
    items.append('<div style="font-size: 11px; font-weight: 800; color: #7c3aed; text-transform: uppercase; margin: 10px 0 4px; padding-left: 6px; letter-spacing: 0.5px; break-inside: avoid;">Unit IV (Mods 18–25)</div>')
    for i in range(18, 26):
        cls = 'nav-item current' if i == current_mod else 'nav-item'
        items.append(f'<a class="{cls}" href="maths-module-{i}.html">{MODULE_TITLES[i]}</a>')
        
    # Unit 5
    items.append('<div style="font-size: 11px; font-weight: 800; color: #7c3aed; text-transform: uppercase; margin: 10px 0 4px; padding-left: 6px; letter-spacing: 0.5px; break-inside: avoid;">Unit V (Mods 26–29)</div>')
    for i in range(26, 30):
        cls = 'nav-item current' if i == current_mod else 'nav-item'
        items.append(f'<a class="{cls}" href="maths-module-{i}.html">{MODULE_TITLES[i]}</a>')
        
    inner_html = "\n".join(items)
    return f'''    <div class="nav-toggle">
        <button type="button" class="nav-toggle-btn" onclick="toggleNavPanel()">
            <span>📚 Course Syllabus Navigator (Modules 01 &ndash; 29)</span>
            <span>▾ Toggle Menu</span>
        </button>
        <div id="navPanel" class="nav-panel">
            {inner_html}
        </div>
    </div>'''

def get_badge(mod_num):
    if 1 <= mod_num <= 5:
        return f'<div class="math-badge">📐 Unit I: Divisibility, Modular Arithmetic &amp; Base Expansions &bull; Module {mod_num} of 29</div>'
    elif 6 <= mod_num <= 11:
        return f'<div class="math-badge">📐 Unit II: Prime Numbers, GCD &amp; Bézout\'s Identity &bull; Module {mod_num} of 29</div>'
    elif 12 <= mod_num <= 17:
        return f'<div class="math-badge">📐 Unit III: Linear Congruences, CRT &amp; Fermat/Euler &bull; Module {mod_num} of 29</div>'
    return ""

def update_module(mod_num):
    fname = f"maths-module-{mod_num}.html"
    if not os.path.exists(fname):
        print(f"Skipping {fname}, does not exist")
        return
        
    with open(fname, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # 1. Replace header.global-navbar
    content = re.sub(r'<header class="global-navbar">.*?</header>', generate_navbar(), content, flags=re.DOTALL)
    
    # 2. Replace math-badge
    new_badge = get_badge(mod_num)
    content = re.sub(r'<div class="math-badge">.*?</div>', new_badge, content, flags=re.DOTALL)
    
    # 3. Replace nav-toggle
    new_nav = generate_nav_panel(mod_num)
    content = re.sub(r'<div class="nav-toggle">.*?</div>\s*</div>', new_nav, content, flags=re.DOTALL)
    
    with open(fname, 'w', encoding='utf-8') as f:
        f.write(content)
        
    print(f"✅ Updated {fname}")

if __name__ == "__main__":
    for m in range(1, 18):
        update_module(m)
