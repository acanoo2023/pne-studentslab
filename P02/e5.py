from Seq1 import Seq
from Client0 import Client

PRACTICE = 2
EXERCISE = 5

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

IP = "127.0.0.1"
PORT = 8080

c = Client(IP, PORT)
print(c)

s1 = Seq()
FRAT1_gen = s1.read_fasta("../P01/sequences/FRAT1.txt")
print("Gene FRAT 1:", FRAT1_gen)

fragments = []
i = 0
while i < len(FRAT1_gen):
    fragment = FRAT1_gen[i:i + 10]
    fragments.append(fragment)
    i += 10

sending_msg = c.talk("Sending FRAT1 Gene to the server, in fragments of 10 bases...")

for i in range(0,5):
    msg_send = f"Fragment {str(i + 1)}: {fragments[i]}"
    print(msg_send)
    to_server = c.talk(msg_send)