# while loops executes block of statements as long as a test at the toop keeps evaluating to a true value
# if the test is false, the body never runs and thenn

# GENERAL FORMAT
#while test:            # Loop test
#    statements         # Loop body
#else:                  # Optimal else
#    statements         # Run if didn't exit loop with break

x = 'spam'
while x:                # whule x is not empty
    print(x, end=' ')    
    x = x[1:]           # strip the first char off x
# expected output >>> spam pam am m

a = 0; b = 10
while a < b:
    print(a, end=' ')
    a += 1  # equal to a = a + 1
# expected output >>> 0 1 2 3 4 5 6 7 8 9

rabbits = 3
while rabbits > 0:
    print(rabbits)
    rabbits = rabbits - 1
# expected output 2 1

# BREAK , CONTINUE, PASS AND THE LOOP ELSE
# break --> jumps out of the closest enclosing loop (past the entire loop statement)
# continue --> jumps to the top of the closest enclosing loop (to the loop's header)
# pass --> does nothing at all: it;s an empty statement placeholder
# loop else block --> runs if and only if the loop is exited normally

# General format with break and continue statement
#while test:
#    statements
#    if test: break
#    if test: continue
#else: 
#    statements

#pass 
#while True: pass
#or 
#while True: ...

#continue
x = 10
while x:
    x = x - 1 # or x -= 1
    if x % 2 != 0: continue #if odd --> skip print
    print(x, end=' ')

x = 10
while x:
    x = x - 1
    if x % 2 == 0:
        print(x, end=' ')

# break
# causes an immediate exit from loop
while True:
    name = input('Enter name: ')
    if name == "stop": break
    age = input('Enter age: ')
    print('Hello', name, '=>', int(age) ** 2)


