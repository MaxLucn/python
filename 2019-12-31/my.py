# import xml.etree.ElementTree as ET
# data = '''<person>
#     <name>Chuck</name>
#     <phone type = "intl">
#         +1 734 303 4456
#      </phone>
#      <email hide = "yes"/>
# </person>'''
#
# tree = ET.fromstring(data)
# print('name:', tree.find('name').text)
# print('Attr:', tree.find('email').get('hide'))

# import urllib.request, urllib.parse, urllib.error
# from bs4 import BeautifulSoup
# import ssl
#
# ctx = ssl.create_default_context()
# ctx.check_hostname = False
# ctx.verify_mode = ssl.CERT_NONE
#
# url = input('Enter - ')
# for i in range(7):
#     html = urllib.request.urlopen(url, context=ctx).read()
#     soup = BeautifulSoup(html, 'html.parser')
#     tags = soup('a')
#     tag = tags[17]
#     url = tag.get('href')
#     if i == 6:
#         print(tag.string)

import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

# url = input('Enter location: ')
url = input("http：//py4e-data.dr-chuck.net/comments_331832.xml")
print('Retrieving', url)
uh = urllib.request.urlopen(url)
data = uh.read()
print('Retrieved', len(data), 'characters')
tree = ET.fromstring(data)

results = tree.findall('comments/comment')
sum = 0
count = 0
for item in results:
    sum = sum + int(item.find('count').text)
    count += 1

print('count:',count)
print('sum:',sum)