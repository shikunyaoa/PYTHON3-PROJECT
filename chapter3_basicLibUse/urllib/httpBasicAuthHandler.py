#! python3
# HTTPBasicAuthHandler-权限认证的handler

from urllib.request import HTTPPasswordMgrWithDefaultRealm, HTTPBasicAuthHandler, build_opener
from urllib.error import URLError

username = 'username'
password = 'password'
url = 'http://locahost:5000/'

p = HTTPPasswordMgrWithDefaultRealm()
p.add_password(None, url, username, password)
auth_handler = HTTPBasicAuthHandler(p)
operer = build_opener(auth_handler)

try:
    result = operer.open(url)
    html = result.read().decode('utf-8')
    print(html)
except URLError as e:
    print(e.reason)