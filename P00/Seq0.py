def seq_ping():
    print("Ok")


def seq_read_fasta(filename):
    from pathlib import Path

    file_contents = Path(filename).read_text()

    list_contents = file_contents.split('\n')

    for i in range(1, len(list_contents)):
        print(list_contents[i])