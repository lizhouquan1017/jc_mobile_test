# coding:utf-8
import logging
import time
from base.BaseOperation import BaseOperation
from base.BaseReadIni import ReadIni
from time import sleep


class CashierView(BaseOperation):

    def __init__(self, driver):
        super(CashierView, self).__init__(driver)
        self.efg = ReadIni(file_name='cashierView.ini')

    def cashier_goods(self, num=None, flag=False, normal=False, good_value=None, good_discount=False, good_modify=False,
                      offer=True, order_discount=False, order_modify=False, order_value=None):
        self.enter_cash()
        self.choose_goods_action(num=num, flag=flag)
        self.goods_modify_discount(normal=normal, good_value=good_value, good_discount=good_discount,
                                   good_modify=good_modify)
        self.order_modify_discount(offer=offer, order_discount=order_discount, order_modify=order_modify,
                                   order_value=order_value)

    # 进入收银界面
    def enter_cash(self):
        logging.info(r'进入收银界面')
        self.click(self.efg.read_config('收银按钮'))
        time.sleep(2)
        logging.info(r'点击选择已有商品')
        self.click_text(self.efg.read_config('选择商品'))

    # 选择商品action
    def choose_goods_action(self, num=None, goodsname1='测试商品8号', goodsnam2='测试商品3号', flag=False):
        if flag is False:
            logging.info(r'点击选择非整数价格商品')
            self.click_text(goodsname1)
        elif flag is True:
            logging.info(r'点击选择整数价格商品')
            self.click_text(goodsnam2)
        logging.info(r'添加商品数量')
        for i in range(0, num):
            self.click(self.efg.read_config('加减按钮'))
        time.sleep(1)
        logging.info(r'确认选择商品')
        self.click(self.efg.read_config('商品确认按钮'))
        logging.info(r'商品列表界面确认')
        self.click(self.efg.read_config('商品列表确认按钮'))

    # 结账action
    def pay_bill_action(self):
        logging.info(r'现金支付')
        self.click_text(self.efg.read_config('收款类型'))
        logging.info('确认收银')
        self.click(self.efg.read_config('确认收款'))

    # 正常收银用例
    def normal_cashier_action(self, num):
        self.choose_goods_action(num)
        logging.info(r'去结账')
        self.click(self.efg.read_config('结账'))
        self.pay_bill_action()

    # 商品打折改价
    def goods_modify_discount(self, normal=False, good_value=None, good_discount=False, good_modify=False):
        if normal:
            logging.info('点击改价按钮')
            self.click(self.efg.read_config('改价按钮'))
            sleep(2)
            logging.info('点击改价')
            self.click(self.efg.read_config('改价按钮'))
            sleep(2)
            if good_modify:
                logging.info('点击改价tab')
                self.click_text('改价')
                logging.info('输入修改后的价格')
                self.type(self.efg.read_config('改价价格输入框'), good_value)
            elif good_discount:
                logging.info('输入折扣')
                self.type(self.efg.read_config('折扣输入框'), good_value)
            logging.info('点击确认')
            self.click(self.efg.read_config('改价确认按钮'))
            logging.info('点击商品确认')
            self.click(self.efg.read_config('商品确认按钮'))
        else:
            pass

    # 订单打折改价
    def order_modify_discount(self, offer=True, order_discount=False, order_modify=False, order_value=None):
        if offer:
            logging.info(r'去结账')
            self.click(self.efg.read_config('结账'))
            self.pay_bill_action()
        else:
            if order_discount:
                logging.info(r'去结账')
                self.click(self.efg.read_config('结账'))
                logging.info(r'点击整单优惠')
                self.click(self.efg.read_config('优惠框'))
                logging.info(r'滑动')
                self.element_swipe_up(30, self.efg.read_config('优惠选择'))
                logging.info(r'确认')
                self.click(self.efg.read_config('优惠确认'))
                logging.info(r'输入折扣')
                self.type(self.efg.read_config('折扣输入框'), order_value)
                self.pay_bill_action()
            if order_modify:
                logging.info(r'去结账')
                self.click(self.efg.read_config('结账'))
                logging.info(r'点击整单优惠')
                self.click(self.efg.read_config('优惠框'))
                logging.info(r'滑动')
                self.element_swipe_up(60, self.efg.read_config('优惠选择'))
                logging.info(r'确认')
                self.click(self.efg.read_config('优惠确认'))
                logging.info(r'输入改价后的价格')
                self.type(self.efg.read_config('改价输入框'), order_value)
                self.pay_bill_action()

    # 挂单成功后销售成功
    def hangup_order_cashier_action(self, num):
        self.choose_goods_action(num)
        logging.info(r'点击挂单按钮')
        self.click(self.efg.read_config('挂单按钮'))
        logging.info(r'进入挂单界面')
        self.click(self.efg.read_config('挂单界面'))
        logging.info(r'选择所挂的单据')
        self.click_text(self.efg.read_config('商品名称'))
        self.pay_bill_action()

    # 检查交易成功状态
    def check_transaction_success_status(self):
        logging.info(r'检查交易成功状态')
        flag = self.is_exists(self.efg.read_config('交易状态'))
        return flag

    # 获取交易价格
    def get_order_price(self):
        logging.info(r'获取订单金额')
        price = self.get_text(self.efg.read_config('实际收款金额'))
        return price

    # 获取销售单号
    def get_sales_order_num(self):
        logging.info(r'获取销售单单号')
        sales_order_num = self.get_text(self.efg.read_config('销售单单号'))
        return sales_order_num
