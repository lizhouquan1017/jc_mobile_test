# -*- coding:utf-8 -*-
__author__ = "lizhouquan"

from base.BaseDriver_one import BaseDriverTwo
from base.TestCaase import TestCase_
from business.loginView import LoginView
from business.registerView import RegisterView
from business.findPwdView import FindPwdView
from time import sleep
import logging
import random

num = random.randint(100000, 999999)
pwd = 'ab'+str(num)


class TestEnviromentTest(BaseDriverTwo, TestCase_):

    def test_01_user_login(self):
        """正常登录用例"""
        logging.info('==正常账号成功登录用例==')
        login = LoginView(self.driver)
        data = login.get_csv_data('../data/test_data/loginView.csv', 1)
        login.login_action(data[0], data[2])
        sleep(2)
        self.assertTrue(login.check_login_success_status())

    def test_02_user_login_pwderr(self):
        """密码错误登录用例"""
        logging.info('==正确账号密码错误登录=')
        login = LoginView(self.driver)
        data = login.get_csv_data('../data/test_data/loginView.csv', 2)
        login.login_action(data[0], data[1])
        sleep(2)
        self.assertTrue(login.check_login_fail_status())
        # self.assertTrue(login.check_toast_text('用户名或密码错误'))

    def test_03_user_login_pwdempty(self):
        """密码为空登录"""
        logging.info('==正常账号密码为空登录==')
        login = LoginView(self.driver)
        data = login.get_csv_data('../data/test_data/loginView.csv', 3)
        login.login_action(data[0], data[1])
        sleep(2)
        self.assertTrue(login.check_login_fail_status())

    def test_04_user_login_phonenumerror(self):
        """手机号为错误登录"""
        logging.info('==手机号格式错误登录==')
        login = LoginView(self.driver)
        data = login.get_csv_data('../data/test_data/loginView.csv', 4)
        login.login_action(data[0], data[1])
        sleep(2)
        self.assertTrue(login.check_login_fail_status())

    def test_05_user_login_unregistered(self):
        """未注册账号登录"""
        logging.info('==未注册账号登录==')
        login = LoginView(self.driver)
        data = login.get_csv_data('../data/test_data/loginView.csv', 5)
        login.login_action(data[0], data[1])
        sleep(2)
        self.assertTrue(login.check_login_fail_status())

    def test_06_user_login_phonenumEmpty(self):
        """ 手机号为空登录"""
        logging.info('==手机号为空登录==')
        login = LoginView(self.driver)
        data = login.get_csv_data('../data/test_data/loginView.csv', 6)
        login.login_action(data[0], data[1])
        sleep(2)
        self.assertTrue(login.check_login_fail_status())

    def test_07_user_login_RestrictedAccounts(self):
        """限制账号登录"""
        logging.info('==限制账号登录==')
        login = LoginView(self.driver)
        data = login.get_csv_data('../data/test_data/loginView.csv', 7)
        login.login_action(data[0], data[1])
        sleep(2)
        self.assertTrue(login.check_login_fail_status())

    def test_08_user_login_DeactivatedAccount(self):
        """停用账号登录"""
        logging.info('==停用账号登录==')
        login = LoginView(self.driver)
        data = login.get_csv_data('../data/test_data/loginView.csv', 8)
        login.login_action(data[0], data[1])
        sleep(2)
        self.assertTrue(login.check_login_fail_status())

    def test_09_user_login_VerificationCode(self):
        """验证码登录"""
        logging.info('==验证码登录==')
        login = LoginView(self.driver)
        data = login.get_csv_data('../data/test_data/loginView.csv', 9)
        login.login_code_action(data[0], data[1])
        sleep(2)
        self.assertTrue(login.check_login_success_status())

    def test_10_user_login_ExperienceAccount(self):
        """体验账号登录"""
        logging.info('==体验账号登录==')
        login = LoginView(self.driver)
        login.login_experience_account_action()
        sleep(2)
        self.assertTrue(login.check_login_success_status())

    def test_11_user_login_VerificationCodeEmpty(self):
        """验证码为空登录"""
        logging.info('==验证码为空登录==')
        login = LoginView(self.driver)
        data = login.get_csv_data('../data/test_data/loginView.csv', 10)
        login.login_code_action(data[0], data[1])
        sleep(2)
        self.assertTrue(login.check_login_fail_status())

    def test_12_user_login_VerificationCodeError(self):
        """验证码错误登录"""
        logging.info('==验证码错误登录==')
        login = LoginView(self.driver)
        data = login.get_csv_data('../data/test_data/loginView.csv', 11)
        login.login_code_action(data[0], data[1])
        sleep(2)
        self.assertTrue(login.check_login_fail_status())

    # 正常注册
    def test_13_user_register(self):
        """正常注册"""
        logging.info('=用户正常注册成功=')
        register = RegisterView(self.driver)
        data = register.get_csv_data('../data/test_data/register.csv', 1)
        register.register_action(data[0], data[2], data[3])
        newdata = str(int(data[0])+1)
        self.assertTrue(register.check_register_success_status())
        sleep(2)
        register.update_csv_data('../data/test_data/register.csv', 1, '用户正常注册', data[0], newdata)

    # 注册手机号为空
    def test_14_register_phonenumEmpty(self):
        """注册手机号为空"""
        logging.info('=用户注册手机号码为空=')
        register = RegisterView(self.driver)
        data = register.get_csv_data('../data/test_data/register.csv', 2)
        register.register_common_action(data[0], data[1], data[2])
        sleep(2)
        self.assertTrue(register.check_register_fail_status())

    # 注册手机号格式不正确
    def test_15_register_phonenumError(self):
        """注册手机号格式不正确"""
        logging.info('=用户注册手机号格式错误=')
        register = RegisterView(self.driver)
        data = register.get_csv_data('../data/test_data/register.csv', 3)
        register.register_common_action(data[0], data[1], data[2])
        sleep(2)
        self.assertTrue(register.check_register_fail_status())

    # 注册手机号已注册
    def test_16_registered(self):
        """注册手机号已注册"""
        logging.info('=用户手机号已注册=')
        register = RegisterView(self.driver)
        data = register.get_csv_data('../data/test_data/register.csv', 4)
        register.register_common_action(data[0], data[1], data[2])
        sleep(2)
        self.assertTrue(register.check_register_fail_status())

    # 修改密码成功
    def test_17_modify_pwdSuccess(self):
        """修改密码成功"""
        logging.info(r'==修改密码成功用例==')
        find = FindPwdView(self.driver)
        data0 = find.get_csv_data('../data/test_data/loginView.csv', 1)
        data1 = find.get_csv_data('../data/test_data/pwd.csv', 10)
        data2 = find.get_csv_data('../data/test_data/pwd.csv', 11)
        find.findpwd_action(data0[0], data1[2])
        find.modify_action(data1[3], data1[3])
        sleep(2)
        self.assertTrue(find.check_find_pwd_success_status())
        find.update_csv_data('../data/test_data/loginView.csv', 1, '正式账号', data0[2], data1[3])
        find.update_csv_data('../data/test_data/pwd.csv', 1, '密码相同', data2[3], data1[3])
        logging.info(pwd)
        find.update_csv_data('../data/test_data/pwd.csv', 1, '修改密码', data1[3], pwd)

    # 手机号为空找回密码
    def test_18_findpwd_phoneNumEmpty(self):
        """找回密码手机号为空"""
        logging.info(r'==找回密码手机号为空用例==')
        find = FindPwdView(self.driver)
        data = find.get_csv_data('../data/test_data/pwd.csv', 1)
        find.findpwd_action(data[0], data[1])
        sleep(2)
        self.assertTrue(find.check_find_pwd_fail_status())

    # 手机号格式错误找回密码
    def test_19_findpwd_phoneNumError(self):
        """找回密码手机号格式错误"""
        logging.info(r'==找回密码手机号格式错误用例==')
        find = FindPwdView(self.driver)
        data = find.get_csv_data('../data/test_data/pwd.csv', 2)
        find.findpwd_action(data[0], data[1])
        sleep(2)
        self.assertTrue(find.check_find_pwd_fail_status())

    # 未注册手机号找回密码
    def test_20_findpwd_phoneNumUnregistered(self):
        """未注册手机号找回密码"""
        logging.info(r'==未注册手机号找回密码用例==')
        find = FindPwdView(self.driver)
        data = find.get_csv_data('../data/test_data/pwd.csv', 3)
        find.findpwd_action(data[0], data[1])
        sleep(2)
        self.assertTrue(find.check_find_pwd_fail_status())

    # 验证码为空找回密码
    def test_21_findpwd_codeEmpty(self):
        """验证码为空找回密码"""
        logging.info(r'==验证码为空找回密码用例==')
        find = FindPwdView(self.driver)
        data = find.get_csv_data('../data/test_data/pwd.csv', 4)
        find.findpwd_action(data[0], data[1])
        sleep(2)
        self.assertTrue(find.check_find_pwd_fail_status())

    # 验证码错误
    def test_22_findpwd_codeError(self):
        """验证码错误找回密码"""
        logging.info(r'==验证码错误找回密码用例==')
        find = FindPwdView(self.driver)
        data = find.get_csv_data('../data/test_data/pwd.csv', 5)
        find.findpwd_action(data[0], data[1])
        sleep(2)
        self.assertTrue(find.check_find_pwd_fail_status())

    # 修改密码密码为空
    def test_23_modify_pwdEmpty(self):
        """修改密码密码为空"""
        logging.info(r'==修改密码密码为空用例==')
        find = FindPwdView(self.driver)
        data = find.get_csv_data('../data/test_data/pwd.csv', 6)
        find.findpwd_action(data[0], data[1])
        find.modify_action(data[2], data[3])
        sleep(2)
        self.assertTrue(find.check_modify_pwd_fail_status())

    # 修改密码不符合长度
    def test_24_modify_pwdNomatchLength(self):
        """修改密码不符合长度"""
        logging.info(r'==修改密码不符合长度用例==')
        find = FindPwdView(self.driver)
        data = find.get_csv_data('../data/test_data/pwd.csv', 7)
        find.findpwd_action(data[0], data[1])
        find.modify_action(data[2], data[3])
        sleep(2)
        self.assertTrue(find.check_modify_pwd_fail_status())

    # 修改密码不符合规则
    def test_25_modify_pwdNomatchRules(self):
        """修改密码不符合规则"""
        logging.info(r'==修改密码不符合规则用例==')
        find = FindPwdView(self.driver)
        data = find.get_csv_data('../data/test_data/pwd.csv', 8)
        find.findpwd_action(data[0], data[1])
        find.modify_action(data[2], data[3])
        sleep(2)
        self.assertTrue(find.check_modify_pwd_fail_status())

    # 修改密码前后输入不一致
    def test_26_modify_pwdInconsistent(self):
        """修改密码前后不一致"""
        logging.info(r'==修改密码输入前后不一致用例==')
        find = FindPwdView(self.driver)
        data = find.get_csv_data('../data/test_data/pwd.csv', 9)
        find.findpwd_action(data[0], data[1])
        find.modify_action(data[2], data[3])
        sleep(2)
        self.assertTrue(find.check_modify_pwd_fail_status())

    # 修改密码新旧密码重复
    def test_27_modify_pwdRepeat(self):
        """修改密码新旧密码重复"""
        logging.info(r'==修改密码新旧密码重复用例==')
        find = FindPwdView(self.driver)
        data = find.get_csv_data('../data/test_data/pwd.csv', 11)
        find.findpwd_action(data[0], data[2])
        find.modify_action(data[3], data[3])
        sleep(2)
        self.assertTrue(find.check_modify_pwd_fail_status())

