# 超文本传输协议是internet的主要应用程序层，它的发明是用来检索网页的
# HTTP是统一资源定位符或URL的协议
# 文档的概念是指向其他文档的一个链接
# HTML超文本标记语言


# 应该在下一页上单击该文本。 然后，返回，您的浏览器将读取该内容， 然后使页面显示在其中。
# 因此，它读取HTML， 解析它，有一堆规则 关于在哪里添加空白行以及所有其他这些东西， 使其看起来像您想要的方式
# 。 因此，这称为请求响应周期。 与您单击时有关， 它到达服务器的位置 取回数据，然后向您显示。 您基本上会看到点击新页面

# 典型的URL可以采用形式http://www.example.com/index.html，表示协议（http），主机名（www.example.com）和文件名（index.html）

# import socket
# my_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# my_sock.connect(('data.pr4e.org', 80))
# cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\n\n'.encode()
# my_sock.send(cmd)
#
# while True:
#     data = my_sock.recv(512)
#     if len(data) < 1:
#         break
#     print(data.decode(), end='')
# my_sock.close()
