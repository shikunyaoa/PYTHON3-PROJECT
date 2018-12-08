#! python3
# parse_qsl - 将GET请求参数转化为元组组成的列表

from urllib.parse import parse_qsl

query = 'name=gerney&age=22'
print(parse_qsl(query)) # [('name', 'gerney'), ('age', '22')]