# HOW TO DESIGN A BEAUTIFUL FUNCTION
"""
we can use the following questions before designing function
1. name of the function --> must reflect the function
2. the paramters and information they refer to
3. the calc we will do with that information
4. what info does the funtion return
5. does it work as we expect?
"""

def days_difference(day1: int, day2: int) -> int:
    """Return the number of days between day1 and day2, which are 
    both in the range 1 - 365 (thus indicating the day of the year).
    >>> days_difference(200, 224)
    ... 24
    >>> days difference(50, 50)
    ... 0
    """
    return day2 - day1

day_1 = int(input("Enter the number for day 1: "))
day_2 = int(input("Enter the number for day 2: "))
print(f"The difference is: {days_difference(day_1, day_2)} days.")