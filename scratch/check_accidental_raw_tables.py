import glob
import re

for path in sorted(glob.glob("*.html")):
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # remove <script>, <style>, <table>, <pre>, <code>
    clean = re.sub(r'<script.*?</script>', '', content, flags=re.DOTALL)
    clean = re.sub(r'<style.*?</style>', '', clean, flags=re.DOTALL)
    clean = re.sub(r'<table.*?</table>', '', clean, flags=re.DOTALL)
    clean = re.sub(r'<pre.*?</pre>', '', clean, flags=re.DOTALL)
    clean = re.sub(r'<code.*?</code>', '', clean, flags=re.DOTALL)
    
    # Check for | --- in normal paragraph text
    m = re.findall(r'(\|[^\n<]+\|[^\n<]+\|\s*<br\s*/?>\s*\|[\s:-]+\|)', clean)
    if m:
        print(f"[ACCIDENTAL RAW TABLE IN PROSE] {path}: found {len(m)} tables!")
        for x in m:
            print(f"   {x[:100]}...")
