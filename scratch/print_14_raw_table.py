lines = open("raw_notes/blockchain/14.txt", encoding='utf-8').readlines()
for i, l in enumerate(lines):
    if "Important messages" in l:
        print("".join(lines[i:i+35]))
        break
