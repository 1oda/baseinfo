#!/usr/bin/env python3
# coding: UTF-8

# File       : systemInfo.py
# Time       ：2022/1/19
# Author     ：tang
# version    ：python 3
import subprocess


def systemInfo():
    """系统信息"""
    system_dict = {}
    system_info = subprocess.getoutput("dmidecode -t system 2>/dev/null")
    try:
        serial_number = subprocess.getoutput(
            "echo '{0}'|grep 'Serial Number' |awk '{{print $3}}'".format(
                system_info))
        system_dict['serial_number'] = serial_number.split()[0].strip()
    except:
        system_dict['serial_number'] = 0

    try:
        manufacturer = subprocess.getoutput(
            "echo '{0}'|grep Manufacturer |awk '{{print $2}}'".format(
                system_info))
        system_dict['manufacturer'] = manufacturer.split()[0].strip()
    except:
        system_dict['manufacturer'] = 0

    try:
        product_name = subprocess.getoutput(
            "echo '{0}'|grep 'Product Name'".format(system_info))
        system_dict['product_name'] = product_name.split(':')[-1].strip()
    except:
        system_dict['product_name'] = 0

    return system_dict


systemInfo()
