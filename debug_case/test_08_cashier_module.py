# coding:utf-8
from business.cashierView import CashierView
from business.loginView import LoginView
from base.BaseDriver_one import BaseDriverOne
from base.TestCaase import TestCase_
from base.BaseReadCfg import ReadData
import time
import logging


class CashierTest(BaseDriverOne, TestCase_):
    
    # 登录操作
    def login_action(self):
        login = LoginView(self.driver)
        data = login.get_csv_data('../data/product_data/loginView.csv', 1)
        login.login_action(data[0], data[2])

    # 正常收银
    def test_01_cashier_case(self):
        """正常收银"""
        self.login_action()
        # 销售之前商品库存数
        logging.info('开始收银')
        cashier = CashierView(self.driver)
        cashier.cashier_goods(num=30)
        time.sleep(1)
        sales_order_num = cashier.get_sales_order_num()
        ReadData().write_data('sale_order', 'num1', sales_order_num)
        self.assertTrue(cashier.check_transaction_success_status())

    # 商品打折销售
    def test_02_goods_discount_sales_case(self):
        """商品打折销售(1折),订单无优惠"""
        self.login_action()
        cashier = CashierView(self.driver)
        cashier.cashier_goods(num=1, normal=True, good_discount=True, good_value=1)
        sales_order_num = cashier.get_sales_order_num()
        ReadData().write_data('sale_order', 'num2', sales_order_num)
        self.assertTrue(cashier.check_transaction_success_status())
        self.assertEqual(cashier.get_order_price(), r'￥20.00')

    # 商品改价销售
    def test_03_goods_modify_sales_case(self):
        """商品改价销售(￥20.00)，订单无优惠"""
        self.login_action()
        cashier = CashierView(self.driver)
        cashier.cashier_goods(num=1, normal=True, good_modify=True, good_value=20)
        sales_order_num = cashier.get_sales_order_num()
        ReadData().write_data('sale_order', 'num3', sales_order_num)
        self.assertTrue(cashier.check_transaction_success_status())
        self.assertEqual(cashier.get_order_price(), r'￥20.00')

    # 商品打折，订单打折销售
    def test_04_discount_discount_sales_case(self):
        """商品打折(5折)，订单打折销售（5折）"""
        self.login_action()
        cashier = CashierView(self.driver)
        cashier.cashier_goods(num=1, normal=True, good_discount=True, good_value=5, offer=False,
                               order_discount=True, order_value=5)
        sales_order_num = cashier.get_sales_order_num()
        ReadData().write_data('sale_order', 'num4', sales_order_num)
        self.assertTrue(cashier.check_transaction_success_status())
        # self.assertEqual(cashier.get_order_price(), r'￥50.00')

    # 商品改价，订单打折销售
    def test_05_modify_discount_sales_case(self):
        """商品改价(￥100)，订单打折销售（8折）"""
        self.login_action()
        cashier = CashierView(self.driver)
        cashier.cashier_goods(num=1, normal=True, good_modify=True, good_value=100, offer=False,
                               order_discount=True, order_value=8)
        sales_order_num = cashier.get_sales_order_num()
        ReadData().write_data('sale_order', 'num5', sales_order_num)
        self.assertTrue(cashier.check_transaction_success_status())

    # 商品打折，订单改价销售
    def test_06_discount_modify_sales_case(self):
        """商品打折（5折），订单改价（￥88）"""
        self.login_action()
        cashier = CashierView(self.driver)
        cashier.cashier_goods(num=1, normal=True, good_discount=True, good_value=5, offer=False,
                               order_modify=True, order_value=88)
        sales_order_num = cashier.get_sales_order_num()
        ReadData().write_data('sale_order', 'num6', sales_order_num)
        self.assertTrue(cashier.check_transaction_success_status())

    # 商品改价，订单改价销售
    def test_07_modify_modify_sales_case(self):
        """商品改价(￥100)，订单改价（￥88）"""
        self.login_action()
        cashier = CashierView(self.driver)
        cashier.cashier_goods(num=1, normal=True, good_modify=True, good_value=100, offer=False,
                               order_modify=True, order_value=88)
        sales_order_num = cashier.get_sales_order_num()
        ReadData().write_data('sale_order', 'num7', sales_order_num)
        self.assertTrue(cashier.check_transaction_success_status())

    # 订单打折销售
    def test_08_order_discount_sales_case(self):
        """商品无优惠，订单打折（5）"""
        self.login_action()
        cashier = CashierView(self.driver)
        cashier.cashier_goods(num=1, offer=False, order_discount=True, order_value=5)
        sales_order_num = cashier.get_sales_order_num()
        ReadData().write_data('sale_order', 'num8', sales_order_num)
        self.assertTrue(cashier.check_transaction_success_status())

    # 商品改价，订单改价销售
    def test_09_order_modify_sales_case(self):
        """商品无优惠，订单改价（￥88）"""
        self.login_action()
        cashier = CashierView(self.driver)
        cashier.cashier_goods(num=1, offer=False, order_modify=True, order_value=88)
        sales_order_num = cashier.get_sales_order_num()
        ReadData().write_data('sale_order', 'num9', sales_order_num)
        self.assertTrue(cashier.check_transaction_success_status())
        # self.assertEqual(cashier.get_order_price(), r'￥88.00')

    # # 开启抹零,商品打折销售
    # def test_10_goods_discount_moling_case(self):
    #     """商品打折，抹零销售"""
    #     self.login_action()
    #     cashier = CashierView(self.driver)
    #     cashier.moling_switch(True)
    #     cashier.goods_modify_discount(1, '打折', 3, True)
    #     cashier.order_modify_discount('无优惠')
    #     sales_order_num = cashier.get_sales_order_num()
    #     ReadData().write_data('sale_order', 'num10', sales_order_num)
    #     self.assertTrue(cashier.check_transaction_success_status())
    #     # self.assertEqual(cashier.get_order_price(), r'￥27.00')

    # def test_11_goods_modify_moling_case(self):
    #     """商品改价，抹零销售"""
    #     self.login_action()
    #     cashier = CashierView(self.driver)
    #     cashier.moling_switch(True)
    #     cashier.goods_modify_discount(1, '改价', 100.33, True)
    #     cashier.order_modify_discount('无优惠')
    #     sales_order_num = cashier.get_sales_order_num()
    #     ReadData().write_data('sale_order', 'num11', sales_order_num)
    #     self.assertTrue(cashier.check_transaction_success_status())
    #     # self.assertEqual(cashier.get_order_price(), r'￥100.00')
    #
    # def test_12_discount_discount_moling_case(self):
    #     """商品打折，订单打折,抹零销售"""
    #     self.login_action()
    #     cashier = CashierView(self.driver)
    #     cashier.moling_switch(True)
    #     cashier.goods_modify_discount(1, '打折', 8, True)
    #     cashier.order_modify_discount('打折', 5)
    #     sales_order_num = cashier.get_sales_order_num()
    #     ReadData().write_data('sale_order', 'num12', sales_order_num)
    #     self.assertTrue(cashier.check_transaction_success_status())
    #     # self.assertEqual(cashier.get_order_price(), r'￥36.00')
    #
    # def test_13_modify_discount_moling_case(self):
    #     """商品改价，订单打折,抹零销售"""
    #     self.login_action()
    #     cashier = CashierView(self.driver)
    #     cashier.moling_switch(True)
    #     cashier.goods_modify_discount(1, '改价', 100.5, True)
    #     cashier.order_modify_discount('打折', 8)
    #     sales_order_num = cashier.get_sales_order_num()
    #     ReadData().write_data('sale_order', 'num13', sales_order_num)
    #     self.assertTrue(cashier.check_transaction_success_status())
    #     # self.assertEqual(cashier.get_order_price(), r'￥80.00')
    #
    # def test_14_order_discount_moling_case(self):
    #     """订单打折,抹零销售"""
    #     self.login_action()
    #     cashier = CashierView(self.driver)
    #     cashier.moling_switch(True)
    #     cashier.choose_goods_action(1, True)
    #     cashier.order_modify_discount('打折', 8)
    #     sales_order_num = cashier.get_sales_order_num()
    #     ReadData().write_data('sale_order', 'num14', sales_order_num)
    #     self.assertTrue(cashier.check_transaction_success_status())
    #     # self.assertEqual(cashier.get_order_price(), r'￥72.00')
    #
    # def test_15_order_modify_moling_case(self):
    #     """订单改价，抹零销售"""
    #     self.login_action()
    #     cashier = CashierView(self.driver)
    #     cashier.moling_switch(True)
    #     cashier.choose_goods_action(1, True)
    #     cashier.order_modify_discount('改价', 88.88)
    #     sales_order_num = cashier.get_sales_order_num()
    #     ReadData().write_data('sale_order', 'num15', sales_order_num)
    #     self.assertTrue(cashier.check_transaction_success_status())
    #     # self.assertEqual(cashier.get_order_price(), r'￥88.88')
    #
    # def test_16_moling_case(self):
    #     """抹零销售"""
    #     self.login_action()
    #     cashier = CashierView(self.driver)
    #     cashier.moling_switch(True)
    #     cashier.choose_goods_action(1, True)
    #     cashier.order_modify_discount('无优惠')
    #     sales_order_num = cashier.get_sales_order_num()
    #     ReadData().write_data('sale_order', 'num16', sales_order_num)
    #     self.assertTrue(cashier.check_transaction_success_status())
    #     # self.assertEqual(cashier.get_order_price(), r'￥90.00')
