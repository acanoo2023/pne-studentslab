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
