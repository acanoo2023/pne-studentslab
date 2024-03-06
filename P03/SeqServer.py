import socket
import termcolor

class SeqServer:
    PORT = 8080
    IP = "127.0.0.1"
    def __init__(self, PORT, IP):
        self.PORT = PORT
        self.IP = IP

        ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        ls.bind((self.IP, self.PORT))

        ls.listen()

        print("SEQ Server Configured!")

        while True:
            print("\nWaiting for Clients to connect...")

            try:
                (cs, client_ip_port) = ls.accept()

            except KeyboardInterrupt:  # -- Server stopped manually by the user:
                print("\nServer stopped by the user")
                ls.close()
                exit()

            else:  # -- If the user doesn't close the program --> Execute this part

                msg_raw = cs.recv(2048)
                msg = msg_raw.decode()

                response = ""

                if msg.startswith("PING"):
                    response = send_response(msg)
                    print(termcolor.colored("PING Command", "green"))

                cs.send(response.encode())

                cs.close()

def send_response(msg):
    if msg


server1 = SeqServer(8080, "127.0.0.1")