# list comprehensions are a way to build a new list by applying an expression
# to each item in a sequence and are close relatives to for loops

res = [c * 4 for c in 'SPAM'] #list comprehensions
print(res)

# list comprehensions above == for loop below
ok = []
for c in 'SPAM':
    ok.append(c * 4)
print(ok)

# lists are sequences so we can operate the same with what we can do with string
L = ['spam', 'Spam', 'SPAM!']
print(L[2]) # print index 2 from list
print(L[-2]) # print index no.2 from the end 
print(L[1:]) # slicing fetches section

# nested list 
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matrix[1]) # [4, 5, 6]
print(matrix[1][1]) # 5
print(matrix[2][0])
print(matrix)
