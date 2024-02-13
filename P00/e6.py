from Seq0 import *

seq = seq_read_fasta("sequences/U5.txt")
short_seq = seq[:20]
reversed_seq = seq_reverse(seq, 20)

print("Gene U5")
print("Fragment: ", short_seq)
print("Reverse: ", reversed_seq)