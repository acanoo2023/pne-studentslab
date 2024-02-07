from Seq0 import *

filename_list = ["U5", "ADA", "FRAT1", "FXN", ]
bases_list = ["A", "C", "T", "G"]

for file in filename_list:
    print("GENE", file + ":")
    for base in bases_list:
        seq_count_base(file, base)
    print(" ")