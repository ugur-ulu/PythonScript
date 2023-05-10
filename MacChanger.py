import random
import subprocess
import re

charList = ["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]

a = random.choice(charList)

newMac = ""

for i in range(12):
    newMac = newMac + random.choice(charList)

#print(newMac)

ifconfigResult = subprocess.check_output("ifconfig eth0", shell=True,).decode()
print(ifconfigResult)

#oldMac = re.search("ether (.+) ", ifconfigResult).group().split(" ")[1]
oldMac = re.search("ether(.*?)txqueuelen", ifconfigResult).group(1).strip()

subprocess.check_output("ifconfig eth0 down", shell=True)
print("Calisti")
subprocess.check_output("ifconfig eth0 hw ether "+newMac, shell=True)
print("Burası Bende Çalışmıyor Buraya kadar sorun yok")
subprocess.check_output("ifconfig eth0 up" + newMac, shell=True)

print("Old Mac ", oldMac)
print("New Mac ", newMac)



