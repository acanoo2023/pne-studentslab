def information(seq_from_user):
    output = ""

    length = len(seq_from_user)
    output += "Total length: " + str(length) + "\n"

    bases_dict = {"A": 0, "C": 0, "G":0, "T":0}
    for i in ["A", "C", "G", "T"]:
        bases_dict[i] += seq_from_user.count(i)

    for i in ["A", "C", "G", "T"]:
        output += i + ": " + str(bases_dict[i]) + " (" + str(round(((bases_dict[i] * 100) / length), 2)) + "%)" + "\n"

    return output

print(information("AAACGCAGCATCAGCATCAGACTACGA"))