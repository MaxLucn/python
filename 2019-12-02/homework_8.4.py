inp = input('Enter file name')
stuff = open(inp).read().split()
my_list = list()
for stu in stuff:
    if stu not in my_list:
        my_list.append(stu)

my_list.sort()
print(my_list)

