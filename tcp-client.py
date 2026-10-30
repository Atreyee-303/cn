import socket

# Create TCP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to server
client_socket.connect(("localhost", 9999))

print("Connected to TCP Chat Server.")
print("Type 'exit' to close the chat.\n")

while True:

    # Enter message
    message = input("Client: ")

    # Send message to server
    client_socket.send(message.encode())

    # Check if client wants to exit
    if message.lower() == "exit":
        break

    # Receive reply from server
    data = client_socket.recv(1024)

    if not data:
        break

    reply = data.decode()
    print("Server:", reply)

    # Check if server wants to exit
    if reply.lower() == "exit":
        break

# Close socket
client_socket.close()

print("Chat closed.")