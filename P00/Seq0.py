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

def seq_len(filename):
    seq = seq_read_fasta("sequences/" + filename + ".txt")
    print("Gene", filename, "-> Length:", len(seq))

def seq_count_base(filename, base):
    seq = seq_read_fasta("sequences/" + filename + ".txt")
    print(" ", base + ":", seq.count(base))

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