#! python3
#-*- coding:utf-8 -*-
# author: shikunyao
# datetime: 2018/11/28 0028 14:35
# 隐式等待：当查找节点而节点没有立即出现的时候，隐式等待蒋等待一段时间再查找DOM
# 超出设定时间后，则抛出找不到节点的异常

from selenium import webdriver

browser = webdriver.Firefox()
browser.implicitly_wait(10)
browser.get('https://www.zhihu.com/explore')
input = browser.find_element_by_class_name('zu-top-add-question')
print(input)