from Seq02 import *

filename_list = ["U5", "ADA", "FRAT1", "FXN"]
bases_list = ["A", "C", "T", "G"]

for file in filename_list:
    seq = seq_read_fasta("sequences/" + file + ".txt")
    print("GENE", file + ":")
    for base in bases_list:
        number = seq_count_base(seq, base)
        print(" ", base + ":", number)
    print(" ")