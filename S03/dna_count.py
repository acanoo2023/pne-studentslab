# Considerations:
#    You must use a loop for counting the bases.
#    Suppose that the user always introduce correct sequences (you do not have to manage errors yet).


user_seq = input("Enter your sequence: ")
dna_dict = {}

for i in user_seq:
    if i not in dna_dict:
        dna_dict[i] = 1
    else:
        dna_dict[i] += 1

print("Total length:", len(user_seq))

for key, value in dna_dict.items():
    print(key + ":", value)


