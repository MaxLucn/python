# birth_year = input("你出生的年份")
# age = 2019 - int(birth_year)
# print(age)

# weight_kg = input("你的体重是多少千克：")
# weight_lbs = int(weight_kg) / 0.45
# print(weight_lbs)

# first = "john"
# last = "Tom"
# message = first + '[' + last + '] is a cold'
# msg = f'{first}[{last}is a colder'
# print(message)

# course = 'python for beginner'
# print(len(course), course.upper())

# x = 2.9
# y = -72
# print(round(x), abs(y))    # 这些方法在python中的math模块中都有固定的函数，比如下面引入math模块
# import math
# print(math.ceil(2.9), math.floor(2.9))

# 情景：1、今天很热，你需要多喝水，注意避暑
#      2、今天很冷，你需要注意保暖
#      3、享受你的每一天
#      4、无论今天热还是冷都是美好的一天
# is_hot = True
# is_cold = False
# if is_hot:
#     print('今天很热，你需要多喝水，注意避暑')
# elif is_cold:
#     print('今天很冷，你需要注意保暖')
# else:
#     print('无论今天热还是冷都是美好的一天')
# print('享受你的每一天')

# 情景；知道体重，换算成英镑或者千克
# weight = int(input("Weight:"))
# unit = input("(L)bs or (K)g:")
# if unit.upper() == "L":
#     converted = weight * 0.45
#     print(f" you are {converted} kilos")
# else:
#     converted = weight / 0.45
#     print(f" you are {converted} pounds")

# 情景：猜数字游戏，有三次机会，猜中输出，"你赢了"，三次都错则没有机会。使用while循环。
# secret_number = 7
# guess_count = 0
# guess_limit = 3
# while guess_count < guess_limit:
#     guess = int(input("Guess:"))
#     guess_count += 1
#     # print("Game Over")
#     if guess == secret_number:
#         print("你赢了")
#         break
# else:
#     print("Game Over")

# command = ""
# stared = False
# while command != "quit ":
#     command = input(">  ").lower()
#     if command == "start":
#         if stared:
#             print("汽车已经准备好了")
#         else:
#             stared = True
#             print("汽车启动了，准备去哪呢？")
#     elif command == "stop":
#         if not stared:
#             print("汽车准备好停了")
#         else:
#             stared = False
#             print("汽车停好了")
#     elif command == "help":
#         print('''start--汽车启动了，准备去哪呢
# stop--汽车停好了
# quit''')
#     elif command == "quit":
#         break
#     else:
#         print("对不起，你输入的我有些看不明白。。。")


# numbers = [5, 2, 5, 2, 2]
# for number in numbers:
#     output = ''
#     for count in range(number):
#         output += 'x'
#     print(output)


# 有关列表的各种方法
# names = ['Bob', 'jim', 'Tom', 'Jerry', 'Kim']
# print(names[2:])
# print(names[-1])
# print(names[0])
# print(names[:3])

# 练习：找到列表中最大的数
# numbers = [2, 32, 4, 656, 6346, 3, 532, 55]
# my_max = numbers[0]
# for number in numbers:
#     if number > my_max:
#         my_max = number
# print(max)


# 矩阵
# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# print(matrix)
# print(matrix[0][1])
# for row in matrix:
#     for i in row:
#         print(i)

# 有关列表的各种方法
# numbers =[1, 3, 5, 6, 78, 63, 7]
# numbers.append(98)  # 给列表添加某个元素
# numbers.insert(0, 109)       # 在列表最开始的位置添加元素
# numbers.remove(63)            # 移除某一个元素
# numbers.clear()          # 清空列表，这个方法不带任何的值
# numbers.pop()              # 从列表的末尾删除
# numbers.index(78)         # 查看某一个值在列表中的位置
# numbers.sort()          # 对列表里的值进行从小到大的排序，反向排序用reserve
# print(numbers)

# 情景：删除列表中重复的元素
# numbers = [2, 3, 3, 5, 6, 7, 7, 8]
# uniques = []
# for number in numbers:
#     if number not in uniques:
#         uniques.append(number)
# print(uniques)

