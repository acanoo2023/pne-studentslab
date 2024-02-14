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


s1 = Seq("ACCTGC")
s2 = Seq("Hello? Am I a valid sequence?")
print(f"Sequence 1: {s1}")
print(f"Sequence 2: {s2}")
