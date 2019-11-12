# coding:utf-8

import logging
from base.BaseOperation import BaseOperation
from base.BaseReadIni import ReadIni
from time import sleep


class SalesReturnBusiness(BaseOperation):

    def __init__(self, driver):
        super(SalesReturnBusiness, self).__init__(driver)
        self.efg = ReadIni(file_name='salereturn_page.ini')

    # 进入采购退货界面
    def enter_sales_return(self):
        logging.info(r'进入库存界面')
        self.click(self.efg.read_config('库存'))
        logging.info(r'点击进入销售退货界面')
        self.click_text(self.efg.read_config('销售退货按钮'))

    # 选择原单退货
    def sales_order_selection(self):
        logging.info('选择原单')
        self.click(self.efg.read_config('原始单选择'))
        logging.info('点击筛选')
        self.click(self.efg.read_config('原单筛选按钮'))

    # 单据筛选
    def filter_order(self, keyword=None, settlement=None, seller_name=None, returned=None, status=None):
        if keyword is not None:
            logging.info(r'输入单号')
            self.type(self.efg.read_config('关键字'), keyword)
        if settlement is not None:
            logging.info('输入开始时间')
            self.click(self.efg.read_config('结算方式'))
            self.click_text(settlement)
        if seller_name is not None:
            logging.info('选择销售员')
            self.click(self.efg.read_config('选择销售员'))
            self.click_text(seller_name)
        if returned is not None:
            logging.info('选择退货状态')
            self.click(self.efg.read_config('退货状态'))
            if returned is True:
                logging.info('选择有退货')
                self.element_swipe_up(30, self.efg.read_config('状态框'))
                self.click(self.efg.read_config('状态框确认'))
            elif returned is False:
                logging.info('选择无退货')
                self.element_swipe_up(60, self.efg.read_config('状态框'))
                self.click(self.efg.read_config('状态框确认'))
        if status is not None:
            logging.info('选择订单状态')
            self.click(self.efg.read_config('订单状态'))
            if status is True:
                logging.info('选择订单正常')
                self.element_swipe_up(30, self.efg.read_config('状态框'))
                self.click(self.efg.read_config('状态框确认'))
            elif status is False:
                logging.info('选择订单作废')
                self.element_swipe_up(60, self.efg.read_config('状态框'))
                self.click(self.efg.read_config('状态框确认'))
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

    # 直接退货选择销售员
    def direct_return_seller_selection(self, seller_name):
        self.click(self.efg.read_config('选择销售员'))
        self.click_text(seller_name)
        self.click(self.efg.read_config('确认退货'))

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
        self.click(self.efg.read_config('确认退货'))

    # 选择退货商品
    def choose_return_goods(self, good_num=None, good_name=None):
        self.click_text(good_name)
        for i in range(0, good_num):
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
        self.type(self.efg.read_config('改价输入框'), price)
        logging.info(r'点击改价确认')
        self.click(self.efg.read_config('弹框确认'))
        logging.info(r'确认选择商品')
        self.click(self.efg.read_config('悬浮框商品确认按钮'))

    # 确认退货
    def define_salesreturn(self):
        logging.info(r'点击确认退货按钮')
        self.click(self.efg.read_config('确认退货'))

    # 查看详情
    def enter_detail_interface(self):
        logging.info('进入详情界面')
        self.click(self.efg.read_config('查看详情'))

    # 获取销售成功状态
    def check_sales_return_success_status(self):
        logging.info(r'检查交易成功状态')
        flag = self.is_exists(self.efg.read_config('退货成功'))
        return flag

    # 获取销售退货单号
    def get_sales_return_ordernum(self):
        logging.info(r'获取销售退货单号')
        sales_return_ordernum = self.get_text(self.efg.read_config('销售退货单号'))
        return sales_return_ordernum

    def get_detail_return_ordernum(self):
        logging.info(r'获取销售退货单号')
        sales_return_ordernum = self.get_text(self.efg.read_config('详情销售退货单号'))
        return sales_return_ordernum

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
    def original_order_return_action(self, good_name=None, good_num=None, normal=False, keyword=None, account=None,
                                     remark=None, modify=None, is_continue=False):
        self.enter_sales_return()
        self.sales_order_selection()
        self.filter_order(keyword=keyword)
        self.choose_return_goods(good_name=good_name, good_num=good_num)
        if normal is True:
            self.define_salesreturn()
        if modify is not None:
            self.modfiy_price_action(modify)
            self.define_salesreturn()
            self.enter_detail_interface()
        if account is not None:
            self.original_order_account_selection(account)
            self.define_salesreturn()
            self.enter_detail_interface()
        if remark is not None:
            self.original_order_remarks_edit(remark)
            self.define_salesreturn()
            self.enter_detail_interface()
        if is_continue:
            self.click(self.efg.read_config('继续退货'))
            self.sales_order_selection()
            self.filter_order(keyword=keyword)
            self.choose_return_goods(good_name=good_name, good_num=good_num)
            if modify is not None:
                self.modfiy_price_action(modify)
            if account is not None:
                self.original_order_account_selection(account)
            if remark is not None:
                self.original_order_remarks_edit(remark)
            self.define_salesreturn()

    # 直接退货
    def direct_return_action(self, seller_name, normal=False, name=None, num=None, account=None,
                             modify=None, remark=None, is_continue=False):
        self.enter_sales_return()
        self.click_text('直接退货')
        self.direct_return_goods_selection(name, num)
        self.direct_return_seller_selection(seller_name=seller_name)
        if normal:
            self.define_salesreturn()
        if account is not None:
            logging.info('选择账户')
            self.direct_return_account_selection(account)
            self.define_salesreturn()
        if modify is not None:
            self.modfiy_price_action(modify)
            self.define_salesreturn()
            self.enter_detail_interface()
        if remark is not None:
            self.direct_return_remarks_edit(remark)
            self.define_salesreturn()
            self.enter_detail_interface()
        if is_continue:
            self.click(self.efg.read_config('继续退货'))
            self.click_text('直接退货')
            self.direct_return_goods_selection(name, num)
            self.direct_return_seller_selection(seller_name=seller_name)
            self.define_salesreturn()






