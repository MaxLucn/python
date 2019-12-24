# ord方法可以查看某个字符对应的ASC-II值
# print(ord('\n'))                        # \n转义字符是一个整体
# print(ord('E'))
# print(ord('e'))


# urllib模块包括的一些设计互联网的工具函数：
#    函数urlencode把一个字典的键-值对转换为查询字符串用于url
#    函数quote与quote_plus编码正常字符串
#    函数unquote与unquote_plus把url编码的字符串转换为平常文本


# import urllib.request, urllib.parse, urllib.error
# hand = urllib.request.urlopen('http//data.pr4e.org/romeo.txt')
# for line in hand:
#     print(line.decode(), strip())

# import urllib.request, urllib.parse, urllib.error
# hand = urllib.request.urlopen('http//data.pr4e.org/romeo.txt')
#
# counts = dict()
# for line in hand:
#     words = line.decode().split()
#     for word in words:
#         counts[word] = counts.get(word, 0) + 1
# print(counts)

# import urllib.request
# from bs4 import BeautifulSoup
# import ssl

# import urllib.request, urllib.parse, urllib.error
#
# hand = urllib.request.urlopen('http://data.pr4e.org/remeo.txt')
# for line in hand:
#     print(line.decode().strip())


# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

# import urllib.request, urllib.parse, urllib.error
# from bs4 import BeautifulSoup
# import ssl
#
# # Ignore SSL certificate errors
# ctx = ssl.create_default_context()
# ctx.check_hostname = False
# ctx.verify_mode = ssl.CERT_NONE
#
# url = input('Enter - ')
# html = urllib.request.urlopen(url, context=ctx).read()
# soup = BeautifulSoup(html, 'html.parser')
#
# # Retrieve all of the anchor tags
# tags = soup('a')
# for tag in tags:
#     print(tag.get('href', None))


# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

# from urllib.request import urlopen
# from bs4 import BeautifulSoup
# import ssl
#
# # Ignore SSL certificate errors
# ctx = ssl.create_default_context()
# ctx.check_hostname = False
# ctx.verify_mode = ssl.CERT_NONE
#
# url = input('Enter - ')
# html = urlopen(url, context=ctx).read()
# soup = BeautifulSoup(html, "html.parser")
#
# # Retrieve all of the anchor tags
# my_sum = 0
# tags = soup('span')
# for tag in tags:
#     # Look at the parts of a tag
#     my_num = int(tag.contents[0])
#     my_sum += my_num
# print(my_sum)


# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSl certificate errors
cts = ssl.create_default_context()
cts.check_hostname = False
cts.verify_mode = ssl.CERT_NONE

# url = input('Enter - ')
url = 'http://py4e-data.dr-chuck.net/known_by_Fikret.html'
html = urllib.request.urlopen(url, context=cts).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
tags = soup('3')
for tag in tags:
    print(tag.get('href', None))


# urllib.quote(string[,safe])对字符串进行编码。参数safe指定了不需要编码的字符
# urllib.unquote(string)对字符串进行编码
# urllib.quote_plus(sting[,safe])与urllib.quote类似，但这个方法用'+'来替换' '，而quote用'%20'来代替。
# urllib.unquote_plus(string)对字符串进行解码
# urllib.urlencode(query[,doseq])将dict或者包含两个元素的元组列表转换成url参数。
# 例如字典{'name':'wklken', 'pwd':'123'}将被转换为"name=wklken&pwd= 123"
# urllib.pathname2rul(path)将本地路径转换成url路径
# urllib.url2pathname(path)将url路径转换成本地路径
# urllib.urlretrieve(url[,filename[,reporthook[,data]]])下载远程数据到本地
# filename：指定保存到本地的路径（若未指定，urllib生成一个临时文件保存数据）