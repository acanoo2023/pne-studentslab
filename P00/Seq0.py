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

def seq_count_base(seq, base)
