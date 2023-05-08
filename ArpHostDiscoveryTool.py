from scapy.all import *

eth = Ether()
arp = ARP()

eth.dst = 'ff:ff:ff:ff:ff:ff'

arp.pdst = '10.10.10.1/24'

bcPckt = eth/arp

# bcPckt.show() #paket içeriğine baktık

ans,unans = srp(bcPckt, timeout=5)
#scapy de help(sr) help(sr1) help(send) help(sendp) bilgisini oku Layer 2 sonuna p ekle

ans.summary()
print("*"*30)
unans.summary()

for snd,rcv in ans:
    #rcv.show()
    print(rcv.psrc, ':', rcv.src)