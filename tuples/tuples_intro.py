T = () # empty tuple
T = (1, 2, 'tiga', 4.0, 5) # tuple with five items
print(T[0], T[1:3]) # indexing & slicing

x = (40) # an integer
y = (40,) # a tuple containing an integer
print(x, y)

# in tuples we can omit the parenthesis but when we need the parenthesis and we we don't?
# parenthesis matter -- within a function call, or nested in a larger expr
# commas matter--embedded in the literal of a larger data structure like a list or dict

# conversions, methods, and immutability
# Note: the operations in tuples are simmilar to list and string

Tu = ('cc', 'aa', 'dd', 'bb') # initialized a tupple
tmp = list(Tu)      # make a list from a tuple's item
tmp.sort()          # sort the list
print(tmp)

print(sorted(Tu))   # use the sorted built-in and save two steps and we directly convert the tupple into a list

# list comprehensions can also be used to convert tuple
T = (1, 2, 3, 4, 5,)
L = (x + 20 for x in T)
for x in L:
    print(x)

# index and count
Tup = (1, 2, 3, 2, 4, 2)
print(Tup.index(2)) # offset of first appearance of 2
print(Tup.index(2, 2)) # offset of appearance after offset 2
print(Tup.count(2)) # hiw many 2s are there

# the rule about tupple immutability applies only to the top level of the tuple itself
T = (1, [2, 3], 4)
# T[1] = 'spam' # raised error
 # the list inside the tuple can be changed as usual
T[1][0] = 'spam'
print(T)  # --> (1, ['spam', 3], 4)

# Why we need tuples when we have list?
# its immutability serve a role as a constant declarations
bob = ('Bob', 40.5, ['dev', 'mgr'])     # tuple record
print(bob)
print(bob[0], bob[2])       # access by position

