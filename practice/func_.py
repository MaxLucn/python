# coding:utf-8
# f = open("text.txt", "r")
# text = f.readline()
# print("读取的数据是:", text)
# f.close()


# from functools import reduce
#
#
# def fn(x, y):
#     return x * 10 + y
#
#
# def charToNum(s):
#     dict = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4}
#     return dict[s]
#
#
# r1 = reduce(fn, map(charToNum, "23443"))
# print(r1)
# print(type(r1))


# a = ("imooc" != "mooc")
# b = (12 == 12.0)
# c = (19 <= 12)
# d = (18==True)
#
# print(not a)
# print(a and not d)
# print(c or d)
# print(a and d or not c)


# count = 1
# while count < 100:
#     count += 1
# print(count)

# content = "hello,everybody"
# print(content.find("o"))

# print(type(set([1, 2, 3])))
# print(type(set((1, 2, 3))))
# # print(type(set(1, 2, 3)))
# print(type({1, 2,3}))


# class Dog(object):
#     def shut(self):
#         print("wang")
#
#
# class Cat(object):
#     def shut(self):
#         print('miao')
#
#
# small_black = Cat()
# small_white = Dog()
# small_yellow = Cat()
# small_tinkle = Dog()
#
#
# print(isinstance(small_tinkle, Dog))
# print(isinstance(small_yellow, Dog))
# print(isinstance(small_white, Cat))


# def title(show=''):
#     def wrapper(func):
#         def inner():
#             print('show = %s' % show)
#             func()
#         return inner
#     return wrapper
#
#
# @title('add')
# def add():
#     print(1+1)
#
# add()


# class Imooc(object):
#     @property
#     def study(self):
#         print("_________-")
#
# if __name__ == '__main__':
#     imooc = Imooc()
#     imooc.study


# def memory(data, l = []):
#     l.append(data)
#     print(l)
#
# memory("i")
# memory('love', [])
# memory('you')


# import threading, time
#
#
# def loop():
#     n = 0
#     while n < 5:
#         print("子线程", threading.current_thread())
#         print("逆流而上")
#         time.sleep(1)
#         n += 1
#
#
# def use_thread():
#     print("主线程", threading.current_thread())
#     t = threading.Thread(target=loop(), name='loop_thread')
#     t.start()
#     t.join()
#
#
# if __name__ == '__main__':
#     use_thread()


# import threading, time
#
# balance = 0
#
#
# def change_it(n):
#     global balance
#     balance = balance + n
#     time.sleep(2)
#     balance = balance - n
#     time.sleep(1)
#     print('n:{0}---balance:{1}'.format(n, balance))
#
#
# class Change_thread(threading.Thread):
#     def __init__(self, num, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.num = num
#
#     def run(self):
#         for i in range(1000000):
#             change_it(self.num)
#
#
# if __name__ == "__main__":
#     t1 = Change_thread(66)
#     t2 = change_it(88)
#     t1.start()
#     t2.start()
#     t1.join()
#     t2.join()

#
# import os, time
# from multiprocessing import Process
#
#
# def do_sth(name):
#     print('进程的名称{0}, pid:{1}'.format(name, os.getpid()))
#     time.sleep(2)
#
#
# if __name__ == '__main__':
#     p = Process(target=do_sth, args=('my_process',))
#     p.start()
#     p.join()


# import re
#
# content = "18C5h90i3n7a0"
# pattern = re.compile(r'[a-z]', re.I)
# res = pattern.findall(content)
# print(res)

# import re
#
#
# text = 'Hello ! Python'
# pattern = re.compile(r'Python')
# res = pattern.search(text)
# print(res)

# import re
#
# text = 'Hello ! Imooc'
# pattern = re.compile(r'Imooc', re.I)
# res = pattern.search(text)
# print(res)
#
# res_match = pattern.match(text)
# print(res_match)

# import re
#
# p = re.compile('(\d)-(\d)-(\d)')
# m = p.match('2-3-1')
# print(m.groups())
# print(m.groups(0))

# import re
#
# my_str = '185ip2h30o5s9i7k01'
# pattern = re.compile(r'[a-z]+')
# result = pattern.split(my_str)
# print(result)

