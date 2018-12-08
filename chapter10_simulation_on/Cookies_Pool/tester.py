#! python3
#-*- coding:utf-8 -*-
# author: shikunyao
# datetime: 2018/12/4 0004 18:19
# 检测模块：负责遍历池中的所有Cookies，同时设置好对应的检测链接
# 用一个个Cookies去请求这个链接，如果请求成功，或者状态码合法
# 那么该Cookies有效，如果请求失败，或者无法获取正常的数据
# 那么此Cookies无效，需要将该Cookies从数据库中移除
import json

import requests

from chapter10_simulation_on.Cookies_Pool.config import TEST_URL_MAP
from chapter10_simulation_on.Cookies_Pool.db import RedisClient


class ValidTester(object):
    def __init__(self, website='default'):
        self.website = website
        self.cookies_db = RedisClient('cookies', self.website)
        self.accounts_db = RedisClient('accounts', self.website)

    def test(self, username, cookies):
        raise NotImplementedError

    def run(self):
        cookies_groups = self.cookies_db.all()
        for username, cookies in cookies_groups.items():
            self.test(username, cookies)

class WeiboValidTester(ValidTester):
    def __init__(self, website='weibo'):
        ValidTester.__init__(self, website)

    def test(self, username, cookies):
        print('正在测试Cookies', '用户名', username)
        try:
            cookies = json.loads(cookies)
        except TypeError:
            print('Cookies不合法', username)
            self.cookies_db.delete(username)
            print('删除Cookies', username)
            return
        try:
            test_url = TEST_URL_MAP[self.website]
            response = requests.get(test_url, cookies=cookies, timeout=5, allow_redirects=False)
            if response.status_code == 200:
                print('Cookies有效', username)
                print('部分测试结果', response.text[0:50])
            else:
                print(response.status_code, response.headers)
                print('Cookies失效', username)
                self.cookies_db.delete(username)
                print('删除Cookies', username)
        except ConnectionError as e:
            print('发生异常', e.args)
