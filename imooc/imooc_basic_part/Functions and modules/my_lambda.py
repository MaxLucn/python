# def f(n):
#     """判断给定的数是不是奇数"""
#     return n % 2 != 0        # 这里定义的 f 函数的作用跟：lambda n: n % 2 != 0 作用相同
#
# # filter 、 lambda 函数的示例
# def use_filter(i):
#     """
#     获取指定列表/元组的奇数
#     :return l: list/tuple 要过滤的数据
#     :return: 过滤的奇数列表
#     """
#     # rest = filter(lambda n: n % 2 != 0, i)
#     rest = filter(f, i)
#     return rest
#
#
# if __name__ == '__main__':
#     i = [1, 11, 23, 4, 56, 8, 9, 589]
#     rest = use_filter(i)
#     print(list(sorted(rest)))

"""编程练习
使用filter函数，求0-50以内（包括50）的偶数
任务
1、定义use_filter函数
2、函数体内：实现过滤偶数值的功能"""
# def use_filter(data):
#     # 使用result接收filter过滤偶数值的功能
#     result = filter(lambda n: n % 2 == 0, data)
#     return result
#
#
# if __name__ == '__main__':
#     # 使用data接收0-50的数值
#     data = range(0, 51)
#     # 调用use_filter函数传入data,使用result变量接收
#     result = use_filter(data)
#     print(list(result))


# # map()函数的示例
# # 求立方的第一种方法
# def pow_number(l):
#     """根据给定的列表数据，计算里面每一项的立方
#     :param l: list/type int 类型的列表或者元组
#     :return: 原来列表中每一项的立方
#     """
#     rest_list = []
#     for x in l:
#         rest_list.append(x * x * x)
#     return rest_list
#
# # 求立方的第二种方法
# def f(n):
#     """求给定数的立方"""
#     return n * n * n
#
#
# def pow_num_use_map(l):
#     """根据给定的 map 函数，计算里面每一项的立方
#     :param l: list/type int 类型的列表或者元组
#     :return: 原来列表中每一项的立方
#     """
#     return map(f, l)
#
#
# # 求立方的第三种方法
# def pow_num_use_lambda(l):
#     """使用 map/ lambda 计算里面每一项的立方
#     :param l: list/type int 类型的列表或者元组
#     :return: 原来列表中每一项的立方
#     """
#     return map(lambda n: n * n * n, l)
#
#
# if __name__ == "__main__":
#     l = [1, 2, 5, 8, 7, 9, 3]
#     rest = pow_number(l)
#     print(rest)
#     print("`````````````````````````````````")
#     rest_map = pow_num_use_map(l)
#     print(list(rest_map))
#     print('================================')
#     rest_lambda = pow_num_use_lambda(l)
#     print(list(rest_lambda))


"""编程练习
使用map函数，求元组中各个元素的5次方
任务
1、函数体内：实现各个元素的5次方功能
2、调用use_map函数传入data，使用result接收"""
# def use_map(data):
#     # 使用result接收map实现各个元素的5次方功能
#     result = map(lambda n: pow(n, 5), data)
#     return result
#
#
# if __name__ == '__main__':
#     data = (2, 4, 6, 8, 10, 12)
#     # 调用use_map函数传入data，使用result接收
#     result = use_map(data)
#     print(tuple(result))


# # # reduce()函数的使用
# # 求和
# from functools import reduce
#
#
# def get_sum(i):                # 第一种方法
#     """
#     根据给定的列表，求里面各个数字的总和
#     :param i: list/tuple 里面是整数
#     :return:列表所有项的和
#     """
#     rest = 0
#     for num in i :
#         rest += num
#     return rest
#
#
# def get_sum_py(i):                # 第二种方法
#     """
#     使用 python 内置的 sum() 进行求和
#     :param i:
#     :return:
#     """
#     return sum(i)
#
#
# def f(m, n):                    # 第三种方法
#     """ 求两个数的和"""
#     return m + n
#
#
# def get_sum_use_reduce(i):
#     """
#     使用 reduce() 函数进行求和
#     :param i:
#     :return:
#     """
#     return reduce(f, i)
#
#
# def get_lambda(i):       # 第四种方法
#     """
#     使用 lambda() 表达式求和
#     :param i:
#     :return:
#     """
#     return reduce(lambda m, n: m + n, i)
#
#
# if __name__ == '__main__':
#     i = [1, 3, 4, 5, 6]
#     rest = get_sum(i)
#     print(rest)
#     print("======================")
#     rest_py = get_sum_py(i)
#     print(rest_py)
#     print("=======================")
#     rest_reduce = get_sum_use_reduce(i)
#     print(rest_reduce)
#     print("=======================")
#     rest_lambda = get_lambda(i)
#     print(rest_lambda)


"""编程练习：请运用reduce函数，计算20的阶乘，并于终端打印计算结果
任务
1、定义use_reduce函数
2、函数体内：实现某个数值的阶乘"""
from functools import reduce


def use_reduce(data):
    result = reduce(lambda x, y: x * y, data)
    return result


if __name__ == '__main__':
    data = list(range(1, 21))
    print(use_reduce(data))