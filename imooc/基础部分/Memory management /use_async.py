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
