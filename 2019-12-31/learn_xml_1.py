# import xml.etree.ElementTree as ET
# 该Element类型是一个灵活的容器对象，旨在将分层数据结构存储在内存中。类型可以描述为列表和字典之间的交叉。
# 需要注意的是，该模块对恶意构建的数据是不安全的


# import xml.etree.ElementTree as ET
#
# tree = ET.parse('county_data.xml')
# root = tree.getroot()



# We provide two files for this assignment. One is a sample file where we give you the sum for your testing and the other is the actual data you need to process for the assignment.
#
# Sample data: http://py4e-data.dr-chuck.net/comments_42.xml (Sum=2553)
# Actual data: http://py4e-data.dr-chuck.net/comments_331832.xml (Sum ends with 53)
# Data Format and Approach
# The data consists of a number of names and comment counts in XML as follows:
#
# <comment>
#   <name>Matthias</name>
#   <count>97</count>
# </comment>
# You are to look through all the <comment> tags and find the <count> values sum the numbers. The closest sample code that shows how to parse XML is geoxml.py. But since the nesting of the elements in our data is different than the data we are parsing in that sample code you will have to make real changes to the code.

import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# url = input('Enter location: ')
uh = urllib.request.urlopen('http://py4e-data.dr-chuck.net/comments_331832.xml')
data = uh.read()
tree = ET.fromstring(data)
results = tree.findall('.//comment')

sum = 0
count = 0
for item in results:
    sum = sum + int(item.find('count').text)
    count += 1

print('count:', count)
print('sum:', sum)
