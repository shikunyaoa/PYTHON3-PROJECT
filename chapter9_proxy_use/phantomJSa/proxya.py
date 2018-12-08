#! python3
#-*- coding:utf-8 -*-
# author: shikunyao
# datetime: 2018/12/2 0002 15:56
# 基于PhantomJS设置代理

from selenium import webdriver

service_args = [
    '--proxy=127.0.0.1:9743',
    '--proxy-type=http',
    '--proxy-auth=username:password'
]

browser = webdriver.PhantomJS(service_args=service_args)
browser.get('http://httpbin/org/get')
print(browser.page_source)