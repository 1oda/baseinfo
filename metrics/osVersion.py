#!/usr/bin/env python3
# coding: UTF-8

# File       : os.py
# Time       ：2021/10/14
# Author     ：tang
# version    ：python 3


import subprocess


def osVersion():
    """Linux系统版本"""
    os_version_dict = {}
    check_linux = subprocess.getoutput("head -1 /etc/issue")
    if "Ubuntu" in check_linux:
        os_result = 'Ubuntu'
        os_version = subprocess.getoutput(
            "cat /etc/issue |grep Ubuntu |awk '{print $2}'")
    else:
        os_result = subprocess.getoutput("cat /etc/redhat-release |awk '{"
                                         "print $1}'")
        if os_result == 'CentOS':
            os_version = subprocess.getoutput("cat /etc/redhat-release "
                                              "|awk '{print $4}'")
        else:
            os_version = 0
    os_version_dict['os'] = os_result
    os_version_dict['version'] = os_version

    return os_version_dict


osVersion()
