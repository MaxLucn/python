# my_name = 'imooc'
# my_age = 18
# my_sex = False
# print("My name is", my_name, "and my age is", my_age, "and my sex is", my_sex)

# print(78 % 10, 78 / 10, 2 ** 3, 78 // 10)

# print((18/9) ** (8 % 3))

# m = 10
# n = 5
# # 变量m的值加3，n的值加5
# # 求m和n的平均值
# # 求m的平方乘以n的平方
# # 根据效果图进行输出averageResult、productResult
# m += 3
# n += 5
# print(m, n)
# print((m+n)/2)
# print((m**2)*(n**2))

# 大小写转换  upper , lower  全字符大、小写转换
#  capitalize  首字母大写
#  title  设置每一个单词的首字母大写
# print('asdf safbkj kjfhaj ajhsf '.title())
# swapcase 大小写互换


# format 格式化字符串、数字返回的都是字符串
# 格式化字符串，示例：
# print('{} {} you'.format('i', 'miss'))
# print('{2}.{1}.{0}'.format('you', 'miss', 'i'))

# 格式化数字，示例：
# print(format(1231.3252387, '0.2f'))    #  0.2f 小数保留2位
# print(format(12313252387, ','))     #  ， 千分位分隔符


# # 练习
# account = 'max:6522465'
# amt = 1234568
# # 在字符串格式化输出时，如果遇到格式化输出的数字，则需要在{}内增加 : 前缀，之后写上格式化语句
# print('请您向账户{}转账：¥{:0,.3f}'.format(account, amt))


# 制表符是指增加自负的缩进，在字符串中使用 \t    换行符是指为字符串换行输出，在字符串中使用  \n   示例：
# print('姓名\t性别\t年龄\nTom\t男\t23\n\t')


# 删除空白   str.strip()删除两侧空白； str.lstrip()删除左侧空白；str.rstrip()删除右侧空白  示例：
#  查找字符串： str.find()   字符串替换： str.replace()
