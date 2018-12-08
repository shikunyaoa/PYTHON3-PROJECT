#! python3
#*- coding:utf-8 -*-
# author: shikunyao
# datetime: 2018/11/28 0028 18:50
# 抓取淘宝商品数据

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from urllib.parse import quote
from pyquery import PyQuery as pq
import pymongo
options = webdriver.ChromeOptions()
options.add_argument("cookie='thw=cn; v=0; cna=l32FFNtHrzUCAbeeQ9smXLMz; t=dc5bfce05cae1e1389bc85aebebd90d2; cookie2=171a377451b634159ffa0ddd202e5c1d; _tb_token_=ee175be5f7e5d; unb=2877561123; sg=73c; _l_g_=Ug%3D%3D; skt=f409bad3fede9997; cookie1=BxE2q%2FsXLDHwWf8%2FhpcL7WlNOcqVlZAjfWCu3Q%2FOqxE%3D; csg=92beb6a3; uc3=vt3=F8dByR1WSpvw96qQqRE%3D&id2=UUBfReVfofZtGQ%3D%3D&nk2=0Xni5Ye81C%2FEnFBWYNHI9Q%3D%3D&lg2=W5iHLLyFOGW7aA%3D%3D; existShop=MTU0MzQwOTY4Mg%3D%3D; tracknick=%5Cu4E0D%5Cu53EA%5Cu662F%5Cu68A689325637; lgc=%5Cu4E0D%5Cu53EA%5Cu662F%5Cu68A689325637; _cc_=UtASsssmfA%3D%3D; dnk=%5Cu4E0D%5Cu53EA%5Cu662F%5Cu68A689325637; _nk_=%5Cu4E0D%5Cu53EA%5Cu662F%5Cu68A689325637; cookie17=UUBfReVfofZtGQ%3D%3D; tg=0; enc=WRBz5p4pw5gf574%2FtYqDNhUqQtoNT4owWXRh94BNvv1XA8ZXp5eBlSVgCJcc29hM%2BnZNAxivFlTFtvYwZkbWQQ%3D%3D; JSESSIONID=F1B4F3EA4B03EC20ED095808681149CD; hng=CN%7Czh-CN%7CCNY%7C156; mt=ci=0_1; swfstore=242330; x=e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0%26__ll%3D-1%26_ato%3D0; whl=-1%260%260%261543409737619; isg=BJ2drs82msLb1H7uQITwoK6drHlXEtFpf18j7l9ixPQjFrxIJwrl3HDEREu11unE; uc1=cookie14=UoTYNc%2File5YUQ%3D%3D&lng=zh_CN&cookie16=VT5L2FSpNgq6fDudInPRgavC%2BQ%3D%3D&existShop=false&cookie21=W5iHLLyFeYZ1WM9hVnmS&cookie15=UIHiLt3xD8xYTw%3D%3D&pas=0'")
options.add_argument("user-agent='Mozilla/5.0 (Windows NT 10.0; WOW64; rv:63.0) Gecko/20100101 Firefox/63.0'")
browser = webdriver.Chrome(chrome_options=options)
wait = WebDriverWait(browser, 10)
KEYWORD = 'iPad'
MONGO_URL = 'localhost'
MONGO_DB = 'taobao'
MONGO_COLLECTION = 'products'

client = pymongo.MongoClient(MONGO_URL)
db = client[MONGO_DB]
def save_to_mongo(result):
    '''
    保存到MongoDB
    :param result: 结果
    :return:
    '''
    try:
        if db[MONGO_COLLECTION].insert(result):
            print('存储到MongoDB成功')
    except Exception:
        print('存储失败')

def index_page(page):
    '''
    抓取搜索页
    :param page: 页码
    :return:
    '''
    print('正在抓取第', page,'页')
    try:

        url = 'https://s.taobao.com/search?q=' + quote(KEYWORD)
        browser.get(url)

        if page > 1:
            input = wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, '#mainsrp-pager div.form > input')))
            submit = wait.until(EC.element_to_be_clickable((
                By.CSS_SELECTOR, '#mainsrp-pager div.form > span.btn.J_Submit'
            )))
            input.clear()
            input.send_keys(page)
            submit.click()
        wait.until(
            EC.text_to_be_present_in_element((
                By.CSS_SELECTOR, '#mainsrp-pager li.item.active > span'
            ), str(page))
        )

        wait.until((EC.presence_of_element_located(By.CSS_SELECTOR, '.m-itemlist .items .item')))
        get_products()
    except TimeoutException:
        index_page(page)


def get_products():
    '''
    抓取商品数据
    :return:
    '''
    html = browser.page_source
    doc = pq(html)
    items = doc('#mainsrp-itemlist .items .item').items()
    for item in items:
        product = {
            'image': item.find('.plc .img').attr('data-src'),
            'price': item.find('.price').text(),
            'deal': item.find('.deal-cnt').text(),
            'title': item.find('.title').text(),
            'shop': item.find('.shop').text(),
            'location': item.find('.location').text()
        }
        print(product)
        save_to_mongo(product)

MAX_PAGE = 100
def main():
    '''
    遍历每一页
    :return:
    '''
    for i in range(1, MAX_PAGE + 1):
        index_page(i)

main()