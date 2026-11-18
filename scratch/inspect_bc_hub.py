with open('blockchain.html', 'r', encoding='utf-8') as f:
    text = f.read()

print("File length:", len(text))
hero_idx = text.find('hub-hero')
print("Hero snippet:", text[hero_idx:hero_idx+600])

exam_idx = text.find('exam-banner')
print("Exam snippet:", text[exam_idx:exam_idx+600])

cards_idx = text.find('id="bcModulesGrid"')
print("Cards container found at:", cards_idx)
