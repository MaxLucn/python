from colorama import Fore, Style
from getpass import getpass
from service.news_service import NewsService

from service.user_service import UserService
import os
import time
import sys


__user_service = UserService()
__news_service = NewsService()

while True:
    os.system("clear")
    print(Fore.LIGHTBLUE_EX, "\n\t======================")
    print(Fore.LIGHTBLUE_EX, "\n\t欢迎使用新闻管理系统")
    print(Fore.LIGHTBLUE_EX, "\n\t======================")
    print(Fore.LIGHTGREEN_EX, "\n\t1.登录系统")
    print(Fore.LIGHTGREEN_EX, "\n\t2.退出系统")
    print(Style.RESET_ALL)
    opt = input("\n\t输入操作编号:")
    if opt == "1":
        username = input("\n\t用户名:")
        password = getpass("\n\t密码:")
        result = __user_service.login(username, password)
        # 登录成功
        if result == True:
            # 查询角色
            role = __user_service.search_user_role(username)

            while True:
                os.system("clear")
                if role == "新闻编辑":
                    print(Fore.LIGHTRED_EX, "\n\t新闻编辑模块正在开发中...")
                    time.sleep(3)
                    break
                elif role == "管理员":
                    print(Fore.LIGHTGREEN_EX, "\n\t1.审批新闻")
                    print(Fore.LIGHTGREEN_EX, "\n\t2.删除新闻")
                    print(Fore.LIGHTRED_EX, "\n\tback. 返回上一层")
                    print(Style.RESET_ALL)
                    opt = input("\n\t输入操作编号：")
                    if opt == "1":
                        # 审批新闻
                        page = 1
                        while True:
                            os.system("clear")
                            count_page = __news_service.search_unreview_count_page()
                            result = __news_service.search_unreview_list(page)
                            for index in range(len(result)):
                                one = result[index]
                                print(Fore.LIGHTBLUE_EX, "\n\t%d\t%s\t%s\t%s" % (index + 1, one[1], one[2], one[3]))
                            print(Fore.LIGHTBLUE_EX, "\n\t-------------------")
                            print(Fore.LIGHTBLUE_EX, "\n\t%d/%d" % (page, count_page))
                            print(Fore.LIGHTBLUE_EX, "\n\t-------------------")
                            print(Fore.LIGHTRED_EX, "\n\tback. 返回上一层")
                            print(Fore.LIGHTRED_EX, "\n\tprev. 返回上一页")
                            print(Fore.LIGHTRED_EX, "\n\tnext. 返回下一页")
                            print(Style.RESET_ALL)
                            opt = input("\n\t输入操作编号：")
                            if opt == "back":
                                break
                            elif opt == "prev" and page > 1:
                                page -= 1
                            elif opt == "next" and page < count_page:
                                page += 1
                            elif int(opt) >= 1 and int(opt) <= 10:
                                news_id = result[int(opt) - 1][0]
                                __news_service.update_unreview_news(news_id)
                    elif opt == "2":
                        # 删除新闻
                        page = 1
                        while True:
                            os.system("clear")
                            count_page = __news_service.search_count_page()
                            result = __news_service.search_list(page)
                            for index in range(len(result)):
                                one = result[index]
                                print(Fore.LIGHTBLUE_EX, "\n\t%d\t%s\t%s\t%s" % (index + 1, one[1], one[2], one[3]))
                            print(Fore.LIGHTBLUE_EX, "\n\t-------------------")
                            print(Fore.LIGHTBLUE_EX, "\n\t%d/%d" % (page, count_page))
                            print(Fore.LIGHTBLUE_EX, "\n\t-------------------")
                            print(Fore.LIGHTRED_EX, "\n\tback. 返回上一层")
                            print(Fore.LIGHTRED_EX, "\n\tprev. 返回上一页")
                            print(Fore.LIGHTRED_EX, "\n\tnext. 返回下一页")
                            print(Style.RESET_ALL)
                            opt = input("\n\t输入操作编号：")
                            if opt == "back":
                                break
                            elif opt == "prev" and page > 1:
                                page -= 1
                            elif opt == "next" and page < count_page:
                                page += 1
                            elif int(opt) >= 1 and int(opt) <= 10:
                                news_id = result[int(opt) - 1][0]
                                __news_service.delete_by_id(news_id)
                    elif opt == "back":
                        break
        else:
            print("\n\t登录失败(3秒之后自动返回)")
            time.sleep(3)
    elif opt == "2":
        sys.exit(0)