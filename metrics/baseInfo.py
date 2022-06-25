#!/usr/bin/env python3
# coding: UTF-8

# File       : base_info.py
# Time       ：2021/10/25
# Author     ：tang
# version    ：python 3

import diskInfo, osVersion, networkSpeedInfo, memInfo, gpuInfo, cpuInfo, getCpuMax, netDriverVersion, getDns, uuidInfo, systemInfo, getBondingMode, otherInfo, ulimitOpenFiles

server_info = {}
server_info['BASE_VERSION'] = 'base-v3,by yuetang2'


def setServerInfo():
    # osVersion
    osversion = osVersion.osVersion()
    server_info.update(osversion)

    # diskInfo
    diskinfo = diskInfo.diskInfo()
    server_info.update(diskinfo)

    diskmem = diskInfo.diskMem()
    server_info.update(diskmem)

    disklist = diskInfo.diskMem()
    server_info.update(disklist)

    # networkSpeedInfo
    network_speed = networkSpeedInfo.networkSpeedInfo()
    server_info.update(network_speed)

    # memInfo
    mem_info = memInfo.memInfo()
    server_info.update(mem_info)

    # # gpuInfo
    # gpuinfo = gpuInfo.gpuInfo()
    # server_info.update(gpuinfo)

    # cpuInfo
    cpuinfo = cpuInfo.cpuInfo()
    server_info.update(cpuinfo)

    # getCpuMax
    getcpumax = getCpuMax.getCpuMax()
    server_info.update(getcpumax)

    # netDriverVersion
    netdriverversion = netDriverVersion.netDriverVersion()
    server_info.update(netdriverversion)

    # getDns
    getdns = getDns.getDns()
    server_info.update(getdns)

    # uuidInfo
    uuidinfo = uuidInfo.uuidInfo()
    server_info.update(uuidinfo)

    # systemInfo
    systeminfo = systemInfo.systemInfo()
    server_info.update(systeminfo)

    # getBondingMode
    getbondingmode = getBondingMode.getBondingMode()
    server_info.update(getbondingmode)

    # ulimitOpenFiles
    ulimitopenfiles = ulimitOpenFiles.ulimitOpenFiles()
    server_info.update(ulimitopenfiles)

    # otherInfo
    otherinfo = otherInfo.otherInfo()
    server_info.update(otherinfo)

    return server_info


setServerInfo()
