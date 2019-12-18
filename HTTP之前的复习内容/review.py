
# 复习内容  一、
# hours = input('Enter Hours:')
# rate = input('Enter Rate:')
# pay = float(hours) * float(rate)                 # 把字符串转化成浮点数类型求积
# print(pay)

# 二、判断
# x = 19
# if x < 2:
#     print('small')
# elif x < 10:
#     print('smaller')
# else:
#     print('largest')
# print('done')

# 三、try、except方法捕可能出现的错误
# my_str = 'Bob'
# try:
#     print(my_str)
#     my_str = int(my_str)
#     print(my_str)
# except:
#     print(-1)
#
# print('done')

# 四、
# hour = input('Enter a hour:')
# rate = input('Enter a rate:')
# hour = float(hour)
# rate = float(rate)
# if hour > 40:
#     pay = (hour - 40) * (rate * 0.5) + hour * rate
# else:
#      pay = hour * rate
#
# print(pay)

# 五、
# x = 5
# while x > 0:
#     x = x - 1
# print(x)

# 六、
# # largest = -1                                   # 如果把largest赋值为None，在后面怎么样才能把None类型转换成为int类型与large进行比较?
# # for large in [7, 34, 523, 54, 2, 52, 5347]:
# #     largest = str(largest)
# #     if large > largest:
# #         largest = large
# #
# # print(largest)
#
# largest = None
# small = None
# for lar in [7, 34, 523, 54, 2, 52, 5347]:
#     if largest is None and small is None:        # 这个是对上面疑问的回答，在这酷爱代码里还查找了列表里的最小值
#         largest = lar
#         small = lar
#     elif lar > largest:
#         largest = lar
#     elif lar < small:
#         small = lar
#
# print(largest, small)

# 七、
# word = 'banana'
# total = 0
# for letter in word:
#     if letter == 'a':
#         total = total + 1
#
# print(total, letter)

# 八、
# word = '    Hello  World   '
# words = word.upper()                   # 把字符串中所有小写的值变成大些返回
# print(words)
# letter = word.lower()                  # 把字符串中所有大写的值变成小写返回
# print(letter)
# left = word.lstrip()                   # 去掉字符串中左侧的空格
# print(left)
# right = word.rstrip()                  # 去掉字符串右侧的空格
# print(right)
# air = word.strip()                     # 去掉字符串中两侧的空格
# print(air)
# line = word.replace('World', 'Tom')    # replace方法，替换字符串中的某一个值
# print(line)
# line = word.startswith('    Hello')    # startswith方法查找字符串中是否存在某个值，返回值是一个布尔值
# print(line)
# line = word.find('W')                    # 在字符串中查找一个特定的值的位置，这里需要注意的是字符串的位置都是从0开始数起的
# print(line)
# host = word[line + 1]          # 这个是跟上面方法配合使用的，当要查找某个忘记是什么值但是记得它旁边的值的时候就可以用这样的方法来查找到
# print(host)

# 九、
# counts = dict()
# names = ['BOb', 'Tom', 'Jerry', 'Ricard', 'Kim']
# for name in names:
#     if name not in counts:
#         counts[name] = 1
#     else:
#         counts[name] = counts[name] + 1
# print(counts)                                           # 这是一个计算一个列表中某个元算出现多少次的字典
#
# counts = dict()
# names = ['BOb', 'Tom', 'Jerry', 'Ricard', 'Kim']
# for name in names:
#     counts[name] = counts.get(name, 0) + 1
# print(counts)                                           # 运用字典里的get方法，可以更简单的实现上面的代码

# 十、
# my_dic = {'Bob': 2, 'Tom': 21, 'Jerry': 3, 'Kim': 9}
# print(list(my_dic))                                     # 把字典转化成列表
# print(my_dic.keys())                                    # 找出列表里的键值
# print(my_dic.values())                                  # 找出列表里的数值
# print(my_dic.items())                                   # Python 字典 items() 方法以列表返回可遍历的(键, 值) 元组数组。

# my_dic = {'Bob': 2, 'Tom': 21, 'Jerry': 3, 'Kim': 9}
# for keys, values in my_dic.items():
#     print(keys, values)                                   # Python 字典 items() 方法以列表返回可遍历的(键, 值) 元组数组


# 十一、
# 打开一个文件，把它转化成一个列表，然后计算这个文件中每个词出现的次数，再找出出现次数最多的词，并且计算出现了多少次
# name = input('Enter name:')                       # 输入一个文件
# hand = open(name)                                 # 打开文件
#
# my_dic = dict()                                   # 新建一个字典
# for line in hand:                                 # 新建循环，如果line在这个文件中
#     line = line.rstrip()                          # 把每一行后面多余的空行去掉
#     words = line.split()                          # 把文件转化成一个列表
#     for word in words:                            # 建立循环， 如果这个词在列表中
#         my_dic[word] = my_dic.get(word, 0) + 1    # 在列表中出现的每一个词的计数
# 找出现次数最多的词，并且出现了多少次
# largest = -1                                      # 设定最大初始值
# the_word = None                                   # 设定出现最多次数的词为空
# for keys, values in my_dic.items():               # 字典的items()方法的使用
#     if values > largest:                          # 判断，如果值大于初识最大值的话
#         largest = values                          # 上面的判断成立的话，把当前值赋值到初识最大值
#         the_word = keys                           # 上面判断成立的话，把出现最多次数的词赋值到空值
#
# print(the_word, largest)                          # 输出在这个文件中出现最多次数的词，以及出现的次数

# 十二、
# a = {'Bob': 2, 'Tom': 34, 'Jerry': 21, 'Kim': 7}   # 新建一个字典
# my_list = list()                                   # 新建一个空的列表
# for keys, values in a.items():                     # 建立循环，遍历字典里每个对应的key，value
#     print(keys, values)                            # 输出字典中每一对的key，value
#     my_list.append((values, keys))                 # 把循环找出来的每一个key，value添加进这个空的列表
# print(my_list)                                     # 输出这个列表
#
# my_list = sorted(my_list, reverse=True)            # 把列表反转并排序，sorted排序函数，reverse反转函数
# print(my_list)                                     # 输出最终需要的列表


# 十三、
# import socket                                       # HTTP套接字
# my_sock = socket.socke(socket.AF_INET, socket.SOCK_STREAM)
# my_sock.connect(('data.pr4e,org', 80))

# socket.AF_UNIX
# socket.AF_INET
# socket.AF_INET6
# 这些常量表示地址（和协议）系列，用于socket（）的第一个参数。如果未定义AF_UNIX常量，则不支持此协议。
# Python 中，我们用 socket（）函数来创建套接字，语法格式如下：
# socket.socket([family[, type[, proto]]])
# family: 套接字家族可以使AF_UNIX或者AF_INET
# type: 套接字类型可以根据是面向连接的还是非连接分为SOCK_STREAM或SOCK_DGRAM
# protocol: 一般不填默认为0.