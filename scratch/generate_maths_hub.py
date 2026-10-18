import os
import json

modules_data = [
    {
        "num": 1,
        "unit": 1,
        "unit_name": "Unit 1: Divisibility & Bases",
        "title": "The Division Algorithm & Integer Divisibility",
        "desc": "The foundational bedrock of number theory: definitions of divisibility, division algorithm with unique quotient & remainder, properties of divisibility, and floor/ceiling functions.",
        "formula": r"a = d \cdot q + r \quad \text{where } 0 \le r < d, \quad q = \lfloor a/d \rfloor, \; r = a \bmod d",
        "topics": ["Divisibility Relation a | b", "The Division Theorem", "Quotient & Remainder", "Floor & Ceiling Arithmetic", "Transitivity & Linearity of Divisibility"],
        "badge": "Core Foundation"
    },
    {
        "num": 2,
        "unit": 1,
        "unit_name": "Unit 1: Divisibility & Bases",
        "title": "Modular Arithmetic Operations & Clock Math",
        "desc": "Congruence modulo m as an equivalence relation, clock arithmetic, modular addition, subtraction, multiplication, and algebraic residue classes in Z_m.",
        "formula": r"a \equiv b \pmod m \iff m \mid (a - b) \iff a \bmod m = b \bmod m",
        "topics": ["Equivalence Modulo m", "Residue Classes Z_m", "Modular Addition & Multiplication", "Compatibility with Arithmetic", "Clock Ring Z_12 and Z_24"],
        "badge": "Core Foundation"
    },
    {
        "num": 3,
        "unit": 1,
        "unit_name": "Unit 1: Divisibility & Bases",
        "title": "Binary & Decimal Base-b Integer Expansions",
        "desc": "Positional numeral systems, base-b expansions, radix representations, binary, decimal, and step-by-step algorithms using successive division by b.",
        "formula": r"n = \sum_{i=0}^{k-1} a_i b^i = (a_{k-1} \dots a_1 a_0)_b, \quad 0 \le a_i < b",
        "topics": ["Base-b Expansion Theorem", "Binary (Base 2)", "Successive Division Algorithm", "Reversing Remainders", "Radix Conversion"],
        "badge": "Algorithms"
    },
    {
        "num": 4,
        "unit": 1,
        "unit_name": "Unit 1: Divisibility & Bases",
        "title": "Octal, Hexadecimal & Fast Base Conversion",
        "desc": "Power-of-two bases, octal (base 8), hexadecimal (base 16), direct bit-grouping (3-bit and 4-bit chunks), fast conversions without decimal intermediate.",
        "formula": r"(110111101011)_2 = (\underbrace{1101}_{\text{D}}\,\underbrace{1110}_{\text{E}}\,\underbrace{1011}_{\text{B}})_{16} = (\text{DEB})_{16}",
        "topics": ["Hexadecimal Digits 0-F", "Octal Radix 8", "3-Bit & 4-Bit Grouping", "Direct Power-of-2 Conversion", "Hex to Binary Table"],
        "badge": "Algorithms"
    },
    {
        "num": 5,
        "unit": 1,
        "unit_name": "Unit 1: Divisibility & Bases",
        "title": "Addition & Multiplication Algorithms for Base-b",
        "desc": "Formal algorithmic implementation of addition, subtraction, and multiplication for arbitrary base-b integers with full carry propagation and bit complexity analysis.",
        "formula": r"s_j = (a_j + b_j + c_j) \bmod b, \quad c_{j+1} = \lfloor (a_j + b_j + c_j) / b \rfloor, \quad O(n) \text{ Addition}",
        "topics": ["Algorithmic Column Addition", "Carry Bit Propagation", "Base-b Multiplication O(n^2)", "Bit Complexity", "Pseudocode Verification"],
        "badge": "Complexity"
    },
    {
        "num": 6,
        "unit": 2,
        "unit_name": "Unit 2: Primes, GCD & Bézout",
        "title": "Prime Numbers & The Sieve of Eratosthenes",
        "desc": "Definition of primes and composites, trial division up to sqrt(n), the ancient Sieve of Eratosthenes algorithm, and prime counting function pi(x).",
        "formula": r"n \text{ is composite} \implies \exists \text{ prime } p \mid n \text{ with } p \le \sqrt{n}; \quad \pi(x) \sim \frac{x}{\ln x}",
        "topics": ["Prime vs Composite", "Trial Division Bound sqrt(n)", "Sieve of Eratosthenes", "Prime Number Theorem", "Prime Density"],
        "badge": "Primes"
    },
    {
        "num": 7,
        "unit": 2,
        "unit_name": "Unit 2: Primes, GCD & Bézout",
        "title": "Fundamental Theorem of Arithmetic & Factorization",
        "desc": "Unique factorization of every positive integer greater than 1 into primes, canonical prime-power decomposition, and divisibility criterion via exponents.",
        "formula": r"n = p_1^{a_1} p_2^{a_2} \dots p_k^{a_k} \quad (\text{unique up to order}), \quad a \mid b \iff \alpha_i \le \beta_i \; \forall i",
        "topics": ["Fundamental Theorem of Arithmetic", "Canonical Decomposition", "Euclid's Lemma", "Exponent Divisibility Test", "Number of Divisors d(n)"],
        "badge": "Theorem"
    },
    {
        "num": 8,
        "unit": 2,
        "unit_name": "Unit 2: Primes, GCD & Bézout",
        "title": "Infinitude of Primes & Famous Conjectures",
        "desc": "Euclid's classic proof of the infinitude of primes, Mersenne primes, Fermat primes, Goldbach's conjecture, and the Twin Prime conjecture.",
        "formula": r"N = p_1 p_2 \dots p_n + 1 \implies \text{every prime factor } q \notin \{p_1, \dots, p_n\} \implies \text{infinite primes}",
        "topics": ["Euclid's Infinitude Proof", "Mersenne Primes 2^p - 1", "Fermat Primes 2^{2^k} + 1", "Goldbach's Conjecture", "Twin Prime Conjecture"],
        "badge": "Open Problems"
    },
    {
        "num": 9,
        "unit": 2,
        "unit_name": "Unit 2: Primes, GCD & Bézout",
        "title": "Greatest Common Divisor (GCD) & LCM",
        "desc": "Greatest common divisor, coprime (relatively prime) integers, pairwise coprime sets, least common multiple, and the fundamental product identity.",
        "formula": r"\gcd(a, b) \cdot \operatorname{lcm}(a, b) = |a \cdot b|, \quad \gcd(a,b) = \prod p_i^{\min(a_i, b_i)}",
        "topics": ["Definition of GCD & LCM", "Relatively Prime (Coprime)", "Pairwise Relatively Prime", "Prime Exponent Formula", "Product Duality Identity"],
        "badge": "Core GCD"
    },
    {
        "num": 10,
        "unit": 2,
        "unit_name": "Unit 2: Primes, GCD & Bézout",
        "title": "The Euclidean Algorithm for Fast GCD",
        "desc": "The Euclidean algorithm based on gcd(a, b) = gcd(b, a mod b), step-by-step division chains, and Lamé's Theorem bounding steps by 5 times digits.",
        "formula": r"\gcd(a, b) = \gcd(b, a \bmod b) \implies r_{k-2} = q_k r_{k-1} + r_k, \quad \gcd(a, b) = r_n",
        "topics": ["Euclidean Lemma gcd(a,b)=gcd(b,r)", "Successive Division Chain", "Last Nonzero Remainder", "Lamé's Theorem & Fibonacci", "Logarithmic Complexity O(log b)"],
        "badge": "Algorithms"
    },
    {
        "num": 11,
        "unit": 2,
        "unit_name": "Unit 2: Primes, GCD & Bézout",
        "title": "Bézout's Identity & Extended Euclidean Algorithm",
        "desc": "Expressing gcd(a, b) as a linear combination as + bt, Bézout coefficients, the Extended Euclidean Algorithm forward & backward substitution, and table method.",
        "formula": r"\exists s, t \in \mathbb{Z} : a \cdot s + b \cdot t = \gcd(a, b); \quad \text{if } \gcd(a,m)=1 \implies as \equiv 1 \pmod m",
        "topics": ["Bézout's Theorem", "Bézout Coefficients (s, t)", "Back-Substitution Method", "Tabular Extended Algorithm", "Application to Modular Inverses"],
        "badge": "High Yield"
    },
    {
        "num": 12,
        "unit": 3,
        "unit_name": "Unit 3: Congruences, CRT & Euler",
        "title": "Linear Congruences & Modular Inverses",
        "desc": "Solving ax = b (mod m), modular inverse a^-1 (mod m) existence criterion gcd(a, m) = 1, computation via Extended Euclidean Algorithm, and general solution sets.",
        "formula": r"a \bar{a} \equiv 1 \pmod m \iff \gcd(a, m) = 1; \quad ax \equiv b \pmod m \implies x \equiv \bar{a}b \pmod m",
        "topics": ["Modular Inverse Existence", "Inverse via Extended GCD", "Solving Linear Congruences", "Number of Solutions gcd(a,m)", "Systematic Steps"],
        "badge": "Cryptographic Core"
    },
    {
        "num": 13,
        "unit": 3,
        "unit_name": "Unit 3: Congruences, CRT & Euler",
        "title": "Solving Systems with Chinese Remainder Theorem",
        "desc": "The Chinese Remainder Theorem (CRT) for simultaneous congruences with pairwise coprime moduli, the constructive formula, and applications in fast computer arithmetic.",
        "formula": r"x \equiv \sum_{i=1}^n a_i M_i y_i \pmod M, \quad M = \prod m_i, \; M_i = \frac{M}{m_i}, \; M_i y_i \equiv 1 \pmod{m_i}",
        "topics": ["CRT Statement & Moduli Conditions", "Constructive Solution Formula", "Uniqueness Modulo M", "Multi-Modular Computer Arithmetic", "Back-Substitution Alternative"],
        "badge": "Major Theorem"
    },
    {
        "num": 14,
        "unit": 3,
        "unit_name": "Unit 3: Congruences, CRT & Euler",
        "title": "Fermat's Little Theorem & Modular Exponentiation",
        "desc": "Fermat's Little Theorem, computing huge powers a^k mod p, pseudoprimes, Carmichael numbers, and the Fast Repeated Squaring algorithm (O(log k)).",
        "formula": r"p \text{ prime}, \; p \nmid a \implies a^{p-1} \equiv 1 \pmod p \implies a^p \equiv a \pmod p",
        "topics": ["Fermat's Little Theorem (FLT)", "Reducing Massive Exponents", "Fast Repeated Squaring Algorithm", "Fermat Pseudoprimes to Base b", "Carmichael Numbers"],
        "badge": "Cryptographic Core"
    },
    {
        "num": 15,
        "unit": 3,
        "unit_name": "Unit 3: Congruences, CRT & Euler",
        "title": "Euler's Totient Function & Euler's Theorem",
        "desc": "Euler's totient function phi(n), formula for prime powers and multiplicativity, Euler's Generalization of Fermat's Theorem, and exponent reduction for composite moduli.",
        "formula": r"\phi(n) = n \prod_{p \mid n} \left(1 - \frac{1}{p}\right); \quad \gcd(a, m) = 1 \implies a^{\phi(m)} \equiv 1 \pmod m",
        "topics": ["Definition of Totient phi(n)", "Multiplicative Property phi(mn)", "Prime Power Formula phi(p^k)", "Euler's Totient Theorem", "Exponent Reduction Mod Composite"],
        "badge": "Major Theorem"
    },
    {
        "num": 16,
        "unit": 4,
        "unit_name": "Unit 4: Cryptography & Mastery",
        "title": "Public-Key Cryptography & The RSA Cryptosystem",
        "desc": "Asymmetric cryptography, RSA key generation (p, q, n, phi(n), e, d), encryption c = m^e mod n, decryption m = c^d mod n, mathematical proof via Euler's Theorem, and digital signatures.",
        "formula": r"n = pq, \; \phi(n) = (p-1)(q-1), \; ed \equiv 1 \pmod{\phi(n)} \implies c = m^e \bmod n, \; m = c^d \bmod n",
        "topics": ["Public vs Private Keys", "RSA Key Generation Algorithm", "Encryption & Decryption Math", "Correctness Proof via Euler's Theorem", "Computational Hardness of Factoring"],
        "badge": "Cryptography Star"
    },
    {
        "num": 17,
        "unit": 4,
        "unit_name": "Unit 4: Cryptography & Mastery",
        "title": "Comprehensive Mastery Exam & Quick Revision",
        "desc": "Full syllabus master revision: 16 core theorems quick reference, comparison tables, high-yield exam traps, formulas cheat-sheet, and comprehensive final mastery exam.",
        "formula": r"\text{Complete Review: } \gcd \cdot \operatorname{lcm} = ab \quad|\quad as + bt = \gcd \quad|\quad a^{\phi(m)} \equiv 1 \pmod m \quad|\quad c^d \equiv m \pmod n",
        "topics": ["16 Core Theorems Quick Reference", "Algorithm Comparison Matrix", "Exam Viva Master Traps", "Formula Summary Cheat Sheet", "Final Comprehensive Mastery Exam"],
        "badge": "Final Exam"
    }
]

