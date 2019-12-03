# coding = utf-8

import configparser
from os import path


parent_path = path.dirname(path.dirname(__file__))
file1_path = path.join(parent_path, r"data\test_data\data1.ini")
file2_path = path.join(parent_path, r"data\test_data\data2.ini")


class ReadData(object):
    """ 读取cfg.ini文件，返回各个参数值构成的字典"""
    def __init__(self, param):
        self.param = param
        self.cof = configparser.ConfigParser()
        if param == 0:
            self.cof.read(file1_path, encoding='utf-8')
        else:
            self.cof.read(file2_path, encoding='utf-8')

    """data.ini文件写入/修改操作"""
    def write_data(self, section, key, value):
        if self.param == 0:
            self.cof.set(section, key, value)
            with open(file1_path, "w") as f:
                self.cof.write(f)
        else:
            self.cof.set(section, key, value)
            with open(file2_path, "w") as f:
                self.cof.write(f)

    """读取data.ini文件的数据"""
    def get_data(self, section, key):
        data = self.cof.get(section, key)
        return data
