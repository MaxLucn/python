# 一、这是练习len()函数的
# poj = [1, 2, 3, [7, 8, 9], 0, 4]
# print(len(poj))  # len()函数可以知道列表里有多少的元素
# for i in poj:
#
#     poj[3] = 7
#     print(i)

# 二、这是练习range()函数的
# friends = ['Bob', 'Tom', 'Jerry']
# # for friend in friends:
# #    print('happy new year', friend)
# for i in range(len(friends)):  #  range() 函数会把当前列表改变成一个整数列表，一般用在 for 循环中
#     friend = friends[i]
#     print('Happy new year:', friend)

# 三、这是练习查找方法的
# x = ['Bob', 'Tom', 'Jerry', 'Henry', 'Ricardo', 'Kim']
# y = x[1:3]
# z = x[:4]
# t = x[5:]
# a = x[:]  # 这个方法可以查找列表里具体某个位置的元素
# print(y)
# print(z)
# print(t)
# print(a)

# 四、这是练习append()函数的
# stuff = list()
# stuff.append('Tom')
# stuff.append('Jerry')  # 这是建一个空列表，然后用append()函数往空列表里加任何自己想加进去的元素
# print(stuff)
# stuff.append('Ricardo')
# print(stuff)
# if 'Tom' in stuff:
#     print(True)
# if 'she' in stuff:
#     print(True)
# else:
#     print(False)

# 五、这是练习sort()函数的
# x = ['Bob', 'Tom', 'Jerry', 'Henry', 'Ricardo', 'Kim']
# x.sort()  # 把列表里的元素进行排序，sort的意思是分类  ，sort()函数重新排序列表实际上是改变了列表
# print(x)

# 六、这是练习求最大值之类的
# nums = [1, 2, 3, 4, 5, 6, 7, 8]
# print(max(nums))
# print(min(nums))
# print(sum(nums))
# print(sum(nums)/len(nums))  # 查找列表里元素的最大值，最小值，和，平均值

# 七、这是用以前的方法跟有列表方法之后求平均数的对比
# total = 0
# count = 0
# while True:
#     inp = input('Enter a number:')
#     if inp == 'done':
#         break
#     value = float(inp)
#     total += value
#     count += 1
#
# average = total/count
# print('average', average) # 这是用以前的方法

# num = list()
# while True:
#     inp = input('Enter a number:')
#     if inp == 'done':
#         break
#     value = float(inp)
#     num.append(value)
#
# average = sum(num)/len(num)
# print(average)  # 这是用了关于列表的方法

# 八、split()函数是一种拆分字符串的内置函数，使用split函数的时候不必使用空格
# x = 'This is my exercise'
# stuff = x.split()
# print(stuff)

inp = input('Enter file name')
# inp = 'mbox-short.txt'
file = open(inp)
count = 0
words = list()
for line in file:
    if line.startswith('From'):
        line = line.rstrip().split()
        if line[1] not in words:
            words.append(line[1])
            count += 1
            print(line[1])
print("There were", count, "lines in the file with From as the first word")



