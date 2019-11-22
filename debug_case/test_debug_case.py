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
import logging
import random

num = random.randint(100000, 999999)
pwd = 'ab'+str(num)

class DebugTest(ParametrizedCase):

    def setUp(self):
        driver = BaseDriver()
        self.driver = driver.appium_desired(0)

    def tearDown(self):
        self.driver.quit()

    # 登录操作
    def login_action(self):
        login = LoginBusiness(self.driver)
        data = login.get_csv_data('../data/product_data/login_data.csv', 1)
        login.login_action(data[0], data[2])

    # 采购单筛选用例
    def test_06014_purchase_order_filer_case(self):
        """关键字筛选(作废单据)"""
        self.login_action()
        purchaseorder = PurchaseOrderBusiness(self.driver)
        ordernum = ReadData().get_data('product_purchase_order', 'num2')
        purchaseorder.purchaseorder_action(status=False)
        detail_ordernum = purchaseorder.get_detail_ptuchase_order()
        self.assertEqual(ordernum, detail_ordernum)
