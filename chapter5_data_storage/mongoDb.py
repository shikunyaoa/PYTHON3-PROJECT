#! python3
#-*- coding:utf-8 -*-
# author: shikunyao
# datetime: 2018/11/26 0026 20:41
# 使用mongodb存储数据

import pymongo
from bson.objectid import ObjectId
client = pymongo.MongoClient(host='localhost', port=27017)

# 指定数据库
db = client.test

# 指定集合，类似于关系型数据库中的表
collection = db.students

# 插入数据
student = {
    'id': '20180111',
    'name': 'Jordan',
    'age': 20,
    'gerder': 'male'
}
# 官方推荐insert_one 和 insert_many
result = collection.insert_one(student)
print(result)
# 可以调用inserted_id获取插入的id
print(result.inserted_id)

# 插入
result = collection.find_one({'name': 'Jordan'})
# MongoDB在插入过程中自动添加的

print(result) # {'_id': ObjectId('5bfbebb597329a56085ba078'), 'id': '20180111', 'name': 'Jordan', 'age': 20, 'gerder': 'male'}

# 使用bson库里面的objectId可以根据ObjectId查询数据
result = collection.find_one({'_id': ObjectId('5bfbebb597329a56085ba078')})
print(result)

# 查询年龄大于20的数据
results = collection.find({'age': {'$gt': 20}})

# $regex : 匹配正则表达式
# $exists: 属性是否存在
# $type : 类型判断
# $mod : 数字模操作
# $text : 文本查询
# $where : 高级条件查询
# 使用正则匹配查询
results = collection.find({'name': {'$regex': 'M.*'}})


# 计数
count = collection.find().count()

# 排序
results = collection.find().sort('name', pymongo.ASCENDING)

# 偏移
# skip(2) :忽略前两个元素
results = collection.find().sort('name', pymongo.ASCENDING).skip(2)

# 更新
condition = {'name', 'Kavln'}
student = collection.find_one(condition)
student['age'] = 25
# 分别调用matched_count和modified_count属性，可以获得匹配的数据条数和影响的数据条数
result = collection.update_one(condition, student)

# 删除
# 调用deleted_count属性获取删除的数据条数
result = collection.remove({'name': 'Kevln'})

