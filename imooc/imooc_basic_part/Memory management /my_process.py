# # """ 进程模块介绍
# # 使用 multiprocessing 实现多进程代码
# # 用 multiprocessing.Process 创建进程
# # start() 启动进程
# # join() 挂起进程
# # os.getpid() 获得进程的 ID"""
# # # import time
# # # import os
# # # from multiprocessing.dummy import Process
# # #
# # # """
# # # 实现进程
# # # """
# # #
# # #
# # # def something(name):
# # #     """
# # #     进程要做的事
# # #     :param name:  str 进程的名称
# # #     :return:
# # #     """
# # #     print('进程的名称：{0}, pid{1}'.format(name, os.getpid()))
# # #     time.sleep(3)
# # #     print('进程要做的事')
# # #
# # #
# # # class MyProcess(Process):
# # #
# # #     def __init__(self, name, *args, **kwargs):
# # #         self.my_name = name
# # #         super().__init__(*args, **kwargs)
# # #
# # #     def run(self):
# # #         print('MyProcess进程的名称：{0}, pid{1}'.format(self.my_name, os.getpid()))
# # #         time.sleep(3)
# # #         print('MyProcess进程要做的事')
# # #
# # #
# # # if __name__ == "__main__":
# # #     # p = Process(target=something, args=('my process', ))
# # #     p = MyProcess('my process class')
# # #     p.start()
# # #     p.join()
# #
# # import time
# #
# # import random
# # from multiprocessing import Process, Queue
# # """ 进程之间的通信 """
# #
# #
# # class WriteProcess(Process):
# #     """ 写的进程 """
# #
# #     def __init__(self, q, *args, **kwargs):
# #         self.q = q
# #         super().__init__(*args, **kwargs)
# #
# #     def run(self):
# #         """ 实现进程的业务逻辑 """
# #         # 要写的进程
# #         my_list = ['第一行内容',
# #                    '第二行内容',
# #                    '第三行内容',
# #                    '第si行内容',
# #                    ]
# #         for line in my_list:
# #             print('写入内容：{0}'.format(line))
# #             self.q.put(line)
# #             # 每写入一次休息 1--5 秒
# #             time.sleep(random.randint(1, 5))
# #
# #
# # class ReadProcess(Process):
# #     """ 读取的进程 """
# #     def __init__(self, q, *args, **kwargs):
# #         self.q = q
# #         super().__init__(*args, **kwargs)
# #
# #     def run(self):
# #         while True:
# #             content = self.q.get()
# #             print('读取的内容：{0}'.format(content))
# #
# #
# # if __name__ == "__main__":
# #     # 通过 Queue 共享数据
# #     q = Queue()
# #     # 写入内容的进程
# #     t_write = WriteProcess(q)
# #     t_write.start()
# #     # 读取进程启动
# #     t_read = ReadProcess(q)
# #     t_read.start()
# #
# #     t_write.join()
# #     # t_read.join()
# #     # 在读的进程是死循环，无法等待其结束，只能使用 terminate 强制结束
# #
# #     t_read.terminate()
#
# """ 多进程中的锁的实现 """
# import time
# import random
#
# from multiprocessing import Process, Lock
#
#
# class WriteProcess(Process):
#     """ 写入文件 """
#
#     def __init__(self, file_name,  num, my_lock, *args, **kwargs):
#         # 文件的名称
#         self.file_name = file_name
#         self.num = num
#         # 锁对象
#         self.my_lock = my_lock
#         super().__init__(*args, **kwargs)
#
#     def run(self):
#         """ 写入文件的主要业务逻辑 """
#         try:
#             # 添加锁
#             self.my_lock.acquire()
#             for i in range(5):
#                 content = '现在是: {0}: {1}---{2} \n'.format(self.name, self.pid, self.num)
#
#                 with open(self.file_name, 'a+', encoding='utf-8') as f:
#                     f.write(content)
#                     time.sleep(random.randint(1, 5))
#                     print(content)
#         finally:
#             # 释放锁
#             self.my_lock.release()
#
#
# if __name__ == "__main__":
#     file_name = 'test_txt'
#     # 锁的对象
#     my_lock = Lock()
#     for x in range(5):
#         p = WriteProcess(file_name, x, my_lock)
#         p.start()


# """ 使用进程池 """
# import time
# import random
# from multiprocessing import current_process, Pool
#
#
# def run(file_name, num):
#     """
#     进程执行的业务逻辑，往文件中写入数据
#     :param file_name: str 文件mingc
#     :param num: int 写入的数字
#     :return: str 写入的结果
#     """
#     with open(file_name, 'a+', encoding='utf-8') as f:
#         # 当前的进程
#         noe_process = current_process()
#         # 写入的内容
#         content = '{0}--{1}--{2}'.format(noe_process.name, noe_process.pid, num)
#         f.write(content)
#         f.write('\n')
#         # 写入的时候随机休息 1-5 秒
#         time.sleep(random.randint(1, 5))
#         print(content)
#
#     return 'ok'
#
#
# if __name__ == '__main__':
#     file_name = 'test_pool'
#     # 进程池
#     pool = Pool(2)
#     rest_list = []
#     for i in range(20):
#         # # 同步添加任务
#         # rest = pool.apply(run, args=(file_name, i))
#         # print('{0}----{1}'.format(i, rest))
#         # 异步添加任务
#         rest = pool.apply_async(run, args=(file_name, i))
#         rest_list.append(rest)
#         # print('{0}----{1}'.format(i, rest.get()))
#     # 关闭进程池
#     pool.close()
#     pool.join()
#     # 查看异步执行的结果
#     print(rest_list[0].get())
