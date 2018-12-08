#! python3
# -*- coding:utf-8 -*-
# author: shikunyao
# datetime: 2018/11/30 0030 14:55
# 点击验证码识别
from io import BytesIO

import requests
from hashlib import md5
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from numba import Object
from PIL import Image

import time


class Chaojiying(Object):

    def __init__(self, username, password, soft_id):
        self.username = username
        self.password = md5(password.encode('utf-8')).hexdigest()
        self.soft_id = soft_id
        self.base_params = {
            'user': self.username,
            'pass2': self.password,
            'softid': self.soft_id,
        }
        self.headers = {
            'Connection': 'Keep-Alive',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:63.0) Gecko/20100101 Firefox/63.0',
        }

    def post_pic(self, im, codetype):
        '''

        :param im: 图片字节
        :param codetype: 题目类型
        :return:
        '''
        params = {
            'codetype': codetype
        }
        params.update(self.base_params)
        files = {'userfile': ('ccc.jpg', im)}
        r = requests.post('http://upload.chaojiying.net/Upload/Processing.php', data=params, files=files,
                          headers=self.headers)
        return r.json()

    def report_error(self, im_id):
        '''

        :param im_id: 报错图片的ID
        :return:
        '''
        params = {
            'id': im_id
        }
        params.update(self.base_params)
        r = requests.post('http://upload.chaojiying.net/Upload/ReportError.php', data=params, headers=self.headers)
        return r.json()


EMAIL = 'shikunyaoaaa@163.com'
PASSWORD = ''
# 超级鹰用户名，密码，软件ID，验证码类型
CHAOJIYING_USERNAME = 'Germey'
CHAOJIYING_PASSWORD = ''
CHAOJIYING_SOFT_ID = 111111
CHAOJIYING_KIND = 3333


class CrackTouClick():
    def __init__(self):
        self.url = 'http://admin.touclick.com/login.html'
        self.browser = webdriver.Chrome()
        self.wait = WebDriverWait(self.browser, 20)
        self.email = EMAIL
        self.password = PASSWORD
        self.chaojiying = Chaojiying(CHAOJIYING_USERNAME, CHAOJIYING_PASSWORD, CHAOJIYING_SOFT_ID)

    def open(self):
        '''
        打开网页输入用户名密码
        :return: None
        '''
        self.browser.get(self.url)
        email = self.wait.until(EC.presence_of_element_located((By.ID, 'email')))
        password = self.wait.until(EC.presence_of_element_located((By.ID, 'password')))
        email.send_keys(self.email)
        password.send_keys(self.password)

    def get_touclick_button(self):
        '''
        获取初始化验证按钮
        :return:
        '''
        button = self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'touclick-hod-wrap')))
        return button

    def get_touclick_element(self):
        '''
        获取验证图片对象
        :return: 图片对象
        '''
        element = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'touclick-pub-content')))
        return element

    def get_position(self):
        '''
        获取验证码位置
        :return: 验证码位置元组
        '''
        element = self.get_touclick_element()
        time.sleep(2)
        location = element.location
        size = element.size
        top, bottom, left, right = location['y'], location['y'] + size['height'], location['x'], location['x'] + size[
            'width']
        return (top, bottom, left, right)

    def get_screenshot(self):
        '''
        获取网页截图
        :return: 截图对象
        '''
        screenshot = self.browser.get_screenshot_as_png()
        screenshot = Image.open(BytesIO(screenshot))
        return screenshot

    def get_touclick_image(self, name='captcha.png'):
        '''
        获取验码图片
        :return: 图片对象
        '''
        top, bottom, left, right = self.get_position()
        print('验证码位置', top, bottom, left, right)
        screenshot = self.get_screenshot()
        captch = screenshot.crop((left, top, right, bottom))

    def get_result(self):
        '''
        获取超级鹰识别结果
        :return: 识别结果
        '''
        image = self.get_touclick_image()
        bytes_array = BytesIO()
        image.save(bytes_array, format='PNG')
        # 识别验证码
        result = self.chaojiying.post_pic(bytes_array.getvalue(), CHAOJIYING_KIND)
        return result

    def get_points(self, captcha_result):
        '''
        解析识别的结果
        :param captcha_result: 识别结果
        :return: 转化后的结果
        '''
        groups = captcha_result.get('pic_str').split('|')
        locations = [[int(number) for number in groups.split(',')] for group in groups]
        return locations

    def touch_click_words(self, locations):
        '''
        点击验证图片
        :param locations: 点击位置
        :return: None
        '''
        for location in locations:
            print(location)
            ActionChains(self.browser).move_to_element_with_offset(self.get_touclick_element(), location[0],
                                                                   location[1]).click().perform()
            time.sleep(1)
