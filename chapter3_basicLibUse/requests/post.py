#! python3
#-*- coding:utf-8 -*-
# author: shikunyao
# datetime: 2018/11/24 0024 16:30
# post请求

import requests

data = {'name': 'gerney', 'age': '22'}
r = requests.post('http://httpbin.org/post', data=data)
print(r.text)