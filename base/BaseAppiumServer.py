import subprocess
from time import ctime
from base.BaseAdb import AndroidDebugBridge


def appium_start(host, port, devices):

    bootstrap_prot = str(port+1)

    cmd = 'start /b appium -a ' + host + ' -p ' + str(port) + ' -bp ' + str(bootstrap_prot) + ' -U ' + str(devices)

    print('%s at %s' % (cmd, ctime()))

    subprocess.Popen(cmd, shell=True, stdout=open('../appium_log/'+str(port)+'.log', 'a'), stderr=subprocess.STDOUT)


if __name__ == '__main__':

    devices = AndroidDebugBridge().attached_devices()
    host = '127.0.0.1'
    port = 4723
    for i in range(len(devices)):
        port = 4728 + 2*i
        appium_start(host, port, devices[0])
