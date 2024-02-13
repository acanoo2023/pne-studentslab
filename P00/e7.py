from Seq02 import *

seq = seq_read_fasta("sequences/U5.txt")

seq_20, complement_seq = seq_complement(seq)

print("Gene U5")
print("Frag :", seq_20)
print("Comp :", complement_seq)