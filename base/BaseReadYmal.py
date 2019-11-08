# -*- coding:utf-8 -*-
__author__ = "lizhouquan"

import yaml
import os
PATH = (lambda p: os.path.abspath(os.path.join(os.path.dirname(__file__), p)))
yaml.warnings({'YAMLLoadWarning': False})

# # 获取当前文件夹脚本路径
# curPath = os.path.dirname(os.path.realpath(__file__))
#
# # 获取yaml文件路径
# yamlPath = os.path.join(PATH('../page'), 'cfgyaml.yaml')
# print(curPath)
# print(yamlPath)
#
# with open(yamlPath, 'r', encoding='utf-8') as f:
#     cfg = f.read()
#     print(cfg)
#
#     d = yaml.load(cfg)
#     print(d)


# 当前脚本路径
basepath = os.path.dirname(os.path.realpath(__file__))
# yaml文件夹
# yamlPagesPath = os.path.join(basepath, "pageelement")
yamlPagesPath = PATH('../page')

print(basepath)
print(yamlPagesPath)


def parseyaml():
    """
    遍历yaml文件
    :return:
    """
    pageElements = {}
    # 遍历读取yaml文件
    for fpath, dirname, fnames in os.walk(yamlPagesPath):
        for name in fnames:
            # yaml文件绝对路径
            yaml_file_path = os.path.join(fpath, name)
            # 排除一些非.yaml的文件
            if ".yaml" in str(yaml_file_path):
                with open(yaml_file_path, 'r', encoding='utf-8') as f:
                    page = yaml.load(f)
                    pageElements.update(page)
    return pageElements


if __name__ == "__main__":
    a = parseyaml()
    print(a)
    for i in a["LoginPage"]['locators']:
        print(i)
