# coding:utf-8

import logging
from base.BaseOperation import BaseOperation
from base.BaseReadIni import ReadIni
from time import sleep


class PurchaseReturnBusiness(BaseOperation):

    def __init__(self, driver):
        super(PurchaseReturnBusiness, self).__init__(driver)
        self.efg = ReadIni(file_name='purchasereturn_page.ini')

    # 进入采购退货界面
    def enter_purchase_return(self):
        logging.info(r'进入库存界面')
        self.click(self.efg.read_config('库存按钮'))
        sleep(2)
        logging.info(r'点击进入采购退货界面')
        self.click_text(self.efg.read_config('采购退货按钮'))
        sleep(2)

    # 确认原单退货/直接退货
    def purchase_return_selection(self, flag=True):
        if flag is True:
            self.click_text('关联原单退货')
        if flag is False:
            self.click_text('直接退货')

    # 选择原单退货
    def purchase_order_selection(self):
        logging.info('选择原单')
        self.click(self.efg.read_config('原始单选择'))
        logging.info('点击筛选')
        self.click(self.efg.read_config('原单筛选按钮'))

    # 单据筛选
    def filter_order(self, keyword=None, settlement=None, supplier_name=None, returned=None, status=None):
        if keyword is not None:
            logging.info(r'输入单号')
            self.type(self.efg.read_config('关键字'), keyword)
        if settlement is not None:
            logging.info('输入开始时间')
            self.click(self.efg.read_config('结算方式'))
            self.click_text(settlement)
        if supplier_name is not None:
            logging.info('选择供应商')
            self.click(self.efg.read_config('供应商'))
            self.click_text(supplier_name)
        if returned is not None:
            logging.info('选择退货状态')
            self.click(self.efg.read_config('退货状态'))
            if returned is True:
                logging.info('选择有退货')
                self.element_swipe_up(30, self.efg.read_config('状态框'))
                self.click(self.efg.read_config('滑框确认'))
            elif returned is False:
                logging.info('选择无退货')
                self.element_swipe_up(60, self.efg.read_config('状态框'))
                self.click(self.efg.read_config('滑框确认'))
        if status is not None:
            logging.info('选择订单状态')
            self.click(self.efg.read_config('订单状态'))
            if status is True:
                logging.info('选择订单正常')
                self.element_swipe_up(30, self.efg.read_config('状态框'))
                self.click(self.efg.read_config('滑框确认'))
            elif status is False:
                logging.info('选择订单作废')
                self.element_swipe_up(60, self.efg.read_config('状态框'))
                self.click(self.efg.read_config('滑框确认'))
        else:
            pass
        logging.info(r'点击确认')
        self.click(self.efg.read_config('筛选确认'))

    # 原单账户选择
    def original_order_account_selection(self, name):
        self.click(self.efg.read_config('退款账户'))
        self.click_text(name)

    # 原单备注填写
    def original_order_remarks_edit(self, info):
        self.type(self.efg.read_config('备注信息'), info)

    # 直接退货选择供应商
    def direct_return_supplier_selection(self, supplier_name):
        self.click(self.efg.read_config('供应商'))
        self.click_text(supplier_name)

    # 直接退货账户选择
    def direct_return_account_selection(self, name):
        self.click(self.efg.read_config('直接退货退款账户'))
        self.click_text(name)

    # 直接退货备注填写
    def direct_return_remarks_edit(self, info):
        logging.info('填写备注信息')
        self.type(self.efg.read_config('直接退货备注'), info)

    # 直接退货选择商品
    def direct_return_goods_selection(self, name, num):
        logging.info('点击选择已有商品')
        self.click_text(self.efg.read_config('选择商品'))
        self.click_text(name)
        for i in range(0, num):
            self.click(self.efg.read_config('加减按钮'))
        logging.info('点击确认')
        self.click(self.efg.read_config('悬浮框商品确认按钮'))
        self.click((self.efg.read_config('确认退货')))

    # 选择退货商品
    def choose_return_goods(self, num):
        self.click(self.efg.read_config('采购单列表商品名称'))
        for i in range(0, num):
            self.click(self.efg.read_config('加减按钮'))
        logging.info('点击确认')
        self.click(self.efg.read_config('确认退货'))

    # 改价
    def modfiy_price_action(self, price):
        logging.info(r'改价操作')
        self.click(self.efg.read_config('改价按钮'))
        logging.info(r'悬浮框改价按钮')
        sleep(2)
        self.click(self.efg.read_config('改价按钮'))
        logging.info(r'输入修改价格')
        sleep(2)
        self.type(self.efg.read_config('改价输入框'), price)
        logging.info(r'点击改价确认')
        self.click(self.efg.read_config('弹框确认'))
        logging.info(r'确认选择商品')
        self.click(self.efg.read_config('悬浮框商品确认按钮'))

    # 确认退货
    def define_purchasereturn(self):
        logging.info(r'点击确认退货按钮')
        self.click(self.efg.read_config('确认退货'))

    # 查看详情
    def enter_detail_interface(self):
        logging.info('进入详情界面')
        self.click(self.efg.read_config('查看详情'))
        sleep(3)

    # 获取采购成功状态
    def check_purchase_return_success_status(self):
        logging.info(r'检查交易成功状态')
        flag = self.is_exists(self.efg.read_config('退货成功'))
        return flag

    # 获取采购退货单号
    def get_purchase_return_ordernum(self):
        logging.info(r'获取采购单单号')
        purchase_return_ordernum = self.get_text(self.efg.read_config('采购退货单号'))
        return purchase_return_ordernum

    # 检查结算方式
    def check_account_type(self):
        info = self.get_text(self.efg.read_config('检查结算方式'))
        return info

    # 检查退款金额
    def check_total_money(self):
        total = self.get_text(self.efg.read_config('退货金额'))
        return total

    # 检查备注信息
    def check_remaks(self):
        info = self.get_text(self.efg.read_config('详情备注'))
        return info

    # 原单退货
    def original_order_return_action(self, num, normal=False, keyword=None, account=None, remark=None, modify=None,
                                     is_continue=False):
        sleep(3)
        self.enter_purchase_return()
        sleep(2)
        self.purchase_return_selection(flag=True)
        sleep(2)
        self.purchase_order_selection()
        sleep(2)
        self.filter_order(keyword=keyword)
        sleep(2)
        self.choose_return_goods(num)
        if normal is True:
            self.define_purchasereturn()
        if modify is not None:
            self.modfiy_price_action(modify)
            self.define_purchasereturn()
            self.enter_detail_interface()
        if account is not None:
            self.original_order_account_selection(account)
            self.define_purchasereturn()
            self.enter_detail_interface()
        if remark is not None:
            self.original_order_remarks_edit(remark)
            self.define_purchasereturn()
            self.enter_detail_interface()
        if is_continue:
            self.click(self.efg.read_config('继续退货'))
            self.purchase_order_selection()
            self.filter_order(keyword=keyword)
            self.choose_return_goods(num)
            if modify is not None:
                self.modfiy_price_action(modify)
            if account is not None:
                self.original_order_account_selection(account)
            if remark is not None:
                self.original_order_remarks_edit(remark)
            self.define_purchasereturn()

    # 直接退货
    def direct_return_action(self, supplier_name, normal=False, name=None, num=None, account=None,
                             modify=None, remark=None, is_continue=False):
        sleep(2)
        self.enter_purchase_return()
        sleep(2)
        self.purchase_return_selection(flag=False)
        sleep(2)
        self.direct_return_goods_selection(name, num)
        sleep(2)
        self.direct_return_supplier_selection(supplier_name=supplier_name)
        sleep(2)
        if normal:
            self.define_purchasereturn()
        if account is not None:
            logging.info('选择账户')
            self.direct_return_account_selection(account)
            self.define_purchasereturn()
        if modify is not None:
            self.modfiy_price_action(modify)
            self.define_purchasereturn()
            self.enter_detail_interface()
        if remark is not None:
            self.direct_return_remarks_edit(remark)
            self.define_purchasereturn()
            self.enter_detail_interface()
        if is_continue:
            self.click(self.efg.read_config('继续退货'))
            self.purchase_return_selection(flag=False)
            self.direct_return_goods_selection(name, num)
            self.direct_return_supplier_selection(supplier_name=supplier_name)
            self.define_purchasereturn()
