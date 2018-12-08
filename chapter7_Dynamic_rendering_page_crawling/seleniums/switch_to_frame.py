#! python3
#-*- coding:utf-8 -*-
# author: shikunyao
# datetime: 2018/11/28 0028 14:22
# iframe: 是子Frame，相当于页面的子页面，结构和外部的网页的结构完全一致
# 操作Frame中子Frame的节点，需要使用switch_to.frame()方法来切换Frame

import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchFrameException

browser = webdriver.Firefox()
url = 'http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
browser.get(url)
browser.switch_to.frame('iframeResult')
try:
    logo = browser.find_element_by_class_name('logo')
except NoSuchFrameException:
    print("No LOGO")
browser.switch_to.parent_frame()
logo = browser.find_element_by_class_name('logo')
print(logo)
print(logo.text)