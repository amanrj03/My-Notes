import re

test_text = """| Message | Purpose |
| --- | --- |
| version | Introduces a node |

Mastering_Blockchain_Third_Edition.pdf"""

# Check what the regex does
m = re.search(r'([A-Za-z0-9_\-\s]+\.pdf)', test_text)
if m:
    print("MATCHED:")
    print(repr(m.group(0)))
