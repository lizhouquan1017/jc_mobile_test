# -*- coding:utf-8 -*-
__author__ = "lizhouquan"

import unittest
from base.BaseDevicesStart import appium_start_sync
from base.desired_caps import BaseDriver
from base.BaseAdb import AndroidDebugBridge
from base.BaseDevicesStart import start_devices
from base.BaseAppiumServer import Server
import time


devices_list = AndroidDebugBridge().attached_devices()
devices = devices_list[0]


class BaseDriverOne(unittest.TestCase):
        @classmethod
        def setUpClass(cls):
            s = Server()
            s.start_server(devices)
            d = BaseDriver()
            d.appium_desired(0)
            cls.driver =

        def setUp(self):
            self.driver.launch_app()

        def tearDown(self):
            self.driver.close_app()

        @classmethod
        def tearDownClass(cls):
            cls.driver.close_app()
            cls.driver.quit()


class BaseDriverTwo(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        time.sleep(15)
        # cls.driver = appium_desired(devices, 4725)
        # cls.driver = multiprocessing.Process(target=appium_desired, args=(devices, 4725))
        cls.driver = start_devices(devices_list[1], 4725)

    def setUp(self):
        self.driver.launch_app()

    def tearDown(self):
        self.driver.close_app()


    @classmethod
    def tearDownClass(cls):
        cls.driver.close_app()
        cls.driver.quit()
