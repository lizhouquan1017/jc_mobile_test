# -*- coding:utf-8 -*-
__author__ = "lizhouquan"

from base.BaseDriver_one import BaseDriverOne
from base.TestCaase import TestCase_
from business.loginView import LoginView
from business.registerView import RegisterView
from business.findPwdView import FindPwdView
from business.purchaseView import PurchaseView
from business.purchaseorderView import PurchaseOrderView
from business.purchasereturnView import PurchaseReturnView
from business.purchasereturnorderView import PurchaseReturnOrderView
from business.goodsView import GoodsViews
from business.cashierView import CashierView
from business.salesorderView import SalesOrderView
from business.salesreturnView import SalesReturnView
from base.BaseReadCfg import ReadData
from time import sleep
import logging
import random

num = random.randint(100000, 999999)
pwd = 'ab'+str(num)


class ProdcutEnviromentTest(BaseDriverOne, TestCase_):

    # 登录操作
    def login_action(self):
        login = LoginView(self.driver)
        data = login.get_csv_data('../data/product_data/loginView.csv', 1)
        login.login_action(data[0], data[2])
        sleep(2)

    def test_001_add_case(self):
        """正常添加商品"""
        """
        商品名称，成本价，零售价，颜色属性，尺码属性 ：必填
        """
        self.login_action()
        goods = GoodsViews(self.driver)
        goods.enter_goods_list()
        goods.type_must_field('测试商品1号', 100, 200, '均色', '均码')
        goods.confirm_add_goods()
        status = goods.check_success_status()
        goods.get_goods_details()
        goods_num = goods.get_goods_num()
        sku_num = goods.get_sku_barcode()
        ReadData().write_data('product_goods_bar_code', 'num1', goods_num)
        ReadData().write_data('product_goods_single_barcode', 'num1', sku_num)
        self.assertEqual('添加新品成功', status)

    def test_002_add_case(self):
        """自定义商品货号添加商品"""
        """
        商品名称，成本价，零售价，颜色属性，尺码属性 ：必填
        商品货号，库存数，商品条码，商品备注，其他参数： 非必填
        """
        self.login_action()
        goods = GoodsViews(self.driver)
        goods.enter_goods_list()
        goods.type_must_field('测试商品2号', 100, 200, '均色', '均码', 19891017)
        goods.confirm_add_goods()
        status = goods.check_success_status()
        goods.get_goods_details()
        goods_num = goods.get_goods_num()
        sku_code = goods.get_sku_barcode()
        ReadData().write_data('product_goods_bar_code', 'num2', goods_num)
        ReadData().write_data('product_goods_single_barcode', 'num2', sku_code)
        self.assertEqual('添加新品成功', status)

    def test_003_add_case(self):
        """自定义商品货号添加商品,添加初始库存"""
        """
        商品名称，成本价，零售价，颜色属性，尺码属性 ：必填
        商品货号，库存数，商品条码，商品备注，其他参数： 非必填
        """
        self.login_action()
        goods = GoodsViews(self.driver)
        goods.enter_goods_list()
        goods.type_must_field('测试商品3号', 100, 200, '均色', '均码', 19891018, 10)
        goods.confirm_add_goods()
        status = goods.check_success_status()
        goods.get_goods_details()
        goods_code = goods.get_goods_num()
        sku_code = goods.get_sku_barcode()
        ReadData().write_data('product_goods_bar_code', 'num3', goods_code)
        ReadData().write_data('product_goods_single_barcode', 'num3', sku_code)
        self.assertEqual('添加新品成功', status)

    def test_004_add_case(self):
        """自定义商品货号添加商品,添加初始库存，添加商品条码"""
        """
        商品名称，成本价，零售价，颜色属性，尺码属性 ：必填
        商品货号，库存数，商品条码，商品备注，其他参数： 非必填
        """
        self.login_action()
        goods = GoodsViews(self.driver)
        goods.enter_goods_list()
        goods.type_must_field('测试商品4号', 50, '200', '均色', '均码', 19891019, 30, '20190916-01')
        goods.confirm_add_goods()
        status = goods.check_success_status()
        goods.get_goods_details()
        goods_num = goods.get_goods_num()
        sku_code = goods.get_sku_barcode()
        ReadData().write_data('product_goods_bar_code', 'num4', goods_num)
        ReadData().write_data('product_goods_single_barcode', 'num4', sku_code)
        self.assertEqual('添加新品成功', status)

    def test_005_add_case(self):
        """自定义商品货号添加商品,添加初始库存，添加商品条码,添加备注"""
        """
        商品名称，成本价，零售价，颜色属性，尺码属性 ：必填
        商品货号，库存数，商品条码，商品备注，其他参数： 非必填
        """
        self.login_action()
        goods = GoodsViews(self.driver)
        goods.enter_goods_list()
        goods.type_must_field('测试商品5号', 100, 200, '均色', '均码', 19891020, 30, '20190917-01', '测试商品备注')
        goods.confirm_add_goods()
        status = goods.check_success_status()
        goods.get_goods_details()
        goods_num = goods.get_goods_num()
        sku_code = goods.get_sku_barcode()
        ReadData().write_data('product_goods_bar_code', 'num5', goods_num)
        ReadData().write_data('product_goods_single_barcode', 'num5', sku_code)
        self.assertEqual('添加新品成功', status)

    # 商品下架
    def test_006_obtained_case(self):
        """商品下架功能"""
        self.login_action()
        goods = GoodsViews(self.driver)
        goods.enter_goods_list()
        goods.goods_obtained_action('测试商品5号')
        status = goods.check_obtained_status()
        self.assertEqual('该商品已下架', status)

    # 商品上架
    def test_007_shelf_case(self):
        """商品上架"""
        self.login_action()
        goods = GoodsViews(self.driver)
        goods.enter_goods_list()
        goods.goods_shelf_action('测试商品5号')
        self.assertTrue(goods.check_shelf_status('测试商品5号'))

    # 商品删除操作
    def test_008_delete_case(self):
        """删除商品"""
        self.login_action()
        goods = GoodsViews(self.driver)
        goods.enter_goods_list()
        goods.goods_delete_action()
        self.assertTrue(goods.check_goods_is_not_exist('测试商品5号'))

    # 列表编辑
    def test_009_edit_case(self):
        """"列表编辑商品"""
        self.login_action()
        goods = GoodsViews(self.driver)
        goods.enter_goods_list()
        goods.list_edit_action('测试商品6号')
        self.assertEqual('测试商品6号', goods.get_goods_names())

    # 列表编辑
    def test_010_edit_case(self):
        """详情编辑商品"""
        self.login_action()
        goods = GoodsViews(self.driver)
        goods.enter_goods_list()
        goods.details_edit_action('测试商品8号')
        self.assertEqual('测试商品8号', goods.get_goods_names())

    # 新增自定义类目
    def test_011_custom_classification(self):
        """新增自定义类目"""
        self.login_action()
        goods = GoodsViews(self.driver)
        goods.enter_goods_list()
        goods.add_custom_classification('自定义分组2')
        self.assertTrue(goods.check_classification_is_exist('自定义分组2'))

    def test_012_user_login(self):
        """正常登录用例"""
        logging.info('==正常账号成功登录用例==')
        login = LoginView(self.driver)
        data = login.get_csv_data('../data/product_data/loginView.csv', 1)
        login.login_action(data[0], data[2])
        sleep(2)
        self.assertTrue(login.check_login_success_status())

    def test_013_user_login_pwderr(self):
        """密码错误登录用例"""
        logging.info('==正确账号密码错误登录=')
        login = LoginView(self.driver)
        data = login.get_csv_data('../data/product_data/loginView.csv', 2)
        login.login_action(data[0], data[1])
        sleep(2)
        self.assertTrue(login.check_login_fail_status())
        # self.assertTrue(login.check_toast_text('用户名或密码错误'))

    def test_014_user_login_pwdempty(self):
        """密码为空登录"""
        logging.info('==正常账号密码为空登录==')
        login = LoginView(self.driver)
        data = login.get_csv_data('../data/product_data/loginView.csv', 3)
        login.login_action(data[0], data[1])
        sleep(2)
        self.assertTrue(login.check_login_fail_status())

    def test_015_user_login_phonenumerror(self):
        """手机号为错误登录"""
        logging.info('==手机号格式错误登录==')
        login = LoginView(self.driver)
        data = login.get_csv_data('../data/product_data/loginView.csv', 4)
        login.login_action(data[0], data[1])
        sleep(2)
        self.assertTrue(login.check_login_fail_status())

    def test_016_user_login_unregistered(self):
        """未注册账号登录"""
        logging.info('==未注册账号登录==')
        login = LoginView(self.driver)
        data = login.get_csv_data('../data/product_data/loginView.csv', 5)
        login.login_action(data[0], data[1])
        sleep(2)
        self.assertTrue(login.check_login_fail_status())

    def test_017_user_login_phonenumEmpty(self):
        """ 手机号为空登录"""
        logging.info('==手机号为空登录==')
        login = LoginView(self.driver)
        data = login.get_csv_data('../data/product_data/loginView.csv', 6)
        login.login_action(data[0], data[1])
        sleep(2)
        self.assertTrue(login.check_login_fail_status())

    def test_018_user_login_RestrictedAccounts(self):
        """限制账号登录"""
        logging.info('==限制账号登录==')
        login = LoginView(self.driver)
        data = login.get_csv_data('../data/product_data/loginView.csv', 7)
        login.login_action(data[0], data[1])
        sleep(2)
        self.assertTrue(login.check_login_fail_status())

    def test_019_user_login_DeactivatedAccount(self):
        """停用账号登录"""
        logging.info('==停用账号登录==')
        login = LoginView(self.driver)
        data = login.get_csv_data('../data/product_data/loginView.csv', 8)
        login.login_action(data[0], data[1])
        sleep(2)
        self.assertTrue(login.check_login_fail_status())

    def test_020_user_login_VerificationCode(self):
        """验证码登录"""
        logging.info('==验证码登录==')
        login = LoginView(self.driver)
        data = login.get_csv_data('../data/product_data/loginView.csv', 9)
        login.login_code_action(data[0], data[1])
        sleep(2)
        self.assertTrue(login.check_login_success_status())

    def test_021_user_login_ExperienceAccount(self):
        """体验账号登录"""
        logging.info('==体验账号登录==')
        login = LoginView(self.driver)
        login.login_experience_account_action()
        sleep(2)
        self.assertTrue(login.check_login_success_status())

    def test_022_user_login_VerificationCodeEmpty(self):
        """验证码为空登录"""
        logging.info('==验证码为空登录==')
        login = LoginView(self.driver)
        data = login.get_csv_data('../data/product_data/loginView.csv', 10)
        login.login_code_action(data[0], data[1])
        sleep(2)
        self.assertTrue(login.check_login_fail_status())

    def test_023_user_login_VerificationCodeError(self):
        """验证码错误登录"""
        logging.info('==验证码错误登录==')
        login = LoginView(self.driver)
        data = login.get_csv_data('../data/product_data/loginView.csv', 11)
        login.login_code_action(data[0], data[1])
        sleep(2)
        self.assertTrue(login.check_login_fail_status())

    # 正常注册
    def test_024_user_register(self):
        """正常注册"""
        logging.info('=用户正常注册成功=')
        register = RegisterView(self.driver)
        data = register.get_csv_data('../data/product_data/register.csv', 1)
        register.register_action(data[0], data[2], data[3])
        newdata = str(int(data[0])+1)
        self.assertTrue(register.check_register_success_status())
        sleep(2)
        register.update_csv_data('../data/product_data/register.csv', 1, '用户正常注册', data[0], newdata)

    # 注册手机号为空
    def test_025_register_phonenumEmpty(self):
        """注册手机号为空"""
        logging.info('=用户注册手机号码为空=')
        register = RegisterView(self.driver)
        data = register.get_csv_data('../data/product_data/register.csv', 2)
        register.register_common_action(data[0], data[1], data[2])
        sleep(2)
        self.assertTrue(register.check_register_fail_status())

    # 注册手机号格式不正确
    def test_026_register_phonenumError(self):
        """注册手机号格式不正确"""
        logging.info('=用户注册手机号格式错误=')
        register = RegisterView(self.driver)
        data = register.get_csv_data('../data/product_data/register.csv', 3)
        register.register_common_action(data[0], data[1], data[2])
        sleep(2)
        self.assertTrue(register.check_register_fail_status())

    # 注册手机号已注册
    def test_027_registered(self):
        """注册手机号已注册"""
        logging.info('=用户手机号已注册=')
        register = RegisterView(self.driver)
        data = register.get_csv_data('../data/product_data/register.csv', 4)
        register.register_common_action(data[0], data[1], data[2])
        sleep(2)
        self.assertTrue(register.check_register_fail_status())

    # 修改密码成功
    def test_028_modify_pwdSuccess(self):
        """修改密码成功"""
        logging.info(r'==修改密码成功用例==')
        find = FindPwdView(self.driver)
        data0 = find.get_csv_data('../data/product_data/loginView.csv', 1)
        data1 = find.get_csv_data('../data/product_data/pwd.csv', 10)
        data2 = find.get_csv_data('../data/product_data/pwd.csv', 11)
        find.findpwd_action(data0[0], data1[2])
        find.modify_action(data1[3], data1[3])
        sleep(2)
        self.assertTrue(find.check_find_pwd_success_status())
        find.update_csv_data('../data/product_data/loginView.csv', 1, '正式账号', data0[2], data1[3])
        find.update_csv_data('../data/product_data/pwd.csv', 1, '密码相同', data2[3], data1[3])
        logging.info(pwd)
        find.update_csv_data('../data/product_data/pwd.csv', 1, '修改密码', data1[3], pwd)

    # 手机号为空找回密码
    def test_029_findpwd_phoneNumEmpty(self):
        """找回密码手机号为空"""
        logging.info(r'==找回密码手机号为空用例==')
        find = FindPwdView(self.driver)
        data = find.get_csv_data('../data/product_data/pwd.csv', 1)
        find.findpwd_action(data[0], data[1])
        sleep(2)
        self.assertTrue(find.check_find_pwd_fail_status())

    # 手机号格式错误找回密码
    def test_030_findpwd_phoneNumError(self):
        """找回密码手机号格式错误"""
        logging.info(r'==找回密码手机号格式错误用例==')
        find = FindPwdView(self.driver)
        data = find.get_csv_data('../data/product_data/pwd.csv', 2)
        find.findpwd_action(data[0], data[1])
        sleep(2)
        self.assertTrue(find.check_find_pwd_fail_status())

    # 未注册手机号找回密码
    def test_031_findpwd_phoneNumUnregistered(self):
        """未注册手机号找回密码"""
        logging.info(r'==未注册手机号找回密码用例==')
        find = FindPwdView(self.driver)
        data = find.get_csv_data('../data/product_data/pwd.csv', 3)
        find.findpwd_action(data[0], data[1])
        sleep(2)
        self.assertTrue(find.check_find_pwd_fail_status())

    # 验证码为空找回密码
    def test_032_findpwd_codeEmpty(self):
        """验证码为空找回密码"""
        logging.info(r'==验证码为空找回密码用例==')
        find = FindPwdView(self.driver)
        data = find.get_csv_data('../data/product_data/pwd.csv', 4)
        find.findpwd_action(data[0], data[1])
        sleep(2)
        self.assertTrue(find.check_find_pwd_fail_status())

    # 验证码错误
    def test_033_findpwd_codeError(self):
        """验证码错误找回密码"""
        logging.info(r'==验证码错误找回密码用例==')
        find = FindPwdView(self.driver)
        data = find.get_csv_data('../data/product_data/pwd.csv', 5)
        find.findpwd_action(data[0], data[1])
        sleep(2)
        self.assertTrue(find.check_find_pwd_fail_status())

    # 修改密码密码为空
    def test_034_modify_pwdEmpty(self):
        """修改密码密码为空"""
        logging.info(r'==修改密码密码为空用例==')
        find = FindPwdView(self.driver)
        data = find.get_csv_data('../data/product_data/pwd.csv', 6)
        find.findpwd_action(data[0], data[1])
        find.modify_action(data[2], data[3])
        sleep(2)
        self.assertTrue(find.check_modify_pwd_fail_status())

    # 修改密码不符合长度
    def test_035_modify_pwdNomatchLength(self):
        """修改密码不符合长度"""
        logging.info(r'==修改密码不符合长度用例==')
        find = FindPwdView(self.driver)
        data = find.get_csv_data('../data/product_data/pwd.csv', 7)
        find.findpwd_action(data[0], data[1])
        find.modify_action(data[2], data[3])
        sleep(2)
        self.assertTrue(find.check_modify_pwd_fail_status())

    # 修改密码不符合规则
    def test_036_modify_pwdNomatchRules(self):
        """修改密码不符合规则"""
        logging.info(r'==修改密码不符合规则用例==')
        find = FindPwdView(self.driver)
        data = find.get_csv_data('../data/product_data/pwd.csv', 8)
        find.findpwd_action(data[0], data[1])
        find.modify_action(data[2], data[3])
        sleep(2)
        self.assertTrue(find.check_modify_pwd_fail_status())

    # 修改密码前后输入不一致
    def test_037_modify_pwdInconsistent(self):
        """修改密码前后不一致"""
        logging.info(r'==修改密码输入前后不一致用例==')
        find = FindPwdView(self.driver)
        data = find.get_csv_data('../data/product_data/pwd.csv', 9)
        find.findpwd_action(data[0], data[1])
        find.modify_action(data[2], data[3])
        sleep(2)
        self.assertTrue(find.check_modify_pwd_fail_status())

    # 修改密码新旧密码重复
    def test_038_modify_pwdRepeat(self):
        """修改密码新旧密码重复"""
        logging.info(r'==修改密码新旧密码重复用例==')
        find = FindPwdView(self.driver)
        data = find.get_csv_data('../data/product_data/pwd.csv', 11)
        find.findpwd_action(data[0], data[2])
        find.modify_action(data[3], data[3])
        sleep(2)
        self.assertTrue(find.check_modify_pwd_fail_status())

    # 新增供应商
    def test_039_add_supplier_case(self):
        """新增供应商"""
        self.login_action()
        purchase = PurchaseView(self.driver)
        purchase.add_supplier('李洲全供应商1')
        self.assertTrue(purchase.check_supplier_is_exist('李洲全供应商1'))

    # 正常采购用例
    def test_040_first_purchase_case(self):
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
    def test_041_second_purchase_case(self):
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
    def test_042_purchase_multiple_goods_case(self):
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
    def test_043_purchase_modfiy_price_case(self):
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
    def test_044_purchase_multiple_goods_case(self):
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

    # 采购单筛选用例
    def test_045_purchase_order_filer_case(self):
        """关键字筛选(单号)"""
        self.login_action()
        purchaseorder = PurchaseOrderView(self.driver)
        ordernum = ReadData().get_data('product_purchase_order', 'num1')
        purchaseorder.enter_puchaseorder_interface()
        purchaseorder.filter_order(keyword=ordernum)
        purchaseorder.enter_order_detail()
        detail_ordernum = purchaseorder.get_detail_ptuchase_order()
        self.assertEqual(ordernum, detail_ordernum)

    def test_046_purchase_order_filer_case(self):
        """关键字筛选(备注)"""
        self.login_action()
        purchaseorder = PurchaseOrderView(self.driver)
        ordernum = ReadData().get_data('product_purchase_order', 'num5')
        purchaseorder.enter_puchaseorder_interface()
        purchaseorder.filter_order(keyword='采购两种商品')
        purchaseorder.enter_order_detail()
        detail_ordernum = purchaseorder.get_detail_ptuchase_order()
        self.assertEqual(ordernum, detail_ordernum)

    def test_047_purchase_order_filer_case(self):
        """结算账户筛选（现金）"""
        self.login_action()
        purchaseorder = PurchaseOrderView(self.driver)
        ordernum = ReadData().get_data('product_purchase_order', 'num5')
        purchaseorder.enter_puchaseorder_interface()
        purchaseorder.filter_order(settlement='现金')
        purchaseorder.enter_order_detail()
        detail_ordernum = purchaseorder.get_detail_ptuchase_order()
        self.assertEqual(ordernum, detail_ordernum)

    def test_048_purchase_order_filer_case(self):
        """供应商名称筛选"""
        self.login_action()
        purchaseorder = PurchaseOrderView(self.driver)
        ordernum = ReadData().get_data('product_purchase_order', 'num5')
        purchaseorder.enter_puchaseorder_interface()
        purchaseorder.filter_order(supplier_name='李洲全供应商1')
        purchaseorder.enter_order_detail()
        detail_ordernum = purchaseorder.get_detail_ptuchase_order()
        self.assertEqual(ordernum, detail_ordernum)

    def test_049_purchase_order_filer_case(self):
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
    def test_050_obsolete_purchase_order_case(self):
        """采购单作废"""
        self.login_action()
        purchaseorder = PurchaseOrderView(self.driver)
        ordernum = ReadData().get_data('product_purchase_order', 'num1')
        purchaseorder.enter_puchaseorder_interface()
        purchaseorder.filter_order(keyword=ordernum)
        purchaseorder.operating_document_action(obsolete=True, keyword=ordernum)
        self.assertTrue(purchaseorder.check_obsolete_status())

    # 复制订单用例
    def test_051_copy_purchase_order_case(self):
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

    def test_052_purchase_order_return_case(self):
        """采购单退货"""
        self.login_action()
        purchaseorder = PurchaseOrderView(self.driver)
        ordernum = ReadData().get_data('product_purchase_order', 'num3')
        purchaseorder.enter_puchaseorder_interface()
        purchaseorder.filter_order(keyword=ordernum)
        purchaseorder.purchase_order_return()
        self.assertTrue(purchaseorder.get_purchase_return_status())

    def test_053_purchase_order_filer_case(self):
        """有退货进行筛选"""
        self.login_action()
        purchaseorder = PurchaseOrderView(self.driver)
        ordernum = ReadData().get_data('product_purchase_order', 'num3')
        purchaseorder.enter_puchaseorder_interface()
        purchaseorder.filter_order(returned=True)
        purchaseorder.enter_order_detail()
        detail_ordernum = purchaseorder.get_detail_ptuchase_order()
        self.assertEqual(ordernum, detail_ordernum)

    def test_054_purchase_order_return_case(self):
        """采购单改价退货"""
        self.login_action()
        purchaseorder = PurchaseOrderView(self.driver)
        ordernum = ReadData().get_data('product_purchase_order', 'num4')
        purchaseorder.enter_puchaseorder_interface()
        purchaseorder.filter_order(keyword=ordernum)
        purchaseorder.purchase_order_return(modify=True, price=50)
        self.assertTrue(purchaseorder.get_purchase_return_status())

    # 采购单筛选用例
    def test_055_purchase_order_filer_case(self):
        """关键字筛选(作废单据)"""
        self.login_action()
        purchaseorder = PurchaseOrderView(self.driver)
        ordernum = ReadData().get_data('product_purchase_order', 'num1')
        purchaseorder.enter_puchaseorder_interface()
        purchaseorder.filter_order(status=False)
        purchaseorder.enter_order_detail()
        detail_ordernum = purchaseorder.get_detail_ptuchase_order()
        self.assertEqual(ordernum, detail_ordernum)

    # 采购单筛选用例
    def test_056_purchase_order_filer_case(self):
        """关键字筛选(退货)"""
        self.login_action()
        purchaseorder = PurchaseOrderView(self.driver)
        ordernum = ReadData().get_data('product_purchase_order', 'num4')
        purchaseorder.enter_puchaseorder_interface()
        purchaseorder.filter_order(returned=True)
        purchaseorder.enter_order_detail()
        detail_ordernum = purchaseorder.get_detail_ptuchase_order()
        self.assertEqual(ordernum, detail_ordernum)

    def test_057_original_purchase_return_case(self):
        """原始采购单退货"""
        self.login_action()
        purchasereutrn = PurchaseReturnView(self.driver)
        pruchase_order = ReadData().get_data('product_purchase_order', 'num2')
        purchasereutrn.original_order_return_action(1, normal=True, keyword=pruchase_order)
        purchasereturn_num = purchasereutrn.get_purchase_return_ordernum()
        ReadData().write_data('product_purchase_return_order', 'num1', purchasereturn_num)
        self.assertTrue(purchasereutrn.check_purchase_return_success_status())

    # 原始采购单退货
    def test_058_original_purchase_return_case(self):
        """原单退货（现金）"""
        self.login_action()
        purchasereutrn = PurchaseReturnView(self.driver)
        pruchase_order = ReadData().get_data('product_purchase_order', 'num2')
        purchasereutrn.original_order_return_action(1, keyword=pruchase_order, account='现金')
        purchasereturn_num = purchasereutrn.get_purchase_return_ordernum()
        ReadData().write_data('product_purchase_return_order', 'num2', purchasereturn_num)
        sleep(1)
        info = purchasereutrn.check_account_type()
        self.assertEqual(info, '现金')

    # 原始采购单退货
    def test_059_original_purchase_return_case(self):
        """原单退货（银行卡）"""
        self.login_action()
        puchasereutrn = PurchaseReturnView(self.driver)
        pruchase_order = ReadData().get_data('product_purchase_order', 'num2')
        puchasereutrn.original_order_return_action(1, keyword=pruchase_order, account='银行卡')
        purchasereturn_num = puchasereutrn.get_purchase_return_ordernum()
        ReadData().write_data('product_purchase_return_order', 'num3', purchasereturn_num)
        self.assertEqual(puchasereutrn.check_account_type(), '银行卡')

    # 原始采购单退货
    def test_060_original_purchase_return_case(self):
        """原单退货（支付宝账户）"""
        self.login_action()
        puchasereutrn = PurchaseReturnView(self.driver)
        pruchase_order = ReadData().get_data('product_purchase_order', 'num2')
        puchasereutrn.original_order_return_action(1, keyword=pruchase_order, account='支付宝账户')
        purchasereturn_num = puchasereutrn.get_purchase_return_ordernum()
        ReadData().write_data('product_purchase_return_order', 'num4', purchasereturn_num)
        self.assertEqual(puchasereutrn.check_account_type(), '支付宝账户')

    # 原始采购单退货
    def test_061_original_purchase_return_case(self):
        """原单退货（微信支付账户）"""
        self.login_action()
        puchasereutrn = PurchaseReturnView(self.driver)
        pruchase_order = ReadData().get_data('product_purchase_order', 'num2')
        puchasereutrn.original_order_return_action(1, keyword=pruchase_order, account='微信支付账户')
        purchasereturn_num = puchasereutrn.get_purchase_return_ordernum()
        ReadData().write_data('product_purchase_return_order', 'num5', purchasereturn_num)
        self.assertEqual(puchasereutrn.check_account_type(), '微信支付账户')

    # 原始采购单退货
    def test_062_original_purchase_return_case(self):
        """原单退货（其他账户）"""
        self.login_action()
        puchasereutrn = PurchaseReturnView(self.driver)
        pruchase_order = ReadData().get_data('product_purchase_order', 'num2')
        puchasereutrn.original_order_return_action(1, keyword=pruchase_order, account='其他账户')
        purchasereturn_num = puchasereutrn.get_purchase_return_ordernum()
        ReadData().write_data('product_purchase_return_order', 'num6', purchasereturn_num)
        self.assertEqual(puchasereutrn.check_account_type(), '其他账户')

    # 原始采购单退货
    def test_063_original_purchase_return_case(self):
        """原单退货（继续退货）"""
        self.login_action()
        purchasereutrn = PurchaseReturnView(self.driver)
        pruchase_order = ReadData().get_data('product_purchase_order', 'num2')
        purchasereutrn.original_order_return_action(1, normal=True, keyword=pruchase_order, is_continue=True)
        purchasereturn_num = purchasereutrn.get_purchase_return_ordernum()
        ReadData().write_data('product_purchase_return_order', 'num7', purchasereturn_num)
        self.assertTrue(purchasereutrn.check_purchase_return_success_status())

    # 原始采购单退货
    def test_064_original_purchase_return_case(self):
        """原单退货（改价）"""
        self.login_action()
        purchasereutrn = PurchaseReturnView(self.driver)
        pruchase_order = ReadData().get_data('product_purchase_order', 'num2')
        purchasereutrn.original_order_return_action(1, keyword=pruchase_order, modify=1000)
        purchasereturn_num = purchasereutrn.get_purchase_return_ordernum()
        total_money = purchasereutrn.check_total_money()
        ReadData().write_data('product_purchase_return_order', 'num8', purchasereturn_num)
        self.assertEqual(total_money, '￥1000.00')

    # 原始采购单退货
    def test_065_original_purchase_return_case(self):
        """原单退货（备注）"""
        self.login_action()
        purchasereutrn = PurchaseReturnView(self.driver)
        pruchase_order = ReadData().get_data('product_purchase_order', 'num2')
        purchasereutrn.original_order_return_action(1, keyword=pruchase_order, remark='退货商品')
        purchasereturn_num = purchasereutrn.get_purchase_return_ordernum()
        info = purchasereutrn.check_remaks()
        ReadData().write_data('product_purchase_return_order', 'num9', purchasereturn_num)
        self.assertEqual(info, '退货商品')

    # 直接退货
    def test_066_direct_purchase_return_case(self):
        """直接退货（正常）"""
        self.login_action()
        purchasereutrn = PurchaseReturnView(self.driver)
        purchasereutrn.direct_return_action('李洲全供应商1', normal=True, name='测试商品8号', num=1)
        purchasereturn_num = purchasereutrn.get_purchase_return_ordernum()
        ReadData().write_data('product_purchase_return_order', 'num10', purchasereturn_num)
        self.assertTrue(purchasereutrn.check_purchase_return_success_status())

    # 直接退货
    def test_067_direct_purchase_return_case(self):
        """直接退货（现金）"""
        self.login_action()
        purchasereutrn = PurchaseReturnView(self.driver)
        purchasereutrn.direct_return_action('李洲全供应商1', name='测试商品8号', num=1, account='现金')
        purchasereturn_num = purchasereutrn.get_purchase_return_ordernum()
        ReadData().write_data('product_purchase_return_order', 'num11', purchasereturn_num)
        self.assertTrue(purchasereutrn.check_purchase_return_success_status())

    # 直接退货
    def test_068_direct_purchase_return_case(self):
        """直接退货（银行卡）"""
        self.login_action()
        purchasereutrn = PurchaseReturnView(self.driver)
        purchasereutrn.direct_return_action('李洲全供应商1', name='测试商品8号', num=1, account='银行卡')
        purchasereturn_num = purchasereutrn.get_purchase_return_ordernum()
        ReadData().write_data('product_purchase_return_order', 'num12', purchasereturn_num)
        self.assertTrue(purchasereutrn.check_purchase_return_success_status())

    # 直接退货
    def test_069_direct_purchase_return_case(self):
        """直接退货（支付宝账户）"""
        self.login_action()
        purchasereutrn = PurchaseReturnView(self.driver)
        purchasereutrn.direct_return_action('李洲全供应商1', name='测试商品8号', num=1, account='支付宝账户')
        purchasereturn_num = purchasereutrn.get_purchase_return_ordernum()
        ReadData().write_data('product_purchase_return_order', 'num13', purchasereturn_num)
        self.assertTrue(purchasereutrn.check_purchase_return_success_status())

    # 直接退货
    def test_070_direct_purchase_return_case(self):
        """直接退货（微信支付账户）"""
        self.login_action()
        purchasereutrn = PurchaseReturnView(self.driver)
        purchasereutrn.direct_return_action('李洲全供应商1', name='测试商品8号', num=1, account='微信支付账户')
        purchasereturn_num = purchasereutrn.get_purchase_return_ordernum()
        ReadData().write_data('product_purchase_return_order', 'num14', purchasereturn_num)
        self.assertTrue(purchasereutrn.check_purchase_return_success_status())

    # 直接退货
    def test_071_direct_purchase_return_case(self):
        """直接退货（其他账户）"""
        self.login_action()
        purchasereutrn = PurchaseReturnView(self.driver)
        purchasereutrn.direct_return_action('李洲全供应商1', name='测试商品8号', num=1, account='其他账户')
        purchasereturn_num = purchasereutrn.get_purchase_return_ordernum()
        ReadData().write_data('product_purchase_return_order', 'num15', purchasereturn_num)
        self.assertTrue(purchasereutrn.check_purchase_return_success_status())

    # 直接退货
    def test_072_direct_purchase_return_case(self):
        """直接退货（继续退货）"""
        self.login_action()
        purchasereutrn = PurchaseReturnView(self.driver)
        purchasereutrn.direct_return_action('李洲全供应商1', normal=True, name='测试商品8号', num=1, is_continue=True)
        purchasereturn_num = purchasereutrn.get_purchase_return_ordernum()
        ReadData().write_data('product_purchase_return_order', 'num16', purchasereturn_num)
        self.assertTrue(purchasereutrn.check_purchase_return_success_status())

    # 直接退货
    def test_073_direct_purchase_return_case(self):
        """直接退货（改价）"""
        self.login_action()
        purchasereutrn = PurchaseReturnView(self.driver)
        purchasereutrn.direct_return_action('李洲全供应商1', name='测试商品8号', num=1, modify=1000)
        purchasereturn_num = purchasereutrn.get_purchase_return_ordernum()
        ReadData().write_data('product_purchase_return_order', 'num17', purchasereturn_num)
        total_money = purchasereutrn.check_total_money()
        self.assertEqual(total_money, '￥1000.00')

    # 直接退货
    def test_074_direct_purchase_return_case(self):
        """直接退货（备注）"""
        self.login_action()
        purchasereutrn = PurchaseReturnView(self.driver)
        purchasereutrn.direct_return_action('李洲全供应商1', name='测试商品8号', num=1, remark='直接退货备注')
        purchasereturn_num = purchasereutrn.get_purchase_return_ordernum()
        ReadData().write_data('product_purchase_return_order', 'num18', purchasereturn_num)
        info = purchasereutrn.check_remaks()
        self.assertEqual(info, '直接退货备注')

    # 采购退货单筛选
    def test_075_purchase_return_order(self):
        """正常筛选"""
        self.login_action()
        p = PurchaseReturnOrderView(self.driver)
        purchase_return_order = ReadData().get_data('product_purchase_return_order', 'num1')
        p.purchase_return_order_action(keyword=purchase_return_order)
        confim_num = p.get_detail_ptuchase_order()
        self.assertEqual(purchase_return_order, confim_num)

    def test_076_purchase_return_order(self):
        """采购退货单作废"""
        self.login_action()
        p = PurchaseReturnOrderView(self.driver)
        purchase_return_order = ReadData().get_data('product_purchase_return_order', 'num2')
        p.purchase_return_order_action(keyword=purchase_return_order, obsolete=True)
        self.assertTrue(p.check_obsolete_status_())

    def test_077_purchase_return_order(self):
        """作废单据筛选"""
        self.login_action()
        p = PurchaseReturnOrderView(self.driver)
        purchase_return_order = ReadData().get_data('product_purchase_return_order', 'num2')
        p.purchase_return_order_action(status=False)
        confim_num = p.get_detail_ptuchase_order()
        self.assertEqual(purchase_return_order, confim_num)

    def test_078_purchase_return_order(self):
        """单据复制（原单退货）"""
        self.login_action()
        p = PurchaseReturnOrderView(self.driver)
        purchase_return_order = ReadData().get_data('product_purchase_return_order', 'num3')
        p.purchase_return_order_action(keyword=purchase_return_order, copy=True, supplier_name='李洲全供应商1',
                                       is_original=True)
        purchase_return_num = p.get_detail_ptuchase_order()
        ReadData().write_data('product_purchase_return_order', 'num19', purchase_return_num)
        self.assertTrue(p.check_purchase_return_status())

    def test_079_purchase_return_order(self):
        """单据复制（直接退货）"""
        self.login_action()
        p = PurchaseReturnOrderView(self.driver)
        purchase_return_order = ReadData().get_data('product_purchase_return_order', 'num10')
        p.purchase_return_order_action(keyword=purchase_return_order, copy=True, supplier_name='李洲全供应商1')
        purchase_return_num = p.get_detail_ptuchase_order()
        ReadData().write_data('product_purchase_return_order', 'num20', purchase_return_num)
        self.assertTrue(p.check_purchase_return_status())

    def test_080_purchase_return_order(self):
        """结算方式（现金）"""
        self.login_action()
        p = PurchaseReturnOrderView(self.driver)
        p.purchase_return_order_action(settlement='现金')
        settlement_type = p.get_detail_settlement_type()
        self.assertEqual('现金', settlement_type)

    def test_081_purchase_return_order(self):
        """结算方式（银行卡）"""
        self.login_action()
        p = PurchaseReturnOrderView(self.driver)
        p.purchase_return_order_action(settlement='银行卡')
        settlement_type = p.get_detail_settlement_type()
        self.assertEqual('银行卡', settlement_type)

    def test_082_purchase_return_order(self):
        """结算方式（支付宝账户）"""
        self.login_action()
        p = PurchaseReturnOrderView(self.driver)
        p.purchase_return_order_action(settlement='支付宝账户')
        settlement_type = p.get_detail_settlement_type()
        self.assertEqual('支付宝账户', settlement_type)

    def test_083_purchase_return_order(self):
        """结算方式（微信支付账户）"""
        self.login_action()
        p = PurchaseReturnOrderView(self.driver)
        p.purchase_return_order_action(settlement='微信支付账户')
        settlement_type = p.get_detail_settlement_type()
        self.assertEqual('微信支付账户', settlement_type)

    def test_084_purchase_return_order(self):
        """结算方式（其他账户）"""
        self.login_action()
        p = PurchaseReturnOrderView(self.driver)
        p.purchase_return_order_action(settlement='其他账户')
        settlement_type = p.get_detail_settlement_type()
        self.assertEqual('其他账户', settlement_type)

    def test_085_cashier_case(self):
        """正常收银"""
        self.login_action()
        # 销售之前商品库存数
        logging.info('开始收银')
        cashier = CashierView(self.driver)
        cashier.cashier_goods(num=30)
        sleep(1)
        sales_order_num = cashier.get_sales_order_num()
        ReadData().write_data('sale_order', 'num1', sales_order_num)
        self.assertTrue(cashier.check_transaction_success_status())

    # 商品打折销售
    def test_086_goods_discount_sales_case(self):
        """商品打折销售(1折),订单无优惠"""
        self.login_action()
        cashier = CashierView(self.driver)
        cashier.cashier_goods(num=1, normal=True, good_discount=True, good_value=1)
        sales_order_num = cashier.get_sales_order_num()
        ReadData().write_data('sale_order', 'num2', sales_order_num)
        self.assertTrue(cashier.check_transaction_success_status())
        # self.assertEqual(cashier.get_order_price(), r'￥20.00')

    # 商品改价销售
    def test_087_goods_modify_sales_case(self):
        """商品改价销售(￥20.00)，订单无优惠"""
        self.login_action()
        cashier = CashierView(self.driver)
        cashier.cashier_goods(num=1, normal=True, good_modify=True, good_value=20)
        sales_order_num = cashier.get_sales_order_num()
        ReadData().write_data('sale_order', 'num3', sales_order_num)
        self.assertTrue(cashier.check_transaction_success_status())
        # self.assertEqual(cashier.get_order_price(), r'￥20.00')

    # 商品打折，订单打折销售
    def test_088_discount_discount_sales_case(self):
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
    def test_089_modify_discount_sales_case(self):
        """商品改价(￥100)，订单打折销售（8折）"""
        self.login_action()
        cashier = CashierView(self.driver)
        cashier.cashier_goods(num=1, normal=True, good_modify=True, good_value=100, offer=False,
                              order_discount=True, order_value=8)
        sales_order_num = cashier.get_sales_order_num()
        ReadData().write_data('sale_order', 'num5', sales_order_num)
        self.assertTrue(cashier.check_transaction_success_status())

    # 商品打折，订单改价销售
    def test_090_discount_modify_sales_case(self):
        """商品打折（5折），订单改价（￥88）"""
        self.login_action()
        cashier = CashierView(self.driver)
        cashier.cashier_goods(num=1, normal=True, good_discount=True, good_value=5, offer=False,
                              order_modify=True, order_value=88)
        sales_order_num = cashier.get_sales_order_num()
        ReadData().write_data('sale_order', 'num6', sales_order_num)
        self.assertTrue(cashier.check_transaction_success_status())

    # 商品改价，订单改价销售
    def test_091_modify_modify_sales_case(self):
        """商品改价(￥100)，订单改价（￥88）"""
        self.login_action()
        cashier = CashierView(self.driver)
        cashier.cashier_goods(num=1, normal=True, good_modify=True, good_value=100, offer=False,
                              order_modify=True, order_value=88)
        sales_order_num = cashier.get_sales_order_num()
        ReadData().write_data('sale_order', 'num7', sales_order_num)
        self.assertTrue(cashier.check_transaction_success_status())

    # 订单打折销售
    def test_092_order_discount_sales_case(self):
        """商品无优惠，订单打折（5）"""
        self.login_action()
        cashier = CashierView(self.driver)
        cashier.cashier_goods(num=1, offer=False, order_discount=True, order_value=5)
        sales_order_num = cashier.get_sales_order_num()
        ReadData().write_data('sale_order', 'num8', sales_order_num)
        self.assertTrue(cashier.check_transaction_success_status())

    # 商品改价，订单改价销售
    def test_093_order_modify_sales_case(self):
        """商品无优惠，订单改价（￥88）"""
        self.login_action()
        cashier = CashierView(self.driver)
        cashier.cashier_goods(num=1, offer=False, order_modify=True, order_value=88)
        sales_order_num = cashier.get_sales_order_num()
        ReadData().write_data('sale_order', 'num9', sales_order_num)
        self.assertTrue(cashier.check_transaction_success_status())

    # 销售单复制在销售
    def test_094_sales_order_copy_case(self):
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
    def test_095_sales_order_copy_case(self):
        """销售单作废"""
        self.login_action()
        salesorder = SalesOrderView(self.driver)
        ordernum = ReadData().get_data('product_sale_order', 'num17')
        salesorder.sales_order_action(keyword=ordernum, obsolete=True)
        # 设置检查点
        self.assertTrue(salesorder.check_sales_order_status())

    # 原始销售单退货
    def test_096_original_sales_return_case(self):
        """原始销售单退货"""
        self.login_action()
        salesreturn = SalesReturnView(self.driver)
        sales_order = ReadData().get_data('product_sale_order', 'num1')
        salesreturn.original_order_return_action(good_name='测试商品8号', good_num=1, normal=True, keyword=sales_order)
        sales_return_num = salesreturn.get_sales_return_ordernum()
        ReadData().write_data('product_sale_return_order', 'num1', sales_return_num)
        self.assertTrue(salesreturn.check_sales_return_success_status())

    # 原始销售单退货
    def test_097_original_sales_return_case(self):
        """原单退货（现金）"""
        self.login_action()
        salesreturn = SalesReturnView(self.driver)
        sales_order = ReadData().get_data('product_sale_order', 'num1')
        salesreturn.original_order_return_action(good_name='测试商品8号', good_num=1, keyword=sales_order, account='现金')
        salesreturn_num = salesreturn.get_detail_return_ordernum()
        ReadData().write_data('product_sale_return_order', 'num2', salesreturn_num)
        self.assertEqual(salesreturn.check_account_type(), '现金')

    # 原始销售单退货
    def test_098_original_sales_return_case(self):
        """原单退货（银行卡）"""
        self.login_action()
        salesreturn = SalesReturnView(self.driver)
        sales_order = ReadData().get_data('product_sale_order', 'num1')
        salesreturn.original_order_return_action(good_name='测试商品8号', good_num=1, keyword=sales_order, account='银行卡')
        salesreturn_num = salesreturn.get_detail_return_ordernum()
        ReadData().write_data('product_sale_return_order', 'num3', salesreturn_num)
        self.assertEqual(salesreturn.check_account_type(), '银行卡')

    # 原始销售单退货
    def test_04_original_sales_return_case(self):
        """原单退货（支付宝账户）"""
        self.login_action()
        salesreturn = SalesReturnView(self.driver)
        sales_order = ReadData().get_data('product_sale_order', 'num1')
        salesreturn.original_order_return_action(good_name='测试商品8号', good_num=1, keyword=sales_order, account='支付宝账户')
        salesreturn_num = salesreturn.get_detail_return_ordernum()
        ReadData().write_data('product_sale_return_order', 'num4', salesreturn_num)
        self.assertEqual(salesreturn.check_account_type(), '支付宝账户')

    # 原始销售单退货
    def test_099_original_sales_return_case(self):
        """原单退货（微信支付账户）"""
        self.login_action()
        salesreturn = SalesReturnView(self.driver)
        sales_order = ReadData().get_data('product_sale_order', 'num1')
        salesreturn.original_order_return_action(good_name='测试商品8号', good_num=1, keyword=sales_order, account='微信支付账户')
        salesreturn_num = salesreturn.get_detail_return_ordernum()
        ReadData().write_data('product_sale_return_order', 'num5', salesreturn_num)
        self.assertEqual(salesreturn.check_account_type(), '微信支付账户')

    # 原始销售单退货
    def test_100_original_sales_return_case(self):
        """原单退货（其他账户）"""
        self.login_action()
        salesreturn = SalesReturnView(self.driver)
        sales_order = ReadData().get_data('product_sale_order', 'num1')
        salesreturn.original_order_return_action(good_name='测试商品8号', good_num=1, keyword=sales_order, account='其他账户')
        salesreturn_num = salesreturn.get_detail_return_ordernum()
        ReadData().write_data('product_sale_return_order', 'num6', salesreturn_num)
        self.assertEqual(salesreturn.check_account_type(), '其他账户')

    # 原始销售单退货
    def test_101_original_sales_return_case(self):
        """原单退货（继续退货）"""
        self.login_action()
        salesreturn = SalesReturnView(self.driver)
        sales_order = ReadData().get_data('product_sale_order', 'num1')
        salesreturn.original_order_return_action(good_name='测试商品8号', good_num=1, normal=True, keyword=sales_order,
                                                 is_continue=True)
        salesreturn_num = salesreturn.get_sales_return_ordernum()
        ReadData().write_data('product_sale_return_order', 'num7', salesreturn_num)
        self.assertTrue(salesreturn.check_sales_return_success_status())

    # 原始销售单退货
    def test_102_original_sales_return_case(self):
        """原单退货（改价）"""
        self.login_action()
        salesreturn = SalesReturnView(self.driver)
        sales_order = ReadData().get_data('product_sale_order', 'num1')
        salesreturn.original_order_return_action(good_name='测试商品8号', good_num=1, keyword=sales_order, modify=1000)
        salesreturn_num = salesreturn.get_detail_return_ordernum()
        total_money = salesreturn.check_total_money()
        ReadData().write_data('product_sale_return_order', 'num8', salesreturn_num)
        self.assertEqual(total_money, '￥1000.00')

    # 原始销售单退货
    def test_103_original_sales_return_case(self):
        """原单退货（备注）"""
        self.login_action()
        salesreturn = SalesReturnView(self.driver)
        sales_order = ReadData().get_data('product_sale_order', 'num1')
        salesreturn.original_order_return_action(good_name='测试商品8号', good_num=1, keyword=sales_order, remark='退货商品')
        salesreturn_num = salesreturn.get_detail_return_ordernum()
        info = salesreturn.check_remaks()
        ReadData().write_data('product_sale_return_order', 'num9', salesreturn_num)
        self.assertEqual(info, '退货商品')

    # 直接退货
    def test_104_direct_sales_return_case(self):
        """直接退货（正常）"""
        self.login_action()
        salesreutrn = SalesReturnView(self.driver)
        salesreutrn.direct_return_action('李洲全-13888888811', normal=True, name='测试商品8号', num=1)
        salesreturn_num = salesreutrn.get_sales_return_ordernum()
        ReadData().write_data('product_sale_return_order', 'num10', salesreturn_num)
        self.assertTrue(salesreutrn.check_sales_return_success_status())

    # 直接退货
    def test_105_direct_sales_return_case(self):
        """直接退货（现金）"""
        self.login_action()
        salesreutrn = SalesReturnView(self.driver)
        salesreutrn.direct_return_action('李洲全-13888888811', name='测试商品8号', num=1, account='现金')
        salesreturn_num = salesreutrn.get_sales_return_ordernum()
        ReadData().write_data('product_sale_return_order', 'num11', salesreturn_num)
        self.assertTrue(salesreutrn.check_sales_return_success_status())

    # 直接退货
    def test_106_direct_sales_return_case(self):
        """直接退货（银行卡）"""
        self.login_action()
        salesreutrn = SalesReturnView(self.driver)
        salesreutrn.direct_return_action('李洲全-13888888811', name='测试商品8号', num=1, account='银行卡')
        salesreturn_num = salesreutrn.get_sales_return_ordernum()
        ReadData().write_data('product_sale_return_order', 'num12', salesreturn_num)
        self.assertTrue(salesreutrn.check_sales_return_success_status())

    # 直接退货
    def test_107_direct_sales_return_case(self):
        """直接退货（支付宝账户）"""
        self.login_action()
        salesreutrn = SalesReturnView(self.driver)
        salesreutrn.direct_return_action('李洲全-13888888811', name='测试商品8号', num=1, account='支付宝账户')
        salesreturn_num = salesreutrn.get_sales_return_ordernum()
        ReadData().write_data('product_sale_return_order', 'num13', salesreturn_num)
        self.assertTrue(salesreutrn.check_sales_return_success_status())

    # 直接退货
    def test_108_direct_sales_return_case(self):
        """直接退货（微信支付账户）"""
        self.login_action()
        salesreutrn = SalesReturnView(self.driver)
        salesreutrn.direct_return_action('李洲全-13888888811', name='测试商品8号', num=1, account='微信支付账户')
        salesreturn_num = salesreutrn.get_sales_return_ordernum()
        ReadData().write_data('product_sale_return_order', 'num14', salesreturn_num)
        self.assertTrue(salesreutrn.check_sales_return_success_status())

    # 直接退货
    def test_109_direct_sales_return_case(self):
        """直接退货（其他账户）"""
        self.login_action()
        salesreutrn = SalesReturnView(self.driver)
        salesreutrn.direct_return_action('李洲全-13888888811', name='测试商品8号', num=1, account='其他账户')
        salesreturn_num = salesreutrn.get_sales_return_ordernum()
        ReadData().write_data('product_sale_return_order', 'num15', salesreturn_num)
        self.assertTrue(salesreutrn.check_sales_return_success_status())

    # 直接退货
    def test_110_direct_sales_return_case(self):
        """直接退货（继续退货）"""
        self.login_action()
        salesreutrn = SalesReturnView(self.driver)
        salesreutrn.direct_return_action('李洲全-13888888811', normal=True, name='测试商品8号', num=1, is_continue=True)
        salesreturn_num = salesreutrn.get_sales_return_ordernum()
        ReadData().write_data('product_sale_return_order', 'num16', salesreturn_num)
        self.assertTrue(salesreutrn.check_sales_return_success_status())

    # 直接退货
    def test_111_direct_sales_return_case(self):
        """直接退货（改价）"""
        self.login_action()
        salesreutrn = SalesReturnView(self.driver)
        salesreutrn.direct_return_action('李洲全-13888888811', name='测试商品8号', num=1, modify=1000)
        salesreturn_num = salesreutrn.get_detail_return_ordernum()
        ReadData().write_data('product_sale_return_order', 'num17', salesreturn_num)
        total_money = salesreutrn.check_total_money()
        self.assertEqual(total_money, '￥1000.00')

    # 直接退货
    def test_112_direct_sales_return_case(self):
        """直接退货（备注）"""
        self.login_action()
        salesreutrn = SalesReturnView(self.driver)
        salesreutrn.direct_return_action('李洲全-13888888811', name='测试商品8号', num=1, remark='直接退货备注')
        salesreturn_num = salesreutrn.get_detail_return_ordernum()
        ReadData().write_data('product_sale_return_order', 'num18', salesreturn_num)
        info = salesreutrn.check_remaks()
        self.assertEqual(info, '直接退货备注')
