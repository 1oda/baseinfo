#!/usr/bin/env python3
# coding: UTF-8

# File       : networkSpeedInfo.py
# Time       ：2021/12/29
# Author     ：tang
# version    ：python 3
import subprocess


def networkSpeedInfo():
    """网卡速率"""
    network_speed_dict = {}
    try:
        get_hostip = subprocess.getoutput("hostname -I").split()[0].strip()
        if get_hostip == '172.17.0.1':
            get_hostip = subprocess.getoutput("hostname -I").split()[1].strip()
        if get_hostip.split(".")[0].strip() not in ["172", "10", "192"]:
            get_hostip = subprocess.getoutput("hostname -I").split()[-1].strip()
        network_name = subprocess.getoutput(
            "ip a|grep {0}".format(get_hostip)).strip().split()[-1]
        network_speed = subprocess.getoutput(
            "cat /sys/class/net/{0}/speed 2>/dev/null".format(
                network_name)).strip()
    except:
        network_speed = 0
    network_speed_dict['network_speed_Mbps'] = network_speed

    return network_speed_dict


networkSpeedInfo()
