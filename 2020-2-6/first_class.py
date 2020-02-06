# class PartyAnimal:
#     x = 0                       # 这是制作PartyAnimal对象的模板
#     def party(self):
#         self.x = self.x + 1
#         print("So far", self.x)
#
# an = PartyAnimal()              #  构造一个PartyAnimal对象并存储在变量中
#
# an.party()                    #  PartyAnimal.party(an)
# an.party()
# an.party()

# 这里讨论了对象是如何构建然后丢弃的，有一下几个示例：
# 一、
# class PartyAnimal:
#     x = 0
#
#     def party(self):
#         self.x = self.x + 1
#         print("So far", self.x)
#
# an = PartyAnimal()
#
# print("Type", type(an))
# print("Dir", dir(an))

# 二、
# class PartyAnimal:
#     x = 0
#
#     def __init__(self):
#         print('I an constructed')           # constructed:建造
#
#     def party(self):
#         self.x = self.x + 1
#         print('So far', self.x)
#
#     def __del__(self):
#         print('I am destructed', self.x)     # destructed：毁了
#
# an = PartyAnimal()
# an.party()
# an.party()
# an = 42
# print('an contains', an)                     # contains:包含


# # 三、
# class PartyAnimal:
#     x = 0
#     name = ""
#     def __init__(self, z):
#         self.name = z
#         print(self.name, "constructed")
#
#     def party(self):
#         self.x = self.x + 1
#         print(self.name, "party count", self.x)
#
# s = PartyAnimal("Sally")
# s.party()
#
# j = PartyAnimal("Jim")
# j.party()
# s.party()

# 接下来，所展示的是：定义对象功能的另一种方法：继承的示例
# 一、
class PartyAnimal:
    x = 0
    name = ""
    def __init__(self, nam):
        self.name = nam
        print(self.name, "constructed")

    def party(self):
        self.x = self.x + 1
        print(self.name, "party count", self.x)

class FootballFan(PartyAnimal):
    points = 0
    def touchdown(self):
        self.points = self.points + 7
        self.party()
        print(self.name, "points", self.points)