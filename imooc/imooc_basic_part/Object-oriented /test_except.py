# class ApiException(Exception):
#     """ 我的自定义异常 """
#     err_code = ''
#     err_msg = ''
#
#     def __init__(self, err_code=None, err_msg=None):
#         self.err_code = self.err_code if self.err_code else err_code
#         self.err_msg = self.err_msg if self.err_msg else err_msg
#
#     def __str__(self):
#         return 'Error: {0} - {1}'.format(self.err_code, self.err_msg)
#
#
# class InvalidCtrlExec(ApiException):
#     """ 当参数不合法是触发
#     40001 invalid credential   不合法的调用凭证
#     """
#     err_code = '40001'
#     err_msg = "不合法的调用凭证"
#
#
# # def __str__(self):
# #     return 'Error: {0} - {1}'.format(self.err_code, self.err_msg)
#
#
# def divide(num1, num2):
#     """ 除法的实现 """
#     # 两个书必须为整数
#     if not isinstance(num1, int) or not isinstance(num2, int):
#         raise InvalidCtrlExec('40000', '两个参数必须都是整数')
#     # 除数不能为0
#     if num2 == 0:
#         raise ApiException('40000', '除数不能为0')
#     return num1 / num2
#
#
# if __name__ == "__main__":
#     try:
#         rest = divide(5, 0)
#         print(rest)
#     except ApiException as err:
#         print('出错了')
#         print(err)


# 抛出异常及异常的传递
# 如果在异常产生的地方不捕获，那么它会一层层的往上传递
def my_for():
    """ 定义一个 for 循环的函数 """
    for i in range(1, 20):
        if i == 5:
            # 抛出异常
            raise MemoryError('测试抛出异常')
        print(i)


def do_sth():
    """ 再定义一个函数，调用 my_for 函数 """
    my_for()


def test_trans():
    try:
        do_sth()
    except MemoryError as e:
        print("我在最外层捕获到了{0}".format(e))


if __name__ == '__main__':
    test_trans()
