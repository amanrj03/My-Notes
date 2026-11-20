import markdown

tbl = """| Network | Magic value |
| --- | --- |
| Mainnet | 0xD9B4BEF9 |
"""

res1 = markdown.markdown(tbl, extensions=['tables'])
print("Without nl2br:")
print(res1)

res2 = markdown.markdown(tbl, extensions=['tables', 'nl2br'])
print("With nl2br:")
print(res2)
