# -*- coding:utf-8 -*-
__author__ = "lizhouquan"

from base.BaseCheckPort import Port
from base.BaseAppiumServer import Server
from base.desired_caps import appium_desired
from base.BaseAdb import AndroidDebugBridge
import multiprocessing
from time import sleep
from tomorrow import threads


devices_list = AndroidDebugBridge().attached_devices()
num = len(devices_list)


def start_appium_server(host, port, devices):
    if check_port(host, port):
        appium_start(host, port, devices)
        return True
    else:
        release_port(port)
        return False


@threads(num)
def start_devices(udid, port):
    try:
        driver = appium_desired(udid, port)
        return driver
    except Exception:
        release_port(port)


def appium_start_sync():
    print("=====并发启动appium服务=====")
    appium_process = []
    # 加载appium进程
    for i in range(len(devices_list)):
        host = '127.0.0.1'
        port = 4723+2*i
        devices = devices_list[i]
        appium = multiprocessing.Process(target=start_appium_server, args=(host, port, devices))
        appium_process.append(appium)
    for appium in appium_process:
            appium.start()
    for appium in appium_process:
            appium.join()
    sleep(10)


def devices_start_sync():

    q = multiprocessing.Queue()
    print("=====并发启动设备=====")
    desired_process = []
    # 加载desired进程
    for i in range(len(devices_list)):
        port = 4723+2*i  # 第一个端口号是4723，第二个是4725
        desired = multiprocessing.Process(target=start_devices, args=(devices_list[i], port))
        desired_process.append(desired)
    # 同时启动多设备执行测试
    for desired in desired_process:
        desired.start()
    for desired in desired_process:
        desired.join()


if __name__ == '__main__':
    appium_start_sync()
    for i in range(len(devices_list)):
        result = start_devices(devices_list[i], 4723 + i*2)
        print(result)







