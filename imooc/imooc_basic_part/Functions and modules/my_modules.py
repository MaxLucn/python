'''常用模块属性
dir  列出对象的所有属性及方法
help  查看类、方法的辅助信息
__name__  模块的名称
__file__   文件全路径'''

'''一、获取当前时期'''
# from _datetime import datetime
# from time import time
#
# now_time = datetime.now()
# print("now: {0}".format(now_time))
# now = datetime.today()
# print(now)
# # 当前的日期
#
# # 当前的时间
# print('now_day: {0}'.format(now_time.time()))
# print('year: {0}'.format(now_time.year))
# print('month: {0}'.format(now_time.month))
# print('==================================')
# # 获取毫秒数
# print(time())
# #
# # time.sleep(2)

'''使用from......import......导入datetime模块中的datetime对象，并根据任务要求书写代码。
任务
1、使用两种方法获得当前日期时间，并输出到控制台
2、在控制台上分别对日期和时间进行输出
3、使用-拼接年月日得到当前日期'''
# from datetime import datetime
#
# # 当前日期时间（两种方法）
# now_time = datetime.now()
# print('now: {0}'.format(now_time))
# now = datetime.today()
# print(now)
#
# # 当前日期
# print('now: {0}'.format(now_time.date()))
# # 当前时间
# print('now: {0}'.format(now_time.time()))
# # 当前年月日
# year_ = datetime.now()
# month_ = datetime.now()
# day_ = datetime.now()
# print('{}-{}-{}'.format(year_.year, month_.month, day_.day))

'''二、自定义日期和时间'''
# from datetime import datetime

# d = datetime(1201, 2, 24, 20, 9)
# print(d)
# # 日期、时间与字符串之间的相互转换
# # 字符串转换成 datetime 对象
# now = '2020-4-9  13:32:08'
# now_t = datetime.strptime(now, '%Y-%m-%d %H:%M:%S')     # 转换的时候需要与字符串里的符号保持一致：2020-4-9 , %Y-%m-%d
# print(now_t)
# print('=============================')
# # datetime 对象转换成字符串
# n = datetime.now()
# n_str = n.strftime('%Y-%m-%d %H:%M:%S')
# print(n_str)


'''三、datetime 之间的加减操作'''
# from datetime import datetime, timedelta
#
# n = datetime.now()
# next_n = n + timedelta(days=5, hours=42)
# print(n, "///", next_n)
#
# # 时间的减法
# date1 = datetime(2020, 2, 23)
# date2 = datetime(2020, 5, 25)
# rest = date2 - date1
# print(rest.days)


# 编程练习
'''分别导入datetime和time模块，根据任务要求完成代码的编写。
任务
1、date_time变量接收自定义日期时间为2019-10-10 8:10
2、使用time模块的sleep函数停顿2秒
3、使用date_变量接收自定义日期2019-11-11
4、使用time_变量接收自定义时间11:11'''
# import time
# from datetime import datetime
#
#
# date_time = datetime(2019, 10, 10,  8, 10)
# print(date_time)
# time.sleep(2)
# date_ = datetime(2019, 11, 11)
# print(date_.date())
# time_ = datetime(2019, 12, 23, 11, 11)
# print(time_.time())


'''使用from...import...导入datetime模块中的datetime对象，根据任务要求书写代码。
任务
1、定义一个str_字符串为2019-09-10 8:10:56
2、将str_转换为日期函数2019-09-10 08:10:56，使用str_date变量接收
3、定义now_变量接收当前的日期时间
4、将当前日期时间格式化为——四位的年份/月/日 时:分:秒，使用date_str接收'''
# from datetime import datetime
#
#
# str_ = '2019-09-10 8:10:56'
# str_date = datetime.strptime(str_, '%Y-%m-%d %H:%M:%S')
# print(str_date)
# now_ = datetime.now()
# date_str = now_.strftime('%Y/%m/%d %H:%M:%S')
# print(date_str)


'''使用from......import......导入datetime模块中的datetime，timedelta对象，根据任务要求书写代码。
任务
1、定义now_变量接收当前日期时间
2、使用now_before接收距当前日期时间3天36小时12分钟之前的日期时间
3、使用now_after接收计算10天之后的日期时间'''
# from datetime import datetime, timedelta
# # 定义now_变量接收当前日期时间
# now_ = datetime.now()
# # 计算距当前日期时间3天36小时12分钟之前的日期时间
# now_before = now_ - timedelta(days=3, hours=36, seconds=12)
# # 计算10天之后的日期时间
# now_after = now_ + timedelta(days=10)
# print(now_before)
# print(now_after)


"""python中模块是包含变量、函数、.....代码块的文件；包是存放多个文件/模块的文件夹，
可以统一组织和管理多个python模块；标准的包结构中包含一个特殊的文件[__init__.py]。
两者的区别：包是一个文件夹，可以包含多个文件/模块，模块是一个文件。"""


"""Package和Directory的理解、运用。在引入Package中的模块时可使用from xx import xx和import xx，
而使用后者时还要确保__init__.py文件中个导入了相关模块；在引入Directory中内容时，
只可以引入该目录的子目录中的内容，也可以手动为Directory添加__init__.py使之可以像包一样引用"""