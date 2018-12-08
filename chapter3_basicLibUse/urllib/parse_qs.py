#! python3
# parse_qs - 反序列化，将GET请求参数转化为字典

from urllib.parse import parse_qs

query = 'name=gerney&age=22'
print(parse_qs(query))  # {'name': ['gerney'], 'age': ['22']}