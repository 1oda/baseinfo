#!/usr/bin/env python3
# coding: UTF-8

# File       : netDriverVersion.py
# Time       ：2022/1/19
# Author     ：tang
# version    ：python 3
import os
import subprocess


def netDriverVersion():
    """获取真实网卡驱动版本"""
    try:
        get_hostip = subprocess.getoutput("hostname -I").split()[0].strip()
        if get_hostip == '172.17.0.1':
            get_hostip = subprocess.getoutput("hostname -I").split()[1].strip()
            if get_hostip.split(".")[0].strip() not in ["172", "10", "192"]:
                get_hostip = subprocess.getoutput("hostname -I").split()[-1].strip()
    except:
        get_hostip = '0'
    netdriver_dict = {"net_driver_version": "0", "net_firmware_version": "0",
                      "ip": get_hostip}
    try:
        ubuntu_version = subprocess.getoutput("head -1 /etc/issue |awk '{print $1}'")
    except:
        ubuntu_version = '0'
    if "Ubuntu" in ubuntu_version:
        pass
    else:
        try:
            centos_version = subprocess.getoutput("cat /etc/redhat-release |awk '{print $1}'")
        except:
            centos_version = '0'
        if "CentOS" in centos_version:
            try:
                get_ethtool_cmd = os.system("type ethtool > /dev/null 2>&1")
            except:
                get_ethtool_cmd = 1
            if get_ethtool_cmd == 0:
                get_netcard = subprocess.getoutput(
                    "ip a|grep {0}".format(get_hostip)).split()[-1].strip()
                if get_netcard == 'bond0':
                    netcard_cmd = "grep -l 'MASTER=bond0' /etc/sysconfig/network-scripts/ifcfg-* | head -1 | awk -F'-' '{print $(NF)}'"
                    get_real_netcard = subprocess.getoutput(netcard_cmd)
                    if get_real_netcard.strip() != "":
                        status, output = subprocess.getstatusoutput(
                            "ethtool -i {0}".format(get_real_netcard))
                        if status == 0:
                            get_ethtool_result = os.popen(
                                "ethtool -i {0}".format(
                                    get_real_netcard)).readlines()
                        else:
                            get_ethtool_result = os.popen(
                                "ethtool -i {0}".format(
                                    get_netcard)).readlines()
                    else:
                        get_ethtool_result = os.popen(
                            "ethtool -i {0}".format(get_netcard)).readlines()
                else:
                    get_ethtool_result = os.popen(
                        "ethtool -i {0}".format(get_netcard)).readlines()
                info_list = []
                try:
                    for info in get_ethtool_result[:3]:
                        get_info = info.split(":")[-1].strip()
                        if get_info not in info_list:
                            info_list.append(get_info)
                    netdriver_dict["net_driver_version"] = "{0}-{1}".format(
                    info_list[0], info_list[1])
                    netdriver_dict["net_firmware_version"] = info_list[2]
                    netdriver_dict["ip"] = get_hostip
                except:
                    netdriver_dict = {"net_driver_version": "0",
                                  "net_firmware_version": "0",
                      "ip": get_hostip}

            else:
                netdriver_dict = {"net_driver_version": "0",
                                  "net_firmware_version": "0",
                      "ip": get_hostip}

    return netdriver_dict

netDriverVersion()