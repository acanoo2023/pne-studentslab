class Seq:
    def __init__(self, strbases="NULL"):
        self.strbases = strbases
        if self.strbases != "NULL":
            flag = 0
            for i in self.strbases:
                if i == "A" or i == "C" or i == "G" or i == "T":
                    flag += 1
            if flag == len(self.strbases):
                print("New sequence created!")
            else:
                print("INVALID sequence!")
        else:
            print("NULL sequence created")
    def __str__(self):
        output = ""
        if self.strbases != "NULL":
            flag_2 = 0
            for i in self.strbases:
                if i == "A" or i == "C" or i == "G" or i == "T":
                    flag_2 += 1
            if flag_2 == len(self.strbases):
                output = self.strbases
            else:
                output = "ERROR"
        else:
            output = "NULL"
        return output

    def len(self):
        len_0 = ""
        if self.strbases != "NULL":
            flag_3 = 0
            for i in self.strbases:
                if i == "A" or i == "C" or i == "G" or i == "T":
                    flag_3 += 1
            if flag_3 == len(self.strbases):
                len_0 = len(self.strbases)
            else:
                len_0 = 0
        else:
            len_0 = 0
        return len_0

    def count_base(self, base):
        self.base = base
        output_2 = ""

        if self.strbases != "NULL":
            flag_2 = 0
            for i in self.strbases:
                if i == "A" or i == "C" or i == "G" or i == "T":
                    flag_2 += 1
            if flag_2 == len(self.strbases):
                output_2 = self.strbases.count(base)
            else:
                output_2 = 0
        else:
            output_2 = 0

        return output_2

    def count(self):
        bases_list = ["A", "C", "T", "G"]
        d = {'A': 0, 'T': 0, 'C': 0, 'G': 0}
        output_3 = ""
        if self.strbases != "NULL":
            flag_3 = 0
            for i in self.strbases:
                if i == "A" or i == "C" or i == "G" or i == "T":
                    flag_3 += 1

            if flag_3 == len(self.strbases):
                for base in bases_list:
                    amount = self.strbases.count(base)
                    d[base] = amount
            else:
                output_3 = d
        else:
            output_3 = d

        return d

    def reverse(self):
        output_4 = ""

        if self.strbases != "NULL":
            flag_4 = 0
            for i in self.strbases:
                if i == "A" or i == "C" or i == "G" or i == "T":
                    flag_4 += 1
            if flag_4 == len(self.strbases):
                output_4 = self.strbases[::-1]
            else:
                output_4 = "ERROR"
        else:
            output_4 = "NULL"

        return output_4

    def complement(self):
        output_5 = ""

        if self.strbases != "NULL":
            flag_5 = 0
            for i in self.strbases:
                if i == "A" or i == "C" or i == "G" or i == "T":
                    flag_5 += 1
            if flag_5 == len(self.strbases):
                bases_dict = {"A": "T", "C": "G", "T": "A", "G": "C"}
                complement_seq = ""
                for i in self.strbases:
                    complement_seq += bases_dict[i]
                output_5 = complement_seq
            else:
                output_5 = "ERROR"
        else:
            output_5 = "NULL"

        return output_5

