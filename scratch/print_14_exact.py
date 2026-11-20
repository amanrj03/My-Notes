content = open("blockchain-module-14.html", encoding='utf-8').read()
idx = content.find("Acknowledges version")
print(content[idx-250:idx+350])
