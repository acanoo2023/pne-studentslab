seq_dna = ""

with open('dna.txt', 'r') as f:
    for line in f:
         seq_dna += line

first_line_i = seq_dna.find("\n")
seq_dna = seq_dna[first_line_i:]
seq_dna = seq_dna.replace("\n", "")


dna_dict = {}

for i in seq_dna:
    if i not in dna_dict:
        dna_dict[i] = 1
    else:
        dna_dict[i] += 1

print("Total length:", len(seq_dna))

for key, value in dna_dict.items():
    print(key + ":", value)