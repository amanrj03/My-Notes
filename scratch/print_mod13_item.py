with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('blockchain-module-13.html')
if idx != -1:
    print(text[idx-60:idx+250])
