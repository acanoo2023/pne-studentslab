from Client0 import Client
import termcolor

PORT = 8081
IP = "212.128.255.151"

c = Client(IP, PORT)
for i in range(0, 5):
    msg = "Message " + str(i)
    response = c.talk(msg)

    print("To server: " + termcolor.colored(msg, "blue"))
    print("From server: " + termcolor.colored(response, "green"))

