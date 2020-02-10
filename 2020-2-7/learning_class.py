# 一、
# 类的方法与普通的函数只有一个特别的区别，，它们必须有一个额外的第一个参数名称，按照惯例它的名称是self
#
# class Test:
#     def prt(self):
#         print(self)
#         print(self.__class__)
#
# t = Test()
# t.prt()
#
# 从结果可以看出：self代表的是类的实例，代表当前对象的地址，而self.class则指向类
# self不是python关键字，换成其他的也可以正常运行

# 二、
# 在类的内部，使用def关键字来定义一个方法，以一般函数不同，类方法必须包含参数self，且为第一个参数，self代表的类的实例
#类定义
class people:
    #定义基本属性
    name = ''
    age = 0
    # 定义私有属性，私有属性在类外部无法直接进行访问
    __weight__ = 0
    # 定义构造方法
    def __init__(self, n, a, w):
        self.name = n
        self.age = a
        self.__weight__ = w
    def speak(self):
        print("%s 说： 我 %d 岁。"%(self.name, self.age))

#实例化类
p = people('Kim', 10, 30)
p.speak()