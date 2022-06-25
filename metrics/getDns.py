#!/usr/bin/env python3
# coding: UTF-8

# File       : getDns.py
# Time       ：2022/1/19
# Author     ：tang
# version    ：python 3
import subprocess


def getDns():
    """获取第一个DNS"""
    dns_dict = {}
    try:
        get_dns = subprocess.getoutput(
            "cat /etc/resolv.conf|grep nameserver |grep -v '#' | head -1 | awk '{print $2}'")
        dns_dict['hostdns'] = get_dns.strip()
    except:
        dns_dict['hostdns'] = 0

    return dns_dict


getDns()
