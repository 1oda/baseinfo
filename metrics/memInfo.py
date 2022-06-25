#!/usr/bin/env python3
# coding: UTF-8

# File       : memInfo.py
# Time       ：2022/1/13
# Author     ：tang
# version    ：python 3

import subprocess


def memInfo():
    """内存信息及使用情况"""

    def MBToGB(size):
        if 'GB' in size:
            return size.replace(' GB', '')
        elif 'MB' in size:
            try:
                size_value = size.split(' MB')[0]
                size_value_gb = int(size_value) / 1024
            except:
                size_value_gb = 0
            return float(size_value_gb)
        else:
            size_value_gb = 0
            return size_value_gb

    mem_dict = {}

    try:
        get_mem_size = subprocess.getoutput(
            "dmidecode -t Memory 2>/dev/null|grep Size |grep -v 'No Module Installed'|head -n 1")
        mem_size = get_mem_size.strip().split(':')[-1].strip()
        mem_everyone_size = MBToGB(mem_size)
        mem_dict['mem_everyone_size_GB'] = mem_everyone_size
    except:
        mem_dict['mem_everyone_size'] = 0

    try:
        mem_all_position_num = subprocess.getoutput(
            "dmidecode -t Memory 2>/dev/null|grep Size |wc -l")
    except:
        mem_all_position_num = 0

    try:
        mem_used_position_num = subprocess.getoutput(
            "dmidecode -t Memory 2>/dev/null|grep Size |grep -v 'No Module Installed'|wc -l")
    except:
        mem_used_position_num = 0

    try:
        mem_total = int(mem_everyone_size) * int(mem_used_position_num)
    except:
        mem_total = 0

    mem_dict['mem_total_GB'] = mem_total
    mem_dict['mem_all_position_num'] = mem_all_position_num
    mem_dict['mem_used_position_num'] = mem_used_position_num

    try:
        mem_max_capacity = subprocess.getoutput(
            "dmidecode 2>/dev/null|grep 'Maximum Capacity'|head -1 |awk '{print $3,$4}'")
        mem_dict['mem_max_capacity_TB'] = mem_max_capacity.split(' ')[0]
    except:
        mem_dict['mem_max_capacity'] = 0

    try:
        mem_speed = subprocess.getoutput(
            "dmidecode 2>/dev/null|grep Speed |awk '{{print $2,$3}}' |head -n 1").split(
            ':')[1].strip(' ')
        mem_dict['max_mem_speed_MHz'] = mem_speed
    except:
        mem_dict['mem_speed'] = 0

    try:
        mem_type = subprocess.getoutput(
            "dmidecode 2>/dev/null|grep Type: |grep -v Unknown|grep -v Error|head -n 1")
        mem_dict['mem_type'] = mem_type.split(':')[-1].strip()
    except:
        mem_dict['mem_type'] = 0

    return mem_dict


memInfo()
