with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re

# Find sc-bc
sc_idx = text.find('subject-card sc-bc')
print("sc-bc card found at:", sc_idx)
print(text[sc_idx:sc_idx+900])
