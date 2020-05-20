# my_list = [1, 2, 3, 4, 2]
# print(my_list.index(2))       # index 用于获取指定元素的索引值，返回的是第一次出现元素的索引


# 遍历列表
# names = ['Tom', 'Jerry', 'Kim', 'Vet', 'Max']
# for name in names:
#     if name == 'Max':
#         print(name)
# print(len(names))

'''
任务
1、定义一个列表numList，存储元素为1到10的所有整数
2、for循环遍历输出所有列表中的偶数
'''
# numList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# i = 0
# for i in numList:
#     if i % 2 == 0:
#         print('{}'.format('第i个偶数'), i)
#         i += 1

'''列表的反转与排序：reverse 反转列表
   sort 排序
   示例
'''
# names = ['Tom', 'Jerry', 'Kim', 'Vet', 'Max']
# names.reverse()       #  反转
# print(names)

# num = [12, 35, 4, 623, 445, 64566, 1, 2]
# num.sort()   # 排序
# print(num)
# num.sort(reverse=True)    # 降序排列
# print(num)

'''列表的增删查改
list.append(新元素)                      在列表末端追加新元素
list.insert(索引，新元素)                 在指定索引插入新元素
list[索引] =  新值                       更新指定索引位置数据
list[起始索引：结束索引] = 新列表           更新指定范围数据
list.remove(元素)                       删除指定元素
list.pop(索引)                          按索引删除指定元素
示例如下
'''
# 追加
# name = ['Tom', 'Jerry', 'Kim', 'Vet', 'Max']
# name.append('Bob')
# print(name)
# # 插入
# name.insert(3, 'John')
# print(name)
# # 更新
# name[2] = 'Bob'
# print(name)
# # 范围更新
# name[2:3] = ['Bob', 'John']
# print(name)
# # 按内容删除
# name.remove('John')
# print(name)
# # 按范围删除
# name.pop(3)
# print(name)
# name[2:3] = []
# print(name)


'''任务
1、定义list2为空列表
2、循环遍历list1
3、if判断list1中的每个元素是否在list2中
4、如果元素不在list2中，则将元素追加到list2中
5、使用sort对list2进行降序排序'''
# list1 = [23, 98, 56, 55, 76, 98, 55]
# list2 = []
# for i in list1:
#     if i not in list2:
#         list2.append(i)
# list2.sort(reverse=True)
# print(list2)


# 嵌套列表
# my_str = 'Hello,world,你好'
# my_list = my_str.split()
# print(my_list)


# my_list = []
# while True:
#     my_str = input('请输入员工信息：')
#     if my_str == '':
#         print('程序结束')
#     my_str_list = my_str.split(',')
#     if len(my_str_list) != 3:
#         print('输入格式不正确，请重新输入：')
#         continue
#     my_list.append(my_str_list)
#     for emp in my_list:
#         print('姓名:{n}, 年龄:{a}, 工资:{s}'.format(n=emp[0], a=emp[1], s=emp[2]))


'''任务
1、定义变量reason为外层列表，里面嵌套列表[3, 4, 5]，列表[6, 7, 8]，列表[9, 10, 11]，列表[12, 1, 2]
2、定义month接收input函数
3、使用if判断语句判断输入的月份为什么季节'''
# reason = [[3, 4, 5], [6, 7, 8], [9, 10, 11], [12, 1, 2]]
# month = int(input('请输入1-12之间的月份：'))
# if month in reason[0]:
#     print('{0}月是春季'.format(month))
# elif month in reason[1][0:3]:
#     print('{0:3}月是夏季'.format(month))
# elif month in reason[2][0:3]:
#     print('{0:3}月是秋季'.format(month))
# elif month in reason[3][0:3]:
#     print('{0:3}月是冬季'.format(month))
# else:
#     print('请输入正确的月份！')
