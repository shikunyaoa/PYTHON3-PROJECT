#! python3
# urlparse() - 实现URL的识别和分段

from urllib.parse import urlparse

result = urlparse('http://www.baidu.com/index.html;user?id=5#comment')
# 返回一个ParseResult类型的对象
# schema : 协议
# netloc : 域名
# path : 访问路径
# params : 参数
# query : 查询条件
# fragment : 锚点，用于定位页面内部的下拉位置
print(type(result), result) # <class 'urllib.parse.ParseResult'> ParseResult(scheme='http', netloc='www.baidu.com', path='/index.html', params='user', query='id=5', fragment='comment')
