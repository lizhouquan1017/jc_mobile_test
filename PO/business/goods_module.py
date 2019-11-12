# coding:utf-8

import logging
from base.BaseOperation import BaseOperation
from base.BaseReadIni import ReadIni
from time import sleep


class GoodsBusiness(BaseOperation):

    def __init__(self, driver):
        super(GoodsBusiness, self).__init__(driver)
        self.efg = ReadIni(file_name='goods_page.ini')

    # 进入商品管理界面
    def enter_goods_list(self):
        sleep(2)
        logging.info('进入商品管理界面')
        self.click_text(self.efg.read_config('商品管理'))
        sleep(2)

    # 选择类目
    def choose_category(self):
        logging.info('点击新增商品')
        self.click(self.efg.read_config('新增按钮'))
        logging.info('选择商品类目')
        self.click(self.efg.read_config('商品类目'))
        sleep(2)
        logging.info('选择男装')
        self.click_text(self.efg.read_config('类目选择1'))
        sleep(2)
        logging.info('选择上装')
        self.click_text(self.efg.read_config('类目选择2'))
        sleep(2)
        logging.info('选择男士T恤')
        self.click_text(self.efg.read_config('类目选择3'))
        sleep(2)

    # 新增商品操作
    def type_must_field(self, goodsname, costprice, saleprice, color_value, size_value, *args):
        """
        :param goodsname:
        :param costprice:
        :param saleprice:
        :param color_value:
        :param size_value:
        :param args:
        :return:
        """
        self.choose_category()
        self.type(self.efg.read_config('商品名称'), goodsname)
        sleep(1)
        logging.info('输入成本价')
        self.type(self.efg.read_config('采购价格'), costprice)
        sleep(1)
        logging.info('输入零售价')
        self.type(self.efg.read_config('销售价格'), saleprice)
        sleep(1)
        logging.info('点击颜色')
        self.click_text(self.efg.read_config('颜色选择'))
        sleep(1)
        logging.info('选择颜色')
        self.click_text(color_value)
        sleep(1)
        logging.info('点击确认')
        self.click(self.efg.read_config('确认选择'))
        sleep(1)
        logging.info('点击尺码')
        self.click_text(self.efg.read_config('尺码选择'))
        sleep(1)
        logging.info('选择尺码')
        self.click_text(size_value)
        sleep(1)
        logging.info('点击确认')
        self.click(self.efg.read_config('确认选择'))
        sleep(1)
        if args:
            if len(args) == 2:
                logging.info('添加商品货号')
                self.type(self.efg.read_config('商品货号输入'), args[0])
                sleep(1)
                logging.info('滑动到自定义分类界面')
                self.swipe_up(500)
                sleep(1)
                # self.swipe(self.新增商品界面, 'up', 0, -1)
                logging.info('输入初始库存')
                self.click(self.efg.read_config('初始库存输入'))
                sleep(1)
                logging.info('输入库存数')
                for i in range(0, args[1]):
                    self.click(self.efg.read_config('添加库存数按钮'))
                    sleep(1)
                logging.info('点击确认')
                self.click(self.efg.read_config('确认选择'))
                sleep(1)
            elif len(args) == 3:
                logging.info('添加商品货号')
                self.type(self.efg.read_config('商品货号输入'), args[0])
                sleep(1)
                logging.info('滑动到自定义分类界面')
                self.swipe_up(500)
                sleep(1)
                # self.swipe(self.新增商品界面, 'up', 0, -1)
                logging.info('输入初始库存')
                self.click(self.efg.read_config('初始库存输入'))
                sleep(1)
                logging.info('输入库存数')
                for i in range(0, args[1]):
                    self.click(self.efg.read_config('添加库存数按钮'))
                    sleep(1)
                logging.info('点击确认')
                self.click(self.efg.read_config('确认选择'))
                sleep(1)
                logging.info('商品条码输入')
                self.type(self.efg.read_config('商品条码输入'), args[2])
                sleep(1)
            elif len(args) == 4:
                logging.info('添加商品货号')
                self.type(self.efg.read_config('商品货号输入'), args[0])
                sleep(1)
                logging.info('滑动到自定义分类界面')
                # self.swipe(self.efg.read_config('新增商品界面'), 'up', 0, -1)
                self.swipe_up(500)
                sleep(1)
                logging.info('输入初始库存')
                self.click(self.efg.read_config('初始库存输入'))
                sleep(1)
                logging.info('输入库存数')
                for i in range(0, args[1]):
                    self.click(self.efg.read_config('添加库存数按钮'))
                    sleep(1)
                logging.info('点击确认')
                self.click(self.efg.read_config('确认选择'))
                sleep(1)
                logging.info('商品条码输入')
                self.type(self.efg.read_config('商品条码输入'), args[2])
                sleep(1)
                logging.info('输入商品备注')
                self.type(self.efg.read_config('商品备注'), args[3])
                sleep(1)

            # elif len(args) == 11:
            #     logging.info('添加商品货号')
            #     self.type(self.efg.read_config('商品货号输入'), args[0])
            #     logging.info('滑动到添加库存界面')
            #     self.swipe_up(500)
            #     # self.swipe(self.新增商品界面, 'up', 0, -1)
            #     logging.info('输入初始库存')
            #     self.click(self.efg.read_config('初始库存输入'))
            #     logging.info('输入库存数')
            #     for i in range(0, args[1]):
            #         self.click(self.efg.read_config('添加库存数按钮'))
            #     logging.info('点击确认')
            #     self.click(self.efg.read_config('确认选择'))
            #     logging.info('商品条码输入')
            #     self.type(self.efg.read_config('商品条码输入'), args[2])
            #     logging.info('输入商品备注')
            #     self.type(self.efg.read_config('商品备注'), args[3])
            #     logging.info('输入库存上限')
            #     self.type(self.efg.read_config('库存上限'), args[4])
            #     logging.info('输入库存下限')
            #     self.type(self.efg.read_config('库存下限'), args[5])
            #     logging.info('滑动到其他参数界面')
            #     self.swipe_up(500)
            #     # self.swipe(self.新增商品界面, 'up', 0, -0.5)
            #     logging.info('输入单位')
            #     self.type_other_parameter('请输入单位信息', args[6])
            #     logging.info('输入成分')
            #     self.type_other_parameter('请输入成分信息', args[7])
            #     logging.info('输入季节')
            #     self.type_other_parameter('请输入季节信息', args[8])
            #     logging.info('输入款式')
            #     self.type_other_parameter('请输入款式信息', args[9])
            #     logging.info('输入品牌')
            #     self.type_other_parameter('请输入品牌信息', args[10])
            # else:
            #     logging.info('添加商品货号')
            #     self.type(self.efg.read_config('商品货号输入'), args[0])
        else:
            pass

    # 确认添加
    def confirm_add_goods(self):
        logging.info('点击保存')
        self.click(self.efg.read_config('保存按钮'))

    # 获取商品货号
    def get_goods_num(self):
        logging.info('获取商品货号')
        goods_num = self.get_text(self.efg.read_config('商品货号'))
        logging.info("商品货号：%s" % goods_num)
        list1 = goods_num.split('：')
        return list1[1]

    # 获取商品条码
    def get_goods_barcode(self):
        logging.info('获取商品条码')
        goods_barcode = self.get_text(self.efg.read_config('商品条码'))
        logging.info("商品条码：%s" % goods_barcode)
        list1 = goods_barcode.split('：')
        return list1[1]

    # 获取其他参数
    def get_other_parameter(self):
        other_parameters = self.get_text(self.efg.read_config('其他参数值'))
        return other_parameters

    # 获取单品货号
    def get_sku_barcode(self):
        logging.info('获取单品货号')
        sku_num = self.get_text(self.efg.read_config('单品货号'))
        logging.info("单品货号：%s" % sku_num)
        return sku_num

    # # 获取库存信息
    # def get_stock_num(self):
    #     logging.info('点击库存信息')
    #     tab_name = self.get_elements(self.库存信息1, self.库存信息2, self.库存信息3, self.库存信息4)
    #     for i in range(0, len(tab_name)):
    #         if tab_name[i].get_text() == '库存信息':
    #             tab_name[i].click()
    #     stock_num = self.get_text(self.详细信息库存数)
    #     return stock_num
    #
    # # 输入其他参数
    # def type_other_parameter(self, value, *args):
    #     logging.info('输入其他参数')
    #     tab_name = self.get_elements(self.其他参数1, self.其他参数2, self.其他参数3)
    #     for i in range(0, len(tab_name)):
    #         if tab_name[i].get_text() == value:
    #             tab_name[i].set_text(args)

    # 查看商品详情
    def get_goods_details(self):
        logging.info('查看商品详情')
        self.click(self.efg.read_config('查看商品详情'))

    # 继续添加商品
    def go_on_add_goods(self):
        logging.info('继续添加商品')
        self.click(self.efg.read_config('继续添加商品'))

    # 返回首页
    def go_home(self):
        logging.info('返回首页')
        self.click(self.efg.read_config('返回首页'))

    # 商品下架操作
    def goods_obtained_action(self, name):
        logging.info('点击商品')
        self.click_text(name)
        logging.info('点击下架')
        self.click(self.efg.read_config('上下架按钮'))
        logging.info('点击弹框确认')
        self.click(self.efg.read_config('弹框确认'))

    # 商品上架操作
    def goods_shelf_action(self, name):
        logging.info('点击筛选按钮')
        self.click(self.efg.read_config('筛选按钮'))
        logging.info('点击取消已上架查询')
        self.click(self.efg.read_config('筛选上架'))
        logging.info('点击选择已下架查询')
        self.click(self.efg.read_config('筛选下架'))
        logging.info('点击确认查询')
        self.click(self.efg.read_config('筛选确认'))
        logging.info('点击商品')
        self.click_text(name)
        logging.info('点击上架')
        self.click(self.efg.read_config('上下架按钮'))
        logging.info('点击确认')
        self.click(self.efg.read_config('弹框确认'))
        logging.info('点击back按钮')
        self.click(self.efg.read_config('回退按钮'))
        logging.info('点击筛选按钮')
        self.click(self.efg.read_config('筛选按钮'))
        logging.info('点击取消已下架查询')
        self.click(self.efg.read_config('筛选下架'))
        logging.info('点击选择已上架查询')
        self.click(self.efg.read_config('筛选上架'))
        logging.info('点击确认查询')
        self.click(self.efg.read_config('筛选确认'))

    # 删除操作
    def goods_delete_action(self):
        logging.info('点击商品')
        self.click_text(self.efg.read_config('商品列表名称'))
        logging.info('点击详情页面操作按钮')
        self.click(self.efg.read_config('商品详情页面操作按钮'))
        logging.info('点击删除按钮')
        self.click(self.efg.read_config('删除商品'))
        logging.info('点击确认')
        self.click(self.efg.read_config('弹框确认'))

    # 检查新增是否成功
    def check_success_status(self):
        status = self.get_text(self.efg.read_config('添加成功'))
        return status

    # 检查下架状态
    def check_obtained_status(self):
        status = self.get_text(self.efg.read_config('下架状态'))
        return status

    # 列表编辑操作
    def list_edit_action(self, value):
        logging.info('点击列表操作')
        self.click(self.efg.read_config('列表操作按钮'))
        sleep(2)
        logging.info('点击编辑')
        self.click(self.efg.read_config('列表编辑按钮'))
        sleep(2)
        logging.info('修改商品名称')
        self.type(self.efg.read_config('商品名称'), value)
        sleep(2)
        logging.info('点击保存')
        self.click(self.efg.read_config('保存按钮'))

    # 详情编辑操作
    def details_edit_action(self, value):
        logging.info('点击商品详情')
        self.click(self.efg.read_config('商品名称'))
        sleep(2)
        logging.info('点击编辑')
        self.click(self.efg.read_config('详情编辑按钮'))
        sleep(1)
        logging.info('修改商品名称')
        self.type(self.efg.read_config('商品名称'), value)
        sleep(1)
        logging.info('点击保存')
        self.click(self.efg.read_config('保存按钮'))

    # 新增规则组
    def add_rule_group(self, name, group_name):
        self.choose_category()
        logging.info('点击颜色或者尺码')
        self.click_text(name)
        logging.info('点击添加属性规则组')
        self.click(self.efg.read_config('属性规则组添加'))
        logging.info('输入规则组名称')
        self.type(self.efg.read_config('规则组输入框'), group_name)
        logging.info('点击确认')
        self.click(self.efg.read_config('弹框确认'))

    # 编辑规则组
    def edit_rule_group(self, name, group_name):
        self.choose_category()
        logging.info('点击颜色或者尺码')
        self.click_text(name)
        logging.info('点击编辑规则组名称')
        self.click(self.efg.read_config('规则组编辑'))
        logging.info('输入修改后规则组名称')
        self.type(self.efg.read_config('规则组输入框'), group_name)
        logging.info('点击确认')
        self.click(self.efg.read_config('弹框确认'))

    # 编辑规则组
    def delete_rule_group(self, name):
        self.choose_category()
        logging.info('点击颜色或者尺码')
        self.click_text(name)
        logging.info('点击删除按钮')
        self.click(self.efg.read_config('规则组删除'))
        logging.info('点击确认')
        self.click(self.efg.read_config('弹框确认'))

    # 新增自定义分类
    def add_custom_classification(self, name):
        logging.info('点击新增商品')
        self.click(self.efg.read_config('新增按钮'))
        logging.info('滑动到自定义分类界面')
        self.swipe_up(500)
        # self.swipe(self.新增商品界面, 'up', 0, -0.8)
        logging.info('点击自定义分类')
        self.click(self.efg.read_config('自定义分类'))
        logging.info('点击新增')
        self.click(self.efg.read_config('操作按钮'))
        logging.info('输入自定义分类名称')
        self.type(self.efg.read_config('自定义分类名称'), name)
        logging.info('点击确认')
        self.click(self.efg.read_config('确认选择'))

    # # 编辑自定义分类
    # def edit_custom_classification(self, name):
    #     logging.info('点击新增商品')
    #     self.click(self.新增按钮)
    #     logging.info('滑动到自定义分类界面')
    #     self.swipe(self.新增商品界面, 'up', 0, -0.8)
    #     logging.info('点击自定义分类')
    #     self.click(self.自定义分类)
    #     logging.info('向左滑动已有分类')
    #     self.swipe(self.自定义分类滑动, 'left', -0.5, 0)
    #     logging.info('点击编辑')
    #     self.click(self.自定义类目编辑)
    #     logging.info('输入自定义分类名称')
    #     self.type(self.自定义分类名称, name)
    #     logging.info('点击确认')
    #     self.click(self.确认选择)

    # # 删除自定义分类
    # def delete_custom_classification(self):
    #     logging.info('点击新增商品')
    #     self.click(self.新增按钮)
    #     logging.info('滑动到自定义分类界面')
    #     self.swipe(self.新增商品界面, 'up', 0, -0.8)
    #     logging.info('点击自定义分类')
    #     self.click(self.自定义分类)
    #     logging.info('向左滑动已有分类')
    #     self.swipe(self.自定义分类滑动, 'left', -0.5, 0)
    #     logging.info('点击删除')
    #     self.click(self.自定义类目删除)

    # # 规则属性新增
    # def add_rule_attribute(self, name, prop_name):
    #     self.choose_category()
    #     logging.info('点击尺码或者颜色')
    #     self.click_text(name)
    #     logging.info('点击新增属性')
    #     self.click(self.efg.read_config('规则属性新增'))
    #     logging.info('输入新增属性名称')
    #     self.type(self.efg.read_config('属性输入框'), prop_name)
    #     logging.info('点击保存')
    #     self.click(self.efg.read_config('确认选择'))
    #
    # # 判断长按的属性
    # def long_cilck_prop(self, value):
    #     array_list = self.get_elements(self.属性值组, self.属性值获取)
    #     for i in range(0, len(array_list)):
    #         if array_list[i].get_text() == value:
    #             array_list[i].long_click()
    #
    # # 选择属性规则
    # def choose_prop(self, value):
    #     array_list = self.get_elements(self.属性值组, self.属性值获取)
    #     for i in range(0, len(array_list)):
    #         if array_list[i].get_text() == value:
    #             array_list[i].click()
    #
    # # 判断属性编辑或删除
    # def edit_delete_prop(self, value):
    #     array_list = self.get_elements(self.属性值编辑删除, self.属性值编辑删除2)
    #     for i in range(0, len(array_list)):
    #         if array_list[i].get_text() == value:
    #             array_list[i].click()
    #
    # # 规则属性编辑
    # def edit_rule_attribute(self, name, prop_name, new_prop_name):
    #     self.choose_category()
    #     logging.info('点击尺码或者颜色')
    #     self.click_text(name)
    #     logging.info('点击需要编辑的属性值')
    #     self.long_cilck_prop(prop_name)
    #     logging.info('点击编辑')
    #     self.edit_delete_prop('编辑')
    #     logging.info('编辑属性名称')
    #     self.type(self.属性输入框, new_prop_name)
    #     logging.info('点击保存')
    #     self.click(self.确认选择)
    #
    # # 规则属性删除
    # def delete_rule_attribute(self, name, prop_name):
    #     self.choose_category()
    #     logging.info('点击尺码或者颜色')
    #     self.click_text(name)
    #     logging.info('点击需要编辑的属性值')
    #     self.long_cilck_prop(prop_name)
    #     logging.info('点击删除')
    #     self.edit_delete_prop('删除')
    #     logging.info('点击确认')
    #     self.click(self.弹框确认)
    #
    # # 搜索规则属性
    # def search_prop(self, prop_name, porp_value):
    #     self.choose_category()
    #     logging.info('点击尺码或者颜色')
    #     self.click_text(prop_name)
    #     logging.info('输入查询的属性值')
    #     self.click(self.搜索框)
    #     text(porp_value)
    #     time.sleep(3)
    #     dev = device()
    #     dev.yosemite_ime.code("3")
    #
    # # 搜索颜色属性
    # def search_color_prop(self, porp_value):
    #     self.search_prop(self.颜色选择, porp_value)
    #
    # # 新增颜色属性
    # def add_color_prop(self, prop_name):
    #     self.add_rule_attribute(self.颜色选择, prop_name)
    #
    # # 新增尺码属性
    # def add_size_prop(self, prop_name):
    #     self.add_rule_attribute(self.尺码选择, prop_name)
    #
    # # 编辑颜色属性
    # def edit_color_prop(self, prop_name, new_prop_name):
    #     self.edit_rule_attribute(self.颜色选择, prop_name, new_prop_name)
    #
    # # 编辑尺码属性
    # def edit_size_prop(self, prop_name, new_prop_name):
    #     self.edit_rule_attribute(self.尺码选择, prop_name, new_prop_name)
    #
    # # 删除颜色属性
    # def delete_color_prop(self, prop_name):
    #     self.delete_rule_attribute(self.颜色选择, prop_name)
    #
    # # 删除尺码属性
    # def delete_size_prop(self, prop_name):
    #     self.delete_rule_attribute(self.尺码选择, prop_name)
    #
    # # 新增颜色规则组
    # def add_color_rule_group(self, group_name):
    #     self.add_rule_group(self.颜色选择, group_name)
    #
    # # 新增尺码规则组
    # def add_size_rule_group(self, group_name):
    #     self.add_rule_group(self.尺码选择, group_name)
    #
    # # 编辑颜色规则组
    # def edit_color_rule_group(self, group_name):
    #     self.edit_rule_group(self.颜色选择, group_name)
    #
    # # 编辑颜色规则组
    # def edit_size_rule_group(self, group_name):
    #     self.edit_rule_group(self.尺码选择, group_name)
    #
    # # 删除颜色规则组
    # def delete_color_rule_group(self):
    #     self.delete_rule_group(self.颜色选择)
    #
    # # 删除尺码规则组
    # def delete_size_rule_group(self):
    #     self.delete_rule_group(self.尺码选择)

    def check_shelf_status(self, name):
        flag = self.find_element_text(name)
        if flag:
            return True
        else:
            return False

    def check_goods_is_not_exist(self, name):
        flag = self.find_element_text(name)
        if flag:
            return False
        else:
            return True

    def get_goods_names(self):
        text = self.find_element(self.efg.read_config('商品名称')).text
        return text

    def check_classification_is_exist(self, value):
        flag = self.find_element_text(value)
        if flag:
            return True
        else:
            return False
