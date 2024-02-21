from Seq1 import Seq
print("-----| Practice 1, Exercise 10 |------")

genes = ["U5", "ADA", "FRAT1", "FXN", "RNU6_269P"]

for gene in genes:
    filename = "sequences/" + gene + ".txt"
    s = Seq()
    s.read_fasta(filename)
    print("Gene ", gene, ": Most frequent Base:", s.most_frequent())

