
import socket

s = socket.socket()
s.bind(("127.0.0.1", 5002))
s.listen(1)

print("Waiting for client...")
c, addr = s.accept()
print("Client connected")

msg = c.recv(1024).decode()
print("Client:", msg)

reply = input("Enter reply: ")
c.send(reply.encode())

c.close()
s.close()
