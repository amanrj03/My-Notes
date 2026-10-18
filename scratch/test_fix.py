import os
import re
import sys
import markdown

sys.path.append(r"C:\Users\Lenovo\.gemini\antigravity-ide\brain\95c33bf5-cdd6-4752-a936-5ac55e3df2fa\scratch")
from quiz_extractor import extract_module_quiz
from render_math_quiz import render_math_quiz_html

def clean_and_convert_module(mod_num):
    raw_path = f"raw_notes/NumberTheory&Cryptography/{mod_num}.txt"
    with open(raw_path, "r", encoding="utf-8") as f:
        text = f.read()

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
    # First, handle display math \[ ... \]
    # Replace \\\[ with \[ and \\\] with \]
    text = text.replace(r'\\[' , r'\[').replace(r'\\]', r'\]')
    text = text.replace(r'\\(', r'\(').replace(r'\\)', r'\)')

    # Step 5: Extract and sanitize Display Math
    math_display = []
    def rep_disp(m):
        idx = len(math_display)
        c = m.group(1).strip()
        # Restore array line break
        c = re.sub(r'ARRAYLINEBREAK(\d+pt)END', r'\\\\\\[\1\\]', c)
        c = c.replace(r'\_', '_').replace(r'\\%', r'\%')
        # Fix \|a\| to |a| (norm to absolute value)
        c = re.sub(r'\\\|([^|]+?)\\\|', r'|\1|', c)
        # Fix all \< and < to \lt
        c = re.sub(r'\\<', r'\\lt ', c)
        c = re.sub(r'<', r'\\lt ', c)
        # Fix all \> and > to \gt
        c = re.sub(r'\\>', r'\\gt ', c)
        c = re.sub(r'>', r'\\gt ', c)
        # Ensure clean spacing
        math_display.append(c)
        return f"\n\nMATHDISPTOKEN{idx}END\n\n"

    text = re.sub(r'\\\[(.*?)\\\]', rep_disp, text, flags=re.DOTALL)

    # Step 6: Extract and sanitize Inline Math
    math_inline = []
    def rep_inline(m):
        idx = len(math_inline)
        c = m.group(1).strip()
        c = c.replace(r'\_', '_').replace(r'\\%', r'\%')
        # Fix \|a\| to |a|
        c = re.sub(r'\\\|([^|]+?)\\\|', r'|\1|', c)
        # Fix all \< and < to \lt
        c = re.sub(r'\\<', r'\\lt ', c)
        c = re.sub(r'<', r'\\lt ', c)
        # Fix all \> and > to \gt
        c = re.sub(r'\\>', r'\\gt ', c)
        c = re.sub(r'>', r'\\gt ', c)
        math_inline.append(c)
        return f"MATHINLTOKEN{idx}END"

    text = re.sub(r'\\\((.*?)\\\)', rep_inline, text)

    # Step 7: Outside of math, escape remaining raw < and > so browser won't parse them as HTML tags
    # Don't touch HTML tags we already have (like <span class="ref-pill">)
    # Replace lone < not part of a tag
    text = re.sub(r'<(?![a-zA-Z/])', '&lt;', text)
    # Also in text, convert `\<` to `&lt;`
    text = text.replace(r'\<', '&lt;')
    text = text.replace(r'\>', '&gt;')
    # Replace remaining raw < followed by letter if it's like < d or <d in plain text
    text = re.sub(r'<([a-zA-Z0-9_])', r'&lt;\1', text)

    # Step 8: Strip initial module title heading
    text = re.sub(r'^#\s+Module\s+\d+[^#\n]+\n', '', text, flags=re.IGNORECASE)

    # Step 9: Markdown conversion
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

# Test on Module 1
test_html = clean_and_convert_module(1)
print(f"Generated Module 1: {len(test_html)} chars")
# Check if any '<d' or invalid tag exists
invalid_tags = re.findall(r'<([a-zA-Z0-9_]+)', test_html)
valid = {'html', 'head', 'meta', 'title', 'link', 'script', 'style', 'body', 'header', 'div', 'a', 'span', 'button', 'p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'ul', 'ol', 'li', 'table', 'thead', 'tbody', 'tr', 'th', 'td', 'input', 'label', 'strong', 'em', 'br', 'hr', 'code', 'pre', 'b', 'i', 'u', 'details', 'summary', 'footer'}
bad = [t for t in invalid_tags if t.lower() not in valid]
print("Invalid HTML tags in Module 1:", bad)

# Check Section 3.1 formula specifically
m = re.search(r'boxed\{a=dq\+r.*', test_html)
if m:
    print("Section 3.1 formula:", m.group(0)[:80])

# Check Revision sheet table specifically
m_table = re.search(r'Division Algorithm.*?</td>\s*<td>(.*?)</td>', test_html, re.DOTALL)
if m_table:
    print("Table Division Algorithm row:", m_table.group(1).strip()[:100])
