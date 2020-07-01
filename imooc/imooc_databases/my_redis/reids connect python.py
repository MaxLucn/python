# # 创建链接
# import redis
#
# r = redis.Redis(
#     host="localhost",
#     port=6379,
#     password="835895023",
#     db=0
# )


# 创建连接池
import redis

r = redis.ConnectionPool(
    host="localhost",
    port=6379,
    password="835895023",
    db=0,
    max_connections=20
)

# # 创建与关闭连接
# # 从连接池中获取的连接，不必关闭，垃圾回收的时候，连接会自动被归还到连接池
# r = redis.Redis(
#     connection_pool=pool
# )
# ...
# del r
