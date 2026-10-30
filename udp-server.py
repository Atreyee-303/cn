import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(("127.0.0.1", 8080))

print("Server is ready")

data, addr = s.recvfrom(1024)
text = data.decode()

print("Received:", text)

rev = text[::-1]
s.sendto(rev.encode(), addr)

s.close()



