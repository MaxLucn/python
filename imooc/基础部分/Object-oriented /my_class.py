# class Cat(object):
#     """
#     猫科动物
#     """
#     # 类的属性
#     tag = '猫科动物'
#
#     def __init__(self, name, age):
#         # 实例化后的属性
#         self.name = name
#         self.__age = age
#
#     def set_age(self, age):
#         """
#         改变猫的年龄
#         :param age: int 年龄
#         :return: 更改后的年龄
#         """
#         self.__age = age
#
#     def catch(self):
#         print("猫会抓老鼠")
#
#     def eat(self):
#         print("猫喜欢吃鱼")
#
#     def show_info(self):
#         rest = ("{0}的年龄是{1}岁".format(self.name, self.__age))
#         print(rest)
#         return rest
#
#
# if __name__ == '__main__':
#     # 实例化小明
#     cat_balck = Cat("小明", 1.5)
#     cat_balck.eat()
#     cat_balck.show_info()
#     print("==========")
#     print(cat_balck.name)
#     """ 两个双下划线的变量默认为私有变量 """
#     # print(cat_balck.__age)
#     # 可以直接改变名称
#     cat_balck.name = "毛毛"
#     # 私有变量不可以直接被更改
#     cat_balck.__age = 3
#     cat_balck.show_info()
#     print("============")
#     # 通过放在外面的接口可以更改私有变量的值
#     cat_balck.set_age(11)
#     cat_balck.show_info()
#     print(cat_balck.tag)
#
#     """ 类的实例判断"""
#     print(isinstance(cat_balck, Cat))


# class Teacher(object):
#     """ 这是个教师类 """
#     def __init__(self):
#         pass
#
#     def study(self):
#         pass
#
#
# class Student(Teacher):
#     """ 这是个学生类 """
#     pass

""" 编程练习：自定义一个交通工具类(Vehicle)，并根据提示对该类进行进一步封装，
使其拥有工具类型、速度、体积等属性值。通过自定义实例方法实现交通工具的前移、
速度设置、获取当前速度、加速行驶、减速行驶、实例信息展示、实例类型判别等功能"""

# class Vehicle(object):
#     """ 交通工具 """
#     tag = '交通工具类'
#
#     # 自定义实例的初始化方法
#     def __init__(self, speed, size, trans_type="SUV"):
#         self.speed = speed
#         self.size = size
#         self.trans_type = trans_type
#
#     # 自定义实例方法show_info，打印实例的速度和体积
#     def show_info(self):
#         print("我所属的类型为：{0},速度：{1}km/h,体积：{2}".format(self.trans_type, self.speed, self.size))
#
#     # 自定义实例方法move,打印“我已向前移动了50米”
#     def move(self):
#         print("我已向前移动了50米")
#
#     # 自定义实例方法set_speed，设置对应的速度值
#     def set_speed(self, new_speed):
#         self.speed = new_speed
#
#     # 自定义实例方法get_speed，打印当前的速度值
#     def get_speed(self):
#         print("我的时速为:{0}km/h".format(self.speed))
#
#     # 自定义实例方法speed_up，实现对实例的加速
#     def speed_up(self):
#         self.speed = self.speed + 10
#         print("我的速度由{0}km/h提升到了{1}km/h".format(self.speed, self.speed + 10))
#
#     # 自定义实例方法speed_down，实现对实例的减速
#     def speed_down(self):
#         self.speed = self.speed - 15
#         print("我的速度由{0}km/h下降到了{1}km/h".format(self.speed, self.speed - 15))
#
#     # 自定义实例方法transport_identify，实现对实例所属类型的判断
#     def transport_identify(self):
#         if isinstance(self, Vehicle) is True:
#             print("类型匹配")
#         else:
#             print('类型不匹配')
#
#
# if __name__ == '__main__':
#     tool_1 = Vehicle(20, (3.6, 1.9, 1.75))
#     # 调用实例方法 打印实例的速度和体积
#     tool_1.show_info()
#     # 调用实例方法 实现实例的前移
#     tool_1.move()
#
#     tool_1.set_speed(40)
#     # 调用实例方法 打印当前速度
#     tool_1.get_speed()
#     # 调用实例方法 对实例进行加速
#     tool_1.speed_up()
#     # 调用实例方法 对实例进行减速
#     tool_1.speed_down()
#     # 调用实例方法 判断当前实例的类型
#     tool_1.transport_identify()

# 类的继承关系演示
# class BaseCat(object):
#     """ 猫科动物的基础类
#     """
#     tag = '猫科动物'
#
#     def __init__(self, name,):
#         self.name = name
#
#     def eat(self):
#         print("猫都要吃东西")
#
#
# class Tiger(BaseCat):
#     """
#     老虎类
#     """
#     def eat(self):
#         # 调用父类的方法
#         super(Tiger, self).eat()
#         print("更喜欢吃肉")
#
#
# class PetCat(BaseCat):
#     """
#     家猫类
#     """
#     def eat(self):
#         super(PetCat, self).eat()
#         print('还喜欢吃猫粮')
#
#
# class HuaCat(PetCat):
#     """
#     中华田园猫
#     """
#     def eat(self):
#         super(HuaCat, self).eat()
#         print('更喜欢吃小鱼干')
#
#
# if __name__ == "__main__":
#     cat = HuaCat('花花')
#     cat.eat()
#
#     # 子类的判断
#     print(issubclass(HuaCat, BaseCat))


