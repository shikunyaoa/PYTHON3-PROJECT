#! python3
#-*- coding:utf-8 -*-
# author: shikunyao
# datetime: 2018/11/24 0024 17:39
# 超时设置

import requests

r = requests.get('https://www.taobao.com', timeout = 1)
print(r.status_code)