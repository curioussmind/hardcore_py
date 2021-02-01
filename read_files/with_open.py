with open('file_ex.txt', 'r') as file:
    contents = file.read()

print(contents)

# we use this methid when we want to read the contents of a file into a single string
# or when we want to specify how many characterrs to read
with open('file_ex.txt', 'r') as example_file:
    first_ten_chars = example_file.read(10)
    the_rest = example_file.read()

print("The first 10 characters:", first_ten_chars)
print("The rest of the file:", the_rest)