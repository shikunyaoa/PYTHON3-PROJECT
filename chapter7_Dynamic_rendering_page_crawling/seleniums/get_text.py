#! python3
#-*- coding:utf-8 -*-
# author: shikunyao
# datetime: 2018/11/28 0028 14:19
# 获取文本值

from selenium import webdriver

browser = webdriver.Firefox()
url = 'https://www.zhihu.com/explore'
browser.get(url)
input = browser.find_element_by_class_name('zu-top-add-question')
print(input.text)
