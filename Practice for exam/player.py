from Client0 import Client
import termcolor

PORT = 8080
IP = "127.0.0.1"

c = Client(IP, PORT)

msg1 = input("Please enter your number between 1 and 100: ")
response1 = c.talk(msg1)
print(response1)


if not response1.startswith("You won"):
    while True:
        msg2 = input("Please enter your number between 1 and 100: ")
        response = c.talk(msg2)
        print(response)
        if response.startswith("You won"):
            break



