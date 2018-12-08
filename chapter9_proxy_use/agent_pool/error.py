#! python3
#-*- coding:utf-8 -*-
# author: shikunyao
# datetime: 2018/12/2 0002 17:55

class PollEmptyError(Exception):

    def __init__(self):
        Exception.__init__(self)


    def __str__(self):
        return repr('代理池已经枯竭')