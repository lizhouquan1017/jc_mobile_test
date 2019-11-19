# -*- coding:utf-8 -*-
__author__ = "lizhouquan"

import os
import socket


class Port(object):

    def check_port(self, host="127.0.0.1", port=None):
        try:
            connect_skt = socket.socket()
            connect_skt.connect((host, port))
            return False
        except EnvironmentError:
            return True

    def release_port(self, port):
        cmd_find = "netstat -ano |findstr %s" % port

        result = os.popen(cmd_find).read()
        print(result)

        if str(port) and 'LISTENING' in result:
            i = result.index('LISTENING')
            start = i + len('LISTENING') + 7
            end = result.index('\n')
            pid = result[start:end]

            cmd_kill = "taskkill -f -pid %s" % pid
            print(cmd_kill)
            os.popen(cmd_kill)

    def check_port_used(self, port):
        """
        判断接口是否被占用
        :param port:
        :return:
        """
        flag = None
        cmd_find = "netstat -ano |findstr %s" % port
        result = os.popen(cmd_find).read()
        print(result)
        if len(result) > 0:
            flag = True
        else:
            flag = False
        return flag

    def creat_port_list(self, start_port, devices_list):
        """
        start_port 从 4723 开始
        :param start_port:    存储可用port
        :param devices_list:  设备list
        :return:
        """
        port_list = []
        if devices_list is not None:
            while len(port_list) != len(devices_list):
                if self.check_port_used(start_port) is False:
                    port_list.append(start_port)
                start_port = start_port + 2
            return port_list
        else:
            print('生成可用端口失败')
            return None


if __name__ == '__main__':
    # devices_list = AndroidDebugBridge().attached_devices()
    p = Port()
    # post_list = p.creat_port_list(4723, devices_list)
    # print(post_list)
    p.release_port(4700)
    p.release_port(4702)
