class PetCat(object):
    def __init__(self, name, age):
        """
        构造方法
        :param name: Cat 的名称
        :param age:  Cat 的年龄
        """
        self.name = name
        #  私有属性
        self.__age = age

    # 描述符
    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if not isinstance(value, int):
            print('年龄只能是整数')
            return 0
        if value < 0 or value > 23:
            print('年龄只能介于0-23之间')
            return 0
        self.__age = value

    @property
    def show_info(self):
        return '我叫：{0}， 今年{1}岁'.format(self.name, self.age)

    def __str__(self):
        return self.show_info


if __name__ == '__main__':
    my_cat = PetCat('小飞', 1)
    rest = my_cat.show_info
    print(rest)
    # 改变猫的年龄
    my_cat.age = -23
    rest = my_cat.show_info
    print(rest)
