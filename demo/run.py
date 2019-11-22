# -*- coding:utf-8 -*-
__author__ = "lizhouquan"

import threading
import os
import unittest
from base.BaseAdb import AndroidDebugBridge
from base.ParametrizedCase import ParametrizedCase
from production_environment_case.pre_release_product_case import ProdcutEnviromentTest
from base import HTMLTestRunnerSimple
from base.BaseReadYaml import ReadYaml
from base.BaseAppiumServer import Server
from time import sleep
from base import opreate_file

base_path = os.path.dirname(os.path.dirname(__file__))
ReadYaml().clear_data()


def get_suite_for_report(i):
    try:
        deviceslist = AndroidDebugBridge().attached_devices()
        suite = unittest.TestSuite()
        ###############需添加的测试套#################
        # suite.addTest(ParametrizedTestCase.parametrize(Test01AddAsset, param=i))
        suite.addTest(ParametrizedCase.parametrize(ProdcutEnviromentTest, param=i))
        ##############################################
        report_title = "进销存·APP自动化测试报告"
        descip = '设备ID：' + deviceslist[i]
        html_file = base_path + '/reports/report_No' + str(i + 1) + '_' + deviceslist[i] + '.html'
        with open(html_file, 'wb') as fp:
            run = HTMLTestRunnerSimple.HTMLTestRunner(stream=fp, title=report_title, verbosity=2, description=descip,
                                                      retry=None, save_last_try=True)
            run.run(suite)
        # if i == len(deviceslist)-1:
        #     Server().kill_server()
        #     sleep(5)
    except Exception as e:
        raise


def Run_All():
    try:
        deviceslist = AndroidDebugBridge().attached_devices()
        opreate_file.remove_file("../reports")
        Server().kill_server()
        sleep(5)
        opreate_file.remove_file("../appium_log")
        sleep(3)
        Server().start_server(deviceslist)
        threads = []
        for i in range(len(deviceslist)):
            t = threading.Thread(target=get_suite_for_report, args=(i,))
            threads.append(t)
        for th in threads:
            th.start()
    except Exception as e:
        raise


# 执行多线程运行测试
if __name__ == '__main__':
    Run_All()
