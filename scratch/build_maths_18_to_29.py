# -*- coding: utf-8 -*-
"""
Builder script for Mathematics Modules 18 to 29:
- Unit IV: Classical Cryptography & Substitution Ciphers (Modules 18-25)
- Unit V: Public Key Cryptography, Diffie-Hellman, RSA & ElGamal (Modules 26-29)

Full visual integrity:
- Amethyst and Celestial Amber theme
- Crisp MathJax 3 LaTeX rendering (zero unrendered math, zero stray backslashes)
- Specialized visual concept cards, tables, alignment strips, and architecture diagrams
- Interactive self-grading quizzes with step-by-step mathematical explanations
"""

import os
import re
import markdown

import render_maths_diagrams_unit4_5 as diag
from extract_questions_18_29 import parse_module_questions
from quiz_data_unit4_5 import MATHS_SOLUTIONS_18_29, EXPLANATIONS_18_29
from quiz_data_unit4_5_extra import EXTRA_MODULE_QUESTIONS

RAW_DIR = r"raw_notes/NumberTheory&Cryptography"
OUT_DIR = r"."

MATH_TITLES = {
    1: "Divisibility and the Division Algorithm",
    2: "Modular Arithmetic and Congruences",
    3: "Integer Representations and Base Expansions",
    4: "Octal, Hexadecimal & Fast Base Conversions",
    5: "Algorithms for Integer Operations",
    6: "Prime and Composite Numbers",
    7: "Fundamental Theorem of Arithmetic",
    8: "Trial Division and the Sieve of Eratosthenes",
    9: "Prime Number Theorem and Prime Distribution",
    10: "GCD, LCM and the Euclidean Algorithm",
    11: "GCD as a Linear Combination (Bézout's Theorem)",
    12: "Linear Congruences and Modular Inverses",
    13: "Chinese Remainder Theorem (CRT)",
    14: "Computer Arithmetic with Large Integers",
    15: "Fermat's Little Theorem (FLT)",
    16: "Applications of Congruences",
    17: "Mixed MCQ Mastery and Final Revision",
    18: "Introduction to Cryptography & Security Models",
    19: "Classical Cryptography & Substitution Ciphers",
    20: "Shift Cipher and Caesar Cipher",
    21: "Affine Cipher & Modular Inverses",
    22: "Vigenère Polyalphabetic Cipher & Tableau",
    23: "Hill Cipher & Matrix Cryptography",
    24: "Permutation & Transposition Ciphers",
    25: "Mathematical Cryptosystems & Attack Models",
    26: "Foundations of Public Key Cryptography & Fast Modular Exponentiation",
    27: "Diffie-Hellman Key Exchange & Discrete Logarithm Problem",
    28: "The RSA Cryptosystem: Key Generation, Encryption & Decryption",
    29: "The ElGamal Cryptosystem & Comprehensive Unit V Exam Mastery"
}

def get_unit_info(mod_num):
    if mod_num <= 5:
        return "Unit I: Divisibility & Base Expansions", "Unit I (Mods 1–5)", 1
    elif mod_num <= 11:
        return "Unit II: Primes, Divisibility Tests & GCD", "Unit II (Mods 6–11)", 2
    elif mod_num <= 17:
        return "Unit III: Congruences, CRT & Fermat/Euler", "Unit III (Mods 12–17)", 3
    elif mod_num <= 25:
        return "Unit IV: Classical Cryptography & Ciphers", "Unit IV (Mods 18–25)", 4
    else:
        return "Unit V: Public Key Cryptography & Modern Protocols", "Unit V (Mods 26–29)", 5

def get_nav_items_html(curr_mod):
    items = []
    current_unit = None
    for i in range(1, 30):
        unit_name, unit_short, u_idx = get_unit_info(i)
        if u_idx != current_unit:
            current_unit = u_idx
            items.append(f'<div style="font-size: 11px; font-weight: 800; color: #7c3aed; text-transform: uppercase; margin: 10px 0 4px; padding-left: 6px; letter-spacing: 0.5px; break-inside: avoid;">{unit_short}</div>')
        t = MATH_TITLES[i]
        if i == curr_mod:
            items.append(f'<span class="nav-item current">{i}. {t}</span>')
        else:
            items.append(f'<a class="nav-item" href="maths-module-{i}.html">{i}. {t}</a>')
    return '\n'.join(items)

def get_global_nav_html(curr_mod):
    dropdown_items = []
    current_u = None
    for i in range(1, 30):
        unit_name, unit_short, u_idx = get_unit_info(i)
        if u_idx != current_u:
            current_u = u_idx
            dropdown_items.append(f'<div class="dropdown-section-title" style="font-size: 10.5px; font-weight: 700; color: #7c3aed; padding: 4px 14px; text-transform: uppercase; background: rgba(124, 58, 237, 0.08);">{unit_name}</div>')
        t = MATH_TITLES[i]
        dropdown_items.append(f'<a href="maths-module-{i}.html">Module {i}: {t}</a>')
    math_links_str = '\n'.join(dropdown_items)

    return f'''
    <header class="global-navbar">
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
                        {math_links_str}
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
    </header>
    '''

