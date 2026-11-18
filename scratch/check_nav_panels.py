import re

for i in range(1, 14):
    path = f'blockchain-module-{i}.html'
    with open(path, 'r', encoding='utf-8') as f:
        text = f.read()
    has_dropdown_13 = 'Blockchain (13)' in text
    has_nav_panel = 'id="bcNavPanel"' in text
    nav_panel_count = len(re.findall(r'href="blockchain-module-\d+\.html"', text[text.find('id="bcNavPanel"'):text.find('</div>', text.find('id="bcNavPanel"'))+500])) if has_nav_panel else 0
    print(f"Mod {i}: Dropdown(13)={has_dropdown_13}, nav_panel={has_nav_panel}, links_in_panel={nav_panel_count}")
