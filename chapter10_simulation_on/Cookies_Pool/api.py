#! python3
#-*- coding:utf-8 -*-
# author: shikunyao
# datetime: 2018/12/4 0004 19:33
"""
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
              ┏┓      ┏┓
            ┏┛┻━━━┛┻┓
            ┃      ☃    ┃
            ┃  ┳┛  ┗┳   ┃
            ┃      ┻      ┃
            ┗━┓      ┏━┛
                ┃      ┗━━━┓
                ┃  神兽保佑    ┣┓
                ┃　永无BUG！   ┏┛
                ┗┓┓┏━┳┓┏┛
                  ┃┫┫  ┃┫┫
                  ┗┻┛  ┗┻┛
"""
from flask import Flask, g

from chapter10_simulation_on.Cookies_Pool.config import GENERATOR_MAP

app = Flask(__name__)

@app.route('/')
def index():
    return '<h2>Welcome to Cookie Pool System</h2>'

def get_conn():
    for website in GENERATOR_MAP:
        if not hasattr(g, website):
            setattr(g, website +'_cookies', eval('RedisClient' +'("cookies", +"' + website + '")'))
    return g

@app.route('/<website>/random')
def random(website):
    '''
    获取随机的Cookie，访问地址如/weibo/random
    :param website:
    :return:
    '''
    g = get_conn()
    cookies = getattr(g, website + '_cookies').random()
    return cookies