#
#
# class Cat(object):
#
#     tag = '猫科动物'
#
#     def __init__(self, name):
#         self.name = name
#
#     @staticmethod
#     def breath():
#         """ 呼吸 """
#         print("猫都要呼吸")
#
#     @classmethod
#     def show_info(cls, name):
#         """ 显示猫的信息 """
#         # print('类的属性:{0}, 实例的属性:{1}'.format(cls.tag, cls.name))
#         return cls(name)
#         # cat = Cat(name)
#         # return cat
#
#     def show_info2(self):
#         """ 显示猫的信息 """
#         # 设计模式
#         print('类的属性:{0}, 实例的属性:{1}'.format(self.tag, self.name))
#
#
# if __name__ == '__main__':
#     # # 通过类进行使用
#     # Cat.breath()
#     # # 通过类的实例化使用
#     # cat = Cat('白白')
#     # cat.breath()
#     # cat.show_info2()
#
#     # 调用 classMethod
#     cat2 = Cat.show_info('花花')
#     cat2.show_info2()


"""根据Python中面向对象的相关知识，对客户车辆的基本信息进行录入，
并分析得出针对同类型的车辆进行合理保养的相关建议。"""


class Car(object):
    # Car类的基本车型设置，列表形式
    descrption = ['大众', '丰田', '广本', '沃尔沃', '凯迪拉克']

    def __init__(self, l, w, h, brand):
        # 重写该类的构造方法，并将参数l、w、h、brand赋值给实例对象属性
        self.L = l
        self.W = w
        self.H = h
        self.brand = brand

    # 自定义该类的基本车型检索方法

    def modeify_des(self):
        if self.descrption is True:
            return self.brand
        else:
            print("请输入您的车辆信息")

    # 自定义静态方法 提示用户：‘已完成车辆基本参数信息的录入！’

    @staticmethod
    def basic_parameters():
        print("已完成车辆信息基本参数信息的录入")

    # 自定义类方法 根据用户车辆的品牌给出相应的合理保养建议

    @classmethod
    def upkeep(cls, desc):
        if desc in cls.descrption:
            print("根据汽车保养的相关经验，{}品牌的车应于5000km/次的频率进行专业性保养".format(desc))
        else:
            print("非常抱歉！{0}品牌不在我们保养范围内".format(desc))


if __name__ == '__main__':
    car_1 = Car(4.2, 1.8, 1.5, '大众')

    # 调用实例方法：basic_parameters（）
    car_1.basic_parameters()
    # 利用if语句，调用modify_des()以判断Car的类属性description是否存在
    desc1 = car_1.modeify_des()
    if desc1 != '':
        # 若if判断条件成立 则调用类方法upkeep（）并将对应实例的brand属性传递给参数desc
        car_1.upkeep('大众')
    # 当if语句的判断条件不成立时，打印输出并提示用户：‘请正确填写相关的车辆信息’
    else:
        print("请输入填写相关的车辆信息")
    car_2 = Car(4.2, 1.8, 1.5, '保时捷')

    # 调用实例方法：basic_parameters（）

    # 利用if语句，调用modify_des()以判断Car的类属性description是否存在
    desc2 = car_1.modeify_des()
    if desc2 != '':
        # 若if判断条件成立，则调用类方法upkeep（）并将对应实例的brand属性传递给参数desc
        car_2.upkeep('保时捷')
    # 当if语句的判断条件不成立时，打印输出并提示用户：‘请正确填写相关的车辆信息’
    else:
        print("请输入填写相关的车辆信息")
