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

# changing list
# keep in mind that unlike string lists are mutable, meaning we can overwrite its former value without making a new list
li = ['spam', 'Spam', 'SPAM']
li[1] = 'eggs'  # index assignment
print(li) # ['spam', 'eggs', 'SPAM']

li[0:2] = ['eat', 'more'] # slice assignment: delete + insert
print(li) # ['eat', 'more', 'SPAM!]

# list method calls
lis = ['eat', 'more', 'SPAM!']
lis.append('please') # append method call: add item at end
print(lis)
lis.sort() # sort item
print(lis)

# other common list methods
liss = [1, 2]
liss.extend([3, 4, 5]) # add many items at the end
print(liss)

liss.pop() #d delete and return the last item
liss.reverse() # In-placed reversal method

my_food = ['spam', 'eggs', 'ham']
my_food.index('eggs') # index of an object (search/find)
my_food.insert(1, 'toast') # insert at position
my_food.reverse('ham') #delete by value
my_food.pop(1) # delete by position
my_food.count('eggs') # number of occurences
del my_food[1:] # delete an entire section