def inject_diagram_tokens_for_maths(text, mod_num):
    if mod_num == 18:
        # Communication model & Kerckhoffs principle
        text = re.sub(r'(\*\*Basic cryptographic communication\*\*.*?\n)', r'\1\n\nTOKEN_MATH_DIAG_18_COMM\n\n', text, count=1)
        text = re.sub(r'(##\s+\*\*1\.8 Kerckhoffs\'s principle.*?\n)', r'\1\n\nTOKEN_MATH_DIAG_18_KERCK\n\n', text, count=1)
    elif mod_num == 19:
        # Frequency table
        text = re.sub(r'(##\s+\*\*2\.4 Why monoalphabetic substitution is vulnerable.*?\n)', r'\1\n\nTOKEN_MATH_DIAG_19_FREQ\n\n', text, count=1)
    elif mod_num == 20:
        # Alphabet ribbon & Caesar wheel
        text = re.sub(r'(##\s+\*\*3\.2 Convert letters into numbers.*?\n)', r'\1\n\nTOKEN_MATH_DIAG_20_RIBBON\n\n', text, count=1)
        text = re.sub(r'(##\s+\*\*3\.5 Caesar cipher — Key = 3.*?\n)', r'\1\n\nTOKEN_MATH_DIAG_20_WHEEL\n\n', text, count=1)
    elif mod_num == 21:
        # Affine inverses table
        text = re.sub(r'(##\s+\*\*4\.7 Modular multiplicative inverse table.*?\n|4\.7 Modular multiplicative inverse table\n)', r'\1\n\nTOKEN_MATH_DIAG_21_INV\n\n', text, count=1)
    elif mod_num == 22:
        # Vigenere alignment
        text = re.sub(r'(\*\*5\.5 Rosen\'s complete worked example: Encrypt ORANGE using RED\*\*.*?\n)', r'\1\n\nTOKEN_MATH_DIAG_22_ALIGN\n\n', text, count=1)
    elif mod_num == 23:
        # Hill matrix
        text = re.sub(r'(##\s+\*\*6\.2 Mathematical representation.*?\n)', r'\1\n\nTOKEN_MATH_DIAG_23_MATRIX\n\n', text, count=1)
    elif mod_num == 24:
        # Transposition grid
        text = re.sub(r'(##\s+\*\*7\.2 Mathematical definition of a permutation.*?\n)', r'\1\n\nTOKEN_MATH_DIAG_24_TRANS\n\n', text, count=1)
    elif mod_num == 25:
        # Cryptosystem 5-tuple
        text = re.sub(r'(##\s+\*\*8\.1 What is a cryptosystem\?.*?\n)', r'\1\n\nTOKEN_MATH_DIAG_25_TUPLE\n\n', text, count=1)
    elif mod_num == 26:
        # Trapdoor & repeated squaring
        text = re.sub(r'(##\s+2\.\s+The Number Theory Tools.*?\n)', r'\1\n\nTOKEN_MATH_DIAG_26_TRAP\n\n', text, count=1)
    elif mod_num == 27:
        # Diffie-Hellman protocol
        text = re.sub(r'(###?\s+2\.\s+The Protocol \(Step-by-Step for Exams\).*?\n|2\.\s+The Protocol \(Step-by-Step for Exams\)\n)', r'\1\n\nTOKEN_MATH_DIAG_27_DH\n\n', text, count=1)
    elif mod_num == 28:
        # RSA architecture
        text = re.sub(r'(###?\s+2\.\s+RSA Key Generation \(Step-by-Step\).*?\n|2\.\s+RSA Key Generation \(Step-by-Step\)\n)', r'\1\n\nTOKEN_MATH_DIAG_28_RSA\n\n', text, count=1)
    elif mod_num == 29:
        # Cryptosystems comparison
        text = re.sub(r'(###?\s+1\.\s+The Mathematical Foundation.*?\n|1\.\s+The Mathematical Foundation\n)', r'\1\n\nTOKEN_MATH_DIAG_29_COMP\n\n', text, count=1)
    return text

def replace_diagram_tokens_for_maths(html, mod_num):
    diag_map = {
        18: {
            "TOKEN_MATH_DIAG_18_COMM": diag.card_mod18_communication_model(),
            "TOKEN_MATH_DIAG_18_KERCK": diag.card_mod18_kerckhoffs_principles(),
        },
        19: {
            "TOKEN_MATH_DIAG_19_FREQ": diag.card_mod19_frequency_table(),
        },
        20: {
            "TOKEN_MATH_DIAG_20_RIBBON": diag.card_mod20_alphabet_ribbon(),
            "TOKEN_MATH_DIAG_20_WHEEL": diag.card_mod20_caesar_wheel(),
        },
        21: {
            "TOKEN_MATH_DIAG_21_INV": diag.card_mod21_affine_inverses(),
        },
        22: {
            "TOKEN_MATH_DIAG_22_ALIGN": diag.card_mod22_vigenere_alignment(),
        },
        23: {
            "TOKEN_MATH_DIAG_23_MATRIX": diag.card_mod23_hill_matrix(),
        },
        24: {
            "TOKEN_MATH_DIAG_24_TRANS": diag.card_mod24_transposition_grid(),
        },
        25: {
            "TOKEN_MATH_DIAG_25_TUPLE": diag.card_mod25_cryptosystem_tuple(),
        },
        26: {
            "TOKEN_MATH_DIAG_26_TRAP": diag.card_mod26_trapdoor_squaring(),
        },
        27: {
            "TOKEN_MATH_DIAG_27_DH": diag.card_mod27_diffie_hellman_protocol(),
        },
        28: {
            "TOKEN_MATH_DIAG_28_RSA": diag.card_mod28_rsa_architecture(),
        },
        29: {
            "TOKEN_MATH_DIAG_29_COMP": diag.card_mod29_cryptosystems_comparison(),
        }
    }
    tokens = diag_map.get(mod_num, {})
    for token, d_html in tokens.items():
        html = html.replace(f"<p>{token}</p>", d_html)
        html = html.replace(token, d_html)
    return html

