#!/usr/bin/env python3
# coding: UTF-8

# File       : getBondingMode.py
# Time       ：2022/1/19
# Author     ：tang
# version    ：python 3
import os
import subprocess


def getBondingMode():
    """获取bond0网卡bonding模式
       mode = 0,1,2,3,4,5,6
       未配置返回空
    """
    bonding_mode = {"bond_mode": ""}
    net_conf = '/etc/sysconfig/network-scripts/ifcfg-bond0'
    if os.path.exists(net_conf):
        try:
            output = subprocess.getoutput("grep '^BONDING_OPTS.*mode' {}".format(
                net_conf))
            mode = output.split("mode=")[-1].split()[0].strip("\"").strip()
        except:
            mode = "-1"
        if mode.isdigit():
            bonding_mode["bond_mode"] = mode
        else:
            bonding_mode["bond_mode"] = '-1'

    return bonding_mode


getBondingMode()