html_template = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Mathematics: Number Theory &amp; Cryptography — 17 Modules Course Hub</title>
    <meta name="description" content="Comprehensive 17-module course hub for Number Theory and Cryptography: Divisibility, Base-b expansions, Primes, Euclidean Algorithm, Bézout's Identity, Linear Congruences, CRT, Fermat, Euler, and RSA.">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600&family=Outfit:wght@500;600;700;800&family=Cinzel:wght@600;700;800&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="shared.css">

    <!-- MathJax 3 -->
    <script>
    MathJax = {
        tex: {
            inlineMath: [['\\\\(', '\\\\)'], ['$', '$']],
            displayMath: [['\\\\[', '\\\\]'], ['$$', '$$']],
            macros: {
                Z: '\\\\mathbb{Z}',
                N: '\\\\mathbb{N}',
                gcd: '\\\\operatorname{gcd}',
                lcm: '\\\\operatorname{lcm}'
            }
        },
        options: {
            skipHtmlTags: ['script', 'noscript', 'style', 'textarea', 'pre', 'code']
        }
    };
    </script>
    <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>

<style>
/* Imperial Oxford Amethyst & Celestial Amber Palette */
:root {
    --math-royal-900: #0f0c29;
    --math-royal-800: #1b1442;
    --math-royal-700: #301e67;
    --math-amethyst: #7c3aed;
    --math-amethyst-light: #a78bfa;
    --math-amber: #f59e0b;
    --math-amber-dark: #d97706;
    --math-gold: #fbbf24;
}

