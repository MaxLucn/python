from connect import pool
import redis

con = redis.Redis(
    connection_pool=pool
)

con.set("country", "英国")
con.set("city", "伦敦")
city = con.get("city").decode("utf-8")
con.expire("city", 5)
# print(city)

con.delete("country", "city")
con.mset({"country": "德国", "city": "柏林"})
result = con.mget("country", "city")
for i in result:
    print(i.decode("utf-8"))


del con
