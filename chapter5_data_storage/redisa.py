#! python3
#-*- coding:utf-8 -*-
# author: shikunyao
# datetime: 2018/11/26 0026 21:41
# 使用redis存储数据

# 连接Redis

from redis import StrictRedis

redis = StrictRedis(host='localhost', port=6379, db=0, password='')
redis.set('name', 'Bob')
print(redis.get('name'))