def render_interactive_quiz_for_maths(mod_num, questions):
    solutions = MATHS_SOLUTIONS_18_29.get(mod_num, [])
    explanations = EXPLANATIONS_18_29.get(mod_num, {})
    total = len(questions)

    blocks_html = []
    for q_idx, q in enumerate(questions):
        q_num = q_idx + 1
        corr_idx = solutions[q_idx] if q_idx < len(solutions) else 0
        expl_text = explanations.get(q_num, "Refer to the textbook proof and definitions in this module.")

        opts_html = []
        for o_idx, opt in enumerate(q['options']):
            let = "ABCD"[o_idx]
            opts_html.append(f'''
            <label class="q-opt" id="q_{mod_num}_{q_num}_opt_{o_idx}">
                <input type="radio" name="math_q_{mod_num}_{q_num}" value="{o_idx}">
                <span><strong>{let}.</strong> {opt}</span>
            </label>
            ''')
        opts_str = "\n".join(opts_html)

        blocks_html.append(f'''
        <div class="q-block" id="q_block_{mod_num}_{q_num}" data-corr="{corr_idx}">
            <div class="q-title"><span class="q-num">{q_num}.</span> <span>{q['text']}</span></div>
            <div class="q-options">
                {opts_str}
            </div>
            <div class="q-explanation" id="q_expl_{mod_num}_{q_num}">
                <strong>Mathematical Explanation:</strong> {expl_text}
            </div>
        </div>
        ''')

    all_blocks_str = "\n".join(blocks_html)

    return f'''
    <div class="quiz-section-wrap" id="moduleQuizContainer_{mod_num}">
        <div class="quiz-card-container">
            <div class="quiz-header">
                <div>
                    <div class="quiz-badge">🧠 Interactive Knowledge Check &bull; Module {mod_num}</div>
                    <h3 class="quiz-title">Self-Grading Multiple Choice Examination</h3>
                    <p class="quiz-subtitle">Attempt all {total} questions to test your mathematical comprehension and exam readiness. Solutions and step-by-step logic unlock instantly.</p>
                </div>
                <div class="quiz-score-badge" id="quizScoreBadge_{mod_num}" style="display: none;">
                    <span id="quizScoreVal_{mod_num}">0</span>/{total} &bull; <span id="quizScorePct_{mod_num}">0%</span>
                </div>
            </div>

            <div class="quiz-body">
                {all_blocks_str}
            </div>

            <div class="quiz-actions">
                <button type="button" class="btn-quiz-check" onclick="checkMathQuiz({mod_num}, {total})">✓ Check Answers &amp; View Solutions</button>
                <button type="button" class="btn-quiz-reset" onclick="resetMathQuiz({mod_num}, {total})">↺ Reset Quiz</button>
            </div>
        </div>
    </div>
    '''

