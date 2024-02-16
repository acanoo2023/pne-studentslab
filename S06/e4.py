import termcolor

class Seq:
    def __init__(self, strbases):
        self.strbases = strbases
        print("New sequence created!")

    def __str__(self):
        return self.strbases

    def len(self):
        return len(self.strbases)



def print_seqs(seq_list, color):
    for seq in seq_list:
        position = seq_list.index(seq)
        termcolor.cprint(f"Sequence {position}: (Length: {Seq.len(seq)}) {seq}", color)
def generate_seqs(pattern, number):

    empty_list = []

    for i in range(1, number + 1):
        empty_list.append(Seq(pattern * i))

    return empty_list


seq_list1 = generate_seqs("A", 3)
seq_list2 = generate_seqs("AC", 5)

print("List 1:")
print_seqs(seq_list1, "blue")

print()
print("List 2:")
print_seqs(seq_list2, "green")
