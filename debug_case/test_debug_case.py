# -*- coding:utf-8 -*-
__author__ = "lizhouquan"
from base.desired_caps import BaseDriver
from PO.business.login_module import LoginBusiness
from PO.business.register_module import RegisterBusiness
from PO.business.findPwd_module import FindPwdBusiness
from PO.business.purchase_module import PurchaseBusiness
from PO.business.purchaseorder_module import PurchaseOrderBusiness
from PO.business.purchasereturn_module import PurchaseReturnBusiness
from PO.business.purchasereturnorder_module import PurchaseReturnOrderBusiness
from PO.business.goods_module import GoodsBusiness
from PO.business.cash_module import CashBusiness
from PO.business.salesorder_module import SalesOrderBusiness
from PO.business.salesreturn_module import SalesReturnBusiness
from base.ParametrizedCase import ParametrizedCase
from base.BaseReadCfg import ReadData
from time import sleep
from base.HTMLTestRunner_cn import HTMLTestRunner
import unittest
import logging
import random

num = random.randint(100000, 999999)
pwd = 'ab'+str(num)


class DebugTest(ParametrizedCase):

    @classmethod
    def setUpClass(cls):
        driver = BaseDriver()
        cls.driver = driver.appium_desired(0)

    def setUp(self):
        self.imgs = []
        self.addCleanup(self.cleanup)
        self.driver.start_activity("com.gengcon.android.jxc", "com.gengcon.android.jxc.login.SplashActivity")
        # driver = BaseDriver()
        # self.driver = driver.appium_desired(self.param)

    def tearDown(self):
        self.driver.close_app()

    def add_img(self):
        # 在是python3.x 中，如果在这里初始化driver ，因为3.x版本 unittest 运行机制不同，会导致用力失败时截图失败
        self.imgs.append(self.driver.get_screenshot_as_base64())
        return True

    def cleanup(self):
        pass

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    # 登录操作
    def login_action(self):
        login = LoginBusiness(self.driver)
        data = login.get_csv_data('../data/test_data/login_data.csv', 1)
        print(data[0])
        login.login_action(data[0], data[2])

    def test_01001_add_case(self):
        """正常添加商品"""
        """
        商品名称，成本价，零售价，颜色属性，尺码属性 ：必填
        """
        self.login_action()
        goods = GoodsBusiness(self.driver)
        goods.enter_goods_list()
        goods.type_must_field('测试商品1号', 100, 200, '均色', '均码')
        goods.confirm_add_goods()
        status = goods.check_success_status()
        goods.get_goods_details()
        goods_num = goods.get_goods_num()
        sku_num = goods.get_sku_barcode()
        ReadData(self.param).write_data('goods_bar_code', 'num1', goods_num)
        ReadData(self.param).write_data('goods_single_barcode', 'num1', sku_num)
        self.assertEqual('添加新品成功1', status)

    def test_01002_add_case(self):
        """自定义商品货号添加商品"""
        """
        商品名称，成本价，零售价，颜色属性，尺码属性 ：必填
        商品货号，库存数，商品条码，商品备注，其他参数： 非必填
        """
        self.login_action()
        goods = GoodsBusiness(self.driver)
        goods.enter_goods_list()
        goods.type_must_field('测试商品2号', 100, 200, '均色', '均码', 19891017)
        goods.confirm_add_goods()
        status = goods.check_success_status()
        goods.get_goods_details()
        goods_num = goods.get_goods_num()
        sku_code = goods.get_sku_barcode()
        ReadData(self.param).write_data('goods_bar_code', 'num2', goods_num)
        ReadData(self.param).write_data('goods_single_barcode', 'num2', sku_code)
        self.assertEqual('添加新品成功', status)

    # def test_04002_modify_pwdSuccess(self):
    #     """修改密码成功"""
    #     logging.info(r'==修改密码成功用例==')
    #     if self.param == 0:
    #         find = FindPwdBusiness(self.driver)
    #         data0 = find.get_csv_data('../data/test_data/login_data.csv', 1)
    #         data1 = find.get_csv_data('../data/test_data/pwd.csv', 10)
    #         data2 = find.get_csv_data('../data/test_data/pwd.csv', 11)
    #         find.findpwd_action(data0[0], data1[2])
    #         find.modify_action(data1[3], data1[3])
    #         sleep(2)
    #         # self.assertTrue(find.check_find_pwd_success_status())
    #         self.assertTrue(False)
    #         # sleep(10)
    #         find.update_csv_data('../data/test_data/login_data.csv', 1, '正式账号1', data0[2], data1[3])
    #         find.update_csv_data('../data/test_data/pwd.csv', 1, '密码相同1', data2[3], data1[3])
    #         logging.info(pwd)
    #         find.update_csv_data('../data/test_data/pwd.csv', 1, '修改密码1', data1[3], pwd)
    #     else:
    #         find = FindPwdBusiness(self.driver)
    #         data0 = find.get_csv_data('../data/test_data/login_data.csv', 2)
    #         data1 = find.get_csv_data('../data/test_data/pwd.csv', 12)
    #         data2 = find.get_csv_data('../data/test_data/pwd.csv', 13)
    #         find.findpwd_action(data0[0], data1[2])
    #         find.modify_action(data1[3], data1[3])
    #         sleep(2)
    #         self.assertTrue(find.check_find_pwd_success_status())
    #         find.update_csv_data('../data/test_data/login_data.csv', 1, '正式账号2', data0[2], data1[3])
    #         find.update_csv_data('../data/test_data/pwd.csv', 1, '密码相同2', data2[3], data1[3])
    #         logging.info(pwd)
    #         find.update_csv_data('../data/test_data/pwd.csv', 1, '修改密码2', data1[3], pwd)


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(DebugTest)
    runer = HTMLTestRunner(title="带截图的测试报告", description="小试牛刀", stream=open("sample_test_report_appium.html", "wb"),
                           verbosity=2, retry=1, save_last_try=True)
    runer.run(suite)
