import re

content = open("blockchain-module-14.html", encoding='utf-8').read()
no_code = re.sub(r'<pre.*?</pre>', '', content, flags=re.DOTALL)
no_code = re.sub(r'<code.*?</code>', '', no_code, flags=re.DOTALL)
no_code = re.sub(r'<table.*?</table>', '', no_code, flags=re.DOTALL)

pipes = re.findall(r'(\|[^\n<]+\|[^\n<]+\|\s*<br\s*/?>\s*\|[\s:-]+\|)', no_code)
print("Matches in 14:", len(pipes))
for p in pipes[:5]:
    print("MATCH:", p)
