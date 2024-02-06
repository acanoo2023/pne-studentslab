from pathlib import Path

# -- Constant with the name of the file to open
FILENAME = "sequences/RNU6_269P.txt"

# -- Open and read the file
file_contents = Path(FILENAME).read_text()

list_contents = file_contents.split('\n')

# -- Print header on the console
print(list_contents[0])