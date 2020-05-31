# # import asyncio
# #
# #
# # async def something(x):
# #     """ 定义协程函数 """
# #     print('等待中： {0}'.format(x))
# #
# #
# # # 判断是否为协程函数
# # print(asyncio.iscoroutinefunction(something))
# #
# # coroutine = something(5)
# # # 事件的循环队列
# # loop = asyncio.get_event_loop()
# # # 注册任务
# # task = loop.create_task(coroutine)
# # print(task)
# # # 等待协程任务执行结束
# # loop.run_until_complete(task)
# # print(task)
#
#
# """ 协程之间的数据通信：
# 嵌套调用
# """
# # import asyncio
# #
# #
# # async def compute(x, y):
# #     print('计算 x + y ---> {0} + {1}'.format(x, y))
# #     await asyncio.sleep(1)
# #     return x + y
# #
# #
# # async def get_sum(x, y):
# #     rest = await compute(x, y)
# #     print('{0} + {1} = {2}'.format(x, y, rest))
# #
# #
# # # 拿到事件循环
# # loop = asyncio.get_event_loop()
# # loop.run_until_complete(get_sum(2, 3))
# # loop.close()
#
# """协程之间的数据通信： 队列
# 1、定义一个队列
# 2、让两个协程来进行通信
# 3、让其中一个协程往队列中写入数据
# 4、让另一个协程从队列中删除数据
# """
# import asyncio
# import random
#
#
# async def add(store, name):
#     """
#     写入数据到队列
#     :param store:队列的对象
#     :return:
#     """
#     for i in range(5):
#         # 往队列中添加数字
#         num = '{0} - {1}'.format(name, i)
#         await asyncio.sleep(random.randint(1, 5))
#         await store.put(i)
#
#         print('{2}--add one ...{0}, size: {1}'.format(num, store.qsize(), name))
#
#
# async def reduce(store):
#     """
#     从队列中删除数据
#     :param store:
#     :return:
#     """
#     for i in range(10):
#         rest = await store.get()
#         print('    reduce one ...{0}, size:{1}'.format(rest, store.qsize()))
#
#
# if __name__ == "__main__":
#     # 准备一个队列
#     store = asyncio.Queue(maxsize=5)
#     rest = add(store, 'a1')
#     rest1 = add(store, 'a2')
#     r1 = reduce(store)
#     # 添加到事件队列
#     loop = asyncio.get_event_loop()
#     loop.run_until_complete(asyncio.gather(rest, rest1, r1))
#     loop.close()
# text = [4,9]
# content = text.copy()
# text.append(13)
# content.append([5, 10])
# print("hello" + '  ' + "Python")
# print(content)
# text = 'noe three'
# print(text.find('e', 3, 8))
# num = input("")
# print(type(num))
# str = 'http://www.imooc.com/'
# print(str.find('im', 14))
# s = 'love,imooc'
# print(s.split(','))
# num = 6.0
# print(type(num))
# num1 = input(";;")
# num2 = input("...")
# s = num1 + num2
# print('he ', s)

# print('a\tb\nc\td')
# print(6.0==int('6'))
# print("imooc".upper()=='IMOOC')
# print("imooc ".rstrip()!='imooc')
# print(" imooc ".strip()=='Imooc')
# t = [32, -3, 10, -8]
# res = map(lambda x: x + 1, t)
# print(list(res))
# from functools import reduce
# nums = [2, 4,6, 8]
# res =reduce(lambda x, y: x*y, nums)
# print(res)

# def test ():
#     sun = 0
#     for i in range(0, 5):
#         sun+=1
#     print(sun)
# test()
# f = open('sa.txt', 'r')
# test = f.readline()
# print('sfs', test)
# f.close()
# rest = lambda x, y:x**2+y**3
# print(rest(y=2,x=3))
# r = filter(lambda x:x%2==0,range(10))
# print(list(r))
# from functools import reduce
#
#
# def fn(x, y):
#     return x * 10 + y
#
#
# def charToNum(s):
#     dict1 = {'0': 0, '1': 1, '2': 2}
#     return dict1[s]
#
#
# r = reduce(fn, map(charToNum, '23443'))
# print(r)
# print(type(r))
print("sdass{:0.2f}adfds".format(1024.6868))