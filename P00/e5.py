from Seq02 import *

filename_list = ["U5", "ADA", "FRAT1", "FXN"]

for file in filename_list:
    seq = seq_read_fasta("sequences/" + file + ".txt")
    bases_dict = seq_count(seq)
    print("GENE", file + ":", bases_dict)




