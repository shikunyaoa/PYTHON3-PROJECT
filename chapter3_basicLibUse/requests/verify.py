#! python3
#-*- coding:utf-8 -*-
# author: shikunyao
# datetime: 2018/11/24 0024 17:33
# verify : 是否检查证书，默认True

import requests

response = requests.get('https://www.12306.cn', verify=False)
print(response.status_code)