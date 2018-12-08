#! python3
#-*- coding:utf-8 -*-
# author: shikunyao
# datetime: 2018/11/24 0024 16:23
# 抓取二进制数据

import requests

r = requests.get('https://github.com/favicon.ico')
# 第一个参数是文件名称，第二个参数代表以二进制写的形式打开
with open('favicon.ico', 'wb') as f:
    # r.content :获得图片的二进制
    f.write(r.content)