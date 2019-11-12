# coding:utf-8
from PO.business import PurchaseOrderView
from PO.business.login_module import LoginView
from base.BaseDriver_one import BaseDriverOne
from base.TestCaase import TestCase_
from base.BaseReadCfg import ReadData


class PurchaseOrderTest(BaseDriverOne, TestCase_):

    # 登录操作
    def login_action(self):
        login = LoginView(self.driver)
        data = login.get_csv_data('../data/product_data/login_data.csv', 1)
        login.login_action(data[0], data[2])

    # 采购单筛选用例
    def test_01_purchase_order_filer_case(self):
        """关键字筛选(单号)"""
        self.login_action()
        purchaseorder = PurchaseOrderView(self.driver)
        ordernum = ReadData().get_data('product_purchase_order', 'num1')
        purchaseorder.enter_puchaseorder_interface()
        purchaseorder.filter_order(keyword=ordernum)
        purchaseorder.enter_order_detail()
        detail_ordernum = purchaseorder.get_detail_ptuchase_order()
        self.assertEqual(ordernum, detail_ordernum)

    def test_02_purchase_order_filer_case(self):
        """关键字筛选(备注)"""
        self.login_action()
        purchaseorder = PurchaseOrderView(self.driver)
        ordernum = ReadData().get_data('product_purchase_order', 'num5')
        purchaseorder.enter_puchaseorder_interface()
        purchaseorder.filter_order(keyword='采购两种商品')
        purchaseorder.enter_order_detail()
        detail_ordernum = purchaseorder.get_detail_ptuchase_order()
        self.assertEqual(ordernum, detail_ordernum)

    def test_03_purchase_order_filer_case(self):
        """结算账户筛选（现金）"""
        self.login_action()
        purchaseorder = PurchaseOrderView(self.driver)
        ordernum = ReadData().get_data('product_purchase_order', 'num5')
        purchaseorder.enter_puchaseorder_interface()
        purchaseorder.filter_order(settlement='现金')
        purchaseorder.enter_order_detail()
        detail_ordernum = purchaseorder.get_detail_ptuchase_order()
        self.assertEqual(ordernum, detail_ordernum)

    def test_04_purchase_order_filer_case(self):
        """供应商名称筛选"""
        self.login_action()
        purchaseorder = PurchaseOrderView(self.driver)
        ordernum = ReadData().get_data('product_purchase_order', 'num5')
        purchaseorder.enter_puchaseorder_interface()
        purchaseorder.filter_order(supplier_name='李洲全供应商1')
        purchaseorder.enter_order_detail()
        detail_ordernum = purchaseorder.get_detail_ptuchase_order()
        self.assertEqual(ordernum, detail_ordernum)

    def test_05_purchase_order_filer_case(self):
        """无退货进行筛选"""
        self.login_action()
        purchaseorder = PurchaseOrderView(self.driver)
        ordernum = ReadData().get_data('product_purchase_order', 'num5')
        purchaseorder.enter_puchaseorder_interface()
        purchaseorder.filter_order(returned=True)
        purchaseorder.enter_order_detail()
        detail_ordernum = purchaseorder.get_detail_ptuchase_order()
        self.assertEqual(ordernum, detail_ordernum)

    def test_06_purchase_order_filer_case(self):
        """正常状态筛选"""
        self.login_action()
        purchaseorder = PurchaseOrderView(self.driver)
        ordernum = ReadData().get_data('product_purchase_order', 'num5')
        purchaseorder.enter_puchaseorder_interface()
        purchaseorder.filter_order(status=True)
        purchaseorder.enter_order_detail()
        detail_ordernum = purchaseorder.get_detail_ptuchase_order()
        self.assertEqual(ordernum, detail_ordernum)

    # 采购单作废用例
    def test_07_obsolete_purchase_order_case(self):
        """采购单作废"""
        self.login_action()
        purchaseorder = PurchaseOrderView(self.driver)
        ordernum = ReadData().get_data('purchase_order', 'num1')
        purchaseorder.enter_puchaseorder_interface()
        purchaseorder.filter_order(keyword=ordernum)
        purchaseorder.operating_document_action(obsolete=True)

    # 复制订单用例
    def test_08_copy_purchase_order_case(self):
        """复制采购单"""
        self.login_action()
        purchaseorder = PurchaseOrderView(self.driver)
        ordernum = ReadData().get_data('product_purchase_order', 'num2')
        purchaseorder.enter_puchaseorder_interface()
        purchaseorder.filter_order(keyword=ordernum)
        purchaseorder.operating_document_action(copy=True)
        purchaseorder.copy_follow_operation('李洲全供应商1')
        order_num = purchaseorder.get_detail_ptuchase_order()
        ReadData().write_data('product_purchase_order', 'num6', order_num)
        # 设置检查点
        self.assertTrue(purchaseorder.check_transaction_success_status())

    def test_09_purchase_order_return_case(self):
        """采购单退货"""
        self.login_action()
        purchaseorder = PurchaseOrderView(self.driver)
        ordernum = ReadData().get_data('product_purchase_order', 'num3')
        purchaseorder.enter_puchaseorder_interface()
        purchaseorder.filter_order(keyword=ordernum)
        purchaseorder.purchase_order_return()
        self.assertTrue(purchaseorder.get_purchase_return_status())

    def test_10_purchase_order_return_case(self):
        """采购单改价退货"""
        self.login_action()
        purchaseorder = PurchaseOrderView(self.driver)
        ordernum = ReadData().get_data('product_purchase_order', 'num4')
        purchaseorder.enter_puchaseorder_interface()
        purchaseorder.filter_order(keyword=ordernum)
        purchaseorder.purchase_order_return(modify=True, price=50)
        self.assertTrue(purchaseorder.get_purchase_return_status())

    # 采购单筛选用例
    def test_11_purchase_order_filer_case(self):
        """关键字筛选(作废单据)"""
        self.login_action()
        purchaseorder = PurchaseOrderView(self.driver)
        ordernum = ReadData().get_data('product_obsolete_purchase_order', 'num1')
        purchaseorder.enter_puchaseorder_interface()
        purchaseorder.filter_order(status=False)
        purchaseorder.enter_order_detail()
        detail_ordernum = purchaseorder.get_detail_ptuchase_order()
        self.assertEqual(ordernum, detail_ordernum)

    # 采购单筛选用例
    def test_12_purchase_order_filer_case(self):
        """关键字筛选(退货)"""
        self.login_action()
        purchaseorder = PurchaseOrderView(self.driver)
        ordernum = ReadData().get_data('product_purchase_order', 'num4')
        purchaseorder.enter_puchaseorder_interface()
        purchaseorder.filter_order(returned=True)
        purchaseorder.enter_order_detail()
        detail_ordernum = purchaseorder.get_detail_ptuchase_order()
        self.assertEqual(ordernum, detail_ordernum)
