#! python3
#-*- coding:utf-8 -*-
# author: shikunyao
# datetime: 2018/11/24 0024 14:29
# unquote - 可以进行URL解码

from urllib.parse import  unquote

url = 'https://www.baidu.com/s?wd=%E5%9D%A4%E5%9E%9A'
print(unquote(url)) # https://www.baidu.com/s?wd=坤垚
