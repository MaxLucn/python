class PetCat(object):

    __slots__ = ('name', '__age')

    def __init__(self, name, age):
        """
        构造方法
        :param name: Cat 的名称
        :param age:  Cat 的年龄
        """
        self.name = name
        #  私有属性
        self.__age = age

    @property
    def show_info(self):
        return '我叫：{0}， 今年{1}岁'.format(self.name, self.__age)

    def __str__(self):
        return self.show_info


class HelloCat(PetCat):
    pass


if __name__ == '__main__':
    # 实例化
    # my_cat = PetCat('小飞', 1)
    # rest = my_cat.show_info
    # print(rest)
    # # 给实例添加新的属性
    # my_cat.color = '白色'
    # print(my_cat.color)
    # 给实例添加新的方法（函数）
    # my_cat.eat = eat
    # my_cat.eat()

    # 使用 slots 不允许给实例添加新的属性
    # my_cat.color = '白色'
    # print(my_cat.color)
    # 使用 slots 不允许给实例添加新的函数
    # my_cat.eat = eat
    # my_cat.eat()

    # 可以添加新的子类，然后在子类里可以随意修改它的属性和方法
    hello_cat = HelloCat('花花', 1)
    rest = hello_cat.show_info
    print(rest)
    hello_cat.color = '白色'
    print(hello_cat.color)
