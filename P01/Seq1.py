class Seq:
    def __init__(self, strbases = None):
        if strbases != None:
            flag = 0
            for i in strbases:
                if i == "A" or i == "C" or i == "G" or i == "T":
                    flag += 1

            if flag == len(strbases):
                print("New sequence created!")
                self.strbases = strbases
            else:
                print("INVALID sequence!")
                self.strbases = "INVALID"
        else:
            print("NULL sequence created")
            self.strbases = "NULL"


    def __str__(self):
        output = ""
        if self.strbases != "NULL":
            if self.strbases == "INVALID":
                output = "ERROR"
            else:
                output = self.strbases
        else:
            output = "NULL"

        return output

    def len(self):
        len_0 = ""
        if self.strbases == "NULL" or self.strbases == "INVALID":
            len_0 = 0
        else:
            len_0 = len(self.strbases)

        return len_0

    def count_base(self, base):
        self.base = base
        output_2 = 0
        if self.strbases == "NULL" or self.strbases == "INVALID":
            output_2 = 0
        else:
            output_2 = self.strbases.count(base)

        return output_2

    def count(self):
        bases_list = ["A", "C", "T", "G"]
        d = {'A': 0, 'T': 0, 'C': 0, 'G': 0}
        output_3 = ""
        if self.strbases == "NULL" or self.strbases == "INVALID":
            output_3 = d
        else:
            for base in bases_list:
                amount = self.strbases.count(base)
                d[base] = amount
                output_3 = d

        return output_3

    def reverse(self):
        output_4 = ""
        if self.strbases == "NULL":
            output_4 = "NULL"
        elif self.strbases == "INVALID":
            output_4 = "ERROR"
        else:
            output_4 = self.strbases[::-1]

        return output_4



    def complement(self):
        output_5 = ""

        if self.strbases == "NULL":
            output_5 = "NULL"
        elif self.strbases == "INVALID":
            output_5 = "ERROR"
        else:
            bases_dict = {"A": "T", "C": "G", "T": "A", "G": "C"}
            complement_seq = ""
            for i in self.strbases:
                complement_seq += bases_dict[i]
            output_5 = complement_seq

        return output_5


    def read_fasta(self, filename):

        from pathlib import Path

        file_contents = Path(filename).read_text()
        first_line = file_contents.find('\n')
        new_sequence = file_contents[first_line:]
        self.strbases = new_sequence.replace("\n", "")

        return self.strbases


    def most_frequent(self):
        bases_dict = {}

        for i in self.strbases:
            if i not in bases_dict:
                bases_dict[i] = 1
            else:
                bases_dict[i] += 1

        base = ""

        max_count = 0
        for i in bases_dict:
            if bases_dict[i] > max_count:
                max_count = bases_dict[i]
                base = i

        return base
