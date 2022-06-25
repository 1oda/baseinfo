#!/usr/bin/env python3
# coding: UTF-8

# File       : otherInfo.py
# Time       ：2022/1/19
# Author     ：tang
# version    ：python 3
import subprocess


def otherInfo():
    """其他补充信息"""
    other_info = {}
    try:
        kernel_version = subprocess.getoutput(
            "cat /proc/version |awk '{print $3}'")
        other_info['kernel_version'] = kernel_version.strip()
    except:
        other_info['kernel_version'] = 0

    try:
        hostname = subprocess.getoutput("hostname")
        other_info['hostname'] = hostname.strip()
    except:
        other_info['hostname'] = 0

    return other_info


otherInfo()
