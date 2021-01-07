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

    # 删除用户
    def delete_by_id(self, id):
        self.__user_dao.delete_by_id(id)

    # 查询用户 ID
    def search_userid(self, username):
        userid = self.__user_dao.search_userid(username)
        return userid