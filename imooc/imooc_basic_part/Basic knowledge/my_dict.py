'''字典的特点：
字典采用键 key ： 值 value 形式表达数据
字典中 key 不允许重复， value 值没限制
字典是可以修改的，运行时动态调整存储空间
下面是几个创建字典的示例
'''
# # 直接花括号创建
# dict1 = {'name': 'Tom', 'age': '154'}
# print(dict1)
#
# # 利用 dict 函数创建
# dict2 = dict(name='Tom', age='213')
# print(dict2)
# dict3 = dict.fromkeys(['name', 'age'], 'Tom/44')
# print(dict3)


# 字典的取值
# dict1 = {'name': 'Tom', 'age': '154'}
# name = dict1['name']
# print(name)
# print(dict1.get('age'), dict1.get('job'))


# 遍历字典
# dict1 = {'name': 'Tom', 'age': '154'}
# for k in dict1:
#     v = dict1[k]
#     print(v)
# for k, v in dict1.items():
#     print(k, v)

# 字典的更新操作
# dict1 = {'name': 'Tom', 'age': '154'}
# dict1['name'] = ['Jerry']                 # 单个 k，v 操作
# print(dict1)
# dict1.update(name='Kim', age='32')        # 多个 k, v 操作
# print(dict1)


'''删除操作
pop 删除指定的键值对
popitem 删除最后一个键值对
clear 清空整个字典'''


'''字典常用的一些操作
1、setdefault 为字典设置默认值，如果某个 key 已存在则忽略，如果不存在则设置
2、获取字典的视图
  keys 获取所有的键
  values 获取所有的值
  item 获取所有的键值对
3、利用字典格式化字符串
 老版本的字符串格式化
 dict2 = "姓名:%(name)s,年龄:%(age)s"
 新版本的字符串格式化
 dict2 = "姓名:{name},年龄:{age}".format_map(dict1)
'''

'''任务
1、创建字典dict01,里面包含name为小王，age为18，sex为女，dept为技术部
2、使用for循环遍历字典dict01的键值对
3、向控制台输出键和值'''
# dict01 = {'name:': '小王', 'age:': '18', 'sex:': '女', 'dept:': '技术部'}
# for k, v in dict01.items():
#     print(k, v)
