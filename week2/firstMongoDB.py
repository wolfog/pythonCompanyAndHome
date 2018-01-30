# -*- coding:utf-8 -*-
# _authur_ = 'wolfog
# purpose:新添加一个数据库，新添加一个表，并且向表中添加1000条数据
from pymongo import MongoClient

host = "localhost"
port = 27017
client = MongoClient(host, port)
db = client['first']
coll = db['firstC']
for i in range(1000):
    # print(i)
    coll.insert_one({'name': 'name' + str(i), 'value': i})
for item in coll.find():
    print(type(item))
    print(item)
    if ({'value': {'$gte': 995}}):  # 这样写的形式与if(item['value']>=995)等价
        print(item['value'])