""" 编程练习：自定义两个类Person和Student，且Student继承自Person。Person类主要描述人的姓名和性别两大基本特征。
Student类除了保持父类的基本属性之外还具有分数、主修两个公有属以及一个私有属性（学号）。
请根据上述的基本说明，对stu和stu_2两个对象的信息进行综合展示"""

# class Person(object):
#     # 重写实例对象的构造方法
#     def __init__(self, name, gender):
#         self.name = name
#         self.gender = gender
#
#     # 自定义实例方法，格式化打印实例属性女 name 的值
#     def speak(self):
#         print('hello, 我是{}'.format(self.name))
#
#     # 自定义实例方法，占位作用
#     def relation(self):
#         pass
#
#
# class Student(Person):
#     # 重写实例对象的构造方法，并调用父类构造方法，实现对实例属性的赋值
#     def __init__(self, score, major, name, gender, stu_num='2018014002'):
#         super().__init__(name, gender)
#         self.score = score
#         self.major = major
#         self.stu_num = stu_num
#
#     # 自定义实例方法，格式化打印实例属性 stu_num
#     def speak(self):
#         print('我的学号是：{},很高兴认识大家'.format(self.stu_num))
#
#     # 自定义实例方法，判断学号是否为既定值，并根据判断结构，进行分类打印
#     def identify_stu(self):
#         if self.stu_num == '2018014002':
#             print("我的分组已经完成")
#         else:
#             print("请稍后，马上为你自动分组")
#
#     # 自定义实例方法，设置实例对象的学号为传入的值
#     def set_num(self, new_num):
#         self.stu_num = new_num
#
#     # 判断该类是否为 Person 的子类，并进行分类打印
#     def relation(self):
#         result = issubclass(Student, Person)
#         if result == True:
#             print("我的父类是 Person")
#         else:
#             print("父类正在查询中")
#
#
# if __name__ == "__main_":
#     stu = Student('小明', "男", 90, "数学")
#     # 调用 speak 方法，打印 stu 对应的值
#     super(Student, stu).speak()
#     stu.speak()
#     # 调用实例方法，判断学号是否为指定值
#     stu.identify_stu()
#     # 鉴别实例对象多数的类
#     stu.relation()
#     print("*********************************")
#     stu2 = Student("小红", "女", 89, "英语")
#     # 调用实例方法，设置 stu2 的学号
#     super(Student, stu2).speak()
#     stu2.set_num("201804062")
#     stu2.speak()
#     # 鉴别学号是否为指定值
#     stu2.identify_stu()


"""圆形、长方形除了是几何学科中的基本图形之外，也还是我们日常生活中最常见的平面图形。
请根据面向对象的相关知识，将上述两种平面图形用Python语言进行表示，使得我们的程序可以正常对其使用。
"""

# class Point(object):
#     # 自定义Point类的构造(初始化)方法
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     # 自定义Point类对象的格式化输出函数(string())
#     def string(self):
#         XY = {'X': self.x, 'Y': self.y}
#         print("该图形初始化点为：{}".format(XY), end=";")
#
#
# class Circle(Point):
#     # 自定义Circle类的构造(初始化)方法
#     def __init__(self, x, y, radiuse):
#         super(Circle, self).__init__(x, y)
#         self.radiuse = radiuse
#
#     # 自定义Circle类对象的格式化输出函数(string())
#     def string(self):
#         super(Circle, self).string()
#         print("半径为：{0}".format(self.radiuse))
#
#
# class Size(object):
#     # 自定义Size类的构造(初始化)方法
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     # 自定义Size类对象的格式化输出函数(string())
#     def string(self):
#         print('Width:{0}, Height:{1}'.format(self.width, self.height))
#
#
# class Rectangle(Point, Size):
#     # 自定义Rectangle类的构造(初始化)方法，并在方法中调用父类的初始化方法以完成初始化
#     def __init__(self, x, y, width, height):
#         Point.__init__(self, x, y)
#         Size.__init__(self, width, height)
#
#     # 自定义Rectangle类对象的格式化输出函数(string())
#     def string(self):
#         xy = {'X': self.x, 'Y': self.y}
#         wh = {'width': self.width, 'height': self.height}
#         print("该图像初始点为:{0}".format(xy), end=";")
#         print("长宽分别为:{0}".format(wh))
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
#     r2.string()


"""已知People、Speaker、Student为三个自定义的类，其中People、Speaker为Student的父类。
请按照Python中多继承的方式进行编码实现下列效果图所示功能。
（注：People和Speaker中分别包含不同功能的__init__( )和speak( )方法）"""


class People(object):
    # 重写People类的构造方法，并将参数n、a赋值给实例属性name、age
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        print('{0}说：我{1}岁'.format(self.name, self.age))


class Speaker(object):
    # 重写Speaker类的构造方法，并将参数n、c、t赋值给实例属性name、career、topic
    def __init__(self, name, career, topic):
        self.name = name
        self.career = career
        self.topic = topic

    def speak1(self):
        print(f'我叫{self.name},我是一个{self.career},我演讲的主题是{self.topic}')


class Student(Speaker, People):
    def __init__(self, name, age, career, topic):
        People.__init__(self, name, age)
        Speaker.__init__(self, name, career, topic)

    pass


# s对象调用父类的speak( )方法
s = Student(name='John', age=30, career='演说家', topic='Python')
s.speak()
s.speak1()
# 格式化打印Student是否为Speaker的子类
print('Student 是否为 Speaker 的子类:', issubclass(Student, Speaker))
# 格式化打印Student是否为People的子类
print('Student 是否为 People 的子类:', issubclass(Student, People))
