with open("raw_notes/blockchain/14.txt", encoding='utf-8') as f:
    text = f.read()

idx = text.find("6.13 Important messages")
print(text[idx-200:idx+600])
