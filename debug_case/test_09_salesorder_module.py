# coding:utf-8
from business.loginView import LoginView
from business.salesorderView import SalesOrderView
from base.BaseReadCfg import ReadData
from base.BaseDriver_one import BaseDriverOne
from base.TestCaase import TestCase_
import time


class SalesReturnTest(BaseDriverOne, TestCase_):

    # 登录操作
    def login_action(self):
        login = LoginView(self.driver)
        data = login.get_csv_data('../data/product_data/loginView.csv', 1)
        login.login_action(data[0], data[2])

    # 销售单复制在销售
    def test_01_sales_order_copy_case(self):
        """销售单复制并生成新的销售单"""
        self.login_action()
        salesorder = SalesOrderView(self.driver)
        ordernum = ReadData().get_data('product_sale_order', 'num8')
        salesorder.sales_order_action(keyword=ordernum, copy=True)
        sales_order_num = salesorder.get_sales_order_num()
        ReadData().write_data('product_sale_order', 'num17', sales_order_num)
        # 设置检查点
        self.assertTrue(salesorder.check_transaction_success_status())

    # 销售单作废
    def test_02_sales_order_copy_case(self):
        """销售单作废"""
        self.login_action()
        salesorder = SalesOrderView(self.driver)
        ordernum = ReadData().get_data('product_sale_order', 'num17')
        salesorder.sales_order_action(keyword=ordernum, obsolete=True)
        # 设置检查点
        self.assertTrue(salesorder.check_sales_order_status())
