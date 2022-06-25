#!/usr/bin/env python3
# coding: UTF-8

# File       : getCpuMax.py
# Time       ：2022/1/18
# Author     ：tang
# version    ：python 3
import os
import re
import subprocess


def getCpuMax():
    """检测CPU性能最大化
       0=未开启
       1=已开启
    """
    cpu_max_dict = {}
    get_cpu_info = subprocess.getoutput(
        "ls /sys/devices/system/cpu | grep 'cpu[0-9]?*'")
    cpu_list = get_cpu_info.strip().split()
    for i in cpu_list:
        file_path = '/sys/devices/system/cpu/%s/cpufreq/scaling_governor' % i
        if os.path.exists(file_path):
            get_cpu_stat = subprocess.getoutput('cat %s' % file_path)
            if get_cpu_stat != 'performance':
                cpu_max_dict["cpu_max"] = 0
                break
            else:
                cpu_max_dict["cpu_max"] = 1
                break
        else:
            cpu_num = int(re.findall(r'(\d+)', i.strip())[0]) + 1
            get_cpu_MHz = subprocess.getoutput(
                "cat /proc/cpuinfo | grep MHz| head -%s | awk '{{print $NF}}'" % cpu_num)

            get_cpu_speed = subprocess.getoutput(
                "cat /proc/cpuinfo |grep 'model name' | head -1 | awk '{print $NF}'")

            try:
                cpu_clock_speed = float(
                    re.findall(r'(\d+.\d+)', get_cpu_speed.strip())[0]) * 1000
                if float(get_cpu_MHz) / float(cpu_clock_speed) > 0.95:
                    cpu_max_dict["cpu_max"] = 1
                    break
            except:
                cpu_max_dict["cpu_max"] = 0
                break
    else:
        cpu_max_dict["cpu_max"] = 0

    return cpu_max_dict


getCpuMax()
