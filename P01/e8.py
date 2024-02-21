from Seq1 import Seq

seq_list = [Seq(), Seq("ACTGA"), Seq("Invalid sequence")]
def print_seqs(seq_list):
    for seq in seq_list:
        position = seq_list.index(seq)
        print(f"Sequence {position}: (Length: {seq.len()}) {seq}")
        print(f"  Bases: {seq.count()}")
        print(f"  Rev: {seq.reverse()}")
        print(f"  Comp: {seq.complement()}")
print_seqs(seq_list)