def convert_txt_to_html_body_unit4_5(raw_text, mod_num):
    text = raw_text

    # Extract quiz questions from raw notes or extra definitions
    parsed_qs = parse_module_questions(text)
    if not parsed_qs and mod_num in EXTRA_MODULE_QUESTIONS:
        parsed_qs = EXTRA_MODULE_QUESTIONS[mod_num]
    
    quiz_html = render_interactive_quiz_for_maths(mod_num, parsed_qs)

    # Cut off raw quiz section from text
    split_markers = [
        "## **1.10 Module 1 MCQ test**",
        "## **2.9 Module 2 MCQ test**",
        "## **3.12 Module 3 MCQ test**",
        "MCQ test\nModule 4 test",
        "## **5.14 Module 5 MCQ test**",
        "## **6.12 Module 6 MCQ test**",
        "## **7.13 Module 7 MCQ test**",
        "## **8.10 Module 8 MCQ test**",
        "Part A: Multiple Choice Questions (1 Mark Each)"
    ]
    has_cut = False
    for sm in split_markers:
        idx = text.find(sm)
        if idx != -1:
            # Check if there is a revision sheet after quiz
            rev_idx = text.find("Final revision sheet", idx)
            if rev_idx != -1:
                # Find start of heading before Final revision sheet
                h_idx = text.rfind("#", idx, rev_idx)
                if h_idx == -1: h_idx = rev_idx
                rev_part = text[h_idx:]
                text = text[:idx] + "\n\nMATHQUIZTOKENXYZ\n\n" + rev_part
            else:
                text = text[:idx] + "\n\nMATHQUIZTOKENXYZ\n\n"
            has_cut = True
            break
    if not has_cut:
        text = text + "\n\nMATHQUIZTOKENXYZ\n\n"

    # Clean textbook / slide references
    text = re.sub(r'(?m)^\s*MTH381[A-Za-z0-9_\-\s]+\.pdf(?:\s*&#x20;)?\s*$', '', text)
    text = re.sub(r'([A-Za-z0-9_\-]+\s+U[0-9]+\s+TB\.pdf)', r'<span class="ref-pill">📚 Textbook Reference: \1</span>', text)
    text = re.sub(r'([A-Za-z0-9_\-]+\.pdf)', r'<span class="ref-pill">📚 Reference: \1</span>', text)
    text = text.replace('&#x20;', '')

    # Inject visual diagrams tokens
    text = inject_diagram_tokens_for_maths(text, mod_num)

    # Protect array linebreaks like \\[2pt] inside LaTeX
    text = re.sub(r'\\\\\[(\d+pt)\]', r'ARRAYLINEBREAK\1END', text)

    # Protect MathJax display math \\[ ... \\], \[ ... \], $$ ... $$
    math_display = []
    def rep_disp(m):
        idx = len(math_display)
        c = m.group(1).strip()
        c = re.sub(r'ARRAYLINEBREAK(\d+pt)END', r'\\\\\\[\1\\]', c)
        c = c.replace(r'\_', '_').replace(r'\\%', r'\%')
        # Fix set braces \\{ and \\} and escaped hash \\#
        c = c.replace(r'\\#', r'\#').replace(r'\\{', r'\{').replace(r'\\}', r'\}')
        c = re.sub(r'(?<!\\)#', r'\#', c)
        # Fix \|a\| to |a| (norm to absolute value)
        c = re.sub(r'\\\|([^|]+?)\\\|', r'|\1|', c)
        # Fix all \< and < to \lt
        c = c.replace(r'\<', r'\lt ').replace('<', r'\lt ')
        # Fix all \> and > to \gt
        c = c.replace(r'\>', r'\gt ').replace('>', r'\gt ')
        math_display.append(c)
        return f"\n\nMATHDISPTOKEN{idx}END\n\n"

    text = re.sub(r'\\+\[(.*?)\\+\]', rep_disp, text, flags=re.DOTALL)
    text = re.sub(r'\$\$(.*?)\$\$', rep_disp, text, flags=re.DOTALL)

    # Protect Inline Math \\( ... \\), \( ... \)
    math_inline = []
    def rep_inline(m):
        idx = len(math_inline)
        c = m.group(1).strip()
        c = c.replace(r'\_', '_').replace(r'\\%', r'\%')
        c = c.replace(r'\\#', r'\#').replace(r'\\{', r'\{').replace(r'\\}', r'\}')
        c = re.sub(r'(?<!\\)#', r'\#', c)
        c = re.sub(r'\\\|([^|]+?)\\\|', r'|\1|', c)
        c = c.replace(r'\<', r'\lt ').replace('<', r'\lt ')
        c = c.replace(r'\>', r'\gt ').replace('>', r'\gt ')
        math_inline.append(c)
        return f"MATHINLTOKEN{idx}END"

    text = re.sub(r'\\+\((.*?)\\+\)', rep_inline, text)

    # Protect HTML tags, then escape remaining raw < and >
    html_tags = []
    def rep_tag(m):
        idx = len(html_tags)
        html_tags.append(m.group(0))
        return f"HTMLTAGTOKEN{idx}END"

    text = re.sub(r'</?[a-zA-Z][^>]*>', rep_tag, text)
    text = re.sub(r'\\<', '&lt;', text)
    text = re.sub(r'\\>', '&gt;', text)
    text = text.replace('<', '&lt;').replace('>', '&gt;')

    for idx, tag in enumerate(html_tags):
        text = text.replace(f"HTMLTAGTOKEN{idx}END", tag)

    # Strip initial module title heading
    text = re.sub(r'^#\s+(?:Unit\s+[IVXLCDM]+\s+[—\-]\s+)?Module\s+\d+[^#\n]+\n', '', text, flags=re.IGNORECASE)

    # For Module 21: format headings that lack markdown markers
    if mod_num == 21:
        lines = text.splitlines()
        f_lines = []
        for l in lines:
            s = l.strip()
            if re.match(r'^\d+\.\d+\s', s) and not s.startswith('#'):
                f_lines.append(f"## **{s}**")
            elif s.startswith('Submit answers') or s.startswith('Module 4 complete'):
                f_lines.append(f"### **{s}**")
            else:
                f_lines.append(l)
        text = "\n".join(f_lines)

    # Markdown conversion
    html = markdown.markdown(text, extensions=['tables', 'fenced_code'])

    # Restore diagram tokens to real visual HTML
    html = replace_diagram_tokens_for_maths(html, mod_num)

    # Restore MathJax display and inline
    for idx, tex in enumerate(math_display):
        token = f"MATHDISPTOKEN{idx}END"
        rep_html = f'<div class="math-display">\\[{tex}\\]</div>'
        html = html.replace(f"<p>{token}</p>", rep_html)
        html = html.replace(token, rep_html)

    for idx, tex in enumerate(math_inline):
        token = f"MATHINLTOKEN{idx}END"
        rep_html = f'<span class="math-inline">\\({tex}\\)</span>'
        html = html.replace(f"<p>{token}</p>", rep_html)
        html = html.replace(token, rep_html)

    # Restore Quiz
    html = re.sub(r'<p>\s*MATHQUIZTOKENXYZ\s*</p>', lambda m: quiz_html, html)
    html = html.replace("MATHQUIZTOKENXYZ", quiz_html)

    # Enhance Callouts & Banners
    html = re.sub(r'<h3>(Theorem[^<]*)</h3>', r'<div class="math-callout theorem"><div class="callout-badge theorem">📐 THEOREM</div><div class="callout-title">\1</div></div>', html, flags=re.IGNORECASE)
    html = re.sub(r'<h3>(Definition[^<]*)</h3>', r'<div class="math-callout definition"><div class="callout-badge definition">📖 DEFINITION</div><div class="callout-title">\1</div></div>', html, flags=re.IGNORECASE)
    html = re.sub(r'<h3>(Property\s*\d*[^<]*)</h3>', r'<div class="math-callout property"><div class="callout-badge property">⚖️ PROPERTY</div><div class="callout-title">\1</div></div>', html, flags=re.IGNORECASE)
    html = re.sub(r'<h3>(Worked example[^<]*|Example\s*\d*[^<]*)</h3>', r'<div class="math-callout example"><div class="callout-badge example">💡 WORKED EXAMPLE</div><div class="callout-title">\1</div></div>', html, flags=re.IGNORECASE)
    html = re.sub(r'<h2>(Final revision sheet|Revision sheet|High-yield formula sheet|Module \d+ — Final revision sheet)[^<]*</h2>', r'<div class="exam-header-banner">🎯 \1</div>', html, flags=re.IGNORECASE)

    # Safety cleanups for stray backslashes
    html = re.sub(r'<p>\s*\\+\s*</p>', '', html)
    html = re.sub(r'<p>\s*\\+<div', '<div', html)
    html = re.sub(r'</div>\s*\\+</p>', '</div>', html)

    return html

