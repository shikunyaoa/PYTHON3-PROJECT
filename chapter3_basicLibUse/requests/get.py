#! python3
#-*- coding:utf-8 -*-
# author: shikunyao
# datetime: 2018/11/24 0024 15:59
# get: requests中使用get()请求网页

import requests

r = requests.get('https://www.baidu.com')
print(type(r))
print(r.status_code)
print(r.text)
# 可以将返回结果是JSON格式的字符串转化为字典
print(r.json())