# import re
#
# pattern = re.compile(r"OH", re.I)
# rest = pattern.match('oh,ye')
# print(rest.string)


import time
import requests

iphone_models = {
    'MGLL3CH/A': '512GB 金色',
    'MGLA3CH/A': '128GB 银色',
    'MGLD3CH/A': '128GB 海蓝色',
    'MGLJ3CH/A': '512GB 石墨色',
    'MGLF3CH/A': '256GB 银色',
    'MGL93CH/A': '128GB 石墨色',
    'MGLE3CH/A': '256GB 石墨色',
    'MGLH3CH/A': '256GB 海蓝色',
    'MGLM3CH/A': '512GB 海蓝色',
    'MGLC3CH/A': '128GB 金色',
    'MGLG3CH/A': '256GB 金色',
    'MGLK3CH/A': '512GB 银色',
    'MGCA3CH/A': 'iPhone 12 Pro Max 512GB 银色',
    'MGC03CH/A': 'iPhone 12 Pro Max 128GB 石墨色',
    'MGC63CH/A': 'iPhone 12 Pro Max 256GB 金色',
    'MGC13CH/A': 'iPhone 12 Pro Max 128GB 银色',
    'MGC93CH/A': 'iPhone 12 Pro Max 512GB 石墨色',
    'MGC53CH/A': 'iPhone 12 Pro Max 256GB 银色',
    'MGCE3CH/A': 'iPhone 12 Pro Max 512GB 海蓝色',
    'MGC43CH/A': 'iPhone 12 Pro Max 256GB 石墨色',
    'MGC23CH/A': 'iPhone 12 Pro Max 128GB 金色',
    'MGCC3CH/A': 'iPhone 12 Pro Max 512GB 金色',
    'MGC33CH/A': 'iPhone 12 Pro Max 128GB 海蓝色',
    'MGC73CH/A': 'iPhone 12 Pro Max 256GB 海蓝色',
}

urls = {
    1: {
        'iphone12_pro_url': 'https://reserve-prime.apple.com/CN/zh_CN/reserve/A/availability.json',
        'iphone12_pro_stores_url': 'https://reserve-prime.apple.com/CN/zh_CN/reserve/A/stores.json'
    },
    2: {
        'iphone12_pro_max_url': 'https://reserve-prime.apple.com/CN/zh_CN/reserve/G/availability.json',
        'iphone12_pro_max_stores_url': 'https://reserve-prime.apple.com/CN/zh_CN/reserve/G/stores.json'
    }
}

iphone_url = 'https://reserve-prime.apple.com/CN/zh_CN/reserve/A/availability.json'
stores_url = 'https://reserve-prime.apple.com/CN/zh_CN/reserve/A/stores.json'
model = int()
while True:
    print('1、iPhone 12 Pro')
    print('2、iPhone 12 Pro Max')
    try:
        model = int(input('请输入手机型号编号:'))
    except:
        print('请输入正确的编号')
        continue
    if model == 1:
        iphone_url = urls[model]['iphone12_pro_url']
        stores_url = urls[model]['iphone12_pro_stores_url']
        break
    elif model == 2:
        iphone_url = urls[model]['iphone12_pro_max_url']
        stores_url = urls[model]['iphone12_pro_max_stores_url']
        break
    else:
        print('你的输入有误，请输入正确的编号。')
        continue

stores_list = list()
stores = requests.get(stores_url).json()
for store in stores['stores']:
    stores_list.append(store)


def get_store_info(store_code):
    for item in stores_list:
        if store_code == item['storeNumber']:
            return item


while True:
    try:
        result = requests.get(iphone_url)
    except:
        try:
            time.sleep(3)
        except KeyboardInterrupt:
            print('程序已经终止')
            exit()
        continue
    result = result.json()

    if result and 'stores' in result:
        for key, value in result['stores'].items():
            for model, has_iphone in value.items():
                store_info = get_store_info(key)
                if has_iphone['availability']['unlocked']:
                    print(
                        f"📢 有 iPhone 可以预约了 {store_info['city']} - {store_info['storeName']} - {iphone_models[model]}")
    else:
        try:
            time.sleep(3)
        except KeyboardInterrupt:
            print('程序已经终止')
            exit()
        continue

    time.sleep(3)