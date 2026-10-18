import re

math_search_items = [
    {"title": "Maths 01: The Division Algorithm & Integer Divisibility", "subj": "Maths", "url": "maths-module-1.html", "keywords": "divisibility division algorithm quotient remainder floor ceiling a=dq+r integer"},
    {"title": "Maths 02: Modular Arithmetic Operations & Clock Math", "subj": "Maths", "url": "maths-module-2.html", "keywords": "modular arithmetic congruence clock math modulo equivalence residue classes zm"},
    {"title": "Maths 03: Binary & Decimal Base-b Integer Expansions", "subj": "Maths", "url": "maths-module-3.html", "keywords": "base-b binary decimal expansions radix successive division remainder conversion"},
    {"title": "Maths 04: Octal, Hexadecimal & Fast Base Conversion", "subj": "Maths", "url": "maths-module-4.html", "keywords": "hexadecimal octal base 16 base 8 grouping 3-bit 4-bit power of 2 fast conversion"},
    {"title": "Maths 05: Addition & Multiplication Algorithms for Base-b", "subj": "Maths", "url": "maths-module-5.html", "keywords": "addition multiplication base-b carry propagation bit complexity o(n) o(n^2)"},
    {"title": "Maths 06: Prime Numbers & The Sieve of Eratosthenes", "subj": "Maths", "url": "maths-module-6.html", "keywords": "primes composite numbers sieve of eratosthenes trial division sqrt(n) prime density"},
    {"title": "Maths 07: Fundamental Theorem of Arithmetic & Factorization", "subj": "Maths", "url": "maths-module-7.html", "keywords": "fundamental theorem arithmetic prime factorization canonical decomposition euclid lemma"},
    {"title": "Maths 08: Infinitude of Primes & Famous Conjectures", "subj": "Maths", "url": "maths-module-8.html", "keywords": "infinitude primes euclid proof mersenne primes fermat primes goldbach twin prime"},
    {"title": "Maths 09: Greatest Common Divisor (GCD) & LCM", "subj": "Maths", "url": "maths-module-9.html", "keywords": "gcd lcm greatest common divisor least common multiple coprime pairwise relatively prime"},
    {"title": "Maths 10: The Euclidean Algorithm for Fast GCD", "subj": "Maths", "url": "maths-module-10.html", "keywords": "euclidean algorithm fast gcd successive division remainder chain lame theorem"},
    {"title": "Maths 11: Bézout's Identity & Extended Euclidean Algorithm", "subj": "Maths", "url": "maths-module-11.html", "keywords": "bezout identity extended euclidean algorithm linear combination as+bt modular inverse tabular"},
    {"title": "Maths 12: Linear Congruences & Modular Inverses", "subj": "Maths", "url": "maths-module-12.html", "keywords": "linear congruences ax=b modular inverse gcd(a,m)=1 extended gcd solution set"},
    {"title": "Maths 13: Chinese Remainder Theorem (CRT)", "subj": "Maths", "url": "maths-module-13.html", "keywords": "chinese remainder theorem crt simultaneous congruences pairwise coprime moduli computer arithmetic"},
    {"title": "Maths 14: Fermat's Little Theorem & Modular Exponentiation", "subj": "Maths", "url": "maths-module-14.html", "keywords": "fermat little theorem flt repeated squaring modular exponentiation pseudoprimes carmichael"},
    {"title": "Maths 15: Euler's Totient Function & Euler's Theorem", "subj": "Maths", "url": "maths-module-15.html", "keywords": "euler totient phi(n) euler theorem modular reduction multiplicative function prime powers"},
    {"title": "Maths 16: Public-Key Cryptography & The RSA Cryptosystem", "subj": "Maths", "url": "maths-module-16.html", "keywords": "rsa public key private key cryptography encryption decryption trapdoor prime factoring ed=1"},
    {"title": "Maths 17: Comprehensive Mastery Exam & Quick Revision", "subj": "Maths", "url": "maths-module-17.html", "keywords": "maths mastery final exam full revision theorems formulas cheat sheet number theory"}
]

with open("d:/Blockchain HTML/Django HTML/index.html", "r", encoding="utf-8") as f:
    content = f.read()

# 1. Update .sc-math CSS
old_math_css = """.sc-math .sc-header {
    background: linear-gradient(135deg, #451a03 0%, #b45309 60%, #f59e0b 100%);
}"""
new_math_css = """.sc-math .sc-header {
    background: linear-gradient(135deg, #0f0c29 0%, #301e67 55%, #7c3aed 100%);
}
.sc-math .check-icon { color: #7c3aed; }
.sc-math .btn-card-main { background: linear-gradient(135deg, #7c3aed, #5b21b6); }"""

