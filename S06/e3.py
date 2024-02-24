class Seq:
    def __init__(self, strbases):
        self.strbases = strbases
        flag = 0
        for i in self.strbases:
            if i == "A" or i == "C" or i == "G" or i == "T":
                flag += 1
        if flag == len(self.strbases):
            print("New sequence created!")
        else:
            print("ERROR!!")

    def __str__(self):
        flag_2 = 0
        output = ""
        for i in self.strbases:
            if i == "A" or i == "C" or i == "G" or i == "T":
                flag_2 += 1
        if flag_2 == len(self.strbases):
            output = self.strbases
        else:
            output = "ERROR"

        return output

    def len(self):
        return len(self.strbases)

def generate_seqs(pattern, number):

    created_list = []

    for i in range(1, number + 1):
        created_list.append(Seq(pattern * i))

    return created_list

def print_seqs(seq_list):
    for seq in seq_list:
        position = seq_list.index(seq)
        print(f"Sequence {position}: (Length: {seq.len()}) {seq}")



seq_list1 = generate_seqs("A", 3)
seq_list2 = generate_seqs("AC", 5)

print("List 1:")
print_seqs(seq_list1)

print()
print("List 2:")
print_seqs(seq_list2)
