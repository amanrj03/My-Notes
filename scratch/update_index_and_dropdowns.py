import re
import json

MATHS_DROPDOWN_HTML = '''            <div class="nav-dropdown">
                <button class="nav-dropdown-btn"><span class="icon">📐</span> Mathematics (29) ▾</button>
                <div class="nav-dropdown-menu">
                    <a href="maths.html" class="nav-dropdown-header">📋 Mathematics Syllabus Hub (All 29)</a>
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
            </div>'''

def update_dropdown_in_file(fname):
    with open(fname, 'r', encoding='utf-8') as f:
        content = f.read()
        
    pattern = r'<div class="nav-dropdown">\s*<button class="nav-dropdown-btn"[^>]*>\s*<span class="icon">📐</span>\s*Mathematics \(\d+\)[^<]*</button>\s*<div class="nav-dropdown-menu">.*?</div>\s*</div>'
    
    if re.search(pattern, content, flags=re.DOTALL):
        content = re.sub(pattern, MATHS_DROPDOWN_HTML.strip(), content, flags=re.DOTALL)
        with open(fname, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"✅ Updated Mathematics dropdown in {fname}")
    else:
        print(f"⚠️ Could not find Mathematics dropdown pattern in {fname}")

# 1. Update dropdowns in other hubs and modules
other_files = [
    "index.html",
    "blockchain.html",
    "django.html",
    "blockchain-module-14.html",
    "blockchain-module-15.html",
    "blockchain-module-16.html",
    "blockchain-module-17.html",
    "blockchain-module-18.html"
]

for f in other_files:
    update_dropdown_in_file(f)

# 2. Update index.html specific content
with open("index.html", 'r', encoding='utf-8') as f:
    idx = f.read()

# Update stats
idx = idx.replace('<span class="stat-val">75+</span>', '<span class="stat-val">92+</span>')
idx = idx.replace('Mathematics: Number Theory (17 Modules)', 'Mathematics: Number Theory &amp; Cryptography (29 Modules)')

# Update Subject 3 Card
new_math_card = '''        <!-- SUBJECT 3: MATHEMATICS -->
        <div class="subject-card sc-math">
            <div class="sc-header">
                <span class="sc-badge">29 Modules Ready &bull; 5 Units &bull; Number Theory &amp; Cryptography</span>
                <h3 class="sc-title">Number Theory &amp; Cryptography</h3>
                <p class="sc-desc">Rigorous discrete mathematical pillars powering modern cryptography, blockchain consensus, and algorithm design across 5 complete units: Divisibility, Primes, Euclidean &amp; Bézout algorithms, Linear Congruences, CRT, Fermat &amp; Euler, Classical Ciphers (Caesar, Affine, Vigenère, Hill, Permutations), and Modern Asymmetric Cryptosystems (Diffie-Hellman, RSA, and ElGamal).</p>
            </div>
            <div class="sc-body">
                <ul class="sc-highlights">
                    <li><span class="check-icon">&check;</span> Modules 1–5: Unit I — The Division Algorithm, Modular Arithmetic, Base-b &amp; Hex Conversion</li>
                    <li><span class="check-icon">&check;</span> Modules 6–11: Unit II — Prime Numbers, Sieve of Eratosthenes, Euclidean Algorithm &amp; Bézout's Identity</li>
                    <li><span class="check-icon">&check;</span> Modules 12–17: Unit III — Linear Congruences, CRT, Large Integers, Fermat's Little Theorem &amp; Revision</li>
                    <li><span class="check-icon">&check;</span> Modules 18–25: Unit IV — Classical Cryptography, Substitution, Caesar, Affine, Vigenère, Hill &amp; Permutations</li>
                    <li><span class="check-icon">&check;</span> Modules 26–29: Unit V — Public-Key Cryptography, Repeated Squaring, Diffie-Hellman, RSA &amp; ElGamal</li>
                    <li><span class="check-icon">&check;</span> 100% LaTeX MathJax Formulas, 29 Self-Grading Quizzes &amp; Visual Cryptosystem Diagrams</li>
                </ul>
                <div class="sc-footer">
                    <a href="maths.html" class="btn-card-main">Explore 29 Modules Across 5 Units &rarr;</a>
                    <a href="maths-module-1.html" class="btn-card-sub">Start from Module 1</a>
                    <a href="maths-module-18.html" class="btn-card-sub">🔐 Classical Cryptography (Mod 18)</a>
                    <a href="maths-module-27.html" class="btn-card-sub">🔑 Diffie-Hellman Key Exchange (Mod 27)</a>
                    <a href="maths-module-28.html" class="btn-card-sub">🛡️ RSA Deep Architecture (Mod 28)</a>
                    <a href="maths-module-29.html" class="btn-card-sub">🎯 Course Capstone &amp; Final Exam (Mod 29)</a>
                </div>
            </div>
        </div>'''

idx = re.sub(r'<!-- SUBJECT 3: MATHEMATICS -->.*?</div>\s*</div>\s*</div>', new_math_card, idx, flags=re.DOTALL)

