# coding:utf-8
import logging
from base.BaseOperation import BaseOperation
from base.BaseReadIni import ReadIni
from time import sleep


class PurchaseOrderBusiness(BaseOperation):

    def __init__(self, driver):
        super(PurchaseOrderBusiness, self).__init__(driver)
        self.efg = ReadIni(file_name='purchaseorder_page.ini')

    # 进入采购单界面
    def enter_puchaseorder_interface(self):
        logging.info(r'进入库存模块')
        self.click(self.efg.read_config('库存按钮'))
        logging.info(r'进入采购单界面')
        self.click_text(self.efg.read_config('采购单界面'))

    # 单据筛选
    def filter_order(self, keyword=None, settlement=None, supplier_name=None, returned=None, status=None):
        logging.info(r'点击筛选按钮')
        self.click(self.efg.read_config('采购单列表筛选按钮'))
        if keyword is not None:
            logging.info(r'输入单号')
            self.type(self.efg.read_config('关键字输入框'), keyword)
        if settlement is not None:
            logging.info('结算方式')
            self.click(self.efg.read_config('选择结算方式'))
            self.click_text(settlement)
        if supplier_name is not None:
            logging.info('选择供应商')
            self.click(self.efg.read_config('选择供应商'))
            self.click_text(supplier_name)
        if returned is not None:
            logging.info('选择退货状态')
            self.click(self.efg.read_config('有无退货'))
            if returned is True:
                logging.info('选择有退货')
                self.element_swipe_up(30, self.efg.read_config('状态滑动框'))
                self.click(self.efg.read_config('滑动框确认'))
            elif returned is False:
                logging.info('选择无退货')
                self.element_swipe_up(60, self.efg.read_config('状态滑动框'))
                self.click(self.efg.read_config('滑动框确认'))
        if status is not None:
            logging.info('选择订单状态')
            self.click(self.efg.read_config('状态选择'))
            if status is True:
                logging.info('选择订单正常')
                self.element_swipe_up(30, self.efg.read_config('状态滑动框'))
                self.click(self.efg.read_config('滑动框确认'))
            elif status is False:
                logging.info('选择订单作废')
                self.element_swipe_up(60, self.efg.read_config('状态滑动框'))
                self.click(self.efg.read_config('滑动框确认'))
        else:
            pass
        logging.info(r'点击确认')
        self.click(self.efg.read_config('筛选界面确认按钮'))

    # 进入单据详情
    def enter_order_detail(self):
        logging.info('进入订单详情')
        self.click(self.efg.read_config('采购单列表商品名称'))

    # 对单据进行操作
    def operating_document_action(self, obsolete=False, copy=False, keyword=None):
        self.enter_order_detail()
        if obsolete is True:
            logging.info(r'作废单据')
            self.click(self.efg.read_config('采购单详情操作按钮'))
            logging.info(r'点击作废')
            self.click(self.efg.read_config('作废订单'))
            logging.info(r'点击确认')
            self.click(self.efg.read_config('弹框确认按钮'))
            sleep(2)
            logging.info(r'点击后退按钮')
            self.click(self.efg.read_config('回退按钮'))
            logging.info(r'')
            self.click(self.efg.read_config('采购单列表筛选按钮'))
            logging.info(r'输入单号')
            self.type(self.efg.read_config('关键字输入框'), keyword)
            logging.info('选择订单状态')
            self.click(self.efg.read_config('状态选择'))
            logging.info('选择订单作废')
            self.element_swipe_up(60, self.efg.read_config('状态滑动框'))
            self.click(self.efg.read_config('滑动框确认'))
            logging.info('点击筛选确认')
            self.click(self.efg.read_config('筛选界面确认按钮'))
        if copy is True:
            logging.info(r'复制订单')
            self.click(self.efg.read_config('采购单详情操作按钮'))
            logging.info(r'点击复制订单')
            self.click(self.efg.read_config('复制订单'))
            logging.info(r'点击确认')
            self.click(self.efg.read_config('弹框确认按钮'))

    # 复制后续操作
    def copy_follow_operation(self, name):
        logging.info(r'进入供应商选择界面')
        self.click(self.efg.read_config('供应商选择'))
        logging.info(r'选择供应商')
        self.click_text(name)
        logging.info(r'确认入库')
        self.click(self.efg.read_config('退货确认'))

    # 退货
    def purchase_order_return(self, modify=False, price=None):
        logging.info('进入订单详情')
        self.click(self.efg.read_config('采购单列表商品名称'))
        logging.info('点击退货按钮')
        self.click(self.efg.read_config('采购单详情退货按钮'))
        if modify is True:
            logging.info('点击改价按钮')
            self.click(self.efg.read_config('改价'))
            logging.info('输入修改后价格')
            self.type(self.efg.read_config('改价输入'), price)
            self.click(self.efg.read_config('弹框确认按钮'))
        logging.info('点击添加商品')
        self.click(self.efg.read_config('加按钮'))
        self.click(self.efg.read_config('退货确认'))
        self.click(self.efg.read_config('退货确认'))

    # 获取采购退货成功状态
    def get_purchase_return_status(self):
        text = self.get_text(self.efg.read_config('采购退货成功'))
        if text == '采购退货成功':
            return True

    # 获取采购单退货生成的采购退货单单号
    def get_purchase_return_order_num(self):
        order_num = self.get_text(self.efg.read_config('采购退货单单号'))
        return order_num

    # 获取原始采购单单号
    def get_purchase_order_num(self):
        order_num = self.get_text(self.efg.read_config('原始采购单单号'))
        return order_num

    # 获取退货数量
    def get_return_num(self):
        num_list = self.get_text(self.efg.read_config('退货数量'))
        num = num_list[0]
        return int(num)

    # 采购单详情采购单单号
    def get_detail_ptuchase_order(self):
        order_num = self.get_text(self.efg.read_config('采购单详情中采购单号'))
        return order_num

    # 检查作废是否成功
    def check_obsolete_status(self):
        logging.info(r'检查成功状态')
        flag = self.is_exists(self.efg.read_config('采购单列表商品名称'))
        return flag

    # 获取采购成功状态
    def check_transaction_success_status(self):
        logging.info(r'检查交易成功状态')
        text = self.get_text(self.efg.read_config('采购退货成功'))
        if text == r'采购单录入成功':
            return True
        else:
            return False
