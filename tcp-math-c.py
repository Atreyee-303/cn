import socket

# Create TCP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to server
client_socket.connect(("localhost", 9999))

print("Connected to TCP Mathematical Operations Server.")

while True:

    print("\n----- MATHEMATICAL OPERATIONS -----")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    choice = input("Enter your choice: ")

    # Exit
    if choice == "5":
        client_socket.send("exit".encode())
        print("Closing client...")
        break

    # Validate choice
    if choice not in ["1", "2", "3", "4"]:
        print("Invalid choice!")
        continue

    # Input numbers
    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")

    # Create message
    message = choice + "|" + num1 + "|" + num2

    # Send request to server
    client_socket.send(message.encode())

    # Receive result
    data = client_socket.recv(1024)

    print("Result from Server:", data.decode())

# Close socket
client_socket.close()

print("Client socket closed.")