#!/usr/bin/env python3
# coding: UTF-8

# File       : main.py
# Time       ：2021/10/15
# Author     ：tang
# version    ：python 3

from flask import Response, Flask
from werkzeug.middleware.dispatcher import DispatcherMiddleware
from prometheus_client import Gauge, generate_latest
import diskInfo, osVersion, baseInfo, networkSpeedInfo, memInfo, gpuInfo, \
    cpuInfo, getCpuMax, netDriverVersion, getDns, uuidInfo, systemInfo, \
    getBondingMode, otherInfo, ulimitOpenFiles
from prometheus_client import make_wsgi_app
import http.server
import json

app = Flask(__name__)
app.debug = True


# todo：+耗时

# class Hello(http.server.BaseHTTPRequestHandler):
# @app.route("/metrics")
def main():
    # osVersion
    try:
        os_version = osVersion.osVersion()
        os_info = Gauge('osVersion', 'version & release',
                        labelnames=os_version.keys())
        os_info.labels(**os_version).set(1)
        os_result = generate_latest(os_info)
        # print(os_result)
    except:
        os_info = Gauge('osVersion', 'version & release',
                        labelnames={'osVersion'})
        os_info.labels(None).set(-1)
        os_result = generate_latest(os_info)

    # baseInfo
    try:
        baseinfo = baseInfo.setServerInfo()
        baseinfo_info = Gauge('baseInfo', 'all baseinfo metrics',
                              labelnames=baseinfo.keys())
        baseinfo_info.labels(**baseinfo).set(1)
        baseinfo_result = generate_latest(baseinfo_info)
    except:
        baseinfo_info = Gauge('baseInfo', 'all baseinfo metrics',
                              labelnames={'baseInfo'})
        baseinfo_info.labels(None).set(-1)
        baseinfo_result = generate_latest(baseinfo_info)

    # diskInfo
    diskinfo = diskInfo.diskList()
    disk_dict = diskInfo.diskMem()
    disk_mem = Gauge('diskInfo', 'disk_mem,GB',
                     ['diskInfo'])
    try:
        for i in diskinfo:
            disk_mem.labels(i).set(disk_dict[i + '_mem_GB'])
    except:
        disk_mem.labels('disk').set(-1)
    try:
        disk_mem.labels('all_disk').set(disk_dict['all_disk_size_GB'])
    except:
        disk_mem.labels('all_disk').set(-1)
    diskmem_result = generate_latest(disk_mem)

    # networkSpeedInfo
    netspeedinfo = networkSpeedInfo.networkSpeedInfo()

    netspeed_info = Gauge('networkSpeedInfo', 'networkSpeed,Mbps',
                              ['networkSpeedInfo'])
    try:
        netspeed_info.labels('network_speed_Mbps').set(netspeedinfo[
                                                           'network_speed_Mbps'])
    except:
        netspeed_info.labels('network_speed_Mbps').set(-1)
    netspeed_result = generate_latest(netspeed_info)

    # memInfo
    meminfo = memInfo.memInfo()
    mem_info = Gauge('memInfo', 'meminfo', ['memInfo'])
    try:
        mem_info.labels('mem_everyone_size_GB').set(
            meminfo['mem_everyone_size_GB'])
    except:
        mem_info.labels('mem_everyone_size_GB').set(-1)
    try:
        mem_info.labels('mem_total_GB').set(meminfo['mem_total_GB'])
    except:
        mem_info.labels('mem_total_GB').set(-1)
    try:
        mem_info.labels('mem_all_position_num').set(
            meminfo['mem_all_position_num'])
    except:
        mem_info.labels('mem_all_position_num').set(-1)
    try:
        mem_info.labels('mem_used_position_num').set(
            meminfo['mem_used_position_num'])
    except:
        mem_info.labels('mem_used_position_num').set(-1)
    try:
        mem_info.labels('mem_max_capacity_TB').set(
            meminfo['mem_max_capacity_TB'])
    except:
        mem_info.labels('mem_max_capacity_TB').set(-1)
    mem_info_result = generate_latest(mem_info)

    # max_mem_speed_MHz
    max_mem_speed_MHz = Gauge('max_mem_speed_MHz', 'max_mem_speed_MHz',
                              ['max_mem_speed_MHz'])
    try:
        max_mem_speed_MHz.labels(meminfo['max_mem_speed_MHz']).set(1)
    except:
        max_mem_speed_MHz.labels(None).set(-1)
    max_mem_speed_MHz_result = generate_latest(max_mem_speed_MHz)

    # memType
    mem_type = Gauge('memType', 'memtype', ['memType'])
    try:
        mem_type.labels(meminfo['mem_type']).set(1)
    except:
        mem_type.labels(None).set(-1)
    mem_type_result = generate_latest(mem_type)

    mem_result = mem_info_result + max_mem_speed_MHz_result + mem_type_result

    # # gpuInfo
    # gpuinfo = gpuInfo.gpuInfo()
    # if gpuinfo['gpu_device'] == '1':
    #     gpu_info = Gauge('gpuInfo', 'gpuInfo(0=off,1=on)', ['gpuInfo'])
    #     gpu_info.labels('gpu_device').set(gpuinfo['gpu_device'])
    #     gpu_info.labels('gpu_mem_MB').set(gpuinfo['gpu_mem_MB'])
    #     gpu_info.labels('gpu_number').set(gpuinfo['gpu_number'])
    #     gpu_inf_result = generate_latest(gpu_info)
    #
    #     gpu_name = Gauge('gpuName', 'gpuName', ['gpuName'])
    #     gpu_name.labels(gpuinfo['gpu_name']).set(1)
    #     gpu_name_result = generate_latest(gpu_name)
    #
    #     gpu_driver_version = Gauge('gpuDriverVersion', 'gpuDriverVersion',
    #                                ['gpuDriverVersion'])
    #     gpu_driver_version.labels(gpuinfo['gpu_driver_version']).set(1)
    #     gpu_driver_version_result = generate_latest(gpu_driver_version)
    #
    #     gpu_result = gpu_inf_result + gpu_name_result + gpu_driver_version_result
    # else:
    #     gpu_info = Gauge('gpuInfo', 'gpuinfo(0=off,1=on)', ['gpuInfo'])
    #     gpu_info.labels('gpu_device').set(gpuinfo['gpu_device'])
    #     gpu_result = generate_latest(gpu_info)

    # cpuInfo
    cpuinfo = cpuInfo.cpuInfo()
    cpu_info = Gauge('cpuInfo', 'cpuInfo', ['cpuInfo'])
    try:
        cpu_info.labels('cpu_speed_GHz').set(cpuinfo['cpu_speed_GHz'])
    except:
        cpu_info.labels('cpu_speed_GHz').set(-1)
    try:
        cpu_info.labels('cpu_core_num').set(cpuinfo['cpu_core_num'])
    except:
        cpu_info.labels('cpu_core_num').set(-1)
    try:
        cpu_info.labels('cpu_num').set(cpuinfo['cpu_num'])
    except:
        cpu_info.labels('cpu_num').set(-1)
    try:
        cpu_info.labels('cpu_logic_num').set(cpuinfo['cpu_logic_num'])
    except:
        cpu_info.labels('cpu_logic_num').set(-1)
    cpu_info_result = generate_latest(cpu_info)

    cpu_name = Gauge('cpuName', 'cpuName', ['cpuName'])
    try:
        cpu_name.labels(cpuinfo['cpu_name']).set(1)
    except:
        cpu_name.labels(None).set(-1)
    cpu_name_result = generate_latest(cpu_name)
    cpu_result = cpu_info_result + cpu_name_result

    # getCpuMax
    getcpumaxinfo = getCpuMax.getCpuMax()
    getcpumax_info = Gauge('getCpuMax', 'getCpuMax(0=off,1=on)', ['getCpuMax'])
    try:
        getcpumax_info.labels('cpu_max').set(getcpumaxinfo['cpu_max'])
    except:
        getcpumax_info.labels('cpu_max').set(-1)
    getcpumax_result = generate_latest(getcpumax_info)

    # netDriverVersion
    netdriverversioninfo = netDriverVersion.netDriverVersion()
    try:
        netdriverversion_info = Gauge('netDriverVersion', 'driver(version) & '
                                                          'firmware-version',
                                      labelnames=netdriverversioninfo.keys())
        netdriverversion_info.labels(**netdriverversioninfo).set(1)
    except:
        netdriverversion_info = Gauge('netDriverVersion', 'driver(version) & '
                                                          'firmware-version',
                                      labelnames={'netDriverVersion'})
        netdriverversion_info.labels(None).set(-1)
    netdriverversion_result = generate_latest(netdriverversion_info)

    # getDns
    getdnsinfo = getDns.getDns()
    try:
        getdns_info = Gauge('getDns', 'get first Dns record',
                            labelnames=getdnsinfo.keys())
        getdns_info.labels(**getdnsinfo).set(1)
    except:
        getdns_info = Gauge('getDns', 'get first Dns record',
                            labelnames={'getDns'})
        getdns_info.labels(None).set(-1)
    getdns_result = generate_latest(getdns_info)

    # uuidInfo
    uuidinfo = uuidInfo.uuidInfo()
    try:
        uuid_info = Gauge('uuidInfo', 'get first uuidInfo record',
                          labelnames=uuidinfo.keys())
        uuid_info.labels(**uuidinfo).set(1)
    except:
        uuid_info = Gauge('uuidInfo', 'get first uuidInfo record',
                          labelnames={'uuidInfo'})
        uuid_info.labels(None).set(-1)
    uuidinfo_result = generate_latest(uuid_info)

    # systemInfo
    systeminfo = systemInfo.systemInfo()
    try:
        system_info = Gauge('systemInfo', 'systemInfo',
                            labelnames=systeminfo.keys())
        system_info.labels(**systeminfo).set(1)
    except:
        system_info = Gauge('systemInfo', 'systemInfo',
                            labelnames={'systemInfo'})
        system_info.labels(None).set(-1)
    systeminfo_result = generate_latest(system_info)

    # getBondingMode
    getbondingmode = getBondingMode.getBondingMode()
    getbondingmode_info = Gauge('getBondingMode',
                                'getBondingMode(mode = 0,1,2,3,4,5,6)',
                                ['getBondingMode'])
    try:
        getbondingmode_info.labels('bond_mode').set(getbondingmode['bond_mode'])
    except:
        getbondingmode_info.labels('bond_mode').set(-1)
    getbondingmode_result = generate_latest(getbondingmode_info)

    # ulimitOpenFiles
    ulimitopenfiles = ulimitOpenFiles.ulimitOpenFiles()
    ulimitopenfiles_info = Gauge('ulimitOpenFiles',
                                 'ulimitOpenFiles',
                                 ['ulimitOpenFiles'])
    try:
        ulimitopenfiles_info.labels('ulimit_open_files').set(
            ulimitopenfiles['ulimit_open_files'])
    except:
        ulimitopenfiles_info.labels('ulimit_open_files').set(-1)
    ulimitopenfiles_result = generate_latest(ulimitopenfiles_info)

    # otherInfo
    otherinfo = otherInfo.otherInfo()
    try:
        other_info = Gauge('otherInfo', 'otherInfo(kernel_version,hostname)',
                           labelnames=otherinfo.keys())
        other_info.labels(**otherinfo).set(1)
    except:
        other_info = Gauge('otherInfo', 'otherInfo(kernel_version,hostname)',
                           labelnames={'otherInfo'})
        other_info.labels(None).set(-1)
    otherinfo_result = generate_latest(other_info)
    other_result = ulimitopenfiles_result + otherinfo_result

    result = os_result + diskmem_result + \
             netspeed_result + mem_result + cpu_result + \
             getcpumax_result + netdriverversion_result + \
             getdns_result + uuidinfo_result + systeminfo_result + \
             getbondingmode_result + other_result + baseinfo_result
    return Response(result, mimetype="text/plain")


app.wsgi_app = DispatcherMiddleware(app.wsgi_app, {
    '/metrics': main()
})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port="946")
    # print("Hello World, Start Prometheus Client metrics Server!\nServer: 127.0.0.1:8000/metrics ")
    # start_http_server(8000)
    # server = http.server.HTTPServer(('0.0.0.0',8001),Hello.osVersion())
    # server.serve_forever()
