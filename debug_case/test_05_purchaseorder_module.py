# coding:utf-8
from PO.business.purchaseorder_module import PurchaseOrderBusiness
from PO.business.login_module import LoginBusiness
from base.BaseDriver_one import BaseDriverOne
from base.TestCaase import TestCase_
from base.BaseReadCfg import ReadData


class PurchaseOrderTest(BaseDriverOne, TestCase_):

    # 登录操作
    def login_action(self):
        login = LoginBusiness(self.driver)
        data = login.get_csv_data('../data/product_data/login_data.csv', 1)
        login.login_action(data[0], data[2])

    # 采购单筛选用例
    def test_05001_purchase_order_filer_case(self):
        """关键字筛选(单号)"""
        self.login_action()
        purchaseorder = PurchaseOrderBusiness(self.driver)
        ordernum = ReadData().get_data('product_purchase_order', 'num1')
        purchaseorder.purchaseorder_action(keyword=ordernum)
        detail_ordernum = purchaseorder.get_detail_ptuchase_order()
        self.assertEqual(ordernum, detail_ordernum)

    def test_05002_purchase_order_filer_case(self):
        """关键字筛选(备注)"""
        self.login_action()
        purchaseorder = PurchaseOrderBusiness(self.driver)
        ordernum = ReadData().get_data('product_purchase_order', 'num7')
        purchaseorder.purchaseorder_action(keyword="采购商品备注")
        detail_ordernum = purchaseorder.get_detail_ptuchase_order()
        self.assertEqual(ordernum, detail_ordernum)

    def test_05003_purchase_order_filer_case(self):
        """结算账户筛选（现金）"""
        self.login_action()
        purchaseorder = PurchaseOrderBusiness(self.driver)
        ordernum = ReadData().get_data('product_purchase_order', 'num9')
        purchaseorder.purchaseorder_action(settlement="现金")
        detail_ordernum = purchaseorder.get_detail_ptuchase_order()
        self.assertEqual(ordernum, detail_ordernum)

    def test_05004_purchase_order_filer_case(self):
        """结算账户筛选（银行卡）"""
        self.login_action()
        purchaseorder = PurchaseOrderBusiness(self.driver)
        ordernum = ReadData().get_data('product_purchase_order', 'num4')
        purchaseorder.purchaseorder_action(settlement="银行卡")
        detail_ordernum = purchaseorder.get_detail_ptuchase_order()
        self.assertEqual(ordernum, detail_ordernum)

    def test_05005_purchase_order_filer_case(self):
        """结算账户筛选（支付宝账户）"""
        self.login_action()
        purchaseorder = PurchaseOrderBusiness(self.driver)
        ordernum = ReadData().get_data('product_purchase_order', 'num5')
        purchaseorder.purchaseorder_action(settlement="支付宝账户")
        detail_ordernum = purchaseorder.get_detail_ptuchase_order()
        self.assertEqual(ordernum, detail_ordernum)

    def test_05006_purchase_order_filer_case(self):
        """结算账户筛选（现金）"""
        self.login_action()
        purchaseorder = PurchaseOrderBusiness(self.driver)
        ordernum = ReadData().get_data('product_purchase_order', 'num6')
        purchaseorder.purchaseorder_action(settlement="微信支付账户")
        detail_ordernum = purchaseorder.get_detail_ptuchase_order()
        self.assertEqual(ordernum, detail_ordernum)

    def test_05007_purchase_order_filer_case(self):
        """供应商名称筛选"""
        self.login_action()
        purchaseorder = PurchaseOrderBusiness(self.driver)
        ordernum = ReadData().get_data('product_purchase_order', 'num9')
        purchaseorder.purchaseorder_action(supplier_name='李洲全供应商1')
        detail_ordernum = purchaseorder.get_detail_ptuchase_order()
        self.assertEqual(ordernum, detail_ordernum)

    # 采购单作废用例
    def test_05008_obsolete_purchase_order_case(self):
        """采购单作废"""
        self.login_action()
        purchaseorder = PurchaseOrderBusiness(self.driver)
        ordernum = ReadData().get_data('product_purchase_order', 'num2')
        purchaseorder.purchaseorder_action(keyword=ordernum, obsolete=True)
        self.assertTrue(purchaseorder.check_obsolete_status())

    # 复制订单用例
    def test_05009_copy_purchase_order_case(self):
        """复制采购单"""
        self.login_action()
        purchaseorder = PurchaseOrderBusiness(self.driver)
        ordernum = ReadData().get_data('product_purchase_order', 'num4')
        purchaseorder.purchaseorder_action(keyword=ordernum, copy=True, copy_supplier_name="李洲全供应商1")
        order_num = purchaseorder.get_detail_ptuchase_order()
        ReadData().write_data('product_purchase_order', 'num10', order_num)
        # 设置检查点
        self.assertTrue(purchaseorder.check_transaction_success_status())

    def test_05010_purchase_order_filer_case(self):
        """无退货进行筛选"""
        self.login_action()
        purchaseorder = PurchaseOrderBusiness(self.driver)
        ordernum = ReadData().get_data('product_purchase_order', 'num10')
        purchaseorder.purchaseorder_action(returned=False)
        detail_ordernum = purchaseorder.get_detail_ptuchase_order()
        self.assertEqual(ordernum, detail_ordernum)

    def test_05011_purchase_order_filer_case(self):
        """正常状态筛选"""
        self.login_action()
        purchaseorder = PurchaseOrderBusiness(self.driver)
        ordernum = ReadData().get_data('product_purchase_order', 'num10')
        purchaseorder.purchaseorder_action(status=True)
        detail_ordernum = purchaseorder.get_detail_ptuchase_order()
        self.assertEqual(ordernum, detail_ordernum)

    def test_05012_purchase_order_return_case(self):
        """采购单退货"""
        self.login_action()
        purchaseorder = PurchaseOrderBusiness(self.driver)
        ordernum = ReadData().get_data('product_purchase_order', 'num1')
        purchaseorder.purchaseorder_action(keyword=ordernum, is_return=True)
        return_dict = purchaseorder.get_purchaseorder_return_information()
        self.assertTrue(return_dict["status"])

    def test_05013_purchase_order_return_case(self):
        """采购单改价退货"""
        self.login_action()
        purchaseorder = PurchaseOrderBusiness(self.driver)
        ordernum = ReadData().get_data('product_purchase_order', 'num1')
        purchaseorder.purchaseorder_action(keyword=ordernum, is_return=True, modify=True, price=50)
        return_dict = purchaseorder.get_purchaseorder_return_information()
        self.assertTrue(return_dict["status"])
        self.assertEqual(return_dict["return_money"], "￥50.00")

    # 采购单筛选用例
    def test_05014_purchase_order_filer_case(self):
        """关键字筛选(作废单据)"""
        self.login_action()
        purchaseorder = PurchaseOrderBusiness(self.driver)
        ordernum = ReadData().get_data('product_purchase_order', 'num2')
        purchaseorder.purchaseorder_action(status=False)
        detail_ordernum = purchaseorder.get_detail_ptuchase_order()
        self.assertEqual(ordernum, detail_ordernum)

    # 采购单筛选用例
    def test_05015_purchase_order_filer_case(self):
        """关键字筛选(退货)"""
        self.login_action()
        purchaseorder = PurchaseOrderBusiness(self.driver)
        ordernum = ReadData().get_data('product_purchase_order', 'num1')
        purchaseorder.purchaseorder_action(returned=True)
        detail_ordernum = purchaseorder.get_detail_ptuchase_order()
        self.assertEqual(ordernum, detail_ordernum)
