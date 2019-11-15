# coding:utf-8
from PO.business.purchase_module import PurchaseBusiness
from PO.business.login_module import LoginBusiness
from base.BaseDriver_one import BaseDriverOne
from base.TestCaase import TestCase_
from base.BaseReadCfg import ReadData


class PurchaseTest(BaseDriverOne, TestCase_):

    # 登录操作
    def login_action(self):
        login = LoginBusiness(self.driver)
        data = login.get_csv_data('../data/product_data/login_data.csv', 1)
        login.login_action(data[0], data[2])

    # # 新增供应商
    # def test_01_add_supplier_case(self):
    #     """新增供应商"""
    #     self.login_action()
    #     purchase = PurchaseBusiness(self.driver)
    #     purchase.add_supplier('李洲全供应商1')
    #     # self.assertTrue(purchase.check_supplier_is_exist('李洲全供应商1'))

    # 正常采购用例
    def test_04001_first_purchase_case(self):
        """第一次采购（后选供应商）"""
        self.login_action()
        purchase = PurchaseBusiness(self.driver)
        purchase.pruchase_action(goodname1="测试商品8号", goodnum=10, supplier_name="李洲全供应商1")
        purchase_information = purchase.get_purchase_information()
        purchase_order_num = purchase_information["purchase_order_num"]
        ReadData().write_data('product_purchase_order', 'num1', purchase_order_num)
        self.assertTrue(purchase_information["status"])

    # 正常采购用例
    def test_04002_second_purchase_case(self):
        """第二次采购（后选供应商）"""
        self.login_action()
        purchase = PurchaseBusiness(self.driver)
        purchase.pruchase_action(goodname1="测试商品8号", goodnum=1, supplier_name="李洲全供应商1")
        purchase_information = purchase.get_purchase_information()
        purchase_order_num = purchase_information["purchase_order_num"]
        ReadData().write_data('product_purchase_order', 'num2', purchase_order_num)
        self.assertTrue(purchase_information["status"])

    # 正常采购用例
    def test_04003_second_purchase_case(self):
        """默认结算账号（现金）"""
        self.login_action()
        purchase = PurchaseBusiness(self.driver)
        purchase.pruchase_action(goodname1="测试商品8号", goodnum=1, supplier_name="李洲全供应商1", settlement="现金")
        purchase_information = purchase.get_purchase_information()
        purchase_order_num = purchase_information["purchase_order_num"]
        ReadData().write_data('product_purchase_order', 'num3', purchase_order_num)
        self.assertTrue(purchase_information["status"])

    # 正常采购用例
    def test_04004_second_purchase_case(self):
        """默认结算账号（银行卡）"""
        self.login_action()
        purchase = PurchaseBusiness(self.driver)
        purchase.pruchase_action(goodname1="测试商品8号", goodnum=1, supplier_name="李洲全供应商1", settlement="银行卡")
        purchase_information = purchase.get_purchase_information()
        purchase_order_num = purchase_information["purchase_order_num"]
        ReadData().write_data('product_purchase_order', 'num4', purchase_order_num)
        self.assertTrue(purchase_information["status"])

    # 正常采购用例
    def test_04005_second_purchase_case(self):
        """默认结算账号（支付宝账户）"""
        self.login_action()
        purchase = PurchaseBusiness(self.driver)
        purchase.pruchase_action(goodname1="测试商品8号", goodnum=1, supplier_name="李洲全供应商1", settlement="支付宝账户")
        purchase_information = purchase.get_purchase_information()
        purchase_order_num = purchase_information["purchase_order_num"]
        ReadData().write_data('product_purchase_order', 'num5', purchase_order_num)
        self.assertTrue(purchase_information["status"])

    # 正常采购用例
    def test_04006_second_purchase_case(self):
        """默认结算账号（微信支付账户）"""
        self.login_action()
        purchase = PurchaseBusiness(self.driver)
        purchase.pruchase_action(goodname1="测试商品8号", goodnum=1, supplier_name="李洲全供应商1", settlement="微信支付账户")
        purchase_information = purchase.get_purchase_information()
        purchase_order_num = purchase_information["purchase_order_num"]
        ReadData().write_data('product_purchase_order', 'num6', purchase_order_num)
        self.assertTrue(purchase_information["status"])

    # 正常采购用例
    def test_04007_purchase_multiple_goods_case(self):
        """有备注的采购单"""
        self.login_action()
        purchase = PurchaseBusiness(self.driver)
        purchase.pruchase_action(goodname1="测试商品8号", goodnum=1, supplier_name="李洲全供应商1", price="30",
                                 remark="采购商品备注")
        purchase_information = purchase.get_purchase_information()
        purchase_order_num = purchase_information["purchase_order_num"]
        ReadData().write_data('product_purchase_order', 'num7', purchase_order_num)
        # 判断采购是否正常，采购单单号是否一致，商品库存是否增加
        self.assertTrue(purchase_information["status"])

    # 正常采购用例
    def test_04008_purchase_multiple_goods_case(self):
        """采购多种商品"""
        self.login_action()
        purchase = PurchaseBusiness(self.driver)
        purchase.pruchase_action(goodname1="测试商品8号", goodname2="测试商品3号", goodnum=1, supplier_name="李洲全供应商1")
        purchase_information = purchase.get_purchase_information()
        purchase_order_num = purchase_information["purchase_order_num"]
        ReadData().write_data('product_purchase_order', 'num8', purchase_order_num)
        self.assertTrue(purchase_information["status"])

    # 采购改价用例
    def test_04009_purchase_modfiy_price_case(self):
        """采购进货修改价格采购成功"""
        self.login_action()
        purchase = PurchaseBusiness(self.driver)
        purchase.pruchase_action(goodname1="测试商品8号", goodnum=1, supplier_name="李洲全供应商1", price="30")
        purchase_information = purchase.get_purchase_information()
        purchase_order_num = purchase_information["purchase_order_num"]
        ReadData().write_data('product_purchase_order', 'num9', purchase_order_num)
        # 判断采购是否正常，采购单单号是否一致，商品库存是否增加
        self.assertTrue(purchase_information["status"])
        self.assertEqual(purchase_information["price"], r'￥30.00')
