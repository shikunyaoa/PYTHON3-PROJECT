#! python3
#-*- coding:utf-8 -*-
# author: shikunyao
# datetime: 2018/11/28 0028 13:42
# selenium节点交互实例
from selenium import webdriver

import time

browser = webdriver.Chrome()
browser.get('https://www.taobao.com')
input = browser.find_element_by_id('q')
input.send_keys('iPhone')
time.sleep(1)
input.clear()
input.send_keys('iPad')
button = browser.find_element_by_class_name('btn-search')
button.click()