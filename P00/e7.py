from Seq0 import *

seq = seq_read_fasta("sequences/U5.txt")
short_seq = seq[:20]
complement_seq = seq_complement(seq)

print("Gene U5")
print("Frag :", short_seq)
print("Comp :", complement_seq)