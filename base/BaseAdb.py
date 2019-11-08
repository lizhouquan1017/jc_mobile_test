# -*- coding:utf-8 -*-
__author__ = "lizhouquan"

import subprocess
import os


class AndroidDebugBridge(object):

    def call_adb(self, command):
        """adb命令行"""
        command_result = ''
        command_text = 'adb %s' % command
        results = os.popen(command_text, "r")
        while 1:
            line = results.readline()
            if not line:
                break
            command_result += line
        results.close()
        return command_result

    # 检查设备
    def attached_devices(self):
        devices = []
        result = subprocess.Popen("adb devices", shell=True, stdout=subprocess.PIPE,
                                  stderr=subprocess.PIPE).stdout.readlines()
        for item in result:
            t = item.decode().split("\tdevice")
            if len(t) >= 2:
                devices.append(t[0])
        return devices

    # 状态
    def get_status(self):
        result = self.call_adb("get-state")
        result = result.strip('\t\n\r')
        return result or None

    # 重启
    def reboot(self, option):
        command = "reboot"
        if len(option) > 7 and option in ("bootloader", "recovery",):
            command = "%s %s" % (command, option.strip())
        self.call_adb(command)

    # 将电脑文件拷贝到手机
    def push(self, local, remote):
        result = self.call_adb("push %s %s" % (local, remote))
        return result

    # 拉数据到本地
    def pull(self, remote, local):
        resutl = self.call_adb("pull %s %s" % (remote, local))
        return resutl

    # 同步更新
    def sync(self, directory, **kwargs):
        command = "sync %s" % directory
        if 'list' in kwargs:
            command += "-l"
            result = self.call_adb(command)
            return result

    # 根据包名得到进程id
    def get_app_pid(self, pkg_name):
        string = self.call_adb("shell ps | grep " + pkg_name)
        if string == '':
            return "the process doesn't exist"
        result = string.split()
        return result[4]


# if __name__ == '__main__':
#     result1 = AndroidDebugBridge().attached_devices()
#     # result2 = AndroidDebugBridge().get_app_pid('com.gengcon.android.jxc')
#     print(result1)



