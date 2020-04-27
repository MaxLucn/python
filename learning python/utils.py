# 导入模块练习
# numbers = [7, 4, 3, 8, 0]
# max = numbers[0]
# for number in numbers:
#     if number > max:
#         max = number
# print(max)
# 用引入模块的的方法实现
# 第一步建立函数
def find_max(numbers):
    # numbers = [7, 4, 3, 8, 0]
    my_max = numbers[0]
    for number in numbers:
        if number > my_max:
            my_max = number
    return my_max
