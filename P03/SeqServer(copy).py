import socket
import termcolor
from Seq1 import Seq

my_sequences = ["ACACGTTACGACTACGCATCGA", "CAGTAGACGTTTGAAGTAGCCGA", "GTTACTCATCAACGACTACGACT", "TCAGTCTTCAACGTACACACGTG"]

def send_response(msg):
    msg = msg.strip()
    if msg.startswith("PING"):
        output = "OK!\n"

    elif msg.startswith("GET"):
        if msg[-1] in ['0', '1', '2', '3']:
            index = int(msg[-1])
            output = my_sequences[index] + "\n"
        else:
            output = "Choice out of range (0-3)\n"

    elif msg.startswith("INFO"):
        s1 = Seq()
        a = s1.count("A") / len(s1)
        c = s1.count("C") / len(s1)
        g = s1.count("G") / len(s1)
        t = s1.count("T") / len(s1)
        output = f"Sequence: {s1} \n Total length: {s1.len()} \n 

    return output


def print_in_server(msg):
    if msg.startswith("PING"):
        see = "PING command!"
    if msg.startswith("GET"):
        see = "GET"
    if msg.startswith("INFO"):
        see = "INFO"
    return see

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
                print(termcolor.colored(print_in_server(msg), "green"))
                print(response)

                cs.send(response.encode())

                cs.close()




server1 = SeqServer(8080, "127.0.0.1")