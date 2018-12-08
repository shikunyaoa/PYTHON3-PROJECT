#! python3
#-*- coding:utf-8 -*-
# author: shikunyao
# datetime: 2018/12/2 0002 15:17
# 基于requests使用SOCKS5代理

import requests

proxy = '127.0.0.1:9742'
proxies = {
    'http': 'socks5://' + proxy,
    'https': 'socks5://' + proxy
}
try:
    response = requests.get('http://httpbin.org/get', proxies=proxies)
    print(response.text)
except requests.exceptions.ConnectionError as e:
    print('Error', e.args)
