# coding:utf-8
import logging
from base.BaseOperation import BaseOperation
from base.BaseReadIni import ReadIni
from time import sleep


class PurchaseReturnOrderView(BaseOperation):

    def __init__(self, driver):
        super(PurchaseReturnOrderView, self).__init__(driver)
        self.efg = ReadIni(file_name='purchasereturnorderView.ini')

    # 进入采购单界面
    def enter_puchas_return_eorder_interface(self):
        logging.info(r'进入库存模块')
        self.click(self.efg.read_config('库存按钮'))
        sleep(2)
        logging.info(r'进入采购退货单界面')
        self.click_text(self.efg.read_config('采购退货单界面'))
        sleep(2)

    # 单据筛选
    def filter_order(self, keyword=None, settlement=None, supplier_name=None, status=None):
        logging.info(r'点击筛选按钮')
        self.click(self.efg.read_config('筛选按钮'))
        if keyword is not None:
            logging.info(r'输入单号')
            self.type(self.efg.read_config('关键字输入框'), keyword)
        if settlement is not None:
            logging.info('输入开始时间')
            self.click(self.efg.read_config('选择结算方式'))
            self.click_text(settlement)
        if supplier_name is not None:
            logging.info('选择供应商')
            self.click(self.efg.read_config('选择供应商'))
            self.click_text(supplier_name)
        if status is not None:
            logging.info('选择订单状态')
            self.click(self.efg.read_config('选择状态栏'))
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
        self.click(self.efg.read_config('筛选界面确认按钮'))

    # 进入单据详情
    def enter_order_detail(self):
        logging.info('进入订单详情')
        self.click(self.efg.read_config('采购退货单列表商品名称'))
        sleep(2)

    # 对单据进行操作
    def operating_document_action(self, keyword=None, obsolete=False, copy=False):
        self.enter_order_detail()
        sleep(2)
        if obsolete is True:
            logging.info(r'作废单据')
            self.click(self.efg.read_config('采购退货单详情操作按钮'))
            logging.info(r'点击作废')
            self.click(self.efg.read_config('作废订单'))
            logging.info(r'点击确认')
            self.click(self.efg.read_config('弹框确认按钮'))
            sleep(2)
            logging.info(r'点击后退按钮')
            self.click(self.efg.read_config('回退按钮'))
            logging.info(r'')
            self.click(self.efg.read_config('筛选按钮'))
            logging.info(r'输入单号')
            self.type(self.efg.read_config('关键字输入框'), keyword)
            logging.info('选择订单状态')
            self.click(self.efg.read_config('选择状态栏'))
            logging.info('选择订单作废')
            self.element_swipe_up(60, self.efg.read_config('状态框'))
            self.click(self.efg.read_config('状态框确认'))
            logging.info('点击筛选确认')
            self.click(self.efg.read_config('筛选界面确认按钮'))
        if copy is True:
            logging.info(r'复制订单')
            self.click(self.efg.read_config('采购退货单详情操作按钮'))
            logging.info(r'点击复制订单')
            self.click(self.efg.read_config('复制订单'))
            logging.info(r'点击确认')
            self.click(self.efg.read_config('弹框确认按钮'))
            sleep(2)

    # 复制后续操作
    def copy_follow_operation(self, name, is_original=False):
        if is_original is False:
            logging.info(r'进入供应商选择界面')
            self.click(self.efg.read_config('选择供应商'))
            logging.info(r'选择供应商')
            self.click_text(name)
            logging.info(r'确认入库')
            self.click(self.efg.read_config('确认退货'))
        else:
            logging.info(r'确认入库')
            self.click(self.efg.read_config('确认退货'))

    # 获取采购退货成功状态
    def check_purchase_return_status(self):
        flag = self.is_exists(self.efg.read_config('采购退货成功'))
        return flag

    # 获取采购单退货生成的采购退货单单号
    def get_purchase_return_order_num(self):
        order_num = self.get_text(self.efg.read_config('采购退货单详情中采购退货单号'))
        return order_num

    # 采购退货单详情采购单单号
    def get_detail_ptuchase_order(self):
        order_num = self.get_text(self.efg.read_config('采购退货单详情中采购退货单号'))
        return order_num

    def get_detail_settlement_type(self):
        settlement = self.get_text(self.efg.read_config('采购退货单详情结算方式'))
        return settlement

    # 获取采购成功状态
    def check_transaction_success_status(self):
        logging.info(r'检查交易成功状态')
        flag = self.is_exists(self.efg.read_config('采购退货成功'))
        return flag

    # 检查作废是否成功
    def check_obsolete_status_(self):
        logging.info(r'检查成功状态')
        flag = self.is_exists(self.efg.read_config('采购退货单列表商品名称'))
        return flag

    # 采购退货单操作
    def purchase_return_order_action(self, keyword=None, settlement=None, supplier_name=None, status=None,
                                     copy=False, obsolete=False, is_original=False):
        self.enter_puchas_return_eorder_interface()
        self.filter_order(keyword=keyword, settlement=settlement, supplier_name=supplier_name, status=status)
        self.enter_order_detail()
        self.operating_document_action(copy=copy, obsolete=obsolete, keyword=keyword)
        if copy:
            self.copy_follow_operation(supplier_name, is_original=is_original)