content = content.replace(old_math_css, new_math_css)

# Update check-icon if still amber
content = content.replace(".sc-math .check-icon { color: #d97706; }", "")
content = content.replace(".sc-math .btn-card-main { background: #d97706; }", "")

# 2. Add .res-math badge CSS
old_badge_css = """.res-bc { background: rgba(2, 132, 199, 0.12); color: #0284c7; }"""
new_badge_css = """.res-bc { background: rgba(2, 132, 199, 0.12); color: #0284c7; }
.res-math { background: rgba(124, 58, 237, 0.12); color: #7c3aed; }"""

content = content.replace(old_badge_css, new_badge_css)

# 3. Update top navbar Mathematics link to dropdown
old_nav_math = """            <a href="maths.html" class="nav-link"><span class="icon">📐</span> Mathematics <span class="badge-soon">Soon</span></a>"""
new_nav_math = """            <div class="nav-dropdown">
                <button class="nav-dropdown-btn"><span class="icon">📐</span> Mathematics (17) ▾</button>
                <div class="nav-dropdown-menu">
                    <a href="maths.html" class="nav-dropdown-header">📋 Mathematics Syllabus Hub</a>
                    <a href="maths-module-1.html">Module 1: Division &amp; Divisibility</a>
                    <a href="maths-module-2.html">Module 2: Modular Arithmetic</a>
                    <a href="maths-module-6.html">Module 6: Primes &amp; Sieve</a>
                    <a href="maths-module-9.html">Module 9: GCD &amp; LCM</a>
                    <a href="maths-module-10.html">Module 10: Euclidean Algorithm</a>
                    <a href="maths-module-11.html">Module 11: Extended GCD &amp; Bézout</a>
                    <a href="maths-module-12.html">Module 12: Linear Congruences</a>
                    <a href="maths-module-13.html">Module 13: Chinese Remainder Theorem</a>
                    <a href="maths-module-14.html">Module 14: Fermat's Little Theorem</a>
                    <a href="maths-module-15.html">Module 15: Euler's Totient &amp; Theorem</a>
                    <a href="maths-module-16.html">Module 16: RSA Cryptosystem</a>
                    <a href="maths-module-17.html">Module 17: Comprehensive Mastery Exam</a>
                </div>
            </div>"""

content = content.replace(old_nav_math, new_nav_math)

# 4. Update Stats
content = content.replace("""            <div class="stat-item">
                <span class="stat-val">58+</span>
                <span class="stat-lbl">Interactive Modules</span>
            </div>""", """            <div class="stat-item">
                <span class="stat-val">75+</span>
                <span class="stat-lbl">Interactive Modules</span>
            </div>""")

# 5. Update Mathematics Subject Card
old_math_card = """        <!-- SUBJECT 3: MATHEMATICS -->
        <div class="subject-card sc-math">
            <div class="sc-header">
                <span class="sc-badge">Shell Primed &bull; Notes Coming Soon</span>
                <h3 class="sc-title">Engineering Mathematics</h3>
                <p class="sc-desc">Mathematical pillars for algorithms, cryptographic curves, AI, and systems engineering. Pre-configured with MathJax equation support.</p>
            </div>
            <div class="sc-body">
                <ul class="sc-highlights">
                    <li><span class="check-icon">&check;</span> Unit 1: Discrete Mathematics, Logic &amp; Graph Theory</li>
                    <li><span class="check-icon">&check;</span> Unit 2: Linear Algebra, Eigenvalues &amp; Matrix SVD</li>
                    <li><span class="check-icon">&check;</span> Unit 3: Calculus, Gradients &amp; Convex Optimization</li>
                    <li><span class="check-icon">&check;</span> Unit 4: Probability, Bayes' Theorem &amp; Random Processes</li>
                    <li><span class="check-icon">&check;</span> Built-in LaTeX MathJax rendering pipeline</li>
                    <li><span class="check-icon">&check;</span> Ready for user notes drop-in anytime</li>
                </ul>
                <div class="sc-footer">
                    <a href="maths.html" class="btn-card-main">Explore Mathematics Hub &rarr;</a>
                    <a href="maths.html#integration" class="btn-card-sub">📝 How to Add Your Notes</a>
                </div>
            </div>
        </div>"""

