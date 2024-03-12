from Client0 import Client
import termcolor

PORT = 8080
IP = "127.0.0.1"

c = Client(IP, PORT)
for i in range(0, 5):
    msg = "Message " + str(i)
    response = c.talk(msg)

    print("To server: " + termcolor.colored(msg, "blue"))
    print("From server: " + termcolor.colored(response, "green"))

