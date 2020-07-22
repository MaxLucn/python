# # from mongo_db import client
# #
# # client.school.teacher.insert_one({"name": "Tom"})
# # client.school.teacher.insert_many([
# #     {"name": "Jerry"},
# #     {"name": "Kim"}
# # ])
#
# # from mongo_db import client
# #
# # client.school.teacher.update_many({}, {"$set": {"role": ["班主任"]}})
# # client.school.teacher.update_one({"name": "Tom"}, {"$set": {"sex": "male"}})
# #
# # try:
# #     teachers = client.school.teacher.find({})
# #     for i in teachers:
# #         print(i["_id"], i["name"])
# #
# # except Exception as e:
# #     print(e)
import datetime
import math
from bson.objectid import ObjectId
from mongo_db import client
from gridfs import GridFS

db = client.school
gfs = GridFS(db, collection="book")

# # 往 mongodb 中存储文件
# file = open("/Users/luweilei/Desktop/测试存储文件到 mongodb 中的文件.pages", "rb")
# args = {"type": "pages", "keyword": "测试存储文件到 mongodb 中的文件"}
# gfs.put(file, filename="测试存储文件到 mongodb 中的文件.pages", **args)
# file.close()

# 用 find_one 在 mongodb 中查找对应的文件
book = gfs.find_one({"filename": "测试存储文件到 mongodb 中的文件.pages"})
print(book.filename)
print(book.type)
print(book.keyword)
print("%dM" % (math.ceil(book.length / 1024 / 1024)))
print("------------")

# 用 find 在 mongodb 中查找对应的文件
book = gfs.find({"type": "pages"})
for i in book:
    # UTC 转换成北京时间
    uploadDate = i.uploadDate + datetime.timedelta(hours=8)
    # 格式化日期
    uploadDate = uploadDate.strftime("%Y - %m - %d %H:%M:%S")
    print(i._id, i.filename, uploadDate)

# exists 函数判断 GridFs 是否存储文件：5f0c374f407fcb2106f9a613
rs = gfs.exists(ObjectId("5f0c374f407fcb2106f9a613"))
print(rs)
rs = gfs.exists(**{"type": "pages"})
print(rs)

# get 函数从 GridFS 中读取文件
document = gfs.get(ObjectId("5f0c40a6edf575fd73a3b93c"))
file = open("/Users/luweilei/Desktop/测试存储文件到 NOSQl 中的文件.pages", "wb")
file.write(document.read())
file.close()

# delete 函数从 GridFS 中删除文件
gfs.delete(ObjectId("5f0c3a45afeb51679194bf55"))