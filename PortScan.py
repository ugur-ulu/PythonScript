import socket

ip = '192.168.1.105'
#port = 80

for port in range(1,65535):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip, port))
        print(str(port), "Port Open")
    except Exception as e:
        print(str(port), "Port Close")
    finally:
        s.close()
