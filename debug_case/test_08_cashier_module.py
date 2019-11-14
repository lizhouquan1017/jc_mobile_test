# coding:utf-8
from PO.business.cash_module import CashBusiness
from PO.business.login_module import LoginBusiness
from base.BaseDriver_one import BaseDriverOne
from base.TestCaase import TestCase_
from base.BaseReadCfg import ReadData
import time
import logging


class CashierTest(BaseDriverOne, TestCase_):
    
    # 登录操作
    def login_action(self):
        login = LoginBusiness(self.driver)
        data = login.get_csv_data('../data/product_data/login_data.csv', 1)
        login.login_action(data[0], data[2])

    # 正常收银
    def test_08001_cashier_case(self):
        """正常收银（现金）"""
        self.login_action()
        logging.info('开始收银')
        cashier = CashBusiness(self.driver)
        cashier.cashier_goods(num=1)
        time.sleep(1)
        status_dict = cashier.get_cash_success_information()
        sales_order_num = status_dict["sales_order_num"]
        ReadData().write_data('product_sale_order', 'num1', sales_order_num)
        self.assertTrue(status_dict["status"])
        self.assertEqual("现金", status_dict["settlement_type"])

    def test_08002_cashier_case(self):
        """正常收银（银行卡）"""
        self.login_action()
        logging.info('开始收银')
        cashier = CashBusiness(self.driver)
        cashier.cashier_goods(num=1, cash_type="银行卡")
        time.sleep(1)
        status_dict = cashier.get_cash_success_information()
        sales_order_num = status_dict["sales_order_num"]
        ReadData().write_data('product_sale_order', 'num1', sales_order_num)
        self.assertTrue(status_dict["status"])
        self.assertEqual("银行卡", status_dict["settlement_type"])

    def test_08003_cashier_case(self):
        """正常收银（支付宝账户）"""
        self.login_action()
        logging.info('开始收银')
        cashier = CashBusiness(self.driver)
        cashier.cashier_goods(num=1, cash_type="支付宝账户")
        time.sleep(1)
        status_dict = cashier.get_cash_success_information()
        sales_order_num = status_dict["sales_order_num"]
        ReadData().write_data('product_sale_order', 'num1', sales_order_num)
        self.assertTrue(status_dict["status"])
        self.assertEqual("支付宝账户", status_dict["settlement_type"])

    def test_08004_cashier_case(self):
        """正常收银（微信支付账户）"""
        self.login_action()
        logging.info('开始收银')
        cashier = CashBusiness(self.driver)
        cashier.cashier_goods(num=1, cash_type="微信支付账户")
        time.sleep(1)
        status_dict = cashier.get_cash_success_information()
        sales_order_num = status_dict["sales_order_num"]
        ReadData().write_data('product_sale_order', 'num1', sales_order_num)
        self.assertTrue(status_dict["status"])
        self.assertEqual("微信支付账户", status_dict["settlement_type"])

    def test_08005_cashier_case(self):
        """正常收银（默认老板销售员）"""
        self.login_action()
        logging.info('开始收银')
        cashier = CashBusiness(self.driver)
        cashier.cashier_goods(num=1)
        time.sleep(1)
        status_dict = cashier.get_cash_success_information()
        sales_order_num = status_dict["sales_order_num"]
        ReadData().write_data('product_sale_order', 'num1', sales_order_num)
        self.assertTrue(status_dict["status"])
        self.assertEqual("老板", status_dict["saler"])

    def test_08006_cashier_case(self):
        """正常收银（手动选择销售员）"""
        self.login_action()
        logging.info('开始收银')
        cashier = CashBusiness(self.driver)
        cashier.cashier_goods(num=1, saler1='李洲全-13888888811')
        time.sleep(1)
        status_dict = cashier.get_cash_success_information()
        sales_order_num = status_dict["sales_order_num"]
        ReadData().write_data('product_sale_order', 'num1', sales_order_num)
        self.assertTrue(status_dict["status"])
        self.assertEqual("李洲全", status_dict["saler"])

    def test_08007_cashier_case(self):
        """正常收银（手动选择销售员）"""
        self.login_action()
        logging.info('开始收银')
        cashier = CashBusiness(self.driver)
        cashier.cashier_goods(num=1, saler1='李洲全-13888888811', saler2="测试人员-16666668888")
        time.sleep(1)
        status_dict = cashier.get_cash_success_information()
        sales_order_num = status_dict["sales_order_num"]
        ReadData().write_data('product_sale_order', 'num1', sales_order_num)
        self.assertTrue(status_dict["status"])
        self.assertEqual("测试人员,李洲全", status_dict["saler"])

    # 商品打折销售
    def test_08008_goods_discount_sales_case(self):
        """商品打折销售(1折),订单无优惠"""
        self.login_action()
        cashier = CashBusiness(self.driver)
        cashier.cashier_goods(num=1, normal=True, good_discount=True, good_value=1)
        status_dict = cashier.get_cash_success_information()
        sales_order_num = status_dict["sales_order_num"]
        ReadData().write_data('product_sale_order', 'num2', sales_order_num)
        self.assertTrue(status_dict["status"])
        self.assertEqual(status_dict["price"], r'￥20.00')

    # 商品改价销售
    def test_08009_goods_modify_sales_case(self):
        """商品改价销售(￥20.00)，订单无优惠"""
        self.login_action()
        cashier = CashBusiness(self.driver)
        cashier.cashier_goods(num=1, normal=True, good_modify=True, good_value=20)
        status_dict = cashier.get_cash_success_information()
        sales_order_num = status_dict["sales_order_num"]
        ReadData().write_data('product_sale_order', 'num3', sales_order_num)
        self.assertTrue(status_dict["status"])
        self.assertEqual(status_dict["price"], r'￥20.00')

    # 商品打折，订单打折销售
    def test_08010_discount_discount_sales_case(self):
        """商品打折(5折)，订单打折销售（5折）"""
        self.login_action()
        cashier = CashBusiness(self.driver)
        cashier.cashier_goods(num=1, normal=True, good_discount=True, good_value=5, offer=False,
                              order_discount=True, order_value=5)
        status_dict = cashier.get_cash_success_information()
        sales_order_num = status_dict["sales_order_num"]
        ReadData().write_data('product_sale_order', 'num4', sales_order_num)
        self.assertTrue(status_dict["status"])
        self.assertEqual(status_dict["price"], r'￥50.00')

    # 商品改价，订单打折销售
    def test_08011_modify_discount_sales_case(self):
        """商品改价(￥100)，订单打折销售（8折）"""
        self.login_action()
        cashier = CashBusiness(self.driver)
        cashier.cashier_goods(num=1, normal=True, good_modify=True, good_value=100, offer=False,
                              order_discount=True, order_value=8)
        status_dict = cashier.get_cash_success_information()
        sales_order_num = status_dict["sales_order_num"]
        ReadData().write_data('product_sale_order', 'num5', sales_order_num)
        self.assertTrue(status_dict["status"])
        self.assertEqual(status_dict["price"], r'￥80.00')

    # 商品打折，订单改价销售
    def test_08012_discount_modify_sales_case(self):
        """商品打折（5折），订单改价（￥88）"""
        self.login_action()
        cashier = CashBusiness(self.driver)
        cashier.cashier_goods(num=1, normal=True, good_discount=True, good_value=5, offer=False,
                              order_modify=True, order_value=88)
        status_dict = cashier.get_cash_success_information()
        sales_order_num = status_dict["sales_order_num"]
        ReadData().write_data('product_sale_order', 'num6', sales_order_num)
        self.assertTrue(status_dict["status"])
        self.assertEqual(status_dict["price"], r'￥88.00')

    # 商品改价，订单改价销售
    def test_08013_modify_modify_sales_case(self):
        """商品改价(￥100)，订单改价（￥88）"""
        self.login_action()
        cashier = CashBusiness(self.driver)
        cashier.cashier_goods(num=1, normal=True, good_modify=True, good_value=100, offer=False,
                              order_modify=True, order_value=88)
        status_dict = cashier.get_cash_success_information()
        sales_order_num = status_dict["sales_order_num"]
        ReadData().write_data('product_sale_order', 'num7', sales_order_num)
        self.assertTrue(status_dict["status"])
        self.assertEqual(status_dict["price"], r'￥88.00')

    # 订单打折销售
    def test_08014_order_discount_sales_case(self):
        """商品无优惠，订单打折（5）"""
        self.login_action()
        cashier = CashBusiness(self.driver)
        cashier.cashier_goods(num=1, offer=False, order_discount=True, order_value=5)
        status_dict = cashier.get_cash_success_information()
        sales_order_num = status_dict["sales_order_num"]
        ReadData().write_data('product_sale_order', 'num8', sales_order_num)
        self.assertTrue(status_dict["status"])
        self.assertEqual(status_dict["price"], r'￥100.00')

    # 商品改价，订单改价销售
    def test_08015_order_modify_sales_case(self):
        """商品无优惠，订单改价（￥88）"""
        self.login_action()
        cashier = CashBusiness(self.driver)
        cashier.cashier_goods(num=1, offer=False, order_modify=True, order_value=88)
        status_dict = cashier.get_cash_success_information()
        sales_order_num = status_dict["sales_order_num"]
        ReadData().write_data('product_sale_order', 'num9', sales_order_num)
        self.assertTrue(status_dict["status"])
        self.assertEqual(status_dict["price"], r'￥88.00')