# 字典:每一个键对在字典中都是唯一的
# coustorm = {
#     "name": "Tom",
#     "age": "20",
#     "is_veryfied": True
# }
# print(coustorm["name"])
# print(coustorm.get("Name"))    # get方法在字典中没有要查找的的键的时候不会报错，而是返回 一个None值
# print(constorm.get("Name", "!!"))    # 后面的双感叹号是在前面的键在字典中不存在的时候自己定义一个的值，可以设置成任何值

# phone = input("phone:")
# digits_mapping = {"1": "One", "2": "Two", "3": "Three"}
# output = ""
# for i in phone:
#     output += digits_mapping.get(i, "!") + " "
# print(output)

# 情景：把标点表情换成小黄脸表情
# message = input(">")
# words = message.split(' ')
# emojis = {
#     ":)": " 😃",
#     ":(": "☹️",
# }
# output = ""
# for word in words:
#     output += emojis.get(word, word) + " "
# print(output)

#函数
# def greet_user():
#     print("Hi there")
#     print("Welcome  aboard")
#
#
# print("Start")
# greet_user()
# print("Finish")

# def greet_user(name):
#     print(f"Hi {name}")
#     print("Welcome  aboard")
#
#
# print("Start")
# greet_user("Tom")
# print("Finish")

# 把这个表情转换的代码用函数的方法实现
# message = input(">")
# words = message.split(' ')
# emojis = {
#     ":)": " 😃",
#     ":(": "☹️",
# }
# output = ""
# for word in words:
#     output += emojis.get(word, word) + " "
# print(output)
# 转换
# def emoji_converter(message):
#     words = message.split(" ")
#     emojis = {
#         ":)": " 😃",
#         ":(": "☹️",
#     }
#     output = ""
#     for word in words:
#         output += emojis.get(word, word) + " "
#     return output
#
#
# message = input(">")
# print(emoji_converter(message))


# try / except的使用
# try:
#     age = int(input("Age: "))
#     income = 2000
#     risk = income / age
#     print(age)
# except ZeroDivisionError:
#     print("零不能做被除数")
# except ValueError:
#     print("Invalid value")


# 类class      在给类命名的时候不会再像前面的列表、元组使用下划线，通常会大写首字母以达到区分的目的
#  这种命名方法成为帕斯卡惯例
# class Point:
#     def move(self):
#         print("move")
#
#     def draw(self):
#         print("draw")
#
#
# point1 = Point()
# point1.x = 10
# point1.y = 20
# print(point1.x)
# point1.draw()

#  __init__(self) 定义 方法，使用定义函数def
# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#
# point = Point(10, 20)
# print(point.x)
#
# 练习
# class Person:
#     def __init__(self, name):
#         self.name = name
#
#     def talk(self):
#         print(f"Hi, I am {self.name}")
#
#
# tom = Person("Tom")
# tom.talk()


# 类的继承
# class Mammal:              # Mammal  哺乳动物
#     def walk(self):
#         print("walk")
#
#
# # 这里Dog继承了Mammal的一切特性，如果我们在Dog下面也用到def walk。。。这些东西，如果出错就必须全都改变，继承可以避免这些
# class Dog(Mammal):
#     pass               # pass可以让代码继续下去，避免出现定义一个空类，让整个代码崩溃
#
#
# class Cat(Mammal):
#     pass


# 引入模块的练习，跟utils.py中的第一节代码是相同用处
# from utils import find_max
#
# numbers = [7, 4, 3, 8, 0]
# my_max = find_max(numbers)
# print(my_max(numbers))


#  引入包，这是组织代码的另一种方式，包更像是目录或者文件夹，里面可以包含多个模块


 # random 模块的演示，他每运行一次都会随机选择一组数
# import random
#
# numbers = [[2, 4], [3, 5], [6, 1], [7, 7]]
# num = random.choice(numbers)
# print(num)


# Path模块的演示，他可以查找当前任何类型的文件/档、目录
# from pathlib import Path
#
# path = Path()
# for item in path.glob('*.py'):
#     print(item)





