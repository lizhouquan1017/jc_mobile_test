# coding:utf-8

from base.BaseReadIni import ReadIni
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.mobileby import By
import logging
import os
import time
import csv


class BaseOperation:

    # 初始化操作
    def __init__(self, driver):
        self.driver = driver
        self.efg = ReadIni(file_name='config.ini')

    # 通过id获取元素
    def find_element(self, *loc):
        try:
            e = WebDriverWait(self.driver, 10, 1, NoSuchElementException).until(
                lambda driver: driver.find_element_by_id(*loc))
            return e
        except NoSuchElementException:
            logging.info('元素不存在')
        except TimeoutException:
            logging.info('查找元素超时')

    # 获取元素属性
    def get_text(self, *loc):
        try:
            e = self.find_element(*loc)
            text = e.text
            return text
        except NoSuchElementException:
            logging.info('元素未找到')

    # 通过xpath定位
    def find_element_xpath(self, *loc):
        try:
            e = self.driver.find_element_by_xpath(*loc)
            return e
        except NoSuchElementException:
            logging.info('元素不存在')
        except TimeoutException:
            logging.info('元素超时')

    # 通过text值获取元素
    def find_element_text(self, name):
        try:
            e = self.driver.find_element_by_android_uiautomator('text(\"'+name+'\")')
            return e
        except NoSuchElementException:
            logging.info('元素不存在')
        except TimeoutException:
            logging.info('元素超时')

    # 输入文本
    def type(self, name, text):
        e = self.find_element(name)
        try:
            e.clear()
            e.send_keys(text)
        except e:
            logging.error('元素无法输入')

    # 点击
    def click(self, name):
        e = self.find_element(name)
        try:
            e.click()
        except e:
            logging.error('元素无法点击')

    def click_text(self, value):
        e = self.find_element_text(value)
        e.click()

    def click_xpath(self, value):
        e = self.find_element_xpath(value)
        e.click()

    def location(self, value):
        loc = self.find_element_xpath(value).location
        print(loc)
        # print(loc)
        # size = self.find_element_xpath(value).size
        # print(size)
        # TouchAction(self.driver).press().move_to(loc, 360, 0).release().perform()

    # 获取toast提示信息
    def is_toast_exist(self, text):
        try:
            toast_loc = (By.XPATH, '//*[@text=\'{}\']'.format(text))
            e = WebDriverWait(self.driver, 10, 0.1).until(EC.presence_of_element_located(toast_loc))
            print('toast获取到了：'+str(e))
            if e.text in text:
                return True
        except TimeoutException:
            # self.get_windows_img(text+r'文本未出现')
            # return False
            logging.info('未出现toast信息')

    # 判断元素是否存在
    def is_exists(self, *loc):
        e = self.find_element(*loc)
        if e:
            return True
        else:
            return False

    def swipe(self, x1, y1, x2, y2, d):
        self.driver.swipe(x1, y1, x2, y2, d)

    def get_screen_size(self):  # 获取当前的width和height的x、y的值
        x = self.driver.get_window_size()['width']  # width为x坐标
        y = self.driver.get_window_size()['height']  # height为y坐标
        return (x, y)

    def element_swipe_up(self, px, *loc):
        e = self.find_element(*loc)
        element_location_x = e.location.get('x')
        element_location_y = e.location.get('y')
        element_size_width = e.size["width"]
        element_size_height = e.size["height"]
        time.sleep(3)
        self.driver.swipe((element_location_x+element_size_width)/2, ((element_location_y+element_size_height/2)+int(px)),
                          (element_location_x+element_size_width)/2, ((element_location_y+element_size_height/2)-int(px)))

    def element_swipe_down(self, px, *loc):
        e = self.find_element(*loc)
        element_location_x = e.location.get('x')
        element_location_y = e.location.get('y')
        element_size_width = e.size["width"]
        element_size_height = e.size["height"]
        time.sleep(3)
        self.driver.swipe((element_location_x+element_size_width)/2, ((element_location_y+element_size_height/2)-int(px)),
                          (element_location_x+element_size_width)/2, ((element_location_y+element_size_height/2)+int(px)))

    def swipe_up(self, t):  # 当前向上滑动swipeup
        screen = self.get_screen_size()
        print(screen)
        x1 = int(screen[0] * 0.5)
        y1 = int(screen[1] * 0.85)
        x2 = int(screen[0] * 0.5)
        y2 = int(screen[1] * 0.5)
        self.driver.swipe(x1, y1, x2, y2, t)  # 设置时间为500

    def swipe_down(self, t):  # 当前向上滑动swipeup
        screen = self.get_screen_size()
        x1 = int(screen[0] * 0.5)
        y1 = int(screen[1] * 0.25)
        x2 = int(screen[0] * 0.5)
        y2 = int(screen[1] * 0.75)
        self.driver.swipe(x1, y1, x2, y2, t)  # 设置时间为500

    def swipe_left(self, t):  # 当前向上滑动swipeup
        screen = self.get_screen_size()
        x1 = int(screen[0] * 0.75)
        y1 = int(screen[1] * 0.5)
        x2 = int(screen[0] * 0.25)
        y2 = int(screen[1] * 0.5)
        self.driver.swipe(x1, y1, x2, y2, t)  # 设置时间为500

    def swipe_right(self, t):  # 当前向上滑动swipeup
        screen = self.get_screen_size()
        x1 = int(screen[0] * 0.25)
        y1 = int(screen[1] * 0.5)
        x2 = int(screen[0] * 0.75)
        y2 = int(screen[1] * 0.5)
        self.driver.swipe(x1, y1, x2, y2, t)  # 设置时间为500

    # 保存图片
    def get_windows_img(self, name):
        """
        在这里我们把file_path这个参数写死，直接保存到我们项目根目录的一个文件夹.\Screenshots下
        """
        file_path = os.path.dirname(os.path.abspath('.')) + '/screenshots/'
        rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
        screen_name = file_path + name + rq + '.png'
        try:
            self.driver.get_screenshot_as_file(screen_name)
            logging.info("保存错误截图")
        except NameError as e:
            logging.error("截图发生错误： %s" % e)
            self.get_windows_img('错误截图')

    # 从csv文件中获取数据
    def get_csv_data(self, csv_file, line):
        logging.info(r'获取输入数据')
        with open(csv_file, 'r', encoding='gbk') as file:
            reader = csv.reader(file)
            for index, row in enumerate(reader, 1):
                if index == line:
                    return row

    # 存数据导csv文件
    def save_csv_data(self, csv_file, datas):
        logging.info(r'存储数据到%s' % csv_file)
        with open(csv_file, 'w', encoding='gbk') as file:
            file.write(datas+'\n')
            logging.info(r'数据保存成功')

    # 更新数据导csv文件
    def update_csv_data(self, csv_file, index, flag, old, new):
        filereader = open(csv_file, 'r')
        rows = filereader.readlines()
        filewriter = open(csv_file, 'w')
        for line in rows:
            l = line.split(',')
            if l[index] == flag:
                filewriter.writelines(line.replace(old, new))
            else:
                filewriter.writelines(line)
        filewriter.close()
        filereader.close()
