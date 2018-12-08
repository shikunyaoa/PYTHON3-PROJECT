#! python3
# URLError - 异常处理类
# HTTPError是URLError的子类，专门来处理HTTP请求错误
from urllib import request, error

try:
    response = request.urlopen('https://cudqingcai.com/index.htm')
except  error.URLError  as  e:
    print(e.reason)