import glob
import re

print("=== 1. SEARCHING FOR TABLE ARTIFACT KEYWORDS IN RAW NOTES & HTML ===")
keywords = ["blue row", "green row", "red row", "yellow row", "key alignment", "plaintext row", "ciphertext row"]

for ext, pattern in [("raw_notes", "raw_notes/**/*.txt"), ("html", "*.html")]:
    for path in sorted(glob.glob(pattern, recursive=True)):
        try:
            with open(path, 'r', encoding='utf-8') as f:
                content = f.read().lower()
            for kw in keywords:
                if kw in content:
                    print(f"[{ext}] {path}: found '{kw}'")
        except Exception as e:
            pass

print("\n=== 2. SEARCHING FOR UNPARSED MARKDOWN TABLES IN HTML FILES ===")
for path in sorted(glob.glob("*.html")):
    try:
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
        # look for pipe table lines like | --- | or | abc | def |
        pipe_lines = re.findall(r'(\|[ \t]*[-:]{2,}[ \t]*\|[ \t]*[-:]{2,})', content)
        if pipe_lines:
            print(f"[UNPARSED TABLE] {path}: found {len(pipe_lines)} unparsed markdown table dividers!")
    except:
        pass

print("\n=== 3. SEARCHING FOR MULTIPLE CONSECUTIVE SHORT HEADINGS/PARAGRAPHS IN ALL HTML ===")
for path in sorted(glob.glob("*.html")):
    try:
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
        # remove scripts & styles
        dom = re.sub(r'<script.*?</script>', '', content, flags=re.DOTALL)
        dom = re.sub(r'<style.*?</style>', '', dom, flags=re.DOTALL)
        
        # look for 4+ consecutive <p><strong>[1-2 chars]</strong></p>
        m = re.findall(r'(?:<p><strong>[A-Za-z0-9]</strong></p>\s*){4,}', dom)
        if m:
            print(f"[CONSECUTIVE SINGLE-CHAR PARAS] {path}: found {len(m)} matches!")
    except Exception as e:
        print(f"Error reading {path}: {e}")
