# -*- coding: utf-8 -*-
__author__ = "lizhouquan"


import configparser
import os


class ReadIni:
    """
    @note: 读取配置文件ini的类，可以配置文件，默认文件为config.ini
    @isPageView:是否为页面元素配置文件，@file_name:文件名称
    """

    def __init__(self, is_pageview=True, file_name=None):
        base_dir = os.path.dirname(os.path.dirname(__file__))
        default_cfg = 'config.ini'
        if file_name is None and is_pageview is False:
            file_path = os.path.join(base_dir + r'/config/' + default_cfg)
        elif is_pageview is False and file_name is not None:
            file_path = os.path.join(base_dir + r'/page/' + file_name)
        else:
            file_path = os.path.join(base_dir + r'/page/' + file_name)

        self.cfg = configparser.ConfigParser()
        self.cfg.read(file_path)

    def read_config(self, para1, para2="value"):
        """
        @para1: 配置文件模块
        @para2: 配置文件子模块
        @return:data 子模块内容
        """
        data = self.cfg.get(para1, para2)
        return data


if __name__ == '__main__':
    config = ReadIni(file_name='config.ini')
    a = config.read_config('用户名输入框')
    print(a)
