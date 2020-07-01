

def read_file():
    """ 读取文件 """
    file_name = 'my_file.txt'
    # 使用绝对路径
    file_path = '/Library/WebServer/Documents/python/code/imooc/Functions and modules/my_file.txt'

    # 使用普通的方式来读取文件
    with open(file_name, encoding='utf-8') as f:
        # 读取所有文件
        # test = f.read()
        # 读取指定内容
        # test = f.read(5)
        # print(test)
        # print(f.read(9))
        # # 随机读取
        # f.seek(6)
        # print(f.read(3))

        # # 按行读取
        # rest = f.readline()
        # print(rest)
        # print(f.readline(7))
        # 读取所有行
        # print(f.readlines())
        test = f.readlines(7)
        for i in test:
            print(i)
        # 关闭文件
        # f.close()


if __name__ == "__main__":
    read_file()
