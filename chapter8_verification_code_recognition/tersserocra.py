#! python3
#-*- coding:utf-8 -*-
# author: shikunyao
# datetime: 2018/11/29 0029 14:47
# 使用tesserocr识别验证码

import tesserocr
from PIL import Image

# 针对一些有干扰的图片，需要进行灰度和二值化处理
image = Image.open('CheckCode.jpg')
# 传入L即可将图片转化为灰度图像
image = image.convert('L')
# threshold：代表二值化阀值
threshold = 127
table = []
for i in range(254):
    if i < threshold:
        table.append(0)
    else:
        table.append(1)
# 先将原图转化为灰度图像，再进行二值化处理
# 传入1即可将图片进行二值化处理
image = image.point(table, '1')
result = tesserocr.image_to_text(image)
print(result)

