import socket
import termcolor
from Seq1 import Seq

my_sequences = ["ACACGTTACGACTACGCATCGA", "CAGTAGACGTTTGAAGTAGCCGA", "GTTACTCATCAACGACTACGACT", "TCAGTCTTCAACGTACACACGTG"]

def send_response(msg):
    msg = msg.strip()

    if msg.startswith("PING"):
        print("PING Command!")
        output = ping_response()
    elif msg.startswith("GET"):
        print("GET")
        output = get_response(msg)


    else:
        print("Invalid Command\n")
        output = "Invalid Command\n"
    return output

def ping_response():
    return "OK!\n"

def get_response(msg):
    sq = ""
    if msg[-1] in ['0', '1', '2', '3']:
        index = int(msg[-1])
        sq = my_sequences[index] + "\n"
        print(sq)
    else:
        print("Choice out of range (0-3)\n")
        sq = "Choice out of range (0-3)\n"

    return sq












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
            print("Waiting for Clients to connect...")

            try:
                (cs, client_ip_port) = ls.accept()

            except KeyboardInterrupt:  # -- Server stopped manually by the user:
                print("\nServer stopped by the user")
                ls.close()
                exit()

            else:  # -- If the user doesn't close the program --> Execute this part

                msg_raw = cs.recv(2048)
                msg = msg_raw.decode()

                response = send_response(msg)

                cs.send(response.encode())

                cs.close()




server1 = SeqServer(8080, "127.0.0.1")