from pathlib import Path

# -- Constant with the name of the file to open
FILENAME = "sequences/RNU6_269P.txt"   #(To open a file, we must go from the outside to the interior)

# -- Open and read the file
file_contents = Path(FILENAME).read_text()

# -- Print the contents on the console
print(file_contents)
