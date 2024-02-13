from Seq02 import *

seq = seq_read_fasta("sequences/U5.txt")
original, reversed_seq = seq_reverse(seq, 20)

print("Gene U5")
print("Fragment: ", original)
print("Reverse: ", reversed_seq)