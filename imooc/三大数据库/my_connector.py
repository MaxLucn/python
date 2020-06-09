"""
# import mysql.connector
#
# # my_sql = mysql.connector.connect(
# #     host="localhost", port="3306",
# #     user="root", password="835895023",
# #     database="demo"
# # )
# #
# # cursor = my_sql.cursor()
# # sql = "SELECT empno,ename,hiredate FROM t_emp;"
# # cursor.execute(sql)
# # for i in cursor:
# #     print(i[0], i[1], i[2])
# # my_sql.close()
#
# # # SQL 预编译防止注入攻击
# # my_sql = {
# #     "host": "localhost", "port": 3306,
# #     "user": "root", "password": "835895023",
# #     "database": "news"
# # }
# # con = mysql.connector.connect(**my_sql)
# # username = "1 or True"
# # password = "1 or True"
# # sql = " SELECT COUNT(*) FROM t_user WHERE username=%s" \
# #       " AND AES_DECRYPT(UNHEX(password), '000000')=%s"
# # cursor = con.cursor()
# # cursor.execute(sql, (username, password))
# # print(cursor.fetchone()[0])
# # con.close()
#
#
# try:
#     con = mysql.connector.connect(
#         host="localhost", port="3306",
#         user="root", password="835895023",
#         database="demo"
#     )
#     con.start_transaction()
#     cursor = con.cursor()
#     sql = "INSERT INTO t_emp(empno, ename, job, mgr,hiredate,sal,comm,deptno)" \
#           "VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
#     cursor.execute(sql, (9687, "牛二", "SALESMAN", None, "1985-12-30", 2894, None, 10))
#
#     con.commit()
#
# except Exception as e:
#     if "con" in dir():
#         con.rollback()
#     print(e)
#
# finally:
#     if "con" in dir():
#         con.close()
#
"""

# """ 数据库连接池 """
# import mysql.connector.pooling
#
# # 连接数据库
# config = {
#     "host": "localhost", "port": 3306,
#     "user": "root", "password": "835895023",
#     "database": "demo"
# }
#
# try:
#     # 创建连接池
#     pool = mysql.connector.pooling.MySQLConnectionPool(
#         **config,
#         pool_size=10
#     )
#     con = pool.get_connection()
#     con.start_transaction()
#     cursor = con.cursor()
#     sql = "update t_emp set sal= sal + %s where deptno=%s"
#     cursor.execute(sql, (200, 20))
#     con.commit()
# except Exception as e:
#     # 判断连接是否存在
#     if "con" in dir():
#         con.rollback()
#     print(e)


# """ connector 删除数据 """
# import mysql.connector.pooling
#
# config = {
#     "host": "localhost", "port": 3306,
#     "user": "root", "password": "835895023",
#     "database": "demo"
# }
#
# try:
#     # 创建连接池
#     pool = mysql.connector.pooling.MySQLConnectionPool(
#         ** config,
#         pool_size=10
#     )
#     # 获得连接池的连接
#     con = pool.get_connection()
#     # 开启事务
#     con.start_transaction()
#     # 定义游标
#     cursor = con.cursor()
#     # sql 语句
#     sql = "DELETE e,d FROM t_emp e JOIN t_dept d ON e.deptno=d.deptno " \
#           "WHERE d.deptno=20"
#     # 执行 sql 语句
#     cursor.execute(sql)
#     # 提交事务
#     con.commit()
# except Exception as e:
#     # 判断链接是否存在
#     if "con" in dir():
#         # 回滚事务
#         con.rollback()
#     print(e)


# """ 使用 INSERT 语句，把部门平均底薪超过公司平均底薪的部门里的员工导入到 temp_new表里面，并且让这些员工隶属于 sales 部门 """
#
# import mysql.connector.pooling
#
# config = {
#     "host": "localhost", "port": 3306,
#     "user": "root", "password": "835895023",
#     "database": "demo"
# }
# try:
#     pool = mysql.connector.pooling.MySQLConnectionPool(
#         **config,
#         pool_size=10
#     )
#     con = pool.get_connection()
#     con.start_transaction()
#     cursor = con.cursor()
#     drop_sql = "DROP TABLE temp_new"
#     cursor.execute(drop_sql)
#     sql = "CREATE TABLE temp_new LIKE t_emp"
#     cursor.execute(sql)
#     sel_avg_sql = "SELECT AVG(sal) as avg FROM t_emp"
#     cursor.execute(sel_avg_sql)
#     temp = cursor.fetchone()
#     # 公司的平均底薪
#     sal_avg = temp[0]
#     # 分组统计每个部门的平均底薪
#     sql = "SELECT deptno FROM t_emp GROUP BY deptno HAVING avg(sal) >= %s"
#     cursor.execute(sql, [sal_avg])
#     temp = cursor.fetchall()
#     ins_new_sql = "INSERT INTO temp_new SELECT * FROM t_emp WHERE deptno IN ("
#     for index in range(len(temp)):
#         one = temp[index][0]
#         if index < len(temp) - 1:
#             ins_new_sql += str(one) + ","
#         else:
#             ins_new_sql += str(one)
#     ins_new_sql += ")"
#     print(ins_new_sql)
#     cursor.execute(ins_new_sql)
#
#     sql = "DELETE FROM t_emp WHERE deptno IN ("
#     for index in range(len(temp)):
#         one = temp[index][0]
#         if index < len(temp) - 1:
#             sql += str(one) + ","
#         else:
#             sql += str(one)
#     sql += ")"
#     print(sql)
#     cursor.execute(sql)
#     sql = "SELECT deptno FROM t_dept WHERE dname=%s"
#     cursor.execute(sql, ["SALES"])
#     deptno = cursor.fetchone()[0]
#     sql = "UPDATE temp_new SET deptno=%s"
#     cursor.execute(sql, [deptno])
#     con.commit()
# except Exception as e:
#     if "con" in dir():
#         con.rollback()
#     print(e)


""" 编写一条 insert 语句，向部门表插入两条记录， 每条记录都在部门原有最大主键值的基础上 + 10 """
import mysql.connector.pooling

config = {
    "host": "localhost", "port": 3306,
    "user": "root", "password": "835895023",
    "database": "demo"
}

try:
    pool = mysql.connector.pooling.MySQLConnectionPool(
        **config,
        pool_size=10
    )
    con = pool.get_connection()
    con.start_transaction()

    sql = "SELECT MAX(deptno) + 10, %s, %s FROM t_dept UNION " \
          "SELECT MAX(deptno) + 20, %s, %s FROM t_dept"
    cursor = con.cursor()
    cursor.execute(sql, ('A部门', '北京', 'B部门', '上海'))
    for i in cursor.fetchall():
        print(i[1], i[2])
        sql = "INSERT INTO t_dept SET deptno=%s, dname=%s, loc=%s"
        cursor.execute(sql, (i[0], i[1], i[2]))
    con.commit()

except Exception as e:
    if "con" in dir():
        con.rollback()
    print(e)
