#! python3
#-*- coding:utf-8 -*-
# author: shikunyao
# datetime: 2018/11/24 0024 14:46

# Robots协议：称为爬虫协议，用来告诉爬虫和搜索引擎哪些页面可以抓取，哪些不可以抓取
# 通常是一个叫做robots.txt的文本文件

# robots.txt的样例
# User-agent: *
# Disallow: /
# Allow: /public/

# set_url : 用来设置robots.txt文件的链接
# read : 读取robots.txt文件并进行分析
# parse : 用来解析robots.txt文件
# can_fetch : 传入两个参数，第一个是User-agent,第二个是要抓取的URL，返回的内容是该搜索引擎是否可以抓取这个URL，返回结果是True或False
# mtime : 返回的上次抓取何分析robots.txt的时间，
# modified : 将当前时间设置为上次抓取和分析robots.txt的时间

from urllib.robotparser import RobotFileParser

rp = RobotFileParser()
rp.set_url('http://www.jianshu.com/robots.txt')
rp.read()
print(rp.can_fetch('*', "http://www.jianshu.com/p/b67554025d7d"))
