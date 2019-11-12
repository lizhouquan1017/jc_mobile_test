# coding:utf-8

import logging
import random
from base.BaseOperation import BaseOperation
from base.BaseReadIni import ReadIni
from time import sleep


class RegisterBusiness(BaseOperation):

    def __init__(self, driver):
        super(RegisterBusiness, self).__init__(driver)
        self.efg = ReadIni(file_name='register_page.ini')

    # 随机数
    number = random.randint(0, 9999999)

    def register_action(self, register_username, register_code, register_password):
        logging.info('进入注册页面')
        self.click(self.efg.read_config("注册按钮"))
        sleep(5)
        logging.info('输入注册手机号: %s' % register_username)
        self.type(self.efg.read_config("注册用户名输入框"), register_username)
        logging.info('输入注册时验证码: %s' % register_code)
        self.type(self.efg.read_config("验证码输入框"), register_code)
        logging.info('输入注册时的密码: %s' % register_password)
        self.type(self.efg.read_config("密码输入框"), register_password)
        logging.info('点击下一步')
        self.click(self.efg.read_config("下一步按钮"))
        sleep(2)
        logging.info('选择商家')
        self.click(self.efg.read_config("商家按钮"))
        logging.info('点击下一步')
        self.click(self.efg.read_config("下一步按钮"))
        sleep(2)
        logging.info('输入公司名称')
        self.type(self.efg.read_config("公司名称输入框"), '自动化测试公司' + str(self.number))
        logging.info('输入门店名称')
        self.type(self.efg.read_config("门店输入框"), '自动化测试门店' + str(self.number))
        logging.info('输入省市县地址')
        self.click(self.efg.read_config("城市选择框"))
        logging.info('点击确认，默认选择第一个城市')
        self.click(self.efg.read_config("城市确认按钮"))
        logging.info('输入详细地址')
        self.type(self.efg.read_config("详细地址"), r'李洲全详细地址' + str(self.number))
        logging.info('点击下一步')
        self.click(self.efg.read_config("下一步按钮"))
        sleep(2)
        logging.info('点击跳过引导按钮')
        self.click(self.efg.read_config("跳过按钮"))
        sleep(2)

    def register_common_action(self, register_username, register_code, register_password):
        logging.info('进入注册页面')
        self.click(self.efg.read_config("注册按钮"))
        sleep(2)
        logging.info('输入注册手机号: %s' % register_username)
        self.type(self.efg.read_config("注册用户名输入框"), register_username)
        logging.info('输入注册时验证码: %s' % register_code)
        self.type(self.efg.read_config("验证码输入框"), register_code)
        logging.info('输入注册时的密码: %s' % register_password)
        self.type(self.efg.read_config("密码输入框"), register_password)
        logging.info('点击下一步')
        self.click(self.efg.read_config("下一步按钮"))
        sleep(2)

    def check_register_success_status(self):
        logging.info('==检查注册后登录状态==')
        flag = self.is_exists(self.efg.read_config("今日销售额"))
        return flag

    def check_register_fail_status(self):
        logging.info(r'检查状态开始')
        flag = self.is_exists(self.efg.read_config("下一步按钮"))
        return flag
