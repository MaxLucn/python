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

    # 删除用户
    def delete_by_id(self, id):
        try:
            con = pool.get_connection()
            con.start_transaction()
            cursor = con.cursor()
            sql = "DELETE FROM t_user WHERE id = %s"
            cursor.execute(sql, [id])
            con.commit()

        except Exception as e:
            if "con" in dir():
                con.rollback()
            print(e)

        finally:
            if "con" in dir():
                con.close()

    # 查询用户 ID
    def search_userid(self, username):
        try:
            con = pool.get_connection()
            cursor = con.cursor()
            sql = "SELECT id FROM t_user WHERE username = %s"
            cursor.execute(sql, [username])
            userid = cursor.fetchone()[0]
            # return True if role == 1 else False
            return userid
        except Exception as e:
            print(e)

        finally:
            if "con" in dir():
                con.close()
