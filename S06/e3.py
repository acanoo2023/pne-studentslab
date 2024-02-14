class Seq:
    def __init__(self, strbases):
        self.strbases = strbases

    def __str__(self):
        return self.strbases

    def len(self):
        return len(self.strbases)

    def generate_seqs(self, pattern, number):


def print_seqs(seq_list):
    for seq in seq_list:
        position = seq_list.index(seq)
        print("Sequence", str(position) + ": (Length:", str(Seq.len(seq)) + ")", seq)


seq_list = [Seq.generate_seqs("A", 1), Seq.generate_seqs("A", 2), Seq.generate_seqs("A", 3)]

print_seqs(seq_list)

"Sequence 0: (Length: 3) ACT"