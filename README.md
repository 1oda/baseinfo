# baseinfo_metrics

linux server base metrics node_exporter


# nvidia
1二进制
`nohup bin/nvidia_gpu_prometheus_exporter --web.listen-address=:8182 &`

2容器
`docker run --privileged --net=host --itd 
mindprince/nvidia_gpu_prometheus_exporter:0.1`


# cpu
`docker run --privileged --net=host --rm 
-v /etc/sysconfig/network-scripts:/etc/sysconfig/network-scripts 
-v /etc/hosts:/etc/hosts 
-v /usr/sbin/ip:/usr/sbin/ip 
-v /usr/sbin/dmidecode:/usr/sbin/dmidecode 
-v /dev/mem:/dev/mem 
-v /usr/sbin/ethtool:/usr/sbin/ethtool 
-v /etc/redhat-release:/etc/redhat-release 
-v /etc/issue:/etc/issue 
-v /dev:/dev 
-v /sys/class/net:/sys/class/net 
xxx/prometheus_exporter/baseinfo-metrics-exporter:1.3 
python3 metrics/main.py`
