def seq_ping():
    print("Ok")



def seq_read_fasta(filename):
    from pathlib import Path

    file_contents = Path(filename).read_text()
    list_contents = file_contents.split('\n')

    seq = ""

    for i in range(1, len(list_contents)):
        seq += list_contents[i]

    return seq



def seq_len(seq):
    length = len(seq)

    return length



def seq_count_base(seq, base):
    number = seq.count(base)

    return number




def seq_count(filename):
    bases_list = ["A", "C", "T", "G"]
    d = {'A': 0, 'T': 0, 'C': 0, 'G': 0}

    seq = seq_read_fasta("sequences/" + filename + ".txt")
    for base in bases_list:
        amount = seq.count(base)
        d[base] = amount

    return d



def seq_reverse(seq, n):
    short_seq = seq[:n]
    reversed = short_seq[::-1]

    return short_seq, reversed



def seq_complement(seq):
    bases_dict = {"A": "T", "C": "G", "T": "A", "G": "C"}
    seq_20 = seq[:20]
    complement_seq = ""

    for i in seq_20:
        complement_seq += bases_dict[i]

    return seq_20, complement_seq



def get_base(seq):
    bases_dict = {}

    for i in seq:
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
