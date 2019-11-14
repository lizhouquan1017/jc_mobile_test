# coding:utf-8
import logging
from time import sleep
from base.BaseOperation import BaseOperation
from base.BaseReadIni import ReadIni


class PurchaseBusiness(BaseOperation):

    def __init__(self, driver):
        super(PurchaseBusiness, self).__init__(driver)
        self.efg = ReadIni(file_name='purchase_page.ini')

    def pruchase_action(self, goodname1=None, goodname2=None, goodnum=None, supplier_name=None, price=None, info=None):
        """
        goodname: 商品名称
        goodnum: 采购商品数量
        price: 采购商品改价，修改价格
        supplier_name: 供应商名称
        :return:
        """
        self.enter_purchase_interface()
        self.choose_goods_action(name1=goodname1, name2=goodname2, num=goodnum)
        self.modfiy_price_action(price=price)
        self.choose_supplier(supplier_name=supplier_name)
        self.edit_remarks(info=info)
        self.define_storage_action()

    # 进入采购界面
    def enter_purchase_interface(self):
        logging.info(r'进入库存模块')
        self.click(self.efg.read_config('库存按钮'))
        logging.info(r'进入采购进货界面')
        self.click_text(self.efg.read_config('采购进货'))
        sleep(2)

    # 采购选购商品
    def choose_goods_action(self, name1=None, name2=None, num=None):
        if name1 is not None:
            logging.info(r'点击选择已有商品')
            self.click_text(self.efg.read_config('选择已有商品'))
            logging.info(r'选择商品')
            self.click_text(name1)
            logging.info(r'添加商品数量')
            for i in range(0, num):
                self.click(self.efg.read_config('加减按钮'))
            logging.info(r'确认选择商品')
            self.click(self.efg.read_config('商品确认按钮'))
            if name2 is not None:
                self.click_text(name2)
                logging.info(r'添加商品数量')
                logging.info(r'添加商品数量')
                for i in range(0, num):
                    self.click(self.efg.read_config('加减按钮'))
                logging.info(r'确认选择商品')
                self.click(self.efg.read_config('商品确认按钮'))
            sleep(2)
            logging.info(r'商品列表界面确认')
            self.click(self.efg.read_config('确认按钮'))
            sleep(2)

    # 选择供应商
    def choose_supplier(self, supplier_name=None):
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
    def modfiy_price_action(self, price=None):
        if price is not None:
            logging.info(r'改价操作')
            self.click(self.efg.read_config('采购改价'))
            sleep(3)
            logging.info(r'悬浮框改价按钮')
            self.click(self.efg.read_config('采购改价'))
            sleep(3)
            logging.info(r'输入修改价格')
            self.type(self.efg.read_config('悬浮框价格输入框'), price)
            logging.info(r'点击改价确认')
            self.click(self.efg.read_config('悬浮框确认'))
            sleep(3)
            logging.info(r'确认选择商品')
            self.click(self.efg.read_config('商品确认按钮'))
            sleep(3)
        else:
            pass

    # 填写备注
    def edit_remarks(self, info=None):
        if info is not None:
            logging.info('添加备注信息')
            self.type(self.efg.read_config('备注'), info)
            sleep(3)
        else:
            pass

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

    # 获取信息
    def get_purchase_information(self):
        flag = self.is_exists(self.efg.read_config('交易状态'))
        purchase_order_num = self.get_text(self.efg.read_config('采购单单号'))
        price = self.get_text(self.efg.read_config('订单总金额'))
        num = self.get_text(self.efg.read_config('采购数'))
        supplier_name = self.get_text(self.efg.read_config('供应商名称'))

        information_dict = {"status": flag, "purchase_order_num": purchase_order_num, "price": price, "num": num,
                            "supplier_name": supplier_name}
        return information_dict


    # # 获取采购成功状态
    # def check_transaction_success_status(self):
    #     logging.info(r'检查交易成功状态')
    #     flag = self.is_exists(self.efg.read_config('交易状态'))
    #     if flag:
    #         logging.info('验证状态成功！用例成功！')
    #         return True
    #     else:
    #         return False
    #
    # # 获取界面采购单单号
    # def get_purchase_order_num(self):
    #     logging.info(r'获取采购单单号')
    #     purchase_order_num = self.get_text(self.efg.read_config('采购单单号'))
    #     return purchase_order_num
    #
    # # 获取采购单订单价格
    # def get_order_price(self):
    #     logging.info(r'获取订单价格')
    #     price = self.get_text(self.efg.read_config('订单总金额'))
    #     return price
    #
    # # 获取采购总数
    # def get_purchase_num(self):
    #     logging.info(r'获取采购数量')
    #     num = self.get_text(self.efg.read_config('采购数'))
    #     return int(num)
    #
    # def check_supplier_is_exist(self, supplier_name):
    #     e = self.find_element_text(supplier_name)
    #     if e:
    #         return True
    #     else:
    #         return False
