# coding:utf-8
import logging
from time import sleep
from base.BaseOperation import BaseOperation
from base.BaseReadIni import ReadIni


class SalesOrderView(BaseOperation):

    def __init__(self, driver):
        super(SalesOrderView, self).__init__(driver)
        self.efg = ReadIni(file_name='salesorderView.ini')

    # 进入销售单界面
    def enter_sales_order_action(self):
        logging.info(r'点击库存按钮')
        self.click(self.efg.read_config('库存按钮'))
        logging.info(r'点击进入销售单界面')
        self.click_text(self.efg.read_config('销售单按钮'))

    # 进入销售单详情
    def enter_sales_order_detail(self):
        logging.info('进入销售单详情')
        self.click(self.efg.read_config('商品列表名称'))

    # 单据筛选
    def filter_order(self, keyword=None, settlement=None, seller_name=None, cashier_name=None,
                     returned=None, status=None):
        logging.info(r'点击筛选按钮')
        self.click(self.efg.read_config('筛选按钮'))
        if keyword is not None:
            logging.info(r'输入单号')
            self.type(self.efg.read_config('关键字'), keyword)
        if settlement is not None:
            logging.info('结算方式')
            self.click(self.efg.read_config('结算方式选择'))
            self.click_text(settlement)
        if seller_name is not None:
            logging.info('选择销售员')
            self.click(self.efg.read_config('销售员选择'))
            self.click_text(seller_name)
        if cashier_name is not None:
            logging.info('选择收银员')
            self.click(self.efg.read_config('收营员选择'))
            self.click_text(cashier_name)
        if returned is not None:
            logging.info('选择退货状态')
            self.click(self.efg.read_config('有无退货选择'))
            if returned is True:
                logging.info('选择有退货')
                self.element_swipe_up(30, self.efg.read_config('状态框'))
                self.click(self.efg.read_config('状态框确认'))
            elif returned is False:
                logging.info('选择无退货')
                self.element_swipe_up(60, self.efg.read_config('状态框'))
                self.click(self.efg.read_config('状态框确认'))
        if status is not None:
            self.swipe_up(2000)
            logging.info('选择订单状态')
            self.click(self.efg.read_config('状态选择'))
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
        self.click(self.efg.read_config('筛选确认按钮'))
        self.enter_sales_order_detail()

    # 结账action
    def pay_bill_action(self):
        logging.info(r'去结账')
        self.click(self.efg.read_config('结账'))
        logging.info(r'现金支付')
        self.click_text(self.efg.read_config('收款类型'))
        logging.info('确认收银')
        self.click(self.efg.read_config('确认收款'))

    # 对单据进行操作
    def operating_document_action(self, obsolete=False, copy=False, keyword=None):
        if obsolete is True:
            logging.info(r'作废单据')
            self.click(self.efg.read_config('销售单详情操作按钮'))
            logging.info(r'点击作废')
            self.click(self.efg.read_config('作废按钮'))
            logging.info(r'点击确认')
            self.click(self.efg.read_config('弹框确认'))
            logging.info(r'点击回退')
            self.click(self.efg.read_config('回退按钮'))
            logging.info(r'点击筛选')
            self.filter_order(keyword=keyword, status=False)
            self.click(self.efg.read_config('回退按钮'))
        if copy is True:
            logging.info(r'复制订单')
            self.click(self.efg.read_config('销售单详情操作按钮'))
            logging.info(r'点击复制订单')
            self.click(self.efg.read_config('复制按钮'))
            logging.info(r'点击确认')
            self.click(self.efg.read_config('弹框确认'))
            self.pay_bill_action()

    # 退货
    def sales_order_return(self, modify=False, price=None):
        logging.info('点击退货按钮')
        self.click(self.efg.read_config('销售单退货按钮'))
        if modify is True:
            logging.info('点击改价按钮')
            self.click(self.efg.read_config('改价'))
            logging.info('输入修改后价格')
            self.type(self.efg.read_config('改价输入框'), price)
            self.click(self.efg.read_config('弹框确认'))
        logging.info('点击添加商品')
        self.click(self.efg.read_config('加按钮'))
        self.click(self.efg.read_config('确认退货'))
        self.click(self.efg.read_config('确认退货'))

    # 检查交易成功状态
    def check_transaction_success_status(self):
        logging.info(r'检查交易成功状态')
        text = self.get_text(self.efg.read_config('交易状态'))
        if text == r'交易成功':
            return True

    # 获取退款总金额
    def check_return_total_money(self):
        money = self.get_text(self.efg.read_config('退款金额'))
        return money

    # 获取交易价格
    def get_order_price(self):
        logging.info(r'获取订单金额')
        price = self.get_text(self.efg.read_config('实际收款金额'))
        return price

    # 获取销售单号
    def get_sales_order_num(self):
        logging.info(r'获取单号')
        sales_order_num = self.get_text(self.efg.read_config('销售单单号'))
        return sales_order_num

    # 获取销售退货单单号
    def get_sales_return_order_num(self):
        logging.info(r'获取单号')
        sales_return_order_num = self.get_text(self.efg.read_config('销售退货单单号'))
        return sales_return_order_num

    # 判断单据是否作废
    def check_sales_order_status(self):
        flag = self.is_exists(self.efg.read_config('商品列表名称'))
        return flag

    # 销售单测试用例
    def sales_order_action(self, keyword=None, settlement=None, seller_name=None, cashier_name=None,
                           returned=None, status=None, obsolete=False, copy=False, modify=False, price=None,
                           sales_return=False):
        self.enter_sales_order_action()
        self.filter_order(keyword=keyword, settlement=settlement, seller_name=seller_name, cashier_name=cashier_name,
                          returned=returned, status=status)
        if copy or obsolete:
            self.operating_document_action(obsolete=obsolete, copy=copy, keyword=keyword)
        if sales_return:
            self.sales_order_return(modify=modify, price=price)
