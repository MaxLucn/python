# def hello():
#     """ 简单功能模拟 """
#     print(" hello world")
#
#
# def hello_wrapper():
#     """ 新的函数，包裹原来的 hello """
#     print("开始执行hello")
#     hello()
#     print('结束执行 hello')


# if __name__ == "__main__":
# hello()
# hello_wrapper()


# 装饰器的演示
# def log(func):
#     """ 记录函数执行的日志 """
#
#     def wrapper():
#         print("开始执行")
#         func()
#         print("执行结束")
#     return wrapper
#
#
# @log
# def hello():
#     """ 简单功能模拟 """
#     print(" hello world")
#
#
# if __name__ == "__main__":
#     hello()


# # 带参数的装饰器的演示
# from functools import wraps
#
#
# def log(name=None):
#     """ 记录函数执行的日志 """
#
#     def decorator(func):
#         # 防止 @log 装饰器改变原来的属性和方法
#         @wraps(func)
#         def wrapper(*args, **kwargs):
#             """ 装饰器内部的函数 """
#             print("{0}.star...".format(name))
#             rest = func(*args, **kwargs)
#             print("{0}.end...".format(name))
#             return rest
#         return wrapper
#     return decorator
#
#
# @log('hello')
# def hello():
#     """ 简单功能模拟 """
#     print(" hello world")
#
#
# @log()
# def test():
#     print("test...")
#
#
# @log('from add')
# def add(a, b):
#     return a + b
#
#
# if __name__ == '__main__':
#     # hello()
#     # test()
#     print(add(5, 6))
#     print("doc:{0}".format(hello.__doc__))
#     print("name:{0}".format(hello.__name__))


def use_range():
    """ python 内置的 range 函数 """
    for i in range(5, 10):
        print(i)


class IterRange(object):
    """ 使用迭代器来模拟 range 函数 """

    def __init__(self, start, end):
        self.start = start - 1
        self.end = end

    def __next__(self):
        self.start += 1
        if self.start >= self.end:
            raise StopIteration
        return self.start

    def __iter__(self):
        return self


class GenRange(object):
    """ 使用生成器模拟 range 函数 """

    def __init__(self, start, end):
        self.start = start - 1
        self.end = end

    def get_num(self):
        while True:
            if self.start >= self.end - 1:
                break
            self.start += 1
            yield self.start


def get_num(start, end):
    start -= 1
    while True:
        if start >= end -1:
            break
        start += 1
        yield start


if __name__ == '__main__':
    # use_range()
    iter = IterRange(5, 10)
    my_list = list(iter)
    print(my_list)
    print("=================")
    gen = GenRange(5, 10).get_num()
    print(gen)
    # print(next(gen))
    # print(next(gen))
    # print(next(gen))
    print(list(gen))
    print("==================")
    gen_f = get_num(5, 10)
    print(gen_f)
    print(list(gen_f))