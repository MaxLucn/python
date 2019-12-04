
name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
counts = dict()

for line in handle:
    line = line.rstrip()
    if not line.startswith('From '):
        continue
    words = line.split()
    words = words[5]
    words = words.split(":")
    words = words[0]

    counts[words] = counts.get(words, 0) + 1
tmp = list()
for key, value in counts.items():
    newt = (key, value)
    tmp.append(newt)
tmp = sorted(tmp)
for key, value in tmp:
    print(key, value)