def generate_maths_module_page(mod_num):
    raw_path = os.path.join(RAW_DIR, f"{mod_num}.txt")
    if not os.path.exists(raw_path):
        print(f"Error: {raw_path} not found!")
        return

    with open(raw_path, 'r', encoding='utf-8') as f:
        raw_text = f.read()

    body_html = convert_txt_to_html_body_unit4_5(raw_text, mod_num)
    nav_items_html = get_nav_items_html(mod_num)
    global_nav_html = get_global_nav_html(mod_num)
    unit_name, unit_short, u_idx = get_unit_info(mod_num)
    title = MATH_TITLES[mod_num]

    prev_link = f"maths-module-{mod_num-1}.html"
    prev_label = f"&larr; Module {mod_num-1}"

    if mod_num < 29:
        next_link = f"maths-module-{mod_num+1}.html"
        next_label = f"Module {mod_num+1} &rarr;"
        completion_msg = f'''
        <div style="margin-top: 35px; padding: 20px 24px; background: rgba(124, 58, 237, 0.05); border: 1.5px solid rgba(124, 58, 237, 0.25); border-radius: 12px;">
            <h4 style="margin: 0 0 6px 0; color: #7c3aed; font-size: 16px;">🚀 Ready for the Next Step?</h4>
            <p style="margin: 0; font-size: 14px; color: var(--text-body);">
                You have completed <strong>Module {mod_num}: {title}</strong>. Test your knowledge with the interactive quiz above, review key theorems, and proceed to <a href="{next_link}" style="color: #7c3aed; font-weight: 700;">Module {mod_num+1}: {MATH_TITLES[mod_num+1]} &rarr;</a>
            </p>
        </div>
        '''
    else:
        next_link = "maths.html"
        next_label = "Complete Course Review &check;"
        completion_msg = f'''
        <div style="margin-top: 35px; padding: 24px 28px; background: rgba(16, 185, 129, 0.06); border: 1.5px solid rgba(16, 185, 129, 0.35); border-radius: 12px;">
            <h4 style="margin: 0 0 8px 0; color: #059669; font-size: 18px;">🎓 All 29 Mathematics Modules Completed!</h4>
            <p style="margin: 0; font-size: 14.5px; color: var(--text-body); line-height: 1.6;">
                Outstanding achievement! You have mastered all 29 modules across <strong>Unit I (Divisibility &amp; Radix Expansions), Unit II (Primes &amp; GCD), Unit III (Congruences, CRT &amp; Fermat), Unit IV (Classical Cryptography &amp; Ciphers), and Unit V (Public Key Cryptography &amp; Modern Protocols)</strong>. Review the syllabus hub, recap key revision sheets, and retake quizzes for 100% exam mastery!
            </p>
        </div>
        '''
    body_html += "\n" + completion_msg

    full_page_html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Module {mod_num}: {title} — Mathematics Study Guide</title>
    <meta name="description" content="Number Theory &amp; Cryptography study notes — Module {mod_num} of 29: {title}. Complete with theorems, proofs, worked examples, and interactive self-test quiz.">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;500&family=Outfit:wght@500;600;700;800&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="shared.css">

    <!-- MathJax 3 configuration for crisp LaTeX rendering -->
    <script>
    MathJax = {{
        tex: {{
            inlineMath: [['\\\\(', '\\\\)'], ['$', '$']],
            displayMath: [['$$', '$$'], ['\\\\[', '\\\\]']],
            processEscapes: true,
            macros: {{
                Z: '\\\\mathbb{{Z}}',
                N: '\\\\mathbb{{N}}',
                R: '\\\\mathbb{{R}}',
                Q: '\\\\mathbb{{Q}}',
                gcd: '\\\\operatorname{{gcd}}',
                lcm: '\\\\operatorname{{lcm}}'
            }}
        }},
        options: {{
            skipHtmlTags: ['script', 'noscript', 'style', 'textarea', 'pre', 'code']
        }}
    }};
    </script>
    <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>

<style>
/* ==========================================================================
   MATHEMATICS THEME — Imperial Oxford Amethyst & Celestial Amber
   ========================================================================== */
:root {{
    --math-royal-primary: #7c3aed;
    --math-royal-hover: #6d28d9;
    --math-gold-accent: #f59e0b;
    --math-gold-glow: rgba(245, 158, 11, 0.25);
}}

