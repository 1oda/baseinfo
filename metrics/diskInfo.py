#!/usr/bin/env python3
# coding: UTF-8
# File       : disk.py
# Time       ：2021/10/15
# Author     ：tang
# version    ：python 3

import subprocess


def diskList():
    """块名称"""
    disk_list = []
    get_partitions = subprocess.getoutput("ls /sys/block/")
    partition_list = get_partitions.strip().split()
    try:
        for i in partition_list:
            disk_list.append(i)
    except:
        disk_list = []
    return disk_list

def diskInfo():
    """块名称"""
    disk_info = {}
    block_name = {}

    get_partitions = subprocess.getoutput("ls /sys/block/")
    partition_list = get_partitions.strip().split()
    try:
        for i in partition_list:
            block_name['block_name_' + i] = i
            disk_info.update(block_name)
    except:
        disk_info["block_name"] = 0

    return disk_info


def diskMem():
    """磁盘使用"""
    disk_dict = {}
    disk_size_sum = 0
    get_partitions = subprocess.getoutput("ls /sys/block/")
    partition_list = get_partitions.strip().split()
    try:
        for partition in partition_list:
            get_disk_size = subprocess.getoutput("cat /sys/block/%s/size" %
                                                 partition)
            disk_size_value = int(get_disk_size) * 512 / 1000 / 1000 / 1000
            # disk_size = '{0}GB'.format(disk_size_value)
            disk_size = disk_size_value
            disk_dict[partition + '_mem_GB'] = disk_size
            disk_size_sum += disk_size_value
    # disk_dict['all_disk_size'] = '{0}GB'.format(disk_size_sum)
        disk_dict['all_disk_size_GB'] = disk_size_sum
    except:
        disk_dict["size_GB"] = 0

    return disk_dict


diskList()
diskInfo()
diskMem()
