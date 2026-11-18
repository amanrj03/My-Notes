with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('Blockchain 13:')
if idx != -1:
    print(text[idx-50:idx+350])
