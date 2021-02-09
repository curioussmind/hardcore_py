# DESIGNING AND USING FUNCTION
def convert_to_celsius(fahrenheit): #1
    return ((fahrenheit-32) * 5 / 9) #3

fahrenheit = int(input("Enter celcius degree: ")) #2
print("its ", convert_to_celsius(fahrenheit), " degree Celcius.") #4


