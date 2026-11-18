import glob
import re

html_files = sorted(glob.glob("*.html"))

print(f"Auditing {len(html_files)} HTML files for stray backslashes and broken math...")

total_issues = 0
for f in html_files:
    with open(f, 'r', encoding='utf-8') as fp:
        html = fp.read()

    # Strip script blocks to inspect only rendered DOM
    dom_text = re.sub(r'<script.*?</script>', '', html, flags=re.DOTALL)

    issues = []

    # 1. Stray backslash tags
    stray_1 = re.findall(r'<p>\s*\\+\s*<', dom_text)
    stray_2 = re.findall(r'<p>\s*\\+\s*</p>', dom_text)
    if stray_1 or stray_2:
        issues.append(f"stray backslash paragraph: {len(stray_1) + len(stray_2)}")

    # 2. Escaped dollar sign at end of math ($$...\$$)
    escaped_closing_dollar = re.findall(r'[^\\]\\\$\$', dom_text)
    if escaped_closing_dollar:
        issues.append(f"broken escaped closing dollar (\\$$): {len(escaped_closing_dollar)}")

    # 3. Unreplaced tokens
    unresolved_tokens = re.findall(r'TOKEN_[A-Z0-9_]+', dom_text)
    if unresolved_tokens:
        issues.append(f"unresolved tokens: {len(unresolved_tokens)}")

    # 4. Nested ref-pill bug found earlier in some files
    nested_pills = re.findall(r'<span class="ref-pill">[^<]*<span class="ref-pill">', dom_text)
    if nested_pills:
        issues.append(f"nested ref-pills: {len(nested_pills)}")

    if issues:
        total_issues += 1
        print(f"❌ {f}: {', '.join(issues)}")

if total_issues == 0:
    print("✅ All HTML files are 100% clean!")
else:
    print(f"\nTotal files with issues: {total_issues}")
