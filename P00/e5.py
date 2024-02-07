from Seq0 import *

filename_list = ["U5", "ADA", "FRAT1", "FXN", ]

for file in filename_list:
    bases_dict = seq_count(file)
    print("GENE", file + ":", bases_dict)


