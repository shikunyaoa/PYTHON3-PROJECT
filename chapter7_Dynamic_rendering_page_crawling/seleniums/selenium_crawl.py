#! python3
#-*- coding:utf-8 -*-
# author: shikunyao
# datetime: 2018/11/28 0028 13:05
# 使用selenium爬取动态渲染页面
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

browser = webdriver.Firefox()
try:
    # 请求网页
    browser.get('https://www.baidu.com')
    input = browser.find_element_by_id('kw')
    input.send_keys('Python')
    input.send_keys(Keys.ENTER)
    wait = WebDriverWait(browser, 10)
    wait.until(EC.presence_of_element_located((By.ID, 'content_left')))
    print(browser.current_url)
    print(browser.get_cookies())
    print(browser.page_source)
finally:
    browser.close()


# 查找节点
# 获取单个节点的方法
# find_element_by_id
# find_element_by_name
# find_element_by_xpath
# find_element_by_link_text
# find_element_by_partial_link_text
# find_element_by_tag_name
# find_element_by_class_name
# find_element_by_css_selector

# 单个节点,三种选择器效果一样

id = browser.find_element_by_id('id')
css_id = browser.find_element_by_css_selector('#id')
xpath_id = browser.find_element_by_xpath('//*[@id="id]")')


# 多个节点，需要用find_elements()，结果是WebElement类型
# find_element方法只能得到第一个节点，结果是列表类型，列表中的每个节点是WebElement类型


# 节点交互
# Selenium可以让浏览器模拟执行一些动作
# send_keys(): 输入文字
# clear(): 清空文字
# click(): 点击按钮
