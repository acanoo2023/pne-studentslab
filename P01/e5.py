from Seq1 import Seq

seq_list = [Seq(), Seq("ACTGA"), Seq("Invalid sequence")]
def print_seqs(seq_list):
    for seq in seq_list:
        position = seq_list.index(seq)
        print(f"Sequence {position}: (Length: {seq.len()}) {seq}")
        print(f"  A: {seq.count_base('A')},  C: {seq.count_base('C')},  G: {seq.count_base('G')},  T: {seq.count_base('T')}")

print_seqs(seq_list)