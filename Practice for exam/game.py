import socket
import termcolor
import random

class NumberGuesser:
    def __init__(self, correct_number, msg_from_client, attempt):
        self.correct_number = correct_number
        self.msg_from_client = msg_from_client
        self.attempt = attempt

    def guess(self):
        output = ""
        if int(self.msg_from_client) < int(self.correct_number):
            output = "Higher"
        elif int(self.msg_from_client) > int(self.correct_number):
            output = "Lower"
        elif int(self.msg_from_client) == int(self.correct_number):
            output = f"You won after {self.attempt} attempts"

        return output






PORT = 8080
IP = "127.0.0.1"

ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

ls.bind((IP, PORT))

ls.listen()

print("The server is configured!")
number = random.randint(1, 100)
print("THE CORRECT NUMBER IS " + str(number))


client_counter = 1

while True:

    try:
        (cs, client_ip_port) = ls.accept()

    except KeyboardInterrupt:     # -- Server stopped manually by the user:
        print("\nServer stopped by the user")
        ls.close()
        exit()

    else:    # -- If the user doesn't close the program --> Execute this part
        msg_raw = cs.recv(2048)
        msg = msg_raw.decode()

        print(f"\tMessage received: " + termcolor.colored(msg, "green"))

        object = NumberGuesser(number, msg, client_counter)
        clue = object.guess()

        response = str(clue) + "\n"

        cs.send(response.encode())

        cs.close()

        client_counter += 1