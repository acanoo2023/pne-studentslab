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
    elif msg.startswith("INFO"):
        print("INFO")
        output = info_response(msg)
    elif msg.startswith("COMP"):
        print("COMP")
        output = info_complement(msg)
    elif msg.startswith("REV"):
        print("REV")
        output = info_reverse(msg)
    elif msg.startswith("GENE"):
        print("GENE")
        output = info_gene(msg)


    else:
        print("Invalid Command\n")
        output = "Invalid Command\n"
    return output

def ping_response():
    print("OK!\n")
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

def info_response(msg):
    new_msg = msg.replace("INFO", "").strip()

    s1 = Seq(new_msg)

    a = "A: " + str(s1.count_base("A")) + " (" + str(round(s1.count_base("A") * 100 / s1.len(), 2)) + "%)"
    c = "C: " + str(s1.count_base("C")) + " (" + str(round(s1.count_base("C") * 100 / s1.len(), 2)) + "%)"
    g = "G: " + str(s1.count_base("G")) + " (" + str(round(s1.count_base("G") * 100 / s1.len(), 2)) + "%)"
    t = "T: " + str(s1.count_base("T")) + " (" + str(round(s1.count_base("T") * 100 / s1.len(), 2)) + "%)"

    l = ["A", "C", "G", "T"]
    print("Sequence:", s1)
    print("Total length:", s1.len())
    for i in l:
        print(f"{i}: {s1.count_base(i)} ({round(s1.count_base(i) * 100 / s1.len(),2)}%)")

    print("\n")
    output = f"Sequence: {s1} \n Total length: {s1.len()} \n {a} \n {c} \n {g} \n {t} \n"

    return output


def info_complement(msg):
    new_msg = msg.replace("COMP", "").strip()

    s1 = Seq(new_msg)

    print(s1.complement() + "\n")

    return s1.complement() + "\n"

def info_reverse(msg):
    new_msg = msg.replace("REV", "").strip()

    s1 = Seq(new_msg)

    print(s1.reverse() + "\n")

    return s1.reverse() + "\n"


def info_gene(msg):
    file = msg.replace("GENE", "").strip()

    s1 = Seq()
    direction = "../P01/sequences/" + file + ".txt"
    print(s1.read_fasta(direction) + "\n")

    return s1.read_fasta(direction) + "\n"





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