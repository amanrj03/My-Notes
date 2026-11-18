with open('blockchain-module-13.html', 'r', encoding='utf-8') as f:
    text = f.read()

banner_idx = text.find('class="module-banner"')
print("=== BANNER ===")
print(text[banner_idx:banner_idx+400])

nav_idx = text.find('id="bcNavPanel"')
print("=== NAV PANEL ===")
print(text[nav_idx:nav_idx+500])

prev_next_idx = text.find('class="prev-next"')
print("=== PREV NEXT ===")
print(text[prev_next_idx:prev_next_idx+400])
