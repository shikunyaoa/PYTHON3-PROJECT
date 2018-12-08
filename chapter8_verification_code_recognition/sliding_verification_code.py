#! python3
#-*- coding:utf-8 -*-
# author: shikunyao
# datetime: 2018/11/29 0029 18:33
# 滑动验证码识别
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
from selenium.webdriver import ActionChains

EMAIL = '243677061@qq.com'
PASSWORD = 'shi19950815@qq'

class CrackGeetest():
    def __init__(self):
        self.url = 'https://acount.geetest.com/login'
        self.browser = webdriver.Chrome()
        self.wait = WebDriverWait(self.browser, 20)
        self.email = EMAIL
        self.password = PASSWORD



    # 模拟点击
    def get_geetest_button(self):

        button = self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'geetest_radar_tip')))
        return button

    # 识别缺口
    # 获取前后两张比对图片，二者不一致的地方即为缺口

    def get_position(self):
        '''
        获取验证码位置
        :return: 验证码位置元组
        '''
        img = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'geetest_canvas_img')))
        time.sleep(2)
        location = img.location
        size = img.size
        top, bottom, left, right = location['y'], location['y'] + size['height'], location['x'], location['x'] + size['width']
        return (top, bottom, left, right)

    def get_geetest_image(self):
        '''
        获取验证码图片
        :return: 图片对象
        '''
        top, bottom, left, right = self.get_position()
        print('验证码位置', top, bottom, left, right)
        # 获取网页截图
        screenshot = self.get_screenshot()
        # 调用了crop()方法将图片裁切出来
        captcha = screenshot.crop((left, top, right, bottom))
        return captcha

    def get_slider(self):
        '''
        获取滑块
        :return: 滑块对象
        '''
        slider = self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'geetest_slider_button')))
        return slider


    def is_pixel_equal(self, image1, image2, x, y):
        '''
        判断两个像素是否相同
        :param image1: 图片1
        :param image2: 图片2
        :param x: 位置x
        :param y: 位置y
        :return: 像素是否相同
        '''

        # 去两个图片的像素点
        pixel1 = image1.load()[x, y]
        pixel2 = image2.load()[x, y]
        threshold = 60
        if abs(pixel1[0] - pixel2[0]) < threshold and abs(pixel1[1] - pixel2[1]) < threshold and abs(pixel1[2] - pixel2[2]) < threshold:
            return True
        else:
            return False

    def get_gep(self, image1, image2):
        '''
        获取缺口偏移量
        :param image1: 不带缺口图片
        :param image2: 带缺口图片
        :return:
        '''
        # 缺口的位置一般会在滑块的右侧，直接设置遍历的横坐标为60
        left = 60
        for i in range(left, image1.size[0]):
            for j in range(image1.size[1]):
                if not self.is_pixel_equal(image1, image2, i, j):
                    left = i
                    return left
        return left

    def get_track(self, distance):
        '''
        根据偏移量获取移动轨迹
        :param distance: 偏移量
        :return: 移动轨迹
        '''
        # 移动轨迹
        track = []
        # 当前位置
        current = 0
        # 减速阀值,即加速到什么位置开始减速
        # 即模拟前4/5路程是加速过程
        mid = distance * 4 / 5
        # 计算间隔
        t = 0.2
        # 初速度
        v = 0

        while current < distance:
            if current < mid:
                # 加速度为正2
                a = 2
            else:
                # 加速度为 -3
                a = -3

            # 初速度为v0
            v0 = v
            # 当前速度v = v0 + at
            v = v0 + a * t
            # 移动距离 x = v0t + 1/2 * a * t*2
            move = v0 * t + 1/2 * a * t * t
            # 当前位移
            current += move
            # 加入轨迹
            track.append(round(move))
        return track

    def move_to_gep(self, slider, tracks):
        '''
        运动滑块到缺口处
        :param slider: 滑块
        :param tracks: 轨迹
        :return:
        '''
        # click_and_hold:按住拖动
        ActionChains(self.browser).click_and_hold(slider).perform()
        for x in tracks:
            # move_by_offset: 移动此位移
            ActionChains(self.browser).move_by_offset(xoffset=x, yoffset=0).perform()
        time.sleep(0.5)
        # 调用release() 松开鼠标
        ActionChains(self.browser).release().perform()

    def main(self):
        button = self.get_geetest_button()
        button.click()

        slider = self.get_slider()
        slider.click()
        distance = self.get_gep()
        tracks = self.get_track(distance)
        self.move_to_gep(slider, tracks)

if __name__ == '__main__':
    crack = CrackGeetest()
    crack.main()