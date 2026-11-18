with open('blockchain.html', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.rfind('data-mod="13"')
print(text[idx:])
