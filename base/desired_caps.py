# coding:utf-8
from appium import webdriver
import yaml
import logging.config
import os
from time import ctime
from base.BaseReadYaml import ReadYaml
PATH = (lambda p: os.path.abspath(os.path.join(os.path.dirname(__file__), p)))
yaml.warnings({'YAMLLoadWarning': False})
log_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../config/log.conf')
logging.config.fileConfig(log_file_path)
logger = logging.getLogger()


class BaseDriver:
    def appium_desired(self, i):
            with open('../config/device.yaml', 'r', encoding='utf-8') as file:
                data = yaml.load(file)
                ry = ReadYaml()
                devices = ry.get_value('user_info_'+str(i), 'deviceName')
                port = ry.get_value('user_info_' + str(i), 'port')
                desired_caps = {}
                desired_caps['platformName'] = "Android"
                desired_caps['platformVersion'] = "9"
                # desired_caps['deviceName'] = data['deviceName']
                desired_caps['deviceName'] = devices
                desired_caps['app'] = PATH('../app/jxc.apk')
                # desired_caps['udid'] = udid
                desired_caps['appPackage'] = "com.gengcon.android.jxc"
                desired_caps['appActivity'] = "com.gengcon.android.jxc.login.SplashActivity"
                desired_caps['noReset'] = "True"
                # desired_caps['unicodeKeyboard'] = data['unicodeKeyboard']
                # desired_caps['resetKeyboard'] = data['resetKeyboard']
                desired_caps['automationName'] = "uiautomator2"
                desired_caps['systemPort'] = port+8000
                driver = webdriver.Remote('http://127.0.0.1' + ':' + str(port) + '/wd/hub', desired_caps)
            return driver


if __name__ == '__main__':
    b = BaseDriver()
    driver = b.appium_desired(0)
    driver.find_element_by_id('com.gengcon.android.jxc:id/phone_num_edit_text').send_keys('15927169432')
