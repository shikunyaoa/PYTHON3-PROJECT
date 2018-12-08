#! python3
# urljoin - 提供一个base_url作为第一个参数，将新的超链接作为第二个参数
# 该方法会分析base_url的schme,netloc和path这3个内容并对新连接缺失的部分进行补充

from urllib.parse import urljoin

print(urljoin('www.baidu.com', '?category=2#comment')) # www.baidu.com?category=2#comment

