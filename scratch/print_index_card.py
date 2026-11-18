with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('Blockchain &amp; Cryptography</h3>')
if idx != -1:
    print(text[idx-200:idx+1500])
