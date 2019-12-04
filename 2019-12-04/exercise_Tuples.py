# 一
# 元组是列表的受限版本。 总的来说，元组是一种更有效的 您无法修改的列表的版本
# 元组看起来跟列表很像，元组我们要用括号括起来      元组不可改变
# 二
# 元组与列表的不同：
# 1、区别在于列表是可变的，而字符串和元组则不是可变的。
# 2'您无法对元组进行排序。 无论在创建元组时将其放入的顺序如何，它都会保留在其中。
# my_list = ['Tom', 'Jerry', 'Ricardo', 'Kim']  # 列表
# my_tuples = ('Tom', 'Jerry', 'Ricardo', 'Kim') # 元组
# my_list[2] = 'Bob'       # 列表 List
# print(my_list)           # 这里证明列表是可变的
# # my_tuples[2] = 'Bob'   # 元组 Tuple
# #print(my_tuples)        # 这里证明元组不可变，它会输出错误
# my_str = 'hello,world'   # 字符串 String
# my_str[2] = 'i'
# print(my_str)            #这里证明字符串不可变，它会输出错误
# 三
# 在元组中查找等方法的使用跟在列表中是一样的
# 可以在元组等于元组，这跟赋值很相似，注意：这样做的是时候它是左右对称的，比如
# (Name, Age) = ('Tom', '18')
# print(Name, Age)
# 四
# 这种方法的工作方式就是记住d.items， d.items为您提供元组列表。
# my_dict = dict()
# my_dict['Tom'] = 18
# my_dict['Jerry'] = 20
    # for (key, value) in my_dict.items():
#     print(my_dict)
# my_tup = my_dict.items()
# print(my_tup)              # 这就是我们构造这两个迭代变量的方式 使用元组的循环
# 五
# 我们可以把元组拿来比较，不论元组里面的是字符串还是整型还是浮点型都可以。
# 六
# 通过key值来把由字典转化来的列表用sorted()函数重新排序 ，注意sorted函数只适用于列表
# count = dict()
# count['Tom'] = 10
# count['Jerry'] = 34
# count['Ricardo'] = 7
# count['Kim'] = 3
# # counts = count.items()
# # my_list = sorted(count.items())
# my_list = list()                              # 用sorted函数按key值重新排序
# for key, value in count.items():
#     # print(key, value)           # 遍历整个列表找出对应字典里的key值以及跟它对应的value
#     my_list.append(value)
#     my_list.append(key)
#
# print(my_list)
# my_list =list()
# my_list = sorted(my_list, reverse=True)      # reverse是测验操作符，即：如果这样为真的话...
# print(my_list)                               # 按value值来重新排序列表