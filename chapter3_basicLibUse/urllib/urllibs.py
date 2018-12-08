#! python3
# urllib - HTTP request library of Python

# 包含四个模块
# request: 最基本的HTTP请求模块，用来模拟发送请求
# error : 异常处理模块
# parse : 一个工具模块，提供了许多URL处理方法，比如拆分
# robotparser: 主要用来识别网站的robot.txt文件，然后判断哪些网站可以爬，哪些网站不可以爬

import urllib.request

response = urllib.request.urlopen('https://www.python.org')
# print(response.read().decode('utf-8'))
print(response.status)
print(response.getheaders())