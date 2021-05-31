# redis数据存储到mongodb数据库
import json
from redis import Redis
from pymongo import MongoClient

# 创建redis的连接
redis_client = Redis(host='127.0.0.1', port=6379, password='123')

# 创建Mongodb的连接
mongo_client = MongoClient()
# 循环取多条数据
while True:
    # 从redis数据库中取出数据
    source, data = redis_client.blpop(['lianjia:items'])
    # print(source, data)

    print(type(data))  # <class 'bytes'>

    # 使用json转为字典格式
    change_data = json.loads(data)
    # print(change_data)
    print(type(change_data))  # <class 'dict'>

    lianjia = mongo_client.zufang.lianjia
    lianjia.insert(change_data)
