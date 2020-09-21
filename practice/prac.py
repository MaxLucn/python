# coding:utf-8

# i = 1
# number = 0
# while i <= 8:
#     number = number + i
#     i = i + 1
# print(number)
# i = 0
# while i < 3:
#     name = "imooc"
#     if name == "imooc":
#         print("imooc-python")
#         break
#         print("imooc")
#         i += 1
# print("++++++++++")
#
# i = 1
# while i <= 100:
#     i += 1
#
#     if i % 3 == 0:
#         continue
#
#     print(i)

# i = 0
# while i < 10:
#     i += 1
#     if i ==5:
#         continue
#     print(i, end=" , ")


""" 用 for 循环及 while 循环实现九九乘法表 """


# for 循环的方法
# for i in range(1, 10):
#     for j in range(1, i + 1):
#         print("%s * %s = %s" % (i, j, i * j), end="  ")
#     print("  ")


# while 循环的方法、
# i = 0
# j = 0
#
# while i < 9:
#     i += 1
#     while j < 9:
#         j += 1
#         print("{} * {} = {}".format(i, j, i * j), end="  ")
#         if i == j:
#             j = 0
#             print("  ")
#             break


# num = 1
# count = 0
# # 循环条件
# while num <= 100:
#     # 循环体，设置条件
#     if (num % (3 * 7) != 0) and (num % 3 == 0 or num % 7 == 0):
#         count += 1
#     # 补全代码
#     num = num + 1
# print(count)


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


# def content(a, b):
#     if a > 0 and b > 0:
#         print(a % b)
#     else:
#         print(a + b)
#
#
# content(9, 2)


# text = [4, 9]
# content = text.copy()
# text.append(13)
# content.append([5, 10])
# print(content)
#
#
# print("hello" + '  ' + "Python")

# text = "Tomorrow"
# print(text.find("m", 3))

# text = "one three"
# print(text.find("e", 3, 8))

# number = input("请输入您的学号：")
# print(type(number))

# str = "http://www.imooc.com/ "
# print((str.find("im", 14)))

# print("我话费 %f 元买了台冰箱" % 2000)

# i = 0
#
# while i < 10:
#     i += 1
#     if i == 5:
#         continue
#     print(i, end=" , ")

# num = 6.0
# print(type(num))

# num1 = input("第一个数：")
# num2 = input("第二个数：")
# sum1 = num1 + num2
# print("两个数的和：", sum1)

# print("A \t B \n C \t D")

# print(6.0 == int('6'))
# print("imooc".upper() == "IMOOC")
# print("imooc ".rstrip()!='imooc')
# print(" imooc ".strip()=='Imooc')

# print(type({1,2,3}))

# class Teacher(object):
#     """  这是个教师类 """
#     company = "imooc"
#
#     def __init__(self, name, sex):
#         self.__sex = sex
#         self.name = name
#
#     def study(self):
#         print("公司名称：{}".format(self.company))
#         print("性别：{}".format(self.__sex))
#         print("教师姓名：{}".format(self.name))
#
#
# teacher = Teacher("Kim", "Man")
# teacher.study()


# class Vehicle(object):
#     # 自定义 Vehicle 类属性
#     trans_type = "SUV"
#
#     # 自定义实例的初始化方法
#     def __init__(self, speed, size):
#         self.speed = speed
#         self.size = size
#
#     # 自定义实例方法show_info，打印实例的速度和体积
#     def show_info(self):
#         print("我所属的类型:{},速度：{} km/h, 体积: {}".format(self.trans_type, self.speed, self.size))
#
#     # 自定义实例方法move,打印“我已向前移动了50米”
#     def move(self):
#         print("我已经向前移动了 50 米")
#
#     # 自定义实例方法set_speed，设置对应的速度值
#     def set_speed(self, new_speed):
#         self.new_speed = new_speed
#
#     # 自定义实例方法get_speed，打印当前的速度值
#     def get_speed(self):
#         print("我的时速是：{} km/h".format(self.new_speed))
#
#     # 自定义实例方法speed_up，实现对实例的加速
#     def speed_up(self):
#         self.speed_up = self.new_speed + 10
#         print("我的速度由{}km/h提升到了{}km/h".format(self.new_speed, self.speed_up))
#
#     # 自定义实例方法speed_down，实现对实例的减速
#     def speed_down(self):
#         self.speed_down = self.speed_up - 15
#         print("我的速度由{}km/h下降到了{}km/h".format(self.speed_up, self.speed_down))
#
#     # 自定义实例方法transport_identify，实现对实例所属类型的判断
#     def transport_identify(self):
#         if Vehicle.trans_type == "SUV":
#             print("类型匹配")
#
#         else:
#             print("类型不匹配")
#
#
# if __name__ == "__main__":
#     tool_1 = Vehicle(20, (3.6, 1.9, 1.75))
#
#     # 调用实例方法 打印实例的速度和体积
#     tool_1.show_info()
#     # 调用实例方法 实现实例的前移
#     tool_1.move()
#     tool_1.set_speed(40)
#     # 调用实例方法 打印当前速度
#     tool_1.get_speed()
#     # 调用实例方法 对实例进行加速
#     tool_1.speed_up()
#     # 调用实例方法 对实例进行减速
#     tool_1.speed_down()
#     # 调用实例方法 判断当前实例的类型
#     tool_1.transport_identify()

# 装饰器
# def check_str(func):
#     def inner(*args, **kwargs):
#         result = func(*args, **kwargs)
#         if result == "ok":
#             return "result is %s" % result
#         else:
#             return "result is %s" % result
#
#     return inner
#
#
# @check_str
# def test(data):
#     return data
#
#
# result = test(data="no")
# print(result)
#
# result = test(data="ok")
# print(result)


