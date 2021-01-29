def convert_to_celcius(fahrenheit: float) -> float:
    """return the number of celcius degree equivalent to fahrenheit
    degrees.

    >>> convert_to_celcius(75)
    23.888888888889
    """

    return fahrenheit -32.0 * 5.0/9.0

def above_freezing(celcius: float) -> bool:
    """Return true if temperature celcius degrees is above freezing.
    >>> above freezing(5.2)
    True
    >>> above freezing(-2)
    False
    """
    return celcius > 0

if __name__ == '__main__':
    fahrenheit = float(input('Enter the fahrenheit inn degrees Fahrenheit: '))
    celcius = convert_to_celcius(fahrenheit)
    if above_freezing(celcius):
        print("It's above freezing.")
    else:
        print("It's below freezing.")