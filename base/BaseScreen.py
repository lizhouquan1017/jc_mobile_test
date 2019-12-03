# -*- coding:utf-8 -*-
__author__ = "lizhouquan"


class Screen(object):

    def __init__(self, driver):
        self.driver = driver

    def __call__(self, func):
        def inner(*args, **kwargs):
            try:
                func(*args, **kwargs)
            except:
                import time
                nowtime = time.strftime("%Y_%m_%d_%H_%M_%S")
                self.driver.get_screenshot_as_file("%s.png" % nowtime)
                raise
        return inner
