from Seq02 import *
u5_seq = seq_read_fasta("sequences/U5.txt")

seq_with_20_char = ""

for i in range(0, 20):
    seq_with_20_char += u5_seq[i]

print("DNA file: U5.txt")
print("The first 20 bases are:")
print(seq_with_20_char)