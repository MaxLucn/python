# import xml.etree.ElementTree as ET
# 该Element类型是一个灵活的容器对象，旨在将分层数据结构存储在内存中。类型可以描述为列表和字典之间的交叉。
# 需要注意的是，该模块对恶意构建的数据是不安全的

#
# import xml.etree.ElementTree as ET
#
# tree = ET.parse('county_data.xml')
# root = tree.getroot()

# import xml.etree.ElementTree as ET
#
# # build a tree structure
# root = ET.Element("html")
#
# head = ET.SubElement(root, "head")
#
# title = ET.SubElement(head, "title")
# title.text = "Page Title"
#
# body = ET.SubElement(root, "body")
# body.set("bgcolor", "#ffffff")
#
# body.text = "Hello, World!"
#
# # wrap it in an ElementTree instance, and save as XML
# tree = ET.ElementTree(root)
# tree.write("page.xhtml")



import xml.etree.ElementTree as ET
data = '''<person>
    <name>Chuck</name>
    <phone type = "intl">
        +1 734 303 4456
     </phone>
     <email hide = "yes"/>
</person>'''

tree = ET.fromstring(data)
print('name:', tree.find('name').text)
print('Attr:', tree.find('email').get('hide'))


