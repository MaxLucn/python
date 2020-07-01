from datetime import datetime
import random


# def write_file():
#     """ 写入文件 """
#     file_name = 'text.txt'
#     # 以写入的方式打开文件
#     f = open(file_name, 'w')
#     # 写入内容
#     f.write("这是测试写入文件的代码")         # 需要写入多行内容的话需要在中间加入换行符： \n  \r  \r\r  比如；
#     f.write('\n')
#     f.write("这是测试换行符有没有其作用的一句话")
#
#     # 关闭文件
#     f.close()
#
#
# def write_mult_line():
#     """ 向文件中写入多行内容"""
#     file_name = 'write_mult_line.txt'
#     with open(file_name, 'w', encoding='utf-8') as f:
#         i = ['第一行', '\n',  '第二行', '\r\r',  '第三行']
#         f.writelines(i)
#
#
# def write_user_log():
#     """记录用户的日志"""
#     rest = '用户：{0} - 访问时间 {1}'.format(random.randint(1000, 9999), datetime.now())
#     # 文件名称
#     file_name = 'write_user_log.txt'
#     with open(file_name, 'a', encoding='utf-8') as f:
#         f.write(rest)
#         f.write('\n')


def read_and_write():
    """ 先读, 再写"""
    file_name = 'read_and_write.txt'
    with open(file_name, 'r+', encoding='utf-8') as f:
        read_rest = f.read()
        # 如果里面有 i ， 就写入一行数据： 12
        # 如果里面没有 i ，就写入一行数据： 1232154564132544
        if 'i' in read_rest:
            f.write('12')
        else:
            f.write('1232154564132544')

        f.write('\n')


if __name__ == '__main__':
    # write_file()
    # write_mult_line()
    # write_user_log()
    read_and_write()
