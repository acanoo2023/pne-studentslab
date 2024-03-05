import socket

# SERVER IP, PORT
PORT = 5362
IP = "192.168.0.39"

flag = True
while flag:
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
    flag = False


