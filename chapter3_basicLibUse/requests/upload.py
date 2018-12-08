#! python3
#-*- coding:utf-8 -*-
# author: shikunyao
# datetime: 2018/11/24 0024 16:35
# 文件上传

import requests

files = {'file': open('favicon.ico', 'rb')}
r = requests.post('http://httpbin.org/post', files=files)
print(r.text)