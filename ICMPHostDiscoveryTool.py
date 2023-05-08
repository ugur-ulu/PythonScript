from scapy.all import *

ip = IP()
icmp = ICMP()

pingPckt = ip/icmp #birleştirme yaptık

addr = '192.168.1.'

ipList = []

for i in range(256):
    pingPckt[IP].dst = addr+str(i)
    #print(pingPckt)
    response = sr1(pingPckt, timeout=0.5, verbose=False )
    #print(response)
    if(response):
        #print(pingPckt[IP].dst, 'is up')
        ipList.append(pingPckt[IP].dst)
    else:
        pass

print(ipList)