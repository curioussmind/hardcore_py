with open('file_ex.txt', 'r') as example_file:
    lines = example_file.readlines()
print(lines)

# we use this technique when we want to get a python list 
# of strings containing indivisual lines from a file.