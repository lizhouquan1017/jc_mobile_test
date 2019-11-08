# coding:utf-8
import logging
from base.BaseOperation import BaseOperation
from base.BaseReadIni import ReadIni
from time import sleep


class FindPwdView(BaseOperation):

    def __init__(self, driver):
        super(FindPwdView, self).__init__(driver)
        self.efg = ReadIni(file_name='findpwdView.ini')

    # 找回密码界面公共方法
    def findpwd_action(self, phonenum, code):
        logging.info(r'进入找回密码界面')
        self.click(self.efg.read_config("找回密码按钮"))
        sleep(5)
        logging.info('找回密码账号: %s ' % phonenum)
        self.type(self.efg.read_config("电话输入框"), phonenum)
        logging.info('输入验证码: %s' % code)
        self.type(self.efg.read_config("验证码输入框"), code)
        logging.info(r'点击下一步操作')
        self.click(self.efg.read_config("下一步"))
        sleep(5)

    # 修改密码界面公共方法
    def modify_action(self, first, second):
        sleep(2)
        logging.info(r'进入修改密码界面')
        logging.info(r'第一次输入密码: %s' % first)
        self.type(self.efg.read_config("第一次密码输入"), first)
        logging.info(r'第二次输入密码: %s' % second)
        self.type(self.efg.read_config("第二次密码输入"), second)
        logging.info(r'点击提交')
        self.click(self.efg.read_config("提交按钮"))
        sleep(2)

    # 找回密码成功状态检查
    def check_find_pwd_success_status(self):
        sleep(3)
        flag = self.is_exists(self.efg.read_config("登录按钮"))
        return flag

    # 进入修改界面错误状态检查
    def check_find_pwd_fail_status(self):
        sleep(3)
        flag = self.is_exists(self.efg.read_config("下一步"))
        return flag

    # 修改密码界面状态检查
    def check_modify_pwd_fail_status(self):
        sleep(3)
        flag = self.is_exists(self.efg.read_config("提交按钮"))
        return flag
