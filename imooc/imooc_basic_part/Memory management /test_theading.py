# # # import threading
# # # import time
# # #
# # #
# # # def loop():
# # #     """ 新的线程执行的代码 """
# # #
# # #     self.num = 0
# # #     while self.num < 5:
# # #         print(self.num)
# # #         now_thread = threading.current_thread()
# # #         print('【loop】 now thread name: {0}'.format(now_thread.name))
# # #         time.sleep(1)
# # #         self.num += 1
# # #
# # #
# # # def use_thread():
# # #     """ 使用线程来实现 """
# # #     # 当前正在执行的线程名称
# # #     now_thread = threading.current_thread()
# # #     print('now thread name: {0}'.format(now_thread.name))
# # #     # 设置线程
# # #     t = threading.Thread(target=loop, name='loop_thread')
# # #     # 启动线程
# # #     t.start()
# # #     # 挂起线程
# # #     t.join()
# # #
# # #
# # # if __name__ == '__main__':
# # #     use_thread()
# #
# # """ 以继承的方式实现 """
# # import threading
# # import time
# # # from threading import Thread
# #
# #
# # class LoopThread(threading.Thread):
# #     """ 自定义线程 """
# #     num = 0
# #
# #     def run(self):
# #         while self.num < 5:
# #             print(self.num)
# #             now_thread = threading.current_thread()
# #             print('【loop】 now thread name: {0}'.format(now_thread.name))
# #             time.sleep(1)
# #             self.num += 1
# #
# #
# # if __name__ == '__main__':
# #     t = LoopThread(name='loop_thread_oop')
# #     t.start()
# #     t.join()
#
# """
# 实现多线程
# """
#
# import threading
# import time
#
# # 我的银行账户
#
#
# balance = 0
# # 设置线程锁
# # 重复添加会造成死锁
# my_lock = threading.Lock()
# # 添加几次就要释放几次，不会造成死锁
# your_lock = threading.RLock()
#
#
# def change_it(num):
#     """ 改变我的余额 """
#     global balance
#     # 方式一，使用 with 添加线程锁，它会自己打开线程锁，所以不怕会忘记打开线程锁造成出错
#     with my_lock:
#         balance = balance + num
#         time.sleep(0.7)
#         balance = balance - num
#         time.sleep(0.7)
#         print('num------> {0}; balance: {1}'.format(num, balance))
#     # 方式二
#     # try:
#     #     # 添加线程锁
#     #     my_lock.acquire()
#     #     # # 再添加线程锁即可锁住资源，产生死锁
#     #     # my_lock.acquire()
#     #
#     #     balance = balance + num
#     #     balance = balance - num
#     #
#     #     print('num------> {0}; balance: {1}'.format(num, balance))
#     # finally:
#     #     # 解开线程锁
#     #     my_lock.release()
#
#
# class ChangeBalanceThread(threading.Thread):
#     """ 改变银行余额的线程 """
#
#     def __init__(self, num, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.num = num
#
#     def run(self):
#         for i in range(1000):
#             change_it(self.num)
#
#
# if __name__ == '__main__':
#     t1 = ChangeBalanceThread(5)
#     t2 = ChangeBalanceThread(8)
#     t1.start()
#     t2.start()
#     t1.join()
#     t2.join()
#     print('the last : {0} '.format(balance))


""" 线程的优化：线程池 """
import time
import threading
from concurrent.futures.thread import ThreadPoolExecutor
from multiprocessing.dummy import Pool


def run(n):
    """ 线程要做的事 """
    time.sleep(1)
    print(threading.current_thread().name, n)


def main():
    """ 使用传统的方法来做任务 """
    t1 = time.time()
    for n in range(100):
        run(n)
    print(time.time() - t1)


def main_use_thread():
    """ 使用线程优化任务 """
    # 资源有限，最多只能跑10个线程
    t1 = time.time()
    my_list = []
    for count in range(10):
        for i in range(10):
            t = threading.Thread(target=run, args=(i,))
            my_list.append(t)
            t.start()

        for l in my_list:
            l.join()
    print(time.time() - t1)


def main_use_pool():
    """ 使用线程池来优化 """
    t1 = time.time()
    n_list = range(100)
    pool = Pool(10)
    pool.map(run, n_list)
    pool.close()
    pool.join()
    print(time.time() - t1)


def main_use_executor():
    """ 使用 ThreadPoolExecutor 来优化 """
    t1 = time.time()
    n_list = range(100)
    with ThreadPoolExecutor(max_workers=10) as executor:
        executor.map(run, n_list)
    print(time.time() - t1)


if __name__ == '__main__':
    main_use_executor()
