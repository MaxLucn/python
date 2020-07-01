import random
import sys
import datetime


def guide_page(guide_word):
    """
    设置参数 guide_word ，记录要输出的标题文字信息
    :return: 运用字符串的格式化函数: format ，拼接 "*"号和标题文字信息
    """
    print("*************{}*************".format(guide_word))


def all_num(n):
    """
    判定指定的值是否为数字
    :return: 运用 isdigit() 方法进行判定并返回其判定结果
    """
    return n.isdigit()


def num_legal(ls):
    """ 设置列表类型的参数用于接收指定的数列 """
    # 取出序列中相等的值并进行比较, 若想等
    if int(ls[0]) == int(ls[1]):
        print("您输入的区间数字相等！请重新启动程序。")
        sys.exit()

    # 若表示数字区间其实位置的值大于数字区间终止位置的值
    elif int(ls[0]) > int(ls[1]):
        print("您输入的数字区间大小有误！请重新启动程序。")
        sys.exit()
    else:
        return 1


def set_final_num(num1, num2):
    """
    设置两个参数用于接收用户所输入区间的起始值和终止值
    :return: 运用 random 模块，返回产生区间内的随机数
    """
    ls = [num1, num2]
    # 利用内置函数 filter() 及思路分析2中的all_num(n)过滤以确保输入值全部为数字
    ls = list(filter(all_num, ls))
    if len(ls) == 2:
        if num_legal(ls) == 1:
            print("所产生的随机数字区间为:", ls)
            return random.randint(int(num1), int(num2))
    else:
        print('你输入的字符非数字字符，请重新启动！')
        sys.exit()


def check_num_legal(num):
    # 利用条件语句判断输入数值是否在指定区间
    if num < int(i) or num > int(j):
        print("对不起您输入的数字不在指定区间！！！")
        return True
    else:
        return False


def write_record(time, value):
    """
    设置参数接受玩家猜测的数字（time）和本次猜测的具体数字(value)
    :return: 根据 datetime 模块获取玩家进行每一次猜测数字输入的时间
    """
    # 使用 with 语法操作日志文件，将获取的参数和时间信息以追加方式写入日志文件
    with open('record.txt', "a+", encoding='utf-8') as f:
        f.write("{d}: 第 {t} 次您猜想的数字为：{v}\n".format(d=datetime.datetime.now(), t=time, v=value))


def main(rand1):
    temp = rand1  # 设置变量 temp 接收已经产生的随机数
    times = 0  # 记录猜测数字的次数， 默认值为0
    while True:  # 设置无限循环
        num = int(input("请输入您猜测的数字:"))
        print("*****************************")
        # if 判断核查数值函数，如果为真，条过本次循环
        if check_num_legal(num):
            continue
        # if 语句判断用户猜测的数值。相等，大于，小于的情况
        if num == temp:
            times += 1
            # 调用日志写入函数，传入猜测的次数和用户猜测的数字
            write_record(times, num)
            print('恭喜您！只用了{}次就赢得了游戏。'.format(times))
            break
        elif num > temp:
            times += 1
            write_record(times, num)
            print("Higher than the answer")
            continue
        else:
            times += 1
            write_record(times, num)
            print("Lower than the answer")
            continue


if __name__ == "__main__":
    # 调用 guide_page() 输出如效果图所示的信息
    guide_page("欢迎进入数字猜猜猜小游戏")
    # 设置两个变量(i, j) 分别接受用户输入数字区间的起始值、终止值
    i = input("数字区间起始值:")
    j = input("数字区间终止值:")
    # 调用 set_final_num() 函数得倒随机值
    rand1 = set_final_num(num1=i, num2=j)
    # 调用 main() 执行程序流程
    main(rand1)
