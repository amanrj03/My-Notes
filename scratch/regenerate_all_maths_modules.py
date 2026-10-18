# -*- coding: utf-8 -*-
"""
Regenerates maths-module-1.html through maths-module-17.html with 100% visual integrity:
1. Replaces all \< and < with \lt in LaTeX
2. Replaces all \> and > with \gt in LaTeX
3. Replaces all raw text < and > with &lt; and &gt; to eliminate unclosed HTML tags
4. Protects array linebreaks like \\[2pt] inside LaTeX
5. Fixes \|a\| to |a| (norm to absolute value)
6. Adds defensive CSS to prevent any accidental text/heading/list centering
7. Formats tables with clean headers and left-aligned cells
8. Formats interactive quiz with sanitized questions and mathematical explanations
"""

import os
import re
import sys
import markdown

sys.path.append(r"C:\Users\Lenovo\.gemini\antigravity-ide\brain\95c33bf5-cdd6-4752-a936-5ac55e3df2fa\scratch")
from quiz_extractor import extract_module_quiz
from render_math_quiz import render_math_quiz_html

raw_dir = r"d:\Blockchain HTML\Django HTML\raw_notes\NumberTheory&Cryptography"
out_dir = r"d:\Blockchain HTML\Django HTML"

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
    17: "Mixed MCQ Mastery and Final Revision"
}

def get_nav_items_html(curr_mod):
    items = []
    for i in range(1, 18):
        t = MATH_TITLES[i]
        if i == curr_mod:
            items.append(f'<span class="nav-item current">{i}. {t}</span>')
        else:
            items.append(f'<a class="nav-item" href="maths-module-{i}.html">{i}. {t}</a>')
    return '\n'.join(items)

