import socket

# Create TCP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind socket to IP address and port
server_socket.bind(("localhost", 9999))

# Listen for client connection
server_socket.listen(1)

print("TCP Chat Server is running...")
print("Waiting for client connection...")

# Accept client connection
client_socket, client_address = server_socket.accept()

print("Client connected:", client_address)
print("Type 'exit' to close the chat.\n")

while True:

    # Receive message from client
    data = client_socket.recv(1024)

    if not data:
        break

    message = data.decode()
    print("Client:", message)

    # Check if client wants to exit
    if message.lower() == "exit":
        print("Client ended the chat.")
        break

    # Enter reply
    reply = input("Server: ")

    # Send reply to client
    client_socket.send(reply.encode())

    # Check if server wants to exit
    if reply.lower() == "exit":
        break

# Close sockets
client_socket.close()
server_socket.close()

print("Chat closed.")