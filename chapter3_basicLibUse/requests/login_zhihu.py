#! python3
#-*- coding:utf-8 -*-
# author: shikunyao
# datetime: 2018/11/24 0024 17:13
import requests

headers = {
    'Cookie':   '_xsrf=YtP7BZIxylfGsfnSbA0WqfPvdYqdTypQ; _zap=44e59e8a-90b4-4b8e-9440-e496082add88; d_c0="AFDiaRxOkQ6PTgqv3tiFyGM38Y8QCNX4Dcw=|1543049430"; capsion_ticket="2|1:0|10:1543049520|14:capsion_ticket|44:OTllMWU0ODZjMGQwNGM4YTllZjdlYjk4M2E2NmIwYTg=|bf01ed1677db5bfa051f688653e3ad26e437ac75e79e108823c5196c34701e4c"; l_n_c=1; r_cap_id="MjNjZjcyZmExODFmNGI1Y2E2MmU3ZjMzOWMyYzAzMDM=|1543049530|ad33d4305cd8bf02f3955b386a7dac17e5438837"; cap_id="N2M2ZTg0OWZjY2NkNDJlNzk0YzZjNmEyZjlmZTg5ODk=|1543049530|4c341231595129956c33e17d4f212c25d37776ba"; l_cap_id="MWVmZTAwYjFmZDZiNGUwYjgzMzdiYzcwZGU0NTI1YTU=|1543049530|904d1af0444cb296185fed3d88542c2581f2b4fc"; n_c=1; z_c0=Mi4xRXpjdEJnQUFBQUFBVU9KcEhFNlJEaGNBQUFCaEFsVk5YRl9tWEFDTjgwYVJHS3A3VjMtTDNFSlIyalFpMjhUMXVR|1543049564|f45fb076b8c390a0d024de2374b046a74dae004f; tst=r; q_c1=393a1cc3141c41489e7729707966244d|1543049566000|1543049566000; tgw_l7_route=69f52e0ac392bb43ffb22fc18a173ee6',
    'Host': 'www.zhihu.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36'

}
r = requests.get('http://www.zhihu.com', headers=headers)
print(r.text)