body {
    font-family: 'Inter', sans-serif;
    background: var(--bg-body);
    color: var(--text-body);
    margin: 0; padding: 0;
}

/* Hero Section */
.hub-hero {
    background: linear-gradient(135deg, #0f0c29 0%, #301e67 45%, #5b21b6 75%, #b45309 100%);
    color: white;
    padding: 65px 24px 75px;
    position: relative;
    overflow: hidden;
}

.hub-hero::before {
    content: "∀x∈ℤ ∃q,r a=dq+r gcd(a,b)=as+bt a^(p-1)≡1 mod p φ(n) c=m^e mod n";
    position: absolute;
    top: 10px;
    right: 20px;
    font-family: 'JetBrains Mono', monospace;
    font-size: 16px;
    line-height: 2.2;
    color: rgba(255, 255, 255, 0.05);
    max-width: 480px;
    word-break: break-all;
    user-select: none;
    pointer-events: none;
}

.hub-hero-container {
    max-width: 1240px;
    margin: 0 auto;
    position: relative;
    z-index: 2;
}

.hub-badge {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    background: rgba(255, 255, 255, 0.15);
    border: 1px solid rgba(255, 255, 255, 0.25);
    padding: 6px 16px;
    border-radius: 20px;
    font-size: 13px;
    font-weight: 700;
    margin-bottom: 18px;
    letter-spacing: 0.6px;
    text-transform: uppercase;
    backdrop-filter: blur(8px);
}

.hub-hero-title {
    font-family: 'Outfit', sans-serif;
    font-size: 42px;
    font-weight: 800;
    line-height: 1.2;
    margin: 0 0 16px;
    letter-spacing: -0.5px;
}

.hub-hero-title .accent-gold {
    color: #fbbf24;
    text-shadow: 0 0 25px rgba(251, 191, 36, 0.4);
}

.hub-hero-desc {
    font-size: 17.5px;
    line-height: 1.65;
    max-width: 820px;
    opacity: 0.95;
    margin-bottom: 30px;
    color: #f1f5f9;
}

.hub-hero-actions {
    display: flex;
    flex-wrap: wrap;
    gap: 14px;
}

.btn-hero-primary {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    padding: 13px 26px;
    border-radius: 10px;
    background: linear-gradient(135deg, #fbbf24, #d97706);
    color: #1e1b4b;
    font-size: 15px;
    font-weight: 800;
    text-decoration: none;
    box-shadow: 0 6px 20px rgba(217, 119, 6, 0.4);
    transition: transform 0.2s, box-shadow 0.2s;
}
.btn-hero-primary:hover {
    transform: translateY(-2px);
    box-shadow: 0 8px 25px rgba(217, 119, 6, 0.6);
}

.btn-hero-secondary {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    padding: 12px 22px;
    border-radius: 10px;
    background: rgba(255, 255, 255, 0.12);
    border: 1px solid rgba(255, 255, 255, 0.28);
    color: #ffffff;
    font-size: 14.5px;
    font-weight: 600;
    text-decoration: none;
    backdrop-filter: blur(8px);
    transition: background 0.2s, transform 0.2s;
}
.btn-hero-secondary:hover {
    background: rgba(255, 255, 255, 0.22);
    transform: translateY(-2px);
}

/* Controls Bar (Filter & Search) */
.controls-container {
    max-width: 1240px;
    margin: -30px auto 40px;
    padding: 0 24px;
    position: relative;
    z-index: 10;
}

.controls-card {
    background: var(--bg-surface);
    border: 1px solid var(--border-color);
    border-radius: 14px;
    padding: 20px 24px;
    box-shadow: var(--shadow-md);
    display: flex;
    flex-wrap: wrap;
    align-items: center;
    justify-content: space-between;
    gap: 16px;
}

.unit-filters {
    display: flex;
    flex-wrap: wrap;
    gap: 8px;
}

.filter-btn {
    padding: 8px 16px;
    border-radius: 20px;
    font-size: 13.5px;
    font-weight: 600;
    border: 1px solid var(--border-color);
    background: var(--bg-subtle);
    color: var(--text-secondary);
    cursor: pointer;
    transition: all 0.2s;
}

.filter-btn:hover {
    color: var(--text-heading);
    border-color: #7c3aed;
}

.filter-btn.active {
    background: linear-gradient(135deg, #7c3aed, #4c1d95);
    color: white;
    border-color: #7c3aed;
    box-shadow: 0 4px 12px rgba(124, 58, 237, 0.3);
}

.search-box-wrapper {
    position: relative;
    min-width: 280px;
    flex-grow: 1;
    max-width: 380px;
}

.search-box-input {
    width: 100%;
    padding: 10px 14px 10px 38px;
    border-radius: 10px;
    border: 1px solid var(--border-color);
    background: var(--bg-subtle);
    color: var(--text-heading);
    font-size: 14px;
    outline: none;
    box-sizing: border-box;
    transition: border-color 0.2s, box-shadow 0.2s;
}

.search-box-input:focus {
    border-color: #7c3aed;
    box-shadow: 0 0 0 3px rgba(124, 58, 237, 0.15);
}

.search-icon-inside {
    position: absolute;
    left: 12px;
    top: 50%;
    transform: translateY(-50%);
    color: var(--text-muted);
    font-size: 16px;
}

/* Stats Pill Bar */
.stats-strip {
    max-width: 1240px;
    margin: 0 auto 35px;
    padding: 0 24px;
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
    gap: 16px;
}

.stat-pill {
    background: var(--bg-surface);
    border: 1px solid var(--border-color);
    border-left: 4px solid #7c3aed;
    border-radius: 10px;
    padding: 14px 18px;
    display: flex;
    align-items: center;
    gap: 14px;
    box-shadow: var(--shadow-sm);
}

.stat-pill-icon {
    font-size: 24px;
    background: rgba(124, 58, 237, 0.12);
    width: 44px;
    height: 44px;
    border-radius: 10px;
    display: flex;
    align-items: center;
    justify-content: center;
    flex-shrink: 0;
}

.stat-pill-val {
    font-family: 'Outfit', sans-serif;
    font-size: 20px;
    font-weight: 800;
    color: var(--text-heading);
    line-height: 1.1;
}

.stat-pill-lbl {
    font-size: 12px;
    color: var(--text-secondary);
    font-weight: 600;
}

/* Modules Grid */
.modules-container {
    max-width: 1240px;
    margin: 0 auto 70px;
    padding: 0 24px;
}

.unit-section-title {
    font-family: 'Outfit', sans-serif;
    font-size: 24px;
    font-weight: 800;
    color: var(--text-heading);
    margin: 36px 0 20px;
    display: flex;
    align-items: center;
    gap: 10px;
    border-bottom: 2px solid rgba(124, 58, 237, 0.2);
    padding-bottom: 10px;
}

.unit-section-title span.tag {
    font-size: 12px;
    font-weight: 700;
    background: rgba(124, 58, 237, 0.15);
    color: #7c3aed;
    padding: 4px 10px;
    border-radius: 20px;
    text-transform: uppercase;
}

.modules-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(360px, 1fr));
    gap: 24px;
}

.mod-card {
    background: var(--bg-surface);
    border: 1px solid var(--border-color);
    border-radius: 14px;
    padding: 24px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    box-shadow: var(--shadow-sm);
    transition: transform 0.2s, box-shadow 0.2s, border-color 0.2s;
    position: relative;
}

.mod-card:hover {
    transform: translateY(-4px);
    box-shadow: 0 12px 28px rgba(124, 58, 237, 0.15);
    border-color: #7c3aed;
}

.mod-card-top {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 12px;
}

.mod-number {
    font-family: 'JetBrains Mono', monospace;
    font-size: 12px;
    font-weight: 700;
    color: #7c3aed;
    background: rgba(124, 58, 237, 0.1);
    padding: 4px 10px;
    border-radius: 6px;
}

.mod-badge {
    font-size: 11px;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    padding: 3px 8px;
    border-radius: 4px;
    background: rgba(217, 119, 6, 0.12);
    color: #d97706;
}

.mod-title {
    font-family: 'Outfit', sans-serif;
    font-size: 19px;
    font-weight: 700;
    color: var(--text-heading);
    margin: 0 0 10px;
    line-height: 1.35;
}

.mod-desc {
    font-size: 13.5px;
    color: var(--text-secondary);
    line-height: 1.55;
    margin: 0 0 16px;
}

/* Formula Callout in Card */
.mod-formula-preview {
    background: rgba(124, 58, 237, 0.05);
    border: 1px dashed rgba(124, 58, 237, 0.3);
    border-radius: 8px;
    padding: 10px 12px;
    margin-bottom: 16px;
    font-size: 13.5px;
    text-align: center;
    color: var(--text-heading);
    overflow-x: auto;
}

/* Topics list in Card */
.mod-topics {
    list-style: none;
    padding: 0;
    margin: 0 0 20px;
}

.mod-topics li {
    font-size: 12.5px;
    color: var(--text-body);
    margin-bottom: 6px;
    display: flex;
    align-items: center;
    gap: 8px;
}

.mod-topics li::before {
    content: "📐";
    font-size: 10px;
}

/* Card Button */
.mod-card-btn {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 8px;
    padding: 11px 18px;
    border-radius: 8px;
    background: linear-gradient(135deg, #7c3aed, #5b21b6);
    color: #ffffff;
    font-size: 14px;
    font-weight: 700;
    text-decoration: none;
    box-shadow: 0 4px 12px rgba(124, 58, 237, 0.25);
    transition: all 0.2s;
}

.mod-card-btn:hover {
    background: linear-gradient(135deg, #6d28d9, #4c1d95);
    box-shadow: 0 6px 16px rgba(124, 58, 237, 0.4);
    transform: translateY(-1px);
}

/* Theorems Quick Cheat-Section */
.theorems-section {
    max-width: 1240px;
    margin: 0 auto 70px;
    padding: 0 24px;
}

.theorems-box {
    background: var(--bg-surface);
    border: 1px solid var(--border-color);
    border-radius: 14px;
    padding: 32px;
    box-shadow: var(--shadow-sm);
}

.theorems-box h2 {
    font-family: 'Outfit', sans-serif;
    font-size: 24px;
    color: var(--text-heading);
    margin: 0 0 8px;
    display: flex;
    align-items: center;
    gap: 10px;
}

.theorems-box p {
    font-size: 14.5px;
    color: var(--text-secondary);
    line-height: 1.6;
    margin: 0 0 24px;
}

.theorems-table-wrapper {
    overflow-x: auto;
}

.theorems-table {
    width: 100%;
    border-collapse: collapse;
    font-size: 13.5px;
}

.theorems-table th {
    background: var(--bg-subtle);
    color: var(--text-heading);
    font-weight: 700;
    text-align: left;
    padding: 12px 16px;
    border-bottom: 2px solid var(--border-color);
}

.theorems-table td {
    padding: 14px 16px;
    border-bottom: 1px solid var(--border-color);
    color: var(--text-body);
    vertical-align: middle;
}

.theorems-table tr:hover td {
    background: var(--bg-card-hover);
}

@media (max-width: 768px) {
    .hub-hero-title { font-size: 32px; }
    .controls-card { flex-direction: column; align-items: stretch; }
    .search-box-wrapper { max-width: 100%; }
    .modules-grid { grid-template-columns: 1fr; }
}
</style>
</head>
<body>

<!-- GLOBAL NAVIGATION HEADER -->
<header class="global-navbar">
    <div class="nav-container">
        <a href="index.html" class="nav-brand">
            <span class="nav-brand-icon">⚡</span>
            <span class="nav-brand-text">OmniCourse<span class="nav-brand-accent">.Hub</span></span>
        </a>
        <div class="nav-links">
            <a href="index.html" class="nav-link"><span class="icon">🏠</span> All Subjects</a>
            <div class="nav-dropdown">
                <button class="nav-dropdown-btn active"><span class="icon">📐</span> Mathematics (17) ▾</button>
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
            </div>
            <div class="nav-dropdown">
                <button class="nav-dropdown-btn"><span class="icon">⛓️</span> Blockchain (13) ▾</button>
                <div class="nav-dropdown-menu">
                    <a href="blockchain.html" class="nav-dropdown-header">📋 Blockchain Syllabus Hub</a>
                    <a href="blockchain-module-1.html">Module 1: History &amp; Bitcoin</a>
                    <a href="blockchain-module-2.html">Module 2: Distributed Systems</a>
                    <a href="blockchain-module-3.html">Module 3: Consensus Protocols</a>
                    <a href="blockchain-module-4.html">Module 4: Decentralization</a>
                    <a href="blockchain-module-5.html">Module 5: Symmetric Crypto</a>
                    <a href="blockchain-module-6.html">Module 6: Public Key Crypto</a>
                    <a href="blockchain-module-7.html">Module 7: Digital Signatures</a>
                    <a href="blockchain-module-8.html">Module 8: SHA &amp; Hashes</a>
                    <a href="blockchain-module-9.html">Module 9: Consensus Problem &amp; Design</a>
                    <a href="blockchain-module-10.html">Module 10: Paxos, Raft &amp; PBFT</a>
                    <a href="blockchain-module-11.html">Module 11: PoW, PoS &amp; Selection</a>
                    <a href="blockchain-module-12.html">Module 12: Bitcoin Keys &amp; UTXO</a>
                    <a href="blockchain-module-13.html">Module 13: Mining, Network &amp; Forks</a>
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
            <a href="index.html" class="nav-action-pill" style="background: linear-gradient(135deg, #7c3aed, #4c1d95);" title="Back to main portal">🏠 Main Portal</a>
        </div>
    </div>
</header>

<!-- HERO SECTION -->
<section class="hub-hero">
    <div class="hub-hero-container">
        <div class="hub-badge">📐 Discrete Mathematics &bull; Number Theory &amp; Cryptography</div>
        <h1 class="hub-hero-title">Number Theory &amp; <span class="accent-gold">Cryptographic Foundations</span></h1>
        <p class="hub-hero-desc">An exhaustive 17-module academic reference covering Integer Divisibility, Base-b Radix Expansions, Prime Factorization, Euclidean &amp; Extended GCD Algorithms, Bézout's Identity, Linear Congruences, Chinese Remainder Theorem, Fermat's Little Theorem, Euler's Totient, and the RSA Cryptosystem. Formatted with rigorous LaTeX formulas and interactive self-grading quizzes.</p>
        <div class="hub-hero-actions">
            <a href="maths-module-1.html" class="btn-hero-primary">Start Module 01 &rarr;</a>
            <a href="maths-module-11.html" class="btn-hero-secondary">⚡ Bézout &amp; Extended GCD (Mod 11)</a>
            <a href="maths-module-13.html" class="btn-hero-secondary">📜 Chinese Remainder Theorem (Mod 13)</a>
            <a href="maths-module-16.html" class="btn-hero-secondary">🔐 RSA Cryptosystem (Mod 16)</a>
            <a href="maths-module-17.html" class="btn-hero-secondary">🎯 Comprehensive Exam (Mod 17)</a>
        </div>
    </div>
</section>

<!-- CONTROLS BAR (FILTERS & REAL-TIME SEARCH) -->
<div class="controls-container">
    <div class="controls-card">
        <div class="unit-filters" id="unitFilters">
            <button class="filter-btn active" data-unit="all">All 17 Modules</button>
            <button class="filter-btn" data-unit="1">Unit 1: Divisibility &amp; Bases (1–5)</button>
            <button class="filter-btn" data-unit="2">Unit 2: Primes &amp; GCD (6–11)</button>
            <button class="filter-btn" data-unit="3">Unit 3: Congruences &amp; CRT (12–15)</button>
            <button class="filter-btn" data-unit="4">Unit 4: RSA &amp; Mastery (16–17)</button>
        </div>
        <div class="search-box-wrapper">
            <span class="search-icon-inside">🔍</span>
            <input type="text" id="mathSearchInput" class="search-box-input" placeholder="Filter math modules &amp; theorems...">
        </div>
    </div>
</div>

<!-- STATS STRIP -->
<div class="stats-strip">
    <div class="stat-pill">
        <div class="stat-pill-icon">📐</div>
        <div>
            <div class="stat-pill-val">17</div>
            <div class="stat-pill-lbl">Interactive Modules</div>
        </div>
    </div>
    <div class="stat-pill">
        <div class="stat-pill-icon">🧠</div>
        <div>
            <div class="stat-pill-val">17</div>
            <div class="stat-pill-lbl">Self-Grading Quizzes</div>
        </div>
    </div>
    <div class="stat-pill">
        <div class="stat-pill-icon">✨</div>
        <div>
            <div class="stat-pill-val">100%</div>
            <div class="stat-pill-lbl">LaTeX MathJax Rendered</div>
        </div>
    </div>
    <div class="stat-pill">
        <div class="stat-pill-icon">🔐</div>
        <div>
            <div class="stat-pill-val">RSA</div>
            <div class="stat-pill-lbl">Applied Public Key Protocol</div>
        </div>
    </div>
</div>

<!-- MODULES GRID -->
<div class="modules-container">
'''

# Generate module cards grouped by units
units_info = {
    1: "Unit 1: Divisibility, Modular Arithmetic & Base Expansions",
    2: "Unit 2: Prime Numbers, GCD, Euclidean Algorithm & Bézout's Identity",
    3: "Unit 3: Linear Congruences, Chinese Remainder Theorem & Euler's Totient",
    4: "Unit 4: Public-Key Cryptography (RSA) & Course Mastery Exam"
}

current_unit = None
for m in modules_data:
    if m["unit"] != current_unit:
        current_unit = m["unit"]
        html_template += f'''
    <div class="unit-group" data-unit-group="{current_unit}">
        <h2 class="unit-section-title">
            <span class="tag">Unit 0{current_unit}</span>
            {units_info[current_unit]}
        </h2>
        <div class="modules-grid">
'''
    topics_html = "".join([f"<li>{t}</li>" for t in m["topics"]])
    html_template += f'''
            <div class="mod-card" data-unit="{m['unit']}" data-search="{m['title'].lower()} {' '.join(m['topics']).lower()}">
                <div>
                    <div class="mod-card-top">
                        <span class="mod-number">MODULE {m['num']:02d}</span>
                        <span class="mod-badge">{m['badge']}</span>
                    </div>
                    <h3 class="mod-title">{m['title']}</h3>
                    <p class="mod-desc">{m['desc']}</p>
                    <div class="mod-formula-preview">
                        \\[ {m['formula']} \\]
                    </div>
                    <ul class="mod-topics">
                        {topics_html}
                    </ul>
                </div>
                <a href="maths-module-{m['num']}.html" class="mod-card-btn">
                    <span>Read Module &amp; Take Quiz</span> &rarr;
                </a>
            </div>
'''
    # Check if next module is different unit or end
    idx = modules_data.index(m)
    if idx == len(modules_data) - 1 or modules_data[idx+1]["unit"] != current_unit:
        html_template += '''
        </div>
    </div>
'''

html_template += '''
</div>

<!-- THEOREMS QUICK LOOKUP SECTION -->
<div class="theorems-section">
    <div class="theorems-box">
        <h2>⚡ 6 Fundamental Theorems Quick-Lookup</h2>
        <p>The definitive mathematical theorems tested in discrete mathematics and modern cryptographic protocols:</p>
        <div class="theorems-table-wrapper">
            <table class="theorems-table">
                <thead>
                    <tr>
                        <th>Theorem Name</th>
                        <th>Mathematical Statement</th>
                        <th>Core Condition</th>
                        <th>Module Link</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td><strong>The Division Algorithm</strong></td>
                        <td>\\( a = d \\cdot q + r \\)</td>
                        <td>\\( 0 \\le r < d \\) unique \\( q, r \\)</td>
                        <td><a href="maths-module-1.html">Module 01 &rarr;</a></td>
                    </tr>
                    <tr>
                        <td><strong>Fundamental Theorem of Arithmetic</strong></td>
                        <td>\\( n = p_1^{a_1} p_2^{a_2} \\dots p_k^{a_k} \\)</td>
                        <td>Unique up to prime order</td>
                        <td><a href="maths-module-7.html">Module 07 &rarr;</a></td>
                    </tr>
                    <tr>
                        <td><strong>Bézout's Identity</strong></td>
                        <td>\\( a \\cdot s + b \\cdot t = \\gcd(a, b) \\)</td>
                        <td>\\( s, t \\in \\mathbb{Z} \\) from Extended GCD</td>
                        <td><a href="maths-module-11.html">Module 11 &rarr;</a></td>
                    </tr>
                    <tr>
                        <td><strong>Chinese Remainder Theorem</strong></td>
                        <td>\\( x \\equiv \\sum a_i M_i y_i \\pmod M \\)</td>
                        <td>Pairwise coprime moduli \\( \\gcd(m_i, m_j) = 1 \\)</td>
                        <td><a href="maths-module-13.html">Module 13 &rarr;</a></td>
                    </tr>
                    <tr>
                        <td><strong>Fermat's Little Theorem</strong></td>
                        <td>\\( a^{p-1} \\equiv 1 \\pmod p \\)</td>
                        <td>\\( p \\text{ is prime}, \\; p \\nmid a \\)</td>
                        <td><a href="maths-module-14.html">Module 14 &rarr;</a></td>
                    </tr>
                    <tr>
                        <td><strong>Euler's Totient Generalization</strong></td>
                        <td>\\( a^{\\phi(m)} \\equiv 1 \\pmod m \\)</td>
                        <td>\\( \\gcd(a, m) = 1 \\)</td>
                        <td><a href="maths-module-15.html">Module 15 &rarr;</a></td>
                    </tr>
                </tbody>
            </table>
        </div>
    </div>
</div>

<!-- FOOTER -->
<footer class="portal-footer">
    <div class="portal-footer-container">
        <div class="footer-col">
            <h4>OmniCourse Hub</h4>
            <p>A unified, interactive study and revision platform built for Computer Science &amp; Engineering students.</p>
        </div>
        <div class="footer-col">
            <h4>Courses</h4>
            <ul>
                <li><a href="maths.html">Mathematics: Number Theory (17 Modules)</a></li>
                <li><a href="blockchain.html">Blockchain &amp; Cryptography (13 Modules)</a></li>
                <li><a href="django.html">Django Web Framework (45 Modules)</a></li>
            </ul>
        </div>
        <div class="footer-col">
            <h4>Special Links</h4>
            <ul>
                <li><a href="maths-module-16.html">RSA Cryptosystem Masterclass</a></li>
                <li><a href="maths-module-17.html">Comprehensive Mastery Exam</a></li>
                <li><a href="blockchain-module-6.html">Public Key Cryptography in Blockchain</a></li>
            </ul>
        </div>
        <div class="footer-col">
            <h4>Repository</h4>
            <ul>
                <li><a href="https://github.com/amanrj03/Django-Full-Course.git" target="_blank" rel="noopener">GitHub Project</a></li>
                <li><a href="index.html">Master Portal Home</a></li>
            </ul>
        </div>
    </div>
    <div class="footer-bottom">
        <div>&copy; 2026 OmniCourse Hub. Open Source &amp; Free for All Learners.</div>
        <div>Connected via Git Repository</div>
    </div>
</footer>

<script src="shared.js"></script>
<script>
// Filter by Unit
const filterBtns = document.querySelectorAll('.filter-btn');
const modCards = document.querySelectorAll('.mod-card');
const unitGroups = document.querySelectorAll('.unit-group');
const searchInput = document.getElementById('mathSearchInput');

function applyFilters() {
    const activeBtn = document.querySelector('.filter-btn.active');
    const selectedUnit = activeBtn ? activeBtn.getAttribute('data-unit') : 'all';
    const query = searchInput.value.toLowerCase().trim();

    modCards.forEach(card => {
        const cardUnit = card.getAttribute('data-unit');
        const cardSearch = card.getAttribute('data-search') || '';
        
        const matchesUnit = (selectedUnit === 'all' || cardUnit === selectedUnit);
        const matchesQuery = (!query || cardSearch.includes(query));

        if (matchesUnit && matchesQuery) {
            card.style.display = 'flex';
        } else {
            card.style.display = 'none';
        }
    });

    // Hide/show unit groups based on whether they contain visible cards
    unitGroups.forEach(group => {
        const visibleCards = group.querySelectorAll('.mod-card:not([style*="display: none"])');
        if (visibleCards.length > 0) {
            group.style.display = 'block';
        } else {
            group.style.display = 'none';
        }
    });
}

filterBtns.forEach(btn => {
    btn.addEventListener('click', () => {
        filterBtns.forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
        applyFilters();
    });
});

searchInput.addEventListener('input', applyFilters);
</script>
</body>
</html>
'''

with open("d:/Blockchain HTML/Django HTML/maths.html", "w", encoding="utf-8") as f:
    f.write(html_template)
print("maths.html written successfully!")
