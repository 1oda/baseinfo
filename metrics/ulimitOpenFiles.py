#!/usr/bin/env python3
# coding: UTF-8

# File       : ulimitOpenFiles.py
# Time       ：2022/1/19
# Author     ：tang
# version    ：python 3
import subprocess


def ulimitOpenFiles():
    """其他补充信息"""

    ulimit_open_files = {}

    try:
        ulimit = subprocess.getoutput("ulimit -n")
        ulimit_open_files['ulimit_open_files'] = ulimit.strip()
    except:
        ulimit_open_files['ulimit_open_files'] = 0

    return ulimit_open_files


ulimitOpenFiles()
