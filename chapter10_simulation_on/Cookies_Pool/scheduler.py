#! python3
#-*- coding:utf-8 -*-
# author: shikunyao
# datetime: 2018/12/4 0004 19:48
"""
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
              ┏┓      ┏┓
            ┏┛┻━━━┛┻┓
            ┃      ☃      ┃
            ┃  ┳┛  ┗┳  ┃
            ┃      ┻      ┃
            ┗━┓      ┏━┛
                ┃      ┗━━━┓
                ┃  神兽保佑    ┣┓
                ┃　永无BUG！   ┏┛
                ┗┓┓┏━┳┓┏┛
                  ┃┫┫  ┃┫┫
                  ┗┻┛  ┗┻┛
"""
# 调度模块： 将几个模块配合运行起来，驱动几个模块定时运行
import time

from multiprocessing import Process

from chapter10_simulation_on.Cookies_Pool.api import app
from chapter10_simulation_on.Cookies_Pool.config import CYCLE, TESTER_MAP, GENERATOR_MAP, API_HOST, API_PORT, \
    API_PROCESS, GENERATOR_PROCESS, VALID_PROCESS


class Scheduler(object):
    @staticmethod
    def valid_cookie(cycle=CYCLE):
        while True:
            print('Cookies检测进程开始执行')
            try:
                for website, cls in TESTER_MAP.items():
                    tester = eval(cls + '(website="' + website + '")')
                    tester.run()
                    print('Cookies检测开始')
                    del tester
                    time.sleep(cycle)
            except Exception as e:
                print(e.args)

    @staticmethod
    def generate_cookie(cycle=CYCLE):
        while True:
            print('Cookies生成进程开始运行')
            try:
                for website, cls in GENERATOR_MAP.items():
                    generator = eval(cls +'(website="'+website+'")')
                    generator.run()
                    print('Cookies生成开始')
                    del generator
                    time.sleep(cycle)
            except Exception as e:
                print(e.args)

    @staticmethod
    def api():
        print('API接口开始运行')
        app.run(host=API_HOST, port=API_PORT)

    def run(self):
        if API_PROCESS:
            api_process = Process(target=Scheduler.api)
            api_process.start()
        if GENERATOR_PROCESS:
            generator_process = Process(target=Scheduler.generate_cookie)
            generator_process.start()
        if VALID_PROCESS:
            valid_process = Process(target=Scheduler.valid_cookie)
            valid_process.start()