from scapy.all import *

def sniffPckt(pkt):
    pkt.show()
def startSniff():
    scapySniff = sniff(prn = sniffPckt, timeout=5, iface='eth0', stop_filter=lambda x:x.haslayer(ICMP))
    wrpcap('btkakademi.pcap', scapySniff)

def startRead():
    scapycap = rdpcap('btkakademi.pcap')

    ipList = []

    for pckt in scapycap:
        if IP in pckt:
            if pckt[IP].src not in ipList:
                ipList.append(pckt[IP].src)
        else:
            pckt.show()
    print(ipList)


print("1 Sniff", "2 Start")

choice = input(">>>")

if(choice=='1'):
    startSniff()
elif(choice=='2'):
    startRead()
else:
    print("Bir şey seçmedin gardaş")

#Kod çalışıyor denedim.