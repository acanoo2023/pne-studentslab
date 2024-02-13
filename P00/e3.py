from Seq02 import *

filename_list = ["U5", "ADA", "FRAT1", "FXN"]

for i in filename_list:
    seq = seq_read_fasta("sequences/" + str(i) + ".txt")

    print("Gene", i, "-> Length:", seq_len(seq))
