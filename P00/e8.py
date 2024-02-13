from Seq02 import *

seq_U5 = seq_read_fasta("sequences/U5.txt")
seq_ADA = seq_read_fasta("sequences/ADA.txt")
seq_FRAT1 = seq_read_fasta("sequences/FRAT1.txt")
seq_FXN = seq_read_fasta("sequences/FXN.txt")

print("Gene U5: Most frequent Base:", get_base(seq_U5))
print("Gene ADA: Most frequent Base:", get_base(seq_ADA))
print("Gene FRAT1: Most frequent Base:", get_base(seq_FRAT1))
print("Gene FXN: Most frequent Base:", get_base(seq_FXN))
