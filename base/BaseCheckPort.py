# -*- coding:utf-8 -*-
__author__ = "lizhouquan"

import os
import socket


def check_port(host,port):
    try:
        connect_skt = socket.socket()
        connect_skt.connect((host, port))
        return False
    except EnvironmentError:
        return True


def release_port(port):
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


if __name__ == '__main__':
    host = '127.0.0.1'
    release_port(4723)
    release_port(4725)
