from Seq1 import Seq
from Client0 import Client

PRACTICE = 2
EXERCISE = 4

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

IP = "127.0.0.1"
PORT = 8080

filename_list = ["U5", "FRAT1", "ADA"]

c = Client(IP, PORT)
print(c)

s1 = Seq()


for file in filename_list:
    print(f"To server: Sending {file} Gene to the server..." )
    response_to_msg = c.talk(f"Sending {file} Gene to the server...")
    print("From server: ")
    print(response_to_msg + "\n")

    direction = "../P01/sequences/" + file + ".txt"
    print("To server:", s1.read_fasta(direction))
    response_to_seq = c.talk(s1.read_fasta(direction))
    print("From server: ")
    print(response_to_seq + "\n")


