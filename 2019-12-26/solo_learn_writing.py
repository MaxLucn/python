# file = open('new_file.txt', 'w')
# file.write('Some new text')
# file.close()
#
# file = open('new_file.text', 'w')
# print('Reading new contents')
# print('Finished')
# file.close()              # 当以写入模式打开文件的时时候，该文件的原内容将被删除

# msg = 'Hello World!!'
# file = open('file.text', 'w')
# amount_written = file.write(msg)
# print(amount_written)
# file.close()     # The write method returns the number of bytes written to a file, if successful.


# with open('file.text') as f:
#     print(f.read())       # 把文件替换成一个临时变量f，替换之后只可以在with语句里使用，即使出现错误，也会在with语句结尾结束

fib = {1: 1, 2: 1, 3: 2, 4: 3}
print(fib.get(4, 0) + fib.get(7, 5))
print(fib)