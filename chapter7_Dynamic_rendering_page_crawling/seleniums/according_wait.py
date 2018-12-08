#! python3
#-*- coding:utf-8 -*-
# author: shikunyao
# datetime: 2018/11/28 0028 14:39
# 显示等待： 指定要查找的节点，在规定时间内加载了这个节点，就返回查找的节点
# 到了规定时间依然没有加载出来该节点，则抛出超时异常

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Firefox()
browser.get('https://www.taobao.com/')
wait = WebDriverWait(browser, 10)
input = wait.until(EC.presence_of_element_located((By.ID, 'q')))
button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.btn.search')))
print(input, button)