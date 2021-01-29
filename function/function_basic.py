
def convert_to_celcius(fahrenheit):
    return(fahrenheit -  32) * 5 / 9

fahrenheit = input('Enter the degree: ')
print('The temperature is:', convert_to_celcius(int(fahrenheit)), 'degree Celcius.')
