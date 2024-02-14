class Seq:
    def __init__(self, strbases):
        self.strbases = strbases

    def __str__(self):
        return self.strbases

    def len(self):
        return len(self.strbases)


def print_seqs(seq_list):
    for seq in seq_list:
        position = seq_list.index(seq)
        print("Sequence", str(position) + ": (Length:", str(Seq.len(seq)) + ")", seq)


seq_list = [Seq("ACT"), Seq("GATA"), Seq("CAGATA")]

print_seqs(seq_list)