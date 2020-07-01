'''函数的介绍：具有特定功能的代码
隐藏实现功能的细节
重用代码
提高可读性，便于调试'''


'''def 函数名(参数):
    函数体 
    return 输出的数据
给函数传参数的几种方法
1、为参数设置默认值，只需要在形参后面增加 '= 具体值'即可
2、以形参形式传传参，有多个参数的时候可以把它封装成一个字典然后传入（关键字传参）
3、当函数形参里出现' * ' 的话，后面的所有参数都要使用关键字传参
'''

''' 编程练习
1、使用format格式化字符串向控制台输出"imooc-程序员的梦工厂出生于2013年8月"
2、调用函数，向函数内传入（程序员的梦工厂，2013年8月'''
# def info(*, desc,birth, name='imooc'):
#     print('{}{}{}{}'.format(name, '-', desc, birth))
#     return
#
#
# info(desc='程序员的梦工厂', birth='2013年8月')

'''任务：定义一个函数，实现在控制台打印3遍唐诗《咏鹅》，并使用50个星（*）号分隔每一次打印结果
1、定义函数名为goose的函数
2、函数体内：向控制台输出唐诗《咏鹅》
3、函数体内：向控制台输出50个*号分隔符
4、调用三次函数名为goose的函数
'''

# def goose():
#     # 向控制台输出唐诗《咏鹅》诗句
#     print('鹅，鹅，鹅，曲项向天歌。白毛浮绿水，红掌拨清波。')
#     # 向控制台输出50个*号分隔符
#     print('*' * 50)
# # 调用函数实现效果
# goose()

# 函数的形参与实参
# def result(verse_name):               # verse_name  形参
#     if verse_name == 'hello':
#         print('你好')
#     elif verse_name == 'bey':
#         print('再见')
#
#
# result('hello')                  #  'hello'  'bey'  实参
# result('bey')


'''定义一个函数，向函数内传入形参num, num1, num2，如果num小于100，则计算num1 和 num2的积并打印；否则计算num1 和num2的和，然后打印输出
任务
1、定义函数名为oper的函数
2、当num值小于100时，求两数的乘积，反之求两数的和
3、调用函数，向函数内传入1314, 52, 0和5, 2, 0两组数据测试结果'''

# def oper(num, num1, num2):
#     if num < 100:
#         print(num1 * num2)
#     else:
#         print(num1 + num2)
#
#
# oper(1314, 52, 0)
# oper(5, 2, 0)


'''定义一个函数，向函数内传入形参username，password，当username值为imooc且password值为字符串123456时，返回“登录成功”；
否则返回“请重新登录”
任务
1、定义函数login
2、if语句判断用户名和密码是否为字符串imooc和123456'''

# def login(username, password):
#     # 使用if语句，判断用户名和密码为“imooc”和“123456”
#     if username == 'imooc' and password == '123456':
#         # 返回登录成功
#         return '登录成功'
#     # 使用else子句处理用户名和密码非“imooc”和“123456”的情况
#     else:
#         # 返回请重新登录
#         return '请重新登录'
# # 调用函数，向函数内传入'imooc','123456'和'mooc','123456'两组数据测试结果
# # 打印函数测试结果
# success = login('imooc', '123456')
# print(success)
#
# false = login('mooc', '123456')
# print(false)


# 序列传参里的字典传参的示例：
# def get_info():
#     dict1 = {
#         'student': [
#             {'name': 'Tom', 'class': '高三7班'},
#             {'name': 'Jerry', 'class': '高三3班'},
#             {'name': 'Kim', 'class': '高二6班'},
#         ],
#         'hobby': [
#             {'id': 57, 'hob': '足球'},
#             {'id': 23, 'hob': '田径'},
#             {'id': 7, 'hob': '美术'},
#         ]
#     }
#     return dict1
#
#
# info = get_info()
# print(info.get('student')[1].get('class'))

'''定义seq函数，向函数内传入形参(num, num1, num2)，如果num小于88，返回num1与num2的积，
否则返回num1和num2的和，调用函数传参时使用元组传参
任务
1、当num小于88，计算num1与num2的乘积，否则计算num1，num2之和
2、定义变量tuple1为(5,2,1)
3、调用函数，并打印函数返回值'''
# def seq(num, num1, num2):
#     if num < 88:
#         return num1 * num2
#     else:
#         return num1 + num2
#
#
# tuple1 = [5, 2, 1]
# print(seq(*tuple1))

'''编程练习：定义函数fun_dict实现向控制台输出如效果图所示结果，传入函数的参数类型为字典类型，请运用所学知识完成该题目。
任务
1、使用format格式化字符串，使得向控制台输出结果——小葫芦隶属于技术部，电话:18795642135, 入职日期：2017-9-23
2、创建字典dict1为{'name':'小葫芦','hiredate':'2017-9-23','tel':18795642135,'dept':'技术部'}
3、使用字典dict1作为参数传入函数fun_dict'''
# def fun_dict(name, hiredate, tel, dept):
#     print('{}隶属于{},电话：{}，入职日期：{}'.format(name, dept, tel, hiredate))
#
#
# dict1 = {'name': '小葫芦', 'hiredate': '2017-9-23', 'tel': 18795642135, 'dept': '技术部'}
# fun_dict(**dict1)


# 实例
import random

phone_numbers = '匪警[110],火警[119],急救中心[120],道路交通事故报警[122],水上求救专用电话[12395],' \
                '天气预报[12121],报时服务[12117],森林火警[12119],电力服务[95598],红十字会急救台[999],' \
                '公安短信报警[12110],通用紧急求救[112],信产部IP/网站备案[010-66411166]'

weather_str = '北京,2019年1月12日,多云,8°C,-4°C,南风3级' \
              '~上海,2019年1月12日,小雨,9°C,6°C,北风2级' \
              '~广州,2019年1月12日,阵雨转多云,22°C,15°C,持续无风向微风'


# 生成双色球
def generate_unionlotto(number):
    for j in range(0, number):
        for i in range(0, 6):
            red = random.randint(1, 33)
            print(red, end='')
        blue = random.randint(1, 16)
        print(blue)


# 号码查询
def find_phone(keyword):
    phone_list = phone_numbers.split(',')
    for i in phone_list:
        if i.find(keyword) != -1:
            print(i)


# 天气查询
def get_weather(city):
    city_list = weather_str.split('~')
    weather_date = {}
    for i in range(0, len(city_list)):
        w = city_list[i].split(',')
        # print(w)
        weather = {'name': w[0], 'date': w[1], 'weather': w[2], 'max': w[3], 'min': w[4], 'wind': w[5]}
        weather_date[weather['name']] = weather
    # print(weather_date)
    if city in weather_date:
        return weather_date.get(city)
    else:
        return {}


while True:
    print('1-双色球随机选号')
    print('2-号码百事通')
    print('3-明天天气预报')
    print('0-结束程序')
    c = input('请输入功能编号：')
    if c == '1':
        num = int(input('您要生成几注双色球号码：'))
        generate_unionlotto(num)
    elif c == '2':
        num = int(input('请输入您要查询的机构或者电话号码： '))
        find_phone(keyword=num)
    elif c == '3':
        n = input('请输入您要查询的城市：')
        w = get_weather(n)
        if 'name' in w:
            print('{date}{name}{weather}{max}/{min}{wind}'.format_map(w))
        else:
            print('未找到{0}的天气预报'.format(n))
    elif c == '0':
        break
    else:
        print('您输入的功能编号有误，请重新输入')
    print('===================================')
print('感谢您的使用，祝您生活愉快，再见。')
