with open('blockchain.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
cards = re.findall(r'<div class="bc-card" data-mod="(\d+)">', text)
print("Modules present in blockchain.html:", cards)

end_grid = text.find('</div>', text.find('id="bcModulesGrid"'))
print("Next 500 chars after cards end:")
last_card = text.rfind('<div class="bc-card"')
print(text[last_card:last_card+600])
