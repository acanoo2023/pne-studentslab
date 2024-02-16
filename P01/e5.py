from Seq1 import Seq

def seq_count(seq):
    bases_list = ["A", "C", "T", "G"]
    d = {'A': 0, 'T': 0, 'C': 0, 'G': 0}
    flag = 0
    for i in seq:
        if i == "A" or i == "C" or i == "G" or i == "T":
            flag += 1
    if flag == len(seq):
        for base in bases_list:
            amount = seq.count(base)
            d[base] = amount
    return d

def print_seqs(seq_list):
    for seq in seq_list:
        position = seq_list.index(seq)
        print(f"Sequence {position}: (Length: {Seq.len(seq)}) {seq}")
        print(seq_count(seq))

seq_list = [Seq(), Seq("ACTGA"), Seq("Invalid sequence")]
print_seqs(seq_list)