from db.mysql_db import pool

class UserDao:
    # 验证用户登录
    def login(self, username, password):
        try:
            con = pool.get_connection()
            cursor = con.cursor()
            sql = "select count(*) from t_user where username = %s and " \
                  "aes_decrypt(unhex(password), '000000') = %s"
            cursor.execute(sql, (username, password))
            count = cursor.fetchone()[0]
            return True if count == 1 else False
        except Exception as e:
            print(e)
        finally:
            if "con" in dir():
                con.close()

    # 查询用户角色
    def search_user_role(self, username):
        try:
            con = pool.get_connection()
            cursor = con.cursor()
            sql = "SELECT r.role FROM t_user u JOIN t_role r ON u.role_id = r.id " \
                  "WHERE u.username = %s"
            cursor.execute(sql, [username])
            role = cursor.fetchone()[0]
            return role
        except Exception as e:
            print(e)

        finally:
            if "con" in dir():
                con.close()