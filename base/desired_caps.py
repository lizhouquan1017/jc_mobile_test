# coding:utf-8
from appium import webdriver
import yaml
import logging.config
import os
from time import ctime
PATH = (lambda p: os.path.abspath(os.path.join(os.path.dirname(__file__), p)))
yaml.warnings({'YAMLLoadWarning': False})
log_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../config/log.conf')
logging.config.fileConfig(log_file_path)
logger = logging.getLogger()


def appium_desired(udid, port):
        with open('../config/devices.yaml', 'r', encoding='utf-8') as file:
            data = yaml.load(file)
            desired_caps = {}
            desired_caps['platformName'] = data['platformName']
            desired_caps['platformVersion'] = data['platformVersion']
            # desired_caps['deviceName'] = data['deviceName']
            desired_caps['deviceName'] = udid
            desired_caps['app'] = PATH('../app/jxc.apk')
            desired_caps['udid'] = udid
            desired_caps['appPackage'] = data['appPackage']
            desired_caps['appActivity'] = data['appActivity']
            desired_caps['noReset'] = data['noReset']
            desired_caps['unicodeKeyboard'] = data['unicodeKeyboard']
            desired_caps['resetKeyboard'] = data['resetKeyboard']
            desired_caps['automationName'] = data['automationName']
            desired_caps['systemPort'] = port+8000
            print('appium port:%s start run %s at %s' % (port, udid, ctime()))
            driver = webdriver.Remote('http://' + str(data['ip']) + ':' + str(port) + '/wd/hub', desired_caps)
        return driver
