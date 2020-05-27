import re

""" match 的演示 """
# # 将正则表达式编译
# pattern = re.compile(r'hello', re.I)
# # print(dir(pattern))
#
# # 通过 match 进行匹配
# rest = pattern.match('Hello, world')
# print(rest)
# print("string:", rest.string)


""" findall 的演示 """
# # 找出一下字符串中的数字
# my_str = 'one1sa02fjs2ah,Two,f44010n5Six2sc9gvx7zcf2452asf'
# p = re.compile(r'\d+')
# rest = p.findall(my_str)
# print(rest)
# # 使用编译的对象
# r = re.compile(r'[a-z]+', re.I)
# my_rest = r.findall(my_str)
# print(my_rest)
# # 不使用编译的对象
# all_rest = re.findall(r'[a-z]+', my_str, re.I)
# print(all_rest)

""" search 的演示 """
# content = 'hello, world!'
#
# p = re.compile(r'world')
# rest = p.search(content)
# print(rest)

""" group groups 的演示 """

# def test_group():
#     content = 'hello, world!!!'
#     p = re.compile(r'world')
#     rest = p.search(content)
#     print(rest)
#     if rest is not None:
#         # group 的使用
#         print(rest.group())
#         # groups 的使用
#         print(rest.groups())


# def test_id_card():
#     """ 身份证号码正则匹配 """
#     # p = re.compile(r'(\d{6})(\d{4})((\d{2})(\d{2}))\d{2}(\d{1})([0-9]|x)')
#     p = re.compile(r'(\d{6})(?P<year>\d{4})((?P<month>\d{2})(?P<days>\d{2}))\d{2}(\d{1})([0-9]|x)')
#
#     # 准备两个身份证号码
#     first = '620421198606152564'
#     second = '225016201312305513'
#     rest1 = p.search(first)
#     #  group 的使用。取出地区编号、 年份、 日期
#     print(rest1.group(1))
#     print(rest1.group(2))
#     print(rest1.group(5))
#     print('++++++++++++++++++++')
#     # groups 的使用
#     print(rest1.groups())
#     print('++++++++++++++++++++')
#     # groupdict 的使用
#     print(rest1.groupdict())
#
#
# if __name__ == "__main__":
#     test_group()
#     test_id_card()


""" split() 正则分割的演示 """
# my_str = 'one1sa02fjs2ah,Two,f44010n5Six2sc9gvx7zcf2452asf'
# p = re.compile(r'\d+')
# rest = p.split(my_str)
# print(rest)


""" sub() 使用正则表达式进行替换 """
my_str = 'one1sa02fjs2ah,Two,f44010n5Six2sc9gvx7zcf2452asf'
# 使用正则表达式把上面字符串中的数字替换成 '@'
p = re.compile(r'\d+')
rest = p.sub('@', my_str)
print(rest)

# 使用正则表达式替换位置
str2 = 'hello world'
p2 = re.compile(r'(\w+) (\w+)')
rest_pos = p2.sub(r'\2!!! \1', str2)
print(rest_pos)


# 替换并改变内容
def f(m):
    return m.group(2).upper() + '  ' + m.group(1)


rest_change = p2.sub(f, str2)
print(rest_change)

# 使用匿名函数进行替换 lambda
rest_lamb = p2.sub(lambda m: m.group(2).upper() + '  ' + m.group(1), str2)
print('--->', rest_lamb)
