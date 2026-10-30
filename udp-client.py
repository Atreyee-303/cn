# UDP Client Program

import socket

# Create UDP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = ("localhost", 9999)

while True:

    print("\n----- UDP STRING OPERATIONS -----")
    print("1. Convert to Lowercase")
    print("2. Reverse String")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "3":
        print("Closing client...")
        break

    if choice not in ["1", "2"]:
        print("Invalid choice!")
        continue

    text = input("Enter a string: ")

    # Combine choice and string
    message = choice + "|" + text

    # Send request to server
    client_socket.sendto(message.encode(), server_address)

    # Receive result from server
    data, _ = client_socket.recvfrom(1024)

    print("Result from Server:", data.decode())

client_socket.close()
print("Client Socket Closed.")