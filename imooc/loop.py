# 这是写 while 循环的。 定义循环的执行条件、编写要被执行的循环代码、编写修改执行条件的代码。 简单示例：
# i = 0
# while i < 4:
#     print('这是测试 while 循环的')
#     i += 1


# 计算从1到1000以内所有奇数的和，并进行输出，结果为250000
# 任务
# 1、定义变量sum1和 num1，sum1用于存放所有奇数和，num1用于存放数值，并对其赋初始值
# 2、使用while来实现1-1000以内的循环
# 3、用if语句实现条件判断，是否为奇数
# 4、输出符合条件的所有奇数的和
# sum1 = 0
# num1 = 1
# # 循环条件
# while num1 <= 1000:
# # 判断条件
#     if num1 % 2 != 0:
# # 求和
#         sum1 = sum1 + num1
#     num1 = num1 + 1
# print(sum1)


#  1-100以内的阶乘示例代码
# i = 1
# num = 1
# while i <= 100:
#     i += 1
#     num = i * i
# print(num)

'''计算1到100以内能被3或者7整除，但不能同时被3和7整除的数的个数，运行结果为39
任务
1、定义变量num用来存放数值，count用来存放个数
2、使用while实现循环
3、通过if来设置符合的条件，符合条件count计数加1
4、输出符合条件的总个数count '''
# num = 1
# count = 0
# while num <= 100:
#     if (num % 3 == 0 or num % 7 == 0) and not num % 21 == 0:      # 但不能同时被3和7整除的数的个数。 即不能被21整除
#         count += 1
#     num += 1
# print(count)


# continue 用于跳过当前循环的剩余语句   break 关键字用来终止循环语句
# continue 之后的语句都会被跳过并执行下一次循环   break 被执行后会直接执行循环最后外的语句
# i = 0
# while i < 3:
#     mobile = input('请输入您要查询的手机号：')
#     i += 1
#     if mobile == '15012514584':
#         print('您的话费余额为：13254元')
#         break
# print('感谢您的来电')

# 循环嵌套： 在循环中出现循环的情况。 简单实例：
'''实现  口口口口
        口口口口
        口口口口
        口口口口'''

# j = 0
# while j < 4:
#     i = 0
#     while i < 4:
#         print('口', end='')     # 结尾不换行
#         i += 1
#     j += 1
#     print('')


# i = 1
# j = 1
# k = 0
# while i < 5:
#     while j < 5:
#         k = i + j
#         if j == 3:
#             break
#         j += 1
#     i += 1
# print(k)


'''利用while循环嵌套实现下图效果
        *
       ***
      *****
任务
1、定义变量n、x、y，并对其赋初始值，n用于控制外层循环，即输出行数；x用于设置满足条件时输出的空格个数；y用于设置满足条件时输出的*个数
2、通过使用while循环嵌套实现，外层循环用于控制输出行数'''

# i = 1
# while i <= 5:
#     j = 1
#     while j <= 5 - i:
#         print(' ', end='')
#         j += 1
#     k = 1
#     while k <= 2 * i - 1:
#         print('*', end='')
#         k += 1
#     print()
#     i += 1


# 列出 1000 以内的所有质数（面试常见题）
# 质数：只能被1 和它本身不能整除其他的数
j = 2
while j <= 1000:
    num = j
    i = 2
    is_prime = True     # 标识当前数字是否是质数，True 是 Flase 不是
    while i < num:
        if num % i == 0:
            is_prime = False
            break
        i += 1
    # if is_prime == False:
    #     print('{}不是质数'.format(num))
    if is_prime == True:
        print('{}是质数'.format(num))
    j += 1
