#!/usr/bin/env python3
# coding: UTF-8

# File       : gpuInfo.py
# Time       ：2022/1/18
# Author     ：tang
# version    ：python 3

import subprocess

def gpuInfo():
    """GPU信息及使用情况"""
    gpu_dict = {}
    gpu_driver_num = subprocess.getoutput("ls /dev|grep -c nvidia")
    status, output = subprocess.getstatusoutput("nvidia-smi")
    if gpu_driver_num != '0' and status == 0:
        gpu_dict['gpu_device'] = '1'
        try:
            gpu_name = subprocess.getoutput(
                "nvidia-smi -q |grep 'Product Name' |awk '{print $4,$5}' |head -n 1")
            if gpu_name == "Graphics Device":
                gpu_dict['gpu_name'] = "Tesla P4"
            else:
                gpu_dict['gpu_name'] = gpu_name
        except:
            gpu_dict['gpu_name'] = 0

        try:
            gpu_mem_size = subprocess.getoutput(
                "nvidia-smi -q |grep Total |grep MiB |head -n 1 |awk '{print $3}'")
            gpu_mem = gpu_mem_size
            gpu_dict['gpu_mem_MB'] = gpu_mem
        except:
            gpu_dict['gpu_mem'] = 0

        try:
            gpu_number = subprocess.getoutput("nvidia-smi -L | wc -l")
            gpu_dict['gpu_number'] = gpu_number
        except:
            gpu_dict['gpu_number'] = 0

        try:
            gpu_driver_version = subprocess.getoutput(
                "nvidia-smi -q |grep 'Driver Version' |awk '{print $4}'")
            gpu_dict['gpu_driver_version'] = gpu_driver_version
        except:
            gpu_dict['gpu_driver_version'] = 0
    else:
        gpu_dict['gpu_device'] = 0

    return gpu_dict

gpuInfo()