# 在 python 中，0 代表 False ， 非 0 代表 True

# 逻辑运算符的优先级：not > and > or
# 判断输入的年份是否是闰年
# year = int(input('请输入正确的年份：'))
# if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
#     print("{0}年是闰年".format(year))
# else:
#     print("{0}年不是闰年".format(year))


# 分支语句  if  else   elif
# 血压评估
# high = int(input('请输入您测量的高压值：'))
# low = int(input('请输入您测量的低压值：'))
# if 90 >= low >= 60 and 140 >= high >=90:
#     print('您的血压正常')
# else:
#     print('您的血压不正常')


# 从控制台输入一个三位数num，如果是水仙花数就打印num是水仙花数，否则打印num不是水仙花数
# num = int(input("请输入一个三位数："))
#
# # 分别求出三位数的个位，十位，百位
# gw = num//1 % 10
# sw = num//10 % 10
# bw = num//100 % 10
# # 定义变量total，保存各位数字立方和
# total = gw*gw*gw + sw*sw*sw + bw*bw*bw
# # 用if语句判断条件是否成立，并做出相应的输出
# # 补全代码
# if total == num:
#     print("是水仙花数")
# else:
#     print("不是水仙花数")


# 多重分支   pow(4, 2) = 16  平方函数