def get_global_nav_html(curr_mod):
    math_dropdown_items = []
    for i in range(1, 18):
        t = MATH_TITLES[i]
        math_dropdown_items.append(f'<a href="maths-module-{i}.html">Module {i}: {t}</a>')
    math_links_str = '\n'.join(math_dropdown_items)

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
                    <button class="nav-dropdown-btn active" style="color: #a78bfa;"><span class="icon">📐</span> Mathematics (17) ▾</button>
                    <div class="nav-dropdown-menu">
                        <a href="maths.html" class="nav-dropdown-header" style="background: linear-gradient(135deg, #7c3aed, #4c1d95); color: #fff;">📋 Mathematics Syllabus Hub</a>
                        {math_links_str}
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
                <a href="maths.html" class="nav-action-pill" style="background: linear-gradient(135deg, #7c3aed, #4c1d95);" title="Return to Mathematics Hub">📋 Maths Hub</a>
            </div>
        </div>
    </header>
    '''

def convert_txt_to_html_body(raw_text, mod_num):
    text = raw_text

    # Step 1: Extract quiz and insert placeholder
    bounds, questions = extract_module_quiz(mod_num)
    quiz_html = render_math_quiz_html(mod_num, questions)
    if bounds:
        start_idx, end_idx = bounds
        text = text[:start_idx] + "\n\nMATHQUIZTOKENXYZ\n\n" + text[end_idx:]
    else:
        text = text + "\n\nMATHQUIZTOKENXYZ\n\n"

    # Step 2: Clean textbook/slide citations
    text = re.sub(r'(?m)^\s*MTH381[A-Za-z0-9_\-\s]+\.pdf(?:\s*&#x20;)?\s*$', '', text)
    text = re.sub(r'([A-Za-z0-9_\-]+\s+U[0-9]+\s+TB\.pdf)', r'<span class="ref-pill">📚 Textbook Reference: \1</span>', text)
    text = re.sub(r'([A-Za-z0-9_\-]+\.pdf)', r'<span class="ref-pill">📚 Reference: \1</span>', text)
    text = text.replace('&#x20;', '')

    # Step 3: Protect array linebreaks like \\[2pt] inside LaTeX
    text = re.sub(r'\\\\\[(\d+pt)\]', r'ARRAYLINEBREAK\1END', text)

    # Step 4: Normalize LaTeX display and inline math delimiters
    text = text.replace(r'\\[' , r'\[').replace(r'\\]', r'\]')
    text = text.replace(r'\\(', r'\(').replace(r'\\)', r'\)')

    # Step 5: Extract and sanitize Display Math
    math_display = []
    def rep_disp(m):
        idx = len(math_display)
        c = m.group(1).strip()
        c = re.sub(r'ARRAYLINEBREAK(\d+pt)END', r'\\\\\\[\1\\]', c)
        c = c.replace(r'\_', '_').replace(r'\\%', r'\%')
        # Replace norm symbols \|a\| with |a|
        c = re.sub(r'\\\|([^|]+?)\\\|', r'|\1|', c)
        # Replace ALL \< and < with \lt
        c = c.replace(r'\<', r'\lt ').replace('<', r'\lt ')
        # Replace ALL \> and > with \gt
        c = c.replace(r'\>', r'\gt ').replace('>', r'\gt ')
        math_display.append(c)
        return f"\n\nMATHDISPTOKEN{idx}END\n\n"

    text = re.sub(r'\\\[(.*?)\\\]', rep_disp, text, flags=re.DOTALL)

    # Step 6: Extract and sanitize Inline Math
    math_inline = []
    def rep_inline(m):
        idx = len(math_inline)
        c = m.group(1).strip()
        c = c.replace(r'\_', '_').replace(r'\\%', r'\%')
        # Replace norm symbols \|a\| with |a|
        c = re.sub(r'\\\|([^|]+?)\\\|', r'|\1|', c)
        # Replace ALL \< and < with \lt
        c = c.replace(r'\<', r'\lt ').replace('<', r'\lt ')
        # Replace ALL \> and > with \gt
        c = c.replace(r'\>', r'\gt ').replace('>', r'\gt ')
        math_inline.append(c)
        return f"MATHINLTOKEN{idx}END"

    text = re.sub(r'\\\((.*?)\\\)', rep_inline, text)

    # Step 7: Outside of math, escape remaining raw < and > so browser won't parse them as HTML tags
    text = re.sub(r'\\<', '&lt;', text)
    text = re.sub(r'\\>', '&gt;', text)
    text = re.sub(r'<([a-zA-Z0-9_])', r'&lt;\1', text)
    text = re.sub(r'>([a-zA-Z0-9_])', r'&gt;\1', text)

    # Step 8: Strip initial module title heading
    text = re.sub(r'^#\s+Module\s+\d+[^#\n]+\n', '', text, flags=re.IGNORECASE)

    # Step 9: Markdown conversion without nl2br for clean paragraph flow
    html = markdown.markdown(text, extensions=['tables', 'fenced_code'])

    # Step 10: Restore MathJax display and inline
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

    # Step 11: Restore Quiz
    html = re.sub(r'<p>\s*MATHQUIZTOKENXYZ\s*</p>', lambda m: quiz_html, html)
    html = html.replace("MATHQUIZTOKENXYZ", quiz_html)

    # Step 12: Callout cards
    html = re.sub(r'<h3>(Theorem[^<]*)</h3>', r'<div class="math-callout theorem"><div class="callout-badge theorem">📐 THEOREM</div><div class="callout-title">\1</div></div>', html, flags=re.IGNORECASE)
    html = re.sub(r'<h3>(Definition[^<]*)</h3>', r'<div class="math-callout definition"><div class="callout-badge definition">📖 DEFINITION</div><div class="callout-title">\1</div></div>', html, flags=re.IGNORECASE)
    html = re.sub(r'<h3>(Property\s*\d+[^<]*)</h3>', r'<div class="math-callout property"><div class="callout-badge property">⚖️ PROPERTY</div><div class="callout-title">\1</div></div>', html, flags=re.IGNORECASE)
    html = re.sub(r'<h3>(Worked example[^<]*|Example\s*\d*[^<]*)</h3>', r'<div class="math-callout example"><div class="callout-badge example">💡 WORKED EXAMPLE</div><div class="callout-title">\1</div></div>', html, flags=re.IGNORECASE)
    html = re.sub(r'<h2>(Final revision sheet|Revision sheet|High-yield formula sheet)[^<]*</h2>', r'<div class="exam-header-banner">🎯 \1</div>', html, flags=re.IGNORECASE)

    return html

def generate_maths_module_page(mod_num):
    txt_path = os.path.join(raw_dir, f"{mod_num}.txt")
    if not os.path.exists(txt_path):
        print(f"Error: {txt_path} not found!")
        return

    with open(txt_path, "r", encoding="utf-8") as f:
        raw_text = f.read()

    body_content = convert_txt_to_html_body(raw_text, mod_num)
    nav_items = get_nav_items_html(mod_num)
    global_nav = get_global_nav_html(mod_num)

    prev_link = f"maths-module-{mod_num-1}.html" if mod_num > 1 else "maths.html"
    prev_label = f"&larr; Module {mod_num-1}" if mod_num > 1 else "&larr; Mathematics Hub"

    if mod_num < 17:
        next_link = f"maths-module-{mod_num+1}.html"
        next_label = f"Module {mod_num+1} &rarr;"
    else:
        next_link = "maths.html"
        next_label = "Syllabus Completed! &check;"

    title = MATH_TITLES[mod_num]

    html_template = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Module {mod_num}: {title} — Mathematics Study Guide</title>
    <meta name="description" content="Number Theory &amp; Cryptography study notes — Module {mod_num} of 17: {title}. Complete with theorems, proofs, worked examples, and interactive self-test quiz.">
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
    text-align: left !important;
}}
.math-callout.theorem {{
    border-left: 4px solid #7c3aed;
    background: rgba(124, 58, 237, 0.04);
}}
[data-theme="dark"] .math-callout.theorem {{ background: rgba(124, 58, 237, 0.1); }}
.callout-badge.theorem {{ background: #7c3aed; color: #fff; }}

.math-callout.definition {{
    border-left: 4px solid #0284c7;
    background: rgba(2, 132, 199, 0.04);
}}
[data-theme="dark"] .math-callout.definition {{ background: rgba(2, 132, 199, 0.1); }}
.callout-badge.definition {{ background: #0284c7; color: #fff; }}

.math-callout.property {{
    border-left: 4px solid #f59e0b;
    background: rgba(245, 158, 11, 0.04);
}}
[data-theme="dark"] .math-callout.property {{ background: rgba(245, 158, 11, 0.1); }}
.callout-badge.property {{ background: #f59e0b; color: #fff; }}

.math-callout.example {{
    border-left: 4px solid #10b981;
    background: rgba(16, 185, 129, 0.04);
}}
[data-theme="dark"] .math-callout.example {{ background: rgba(16, 185, 129, 0.1); }}
.callout-badge.example {{ background: #10b981; color: #fff; }}

/* DISPLAY MATH BOX — CLEAN AND PROPORTIONATE */
.math-display {{
    display: block;
    clear: both;
    width: 100%;
    box-sizing: border-box;
    overflow-x: auto;
    padding: 16px 20px;
    margin: 20px 0;
    text-align: center !important;
    background: rgba(124, 58, 237, 0.04);
    border: 1px dashed rgba(124, 58, 237, 0.3);
    border-radius: 10px;
}}
[data-theme="dark"] .math-display {{
    background: rgba(124, 58, 237, 0.1);
    border-color: rgba(167, 139, 250, 0.35);
}}
.math-inline {{
    display: inline-block;
    padding: 0 2px;
}}

/* REFERENCE PILL */
.ref-pill {{
    display: inline-block;
    background: rgba(124, 58, 237, 0.08);
    color: #7c3aed;
    font-size: 12px;
    font-weight: 600;
    padding: 3px 12px;
    border-radius: 12px;
    margin: 4px 0 14px;
    border: 1px solid rgba(124, 58, 237, 0.2);
}}
[data-theme="dark"] .ref-pill {{ color: #a78bfa; }}

/* REVISION SHEET BANNER */
.exam-header-banner {{
    background: linear-gradient(135deg, rgba(245, 158, 11, 0.12) 0%, rgba(245, 158, 11, 0.22) 100%);
    border-left: 4px solid #f59e0b;
    padding: 14px 20px;
    border-radius: 0 8px 8px 0;
    font-weight: 700;
    font-size: 18px;
    color: var(--text-heading, #0f172a);
    margin: 34px 0 18px;
    text-align: left !important;
}}

/* TABLES */
table {{
    width: 100%;
    border-collapse: collapse;
    margin: 24px 0;
    font-size: 14px;
    text-align: left !important;
}}
th, td {{
    border: 1px solid var(--border-color, #cbd5e0);
    padding: 11px 16px;
    text-align: left !important;
    vertical-align: middle;
}}
th {{
    background: linear-gradient(135deg, #7c3aed, #5b21b6);
    color: #ffffff;
    font-weight: 700;
}}
tr:nth-child(even) td {{
    background: var(--bg-table-stripe, #f8fafc);
}}

/* BOTTOM NAVIGATION */
.prev-next {{
    display: flex;
    justify-content: space-between;
    align-items: center;
    gap: 12px;
    margin-top: 45px;
    padding-top: 24px;
    border-top: 2px solid var(--border-color, #e2e8f0);
}}
.pn-btn {{
    display: inline-flex;
    align-items: center;
    gap: 8px;
    padding: 12px 22px;
    background: var(--bg-subtle, #f8fafc);
    border: 1px solid var(--border-color, #cbd5e0);
    border-radius: 8px;
    color: #7c3aed;
    font-size: 14px;
    font-weight: 700;
    text-decoration: none;
    transition: all 0.2s ease;
}}
.pn-btn:hover {{
    border-color: #7c3aed;
    background: rgba(124, 58, 237, 0.08);
    transform: translateY(-1px);
}}
.pn-hub {{
    display: inline-flex;
    align-items: center;
    gap: 6px;
    padding: 10px 18px;
    background: #1e112a;
    color: #fff;
    border-radius: 8px;
    text-decoration: none;
    font-size: 13px;
    font-weight: 700;
}}
.pn-hub:hover {{ background: #3b1d54; }}

@media (max-width: 768px) {{
    .page-container {{ margin: 12px; padding: 22px 18px; }}
    .prev-next {{ flex-direction: column; align-items: stretch; }}
    .pn-btn {{ justify-content: center; }}
    .nav-panel {{ column-count: 1; }}
}}
</style>

<style>
/* Mathematics Quiz Theme — Imperial Amethyst & Celestial Amber */
.quiz-section-wrap {{
    margin: 40px 0;
    padding: 0;
    text-align: left !important;
}}
.quiz-card-container {{
    background: var(--bg-surface, #ffffff);
    border: 1px solid rgba(124, 58, 237, 0.25);
    border-radius: 14px;
    padding: 32px 28px;
    box-shadow: 0 4px 20px rgba(124, 58, 237, 0.08);
    text-align: left !important;
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
    border: 1px solid rgba(124, 58, 237, 0.3);
    font-size: 11px;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 1px;
    padding: 4px 12px;
    border-radius: 20px;
    margin-bottom: 8px;
}}
[data-theme="dark"] .quiz-badge {{
    color: #a78bfa;
}}
.quiz-title {{
    font-family: 'Outfit', sans-serif;
    font-size: 24px;
    font-weight: 800;
    color: var(--text-heading, #0f172a);
    margin: 0 0 6px;
}}
.quiz-desc {{
    font-size: 14px;
    color: var(--text-secondary, #64748b);
    margin: 0;
}}
.quiz-score-badge {{
    background: linear-gradient(135deg, #7c3aed, #4c1d95);
    color: #ffffff;
    padding: 10px 18px;
    border-radius: 10px;
    font-size: 14px;
    font-weight: 700;
    display: none;
    box-shadow: 0 4px 12px rgba(124, 58, 237, 0.3);
}}
.q-block {{
    background: var(--bg-subtle, #f8fafc);
    border: 1px solid var(--border-color, #e2e8f0);
    border-radius: 10px;
    padding: 20px 22px;
    margin-bottom: 20px;
    transition: all 0.2s ease;
    text-align: left !important;
}}
.q-block:hover {{
    border-color: rgba(124, 58, 237, 0.4);
}}
.q-title {{
    font-weight: 700;
    font-size: 15.5px;
    color: var(--text-heading, #0f172a);
    margin-bottom: 14px;
    display: flex;
    gap: 10px;
    align-items: baseline;
    text-align: left !important;
}}
.q-num {{
    color: #7c3aed;
    font-family: 'JetBrains Mono', monospace;
    font-weight: 800;
}}
.q-options {{
    display: flex;
    flex-direction: column;
    gap: 10px;
}}
.q-opt {{
    display: flex;
    align-items: center;
    gap: 12px;
    padding: 12px 16px;
    background: var(--bg-surface, #ffffff);
    border: 1px solid var(--border-color, #e2e8f0);
    border-radius: 8px;
    cursor: pointer;
    font-size: 14.5px;
    color: var(--text-body, #334155);
    transition: all 0.15s ease;
    text-align: left !important;
}}
[data-theme="dark"] .q-opt {{
    background: #181c30;
    border-color: #242944;
}}
.q-opt:hover {{
    border-color: #7c3aed;
    background: rgba(124, 58, 237, 0.04);
}}
.q-opt input[type="radio"] {{
    accent-color: #7c3aed;
    width: 17px;
    height: 17px;
    margin: 0;
    cursor: pointer;
}}
.q-opt.correct-choice {{
    background: rgba(16, 185, 129, 0.1) !important;
    border-color: #10b981 !important;
    color: #065f46 !important;
    font-weight: 600;
}}
[data-theme="dark"] .q-opt.correct-choice {{
    color: #34d399 !important;
    background: rgba(16, 185, 129, 0.18) !important;
}}
.q-opt.wrong-choice {{
    background: rgba(239, 68, 68, 0.08) !important;
    border-color: #ef4444 !important;
    color: #991b1b !important;
}}
[data-theme="dark"] .q-opt.wrong-choice {{
    color: #f87171 !important;
    background: rgba(239, 68, 68, 0.15) !important;
}}
.q-explanation {{
    display: none;
    margin-top: 14px;
    padding: 12px 16px;
    border-radius: 8px;
    font-size: 13.5px;
    line-height: 1.5;
    background: rgba(124, 58, 237, 0.08);
    border-left: 4px solid #7c3aed;
    color: var(--text-body, #334155);
    text-align: left !important;
}}
[data-theme="dark"] .q-explanation {{
    background: rgba(124, 58, 237, 0.15);
    color: #e2e8f0;
}}
.quiz-actions {{
    display: flex;
    gap: 14px;
    margin-top: 26px;
    flex-wrap: wrap;
}}
.btn-quiz-check {{
    background: linear-gradient(135deg, #7c3aed 0%, #4c1d95 100%);
    color: #ffffff;
    border: none;
    border-radius: 8px;
    padding: 12px 26px;
    font-size: 15px;
    font-weight: 700;
    cursor: pointer;
    box-shadow: 0 4px 15px rgba(124, 58, 237, 0.3);
    transition: transform 0.2s, box-shadow 0.2s;
}}
.btn-quiz-check:hover {{
    transform: translateY(-2px);
    box-shadow: 0 6px 20px rgba(124, 58, 237, 0.4);
}}
.btn-quiz-reset {{
    background: var(--bg-subtle, #f8fafc);
    color: var(--text-secondary, #64748b);
    border: 1px solid var(--border-color, #e2e8f0);
    border-radius: 8px;
    padding: 12px 22px;
    font-size: 15px;
    font-weight: 600;
    cursor: pointer;
    transition: all 0.2s ease;
}}
.btn-quiz-reset:hover {{
    color: var(--text-heading, #0f172a);
    border-color: #7c3aed;
}}
</style>

</head>
<body>

{global_nav}

<div class="page-container">

    <div class="math-banner">
        <div class="math-badge">∑ Module {mod_num} of 17 — Number Theory &amp; Cryptography</div>
        <h1 class="math-banner-title">{title}</h1>
    </div>

    <div class="nav-toggle">
        <button class="nav-toggle-btn" onclick="toggleNavPanel()">
            <span>📚 All 17 Mathematics Modules ▾</span>
            <span style="font-size: 12px; opacity: 0.8;">Jump to Module</span>
        </button>
        <div class="nav-panel" id="navPanel">
            {nav_items}
        </div>
    </div>

    <div class="module-content">
        {body_content}
    </div>

    <div class="prev-next">
        <a class="pn-btn" href="{prev_link}">{prev_label}</a>
        <a class="pn-hub" href="maths.html">📋 Mathematics Hub</a>
        <a class="pn-btn" href="{next_link}">{next_label}</a>
    </div>

</div>

<script src="shared.js"></script>
<script>
function toggleNavPanel() {{
    var panel = document.getElementById('navPanel');
    if (panel) panel.classList.toggle('open');
}}
</script>
</body>
</html>
'''

    out_file = os.path.join(out_dir, f"maths-module-{mod_num}.html")
    with open(out_file, "w", encoding="utf-8") as f:
        f.write(html_template)
    print(f"Generated {out_file} ({len(html_template)/1024:.1f} KB)")

if __name__ == "__main__":
    for i in range(1, 18):
        generate_maths_module_page(i)
    print("All 17 Mathematics Modules successfully regenerated!")
