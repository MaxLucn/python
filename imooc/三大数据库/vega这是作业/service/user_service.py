from db.user_dao import UserDao


class UserService:
    __user_dao = UserDao()

    # 验证用户登录
    def login(self, username, password):
        result = self.__user_dao.login(username, password)
        return result

    # 查询用户角色
    def search_user_role(self, username):
        role = self.__user_dao.search_user_role(username)
        return role