# 字典是另一种可变容器模型，且可存储任意类型对象。
# 字典的每个键值 key=>value 对用冒号 : 分割，每个键值对之间用逗号 , 分割，整个字典包括在花括号 {} 中
# 集合的基本定义是单个变量中包含多个对象，以及建立索引，查找和在单个变量中操作事物。
# 列表是一个非常有序的集合，在列表里面，位置是关键
# 在字典中，不能只放进去一些东西，必须给他一个值或者一个标签，下次打开的时候只需要这个值、标签就可以知道字典里有什么。
# 值可以取任何数据类型，但键必须是不可变的，如字符串，数字或元组。
# 字典（它们）是基于内存的键值存储
# my_dic = dict()
# my_dic['age'] = 32
# my_dic['name'] = 'Tom'
# print(my_dic)

# ccc = {}
# ccc['abc'] = 1
# ccc['nmn'] = 1
# print(ccc)
# ccc['abc'] = ccc['abc'] + 1
# print(ccc)

# count = dict()
# names = ['Tom', 'Jerry', 'Bob', 'Ricardo', 'Henry', 'Kim', 'Tom', 'kim']
# for name in names:
#     if name not in count:
#         count[name] = 1
#     else:
#         count[name] = count[name] + 1
# print(count)

# git 方法只适用于字典里面，它的作用是：查询字典里有没有某一个值所以上面这个代码可以简化成下面这样
# count = dict()
# names = ['Tom', 'Jerry', 'Bob', 'Ricardo', 'Henry', 'Kim', 'Tom', 'kim']
# for name in names:
#     count[name] = count.get(name, 0) + 1
# print(count)

# count = dict()
# line = input('Enter a line of text:')
# words = line.split()
#
# print('words', words)
# print('Counting...')
#
# for word in words:
#     count[word] = count.get(word, 0) + 1
#
# print('count', count)

# 编写程序以通读mbox-short.txt并找出谁发送了最多的邮件。
# 该程序将查找“发件人”行，并将这些行的第二个单词作为发送邮件的人。
# 该程序创建一个Python字典，该字典将发件人的邮件地址映射到它们出现在文件中的次数计数。
# 生成字典后，程序将使用最大循环遍历字典以查找最多产的提交者。
name = input('Enter file name:')
if len(name) < 1: name = 'mbos-short.txt'
names = open(name)
count = dict()
for line in names:
    line = line.rstrip()
    if not line.startswith('From'):
        continue
    line = line.split()
    line = line[1]
    count[line] = count.get(line, 0) + 1
largest = None
new_words = None
for words, count in count.items():
    if largest == None or count > largest:
        largest = count
        new_words = words
print(new_words, largest)