body {{
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    font-size: 15px;
    line-height: 1.7;
    color: var(--text-body, #2d3748);
    margin: 0; padding: 0;
    background-color: var(--bg-body, #f4f6fb);
}}

.page-container {{
    max-width: 1080px;
    margin: 25px auto 50px;
    padding: 40px 50px;
    background-color: var(--bg-page, #ffffff);
    box-shadow: 0 4px 25px rgba(0, 0, 0, 0.07);
    border-radius: 14px;
}}

/* MATH HERO BANNER */
.math-banner {{
    background: linear-gradient(135deg, #1b0a2a 0%, #341253 45%, #581c87 75%, #b45309 100%);
    border-radius: 12px;
    padding: 30px 34px;
    margin-bottom: 28px;
    color: #ffffff;
    box-shadow: 0 6px 24px rgba(124, 58, 237, 0.25);
    position: relative;
    overflow: hidden;
}}
.math-banner::after {{
    content: "∑ ∫ ∏ √";
    position: absolute;
    right: 20px;
    bottom: -15px;
    font-size: 80px;
    font-weight: 800;
    font-family: 'Outfit', sans-serif;
    color: rgba(255, 255, 255, 0.05);
    pointer-events: none;
}}
.math-badge {{
    display: inline-flex;
    align-items: center;
    gap: 6px;
    background: rgba(255, 255, 255, 0.16);
    font-size: 12px;
    font-weight: 700;
    padding: 4px 14px;
    border-radius: 20px;
    text-transform: uppercase;
    letter-spacing: 1.2px;
    border: 1px solid rgba(255, 255, 255, 0.25);
    margin-bottom: 12px;
}}
.math-banner-title {{
    font-family: 'Outfit', sans-serif;
    font-size: 30px;
    font-weight: 800;
    line-height: 1.25;
    margin: 0;
    color: #ffffff;
}}

/* NAVIGATION TOGGLE */
.nav-toggle {{
    margin-bottom: 24px;
}}
.nav-toggle-btn {{
    width: 100%;
    background: var(--bg-subtle, #f8fafc);
    border: 1px solid var(--border-color, #e2e8f0);
    border-radius: 8px;
    padding: 10px 18px;
    font-size: 14px;
    font-weight: 700;
    color: #7c3aed;
    cursor: pointer;
    text-align: left;
    display: flex;
    justify-content: space-between;
    align-items: center;
    transition: all 0.2s ease;
}}
.nav-toggle-btn:hover {{
    background: rgba(124, 58, 237, 0.06);
    border-color: #7c3aed;
}}
.nav-panel {{
    display: none;
    margin-top: 10px;
    padding: 18px;
    background: var(--bg-subtle, #f8fafc);
    border: 1px solid var(--border-color, #e2e8f0);
    border-radius: 8px;
    column-count: 2;
    column-gap: 16px;
}}
.nav-panel.open {{ display: block; }}
.nav-item {{
    display: block;
    padding: 6px 10px;
    font-size: 13px;
    color: var(--text-body, #334155);
    text-decoration: none;
    border-radius: 4px;
    break-inside: avoid;
    margin-bottom: 4px;
    transition: all 0.15s ease;
}}
.nav-item:hover {{
    background: rgba(124, 58, 237, 0.1);
    color: #7c3aed;
}}
.nav-item.current {{
    background: linear-gradient(135deg, #7c3aed, #4c1d95);
    color: #ffffff !important;
    font-weight: 700;
}}

/* CONTENT STYLES — STRICT LEFT ALIGNMENT */
.module-content {{
    color: var(--text-body, #334155);
    font-size: 15px;
    text-align: left !important;
}}
.module-content h1, 
.module-content h2, 
.module-content h3, 
.module-content h4, 
.module-content p, 
.module-content ul, 
.module-content ol, 
.module-content li, 
.module-content table {{
    text-align: left !important;
}}

.module-content h1 {{
    font-family: 'Outfit', sans-serif;
    font-size: 24px;
    font-weight: 800;
    color: var(--text-heading, #0f172a);
    margin: 36px 0 16px;
    padding-bottom: 8px;
    border-bottom: 2px solid rgba(124, 58, 237, 0.2);
}}
.module-content h2 {{
    font-family: 'Outfit', sans-serif;
    font-size: 20px;
    font-weight: 700;
    color: var(--text-heading, #0f172a);
    margin: 30px 0 14px;
}}
.module-content h3 {{
    font-family: 'Outfit', sans-serif;
    font-size: 17px;
    font-weight: 700;
    color: var(--text-heading, #0f172a);
    margin: 24px 0 10px;
}}
.module-content p {{
    margin: 0 0 14px;
    line-height: 1.7;
    text-align: left !important;
}}
.module-content ul, .module-content ol {{
    margin: 12px 0 18px 28px !important;
    padding: 0 !important;
    text-align: left !important;
    list-style-position: outside !important;
}}
.module-content li {{
    margin-bottom: 8px !important;
    line-height: 1.65;
    text-align: left !important;
}}

/* MATHEMATICAL CALLOUTS */
.math-callout {{
    border-radius: 10px;
    padding: 16px 20px;
    margin: 22px 0 16px;
    border: 1px solid var(--border-color, #e2e8f0);
    background: var(--bg-surface, #ffffff);
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.03);
    text-align: left !important;
}}
[data-theme="dark"] .math-callout {{
    background: #141728;
    border-color: #242944;
}}
.callout-badge {{
    display: inline-block;
    font-size: 10.5px;
    font-weight: 800;
    letter-spacing: 0.8px;
    text-transform: uppercase;
    padding: 2px 8px;
    border-radius: 4px;
    margin-bottom: 8px;
}}
.callout-title {{
    font-weight: 700;
    font-size: 16px;
    color: var(--text-heading, #0f172a);
}}
.math-callout.theorem {{
    border-left: 4px solid #7c3aed;
}}
.math-callout.theorem .callout-badge {{
    background: rgba(124, 58, 237, 0.12);
    color: #7c3aed;
}}
.math-callout.definition {{
    border-left: 4px solid #2563eb;
}}
.math-callout.definition .callout-badge {{
    background: rgba(37, 99, 235, 0.12);
    color: #2563eb;
}}
.math-callout.property {{
    border-left: 4px solid #059669;
}}
.math-callout.property .callout-badge {{
    background: rgba(5, 150, 105, 0.12);
    color: #059669;
}}
.math-callout.example {{
    border-left: 4px solid #d97706;
}}
.math-callout.example .callout-badge {{
    background: rgba(217, 119, 6, 0.12);
    color: #d97706;
}}

/* EXAM BANNER */
.exam-header-banner {{
    background: linear-gradient(135deg, rgba(124, 58, 237, 0.1), rgba(245, 158, 11, 0.12));
    border-left: 4px solid #f59e0b;
    border-radius: 8px;
    padding: 14px 18px;
    margin: 28px 0 16px;
    font-weight: 800;
    font-size: 18px;
    color: #b45309;
    font-family: 'Outfit', sans-serif;
}}
[data-theme="dark"] .exam-header-banner {{
    color: #fbbf24;
    background: linear-gradient(135deg, rgba(124, 58, 237, 0.2), rgba(245, 158, 11, 0.15));
}}

/* MATH DIAGRAM BOX */
.math-diagram-box {{
    background: var(--bg-surface, #ffffff);
    border: 1px solid rgba(124, 58, 237, 0.22);
    border-radius: 12px;
    padding: 22px 24px;
    margin: 24px 0;
    box-shadow: 0 4px 18px rgba(124, 58, 237, 0.06);
}}
[data-theme="dark"] .math-diagram-box {{
    background: #111424;
    border-color: rgba(139, 92, 246, 0.3);
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.35);
}}
.math-diagram-title {{
    font-family: 'Outfit', sans-serif;
    font-size: 16px;
    font-weight: 800;
    color: #7c3aed;
    margin: 0 0 12px;
    text-align: center;
}}
[data-theme="dark"] .math-diagram-title {{
    color: #c084fc;
}}
.math-pill {{
    background: var(--bg-subtle, #f8fafc);
    border: 1px solid var(--border-color, #e2e8f0);
    border-radius: 8px;
    padding: 10px 14px;
    font-size: 13px;
    color: var(--text-heading);
}}
[data-theme="dark"] .math-pill {{
    background: #181d33;
    border-color: #2a3154;
}}
.math-card-caption {{
    text-align: center;
    color: var(--text-secondary);
    font-size: 12px;
    margin-top: 14px;
}}

/* MATH DISPLAY CONTAINERS */
.math-display {{
    overflow-x: auto;
    overflow-y: hidden;
    padding: 12px 0;
    margin: 14px 0;
    text-align: center;
}}
.math-inline {{
    white-space: nowrap;
}}

/* REFERENCE PILL */
.ref-pill {{
    display: inline-block;
    font-size: 11px;
    font-weight: 700;
    color: #7c3aed;
    background: rgba(124, 58, 237, 0.08);
    border: 1px solid rgba(124, 58, 237, 0.2);
    border-radius: 12px;
    padding: 2px 10px;
    margin: 4px 0;
}}

/* TABLES */
.module-content table {{
    width: 100%;
    border-collapse: collapse;
    margin: 20px 0;
    font-size: 13.5px;
}}
.module-content th {{
    background: var(--bg-subtle, #f8fafc);
    color: var(--text-heading);
    font-weight: 700;
    padding: 10px 12px;
    border: 1px solid var(--border-color, #e2e8f0);
    text-align: left;
}}
.module-content td {{
    padding: 10px 12px;
    border: 1px solid var(--border-color, #e2e8f0);
    color: var(--text-body);
}}

/* PREV / NEXT NAV BUTTONS */
.prev-next {{
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-top: 45px;
    padding-top: 25px;
    border-top: 2px solid var(--border-color, #e2e8f0);
    gap: 14px;
    flex-wrap: wrap;
}}
.pn-btn {{
    padding: 10px 20px;
    background: var(--bg-subtle, #f8fafc);
    border: 1px solid var(--border-color, #e2e8f0);
    border-radius: 8px;
    text-decoration: none;
    color: #7c3aed;
    font-weight: 700;
    font-size: 14px;
    transition: all 0.2s;
}}
.pn-btn:hover {{
    background: #7c3aed;
    color: #fff;
    border-color: #7c3aed;
}}
.pn-hub {{
    padding: 10px 18px;
    background: linear-gradient(135deg, #7c3aed, #4c1d95);
    color: #fff !important;
    border-radius: 8px;
    text-decoration: none;
    font-weight: 700;
    font-size: 13px;
}}

/* QUIZ STYLES */
.quiz-section-wrap {{
    margin: 45px 0 25px;
}}
.quiz-card-container {{
    background: var(--bg-surface, #ffffff);
    border: 1.5px solid rgba(124, 58, 237, 0.25);
    border-radius: 14px;
    padding: 32px 28px;
    box-shadow: 0 4px 20px rgba(124, 58, 237, 0.08);
}}
[data-theme="dark"] .quiz-card-container {{
    background: #111424;
    border-color: rgba(139, 92, 246, 0.3);
    box-shadow: 0 4px 25px rgba(0, 0, 0, 0.4);
}}
.quiz-header {{
    border-bottom: 2px solid rgba(124, 58, 237, 0.15);
    padding-bottom: 20px;
    margin-bottom: 28px;
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
    flex-wrap: wrap;
    gap: 16px;
}}
.quiz-badge {{
    display: inline-flex;
    align-items: center;
    gap: 6px;
    background: linear-gradient(135deg, rgba(124, 58, 237, 0.12), rgba(245, 158, 11, 0.15));
    color: #7c3aed;
    padding: 5px 14px;
    border-radius: 20px;
    font-size: 12px;
    font-weight: 800;
    letter-spacing: 0.8px;
    text-transform: uppercase;
    margin-bottom: 10px;
}}
.quiz-title {{
    font-family: 'Outfit', sans-serif;
    font-size: 22px;
    font-weight: 800;
    color: var(--text-heading);
    margin: 0 0 6px 0;
}}
.quiz-subtitle {{
    font-size: 13.5px;
    color: var(--text-secondary);
    margin: 0;
    max-width: 680px;
}}
.quiz-score-badge {{
    background: linear-gradient(135deg, #10b981, #059669);
    color: #ffffff;
    padding: 8px 18px;
    border-radius: 30px;
    font-family: 'Outfit', sans-serif;
    font-weight: 800;
    font-size: 16px;
    box-shadow: 0 4px 14px rgba(16, 185, 129, 0.3);
}}
.q-block {{
    background: var(--bg-subtle, #f8fafc);
    border: 1px solid var(--border-color, #e2e8f0);
    border-radius: 10px;
    padding: 18px 20px;
    margin-bottom: 20px;
    transition: all 0.2s ease;
}}
[data-theme="dark"] .q-block {{
    background: #181d33;
    border-color: #272f4e;
}}
.q-title {{
    font-weight: 700;
    font-size: 15px;
    color: var(--text-heading);
    margin-bottom: 14px;
    display: flex;
    gap: 10px;
    line-height: 1.5;
}}
.q-num {{
    color: #7c3aed;
    font-weight: 800;
    flex-shrink: 0;
}}
.q-options {{
    display: flex;
    flex-direction: column;
    gap: 8px;
}}
.q-opt {{
    display: flex;
    align-items: center;
    gap: 12px;
    background: var(--bg-surface, #ffffff);
    border: 1px solid var(--border-color, #e2e8f0);
    border-radius: 8px;
    padding: 10px 14px;
    font-size: 13.5px;
    cursor: pointer;
    color: var(--text-body);
    transition: all 0.15s ease;
}}
[data-theme="dark"] .q-opt {{
    background: #111424;
    border-color: #2a3154;
}}
.q-opt:hover {{
    border-color: #7c3aed;
    background: rgba(124, 58, 237, 0.04);
}}
.q-opt input[type="radio"] {{
    margin: 0;
    accent-color: #7c3aed;
}}
.q-opt.correct-choice {{
    background: rgba(16, 185, 129, 0.12) !important;
    border-color: #10b981 !important;
    color: #065f46 !important;
    font-weight: 600;
}}
[data-theme="dark"] .q-opt.correct-choice {{
    color: #34d399 !important;
}}
.q-opt.wrong-choice {{
    background: rgba(239, 68, 68, 0.12) !important;
    border-color: #ef4444 !important;
    color: #991b1b !important;
}}
[data-theme="dark"] .q-opt.wrong-choice {{
    color: #f87171 !important;
}}
.q-explanation {{
    display: none;
    margin-top: 12px;
    padding: 12px 14px;
    background: rgba(124, 58, 237, 0.06);
    border-left: 3px solid #7c3aed;
    border-radius: 6px;
    font-size: 13px;
    line-height: 1.6;
    color: var(--text-body);
}}
.quiz-actions {{
    display: flex;
    gap: 14px;
    margin-top: 24px;
    flex-wrap: wrap;
}}
.btn-quiz-check {{
    background: linear-gradient(135deg, #7c3aed, #5b21b6);
    color: #ffffff;
    border: none;
    border-radius: 8px;
    padding: 12px 26px;
    font-size: 14px;
    font-weight: 700;
    cursor: pointer;
    box-shadow: 0 4px 14px rgba(124, 58, 237, 0.3);
    transition: all 0.2s;
}}
.btn-quiz-check:hover {{
    background: linear-gradient(135deg, #6d28d9, #4c1d95);
    transform: translateY(-1px);
}}
.btn-quiz-reset {{
    background: var(--bg-subtle, #f8fafc);
    color: var(--text-secondary);
    border: 1px solid var(--border-color, #e2e8f0);
    border-radius: 8px;
    padding: 12px 20px;
    font-size: 14px;
    font-weight: 600;
    cursor: pointer;
    transition: all 0.2s;
}}
.btn-quiz-reset:hover {{
    background: var(--bg-card-hover);
    color: var(--text-heading);
}}

@media (max-width: 768px) {{
    .page-container {{ padding: 22px 18px; margin: 15px auto; }}
    .math-banner {{ padding: 22px 20px; }}
    .math-banner-title {{ font-size: 24px; }}
    .nav-panel {{ column-count: 1; }}
}}
</style>
</head>
<body>

{global_nav_html}

<div class="page-container">

    <!-- Math Banner Header -->
    <div class="math-banner">
        <div class="math-badge">📐 {unit_name} &bull; Module {mod_num} of 29</div>
        <h1 class="math-banner-title">{title}</h1>
        <div style="font-size: 13.5px; opacity: 0.9; margin-top: 6px;">Rigorous lecture notes, theorems, proofs, worked calculation steps &amp; self-grading quiz</div>
    </div>

    <!-- Collapsible Course Navigation Panel -->
    <div class="nav-toggle">
        <button type="button" class="nav-toggle-btn" onclick="toggleNavPanel()">
            <span>📚 Course Syllabus Navigator (Modules 01 &ndash; 29)</span>
            <span>▾ Toggle Menu</span>
        </button>
        <div id="navPanel" class="nav-panel">
            {nav_items_html}
        </div>
    </div>

    <!-- Core Module Academic Content -->
    <div class="module-content">
{body_html}
    </div>

    <!-- Prev / Next Footer Navigation -->
    <div class="prev-next">
        <a class="pn-btn" href="{prev_link}">{prev_label}</a>
        <a class="pn-hub" href="maths.html">📋 Mathematics Hub (29 Modules)</a>
        <a class="pn-btn" href="{next_link}">{next_label}</a>
    </div>

</div>

<script src="shared.js"></script>
<script>
function toggleNavPanel() {{
    var panel = document.getElementById('navPanel');
    if (panel) panel.classList.toggle('open');
}}

function checkMathQuiz(modNum, total) {{
    let score = 0;
    for (let i = 1; i <= total; i++) {{
        let block = document.getElementById("q_block_" + modNum + "_" + i);
        if (!block) continue;
        let corr = parseInt(block.getAttribute("data-corr"));
        let radios = document.getElementsByName("math_q_" + modNum + "_" + i);
        let selected = -1;
        for (let r of radios) {{
            if (r.checked) {{
                selected = parseInt(r.value);
                break;
            }}
        }}

        for (let j = 0; j < 4; j++) {{
            let optEl = document.getElementById("q_" + modNum + "_" + i + "_opt_" + j);
            if (optEl) {{
                optEl.classList.remove("correct-choice", "wrong-choice");
            }}
        }}

        if (selected === corr) {{
            score++;
            let correctEl = document.getElementById("q_" + modNum + "_" + i + "_opt_" + corr);
            if (correctEl) correctEl.classList.add("correct-choice");
        }} else {{
            if (selected !== -1) {{
                let wrongEl = document.getElementById("q_" + modNum + "_" + i + "_opt_" + selected);
                if (wrongEl) wrongEl.classList.add("wrong-choice");
            }}
            let correctEl = document.getElementById("q_" + modNum + "_" + i + "_opt_" + corr);
            if (correctEl) correctEl.classList.add("correct-choice");
        }}

        let expl = document.getElementById("q_expl_" + modNum + "_" + i);
        if (expl) expl.style.display = "block";
    }}

    let badge = document.getElementById("quizScoreBadge_" + modNum);
    let val = document.getElementById("quizScoreVal_" + modNum);
    let pct = document.getElementById("quizScorePct_" + modNum);
    if (badge && val && pct) {{
        val.innerText = score;
        pct.innerText = Math.round((score / total) * 100) + "%";
        badge.style.display = "inline-flex";
        badge.scrollIntoView({{ behavior: 'smooth', block: 'nearest' }});
    }}
}}

function resetMathQuiz(modNum, total) {{
    for (let i = 1; i <= total; i++) {{
        let radios = document.getElementsByName("math_q_" + modNum + "_" + i);
        for (let r of radios) r.checked = false;

        for (let j = 0; j < 4; j++) {{
            let optEl = document.getElementById("q_" + modNum + "_" + i + "_opt_" + j);
            if (optEl) optEl.classList.remove("correct-choice", "wrong-choice");
        }}

        let expl = document.getElementById("q_expl_" + modNum + "_" + i);
        if (expl) expl.style.display = "none";
    }}

    let badge = document.getElementById("quizScoreBadge_" + modNum);
    if (badge) badge.style.display = "none";
}}
</script>
</body>
</html>'''

    out_file = os.path.join(OUT_DIR, f"maths-module-{mod_num}.html")
    with open(out_file, 'w', encoding='utf-8') as f:
        f.write(full_page_html)
    print(f"✅ Generated {out_file} ({len(full_page_html):,} bytes)")

def build_all_18_to_29():
    print("=== BUILDING MATHEMATICS MODULES 18 TO 29 ===")
    for m in range(18, 30):
        generate_maths_module_page(m)
    print("🎉 All 12 new modules (18 to 29) built successfully!")

if __name__ == "__main__":
    build_all_18_to_29()
