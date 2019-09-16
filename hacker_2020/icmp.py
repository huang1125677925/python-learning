import sys
from scapy.all import sr1,IP,ICMP

p=sr1(IP(dst='10.100.100.84')/ICMP())
if p:
    p.show()