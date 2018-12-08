#! python3
#-*- coding:utf-8 -*-
# author: shikunyao
# datetime: 2018/11/26 0026 19:55
# 用mysql存储数据

import pymysql

db = pymysql.connect(host='localhost', user='root', password='123456', port=3306)
cursor = db.cursor()
cursor.execute('SELECT VERSION()')
# 获取第一条数据
data = cursor.fetchone()
print('Database version:', data)
cursor.execute('CREATE DATABASE spiders DEFAULT CHARACTER SET utf8')


sql = 'CREATE TABLE IF NOT EXISTS students (id VARCHAR(255) NOT NULL,' \
      'name VARCHAR(255) NOT NULL, age INT NOT NULL , PRIMARY KEY(id)'
cursor.execute(sql)


data = {
    'id': '20180000',
    'name': 'Bob',
    'age': 20
}
table = 'students'
keys = ','.join(data.keys())
values = ','.join(['%s']) * len(data)
# ON DUPLICATE KEY UPDATE ：表示如果主键已经存在，就执行更新操作，
sql = 'INSERT INTO {table}({keys}) VALUES ({values}) ON DUPLICATE KEY UPDATE '.format(table=table, keys=keys, values=values)
update = ','.join(['{key} = %s'.format(key=key) for key in data])
sql += update
try:
    if cursor.execute(sql, tuple(data.values())):
        print('Successful')
        db.commit()
except:
    print('Failed')
    db.rollback()
db.close()

