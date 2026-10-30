
import socket

s = socket.socket()
s.connect(("127.0.0.1", 5002))

msg = input("Enter message: ")
s.send(msg.encode())

reply = s.recv(1024).decode()
print("Server:", reply)

s.close()


