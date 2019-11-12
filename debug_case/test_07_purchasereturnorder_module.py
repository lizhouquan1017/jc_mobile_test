# coding:utf-8
from PO.business import PurchaseReturnOrderView
from PO.business.login_module import LoginView
from base.BaseDriver_one import BaseDriverOne
from base.TestCaase import TestCase_
from base.BaseReadCfg import ReadData


class PurchaseReturnOrderTest(BaseDriverOne, TestCase_):

    # 登录操作
    def login_action(self):
        login = LoginView(self.driver)
        data = login.get_csv_data('../data/product_data/loginView.csv', 1)
        login.login_action(data[0], data[2])

    # 采购退货单筛选
    def test_01_purchase_return_order(self):
        """正常筛选"""
        self.login_action()
        p = PurchaseReturnOrderView(self.driver)
        purchase_return_order = ReadData().get_data('product_purchase_return_order', 'num1')
        p.purchase_return_order_action(keyword=purchase_return_order)
        confim_num = p.get_detail_ptuchase_order()
        self.assertEqual(purchase_return_order, confim_num)

    def test_02_purchase_return_order(self):
        """采购退货单作废"""
        self.login_action()
        p = PurchaseReturnOrderView(self.driver)
        purchase_return_order = ReadData().get_data('product_purchase_return_order', 'num2')
        p.purchase_return_order_action(keyword=purchase_return_order, obsolete=True)
        self.assertTrue(p.check_obsolete_status_())

    def test_03_purchase_return_order(self):
        """作废单据筛选"""
        self.login_action()
        p = PurchaseReturnOrderView(self.driver)
        purchase_return_order = ReadData().get_data('product_purchase_return_order', 'num2')
        p.purchase_return_order_action(status=False)
        confim_num = p.get_detail_ptuchase_order()
        self.assertEqual(purchase_return_order, confim_num)

    def test_04_purchase_return_order(self):
        """单据复制（原单退货）"""
        self.login_action()
        p = PurchaseReturnOrderView(self.driver)
        purchase_return_order = ReadData().get_data('product_purchase_return_order', 'num3')
        p.purchase_return_order_action(keyword=purchase_return_order, copy=True, supplier_name='李洲全供应商1', is_original=True)
        purchase_return_num = p.get_detail_ptuchase_order()
        ReadData().write_data('product_purchase_return_order', 'num19', purchase_return_num)
        self.assertTrue(p.check_purchase_return_status())

    def test_05_purchase_return_order(self):
        """单据复制（直接退货）"""
        self.login_action()
        p = PurchaseReturnOrderView(self.driver)
        purchase_return_order = ReadData().get_data('product_purchase_return_order', 'num10')
        p.purchase_return_order_action(keyword=purchase_return_order, copy=True, supplier_name='李洲全供应商1')
        purchase_return_num = p.get_detail_ptuchase_order()
        ReadData().write_data('product_purchase_return_order', 'num20', purchase_return_num)
        self.assertTrue(p.check_purchase_return_status())

    def test_06_purchase_return_order(self):
        """结算方式（现金）"""
        self.login_action()
        p = PurchaseReturnOrderView(self.driver)
        p.purchase_return_order_action(settlement='现金')
        settlement_type = p.get_detail_settlement_type()
        self.assertEqual('现金', settlement_type)

    def test_07_purchase_return_order(self):
        """结算方式（银行卡）"""
        self.login_action()
        p = PurchaseReturnOrderView(self.driver)
        p.purchase_return_order_action(settlement='银行卡')
        settlement_type = p.get_detail_settlement_type()
        self.assertEqual('银行卡', settlement_type)

    def test_08_purchase_return_order(self):
        """结算方式（支付宝账户）"""
        self.login_action()
        p = PurchaseReturnOrderView(self.driver)
        p.purchase_return_order_action(settlement='支付宝账户')
        settlement_type = p.get_detail_settlement_type()
        self.assertEqual('支付宝账户', settlement_type)

    def test_09_purchase_return_order(self):
        """结算方式（微信支付账户）"""
        self.login_action()
        p = PurchaseReturnOrderView(self.driver)
        p.purchase_return_order_action(settlement='微信支付账户')
        settlement_type = p.get_detail_settlement_type()
        self.assertEqual('微信支付账户', settlement_type)

    def test_10_purchase_return_order(self):
        """结算方式（其他账户）"""
        self.login_action()
        p = PurchaseReturnOrderView(self.driver)
        p.purchase_return_order_action(settlement='其他账户')
        settlement_type = p.get_detail_settlement_type()
        self.assertEqual('其他账户', settlement_type)
