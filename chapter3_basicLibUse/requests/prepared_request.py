#! python3
#-*- coding:utf-8 -*-
# author: shikunyao
# datetime: 2018/11/24 0024 17:46
# 将请求表示为数据结构

from requests import Request, Session

url = 'http://httpbin.org/post'
data = {
    'name': 'gerney'
}
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36'

}

s = Session()
req = Request('POST', url, data=data, headers=headers)
preped = s.prepare_request(req)
r = s.send(preped)
print(r.text)