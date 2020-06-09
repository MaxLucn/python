# """ 赋值语句内存分析 """
#
#
# def extend_list(val, my_list=[]):
#     my_list.append(val)
#     return my_list
#
#
# my_list1 = extend_list(10)
# my_list2 = extend_list(123, [])
# my_list3 = extend_list('a')
#
# print(my_list1, my_list2, my_list3)

# """ 垃圾回收机制 """
#
#
# class ClassDc(object):
#     def __init__(self):
#         print('对象产生：{0}'.format(id(self)))
#
#     def __del__(self):
#         print('对象删除： {0}'.format(id(self)))
#
#
# def f0():
#     """ 对象产生后，马上删除，引用由1变成0，内存回收 """
#     while True:
#         c1 = ClassDc()
#         # del c1
#
#
# def f1():
#     """ 一直被引用，不会回收 """
#     my_list = []
#     while True:
#         c1 = ClassDc
#         my_list.append(c1)
#         print(len(my_list))
#
#
# if __name__ == '__main__':
#     # f0()
#     f1()

# import sys
#
# my_list = []
#
# # 对象 my_list 被引用的次数
# print(sys.getrefcount(1))

""" 垃圾回收：分代回收
python 将所有的对象分为 0， 1， 2三代
所有的新建对象都是 0 代对象
当某一代对象经历过垃圾回收，依然存活，那么它就被归入下一代对象
"""
import gc
import sys
import objgraph
# 自动回收
print(gc.get_threshold())


class Persion(object):
    pass


class Cat(object):
    pass


p = Persion()
c = Cat()
p.name = 'Tom'
c.pet = c

c.master = p
print(sys.getrefcount(p))
print(sys.getrefcount(c))

# del p
# del c
# 手动回收
gc.collect()
print(objgraph.count('Persion'))
print(objgraph.count('Cat'))