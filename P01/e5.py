from Seq1 import Seq

seq_list = [Seq(), Seq("ACTGA"), Seq("Invalid sequence")]
def print_seqs(seq_list):
    for seq in seq_list:
        position = seq_list.index(seq)
        print(f"Sequence {position}: (Length: {Seq.len(seq)}) {seq}")
        print(f"  A: {Seq.count_base(seq, 'A')},  C: {Seq.count_base(seq, 'C')},  G: {Seq.count_base(seq, 'G')},  G: {Seq.count_base(seq, 'T')}")

print_seqs(seq_list)