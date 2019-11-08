# coding = utf-8
# coding:gbk
import unittest
import time
import sys
sys.path.append('..')
from BeautifulReport import BeautifulReport
from base.BaseCheckPort import release_port


time.sleep(3)
path = "D:\\python_workspace\\jc_moblie_test\\"
sys.path.append(path)

release_port(4723)
release_port(4725)
report_dir = r'D:\python_workspace\jc_moblie_test\reports'
test_dir = '../production_environment_case'
discover = unittest.defaultTestLoader.discover(test_dir, pattern='test*.py')


now = time.strftime('%Y-%m-%d %H_%M_%S')
report_name = 'jxcreport.html'
BeautifulReport(discover).report(filename=report_name, description='进销存Android端测试环境测试报告', report_dir=report_dir)
