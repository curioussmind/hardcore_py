# USING LOCAL VARS FOR TEMP STORAGE
"""
breaking down complex computations 
into separate steps
"""

print("polynomial ax^2 + bx + c!")

def quadratic(a, b, c, x):      
    x1 = a * x ** 2 #local var  |
    x2 =  b * x     #local var  | >> can't be used outside function
    x3 = c          # local var | !function par also local var :)

    return x1 + x2 + x3

x1 = int(input("a: "))
x2 = int(input("b: ")) 
x3 = int(input("c: "))
x4 = int(input("x: "))
print(f"the result of {x1} x {x4}^2 + {x2} x {x4} + {x3} is: ", quadratic(x1, x2, x3, x4))
