import os
import re

raw_path = "raw_notes/blockchain/14.txt"
with open(raw_path, 'r', encoding='utf-8') as f:
    text = f.read()

# Let's see what happens step by step:
idx = text.find("6.13 Important messages")
print("1. In raw text:")
print(repr(text[idx:idx+250]))

# Step 1: PPT/PDF regex
text_cleaned = re.sub(r'([A-Za-z0-9_\-\s]+\.pptx)', r'<span class="ref-pill">📄 Slides Reference: \1</span>', text)
text_cleaned = re.sub(r'([A-Za-z0-9_\-\s]+\.pdf)', r'<span class="ref-pill">📚 Textbook Reference: \1</span>', text_cleaned)
idx2 = text_cleaned.find("6.13 Important messages")
print("\n2. After PPT/PDF regex:")
print(repr(text_cleaned[idx2:idx2+250]))
