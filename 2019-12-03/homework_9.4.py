name = input("Enter file:")
if len(name) < 1: name = "mbox-short.txt"
handle = open(name)
count = dict()
for line in handle:
    if not line.startswith("From "):
        continue
    line = line.split()
    line = line[1]
    count[line] = count.get(line, 0) + 1
new_count = None
new_word = None
for word, value in count.items():
    if new_count is None or value > new_count:
        new_count = value
        new_word = word
print(new_word, new_count)