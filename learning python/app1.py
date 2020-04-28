# def lbs_to_kg(weight):
#     return weight * 0.45
#
#
# def kg_to_lbs(weight):
#     return weight / 0.45

# 自己建议一个文件定义类、函数，然后在这里将它作为一个模块引入，更清楚的知道模块引入的方式
# import converters
# from converters import kg_to_lbs
#
# kg_to_lbs(60)
#
# print(converters.kg_to_lbs(79))


from utils import find_min

numbers = [2, 5, 6, 8, 0, 34, 81]
min = find_min(numbers)
print(min)