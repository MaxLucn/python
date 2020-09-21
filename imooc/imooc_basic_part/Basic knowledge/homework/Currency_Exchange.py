# 定义一个字典存储货币转换的四种服务
service_menu = {'1': '人民币转换美元', '2': '美元转换人民币', '3': '人民币转换欧元', '0': '结束程序'}

while True:
    print("**********欢迎使用货币转换服务系统**********")
    # 遍历字典，输出四种服务
    for k, v in service_menu.items():
        print('{}.{}'.format(k, v))
    your_choice = int(input("请您选择需要的服务："))
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

    # 当选择 1 时，进行人民币与美元的转换
    if your_choice == 1:
        print('欢迎使用人民币转换美元服务')
        # 定义一个整型变量，提示用户输入要兑换的金额
        your_money = int(input('请输入您要兑换的人民币：'))
        print('您需要转换的人民币为：', your_money, '元')
        # 定义人民币与美元的汇率
        RMB_to_US = float(your_money/7.06)
        print('兑换成美元为：{: 0.2f}$'.format(RMB_to_US))
        print('=========================================')
        continue

    # 当选择 2 时，进行美元与人民币的转换
    elif your_choice == 2:
        print('欢迎使用美元转换人民币服务：')
        your_money = int(input('请输入您要转换的美元：'))
        print('您要转换的美元为：', your_money, '$')
        # 定义美元与人民币的汇率
        US_to_RMB = float(your_money * 6.72)
        print('兑换成人民币为：{: 0.2f}¥'.format(US_to_RMB))
        print('=========================================')
        continue

    # 当选择 3 时，进行人民币与欧元的转换
    elif your_choice == 3:
        print("欢迎使用人民币转换欧元服务")
        your_money = int(input("请输入您要兑换人民币的金额："))
        print('您需要兑换的欧元为:', your_money, '欧元')
        # 定义人民币与欧元的汇率
        RMB_to_EUR = float(your_money * 0.13)
        print('兑换成人民币为:{:0.2f}¥'.format(RMB_to_EUR))
        print('=========================================')
        continue
    # 当选择 0 时退出转换系统
    elif your_choice == 0:
        print("感谢您的使用,祝您生活愉快,再见!")
        break
    # 其他选择提示用户输入有误
    else:
        print("您的输入有误，请重新输入")
