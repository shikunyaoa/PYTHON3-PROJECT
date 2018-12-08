#! python3
# -*- coding:utf-8 -*-
# author: shikunyao
# datetime: 2018/12/2 0002 18:43
# 动态调用所有以crawl开头的方法，然后获取抓取到的代理

from .db import RedisClient
from .crawler import Crawler

POOL_UPPER_THRESHOLD = 10000


class Getter():
    def __init__(self):
        self.redis = RedisClient()
        self.crawler = Crawler()

    def is_over_threshold(self):
        '''
        判断是否达到了代理池限制

        '''
        if self.redis.count() >= POOL_UPPER_THRESHOLD:
            return True
        else:
            return False

    def run(self):
        print('获取器开始执行')
        if not self.is_over_threshold():
            for callbakc_lable in range(self.crawler.__CrawlFuncCount__):
                callback = self.crawler.__CrawlFunc__[callbakc_lable]
                proxies = self.crawler.get_proxies(callback)
                for proxy in proxies:
                    self.redis.add(proxy)
