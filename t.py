with open('translation_dataset2.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()

s = []
t = []

for line in lines:
    parts = line.split(':')
    if len(parts) == 2:
        s.append(parts[0])
        t.append(parts[1].strip())

with open('s.txt', 'w', encoding='utf-8') as s_file:
    for item in s:
        s_file.write("%s\n" % item)

with open('t.txt', 'w', encoding='utf-8') as t_file:
    for item in t:
        t_file.write("%s\n" % item)
