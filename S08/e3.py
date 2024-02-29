import socket

# SERVER IP, PORT
PORT = 1234
IP = "212.128.255.90"

while True:
    # -- Ask the user for the message
    user_input = input("Enter your message")

    # -- Create the socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # -- Establish the connection to the Server
    s.connect((IP, PORT))

    # -- Send the user message
    s.send(str.encode(user_input))

    # -- Close the socket
    s.close()

