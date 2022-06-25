#!/usr/bin/env python3
# coding: UTF-8

# File       : cpuInfo.py
# Time       ：2022/1/18
# Author     ：tang
# version    ：python 3

import subprocess


def cpuInfo():
    """CPU信息及使用情况"""
    cpu_dict = {}
    # cpu_info = subprocess.getoutput("cat /proc/cpuinfo")
    try:
        cpu_name = subprocess.getoutput(
            "cat /proc/cpuinfo|grep 'model name'|head -n 1")
        cpu_dict['cpu_name'] = cpu_name.split(':')[-1].strip()
    except:
        cpu_dict['cpu_name'] = 0

    try:
        cpu_speed = subprocess.getoutput(
            "cat /proc/cpuinfo|grep 'model name' |awk '{{print $10}}' |head "
            "-n 1")
        cpu_dict['cpu_speed_GHz'] = cpu_speed.split('GHz')[0]
    except:
        cpu_dict['cpu_speed_GHz'] = 0

    try:
        cpu_core_num = subprocess.getoutput(
            "cat /proc/cpuinfo|grep 'cpu cores' |head -n 1 |awk '{{print $4}}'")
        cpu_dict['cpu_core_num'] = int(cpu_core_num)
    except:
        cpu_dict['cpu_core_num'] = 0

    try:
        cpu_num = subprocess.getoutput(
            "cat /proc/cpuinfo|grep 'physical id' |sort |uniq |wc -l")
        cpu_dict['cpu_num'] = int(cpu_num)
    except:
        cpu_dict['cpu_num'] = 0

    try:
        cpu_logic_num = subprocess.getoutput(
            "cat /proc/cpuinfo|grep -c 'processor'")
        cpu_dict['cpu_logic_num'] = int(cpu_logic_num)
    except:
        cpu_dict['cpu_logic_num'] = 0

    return cpu_dict


cpuInfo()