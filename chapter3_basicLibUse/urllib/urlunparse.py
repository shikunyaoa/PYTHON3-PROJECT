#! python3
# urlunparse - 实现了URL的构造

from urllib.parse import urlunparse

data = ['http', 'www.baidu.com', 'index.html', 'user', 'a=6', 'comment']
print(urlunparse(data)) # http://www.baidu.com/index.html;user?a=6#comment
