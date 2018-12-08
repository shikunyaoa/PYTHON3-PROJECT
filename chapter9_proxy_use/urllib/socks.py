#! python3
#-*- coding:utf-8 -*-
# author: shikunyao
# datetime: 2018/12/2 0002 15:23
# 基于urllib使用socks模块设置代理

import socks
import socket
from urllib import request
from urllib.error import URLError

socks.set_default_proxy(socks.SOCKS5, '127.0.0.1', 9742)
socket.socket = socks.socksocket
try:
    response = request.urlopen('http://httpbin/org/get')
    print(response.read().decode('utf-8'))
except URLError as e:
    print(e.reason)