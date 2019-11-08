# coding:utf-8
import logging
from time import sleep
from base.BaseOperation import BaseOperation
from base.BaseReadIni import ReadIni


class PurchaseView(BaseOperation):

    def __init__(self, driver):
        super(PurchaseView, self).__init__(driver)
        self.efg = ReadIni(file_name='purchaseView.ini')

    # 进入采购界面
    def enter_purchase_interface(self):
        logging.info(r'进入库存模块')
        self.click(self.efg.read_config('库存按钮'))
        logging.info(r'进入采购进货界面')
        self.click_text(self.efg.read_config('采购进货'))
        sleep(2)

    # 新建供应商
    def add_supplier(self, name):
        self.enter_purchase_interface()
        logging.info('点击进入供应商界面')
        self.click(self.efg.read_config('供应商选择'))
        logging.info('点击新增按钮')
        self.click(self.efg.read_config('供应商新增'))
        sleep(2)
        logging.info('输入供应商名称')
        self.type(self.efg.read_config('供应商编辑输入框'), name)
        logging.info('点击确认')
        self.click(self.efg.read_config('悬浮框确认'))
        sleep(2)

    # 采购选购商品
    def choose_goods_action(self, name, num):
        logging.info(r'点击选择已有商品')
        self.click_text(self.efg.read_config('选择已有商品'))
        logging.info(r'选择商品')
        self.click_text(name)
        logging.info(r'添加商品数量')
        for i in range(0, num):
            self.click(self.efg.read_config('加减按钮'))
        logging.info(r'确认选择商品')
        self.click(self.efg.read_config('商品确认按钮'))
        sleep(3)
        logging.info(r'商品列表界面确认')
        self.click(self.efg.read_config('确认按钮'))
        sleep(3)

    # 选择供应商
    def choose_supplier(self, supplier_name):
        logging.info(r'进入供应商选择界面')
        self.click(self.efg.read_config('供应商选择'))
        logging.info(r'选择供应商')
        self.click_text(supplier_name)
        sleep(3)

    # 确认入库
    def define_storage_action(self):
        logging.info(r'确认入库')
        self.click(self.efg.read_config('确认按钮'))
        sleep(3)

    # 改价
    def modfiy_price_action(self, value):
        logging.info(r'改价操作')
        self.click(self.efg.read_config('采购改价'))
        sleep(3)
        logging.info(r'悬浮框改价按钮')
        self.click(self.efg.read_config('采购改价'))
        sleep(3)
        logging.info(r'输入修改价格')
        self.type(self.efg.read_config('悬浮框价格输入框'), value)
        logging.info(r'点击改价确认')
        self.click(self.efg.read_config('悬浮框确认'))
        sleep(3)
        logging.info(r'确认选择商品')
        self.click(self.efg.read_config('商品确认按钮'))
        sleep(3)

    # 填写备注
    def edit_remarks(self, info):
        logging.info('添加备注信息')
        self.type(self.efg.read_config('备注'), info)
        sleep(3)

    # 获取采购成功状态
    def check_transaction_success_status(self):
        logging.info(r'检查交易成功状态')
        flag = self.is_exists(self.efg.read_config('交易状态'))
        if flag:
            logging.info('验证状态成功！用例成功！')
            return True
        else:
            return False

    # 获取界面采购单单号
    def get_purchase_order_num(self):
        logging.info(r'获取采购单单号')
        purchase_order_num = self.get_text(self.efg.read_config('采购单单号'))
        return purchase_order_num

    # 获取采购单订单价格
    def get_order_price(self):
        logging.info(r'获取订单价格')
        price = self.get_text(self.efg.read_config('订单总金额'))
        return price

    # 获取采购总数
    def get_purchase_num(self):
        logging.info(r'获取采购数量')
        num = self.get_text(self.efg.read_config('采购数'))
        return int(num)

    def check_supplier_is_exist(self, supplier_name):
        e = self.find_element_text(supplier_name)
        if e:
            return True
        else:
            return False