#! python3
# quote - 将中文字符转化为URL编码

from urllib.parse import quote

keyword = '坤垚'
url = 'https://www.baidu.com/s?wd=' + quote(keyword)
print(url) #https://www.baidu.com/s?wd=%E5%9D%A4%E5%9E%9A