# Update searchData to include Blockchain 14-18 and Maths 18-29
extra_search_items = [
    {"title": "Module 14: The Bitcoin Network", "subj": "Blockchain", "url": "blockchain-module-14.html", "keywords": "bitcoin network p2p peer discovery inv getdata tx block initial block download handshake addr version verack"},
    {"title": "Module 15: Bitcoin Wallets", "subj": "Blockchain", "url": "blockchain-module-15.html", "keywords": "bitcoin wallets deterministic nondeterministic bip32 bip39 bip44 mnemonic seed root seed hd wallets xprv xpub"},
    {"title": "Module 16: Bitcoin Payments", "subj": "Blockchain", "url": "blockchain-module-16.html", "keywords": "bitcoin payments bip70 payment protocol merchant refund fee estimation replace by fee rbf cpfp child pays for parent"},
    {"title": "Module 17: Innovation in Bitcoin and Advanced Protocols", "subj": "Blockchain", "url": "blockchain-module-17.html", "keywords": "segwit segregated witness lightning network payment channels htlc taproot schnorr signatures mast"},
    {"title": "Module 18: Bitcoin Investment, Buying and Selling Bitcoin", "subj": "Blockchain", "url": "blockchain-module-18.html", "keywords": "bitcoin investment buying selling exchange order book dca dollar cost averaging cold storage taxation custody"},
    {"title": "Maths 18: Introduction to Cryptography & Security Models", "subj": "Maths", "url": "maths-module-18.html", "keywords": "cryptography alice bob eve kerckhoffs principle security models coa kpa cpa cca symmetric unconditional computational"},
    {"title": "Maths 19: Classical Cryptography & Substitution Ciphers", "subj": "Maths", "url": "maths-module-19.html", "keywords": "substitution cipher monoalphabetic key space 26! frequency analysis digrams trigrams letter frequencies"},
    {"title": "Maths 20: Shift Cipher and Caesar Cipher", "subj": "Maths", "url": "maths-module-20.html", "keywords": "caesar cipher shift cipher k=3 z26 modular arithmetic brute force key exhaustion rosen mapping"},
    {"title": "Maths 21: Affine Cipher & Modular Inverses", "subj": "Maths", "url": "maths-module-21.html", "keywords": "affine cipher c=ap+b gcd(a,26)=1 modular inverse 12 coprime keys known plaintext attack"},
    {"title": "Maths 22: Vigenère Polyalphabetic Cipher & Tableau", "subj": "Maths", "url": "maths-module-22.html", "keywords": "vigenere cipher polyalphabetic keyword alignment tabula recta kasiski examination period index coincidence"},
    {"title": "Maths 23: Hill Cipher & Matrix Cryptography", "subj": "Maths", "url": "maths-module-23.html", "keywords": "hill cipher matrix cryptography block encryption modular matrix inverse gcd(det(K),26)=1 2x2 matrix"},
    {"title": "Maths 24: Permutation & Transposition Ciphers", "subj": "Maths", "url": "maths-module-24.html", "keywords": "transposition cipher permutation function sigma rail fence columnar transposition product cipher spn"},
    {"title": "Maths 25: Mathematical Cryptosystems & Attack Models", "subj": "Maths", "url": "maths-module-25.html", "keywords": "cryptosystem formal definition 5-tuple (P,C,K,E,D) shannon perfect secrecy one-time pad vernam"},
    {"title": "Maths 26: Foundations of Public Key Cryptography & Fast Modular Exponentiation", "subj": "Maths", "url": "maths-module-26.html", "keywords": "public key cryptography asymmetric trapdoor one-way function repeated squaring fast modular exponentiation o(log k)"},
    {"title": "Maths 27: Diffie-Hellman Key Exchange & Discrete Logarithm Problem", "subj": "Maths", "url": "maths-module-27.html", "keywords": "diffie-hellman key exchange discrete logarithm dlp generator g shared secret man in the middle cdh ddh"},
    {"title": "Maths 28: The RSA Cryptosystem: Key Generation, Encryption & Decryption", "subj": "Maths", "url": "maths-module-28.html", "keywords": "rsa cryptosystem key generation encryption decryption euler totient phi(n) ed=1 mod phi(n) factoring"},
    {"title": "Maths 29: The ElGamal Cryptosystem & Comprehensive Unit V Exam Mastery", "subj": "Maths", "url": "maths-module-29.html", "keywords": "elgamal cryptosystem probabilistic encryption ephemeral key discrete log modern protocols comparison final exam"}
]

# Find searchData in index.html
m_sd = re.search(r'var searchData = (\[.*?\]);', idx, flags=re.DOTALL)
if m_sd:
    current_data = json.loads(m_sd.group(1))
    # Add items if url not already present
    existing_urls = {item['url'] for item in current_data}
    added_count = 0
    for item in extra_search_items:
        if item['url'] not in existing_urls:
            current_data.append(item)
            added_count += 1
    new_sd_json = json.dumps(current_data)
    idx = idx[:m_sd.start(1)] + new_sd_json + idx[m_sd.end(1):]
    print(f"✅ Added {added_count} items to searchData in index.html (total {len(current_data)})")

with open("index.html", 'w', encoding='utf-8') as f:
    f.write(idx)

print("✅ index.html updated successfully!")
