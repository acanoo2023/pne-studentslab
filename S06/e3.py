class Seq:
    def __init__(self, strbases):
        self.strbases = strbases
        print("New sequence created!")

    def __str__(self):
        return self.strbases

    def len(self):
        return len(self.strbases)

    def generate_seqs(self, pattern, number):
        self.pattern = pattern
        self.number = number

        empty_list = []

        for i in range(number):
            seq_to_add = ""
            seq_to_add += (i * pattern)
            empty_list.append(seq_to_add)

        return empty_list

def print_seqs(seq_list):
    for seq in seq_list:
        position = seq_list.index(seq)
        print("Sequence", str(position) + ": (Length:", str(Seq.len(seq)) + ")", seq)



seq_obj = Seq("")
seq_list1 = seq_obj.generate_seqs("A", 3)
seq_list2 = seq_obj.generate_seqs("AC", 5)

print("List 1:")
print_seqs(seq_list1)

print()
print("List 2:")
print_seqs(seq_list2)
