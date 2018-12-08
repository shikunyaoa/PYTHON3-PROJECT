#! python3
# -*- coding:utf-8 -*-
# author: shikunyao
# datetime: 2018/12/2 0002 19:48
# 调度模块，将其他的模块通过多线程形式运行起来
import time

TESTER_CYCLE = 20
GETTER_CYCLE = 20
TESTER_ENABLED = True
GETTER_ENABLED = True
API_ENABLED = True
API_HOST = ''
API_PORT = ''

from multiprocessing import Process
from chapter9_proxy_use.agent_pool.api import app
from chapter9_proxy_use.agent_pool.getter import Getter
from chapter9_proxy_use.agent_pool.tester import Tester


class Scheduler():
    def schedule_tester(self, cycle=TESTER_CYCLE):
        '''
        定时测试代理
        :param cycle:
        :return:
        '''
        tester = Tester()
        while True:
            print('测试器开始运行')
            tester.run()
            time.sleep(cycle)

    def schedule_getter(self, cycle=GETTER_CYCLE):
        '''
        定时获取代理
        :param cycle:
        :return:
        '''
        getter = Getter()
        while True:
            print('开始抓取代理')
            getter.run()
            time.sleep(cycle)

    def schedule_api(self):
        '''
        开启API
        :return:
        '''
        app.run(API_HOST, API_PORT)

    def run(self):
        print('代理池开始运行')
        if TESTER_ENABLED:
            tester_process = Process(target=self.schedule_tester)
            tester_process.start()

        if GETTER_ENABLED:
            getter_process = Process(target=self.schedule_getter)
            getter_process.start()

        if API_ENABLED:
            api_process = Process(target=self.schedule_api)
            api_process.start()
