# 正则表达式是一种非常专业的语言，它使我们能够简洁地搜索字符串并从字符串中提取数据。正则表达式本身就是一种语言
# 这是一种查找大量文本非常聪明的方法
# 在Python内部，正则表达式不是 内置于基本语言中，例如字符串，列表或字典， 我们必须在导入时首先使用import语句说， 引入该程序的正则表达式库
# findall是提取 ， 点是任何字符，星号表示任意多次，  美元符号表示行尾。 点表示任何字符， 插入符号也有开始的意思

# find方法与正则表达式的对比
# hand = input('enter as file name')
# for line in hand:
#   line = line.rstrip()
#   if line.find('From:') >= 0:
#       print(line)                  #
#
# import re
# hand = open('mbox-short.txt')
# for line in hand:
#     line = line.rstrip()
#     if re.search('From:', line):
#         print(line)

# startswith方法与正则表达式的对比
# hand = input('enter as file name')
# for line in hand:
#     line = line.rstrip()
#     if line.startswith('From:'):
#         print(line)

# import re
# hand = open('mbox-short.txt')
# for line in hand:
#     line = line.rstrip()
#     if re.search('^From:', line):   # ^插入的这个字符并不是文件里真实存在的。它的意思是'F'是该行的第一个字符
#         print(line)



# 在正则表达式中'.'表示任何字符， '*'表示零次或者多次    比如：" '^X.*:' " 表示寻找以X开头的行,在这个表达式里，X、：不是特殊字符


# 正则表达式提取文件中的内容
# import re
# x = 'my 2 favourite numbers are 7 and 10'
# y = re.findall('[0-9]+', x)         # 这里的方括号是正则表达式里特殊字符的一个，+表示大于等于1
# print(y)
# y = re.findall('[AEIOU]+', x)       # 这里的方括号是正则表达式里特殊字符的一个
# print(y)

# 要求：查找from
# 贪婪匹配：在没有申明的情况下会查找、提取出最大可能，比如：
# import re
# x = "from: I'm from China"
# y = re.findall('^f.+:', x)
# print(y)                         # 在我们申明错误或者没有申明的情况下，他会提供给我们最大的可能，'*''+'都是推到最大可能，

# # 要达到要求我们可以在'^f.+'这里做一点处理即可，我们可以在'+'号的后面多加一个'？'，这里的'？'也是正则表达式的一个可以表示任何东西的特殊符号。
# import re
# x = "from: I'm from China"
# y = re.findall('^f.+?:', x)
# print(y)




#  反斜杠可以加上前缀否则为活动字符， 因此，美元符号具有含义， 但斜线美元符号表示它确实是一个美元符号。



import re

hand = open('regex_sum_331828.txt')
num_list = list()
my_sum = 0
my_count = 0
for line in hand:
    line = line.strip()
    stuff = re.findall('[0-9]+', line)
    if len(stuff) > 0:
        for i in stuff:
            i = int(i)
            my_sum += i
    # else:
        # continue

print(my_sum, my_count)