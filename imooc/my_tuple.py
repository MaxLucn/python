'''元组的读写方式跟列表相同
元组一建立就内容不允许修改，但是可以使用运算符创建新元组
t1 = (1, 0, 2) + (5, 8)
print(t1)
使用运算符操作元组的时候如果只有一个元素，必须在这个元素后增加逗号说明这是一个元组
t2 = (9,) * 9
t3 = (9) * 9
print(t2, t3)
如果一个元组里的元素是列表的话，列表里面的值是支持修改的'''
# t1 = (1, 0, 2) + (5, 8)
# print(t1)

# t2 = (9,) * 9
# t3 = (9) * 9
# print(t2, t3)

'''序列中的元素顺序按添加顺序排列
序列中的数据通过'索引'进行获取
序列包含常用数据结构： 字符串、列表、元组、数字序列（数字范围range）'''
# r = range(1, 10, 2)
# print(r[3:5])


# 斐波那且数列前50位的和
# result = []
# for i in range(0, 50):
#     if i == 0 or i == 1:
#         result.append(1)
#     else:
#         result.append(result[i-2] + result[i-1])
# print(result)

# 判断数字是否是质数
# num = 4895754817
# result = True
# for i in range(2, num):
#     if num % i == 0:
#         print(i)
#         result = False
#         break
# if result == True:
#     print('{0}是质数'.format(1))
# else:
#     print('{0}不是质数'.format(1))

'''任务:有四个数字1、2、3、4，能组成多少个互不相同且数字不重复的两位数
1、 定义变量count，用于存放统计出所组成的两个数的个数
2、定义变量lst，用于存放组成后的两位数'''
# count = 0
# # 定义一个空列表用于存放数据
# lst = []
# for i in range(1, 5):
#     # 使用for循环得到另一个数j
#     for j in range(1, 5):
#         if i != j:
#             # 将数据添加到列表中
#             num = j*10 + i
#             lst.append(num)
#             count += 1
# print(count)
# lst.sort()      # 对得到的列表进行排序
# print(lst)


'''list 将一个序列转换成列表
tuple 将一个序列转换成元组，里面有特殊字符的需要先将其转换成列表才能用
str 函数用于将单个数据转换成字符串
join 对所有元素为字符串的列表，元组，进行连接'''


'''
集合可以看成没有 value 值的字典
集合元素是无序的
集合元素不能重复
集合是可变的
集合允许数学运算
集合是分散存储的'''
# college = {'哲学', '法学', '医学', '经济学'}
# print(college)
# # set() 内置函数从其他数据结构转换
# college = {'哲学', '法学', '医学', '经济学'}
# print(college1)
# # set() 创建空集合
# college2 = set()
# print(type(college2))

# 集合关系与数学运算：交集、并集、差集
# college = {'哲学', '法学', '医学', '经济学'}
# college1 = {'哲学', '法学', '医学', '经济学', '体育学', '农学', '电学'}
# c = college.intersection(college1)            # 交集,两个集合重合部分
# print(c)
# c2 = college.union(college1)                   # 并集，把两个集合合并去重
# print(c2)
# college1 = set(['哲学', '法学', '医学', '经济学', '体育学', '农学', '电学'])
# c3 = college1.difference(college)               # 差集，两个集合没有有差异的部分
# print(c3)

'''任务求两个列表中的交集，并集，差集
输出的最终结果数据类型为列表'''
# a_list = [1, 2, 3, 4, 5]
# b_list = [1, 4, 7, 9]
# a_list = set(a_list)
# b_list = set(b_list)
# # 求两个列表之间的交集
# int_list = a_list.intersection(b_list)
# print(int_list)
# # 求两个列表之间的并集
# uni_list = a_list.union(b_list)
# print(uni_list)
# # 求两个列表之间的差集（a_list在b_list中不存在的部分）
# dif_list = a_list.difference(b_list)
# print(dif_list)


# # 列表生成式
# lst = []
# for i in range(10, 20):
#     lst.append(i*10)
# # 生成式表达
# lst = [i*10 for i in range(10, 20)]


# 字典生成式
# list1 = ['Tom', 'Bob', 'Kim', 'Jerry']
# dict1 = {i + 1: list1[i] for i in range(0, len(list1))}
# print(dict1)

# # 集合生成式
# set1 = {i**j for i in range(1, 4) for j in range(1, 4) if i == j}
# print(set1)
#
#
# for i in range(1, 4):
#     for j in range(1, 4):
#         if i == j:
#             set1.add(i**j)
#             print(set1)

'''lst = [23,45,22,44,25,66,78]
用列表生成式完成下面习题：
1、生成lst列表中所有奇数组成的列表
2、与lst列表相比较，使用相应的列表生成式，使得输出结果[28, 50, 27, 49, 30, 71, 83]'''
# lst = [23, 45, 22, 44, 25, 66, 78]
# # 生成所有奇数组成的列表
# lst1 = [i for i in lst if i % 2 != 0]
# print(lst1)
# # 输出结果[28, 50, 27, 49, 30, 71, 83]
# lst2 = [i + 5 for i in lst]
# print(lst2)


'''两个集合关系的判断：
== 判断两个集合是否相等
issubset 判断一个是否是另一个的子集
issuperset  判断一个是否是另一个的父集
isdisjoint 判断两个集合之间是否存在重复元素，返回布尔值
给集合添加、删除元素：
add() 一次只能添加一个元素
update() 以元组或列表的形式添加多个元素
集合不支持直接新增元素，但是可以通过用 remove() 先删除再添加
remove() 删除集合中不存在的元素时会报错
discard() 删除元素的时候如果没有则会跳过
'''

