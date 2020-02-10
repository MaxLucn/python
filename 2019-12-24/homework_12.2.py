# 这是12-2的作业
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
for i in range(7):
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    tag = tags[17]
    url = tag.get('href')
    if i == 6:
        print(tag.string)


# 这是一点之前的内容
# import urllib.request, urllib .parse, urllib.error
#
# hand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
# print(hand)
# # for line in hand:
# #     print(line.decode().strip()
#
# count = dict()
# for line in hand:
#     words = line.decode().strip()
#     for word in words:
#         count[word] = count.get(word, 0) + 1
# print(count)


