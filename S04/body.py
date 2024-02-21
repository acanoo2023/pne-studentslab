from pathlib import Path

# -- Constant with the name of the file to open
FILENAME = "sequences/U5.txt"

# -- Open and read the file
file_contents = Path(FILENAME).read_text()

list_contents = file_contents.split('\n')

# -- Print header on the console
for i in range(1, len(list_contents)):
    print(list_contents[i])


seq_complete = ""
for i in range(1, len(list_contents)):
    seq_complete += list_contents[i]

print(seq_complete)

