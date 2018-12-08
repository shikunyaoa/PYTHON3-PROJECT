#! python3
# -*- coding:utf-8 -*-
# author: shikunyao
# datetime: 2018/12/2 0002 16:39
# 存储模块
# 操作数据库的有序集合，分数设置，代理的获取

MAX_SCORE = 100
MIN_SCORE = 0
INITIAL_SCORE = 10
REDIS_HOST = 'localhost'
REDIS_PORT = 6379
REDIS_PASSWORD = None
REDIS_KEY = 'proxies'

import redis
from random import choice
from .error import PollEmptyError

class RedisClient(object):
    def __init__(self, host=REDIS_HOST, port=REDIS_PORT, password=REDIS_PASSWORD):
        '''
        初始化
        :param host: 地址
        :param port: 端口
        :param password: 密码
        '''
        # 初始化StrictRedis的类，简历Redis连接
        self.db = redis.StrictRedis(host=host, port=port, password=password, decode_responses=True)

    def add(self, proxy, score=INITIAL_SCORE):
        '''
        添加代理 ，设置分数为最高
        :param proxy: 代理
        :param score: 分数
        :return: 添加结果
        '''

        if not self.db.zscore(REDIS_KEY, proxy):
            return self.db.zadd(REDIS_KEY, score, proxy)

    def random(self):
        '''
        随机获取有效代理， 首先尝试获取最高分数代理，如果最高分数不存在，则按照排名获取，否则异常
        :return: 随机代理
        '''
        result = self.db.zrangebyscore(REDIS_KEY, MAX_SCORE, MAX_SCORE)
        if len(result):
            return choice(result)
        else:
            result = self.db.zrevrange(REDIS_KEY, 0, 100)
            if len(result):
                return choice(result)
            else:
                raise PollEmptyError

    def decrease(self, proxy):
        '''
        代理值减一分， 分数小于最小值，则代理移除
        :param proxy: 代理
        :return: 修改后的代理分数
        '''
        score = self.db.zscore(REDIS_KEY, proxy)
        if score and score > MIN_SCORE:
            print('代理', proxy, '当前分数', score, '减1')
            return self.db.zincrby(REDIS_KEY, proxy, -1)
        else:
            print('代理', proxy, '当前分数', score, '移除')
            return self.db.zrem(REDIS_KEY, proxy)

    def exists(self, proxy):
        '''
        判断是否存在
        :param proxy: 代理
        :return: 是否存在
        '''
        return not self.db.zscore(REDIS_KEY, proxy) == None

    def max(self, proxy):
        '''
        将代理设置为MAX_SCORE
        :param proxy: 代理
        :return: 设置结果
        '''
        print('代理', proxy, '可用， 设置为', MAX_SCORE)
        return self.db.zadd(REDIS_KEY, MAX_SCORE, proxy)

    def count(self):
        '''
        获取数量
        :return: 数量
        '''
        return self.db.zcard(REDIS_KEY)

    def all(self):
        '''
        获取全部代理
        :return: 全部代理列表
        '''
        return self.db.zrangebyscore(REDIS_KEY, MIN_SCORE, MAX_SCORE)
