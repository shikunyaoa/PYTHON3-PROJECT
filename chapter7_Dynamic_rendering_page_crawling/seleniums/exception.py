#! python3
#-*- coding:utf-8 -*-
# author: shikunyao
# datetime: 2018/11/28 0028 14:59
# 异常处理

from selenium import  webdriver
from selenium.common.exceptions import TimeoutException, NoSuchElementException
browser = webdriver.Firefox()
try:
    browser.get('https://www.baidu.com')
except TimeoutException:
    print('Time Out')
try:
    browser.find_element_by_id('hello')
except NoSuchElementException:
    print('No Element')
finally:
    browser.close()