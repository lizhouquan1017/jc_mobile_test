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
from base.skip_dependon import skip_dependon
import logging
import random

num = random.randint(100000, 999999)
pwd = 'ab'+str(num)


class ProdcutEnviromentTest(ParametrizedCase):

    @classmethod
    def setUpClass(cls):
        driver = BaseDriver()
        cls.driver = driver.appium_desired(0)

    def setUp(self):
        self.imgs = []
        self.addCleanup(self.cleanup)
        self.driver.start_activity("com.gengcon.android.jxc", "com.gengcon.android.jxc.login.SplashActivity")
        # driver = BaseDriver()
        # self.driver = driver.appium_desired(self.param)

    def tearDown(self):
        # self.driver.quit()
        self.driver.close_app()
        # sleep(5)
        # self.driver.close_app()

    def add_img(self):
        # 在是python3.x 中，如果在这里初始化driver ，因为3.x版本 unittest 运行机制不同，会导致用力失败时截图失败
        self.imgs.append(self.driver.get_screenshot_as_base64())
        return True

    def cleanup(self):
        pass

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    # 登录操作
    def login_action(self):
        if self.param == 0:
            login = LoginBusiness(self.driver)
            data = login.get_csv_data('../data/test_data/login_data.csv', 1)
            login.login_action(data[0], data[2])
        elif self.param == 1:
            login = LoginBusiness(self.driver)
            data = login.get_csv_data('../data/test_data/login_data.csv', 2)
            login.login_action(data[0], data[2])
        sleep(2)

    def test_01001_add_case(self):
        """正常添加商品"""
        """
        商品名称，成本价，零售价，颜色属性，尺码属性 ：必填
        """
        self.login_action()
        goods = GoodsBusiness(self.driver)
        goods.enter_goods_list()
        goods.type_must_field('测试商品1号', 100, 200, '均色', '均码')
        goods.confirm_add_goods()
        status = goods.check_success_status()
        goods.get_goods_details()
        goods_num = goods.get_goods_num()
        sku_num = goods.get_sku_barcode()
        ReadData(self.param).write_data('goods_bar_code', 'num1', goods_num)
        ReadData(self.param).write_data('goods_single_barcode', 'num1', sku_num)
        self.assertEqual('添加新品成功', status)

    def test_01002_add_case(self):
        """自定义商品货号添加商品"""
        """
        商品名称，成本价，零售价，颜色属性，尺码属性 ：必填
        商品货号，库存数，商品条码，商品备注，其他参数： 非必填
        """
        self.login_action()
        goods = GoodsBusiness(self.driver)
        goods.enter_goods_list()
        goods.type_must_field('测试商品2号', 100, 200, '均色', '均码', 19891017)
        goods.confirm_add_goods()
        status = goods.check_success_status()
        goods.get_goods_details()
        goods_num = goods.get_goods_num()
        sku_code = goods.get_sku_barcode()
        ReadData(self.param).write_data('goods_bar_code', 'num2', goods_num)
        ReadData(self.param).write_data('goods_single_barcode', 'num2', sku_code)
        self.assertEqual('添加新品成功', status)

    def test_01003_add_case(self):
        """自定义商品货号添加商品,添加初始库存"""
        """
        商品名称，成本价，零售价，颜色属性，尺码属性 ：必填
        商品货号，库存数，商品条码，商品备注，其他参数： 非必填
        """
        self.login_action()
        goods = GoodsBusiness(self.driver)
        goods.enter_goods_list()
        goods.type_must_field('测试商品3号', 100, 200, '均色', '均码', 19891018, 10)
        goods.confirm_add_goods()
        status = goods.check_success_status()
        goods.get_goods_details()
        goods_code = goods.get_goods_num()
        sku_code = goods.get_sku_barcode()
        ReadData(self.param).write_data('goods_bar_code', 'num3', goods_code)
        ReadData(self.param).write_data('goods_single_barcode', 'num3', sku_code)
        self.assertEqual('添加新品成功', status)

    def test_01004_add_case(self):
        """自定义商品货号添加商品,添加初始库存，添加商品条码"""
        """
        商品名称，成本价，零售价，颜色属性，尺码属性 ：必填
        商品货号，库存数，商品条码，商品备注，其他参数： 非必填
        """
        self.login_action()
        goods = GoodsBusiness(self.driver)
        goods.enter_goods_list()
        goods.type_must_field('测试商品4号', 50, '200', '均色', '均码', 19891019, 30, '20190916-01')
        goods.confirm_add_goods()
        status = goods.check_success_status()
        goods.get_goods_details()
        goods_num = goods.get_goods_num()
        sku_code = goods.get_sku_barcode()
        ReadData(self.param).write_data('goods_bar_code', 'num4', goods_num)
        ReadData(self.param).write_data('goods_single_barcode', 'num4', sku_code)
        self.assertEqual('添加新品成功', status)

    def test_01005_add_case(self):
        """自定义商品货号添加商品,添加初始库存，添加商品条码,添加备注"""
        """
        商品名称，成本价，零售价，颜色属性，尺码属性 ：必填
        商品货号，库存数，商品条码，商品备注，其他参数： 非必填
        """
        self.login_action()
        goods = GoodsBusiness(self.driver)
        goods.enter_goods_list()
        goods.type_must_field('测试商品5号', 100, 200, '均色', '均码', 19891020, 30, '20190917-01', '测试商品备注')
        goods.confirm_add_goods()
        status = goods.check_success_status()
        goods.get_goods_details()
        goods_num = goods.get_goods_num()
        sku_code = goods.get_sku_barcode()
        ReadData(self.param).write_data('goods_bar_code', 'num5', goods_num)
        ReadData(self.param).write_data('goods_single_barcode', 'num5', sku_code)
        self.assertEqual('添加新品成功', status)

    # 商品下架
    @skip_dependon(depend="test_01005_add_case")
    def test_01006_obtained_case(self):
        """商品下架功能"""
        self.login_action()
        goods = GoodsBusiness(self.driver)
        goods.enter_goods_list()
        goods.goods_obtained_action('测试商品5号')
        status = goods.check_obtained_status()
        self.assertEqual('该商品已下架', status)

    # 商品上架
    @skip_dependon(depend="test_01006_obtained_case")
    def test_01007_shelf_case(self):
        """商品上架"""
        self.login_action()
        goods = GoodsBusiness(self.driver)
        goods.enter_goods_list()
        goods.goods_shelf_action('测试商品5号')
        self.assertTrue(goods.check_shelf_status('测试商品5号'))

    # 商品删除操作
    @skip_dependon(depend="test_01005_add_case")
    def test_01008_delete_case(self):
        """删除商品"""
        self.login_action()
        goods = GoodsBusiness(self.driver)
        goods.enter_goods_list()
        goods.goods_delete_action()
        self.assertTrue(goods.check_goods_is_not_exist('测试商品5号'))

    # 列表编辑
    @skip_dependon(depend="test_01005_add_case")
    def test_01009_edit_case(self):
        """"列表编辑商品"""
        self.login_action()
        goods = GoodsBusiness(self.driver)
        goods.enter_goods_list()
        goods.list_edit_action('测试商品6号')
        self.assertEqual('测试商品6号', goods.get_goods_names())

    # 列表编辑
    @skip_dependon(depend="test_01005_add_case")
    def test_01010_edit_case(self):
        """详情编辑商品"""
        self.login_action()
        goods = GoodsBusiness(self.driver)
        goods.enter_goods_list()
        goods.details_edit_action('测试商品8号')
        self.assertEqual('测试商品8号', goods.get_goods_names())

    # 新增自定义类目
    def test_01011_custom_classification(self):
        """新增自定义类目"""
        self.login_action()
        goods = GoodsBusiness(self.driver)
        goods.enter_goods_list()
        goods.add_custom_classification('自定义分组2')
        self.assertTrue(goods.check_classification_is_exist('自定义分组2'))

    def test_02001_user_login(self):
        """正常登录用例"""
        logging.info('==正常账号成功登录用例==')
        if self.param == 0:
            login = LoginBusiness(self.driver)
            data = login.get_csv_data('../data/test_data/login_data.csv', 1)
            login.login_action(data[0], data[2])
        else:
            login = LoginBusiness(self.driver)
            data = login.get_csv_data('../data/test_data/login_data.csv', 2)
            login.login_action(data[0], data[2])
        sleep(2)
        self.assertTrue(login.check_login_success_status())

    def test_02002_user_login_pwderr(self):
        """密码错误登录用例"""
        logging.info('==正确账号密码错误登录=')
        login = LoginBusiness(self.driver)
        data = login.get_csv_data('../data/test_data/login_data.csv', 3)
        login.login_action(data[0], data[1])
        sleep(2)
        self.assertTrue(login.check_login_fail_status())

    def test_02003_user_login_pwdempty(self):
        """密码为空登录"""
        logging.info('==正常账号密码为空登录==')
        login = LoginBusiness(self.driver)
        data = login.get_csv_data('../data/test_data/login_data.csv', 4)
        login.login_action(data[0], data[1])
        sleep(2)
        self.assertTrue(login.check_login_fail_status())

    def test_02004_user_login_phonenumerror(self):
        """手机号为错误登录"""
        logging.info('==手机号格式错误登录==')
        login = LoginBusiness(self.driver)
        data = login.get_csv_data('../data/test_data/login_data.csv', 5)
        login.login_action(data[0], data[1])
        sleep(2)
        self.assertTrue(login.check_login_fail_status())

    def test_02005_user_login_unregistered(self):
        """未注册账号登录"""
        logging.info('==未注册账号登录==')
        login = LoginBusiness(self.driver)
        data = login.get_csv_data('../data/test_data/login_data.csv', 6)
        login.login_action(data[0], data[1])
        sleep(2)
        self.assertTrue(login.check_login_fail_status())

    def test_02006_user_login_phonenumEmpty(self):
        """ 手机号为空登录"""
        logging.info('==手机号为空登录==')
        login = LoginBusiness(self.driver)
        data = login.get_csv_data('../data/test_data/login_data.csv', 7)
        login.login_action(data[0], data[1])
        sleep(2)
        self.assertTrue(login.check_login_fail_status())

    def test_02007_user_login_RestrictedAccounts(self):
        """限制账号登录"""
        logging.info('==限制账号登录==')
        login = LoginBusiness(self.driver)
        data = login.get_csv_data('../data/test_data/login_data.csv', 8)
        login.login_action(data[0], data[1])
        sleep(2)
        self.assertTrue(login.check_login_fail_status())

    def test_02008_user_login_DeactivatedAccount(self):
        """停用账号登录"""
        logging.info('==停用账号登录==')
        login = LoginBusiness(self.driver)
        data = login.get_csv_data('../data/test_data/login_data.csv', 9)
        login.login_action(data[0], data[1])
        sleep(2)
        self.assertTrue(login.check_login_fail_status())

    def test_02009_user_login_VerificationCode(self):
        """验证码登录"""
        logging.info('==验证码登录==')
        login = LoginBusiness(self.driver)
        data = login.get_csv_data('../data/test_data/login_data.csv', 10)
        login.login_code_action(data[0], data[1])
        sleep(2)
        self.assertTrue(login.check_login_success_status())

    def test_02010_user_login_ExperienceAccount(self):
        """体验账号登录"""
        logging.info('==体验账号登录==')
        login = LoginBusiness(self.driver)
        login.login_experience_account_action()
        sleep(2)
        self.assertTrue(login.check_login_success_status())

    def test_02011_user_login_VerificationCodeEmpty(self):
        """验证码为空登录"""
        logging.info('==验证码为空登录==')
        login = LoginBusiness(self.driver)
        data = login.get_csv_data('../data/test_data/login_data.csv', 11)
        login.login_code_action(data[0], data[1])
        sleep(2)
        self.assertTrue(login.check_login_fail_status())

    def test_02012_user_login_VerificationCodeError(self):
        """验证码错误登录"""
        logging.info('==验证码错误登录==')
        login = LoginBusiness(self.driver)
        data = login.get_csv_data('../data/test_data/login_data.csv', 12)
        login.login_code_action(data[0], data[1])
        sleep(2)
        self.assertTrue(login.check_login_fail_status())

    # 正常注册
    def test_03001_user_register(self):
        """正常注册"""
        logging.info('=用户正常注册成功=')
        if self.param == 0:
            register = RegisterBusiness(self.driver)
            data = register.get_csv_data('../data/test_data/register.csv', 1)
            register.register_action(data[0], data[2], data[3])
            newdata = str(int(data[0])+1)
            self.assertTrue(register.check_register_success_status())
            sleep(2)
            register.update_csv_data('../data/test_data/register.csv', 1, '用户正常注册1', data[0], newdata)
        else:
            register = RegisterBusiness(self.driver)
            data = register.get_csv_data('../data/test_data/register.csv', 2)
            register.register_action(data[0], data[2], data[3])
            newdata = str(int(data[0]) + 1)
            self.assertTrue(register.check_register_success_status())
            sleep(2)
            register.update_csv_data('../data/test_data/register.csv', 2, '用户正常注册2', data[0], newdata)

    # 注册手机号为空
    def test_03002_register_phonenumEmpty(self):
        """注册手机号为空"""
        logging.info('=用户注册手机号码为空=')
        register = RegisterBusiness(self.driver)
        data = register.get_csv_data('../data/test_data/register.csv', 3)
        register.register_common_action(data[0], data[1], data[2])
        sleep(2)
        self.assertTrue(register.check_register_fail_status())

    # 注册手机号格式不正确
    def test_026_register_phonenumError(self):
        """注册手机号格式不正确"""
        logging.info('=用户注册手机号格式错误=')
        register = RegisterBusiness(self.driver)
        data = register.get_csv_data('../data/test_data/register.csv', 4)
        register.register_common_action(data[0], data[1], data[2])
        sleep(2)
        self.assertTrue(register.check_register_fail_status())

    # 注册手机号已注册
    def test_03003_registered(self):
        """注册手机号已注册"""
        logging.info('=用户手机号已注册=')
        register = RegisterBusiness(self.driver)
        data = register.get_csv_data('../data/test_data/register.csv', 5)
        register.register_common_action(data[0], data[1], data[2])
        sleep(2)
        self.assertTrue(register.check_register_fail_status())

    # 修改密码成功
    def test_04001_modify_pwdSuccess(self):
        """修改密码成功"""
        logging.info(r'==修改密码成功用例==')
        if self.param == 0:
            find = FindPwdBusiness(self.driver)
            data0 = find.get_csv_data('../data/test_data/login_data.csv', 1)
            data1 = find.get_csv_data('../data/test_data/pwd.csv', 10)
            data2 = find.get_csv_data('../data/test_data/pwd.csv', 11)
            find.findpwd_action(data0[0], data1[2])
            find.modify_action(data1[3], data1[3])
            sleep(2)
            self.assertTrue(find.check_find_pwd_success_status())
            find.update_csv_data('../data/test_data/login_data.csv', 1, '正式账号1', data0[2], data1[3])
            find.update_csv_data('../data/test_data/pwd.csv', 1, '密码相同1', data2[3], data1[3])
            logging.info(pwd)
            find.update_csv_data('../data/test_data/pwd.csv', 1, '修改密码1', data1[3], pwd)
        else:
            find = FindPwdBusiness(self.driver)
            data0 = find.get_csv_data('../data/test_data/login_data.csv', 2)
            data1 = find.get_csv_data('../data/test_data/pwd.csv', 12)
            data2 = find.get_csv_data('../data/test_data/pwd.csv', 13)
            find.findpwd_action(data0[0], data1[2])
            find.modify_action(data1[3], data1[3])
            sleep(2)
            self.assertTrue(find.check_find_pwd_success_status())
            find.update_csv_data('../data/test_data/login_data.csv', 1, '正式账号2', data0[2], data1[3])
            find.update_csv_data('../data/test_data/pwd.csv', 1, '密码相同2', data2[3], data1[3])
            logging.info(pwd)
            find.update_csv_data('../data/test_data/pwd.csv', 1, '修改密码2', data1[3], pwd)

    # 手机号为空找回密码
    def test_04002_findpwd_phoneNumEmpty(self):
        """找回密码手机号为空"""
        logging.info(r'==找回密码手机号为空用例==')
        find = FindPwdBusiness(self.driver)
        data = find.get_csv_data('../data/test_data/pwd.csv', 1)
        find.findpwd_action(data[0], data[1])
        sleep(2)
        self.assertTrue(find.check_find_pwd_fail_status())

    # 手机号格式错误找回密码
    def test_04003_findpwd_phoneNumError(self):
        """找回密码手机号格式错误"""
        logging.info(r'==找回密码手机号格式错误用例==')
        find = FindPwdBusiness(self.driver)
        data = find.get_csv_data('../data/test_data/pwd.csv', 2)
        find.findpwd_action(data[0], data[1])
        sleep(2)
        self.assertTrue(find.check_find_pwd_fail_status())

    # 未注册手机号找回密码
    def test_04004_findpwd_phoneNumUnregistered(self):
        """未注册手机号找回密码"""
        logging.info(r'==未注册手机号找回密码用例==')
        find = FindPwdBusiness(self.driver)
        data = find.get_csv_data('../data/test_data/pwd.csv', 3)
        find.findpwd_action(data[0], data[1])
        sleep(2)
        self.assertTrue(find.check_find_pwd_fail_status())

    # 验证码为空找回密码
    def test_04005_findpwd_codeEmpty(self):
        """验证码为空找回密码"""
        logging.info(r'==验证码为空找回密码用例==')
        find = FindPwdBusiness(self.driver)
        data = find.get_csv_data('../data/test_data/pwd.csv', 4)
        find.findpwd_action(data[0], data[1])
        sleep(2)
        self.assertTrue(find.check_find_pwd_fail_status())

    # 验证码错误
    def test_04006_findpwd_codeError(self):
        """验证码错误找回密码"""
        logging.info(r'==验证码错误找回密码用例==')
        find = FindPwdBusiness(self.driver)
        data = find.get_csv_data('../data/test_data/pwd.csv', 5)
        find.findpwd_action(data[0], data[1])
        sleep(2)
        self.assertTrue(find.check_find_pwd_fail_status())

    # 修改密码密码为空
    def test_04007_modify_pwdEmpty(self):
        """修改密码密码为空"""
        logging.info(r'==修改密码密码为空用例==')
        find = FindPwdBusiness(self.driver)
        data = find.get_csv_data('../data/test_data/pwd.csv', 6)
        find.findpwd_action(data[0], data[1])
        find.modify_action(data[2], data[3])
        sleep(2)
        self.assertTrue(find.check_modify_pwd_fail_status())

    # 修改密码不符合长度
    def test_04008_modify_pwdNomatchLength(self):
        """修改密码不符合长度"""
        logging.info(r'==修改密码不符合长度用例==')
        find = FindPwdBusiness(self.driver)
        data = find.get_csv_data('../data/test_data/pwd.csv', 7)
        find.findpwd_action(data[0], data[1])
        find.modify_action(data[2], data[3])
        sleep(2)
        self.assertTrue(find.check_modify_pwd_fail_status())

    # 修改密码不符合规则
    def test_04009_modify_pwdNomatchRules(self):
        """修改密码不符合规则"""
        logging.info(r'==修改密码不符合规则用例==')
        find = FindPwdBusiness(self.driver)
        data = find.get_csv_data('../data/test_data/pwd.csv', 8)
        find.findpwd_action(data[0], data[1])
        find.modify_action(data[2], data[3])
        sleep(2)
        self.assertTrue(find.check_modify_pwd_fail_status())

    # 修改密码前后输入不一致
    def test_04010_modify_pwdInconsistent(self):
        """修改密码前后不一致"""
        logging.info(r'==修改密码输入前后不一致用例==')
        find = FindPwdBusiness(self.driver)
        data = find.get_csv_data('../data/test_data/pwd.csv', 9)
        find.findpwd_action(data[0], data[1])
        find.modify_action(data[2], data[3])
        sleep(2)
        self.assertTrue(find.check_modify_pwd_fail_status())

    # 修改密码新旧密码重复
    def test_04011_modify_pwdRepeat(self):
        """修改密码新旧密码重复"""
        logging.info(r'==修改密码新旧密码重复用例==')
        find = FindPwdBusiness(self.driver)
        data = find.get_csv_data('../data/test_data/pwd.csv', 11)
        find.findpwd_action(data[0], data[2])
        find.modify_action(data[3], data[3])
        sleep(2)
        self.assertTrue(find.check_modify_pwd_fail_status())

    # 新增供应商
    def test_04012_add_supplier_case(self):
        """新增供应商"""
        self.login_action()
        purchase = PurchaseBusiness(self.driver)
        if self.param == 0:
            purchase.add_supplier("李洲全供应商0号")
        else:
            purchase.add_supplier("李洲全供应商1号")
        # self.assertTrue(purchase.check_supplier_is_exist('李洲全供应商1'))

    # 正常采购用例
    @skip_dependon(depend="test_04012_add_supplier_case")
    def test_05001_first_purchase_case(self):
        """第一次采购（后选供应商）"""
        self.login_action()
        purchase = PurchaseBusiness(self.driver)
        if self.param == 0:
            purchase.pruchase_action(goodname1="测试商品8号", goodnum=50, supplier_name="李洲全供应商0号")
        else:
            purchase.pruchase_action(goodname1="测试商品8号", goodnum=50, supplier_name="李洲全供应商1号")
        purchase_information = purchase.get_purchase_information()
        purchase_order_num = purchase_information["purchase_order_num"]
        ReadData(self.param).write_data('purchase_order', 'num1', purchase_order_num)
        self.assertTrue(purchase_information["status"])

    # 正常采购用例
    @skip_dependon(depend="test_04012_add_supplier_case")
    def test_05002_second_purchase_case(self):
        """第二次采购（后选供应商）"""
        self.login_action()
        purchase = PurchaseBusiness(self.driver)
        if self.param == 0:
            purchase.pruchase_action(goodname1="测试商品8号", goodnum=30, supplier_name="李洲全供应商0号")
        else:
            purchase.pruchase_action(goodname1="测试商品8号", goodnum=30, supplier_name="李洲全供应商1号")
        purchase_information = purchase.get_purchase_information()
        purchase_order_num = purchase_information["purchase_order_num"]
        ReadData(self.param).write_data('purchase_order', 'num2', purchase_order_num)
        self.assertTrue(purchase_information["status"])

    # 正常采购用例
    @skip_dependon(depend="test_04012_add_supplier_case")
    def test_05003_second_purchase_case(self):
        """默认结算账号（现金）"""
        self.login_action()
        purchase = PurchaseBusiness(self.driver)
        if self.param == 0:
            purchase.pruchase_action(goodname1="测试商品8号", goodnum=1, supplier_name="李洲全供应商0号", settlement="现金")
        else:
            purchase.pruchase_action(goodname1="测试商品8号", goodnum=1, supplier_name="李洲全供应商1号", settlement="现金")
        purchase_information = purchase.get_purchase_information()
        purchase_order_num = purchase_information["purchase_order_num"]
        ReadData(self.param).write_data('purchase_order', 'num3', purchase_order_num)
        self.assertTrue(purchase_information["status"])

    # 正常采购用例
    @skip_dependon(depend="test_04012_add_supplier_case")
    def test_05004_second_purchase_case(self):
        """默认结算账号（银行卡）"""
        self.login_action()
        purchase = PurchaseBusiness(self.driver)
        if self.param == 0:
            purchase.pruchase_action(goodname1="测试商品8号", goodnum=1, supplier_name="李洲全供应商0号", settlement="银行卡")
        else:
            purchase.pruchase_action(goodname1="测试商品8号", goodnum=1, supplier_name="李洲全供应商1号", settlement="银行卡")
        purchase_information = purchase.get_purchase_information()
        purchase_order_num = purchase_information["purchase_order_num"]
        ReadData(self.param).write_data('purchase_order', 'num4', purchase_order_num)
        self.assertTrue(purchase_information["status"])

    # 正常采购用例
    @skip_dependon(depend="test_04012_add_supplier_case")
    def test_05005_second_purchase_case(self):
        """默认结算账号（支付宝账户）"""
        self.login_action()
        purchase = PurchaseBusiness(self.driver)
        if self.param == 0:
            purchase.pruchase_action(goodname1="测试商品8号", goodnum=1, supplier_name="李洲全供应商0号", settlement="支付宝账户")
        else:
            purchase.pruchase_action(goodname1="测试商品8号", goodnum=1, supplier_name="李洲全供应商1号", settlement="支付宝账户")
        purchase_information = purchase.get_purchase_information()
        purchase_order_num = purchase_information["purchase_order_num"]
        ReadData(self.param).write_data('purchase_order', 'num5', purchase_order_num)
        self.assertTrue(purchase_information["status"])

    # 正常采购用例
    @skip_dependon(depend="test_04012_add_supplier_case")
    def test_05006_second_purchase_case(self):
        """默认结算账号（微信支付账户）"""
        self.login_action()
        purchase = PurchaseBusiness(self.driver)
        if self.param == 0:
            purchase.pruchase_action(goodname1="测试商品8号", goodnum=1, supplier_name="李洲全供应商0号", settlement="微信支付账户")
        else:
            purchase.pruchase_action(goodname1="测试商品8号", goodnum=1, supplier_name="李洲全供应商1号", settlement="微信支付账户")
        purchase_information = purchase.get_purchase_information()
        purchase_order_num = purchase_information["purchase_order_num"]
        ReadData(self.param).write_data('purchase_order', 'num6', purchase_order_num)
        self.assertTrue(purchase_information["status"])

    # 正常采购用例
    @skip_dependon(depend="test_04012_add_supplier_case")
    def test_05007_purchase_multiple_goods_case(self):
        """有备注的采购单"""
        self.login_action()
        purchase = PurchaseBusiness(self.driver)
        if self.param == 0:
            purchase.pruchase_action(goodname1="测试商品8号", goodnum=1, supplier_name="李洲全供应商0号", price="30",
                                     remark="采购商品备注")
        else:
            purchase.pruchase_action(goodname1="测试商品8号", goodnum=1, supplier_name="李洲全供应商1号", price="30",
                                     remark="采购商品备注")
        purchase_information = purchase.get_purchase_information()
        purchase_order_num = purchase_information["purchase_order_num"]
        ReadData(self.param).write_data('purchase_order', 'num7', purchase_order_num)
        # 判断采购是否正常，采购单单号是否一致，商品库存是否增加
        self.assertTrue(purchase_information["status"])

    # 正常采购用例
    @skip_dependon(depend="test_04012_add_supplier_case")
    def test_05008_purchase_multiple_goods_case(self):
        """采购多种商品"""
        self.login_action()
        purchase = PurchaseBusiness(self.driver)
        if self.param == 0:
            purchase.pruchase_action(goodname1="测试商品8号", goodname2="测试商品3号", goodnum=1, supplier_name="李洲全供应商0号")
        else:
            purchase.pruchase_action(goodname1="测试商品8号", goodname2="测试商品3号", goodnum=1, supplier_name="李洲全供应商1号")
        purchase_information = purchase.get_purchase_information()
        purchase_order_num = purchase_information["purchase_order_num"]
        ReadData(self.param).write_data('purchase_order', 'num8', purchase_order_num)
        self.assertTrue(purchase_information["status"])

    # 采购改价用例
    @skip_dependon(depend="test_04012_add_supplier_case")
    def test_05009_purchase_modfiy_price_case(self):
        """采购进货修改价格采购成功"""
        self.login_action()
        purchase = PurchaseBusiness(self.driver)
        if self.param == 0:
            purchase.pruchase_action(goodname1="测试商品8号", goodnum=1, supplier_name="李洲全供应商0号", price="30")
        else:
            purchase.pruchase_action(goodname1="测试商品8号", goodnum=1, supplier_name="李洲全供应商1号", price="30")
        purchase_information = purchase.get_purchase_information()
        purchase_order_num = purchase_information["purchase_order_num"]
        ReadData(self.param).write_data('purchase_order', 'num9', purchase_order_num)
        # 判断采购是否正常，采购单单号是否一致，商品库存是否增加
        self.assertTrue(purchase_information["status"])
        self.assertEqual(purchase_information["price"], r'￥30.00')

    # 采购单筛选用例
    @skip_dependon(depend="test_05001_first_purchase_case")
    def test_06001_purchase_order_filer_case(self):
        """关键字筛选(单号)"""
        self.login_action()
        purchaseorder = PurchaseOrderBusiness(self.driver)
        ordernum = ReadData(self.param).get_data('purchase_order', 'num1')
        purchaseorder.purchaseorder_action(keyword=ordernum)
        detail_ordernum = purchaseorder.get_detail_purchase_order()
        self.assertEqual(ordernum, detail_ordernum)

    @skip_dependon(depend="test_05007_purchase_multiple_goods_case")
    def test_06002_purchase_order_filer_case(self):
        """关键字筛选(备注)"""
        self.login_action()
        purchaseorder = PurchaseOrderBusiness(self.driver)
        # ordernum = ReadData(self.param).get_data('purchase_order', 'num7')
        purchaseorder.purchaseorder_action(keyword="采购商品备注")
        remark = purchaseorder.get_detail_purchase_remark()
        self.assertEqual(r"采购商品备注", remark)

    @skip_dependon(depend="test_05007_purchase_multiple_goods_case")
    def test_06003_purchase_order_filer_case(self):
        """结算账户筛选（现金）"""
        self.login_action()
        purchaseorder = PurchaseOrderBusiness(self.driver)
        # ordernum = ReadData(self.param).get_data('purchase_order', 'num9')
        purchaseorder.purchaseorder_action(settlement="现金")
        settlement_type = purchaseorder.get_detail_purchase_settlementtype()
        self.assertEqual(r"现金", settlement_type)

    @skip_dependon(depend="test_05004_second_purchase_case")
    def test_06004_purchase_order_filer_case(self):
        """结算账户筛选（银行卡）"""
        self.login_action()
        purchaseorder = PurchaseOrderBusiness(self.driver)
        # ordernum = ReadData(self.param).get_data('purchase_order', 'num4')
        purchaseorder.purchaseorder_action(settlement="银行卡")
        settlement_type = purchaseorder.get_detail_purchase_settlementtype()
        self.assertEqual(r"银行卡", settlement_type)

    @skip_dependon(depend="test_05005_second_purchase_case")
    def test_06005_purchase_order_filer_case(self):
        """结算账户筛选（支付宝账户）"""
        self.login_action()
        purchaseorder = PurchaseOrderBusiness(self.driver)
        # ordernum = ReadData(self.param).get_data('purchase_order', 'num5')
        purchaseorder.purchaseorder_action(settlement="支付宝账户")
        settlement_type = purchaseorder.get_detail_purchase_settlementtype()
        self.assertEqual(r"支付宝账户", settlement_type)

    @skip_dependon(depend="test_05006_second_purchase_case")
    def test_06006_purchase_order_filer_case(self):
        """结算账户筛选（微信支付账户）"""
        self.login_action()
        purchaseorder = PurchaseOrderBusiness(self.driver)
        # ordernum = ReadData(self.param).get_data('purchase_order', 'num6')
        purchaseorder.purchaseorder_action(settlement="微信支付账户")
        settlement_type = purchaseorder.get_detail_purchase_settlementtype()
        self.assertEqual(r"微信支付账户", settlement_type)

    @skip_dependon(depend="test_04012_add_supplier_case")
    def test_06007_purchase_order_filer_case(self):
        """供应商名称筛选"""
        self.login_action()
        purchaseorder = PurchaseOrderBusiness(self.driver)
        # ordernum = ReadData(self.param).get_data('purchase_order', 'num9')
        if self.param == 0:
            purchaseorder.purchaseorder_action(supplier_name='李洲全供应商0号')
        else:
            purchaseorder.purchaseorder_action(supplier_name='李洲全供应商1号')
        supplier = purchaseorder.get_detail_purchase_supplier()
        if self.param == 0:
            self.assertEqual(r'李洲全供应商0号', supplier)
        else:
            self.assertEqual(r'李洲全供应商1号', supplier)

    # 采购单作废用例
    @skip_dependon(depend="test_05002_second_purchase_case")
    def test_06008_obsolete_purchase_order_case(self):
        """采购单作废"""
        self.login_action()
        purchaseorder = PurchaseOrderBusiness(self.driver)
        ordernum = ReadData(self.param).get_data('purchase_order', 'num2')
        purchaseorder.purchaseorder_action(keyword=ordernum, obsolete=True)
        self.assertTrue(purchaseorder.check_obsolete_status())

    # 复制订单用例
    @skip_dependon(depend="test_05004_second_purchase_case")
    def test_06009_copy_purchase_order_case(self):
        """复制采购单"""
        self.login_action()
        purchaseorder = PurchaseOrderBusiness(self.driver)
        ordernum = ReadData(self.param).get_data('purchase_order', 'num4')
        if self.param == 0:
            purchaseorder.purchaseorder_action(keyword=ordernum, copy=True, copy_supplier_name="李洲全供应商0号")
        else:
            purchaseorder.purchaseorder_action(keyword=ordernum, copy=True, copy_supplier_name="李洲全供应商1号")
        order_num = purchaseorder.get_detail_purchase_order()
        ReadData(self.param).write_data('purchase_order', 'num10', order_num)
        # 设置检查点
        self.assertTrue(purchaseorder.check_transaction_success_status())

    @skip_dependon(depend="test_06009_copy_purchase_order_case")
    def test_06010_purchase_order_filer_case(self):
        """无退货进行筛选"""
        self.login_action()
        purchaseorder = PurchaseOrderBusiness(self.driver)
        ordernum = ReadData(self.param).get_data('purchase_order', 'num10')
        purchaseorder.purchaseorder_action(returned=False)
        detail_ordernum = purchaseorder.get_detail_purchase_order()
        self.assertEqual(ordernum, detail_ordernum)

    @skip_dependon(depend="test_06009_copy_purchase_order_case")
    def test_06011_purchase_order_filer_case(self):
        """正常状态筛选"""
        self.login_action()
        purchaseorder = PurchaseOrderBusiness(self.driver)
        ordernum = ReadData(self.param).get_data('purchase_order', 'num10')
        purchaseorder.purchaseorder_action(status=True)
        detail_ordernum = purchaseorder.get_detail_purchase_order()
        self.assertEqual(ordernum, detail_ordernum)

    @skip_dependon(depend="test_05001_first_purchase_case")
    def test_06012_purchase_order_return_case(self):
        """采购单退货"""
        self.login_action()
        purchaseorder = PurchaseOrderBusiness(self.driver)
        ordernum = ReadData(self.param).get_data('purchase_order', 'num1')
        purchaseorder.purchaseorder_action(keyword=ordernum, is_return=True)
        return_dict = purchaseorder.get_purchaseorder_return_information()
        self.assertTrue(return_dict["status"])

    @skip_dependon(depend="test_05001_first_purchase_case")
    def test_06013_purchase_order_return_case(self):
        """采购单改价退货"""
        self.login_action()
        purchaseorder = PurchaseOrderBusiness(self.driver)
        ordernum = ReadData(self.param).get_data('purchase_order', 'num1')
        purchaseorder.purchaseorder_action(keyword=ordernum, is_return=True, modify=True, price=50)
        return_dict = purchaseorder.get_purchaseorder_return_information()
        self.assertTrue(return_dict["status"])
        self.assertEqual(return_dict["return_money"], "￥50.00")

    # 采购单筛选用例
    @skip_dependon(depend="test_06008_obsolete_purchase_order_case")
    def test_06014_purchase_order_filer_case(self):
        """关键字筛选(作废单据)"""
        self.login_action()
        purchaseorder = PurchaseOrderBusiness(self.driver)
        ordernum = ReadData(self.param).get_data('purchase_order', 'num2')
        purchaseorder.purchaseorder_action(status=False)
        detail_ordernum = purchaseorder.get_detail_purchase_order()
        self.assertEqual(ordernum, detail_ordernum)

    # 采购单筛选用例
    @skip_dependon(depend="test_06012_purchase_order_return_case")
    def test_06015_purchase_order_filer_case(self):
        """关键字筛选(退货)"""
        self.login_action()
        purchaseorder = PurchaseOrderBusiness(self.driver)
        ordernum = ReadData(self.param).get_data('purchase_order', 'num1')
        purchaseorder.purchaseorder_action(returned=True)
        detail_ordernum = purchaseorder.get_detail_purchase_order()
        self.assertEqual(ordernum, detail_ordernum)

    @skip_dependon(depend="test_05001_first_purchase_case")
    def test_07001_original_purchase_return_case(self):
        """原始采购单退货"""
        self.login_action()
        purchasereutrn = PurchaseReturnBusiness(self.driver)
        pruchase_order = ReadData(self.param).get_data('purchase_order', 'num1')
        purchasereutrn.original_order_return_action(1, normal=True, keyword=pruchase_order)
        purchasereturn_num = purchasereutrn.get_purchase_return_ordernum()
        ReadData(self.param).write_data('purchase_return_order', 'num1', purchasereturn_num)
        self.assertTrue(purchasereutrn.check_purchase_return_success_status())

    # 原始采购单退货
    @skip_dependon(depend="test_05001_first_purchase_case")
    def test_07002_original_purchase_return_case(self):
        """原单退货（现金）"""
        self.login_action()
        purchasereutrn = PurchaseReturnBusiness(self.driver)
        pruchase_order = ReadData(self.param).get_data('purchase_order', 'num1')
        purchasereutrn.original_order_return_action(1, keyword=pruchase_order, account='现金')
        purchasereturn_num = purchasereutrn.get_purchase_return_ordernum()
        ReadData(self.param).write_data('purchase_return_order', 'num2', purchasereturn_num)
        sleep(1)
        info = purchasereutrn.check_account_type()
        self.assertEqual(info, '现金')

    # 原始采购单退货
    @skip_dependon(depend="test_05001_first_purchase_case")
    def test_07003_original_purchase_return_case(self):
        """原单退货（银行卡）"""
        self.login_action()
        puchasereutrn = PurchaseReturnBusiness(self.driver)
        pruchase_order = ReadData(self.param).get_data('purchase_order', 'num1')
        puchasereutrn.original_order_return_action(1, keyword=pruchase_order, account='银行卡')
        purchasereturn_num = puchasereutrn.get_purchase_return_ordernum()
        ReadData(self.param).write_data('purchase_return_order', 'num3', purchasereturn_num)
        self.assertEqual(puchasereutrn.check_account_type(), '银行卡')

    # 原始采购单退货
    @skip_dependon(depend="test_05001_first_purchase_case")
    def test_07004_original_purchase_return_case(self):
        """原单退货（支付宝账户）"""
        self.login_action()
        puchasereutrn = PurchaseReturnBusiness(self.driver)
        pruchase_order = ReadData(self.param).get_data('purchase_order', 'num1')
        puchasereutrn.original_order_return_action(1, keyword=pruchase_order, account='支付宝账户')
        purchasereturn_num = puchasereutrn.get_purchase_return_ordernum()
        ReadData(self.param).write_data('purchase_return_order', 'num4', purchasereturn_num)
        self.assertEqual(puchasereutrn.check_account_type(), '支付宝账户')

    # 原始采购单退货
    @skip_dependon(depend="test_05001_first_purchase_case")
    def test_07005_original_purchase_return_case(self):
        """原单退货（微信支付账户）"""
        self.login_action()
        puchasereutrn = PurchaseReturnBusiness(self.driver)
        pruchase_order = ReadData(self.param).get_data('purchase_order', 'num1')
        puchasereutrn.original_order_return_action(1, keyword=pruchase_order, account='微信支付账户')
        purchasereturn_num = puchasereutrn.get_purchase_return_ordernum()
        ReadData(self.param).write_data('purchase_return_order', 'num5', purchasereturn_num)
        self.assertEqual(puchasereutrn.check_account_type(), '微信支付账户')

    # 原始采购单退货
    @skip_dependon(depend="test_05001_first_purchase_case")
    def test_07006_original_purchase_return_case(self):
        """原单退货（其他账户）"""
        self.login_action()
        puchasereutrn = PurchaseReturnBusiness(self.driver)
        pruchase_order = ReadData(self.param).get_data('purchase_order', 'num1')
        puchasereutrn.original_order_return_action(1, keyword=pruchase_order, account='其他账户')
        purchasereturn_num = puchasereutrn.get_purchase_return_ordernum()
        ReadData(self.param).write_data('purchase_return_order', 'num6', purchasereturn_num)
        self.assertEqual(puchasereutrn.check_account_type(), '其他账户')

    # 原始采购单退货
    @skip_dependon(depend="test_05001_first_purchase_case")
    def test_07007_original_purchase_return_case(self):
        """原单退货（继续退货）"""
        self.login_action()
        purchasereutrn = PurchaseReturnBusiness(self.driver)
        pruchase_order = ReadData(self.param).get_data('purchase_order', 'num1')
        purchasereutrn.original_order_return_action(1, normal=True, keyword=pruchase_order, is_continue=True)
        purchasereturn_num = purchasereutrn.get_purchase_return_ordernum()
        ReadData(self.param).write_data('purchase_return_order', 'num7', purchasereturn_num)
        self.assertTrue(purchasereutrn.check_purchase_return_success_status())

    # 原始采购单退货
    @skip_dependon(depend="test_05001_first_purchase_case")
    def test_07008_original_purchase_return_case(self):
        """原单退货（改价）"""
        self.login_action()
        purchasereutrn = PurchaseReturnBusiness(self.driver)
        pruchase_order = ReadData(self.param).get_data('purchase_order', 'num1')
        purchasereutrn.original_order_return_action(1, keyword=pruchase_order, modify=1000)
        purchasereturn_num = purchasereutrn.get_purchase_return_ordernum()
        total_money = purchasereutrn.check_total_money()
        ReadData(self.param).write_data('purchase_return_order', 'num8', purchasereturn_num)
        self.assertEqual(total_money, '￥1000.00')

    # 原始采购单退货
    @skip_dependon(depend="test_05001_first_purchase_case")
    def test_07009_original_purchase_return_case(self):
        """原单退货（备注）"""
        self.login_action()
        purchasereutrn = PurchaseReturnBusiness(self.driver)
        pruchase_order = ReadData(self.param).get_data('purchase_order', 'num1')
        purchasereutrn.original_order_return_action(1, keyword=pruchase_order, remark='退货商品')
        purchasereturn_num = purchasereutrn.get_purchase_return_ordernum()
        info = purchasereutrn.check_remaks()
        ReadData(self.param).write_data('purchase_return_order', 'num9', purchasereturn_num)
        self.assertEqual(info, '退货商品')

    # 直接退货
    def test_07010_direct_purchase_return_case(self):
        """直接退货（正常）"""
        self.login_action()
        purchasereutrn = PurchaseReturnBusiness(self.driver)
        if self.param == 0:
            purchasereutrn.direct_return_action('李洲全供应商0号', normal=True, name='测试商品8号', num=1)
        else:
            purchasereutrn.direct_return_action('李洲全供应商1号', normal=True, name='测试商品8号', num=1)
        purchasereturn_num = purchasereutrn.get_purchase_return_ordernum()
        ReadData(self.param).write_data('purchase_return_order', 'num10', purchasereturn_num)
        self.assertTrue(purchasereutrn.check_purchase_return_success_status())

    # 直接退货
    def test_07011_direct_purchase_return_case(self):
        """直接退货（现金）"""
        self.login_action()
        purchasereutrn = PurchaseReturnBusiness(self.driver)
        if self.param == 0:
            purchasereutrn.direct_return_action('李洲全供应商0号', name='测试商品8号', num=1, account='现金')
        else:
            purchasereutrn.direct_return_action('李洲全供应商1号', name='测试商品8号', num=1, account='现金')
        purchasereturn_num = purchasereutrn.get_purchase_return_ordernum()
        ReadData(self.param).write_data('purchase_return_order', 'num11', purchasereturn_num)
        self.assertTrue(purchasereutrn.check_purchase_return_success_status())

    # 直接退货
    def test_07012_direct_purchase_return_case(self):
        """直接退货（银行卡）"""
        self.login_action()
        purchasereutrn = PurchaseReturnBusiness(self.driver)
        if self.param == 0:
            purchasereutrn.direct_return_action('李洲全供应商0号', name='测试商品8号', num=1, account='银行卡')
        else:
            purchasereutrn.direct_return_action('李洲全供应商1号', name='测试商品8号', num=1, account='银行卡')
        purchasereturn_num = purchasereutrn.get_purchase_return_ordernum()
        ReadData(self.param).write_data('purchase_return_order', 'num12', purchasereturn_num)
        self.assertTrue(purchasereutrn.check_purchase_return_success_status())

    # 直接退货
    def test_07013_direct_purchase_return_case(self):
        """直接退货（支付宝账户）"""
        self.login_action()
        purchasereutrn = PurchaseReturnBusiness(self.driver)
        if self.param == 0:
            purchasereutrn.direct_return_action('李洲全供应商0号', name='测试商品8号', num=1, account='支付宝账户')
        else:
            purchasereutrn.direct_return_action('李洲全供应商1号', name='测试商品8号', num=1, account='支付宝账户')
        purchasereturn_num = purchasereutrn.get_purchase_return_ordernum()
        ReadData(self.param).write_data('purchase_return_order', 'num13', purchasereturn_num)
        self.assertTrue(purchasereutrn.check_purchase_return_success_status())

    # 直接退货
    def test_07014_direct_purchase_return_case(self):
        """直接退货（微信支付账户）"""
        self.login_action()
        purchasereutrn = PurchaseReturnBusiness(self.driver)
        if self.param == 0:
            purchasereutrn.direct_return_action('李洲全供应商0号', name='测试商品8号', num=1, account='微信支付账户')
        else:
            purchasereutrn.direct_return_action('李洲全供应商1号', name='测试商品8号', num=1, account='微信支付账户')
        purchasereturn_num = purchasereutrn.get_purchase_return_ordernum()
        ReadData(self.param).write_data('purchase_return_order', 'num14', purchasereturn_num)
        self.assertTrue(purchasereutrn.check_purchase_return_success_status())

    # 直接退货
    def test_07015_direct_purchase_return_case(self):
        """直接退货（其他账户）"""
        self.login_action()
        purchasereutrn = PurchaseReturnBusiness(self.driver)
        if self.param == 0:
            purchasereutrn.direct_return_action('李洲全供应商0号', name='测试商品8号', num=1, account='其他账户')
        else:
            purchasereutrn.direct_return_action('李洲全供应商1号', name='测试商品8号', num=1, account='其他账户')
        purchasereturn_num = purchasereutrn.get_purchase_return_ordernum()
        ReadData(self.param).write_data('purchase_return_order', 'num15', purchasereturn_num)
        self.assertTrue(purchasereutrn.check_purchase_return_success_status())

    # 直接退货
    def test_07016_direct_purchase_return_case(self):
        """直接退货（继续退货）"""
        self.login_action()
        purchasereutrn = PurchaseReturnBusiness(self.driver)
        if self.param == 0:
            purchasereutrn.direct_return_action('李洲全供应商0号', normal=True, name='测试商品8号', num=1, is_continue=True)
        else:
            purchasereutrn.direct_return_action('李洲全供应商1号', normal=True, name='测试商品8号', num=1, is_continue=True)
        purchasereturn_num = purchasereutrn.get_purchase_return_ordernum()
        ReadData(self.param).write_data('purchase_return_order', 'num16', purchasereturn_num)
        self.assertTrue(purchasereutrn.check_purchase_return_success_status())

    # 直接退货
    def test_07017_direct_purchase_return_case(self):
        """直接退货（改价）"""
        self.login_action()
        purchasereutrn = PurchaseReturnBusiness(self.driver)
        if self.param == 0:
            purchasereutrn.direct_return_action('李洲全供应商0号', name='测试商品8号', num=1, modify=1000)
        else:
            purchasereutrn.direct_return_action('李洲全供应商1号', name='测试商品8号', num=1, modify=1000)
        purchasereturn_num = purchasereutrn.get_purchase_return_ordernum()
        ReadData(self.param).write_data('purchase_return_order', 'num17', purchasereturn_num)
        total_money = purchasereutrn.check_total_money()
        self.assertEqual(total_money, '￥1000.00')

    # 直接退货
    def test_07018_direct_purchase_return_case(self):
        """直接退货（备注）"""
        self.login_action()
        purchasereutrn = PurchaseReturnBusiness(self.driver)
        if self.param == 0:
            purchasereutrn.direct_return_action('李洲全供应商0号', name='测试商品8号', num=1, remark='直接退货备注')
        else:
            purchasereutrn.direct_return_action('李洲全供应商1号', name='测试商品8号', num=1, remark='直接退货备注')
        purchasereturn_num = purchasereutrn.get_purchase_return_ordernum()
        ReadData(self.param).write_data('purchase_return_order', 'num18', purchasereturn_num)
        info = purchasereutrn.check_remaks()
        self.assertEqual(info, '直接退货备注')

    # 采购退货单筛选
    @skip_dependon(depend="test_07001_original_purchase_return_case")
    def test_08001_purchase_return_order(self):
        """正常筛选"""
        self.login_action()
        p = PurchaseReturnOrderBusiness(self.driver)
        purchase_return_order = ReadData(self.param).get_data('purchase_return_order', 'num1')
        p.purchase_return_order_action(keyword=purchase_return_order)
        confim_num = p.get_detail_ptuchase_order()
        self.assertEqual(purchase_return_order, confim_num)

    @skip_dependon(depend="test_07002_original_purchase_return_case")
    def test_08002_purchase_return_order(self):
        """采购退货单作废"""
        self.login_action()
        p = PurchaseReturnOrderBusiness(self.driver)
        purchase_return_order = ReadData(self.param).get_data('purchase_return_order', 'num2')
        p.purchase_return_order_action(keyword=purchase_return_order, obsolete=True)
        self.assertTrue(p.check_obsolete_status_())

    @skip_dependon(depend="test_08002_purchase_return_order")
    def test_08003_purchase_return_order(self):
        """作废单据筛选"""
        self.login_action()
        p = PurchaseReturnOrderBusiness(self.driver)
        purchase_return_order = ReadData(self.param).get_data('purchase_return_order', 'num2')
        p.purchase_return_order_action(status=False)
        confim_num = p.get_detail_ptuchase_order()
        self.assertEqual(purchase_return_order, confim_num)

    @skip_dependon(depend="test_07003_original_purchase_return_case")
    def test_08004_purchase_return_order(self):
        """单据复制（原单退货）"""
        self.login_action()
        p = PurchaseReturnOrderBusiness(self.driver)
        purchase_return_order = ReadData(self.param).get_data('purchase_return_order', 'num3')
        if self.param == 0:
            p.purchase_return_order_action(keyword=purchase_return_order, copy=True, supplier_name='李洲全供应商0号',
                                           is_original=True)
        else:
            p.purchase_return_order_action(keyword=purchase_return_order, copy=True, supplier_name='李洲全供应商1号',
                                           is_original=True)
        purchase_return_num = p.get_detail_ptuchase_order()
        ReadData(self.param).write_data('purchase_return_order', 'num19', purchase_return_num)
        self.assertTrue(p.check_purchase_return_status())

    @skip_dependon(depend="test_07010_direct_purchase_return_case")
    def test_08005_purchase_return_order(self):
        """单据复制（直接退货）"""
        self.login_action()
        p = PurchaseReturnOrderBusiness(self.driver)
        purchase_return_order = ReadData(self.param).get_data('purchase_return_order', 'num10')
        if self.param == 0:
            p.purchase_return_order_action(keyword=purchase_return_order, copy=True, supplier_name='李洲全供应商0号')
        else:
            p.purchase_return_order_action(keyword=purchase_return_order, copy=True, supplier_name='李洲全供应商1号')
        purchase_return_num = p.get_detail_ptuchase_order()
        ReadData(self.param).write_data('purchase_return_order', 'num20', purchase_return_num)
        self.assertTrue(p.check_purchase_return_status())

    @skip_dependon(depend="test_07002_original_purchase_return_case")
    def test_08006_purchase_return_order(self):
        """结算方式（现金）"""
        self.login_action()
        p = PurchaseReturnOrderBusiness(self.driver)
        p.purchase_return_order_action(settlement='现金')
        settlement_type = p.get_detail_settlement_type()
        self.assertEqual('现金', settlement_type)

    @skip_dependon(depend="test_07003_original_purchase_return_case")
    def test_08007_purchase_return_order(self):
        """结算方式（银行卡）"""
        self.login_action()
        p = PurchaseReturnOrderBusiness(self.driver)
        p.purchase_return_order_action(settlement='银行卡')
        settlement_type = p.get_detail_settlement_type()
        self.assertEqual('银行卡', settlement_type)

    @skip_dependon(depend="test_07004_original_purchase_return_case")
    def test_08008_purchase_return_order(self):
        """结算方式（支付宝账户）"""
        self.login_action()
        p = PurchaseReturnOrderBusiness(self.driver)
        p.purchase_return_order_action(settlement='支付宝账户')
        settlement_type = p.get_detail_settlement_type()
        self.assertEqual('支付宝账户', settlement_type)

    @skip_dependon(depend="test_07005_original_purchase_return_case")
    def test_08009_purchase_return_order(self):
        """结算方式（微信支付账户）"""
        self.login_action()
        p = PurchaseReturnOrderBusiness(self.driver)
        p.purchase_return_order_action(settlement='微信支付账户')
        settlement_type = p.get_detail_settlement_type()
        self.assertEqual('微信支付账户', settlement_type)

    @skip_dependon(depend="test_07006_original_purchase_return_case")
    def test_08010_purchase_return_order(self):
        """结算方式（其他账户）"""
        self.login_action()
        p = PurchaseReturnOrderBusiness(self.driver)
        p.purchase_return_order_action(settlement='其他账户')
        settlement_type = p.get_detail_settlement_type()
        self.assertEqual('其他账户', settlement_type)

    # 正常收银
    @skip_dependon(depend="test_05001_first_purchase_case")
    def test_09001_cashier_case(self):
        """正常收银（现金）"""
        self.login_action()
        logging.info('开始收银')
        cashier = CashBusiness(self.driver)
        cashier.cashier_goods(num=30)
        sleep(1)
        status_dict = cashier.get_cash_success_information()
        sales_order_num = status_dict["sales_order_num"]
        ReadData(self.param).write_data('sale_order', 'num1', sales_order_num)
        self.assertTrue(status_dict["status"])
        self.assertEqual("现金", status_dict["settlement_type"])

    @skip_dependon(depend="test_09001_cashier_case")
    def test_09002_cashier_case(self):
        """正常收银（银行卡）"""
        self.login_action()
        logging.info('开始收银')
        cashier = CashBusiness(self.driver)
        cashier.cashier_goods(num=1, cash_type="银行卡")
        sleep(1)
        status_dict = cashier.get_cash_success_information()
        sales_order_num = status_dict["sales_order_num"]
        ReadData(self.param).write_data('sale_order', 'num2', sales_order_num)
        self.assertTrue(status_dict["status"])
        self.assertEqual("银行卡", status_dict["settlement_type"])

    @skip_dependon(depend="test_09001_cashier_case")
    def test_09003_cashier_case(self):
        """正常收银（支付宝账户）"""
        self.login_action()
        logging.info('开始收银')
        cashier = CashBusiness(self.driver)
        cashier.cashier_goods(num=1, cash_type="支付宝账户")
        sleep(1)
        status_dict = cashier.get_cash_success_information()
        sales_order_num = status_dict["sales_order_num"]
        ReadData(self.param).write_data('sale_order', 'num3', sales_order_num)
        self.assertTrue(status_dict["status"])
        self.assertEqual("支付宝账户", status_dict["settlement_type"])

    @skip_dependon(depend="test_09001_cashier_case")
    def test_09004_cashier_case(self):
        """正常收银（微信支付账户）"""
        self.login_action()
        logging.info('开始收银')
        cashier = CashBusiness(self.driver)
        cashier.cashier_goods(num=1, cash_type="微信支付账户")
        sleep(1)
        status_dict = cashier.get_cash_success_information()
        sales_order_num = status_dict["sales_order_num"]
        ReadData(self.param).write_data('sale_order', 'num4', sales_order_num)
        self.assertTrue(status_dict["status"])
        self.assertEqual("微信支付账户", status_dict["settlement_type"])

    @skip_dependon(depend="test_09001_cashier_case")
    def test_09005_cashier_case(self):
        """正常收银（默认老板销售员）"""
        self.login_action()
        logging.info('开始收银')
        cashier = CashBusiness(self.driver)
        cashier.cashier_goods(num=1)
        sleep(1)
        status_dict = cashier.get_cash_success_information()
        sales_order_num = status_dict["sales_order_num"]
        ReadData(self.param).write_data('sale_order', 'num5', sales_order_num)
        self.assertTrue(status_dict["status"])
        self.assertEqual("老板", status_dict["saler"])

    @skip_dependon(depend="test_09001_cashier_case")
    def test_09006_cashier_case(self):
        """正常收银（手动选择销售员）"""
        self.login_action()
        logging.info('开始收银')
        cashier = CashBusiness(self.driver)
        if self.param == 0:
            cashier.cashier_goods(num=1, saler1='李洲全-13888888811')
        else:
            cashier.cashier_goods(num=1, saler1='李一-13777777771')
        sleep(1)
        status_dict = cashier.get_cash_success_information()
        sales_order_num = status_dict["sales_order_num"]
        ReadData(self.param).write_data('sale_order', 'num6', sales_order_num)
        self.assertTrue(status_dict["status"])
        self.assertEqual("李洲全", status_dict["saler"])

    @skip_dependon(depend="test_09001_cashier_case")
    def test_09007_cashier_case(self):
        """正常收银（手动选择销售员）"""
        self.login_action()
        logging.info('开始收银')
        cashier = CashBusiness(self.driver)
        cashier.cashier_goods(num=1, saler1='李洲全-13888888811', saler2="测试人员-16666668888")
        sleep(1)
        status_dict = cashier.get_cash_success_information()
        sales_order_num = status_dict["sales_order_num"]
        ReadData(self.param).write_data('sale_order', 'num7', sales_order_num)
        self.assertTrue(status_dict["status"])
        self.assertEqual("测试人员,李洲全", status_dict["saler"])

    # 商品打折销售
    @skip_dependon(depend="test_09001_cashier_case")
    def test_09008_goods_discount_sales_case(self):
        """商品打折销售(1折),订单无优惠"""
        self.login_action()
        cashier = CashBusiness(self.driver)
        cashier.cashier_goods(num=1, normal=True, good_discount=True, good_value=1)
        status_dict = cashier.get_cash_success_information()
        sales_order_num = status_dict["sales_order_num"]
        ReadData(self.param).write_data('sale_order', 'num8', sales_order_num)
        self.assertTrue(status_dict["status"])
        self.assertEqual(status_dict["price"], r'￥20.00')

    # 商品改价销售
    @skip_dependon(depend="test_09001_cashier_case")
    def test_09009_goods_modify_sales_case(self):
        """商品改价销售(￥20.00)，订单无优惠"""
        self.login_action()
        cashier = CashBusiness(self.driver)
        cashier.cashier_goods(num=1, normal=True, good_modify=True, good_value=20)
        status_dict = cashier.get_cash_success_information()
        sales_order_num = status_dict["sales_order_num"]
        ReadData(self.param).write_data('sale_order', 'num9', sales_order_num)
        self.assertTrue(status_dict["status"])
        self.assertEqual(status_dict["price"], r'￥20.00')

    # 商品打折，订单打折销售
    @skip_dependon(depend="test_09001_cashier_case")
    def test_09010_discount_discount_sales_case(self):
        """商品打折(5折)，订单打折销售（5折）"""
        self.login_action()
        cashier = CashBusiness(self.driver)
        cashier.cashier_goods(num=1, normal=True, good_discount=True, good_value=5, offer=False,
                              order_discount=True, order_value=5)
        status_dict = cashier.get_cash_success_information()
        sales_order_num = status_dict["sales_order_num"]
        ReadData(self.param).write_data('sale_order', 'num10', sales_order_num)
        self.assertTrue(status_dict["status"])
        self.assertEqual(status_dict["price"], r'￥50.00')

    # 商品改价，订单打折销售
    @skip_dependon(depend="test_09001_cashier_case")
    def test_09011_modify_discount_sales_case(self):
        """商品改价(￥100)，订单打折销售（8折）"""
        self.login_action()
        cashier = CashBusiness(self.driver)
        cashier.cashier_goods(num=1, normal=True, good_modify=True, good_value=100, offer=False,
                              order_discount=True, order_value=8)
        status_dict = cashier.get_cash_success_information()
        sales_order_num = status_dict["sales_order_num"]
        ReadData(self.param).write_data('sale_order', 'num11', sales_order_num)
        self.assertTrue(status_dict["status"])
        self.assertEqual(status_dict["price"], r'￥80.00')

    # 商品打折，订单改价销售
    @skip_dependon(depend="test_09001_cashier_case")
    def test_09012_discount_modify_sales_case(self):
        """商品打折（5折），订单改价（￥88）"""
        self.login_action()
        cashier = CashBusiness(self.driver)
        cashier.cashier_goods(num=1, normal=True, good_discount=True, good_value=5, offer=False,
                              order_modify=True, order_value=88)
        status_dict = cashier.get_cash_success_information()
        sales_order_num = status_dict["sales_order_num"]
        ReadData(self.param).write_data('sale_order', 'num12', sales_order_num)
        self.assertTrue(status_dict["status"])
        self.assertEqual(status_dict["price"], r'￥88.00')

    # 商品改价，订单改价销售
    @skip_dependon(depend="test_09001_cashier_case")
    def test_09013_modify_modify_sales_case(self):
        """商品改价(￥100)，订单改价（￥88）"""
        self.login_action()
        cashier = CashBusiness(self.driver)
        cashier.cashier_goods(num=1, normal=True, good_modify=True, good_value=100, offer=False,
                              order_modify=True, order_value=88)
        status_dict = cashier.get_cash_success_information()
        sales_order_num = status_dict["sales_order_num"]
        ReadData(self.param).write_data('sale_order', 'num13', sales_order_num)
        self.assertTrue(status_dict["status"])
        self.assertEqual(status_dict["price"], r'￥88.00')

    # 订单打折销售
    @skip_dependon(depend="test_09001_cashier_case")
    def test_09014_order_discount_sales_case(self):
        """商品无优惠，订单打折（5）"""
        self.login_action()
        cashier = CashBusiness(self.driver)
        cashier.cashier_goods(num=1, offer=False, order_discount=True, order_value=5)
        status_dict = cashier.get_cash_success_information()
        sales_order_num = status_dict["sales_order_num"]
        ReadData(self.param).write_data('sale_order', 'num14', sales_order_num)
        self.assertTrue(status_dict["status"])
        self.assertEqual(status_dict["price"], r'￥100.00')

    # 商品改价，订单改价销售
    @skip_dependon(depend="test_09001_cashier_case")
    def test_09015_order_modify_sales_case(self):
        """商品无优惠，订单改价（￥88）"""
        self.login_action()
        cashier = CashBusiness(self.driver)
        cashier.cashier_goods(num=1, offer=False, order_modify=True, order_value=88)
        status_dict = cashier.get_cash_success_information()
        sales_order_num = status_dict["sales_order_num"]
        ReadData(self.param).write_data('sale_order', 'num15', sales_order_num)
        self.assertTrue(status_dict["status"])
        self.assertEqual(status_dict["price"], r'￥88.00')

    # 销售单复制在销售
    @skip_dependon(depend="test_09001_cashier_case")
    def test_10001_sales_order_copy_case(self):
        """销售单复制并生成新的销售单"""
        self.login_action()
        salesorder = SalesOrderBusiness(self.driver)
        ordernum = ReadData(self.param).get_data('sale_order', 'num1')
        salesorder.sales_order_action(keyword=ordernum, copy=True)
        sales_order_num = salesorder.get_sales_order_num()
        ReadData(self.param).write_data('sale_order', 'num16', sales_order_num)
        # 设置检查点
        self.assertTrue(salesorder.check_transaction_success_status())

    # 销售单作废
    @skip_dependon(depend="test_10001_sales_order_copy_case")
    def test_10002_sales_order_copy_case(self):
        """销售单作废"""
        self.login_action()
        salesorder = SalesOrderBusiness(self.driver)
        ordernum = ReadData(self.param).get_data('sale_order', 'num16')
        salesorder.sales_order_action(keyword=ordernum, obsolete=True)
        # 设置检查点
        self.assertTrue(salesorder.check_sales_order_status())

    # 原始销售单退货
    @skip_dependon(depend="test_10001_sales_order_copy_case")
    def test_10003_original_sales_return_case(self):
        """原始销售单退货"""
        self.login_action()
        salesreturn = SalesReturnBusiness(self.driver)
        sales_order = ReadData(self.param).get_data('sale_order', 'num1')
        salesreturn.original_order_return_action(good_name='测试商品8号', good_num=1, normal=True, keyword=sales_order)
        sales_return_num = salesreturn.get_sales_return_ordernum()
        ReadData(self.param).write_data('sale_return_order', 'num1', sales_return_num)
        self.assertTrue(salesreturn.check_sales_return_success_status())

    # 原始销售单退货
    @skip_dependon(depend="test_09001_cashier_case")
    def test_10004_original_sales_return_case(self):
        """原单退货（现金）"""
        self.login_action()
        salesreturn = SalesReturnBusiness(self.driver)
        sales_order = ReadData(self.param).get_data('sale_order', 'num1')
        salesreturn.original_order_return_action(good_name='测试商品8号', good_num=1, keyword=sales_order, account='现金')
        salesreturn_num = salesreturn.get_detail_return_ordernum()
        ReadData(self.param).write_data('sale_return_order', 'num2', salesreturn_num)
        self.assertEqual(salesreturn.check_account_type(), '现金')

    # 原始销售单退货
    @skip_dependon(depend="test_09002_cashier_case")
    def test_10005_original_sales_return_case(self):
        """原单退货（银行卡）"""
        self.login_action()
        salesreturn = SalesReturnBusiness(self.driver)
        sales_order = ReadData(self.param).get_data('sale_order', 'num2')
        salesreturn.original_order_return_action(good_name='测试商品8号', good_num=1, keyword=sales_order, account='银行卡')
        salesreturn_num = salesreturn.get_detail_return_ordernum()
        ReadData(self.param).write_data('sale_return_order', 'num3', salesreturn_num)
        self.assertEqual(salesreturn.check_account_type(), '银行卡')

    # 原始销售单退货
    @skip_dependon(depend="test_09003_cashier_case")
    def test_10006_original_sales_return_case(self):
        """原单退货（支付宝账户）"""
        self.login_action()
        salesreturn = SalesReturnBusiness(self.driver)
        sales_order = ReadData(self.param).get_data('sale_order', 'num3')
        salesreturn.original_order_return_action(good_name='测试商品8号', good_num=1, keyword=sales_order, account='支付宝账户')
        salesreturn_num = salesreturn.get_detail_return_ordernum()
        ReadData(self.param).write_data('sale_return_order', 'num4', salesreturn_num)
        self.assertEqual(salesreturn.check_account_type(), '支付宝账户')

    # 原始销售单退货
    @skip_dependon(depend="test_09004_cashier_case")
    def test_10007_original_sales_return_case(self):
        """原单退货（微信支付账户）"""
        self.login_action()
        salesreturn = SalesReturnBusiness(self.driver)
        sales_order = ReadData(self.param).get_data('sale_order', 'num4')
        salesreturn.original_order_return_action(good_name='测试商品8号', good_num=1, keyword=sales_order, account='微信支付账户')
        salesreturn_num = salesreturn.get_detail_return_ordernum()
        ReadData(self.param).write_data('sale_return_order', 'num5', salesreturn_num)
        self.assertEqual(salesreturn.check_account_type(), '微信支付账户')

    # # 原始销售单退货
    # def test_10008_original_sales_return_case(self):
    #     """原单退货（其他账户）"""
    #     self.login_action()
    #     salesreturn = SalesReturnBusiness(self.driver)
    #     sales_order = ReadData().get_data('sale_order', 'num5')
    #     salesreturn.original_order_return_action(good_name='测试商品8号', good_num=1, keyword=sales_order, account='其他账户')
    #     salesreturn_num = salesreturn.get_detail_return_ordernum()
    #     ReadData().write_data('sale_return_order', 'num6', salesreturn_num)
    #     self.assertEqual(salesreturn.check_account_type(), '其他账户')

    # 原始销售单退货
    @skip_dependon(depend="test_09001_cashier_case")
    def test_10009_original_sales_return_case(self):
        """原单退货（继续退货）"""
        self.login_action()
        salesreturn = SalesReturnBusiness(self.driver)
        sales_order = ReadData(self.param).get_data('sale_order', 'num1')
        salesreturn.original_order_return_action(good_name='测试商品8号', good_num=1, normal=True, keyword=sales_order,
                                                 is_continue=True)
        salesreturn_num = salesreturn.get_sales_return_ordernum()
        ReadData(self.param).write_data('sale_return_order', 'num7', salesreturn_num)
        self.assertTrue(salesreturn.check_sales_return_success_status())

    # 原始销售单退货
    @skip_dependon(depend="test_09001_cashier_case")
    def test_10010_original_sales_return_case(self):
        """原单退货（改价）"""
        self.login_action()
        salesreturn = SalesReturnBusiness(self.driver)
        sales_order = ReadData(self.param).get_data('sale_order', 'num1')
        salesreturn.original_order_return_action(good_name='测试商品8号', good_num=1, keyword=sales_order, modify=1000)
        salesreturn_num = salesreturn.get_detail_return_ordernum()
        total_money = salesreturn.check_total_money()
        ReadData(self.param).write_data('sale_return_order', 'num8', salesreturn_num)
        self.assertEqual(total_money, '￥1000.00')

    # 原始销售单退货
    @skip_dependon(depend="test_09001_cashier_case")
    def test_10011_original_sales_return_case(self):
        """原单退货（备注）"""
        self.login_action()
        salesreturn = SalesReturnBusiness(self.driver)
        sales_order = ReadData(self.param).get_data('sale_order', 'num1')
        salesreturn.original_order_return_action(good_name='测试商品8号', good_num=1, keyword=sales_order, remark='退货商品')
        salesreturn_num = salesreturn.get_detail_return_ordernum()
        info = salesreturn.check_remaks()
        ReadData(self.param).write_data('sale_return_order', 'num9', salesreturn_num)
        self.assertEqual(info, '退货商品')

    # 直接退货
    def test_10012_direct_sales_return_case(self):
        """直接退货（正常）"""
        self.login_action()
        salesreutrn = SalesReturnBusiness(self.driver)
        if self.param == 0:
            salesreutrn.direct_return_action('李洲全-13888888811', normal=True, name='测试商品8号', num=1)
        else:
            salesreutrn.direct_return_action('李一-13777777771', normal=True, name='测试商品8号', num=1)
        salesreturn_num = salesreutrn.get_sales_return_ordernum()
        ReadData(self.param).write_data('sale_return_order', 'num10', salesreturn_num)
        self.assertTrue(salesreutrn.check_sales_return_success_status())

    # 直接退货
    def test_10013_direct_sales_return_case(self):
        """直接退货（现金）"""
        self.login_action()
        salesreutrn = SalesReturnBusiness(self.driver)
        if self.param == 0:
            salesreutrn.direct_return_action('李洲全-13888888811', name='测试商品8号', num=1, account='现金')
        else:
            salesreutrn.direct_return_action('李一-13777777771', name='测试商品8号', num=1, account='现金')
        salesreturn_num = salesreutrn.get_sales_return_ordernum()
        ReadData(self.param).write_data('sale_return_order', 'num11', salesreturn_num)
        self.assertTrue(salesreutrn.check_sales_return_success_status())

    # 直接退货
    def test_10014_direct_sales_return_case(self):
        """直接退货（银行卡）"""
        self.login_action()
        salesreutrn = SalesReturnBusiness(self.driver)
        if self.param == 0:
            salesreutrn.direct_return_action('李洲全-13888888811', name='测试商品8号', num=1, account='银行卡')
        else:
            salesreutrn.direct_return_action('李一-13777777771', name='测试商品8号', num=1, account='银行卡')
        salesreturn_num = salesreutrn.get_sales_return_ordernum()
        ReadData(self.param).write_data('sale_return_order', 'num12', salesreturn_num)
        self.assertTrue(salesreutrn.check_sales_return_success_status())

    # 直接退货
    def test_10015_direct_sales_return_case(self):
        """直接退货（微信支付账户）"""
        self.login_action()
        salesreutrn = SalesReturnBusiness(self.driver)
        if self.param == 0:
            salesreutrn.direct_return_action('李洲全-13888888811', name='测试商品8号', num=1, account='微信支付账户')
        else:
            salesreutrn.direct_return_action('李一-13777777771', name='测试商品8号', num=1, account='微信支付账户')
        salesreturn_num = salesreutrn.get_sales_return_ordernum()
        ReadData(self.param).write_data('sale_return_order', 'num14', salesreturn_num)
        self.assertTrue(salesreutrn.check_sales_return_success_status())

    # 直接退货
    def test_10016_direct_sales_return_case(self):
        """直接退货（其他账户）"""
        self.login_action()
        salesreutrn = SalesReturnBusiness(self.driver)
        if self.param == 0:
            salesreutrn.direct_return_action('李洲全-13888888811', name='测试商品8号', num=1, account='其他账户')
        else:
            salesreutrn.direct_return_action('李一-13777777771', name='测试商品8号', num=1, account='其他账户')
        salesreturn_num = salesreutrn.get_sales_return_ordernum()
        ReadData(self.param).write_data('sale_return_order', 'num15', salesreturn_num)
        self.assertTrue(salesreutrn.check_sales_return_success_status())

    # 直接退货
    def test_10017_direct_sales_return_case(self):
        """直接退货（继续退货）"""
        self.login_action()
        salesreutrn = SalesReturnBusiness(self.driver)
        if self.param == 0:
            salesreutrn.direct_return_action('李洲全-13888888811', normal=True, name='测试商品8号', num=1, is_continue=True)
        else:
            salesreutrn.direct_return_action('李一-13777777771', normal=True, name='测试商品8号', num=1, is_continue=True)
        salesreturn_num = salesreutrn.get_sales_return_ordernum()
        ReadData(self.param).write_data('sale_return_order', 'num16', salesreturn_num)
        self.assertTrue(salesreutrn.check_sales_return_success_status())

    # 直接退货
    def test_10018_direct_sales_return_case(self):
        """直接退货（改价）"""
        self.login_action()
        salesreutrn = SalesReturnBusiness(self.driver)
        if self.param == 0:
            salesreutrn.direct_return_action('李洲全-13888888811', name='测试商品8号', num=1, modify=1000)
        else:
            salesreutrn.direct_return_action('李一-13777777771', name='测试商品8号', num=1, modify=1000)
        salesreturn_num = salesreutrn.get_detail_return_ordernum()
        ReadData(self.param).write_data('sale_return_order', 'num17', salesreturn_num)
        total_money = salesreutrn.check_total_money()
        self.assertEqual(total_money, '￥1000.00')

    # 直接退货
    def test_10019_direct_sales_return_case(self):
        """直接退货（备注）"""
        self.login_action()
        salesreutrn = SalesReturnBusiness(self.driver)
        if self.param == 0:
            salesreutrn.direct_return_action('李洲全-13888888811', name='测试商品8号', num=1, remark='直接退货备注')
        else:
            salesreutrn.direct_return_action('李一-13777777771', name='测试商品8号', num=1, remark='直接退货备注')
        salesreturn_num = salesreutrn.get_detail_return_ordernum()
        ReadData(self.param).write_data('sale_return_order', 'num18', salesreturn_num)
        info = salesreutrn.check_remaks()
        self.assertEqual(info, '直接退货备注')

    # 直接退货
    def test_10020_direct_sales_return_case(self):
        """直接退货（支付宝账户）"""
        self.login_action()
        salesreutrn = SalesReturnBusiness(self.driver)
        if self.param == 0:
            salesreutrn.direct_return_action('李洲全-13888888811', name='测试商品8号', num=1, account='支付宝账户')
        else:
            salesreutrn.direct_return_action('李一-13777777771', name='测试商品8号', num=1, account='支付宝账户')
        salesreturn_num = salesreutrn.get_sales_return_ordernum()
        ReadData(self.param).write_data('sale_return_order', 'num13', salesreturn_num)
        self.assertTrue(salesreutrn.check_sales_return_success_status())
