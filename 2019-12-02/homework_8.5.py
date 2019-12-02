inp = input('Enter file name')
file = open(inp)
count = 0
words = list()
for line in file:
    line = line.rstrip()
    words = line.split()
    if len(words) < 3 or words[0] != 'From':
        continue
    count += 1
    print(words[1])
print("There were", count, "lines in the file with From as the first word")
