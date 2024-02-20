from Seq1 import Seq

seq_list = [Seq(), Seq("ACTGA"), Seq("Invalid sequence")]
def print_seqs(seq_list):
    for seq in seq_list:
        position = seq_list.index(seq)
        print(f"Sequence {position}: (Length: {Seq.len(seq)}) {seq}")
        print(f"  Bases: {Seq.count(seq)}")
        print(f"  Rev: {Seq.reverse(seq)}")
print_seqs(seq_list)