# def log(func):
#     def wrapper():
#         print('call %s():' % func.__name__)
#         func()
#
#     return wrapper
#
#
# @log
# def hello():
#     print("hello world")
#
#
# def now():
#     print("2020-9-15")
#
#
# now()
# hello()


# class Test(object):
#     def __init__(self, a, name):
#         self.a = a
#         self.name = name
#
#     def run(self):
#         print("run")
#
#     @classmethod
#     def jump(cls):
#         print("jump")
#
#     @staticmethod
#     def add_(a, b):
#         print("a + b 的和是:{}".format(a + b))
#
#     @property
#     def name_(self):
#         return "hello {}".format(self.name)
#
#
# t = Test("a", "Kim")
# t.run()
# Test.jump()
# Test.add_(1, 2)
#
# result = t.name_
# print(result)

# 类的继承
# class Person(object):
#     # 重写实例对象的构造方法
#     def __init__(self, name, gender):
#         self.name = name
#         self.gender = gender
#
#     # 自定义实例方法，格式化打印实例属性 name 的值
#     def speak(self):
#         print("hello, 我是%s" % self.name)
#
#     # 自定义实例方法，占位使用
#     def relation(self):
#         pass
#
#
# class Student(Person):
#     # 重写实力对象的实例化方法，并调用父类的实例化方法，实现对视力属性的赋值
#     def __init__(self, name, gender, score, major):
#         Person.__init__(self, name, gender)
#         self.score = score
#         self.major = major
#         self.stu_num = "2018014002"
#
#     # 自定义实例方法，格式化打印实例属性 __stu_num 的值
#     def speak1(self):
#         print("我的学号为 %s , 很高兴认识大家" % self.stu_num)
#
#     # 自定义实例方法，判断学号是否为既定值，并根据判断结构进行分类打印
#     def identify_stu(self):
#         if self.stu_num == "2018014002":
#             print("我的分组已经完成")
#
#         else:
#             print("请稍后，马上为你自动分组")
#
#     # 自定义实例化方法，设置实力对象的学号为传入的值
#     def set_num(self, new_num):
#         self.stu_num = new_num
#         return self.stu_num
#
#     # 自定义实例方法，判断该类是否为 Person 的子类，并进行分类打印
#     def relation(self):
#         if issubclass(Student, Person) is True:
#             print("我的父类是Person")
#
#         else:
#             print("父类正在查询中······")
#
#
# if __name__ == "__main__":
#     stu = Student("小明", "男", 90, "数学")
#     # 调用 speak 方法，打印 stu 对印的值
#     stu.speak()
#     stu.speak1()
#     # 调用实例方法，鉴别学号时候为指定值
#     stu.identify_stu()
#     # 调用实例方法，鉴别实力对象所属的类的父类
#     stu.relation()
#     print("++++++++++++++")
#     stu2 = Student('小红', '女', 89, '英语')
#     # 调用实例方法 设置stu_2的学号为'2018040625'
#     stu2.set_num("2018040625")
#     # 调用实例方法 打印stu_2对应的值
#     stu2.speak()
#     stu2.speak1()
#     # 调用实例方法 鉴别学号是否为指定值
#     stu2.identify_stu()


# # 类的多重继承
# class Point(object):
#     # 自定义Point类的构造(初始化)方法
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     # 自定义Point类对象的格式化输出函数(string())
#     def string(self):
#         print(f"{{X: {self.x}, Y: {self.y}}}")
#
#
# class Circle(Point):
#
#     # 自定义Circle类的构造(初始化)方法
#     def __init__(self, x, y, radius):
#         Point.__init__(self, x, y)
#         self.radius = radius
#
#     # 自定义Circle类对象的格式化输出函数(string())
#     def string(self):
#         print(f"该图形初始化点为: {{X:{self.x}, Y:{self.y}}};{{半径为{self.radius}}}")
#
#
# class Size(object):
#
#     # 自定义Size类的构造(初始化)方法
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     # 自定义Size类对象的格式化输出函数(string())
#     def string(self):
#         print(f"{{Width: {self.width};Height:{self.height}}}")
#
#
# class Rectangle(Point, Size):
#
#     # 自定义Rectangle类的构造(初始化)方法，并在方法中调用父类的初始化方法以完成初始化
#     def __init__(self, x, y, width, height):
#         Point.__init__(self, x, y)
#         Size.__init__(self, width, height)
#
#     # 自定义Rectangle类对象的格式化输出函数(string())
#     def string(self):
#         print(f"该图形的初始化点为： {{X: {self.x}, Y:{self.y}}}; "
#               f"长宽分别为：{{Width:{self.width}, Height:{self.height}}}")
#
#
# if __name__ == "__main__":
#     # 实例化Circle对象，圆心为（5,5），半径为8
#     c = Circle(5, 5, 8)
#     c.string()
#     # 实例化Rectangle对象，顶点位置（15,15），长和宽分别为15和15
#     r1 = Rectangle(15, 15, 15, 15)
#     r1.string()
#     # 实例化Rectangle对象，顶点位置（40,30），长和宽分别为11和14
#     r2 = Rectangle(40, 30, 11, 14)
#     r2.string


# class Test(object):
#     def __str__(self):
#         return "这是对这个类的描述"
#
#
# test = Test()
# print(test)


def test():
    try:
        number = 23 *0
    except Exception as e:
        print(e)
    finally:
        print("sss")

test()