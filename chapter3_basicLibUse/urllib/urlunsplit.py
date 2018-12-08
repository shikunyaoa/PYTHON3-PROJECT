#! python3
# urlunsplit - 将连接各个部分组成完整连接的方法

from urllib.parse import urlunsplit

data = ['http', 'www.baidu.com', 'index.html', 'a=6', 'comment']
print(urlunsplit(data)) # http://www.baidu.com/index.html?a=6#comment
