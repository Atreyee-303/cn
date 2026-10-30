# UDP Server Program

import socket

# Create UDP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind socket to IP address and port
server_socket.bind(("localhost", 9999))

print("UDP Server is running...")
print("Waiting for client request...")

while True:

    # Receive data from client
    data, client_address = server_socket.recvfrom(1024)

    message = data.decode()

    # Message format: choice|string
    choice, text = message.split("|", 1)

    if choice == "1":
        # Convert to lowercase
        result = text.lower()

    elif choice == "2":
        # Reverse the string
        result = text[::-1]

    else:
        result = "Invalid choice!"

    # Send result back to client
    server_socket.sendto(result.encode(), client_address)

    print("Client:", text)
    print("Result:", result)

server_socket.close()