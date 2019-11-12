# coding:utf-8
from PO.business import PurchaseView
from PO.business.login_module import LoginView
from base.BaseDriver_one import BaseDriverOne
from base.TestCaase import TestCase_
from base.BaseReadCfg import ReadData


class PurchaseTest(BaseDriverOne, TestCase_):

    # 登录操作
    def login_action(self):
        login = LoginView(self.driver)
        data = login.get_csv_data('../data/product_data/loginView.csv', 1)
        login.login_action(data[0], data[2])

    # 新增供应商
    def test_01_add_supplier_case(self):
        """新增供应商"""
        self.login_action()
        purchase = PurchaseView(self.driver)
        purchase.add_supplier('李洲全供应商1')
        self.assertTrue(purchase.check_supplier_is_exist('李洲全供应商1'))

    # 正常采购用例
    def test_02_first_purchase_case(self):
        """第一次采购（后选供应商）"""
        self.login_action()
        purchase = PurchaseView(self.driver)
        purchase.enter_purchase_interface()
        purchase.choose_goods_action('测试商品8号', 1)
        purchase.choose_supplier('李洲全供应商1')
        purchase.define_storage_action()
        purchase_order_num = purchase.get_purchase_order_num()
        ReadData().write_data('product_purchase_order', 'num1', purchase_order_num)
        self.assertTrue(purchase.check_transaction_success_status())

    # 正常采购用例
    def test_03_second_purchase_case(self):
        """第二次采购（后选供应商）"""
        self.login_action()
        purchase = PurchaseView(self.driver)
        purchase.enter_purchase_interface()
        purchase.choose_supplier('李洲全供应商1')
        purchase.choose_goods_action('测试商品8号', 30)
        purchase.define_storage_action()
        purchase_order_num = purchase.get_purchase_order_num()
        ReadData().write_data('product_purchase_order', 'num2', purchase_order_num)
        self.assertTrue(purchase.check_transaction_success_status())

    # 正常采购用例
    def test_04_purchase_multiple_goods_case(self):
        """采购多种商品"""
        self.login_action()
        purchase = PurchaseView(self.driver)
        purchase.enter_purchase_interface()
        purchase.choose_goods_action('测试商品8号', 1)
        purchase.choose_goods_action('测试商品3号', 1)
        purchase.choose_supplier('李洲全供应商1')
        purchase.define_storage_action()
        purchase_order_num = purchase.get_purchase_order_num()
        ReadData().write_data('product_purchase_order', 'num3', purchase_order_num)
        self.assertTrue(purchase.check_transaction_success_status())

    # 采购改价用例
    def test_05_purchase_modfiy_price_case(self):
        """采购进货修改价格采购成功"""
        self.login_action()
        purchase = PurchaseView(self.driver)
        purchase.enter_purchase_interface()
        purchase.choose_supplier('李洲全供应商1')
        purchase.choose_goods_action('测试商品8号', 1)
        purchase.modfiy_price_action(str(30))
        purchase.define_storage_action()
        purchase_order_num = purchase.get_purchase_order_num()
        ReadData().write_data('product_purchase_order', 'num4', purchase_order_num)
        purchase_price = purchase.get_order_price()
        # 判断采购是否正常，采购单单号是否一致，商品库存是否增加
        self.assertTrue(purchase.check_transaction_success_status())
        self.assertEqual(purchase_price, r'￥30.00')

    # 正常采购用例
    def test_06_purchase_multiple_goods_case(self):
        """有备注的采购单"""
        self.login_action()
        purchase = PurchaseView(self.driver)
        purchase.enter_purchase_interface()
        purchase.choose_goods_action('测试商品8号', 1)
        purchase.choose_goods_action('测试商品3号', 1)
        purchase.choose_supplier('李洲全供应商1')
        purchase.edit_remarks('采购两种商品')
        purchase.define_storage_action()
        purchase_order_num = purchase.get_purchase_order_num()
        ReadData().write_data('product_purchase_order', 'num5', purchase_order_num)
        # 判断采购是否正常，采购单单号是否一致，商品库存是否增加
        self.assertTrue(purchase.check_transaction_success_status())
