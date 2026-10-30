import socket

# Create TCP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind socket to IP address and port
server_socket.bind(("localhost", 9999))

# Listen for client connection
server_socket.listen(1)

print("TCP Mathematical Operations Server is running...")
print("Waiting for client connection...")

# Accept client connection
client_socket, client_address = server_socket.accept()

print("Client connected:", client_address)

while True:

    # Receive data from client
    data = client_socket.recv(1024)

    if not data:
        break

    message = data.decode()

    # Check for exit
    if message == "exit":
        print("Client disconnected.")
        break

    # Message format: operation|number1|number2
    operation, num1, num2 = message.split("|")

    num1 = float(num1)
    num2 = float(num2)

    # Perform mathematical operation
    if operation == "1":
        result = num1 + num2

    elif operation == "2":
        result = num1 - num2

    elif operation == "3":
        result = num1 * num2

    elif operation == "4":
        if num2 == 0:
            result = "Cannot divide by zero!"
        else:
            result = num1 / num2

    else:
        result = "Invalid operation!"

    # Send result to client
    client_socket.send(str(result).encode())

    print("Operation:", operation)
    print("Numbers:", num1, num2)
    print("Result:", result)

# Close sockets
client_socket.close()
server_socket.close()

print("Server closed.")