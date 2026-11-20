import markdown

content = open("raw_notes/blockchain/14.txt", encoding='utf-8').read()
idx = content.find("Acknowledges version")
# get 500 chars around it
snippet = content[idx-300:idx+400]

print("SNIPPET:")
print(repr(snippet))

html = markdown.markdown(snippet, extensions=['tables', 'fenced_code', 'nl2br'])
print("\nRENDERED HTML:")
print(html)
