#! python3
# urlencode -将一个字典序列化为GET请求参数

from urllib.parse import urlencode

params = {
    'name': 'gerney',
    'age':  22
}
base_url = 'http://www.baidu.com?'
url = base_url + urlencode(params)
print(url) # http://www.baidu.com?name=gerney&age=22