new_math_card = """        <!-- SUBJECT 3: MATHEMATICS -->
        <div class="subject-card sc-math">
            <div class="sc-header">
                <span class="sc-badge">17 Modules Ready &bull; Number Theory &amp; Cryptography</span>
                <h3 class="sc-title">Number Theory &amp; Cryptography</h3>
                <p class="sc-desc">Rigorous discrete mathematical pillars powering modern cryptography, blockchain consensus, and algorithm design. Divisibility, primes, GCD, modular arithmetic, Chinese Remainder Theorem, and RSA.</p>
            </div>
            <div class="sc-body">
                <ul class="sc-highlights">
                    <li><span class="check-icon">&check;</span> Modules 1–5: The Division Algorithm, Modular Arithmetic, Base-b &amp; Hex Conversion</li>
                    <li><span class="check-icon">&check;</span> Modules 6–8: Prime Numbers, Sieve of Eratosthenes &amp; Prime Factorization</li>
                    <li><span class="check-icon">&check;</span> Modules 9–11: Greatest Common Divisor, Euclidean Algorithm &amp; Bézout's Identity</li>
                    <li><span class="check-icon">&check;</span> Modules 12–13: Linear Congruences, Modular Inverses &amp; Chinese Remainder Theorem</li>
                    <li><span class="check-icon">&check;</span> Modules 14–15: Fermat's Little Theorem, Fast Modular Exponentiation &amp; Euler's Totient</li>
                    <li><span class="check-icon">&check;</span> Modules 16–17: Public-Key Cryptography, RSA Cryptosystem &amp; Final Mastery Exam</li>
                    <li><span class="check-icon">&check;</span> 100% LaTeX MathJax Formatted Formulas &amp; 17 Interactive Self-Grading Quizzes</li>
                </ul>
                <div class="sc-footer">
                    <a href="maths.html" class="btn-card-main">Explore 17-Module Syllabus &rarr;</a>
                    <a href="maths-module-1.html" class="btn-card-sub">Start from Module 1</a>
                    <a href="maths-module-16.html" class="btn-card-sub">🔐 Jump to RSA Cryptography (Mod 16)</a>
                    <a href="maths-module-17.html" class="btn-card-sub">🎯 Comprehensive Final Exam (Mod 17)</a>
                </div>
            </div>
        </div>"""

content = content.replace(old_math_card, new_math_card)

# 6. Add two Math Cram Cards into Fast Revision Section
old_cram_insert = """        <a href="module-42.html" class="cram-card">"""
new_cram_insert = """        <a href="maths-module-11.html" class="cram-card">
            <div class="cram-icon">📐</div>
            <div>
                <h4 class="cram-title">Bézout's Identity &amp; Extended GCD</h4>
                <p class="cram-desc">Module 11: Expressing gcd(a,b) = as + bt via backward substitution and tabular method.</p>
            </div>
        </a>

        <a href="maths-module-16.html" class="cram-card">
            <div class="cram-icon">🔐</div>
            <div>
                <h4 class="cram-title">RSA Cryptosystem &amp; Inverses</h4>
                <p class="cram-desc">Module 16: Key generation (p, q, n, φ(n), e, d), encryption, decryption &amp; Euler's proof.</p>
            </div>
        </a>

        <a href="module-42.html" class="cram-card">"""

content = content.replace(old_cram_insert, new_cram_insert)

# 7. Update Footer link
content = content.replace("""<li><a href="maths.html">Engineering Mathematics (Upcoming)</a></li>""",
                        """<li><a href="maths.html">Mathematics: Number Theory (17 Modules)</a></li>""")

# 8. Update searchData array and badge logic in JS
import json
math_json = json.dumps(math_search_items)[1:-1] # strip outer []
old_search_end = """bitcoin blockchain block header 80 bytes merkle tree merkle root p2p network transaction flooding block propagation mining difficulty adjustment 2016 halving 210000 accidental hard soft forks confirmations"}]"""
new_search_end = f"""bitcoin blockchain block header 80 bytes merkle tree merkle root p2p network transaction flooding block propagation mining difficulty adjustment 2016 halving 210000 accidental hard soft forks confirmations"}}, {math_json}]"""

content = content.replace(old_search_end, new_search_end)

# Update badge logic
content = content.replace(
    "var badgeCls = item.subj === 'Django' ? 'res-django' : 'res-bc';",
    "var badgeCls = item.subj === 'Django' ? 'res-django' : (item.subj === 'Blockchain' ? 'res-bc' : 'res-math');"
)

with open("d:/Blockchain HTML/Django HTML/index.html", "w", encoding="utf-8") as f:
    f.write(content)

print("index.html updated successfully!")
