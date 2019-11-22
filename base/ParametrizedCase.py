# -*- coding:utf-8 -*-
__author__ = "lizhouquan"

import unittest


class ParametrizedCase(unittest.TestCase):

    def __init__(self, methodName='runTest', param=None):
        super(ParametrizedCase, self).__init__(methodName)
        self.param = param

    @staticmethod
    def parametrize(testcase_class, param=None):
        test_loader = unittest.TestLoader()
        test_names = test_loader.getTestCaseNames(testcase_class)
        suite = unittest.TestSuite()
        for name in test_names:
            suite.addTest(testcase_class(name, param=param))
        return suite
