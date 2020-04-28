# 导入模块练习
# numbers = [7, 4, 3, 8, 0]
# max = numbers[0]
# for number in numbers:
#     if number > max:
#         max = number
# print(max)
# 用引入模块的的方法实现
# 第一步建立函数
# def find_max(numbers):
#     # numbers = [7, 4, 3, 8, 0]
#     my_max = numbers[0]
#     for number in numbers:
#         if number > my_max:
#             my_max = number
#     return my_max


#练习：把下面的这个找列表里最小值的代码用引入模块的方法实现。
# 第一步：已知引入的模块要有类、函数。所以我们应该先建立所需要的东西
# numbers = [2, 5, 6, 8, 0, 34, 81]
# my_min = numbers[0]
# for number in numbers:
#     if number < my_min:
#         my_min = number
# print(my_min)

def find_min(numbers):
    my_min = numbers[0]
    for number in numbers:
        if number < my_min:
            my_min = number
    return my_min