# coding:utf-8
import logging
from base.BaseOperation import BaseOperation
from base.BaseReadIni import ReadIni
from time import sleep


class LoginView(BaseOperation):

    def __init__(self, driver):
        super(LoginView, self).__init__(driver)
        self.efg = ReadIni(file_name='loginView.ini')

    # 登录成功
    def login_action(self, username, password):
        sleep(8)
        logging.info(r'==登录操作开始==')
        logging.info('输入用户名:%s' % username)
        self.type(self.efg.read_config('用户名输入框'), username)
        logging.info('输入密码:%s' % password)
        self.type(self.efg.read_config('密码输入框'), password)
        logging.info('点击登录按钮')
        self.click(self.efg.read_config('登录按钮'))
        logging.info('登录完成')
        sleep(2)

    # 验证码登录
    def login_code_action(self, username, code):
        sleep(8)
        logging.info('==验证码登录用例开始==')
        self.click(self.efg.read_config("验证码登录"))
        sleep(1)
        logging.info('输入用户名:%s' % username)
        self.type(self.efg.read_config("用户名输入框"), username)
        logging.info('输入验证码:%s' % code)
        self.type(self.efg.read_config("验证码输入框"), code)
        logging.info('点击登录按钮')
        self.click(self.efg.read_config("登录按钮"))
        sleep(1)

    # 体验账号登录
    def login_experience_account_action(self):
        logging.info('==体验账号登录==')
        self.click(self.efg.read_config("体验按钮"))
        sleep(2)
        logging.info(r'体验账号登录状态验证开始')

    # 检查登录成功状态
    def check_login_success_status(self):
        logging.info('==检查登录成功状态==')
        flag = self.is_exists(self.efg.read_config('今日销售额'))
        logging.info(flag)
        if flag:
            logging.info('验证状态成功！用例成功！')
            return True
        else:
            return False

    # 检查登录失败状态
    def check_login_fail_status(self):
        logging.info('==检查登录失败状态')
        flag = self.is_exists(self.efg.read_config("登录按钮"))
        logging.info(flag)
        if flag:
            logging.info('验证状态成功！用例成功！')
            return True
        else:
            return False

    def check_toast_text(self, text):
        flag = self.is_toast_exist(text)
        return flag
