import os, re

for i in range(14, 19):
    path = f'raw_notes/blockchain/{i}.txt'
    with open(path, 'r', encoding='utf-8') as f:
        text = f.read()
    print(f"\n==================== MODULE {i} ====================")
    # Match headers or topic lines
    topics = re.findall(r'^(?:#+\s*|\bTopic\s+\d+:|[A-F]\.\s+)(.+)$', text, re.MULTILINE)
    print(f"Total topics/headers: {len(topics)}")
    for t in topics[:15]:
        print("  -", t.strip().replace('*', ''))
