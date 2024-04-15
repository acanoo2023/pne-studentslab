import socket

PORT = 8080
IP = "127.0.0.1"

flag = True
while flag:
    user_input = input("Enter your message")

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((IP, PORT))
    s.send(str.encode(user_input))
    s.close()
    flag = False