# from connect import pool
# import redis
#
# con = redis.Redis(
#     connection_pool=pool
# )
#
# try:
#     con.delete("country", "city")
#     con.mset({"country": "德国", "city": "慕尼黑"})
#     result = con.mget("country", "city")
#     for i in result:
#         print(i.decode("utf-8"))
#
#     con.delete("name")
#     con.rpush("name", "董事会", "秘书处", "财务部", "技术部")
#     con.lpop("name")
#     result_1 = con.lrange("name", 0, -1)
#     for one in result_1:
#         print(one.decode("utf-8"))
#
#     con.delete("emp")
#     con.sadd("emp", 8001, 8002, 8003)
#     con.srem("emp", 8002)
#     result_2 = con.smembers("emp")
#     for l in result_2:
#         print(l.decode("utf-8"))
#     con.zadd("keyword", {"马云": 0, "张朝阳": 0, "丁磊": 0})
#     con.zincrby("keyword", "10", "马云")
#     result_2 = con.zrevrange("keyword", 0, -1)
#     for l in result_2:
#         print(l.decode("utf-8"))
#
#     con.hmset("9527",{"name":"Tom", "sex": "male", "age": "25"})
#     con.hset("9527", "city", "New York")
#     con.hdel("9527", "age")
#     con.hexists("9527", "name")
#     result_3 = con.hgetall("9527")
#     for i in result_3:
#         print(i.decode('utf-8'), result_3[i].decode("utf-8"))
#
#     # pipeline 的演示
#     pipeline = con.pipeline()
#     pipeline.watch("9527")
#     pipeline.multi()
#     pipeline.hset("9527", "name", "Jerry")
#     pipeline.hset("9527", "age", "25")
#     pipeline.execute()
#
# except Exception as e:
#     print(e)
# finally:
#     if "pipeline" in dir():
#         pipeline.reset()
#     del con

""" 从 TXT 文档中解析学生的信息，把考试成绩超过 85 分的同学信息缓存到 redis 的哈希表中 """
# from connect import pool
# import redis
#
# con = redis.Redis(
#     connection_pool=pool
# )
#
# try:
#     file = open(file="考试成绩.txt", mode="r", encoding="utf-8")
#     data = file.read().splitlines()
#     for i in data:
#         temp = i.split(",")
#         sid = temp[0]
#         name = temp[1]
#         classno = temp[2]
#         score_1 = int(temp[3])
#         score_2 = int(temp[4])
#         score_3 = int(temp[5])
#         if score_1 >= 85 and score_2 >= 85 and score_3 >= 85:
#             con.hmset(sid, {"name": name, "classno": classno,
#                             "score_1": score_1, "score_2": score_2, "score_3": score_3})
#     print("执行成功")
#
#
# except Exception as e:
#     print(e)
# finally:
#     if "file" in dir():
#         file.close()
#     del con


""" 用  python 程序模拟 300 位观众，为 5 位嘉宾随即投票，最后按照降序排列结果"""
# from connect import pool
# import redis
# import random
#
# con = redis.Redis(
#     connection_pool=pool
# )
#
# try:
#     con.delete("ballot")
#     con.zadd("ballot", {"马云": 0, "丁磊": 0, "张朝阳": 0, "马化腾": 0, "李彦宏": 0})
#     names = ["马云", "丁磊", "张朝阳", "马化腾", "李彦宏"]
#     for i in range(300):
#         num = random.randint(0, 4)
#         name = names[num]
#         con.zincrby("ballot", 1, name)
#     result = con.zrevrange("ballot", 0, -1, "WITHSCORES")
#     for i in result:
#         print(i[0].decode("utf-8"), int(i[1]))
#
# except Exception as e:
#     print(e)
# finally:
#
#     del con


""" 线程池案例 """
# from concurrent.futures import ThreadPoolExecutor
#
#
# def say_hello():
#     print("Hello")
#
#
# executor = ThreadPoolExecutor(20)
# for i in range(0, 10):
#     executor.submit(say_hello)

""" 利用 python 多线程模拟商品秒杀过程，不可以出现超买超卖的情况。
 假设 A 商品有 50 件参与秒杀活动，10 分钟秒杀自动结束"""
from concurrent.futures import ThreadPoolExecutor
from connect import pool
import redis
import random

s = set()
while True:
    if len(s) == 1000:
        break
    num = random.randint(10000, 100000)
    s.add(num)
# print(s)
con = redis.Redis(
    connection_pool=pool
)
try:
    con.delete("kill_total", "kill_num", "kill_flag", "kill_user")
    con.set("kill_total", 50)
    con.set("kill_num", 0)
    con.set("kill_flag", 1)
    con.expire("kill_flag", 600)
except Exception as e:
    print(e)
finally:
    del con

executor = ThreadPoolExecutor(200)


def buy():
    connection = redis.Redis(
        connection_pool=pool
    )
    pipeline = connection.pipeline()
    try:
        if connection.exists("kill_flag") == 1:
            pipeline.watch("kill_num", "kill_user")
            total = int(pipeline.get("kill_total").decode("utf-8"))
            num = int(pipeline.get("kill_num").decode("utf-8"))
            if num < total:
                pipeline.multi()
                pipeline.incr("kill_num")
                user_id = s.pop()
                pipeline.rpush("kill_user", user_id)
                pipeline.execute()
    except:
        pass
    finally:
        if "pipeline" in dir():
            pipeline.reset()
        del con


for i in range(0, 1000):
    executor.submit(buy)
print("秒杀结束")
