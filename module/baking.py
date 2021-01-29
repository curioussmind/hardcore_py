import temperature

def get_preheating_instructions(fahrenheit: float) -> str:
    """ Return instructions for preheating the oven in fahrenheit degrees and Celcius degrees.

    >>> get_preheating_instructions(500)
    'preheat oven to 500 degrees F (260.0 degrees c).'
    """

    cels = str(temperature.convert_to_celcius(fahrenheit))
    fahr = str(fahrenheit)
    return 'Preheat oven to ' + fahr + ' degrees F ('+ cels +' degrees C).'

fahr = float(input('Enter the baking temperature in degrees Fahrenheit: '))
print(get_preheating_instructions(fahr))