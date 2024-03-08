from Seq1 import Seq
from Client0 import Client

PRACTICE = 2
EXERCISE = 6

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

IP = "127.0.0.1"
PORT_1 = 8080
PORT_2 = 8081

c1 = Client(IP, PORT_1)
c2 = Client(IP, PORT_2)
print(c1)
print(c2)

s1 = Seq()
FRAT1_gen = s1.read_fasta("../P01/sequences/FRAT1.txt")
print("Gene FRAT 1:", FRAT1_gen)

fragments = []
i = 0
while i < len(FRAT1_gen):
    fragment = FRAT1_gen[i:i + 10]
    fragments.append(fragment)
    i += 10


sending_msg_1 = c1.talk("Sending FRAT1 Gene to the server, in fragments of 10 bases...")
sending_msg_2 = c2.talk("Sending FRAT1 Gene to the server, in fragments of 10 bases...")


for i in range(0,10):
    msg_send = f"Fragment {str(i + 1)}: {fragments[i]}"
    print(msg_send)
    if (i + 1) % 2 == 0:
        to_server = c2.talk(msg_send)
    else:
        to_server = c1.talk(msg_send)
