import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

text = input("Enter a string: ")

s.sendto(text.encode(), ("127.0.0.1", 8080))

data, addr = s.recvfrom(1024)

print("Reversed string:", data.decode())

s.close()


