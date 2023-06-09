import socket

ip = '192.168.1.105'
#port = 80

for port in range(1,65535):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(2.0)
        s.connect((ip, port))
        response = s.recv(1024)
        print(str(port), "Open: Banner", ":", response.decode())
    except socket.timeout as t:
        if(port==80):
            httpMessage  = 'GET / HTTP/1.0\r\n\r\n'
            s.send(httpMessage.encode())
            httpRcv = s.recv(1024)
            print(str(port), "Open: Banner", ":", httpRcv.decode())
        else:
            print(str(port), "Time out: ", str(t))
    except Exception as e:
        print(str(port), "Port Close: Reason: ", str(e ))
        pass
    finally:
        s.close()
