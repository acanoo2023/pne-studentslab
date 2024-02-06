from pathlib import Path

# -- Constant with the name of the file to open
FILENAME = "sequences/ADA.txt"

# -- Open and read the file
file_contents = Path(FILENAME).read_text()

list_contents = file_contents.split('\n')
list_contents.pop(0) # remove header


print(len(''.join(list_contents)))



# ANOTHER WAY with easier code:

index = file_contents.find('\n')
file_contents = (file_contents[index:]).replace('\n', '')
print(len(file_contents))
