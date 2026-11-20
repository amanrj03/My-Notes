import re

content = open("blockchain-module-14.html", encoding='utf-8').read()
tables = re.findall(r'<table.*?</table>', content, flags=re.DOTALL)
print(f"Total table tags found in 14.html: {len(tables)}")

# Is "Acknowledges version" inside one of the tables?
for i, t in enumerate(tables):
    if "Acknowledges version" in t:
        print(f"Yes! 'Acknowledges version' IS inside table #{i}!")
        break
else:
    print("No, it was not inside a table!")
