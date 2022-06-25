#!/usr/bin/env python3
# coding: UTF-8

# File       : uuidInfo.py
# Time       ：2022/1/19
# Author     ：tang
# version    ：python 3


import subprocess


def uuidInfo():
    """系统UUID"""
    uuid_dict = {}
    try:
        uuid_info = subprocess.getoutput(
            "dmidecode -t 1 |grep UUID |awk '{ print $2}'|head -1")
    except:
        uuid_info = 0
    uuid_dict['uuid'] = uuid_info

    return uuid_dict


uuidInfo()
