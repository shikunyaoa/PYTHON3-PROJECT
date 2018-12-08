#! python3
#-*- coding:utf-8 -*-
# author: shikunyao
# datetime: 2018/11/28 0028 14:51
from selenium import webdriver

browser = webdriver.Firefox()
browser.get('https://www.zhihu.com/explore')
print(browser.get_cookies())
browser.add_cookie({'name': 'name', 'domain': 'www.zhihu.com', 'value': 'gerney'})
print(browser.get_cookies())
browser.delete_all_cookies()
print(browser.get_cookies())