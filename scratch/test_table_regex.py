import re

test = "Some text\n| a | b |\n| c | d |\n"
res = re.sub(r'([^\n|])\n(\|[^\n]+\|)', r'\1\n\n\2', test)
print(repr(res))
