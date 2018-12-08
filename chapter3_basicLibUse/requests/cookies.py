#! python3
#-*- coding:utf-8 -*-
# author: shikunyao
# datetime: 2018/11/24 0024 16:38
# request处理cookie

import requests

r = requests.get('https://www.baidu.com')
print(r.cookies)
for key, value in r.cookies.items():
    print(key + '=' + value)