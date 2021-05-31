import pymongo

# 连接对象
client = pymongo.MongoClient()

db = client.schoo
# print(db)

# 获取集合
collection = db.student
# print(collection)

# 插入数据
values = {'name': '张一一', 'age': 49}
# collection.insert_one(values)

# 插入多条数据
data = [
    {'name': '李梅', 'age': 45},
    {'name': '李梅', 'age': 454},
    {'name': '李梅', 'age': 445}
]
# collection.insert_many(data)

# 修改一条数据
# collection.update_one({'name':'李四'}, {'$set':{'age': '25'}})

# 修改多条数据
# collection.update_many({'name': '李梅'}, {'$set':{'age': 21}})

# 删除一条数据
# collection.delete_one({'name': '李梅'})

# 删除多条
# collection.delete_many({'name': '李梅'})

# 查询全部数据
data = collection.find()
# for d in data:
#     print(d)

d =collection.find({'name': '李三'})
# for _ in d:
#     print(_)

# 模糊查询
c = collection.find({'name': {'$regex': '.*李.*'}})
# for cc in c:
#     print(cc)

# 对结果进行排序  升序
# result = collection.find().sort('age', pymongo.ASCENDING)
# 降序
# result = collection.find().sort('age', pymongo.DESCENDING)
# for r in result:
#     print(r)

# 获取3条数据
# result = collection.find().sort('age', pymongo.DESCENDING).limit(3)
# for r in result:
#     print(r)

# 跳过三条数据  skip()
result = collection.find().sort('age', pymongo.DESCENDING).skip(3).limit(3)
for r in result:
    print(r)